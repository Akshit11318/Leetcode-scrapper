## Minimum Sum of Values by Dividing Array
**Problem Link:** https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/description

**Problem Statement:**
- Input: An integer array `nums` and an integer `k`.
- Output: The minimum sum of values by dividing the array into `k` non-empty groups.
- Key requirements:
  - Each group must be a contiguous subarray of `nums`.
  - The value of a group is the sum of its elements.
- Edge cases:
  - `1 <= k <= nums.length`
  - `1 <= nums.length <= 2000`
  - `1 <= nums[i] <= 10^6`

### Brute Force Approach
**Explanation:**
- The initial thought process is to try all possible divisions of the array into `k` groups.
- Step-by-step breakdown:
  1. Generate all possible combinations of `k-1` split points in the array.
  2. For each combination, calculate the sum of values for each group.
  3. Calculate the sum of values for all groups.
  4. Keep track of the minimum sum found so far.

```cpp
#include <vector>
#include <algorithm>

int minSumOfValues(vector<int>& nums, int k) {
    int n = nums.size();
    vector<int> prefixSum(n + 1, 0);
    for (int i = 0; i < n; i++) {
        prefixSum[i + 1] = prefixSum[i] + nums[i];
    }

    int minSum = INT_MAX;
    // Generate all possible combinations of k-1 split points
    for (int mask = 0; mask < (1 << n); mask++) {
        if (__builtin_popcount(mask) != k - 1) continue;
        int sum = 0;
        int start = 0;
        for (int i = 0; i < n; i++) {
            if (mask & (1 << i)) {
                sum += prefixSum[i + 1] - prefixSum[start];
                start = i + 1;
            }
        }
        sum += prefixSum[n] - prefixSum[start];
        minSum = min(minSum, sum);
    }
    return minSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input array. This is because we generate all possible combinations of split points, which takes $O(2^n)$ time, and for each combination, we calculate the sum of values, which takes $O(n)$ time.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we use a prefix sum array to store the cumulative sum of elements in the array.
> - **Why these complexities occur:** The brute force approach generates all possible combinations of split points, which results in exponential time complexity. The space complexity is linear because we only need to store the prefix sum array.

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use dynamic programming to find the minimum sum of values.
- Detailed breakdown:
  1. Initialize a 2D array `dp` where `dp[i][j]` represents the minimum sum of values for the first `i` elements divided into `j` groups.
  2. Fill the `dp` array in a bottom-up manner.
  3. For each `i` and `j`, try all possible split points and calculate the minimum sum of values.
  4. The final answer is stored in `dp[n][k]`.

```cpp
#include <vector>
#include <algorithm>

int minSumOfValues(vector<int>& nums, int k) {
    int n = nums.size();
    vector<int> prefixSum(n + 1, 0);
    for (int i = 0; i < n; i++) {
        prefixSum[i + 1] = prefixSum[i] + nums[i];
    }

    vector<vector<int>> dp(n + 1, vector<int>(k + 1, INT_MAX));
    dp[0][0] = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= min(i, k); j++) {
            for (int x = 1; x <= i; x++) {
                dp[i][j] = min(dp[i][j], dp[i - x][j - 1] + prefixSum[i] - prefixSum[i - x]);
            }
        }
    }
    return dp[n][k];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot k)$, where $n$ is the length of the input array and $k$ is the number of groups. This is because we fill the `dp` array in a bottom-up manner, and for each cell, we try all possible split points.
> - **Space Complexity:** $O(n \cdot k)$, where $n$ is the length of the input array and $k$ is the number of groups. This is because we use a 2D array to store the minimum sum of values for each subproblem.
> - **Optimality proof:** The dynamic programming approach ensures that we consider all possible divisions of the array into `k` groups and find the minimum sum of values. The time complexity is polynomial, which is much better than the exponential time complexity of the brute force approach.

### Final Notes

**Learning Points:**
- Key algorithmic concepts: dynamic programming, prefix sum array.
- Problem-solving patterns: divide and conquer, bottom-up dynamic programming.
- Optimization techniques: memoization, avoiding redundant calculations.
- Similar problems to practice: partition problems, subset sum problems.

**Mistakes to Avoid:**
- Common implementation errors: incorrect initialization of the `dp` array, incorrect calculation of the minimum sum of values.
- Edge cases to watch for: empty input array, `k` is larger than the length of the input array.
- Performance pitfalls: using the brute force approach for large inputs, not using memoization to avoid redundant calculations.
- Testing considerations: test the function with different inputs, including edge cases and large inputs.