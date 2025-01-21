## Number of Ways to Split Array

**Problem Link:** https://leetcode.com/problems/number-of-ways-to-split-array/description

**Problem Statement:**
- Input format: An integer array `nums` and an integer `k`.
- Constraints: `1 <= nums.length <= 1000`, `1 <= nums[i] <= 10^6`, `1 <= k <= nums.length`.
- Expected output format: The number of ways to split the array into `k` non-empty subarrays such that the sum of each subarray is within the range `[left, right]`.
- Key requirements and edge cases to consider: The sum of each subarray must be within the given range, and the array must be split into exactly `k` subarrays.
- Example test cases with explanations:
  - For `nums = [1, 2, 3, 4]`, `k = 2`, `left = 3`, `right = 6`, the output should be `2` because the array can be split into `[[1, 2], [3, 4]]` and `[[1], [2, 3, 4]]`.
  - For `nums = [1, 1, 1, 1]`, `k = 2`, `left = 1`, `right = 3`, the output should be `3` because the array can be split into `[[1], [1, 1, 1]]`, `[[1, 1], [1, 1]]`, and `[[1, 1, 1], [1]]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible ways to split the array into `k` subarrays and check if the sum of each subarray is within the given range.
- The brute force approach involves using recursion to generate all possible splits of the array.
- This approach comes to mind first because it is straightforward and easy to implement.

```cpp
class Solution {
public:
    int numberOfWays(vector<int>& nums, int k, int left, int right) {
        int n = nums.size();
        vector<int> prefix(n + 1, 0);
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + nums[i];
        }
        return dfs(0, k, prefix, left, right);
    }

    int dfs(int start, int k, vector<int>& prefix, int left, int right) {
        if (start == prefix.size() - 1) {
            return k == 0;
        }
        int count = 0;
        for (int end = start + 1; end < prefix.size(); end++) {
            int sum = prefix[end] - prefix[start];
            if (sum >= left && sum <= right && k > 0) {
                count += dfs(end, k - 1, prefix, left, right);
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot k)$, where $n$ is the length of the input array. This is because in the worst case, we generate all possible splits of the array, which has $2^n$ possibilities, and for each split, we recursively call the `dfs` function $k$ times.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we use a prefix sum array to store the cumulative sums of the input array.
> - **Why these complexities occur:** The time complexity occurs because we use recursion to generate all possible splits of the array, which has an exponential number of possibilities. The space complexity occurs because we use a prefix sum array to store the cumulative sums of the input array.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use dynamic programming to store the number of ways to split the array into `k` subarrays up to each position.
- We use a 2D array `dp` where `dp[i][j]` represents the number of ways to split the array into `j` subarrays up to position `i`.
- We iterate over the array and for each position, we iterate over all possible previous positions and check if the sum of the subarray is within the given range. If it is, we update `dp[i][j]` accordingly.

```cpp
class Solution {
public:
    int numberOfWays(vector<int>& nums, int k, int left, int right) {
        int n = nums.size();
        vector<int> prefix(n + 1, 0);
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + nums[i];
        }
        vector<vector<int>> dp(n + 1, vector<int>(k + 1, 0));
        dp[0][0] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= k; j++) {
                for (int prev = 0; prev < i; prev++) {
                    int sum = prefix[i] - prefix[prev];
                    if (sum >= left && sum <= right) {
                        dp[i][j] += dp[prev][j - 1];
                    }
                }
            }
        }
        return dp[n][k];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot k)$, where $n$ is the length of the input array. This is because we use three nested loops to iterate over the array and the `dp` array.
> - **Space Complexity:** $O(n \cdot k)$, where $n` is the length of the input array. This is because we use a 2D array `dp` to store the number of ways to split the array into `k` subarrays up to each position.
> - **Optimality proof:** This solution is optimal because we use dynamic programming to store the number of ways to split the array into `k` subarrays up to each position, which avoids the exponential time complexity of the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, recursion.
- Problem-solving patterns identified: using prefix sums to store cumulative sums, using dynamic programming to store intermediate results.
- Optimization techniques learned: using dynamic programming to avoid exponential time complexity.
- Similar problems to practice: problems involving dynamic programming, recursion, and prefix sums.

**Mistakes to Avoid:**
- Common implementation errors: not initializing the `dp` array correctly, not updating the `dp` array correctly.
- Edge cases to watch for: handling the case where `k` is 0, handling the case where the sum of the subarray is outside the given range.
- Performance pitfalls: using recursion without memoization, using dynamic programming without optimizing the space complexity.
- Testing considerations: testing the solution with different inputs, testing the solution with edge cases.