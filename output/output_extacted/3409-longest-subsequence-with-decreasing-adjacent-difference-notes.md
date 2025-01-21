## Longest Subsequence with Decreasing Adjacent Difference

**Problem Link:** https://leetcode.com/problems/longest-subsequence-with-decreasing-adjacent-difference/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: `2 <= nums.length <= 10^5`, `0 <= nums[i] <= 10^9`.
- Expected output format: The length of the longest subsequence with decreasing adjacent difference.
- Key requirements and edge cases to consider: The subsequence must have decreasing adjacent differences, i.e., `nums[i] - nums[i - 1] > nums[i + 1] - nums[i]`.
- Example test cases with explanations:
  - Input: `nums = [5, 3, 4, 8, 6, 7]`
    - Output: `3`
    - Explanation: The longest subsequence with decreasing adjacent difference is `[5, 3, 4]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subsequences and check each one for the decreasing adjacent difference property.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsequences of the input array `nums`.
  2. For each subsequence, iterate through the elements and check if the adjacent differences are decreasing.
  3. Keep track of the longest subsequence that satisfies the condition.
- Why this approach comes to mind first: It's a straightforward and intuitive approach that checks all possible solutions.

```cpp
#include <iostream>
#include <vector>

int longestSubsequence(std::vector<int>& nums) {
    int n = nums.size();
    int max_length = 0;

    for (int mask = 0; mask < (1 << n); mask++) {
        std::vector<int> subsequence;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                subsequence.push_back(nums[i]);
            }
        }

        if (subsequence.size() < 2) {
            continue;
        }

        bool is_valid = true;
        for (int i = 1; i < subsequence.size() - 1; i++) {
            if (subsequence[i] - subsequence[i - 1] <= subsequence[i + 1] - subsequence[i]) {
                is_valid = false;
                break;
            }
        }

        if (is_valid) {
            max_length = std::max(max_length, (int)subsequence.size());
        }
    }

    return max_length;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input array. This is because we generate all possible subsequences ($2^n$) and iterate through each one ($n$).
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we store each subsequence in memory.
> - **Why these complexities occur:** The brute force approach has exponential time complexity because it generates all possible subsequences, and linear space complexity because we store each subsequence in memory.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use dynamic programming to store the length of the longest subsequence ending at each position.
- Detailed breakdown of the approach:
  1. Initialize a dynamic programming table `dp` of size `n`, where `dp[i]` represents the length of the longest subsequence ending at position `i`.
  2. Iterate through the input array and update the `dp` table based on the decreasing adjacent difference property.
  3. Keep track of the maximum value in the `dp` table, which represents the length of the longest subsequence with decreasing adjacent difference.
- Proof of optimality: The dynamic programming approach has a time complexity of $O(n^2)$, which is optimal because we need to iterate through the input array and compare each pair of elements.

```cpp
#include <iostream>
#include <vector>

int longestSubsequence(std::vector<int>& nums) {
    int n = nums.size();
    std::vector<int> dp(n, 1);

    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (nums[i] - nums[j] > 0) {
                dp[i] = std::max(dp[i], dp[j] + 1);
            }
        }
    }

    int max_length = 0;
    for (int i = 0; i < n; i++) {
        max_length = std::max(max_length, dp[i]);
    }

    return max_length;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input array. This is because we iterate through the input array and compare each pair of elements.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we store the `dp` table in memory.
> - **Optimality proof:** The dynamic programming approach has a time complexity of $O(n^2)$, which is optimal because we need to iterate through the input array and compare each pair of elements.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, decreasing adjacent difference property.
- Problem-solving patterns identified: Using dynamic programming to store the length of the longest subsequence ending at each position.
- Optimization techniques learned: Using a dynamic programming table to avoid redundant calculations.
- Similar problems to practice: Longest increasing subsequence, longest decreasing subsequence.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the dynamic programming table correctly, not updating the table correctly.
- Edge cases to watch for: Empty input array, single-element input array.
- Performance pitfalls: Using a brute force approach with exponential time complexity.
- Testing considerations: Testing with different input sizes, testing with different input values.