## Subsequence of Size K with the Largest Even Sum

**Problem Link:** https://leetcode.com/problems/subsequence-of-size-k-with-the-largest-even-sum/description

**Problem Statement:**
- Input format: You are given an array `nums` of integers and an integer `k`.
- Constraints: `1 <= k <= nums.length <= 1000`, `1 <= nums[i] <= 1000`.
- Expected output format: The largest even sum of a subsequence of size `k`.
- Key requirements and edge cases to consider: Ensure the subsequence sum is even, and all elements are distinct.
- Example test cases with explanations:
  - For `nums = [2,1,2]` and `k = 2`, the largest even sum is `4` (subsequence `[2,2]`).
  - For `nums = [1,2]` and `k = 2`, the largest even sum is `3` (subsequence `[1,2]`).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subsequences of size `k` and calculate their sums.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsequences of `nums` with size `k`.
  2. For each subsequence, calculate the sum of its elements.
  3. Check if the sum is even. If it is, update the maximum even sum found so far.
- Why this approach comes to mind first: It's straightforward to generate all subsequences and check their sums.

```cpp
#include <vector>
#include <algorithm>

void generateSubsequences(std::vector<int>& nums, std::vector<int>& current, int k, int start, int& maxEvenSum) {
    if (current.size() == k) {
        int sum = 0;
        for (int num : current) sum += num;
        if (sum % 2 == 0) maxEvenSum = std::max(maxEvenSum, sum);
        return;
    }
    for (int i = start; i < nums.size(); ++i) {
        current.push_back(nums[i]);
        generateSubsequences(nums, current, k, i + 1, maxEvenSum);
        current.pop_back();
    }
}

int largestEvenSum(std::vector<int>& nums, int k) {
    int maxEvenSum = -1;
    std::vector<int> current;
    generateSubsequences(nums, current, k, 0, maxEvenSum);
    return maxEvenSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\binom{n}{k} \cdot k)$, where $n$ is the size of `nums`. This is because we generate all possible subsequences of size `k` and for each, we calculate the sum.
> - **Space Complexity:** $O(k)$, for the recursion stack and the current subsequence.
> - **Why these complexities occur:** The time complexity is due to generating all subsequences and calculating their sums. The space complexity is due to the recursion stack and storing the current subsequence.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use **bit manipulation** to generate all subsequences and calculate their sums more efficiently.
- Detailed breakdown of the approach:
  1. Use bit manipulation to generate all possible subsequences of size `k`.
  2. For each subsequence, calculate the sum of its elements using the bits to index into `nums`.
  3. Check if the sum is even. If it is, update the maximum even sum found so far.
- Proof of optimality: This approach still generates all possible subsequences but does so more efficiently using bit manipulation.

```cpp
#include <vector>
#include <algorithm>

int largestEvenSum(std::vector<int>& nums, int k) {
    int maxEvenSum = -1;
    int n = nums.size();
    for (int mask = 0; mask < (1 << n); ++mask) {
        if (__builtin_popcount(mask) == k) {
            int sum = 0;
            for (int i = 0; i < n; ++i) {
                if (mask & (1 << i)) sum += nums[i];
            }
            if (sum % 2 == 0) maxEvenSum = std::max(maxEvenSum, sum);
        }
    }
    return maxEvenSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot k)$, where $n$ is the size of `nums`. This is because we generate all possible subsequences using bit manipulation and calculate their sums.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output.
> - **Optimality proof:** This approach is optimal because it generates all possible subsequences and checks their sums, which is necessary to find the largest even sum.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: **bit manipulation**, generating all possible subsequences.
- Problem-solving patterns identified: Using bit manipulation to generate subsequences.
- Optimization techniques learned: Using bit manipulation to improve efficiency.
- Similar problems to practice: Other problems involving generating subsequences and calculating sums.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, not handling bit manipulation correctly.
- Edge cases to watch for: Empty input array, `k` larger than the size of the input array.
- Performance pitfalls: Not using bit manipulation efficiently, generating unnecessary subsequences.
- Testing considerations: Test with different input sizes, different values of `k`, and edge cases.