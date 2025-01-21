## Maximum Coins Heroes Can Collect

**Problem Link:** https://leetcode.com/problems/maximum-coins-heroes-can-collect/description

**Problem Statement:**
- Input: `nums`, an array of integers representing the coins that can be collected.
- Constraints: The length of `nums` is between 1 and 10^5, and each element in `nums` is between 1 and 10^4.
- Expected Output: The maximum number of coins that heroes can collect.
- Key Requirements: Heroes can only collect coins from one end of the array to the other. The goal is to maximize the number of coins collected.
- Edge Cases: If there is only one hero, they can collect all the coins.

**Example Test Cases:**
- If `nums = [1, 2, 3, 4, 5]`, the maximum coins that heroes can collect is `15`.
- If `nums = [1, 1, 1, 1, 1]`, the maximum coins that heroes can collect is `5`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible combinations of collecting coins from the start and end of the array.
- We can use recursion to explore all possible paths and keep track of the maximum coins collected.

```cpp
class Solution {
public:
    int maxCoins(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        // Initialize the dp array
        for (int i = 0; i < n; i++) {
            dp[i][i] = nums[i];
        }
        
        // Fill the dp array
        for (int length = 2; length <= n; length++) {
            for (int i = 0; i <= n - length; i++) {
                int j = i + length - 1;
                for (int k = i; k <= j; k++) {
                    int coins = nums[k];
                    if (k > i) coins += dp[i][k - 1];
                    if (k < j) coins += dp[k + 1][j];
                    dp[i][j] = max(dp[i][j], coins);
                }
            }
        }
        
        return dp[0][n - 1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input array. This is because we have three nested loops.
> - **Space Complexity:** $O(n^2)$, where $n$ is the length of the input array. This is because we use a 2D array to store the dp values.
> - **Why these complexities occur:** The time complexity occurs because we are using recursion to explore all possible paths, and the space complexity occurs because we are storing the dp values in a 2D array.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use dynamic programming to solve the problem.
- We can use a 2D array to store the maximum coins that can be collected for each subarray.
- We can fill the 2D array in a bottom-up manner, starting from the smallest subarrays and moving to the largest subarrays.

```cpp
class Solution {
public:
    int maxCoins(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> dp(n + 2, vector<int>(n + 2, 0));
        
        // Fill the dp array
        for (int length = 1; length <= n; length++) {
            for (int left = 1; left <= n - length + 1; left++) {
                int right = left + length - 1;
                for (int i = left; i <= right; i++) {
                    int coins = nums[i - 1];
                    if (i > left) coins += dp[left][i - 1];
                    if (i < right) coins += dp[i + 1][right];
                    dp[left][right] = max(dp[left][right], coins);
                }
            }
        }
        
        return dp[1][n];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input array. This is because we have three nested loops.
> - **Space Complexity:** $O(n^2)$, where $n$ is the length of the input array. This is because we use a 2D array to store the dp values.
> - **Optimality proof:** This is the optimal solution because we are using dynamic programming to solve the problem, which reduces the time complexity from exponential to cubic.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, recursion, and memoization.
- Problem-solving patterns identified: breaking down the problem into smaller subproblems and solving them recursively.
- Optimization techniques learned: using dynamic programming to reduce the time complexity.

**Mistakes to Avoid:**
- Common implementation errors: not initializing the dp array correctly, not filling the dp array in the correct order.
- Edge cases to watch for: when the input array is empty, when the input array has only one element.
- Performance pitfalls: not using memoization to store the dp values, not using dynamic programming to solve the problem.