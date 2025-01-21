## Minimum Operations to Form Subsequence with Target Sum

**Problem Link:** https://leetcode.com/problems/minimum-operations-to-form-subsequence-with-target-sum/description

**Problem Statement:**
- Given two arrays `nums` and `target`, find the minimum number of operations required to form a subsequence of `nums` that sums up to `target`.
- The operations allowed are adding or removing elements from the subsequence.
- The input arrays `nums` and `target` are non-empty, and the sum of `nums` is greater than or equal to `target`.
- The expected output is the minimum number of operations required.

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible subsequences of `nums` and check if their sum equals `target`.
- We can use a recursive approach to generate all subsequences.
- However, this approach is inefficient due to its exponential time complexity.

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums, int target) {
        int n = nums.size();
        int minOps = INT_MAX;
        for (int mask = 0; mask < (1 << n); mask++) {
            int sum = 0;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    sum += nums[i];
                }
            }
            if (sum == target) {
                int ops = 0;
                for (int i = 0; i < n; i++) {
                    if ((mask & (1 << i)) == 0) {
                        ops++;
                    }
                }
                minOps = min(minOps, ops);
            }
        }
        return minOps;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of `nums`. This is because we generate all possible subsequences and calculate their sum.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum number of operations.
> - **Why these complexities occur:** The exponential time complexity is due to generating all possible subsequences, and the constant space complexity is because we only use a fixed amount of space to store the result.

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use dynamic programming to build up a table of minimum operations required to reach each possible sum from 0 to `target`.
- We iterate over each element in `nums` and update the table accordingly.
- This approach avoids the exponential time complexity of the brute force approach.

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums, int target) {
        int n = nums.size();
        vector<int> dp(target + 1, n + 1);
        dp[0] = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = target; j >= 0; j--) {
                if (j >= nums[i - 1]) {
                    dp[j] = min(dp[j], dp[j - nums[i - 1]] + 1);
                }
                dp[j] = min(dp[j], dp[j] + 1);
            }
        }
        return dp[target] <= n ? dp[target] : -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot target)$, where $n$ is the length of `nums` and `target` is the target sum.
> - **Space Complexity:** $O(target)$, as we use a table of size `target + 1` to store the minimum number of operations required to reach each possible sum.
> - **Optimality proof:** This approach is optimal because it uses dynamic programming to build up a table of minimum operations required to reach each possible sum, avoiding the exponential time complexity of the brute force approach.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, bitmasking.
- Problem-solving patterns identified: building up a table of minimum operations required to reach each possible sum.
- Optimization techniques learned: avoiding exponential time complexity using dynamic programming.

**Mistakes to Avoid:**
- Common implementation errors: incorrect initialization of the dynamic programming table, incorrect updating of the table.
- Edge cases to watch for: `target` is 0, `nums` is empty.
- Performance pitfalls: using the brute force approach for large inputs.
- Testing considerations: testing with different inputs, including edge cases.