## Maximum Amount of Money Robot Can Earn

**Problem Link:** https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/description

**Problem Statement:**
- Input: A 2D array `cells` representing the amount of money in each cell, and a positive integer `maxAmount`.
- Constraints: The robot can only move right or down from any cell, and it can't earn more than `maxAmount` of money in total.
- Expected Output: The maximum amount of money the robot can earn without exceeding `maxAmount`.
- Key Requirements:
  - The robot starts at the top-left cell and can move right or down.
  - The robot can't earn more than `maxAmount` of money in total.
- Edge Cases:
  - If `maxAmount` is greater than or equal to the sum of all money in the cells, the robot can earn all the money.
  - If `maxAmount` is less than the money in the top-left cell, the robot can't earn any money.
- Example Test Cases:
  - `cells = [[1,2,3],[4,5,6],[7,8,9]], maxAmount = 20` should return `15` because the robot can move right from the top-left cell to the top-right cell, and then move down to the bottom-right cell.
  - `cells = [[1,2,3],[4,5,6],[7,8,9]], maxAmount = 5` should return `5` because the robot can't earn more than `maxAmount` of money.

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible paths from the top-left cell to the bottom-right cell and calculate the total amount of money for each path.
- Step-by-step breakdown:
  1. Generate all possible paths from the top-left cell to the bottom-right cell.
  2. For each path, calculate the total amount of money.
  3. Keep track of the maximum amount of money that is less than or equal to `maxAmount`.

```cpp
class Solution {
public:
    int maxMoney(vector<vector<int>>& cells, int maxAmount) {
        int m = cells.size();
        int n = cells[0].size();
        int maxEarned = 0;
        
        function<void(int, int, int)> dfs = [&](int i, int j, int earned) {
            if (i == m || j == n) return;
            if (earned + cells[i][j] > maxAmount) return;
            
            earned += cells[i][j];
            maxEarned = max(maxEarned, earned);
            
            dfs(i + 1, j, earned); // move down
            dfs(i, j + 1, earned); // move right
        };
        
        dfs(0, 0, 0);
        return maxEarned;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{m+n})$ because in the worst case, we need to explore all possible paths from the top-left cell to the bottom-right cell.
> - **Space Complexity:** $O(m+n)$ because of the recursive call stack.
> - **Why these complexities occur:** The brute force approach tries all possible paths, resulting in an exponential time complexity. The space complexity is linear due to the recursive call stack.

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use dynamic programming to store the maximum amount of money that can be earned at each cell.
- Detailed breakdown:
  1. Create a 2D array `dp` to store the maximum amount of money that can be earned at each cell.
  2. Initialize the first cell of `dp` with the value of the first cell in `cells`.
  3. For each cell in `cells`, update the corresponding cell in `dp` with the maximum amount of money that can be earned by moving right or down from the previous cells.
  4. Keep track of the maximum amount of money that is less than or equal to `maxAmount`.

```cpp
class Solution {
public:
    int maxMoney(vector<vector<int>>& cells, int maxAmount) {
        int m = cells.size();
        int n = cells[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 0));
        
        dp[0][0] = min(cells[0][0], maxAmount);
        
        for (int i = 1; i < m; i++) {
            dp[i][0] = min(dp[i-1][0] + cells[i][0], maxAmount);
        }
        
        for (int j = 1; j < n; j++) {
            dp[0][j] = min(dp[0][j-1] + cells[0][j], maxAmount);
        }
        
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = min(max(dp[i-1][j], dp[i][j-1]) + cells[i][j], maxAmount);
            }
        }
        
        return dp[m-1][n-1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$ because we need to fill in the `dp` array.
> - **Space Complexity:** $O(m \cdot n)$ because of the `dp` array.
> - **Optimality proof:** This approach is optimal because it uses dynamic programming to store the maximum amount of money that can be earned at each cell, avoiding redundant calculations and ensuring that we consider all possible paths.

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Dynamic programming, recursion.
- Problem-solving patterns: Using a 2D array to store intermediate results.
- Optimization techniques: Avoiding redundant calculations by storing intermediate results.

**Mistakes to Avoid:**
- Not considering the `maxAmount` constraint when calculating the maximum amount of money.
- Not using dynamic programming to store intermediate results.
- Not handling edge cases correctly.