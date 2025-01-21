## Longest Increasing Subsequence

**Problem Link:** https://leetcode.com/problems/longest-increasing-subsequence/description

**Problem Statement:**
- Input format: An integer array `nums` of length `n`.
- Constraints: `0 <= n <= 10^4`, `0 <= nums[i] <= 10^9`.
- Expected output format: The length of the longest increasing subsequence.
- Key requirements: Find the longest subsequence where every element is greater than its previous element.
- Edge cases to consider: Empty array, array with a single element, array with duplicate elements.
- Example test cases:
  - Input: `nums = [10,9,2,5,3,7,101,18]`, Output: `4`, Explanation: The longest increasing subsequence is `[2,3,7,101]`.
  - Input: `nums = [0,1,0,3,2,3]`, Output: `4`, Explanation: The longest increasing subsequence is `[0,1,2,3]`.
  - Input: `nums = [7,6,5,4,3,2]`, Output: `1`, Explanation: The longest increasing subsequence is `[7]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subsequences and check if each subsequence is increasing.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsequences of the input array.
  2. For each subsequence, check if it is increasing by comparing each element with its previous element.
  3. Keep track of the longest increasing subsequence found so far.
- Why this approach comes to mind first: It is a straightforward approach that checks all possible subsequences.

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int lengthOfLIS(std::vector<int>& nums) {
        if (nums.empty()) return 0;

        int max_length = 1;
        for (int mask = 1; mask < (1 << nums.size()); mask++) {
            std::vector<int> subsequence;
            for (int i = 0; i < nums.size(); i++) {
                if ((mask & (1 << i)) != 0) {
                    subsequence.push_back(nums[i]);
                }
            }

            if (isIncreasing(subsequence) && subsequence.size() > max_length) {
                max_length = subsequence.size();
            }
        }

        return max_length;
    }

    bool isIncreasing(const std::vector<int>& subsequence) {
        for (int i = 1; i < subsequence.size(); i++) {
            if (subsequence[i] <= subsequence[i - 1]) {
                return false;
            }
        }

        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input array. The reason is that we generate $2^n$ subsequences and for each subsequence, we check if it is increasing in $O(n)$ time.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array. The reason is that we need to store the subsequence in memory.
> - **Why these complexities occur:** The brute force approach has high time complexity because it generates all possible subsequences and checks each one. The space complexity is relatively low because we only need to store one subsequence at a time.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use dynamic programming to solve this problem. The idea is to maintain an array `dp` where `dp[i]` is the length of the longest increasing subsequence ending at index `i`.
- Detailed breakdown of the approach:
  1. Initialize an array `dp` of length `n` with all elements set to 1, where `n` is the length of the input array.
  2. For each element in the array, compare it with all previous elements. If the current element is greater than a previous element, update `dp[i]` to be the maximum of its current value and `dp[j] + 1`, where `j` is the index of the previous element.
  3. The length of the longest increasing subsequence is the maximum value in the `dp` array.
- Proof of optimality: This approach is optimal because it only needs to iterate through the array once and uses a constant amount of extra space.

```cpp
class Solution {
public:
    int lengthOfLIS(std::vector<int>& nums) {
        if (nums.empty()) return 0;

        std::vector<int> dp(nums.size(), 1);
        int max_length = 1;

        for (int i = 1; i < nums.size(); i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    dp[i] = std::max(dp[i], dp[j] + 1);
                }
            }

            max_length = std::max(max_length, dp[i]);
        }

        return max_length;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input array. The reason is that we iterate through the array once and for each element, we compare it with all previous elements.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array. The reason is that we need to store the `dp` array in memory.
> - **Optimality proof:** This approach is optimal because it only needs to iterate through the array once and uses a constant amount of extra space. The time complexity is $O(n^2)$ because we compare each element with all previous elements.

---

### Alternative Approach

**Explanation:**
- Different perspective: We can use a binary search approach to solve this problem. The idea is to maintain an array `tails` where `tails[i]` is the smallest tail of all increasing subsequences with length `i`.
- Unique trade-offs: This approach has a time complexity of $O(n \log n)$, which is better than the optimal approach for large inputs. However, it uses more extra space because we need to store the `tails` array.
- Scenarios where this approach might be preferred: When the input array is very large and we need to find the length of the longest increasing subsequence quickly.

```cpp
class Solution {
public:
    int lengthOfLIS(std::vector<int>& nums) {
        if (nums.empty()) return 0;

        std::vector<int> tails;
        for (int num : nums) {
            auto it = std::lower_bound(tails.begin(), tails.end(), num);
            if (it == tails.end()) {
                tails.push_back(num);
            } else {
                *it = num;
            }
        }

        return tails.size();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the length of the input array. The reason is that we use binary search to find the correct position in the `tails` array.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array. The reason is that we need to store the `tails` array in memory.
> - **Trade-off analysis:** This approach has a better time complexity than the optimal approach for large inputs, but it uses more extra space. We should choose this approach when the input array is very large and we need to find the length of the longest increasing subsequence quickly.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Dynamic programming, binary search.
- Problem-solving patterns: Using dynamic programming to solve problems that have overlapping subproblems, using binary search to find the correct position in an array.
- Optimization techniques: Using dynamic programming to reduce the time complexity of a problem, using binary search to reduce the time complexity of a problem.
- Similar problems to practice: Longest common subsequence, shortest path in a graph.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` array correctly, not updating the `dp` array correctly.
- Edge cases to watch for: Empty array, array with a single element, array with duplicate elements.
- Performance pitfalls: Using a brute force approach for large inputs, not using dynamic programming or binary search to reduce the time complexity of a problem.
- Testing considerations: Testing the function with different inputs, including edge cases and large inputs.