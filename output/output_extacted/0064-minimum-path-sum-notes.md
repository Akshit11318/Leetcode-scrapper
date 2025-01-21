## Minimum Path Sum
**Problem Link:** https://leetcode.com/problems/minimum-path-sum/description

**Problem Statement:**
- Input format and constraints: Given a `m x n` grid filled with non-negative numbers, find a path from top-left to bottom-right which minimizes the sum of all numbers along its path.
- Expected output format: Return the minimum sum of the path.
- Key requirements and edge cases to consider: The path must consist of either one step to the right or one step down at any point in time. The grid will not be empty, and it will have at least one row and one column.
- Example test cases with explanations:
  - For `grid = [[1,3,1],[1,5,1],[4,2,1]]`, the output should be `7` because the path with the minimum sum is: `1 -> 3 -> 1 -> 1 -> 1`, which sums up to `7`.
  - For `grid = [[1,2,3],[4,5,6]]`, the output should be `12` because the path with the minimum sum is: `1 -> 4 -> 5 -> 6`, which sums up to `16`, but the optimal path is `1 -> 2 -> 3 -> 6`, summing up to `12`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: To find the minimum path sum, we can try all possible paths from the top-left to the bottom-right and calculate their sums.
- Step-by-step breakdown of the solution: 
  1. Start at the top-left cell.
  2. At each cell, you can either move right or down.
  3. Use recursion to explore all possible paths.
  4. Keep track of the minimum sum found so far.

```cpp
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        return dfs(grid, 0, 0, m, n);
    }
    
    int dfs(vector<vector<int>>& grid, int i, int j, int m, int n) {
        if (i == m - 1 && j == n - 1) return grid[i][j];
        if (i >= m || j >= n) return INT_MAX;
        
        int right = dfs(grid, i, j + 1, m, n);
        int down = dfs(grid, i + 1, j, m, n);
        
        return grid[i][j] + min(right, down);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{m+n})$ because in the worst case, we might have to explore all possible paths, which is exponential in the number of cells.
> - **Space Complexity:** $O(m+n)$ due to the recursion stack.
> - **Why these complexities occur:** The brute force approach is not efficient because it does a lot of repeated work. Each cell is visited multiple times, leading to exponential time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to store the minimum path sum to each cell, avoiding repeated calculations.
- Detailed breakdown of the approach:
  1. Create a `dp` table of the same size as the input grid.
  2. Initialize the first cell of `dp` with the value of the first cell in the grid.
  3. Fill the first row and first column of `dp` based on the values in the grid.
  4. For each remaining cell in `dp`, calculate its value as the minimum of the cell above it and the cell to its left, plus the value of the current cell in the grid.
- Proof of optimality: This approach ensures that we consider all possible paths while avoiding redundant calculations, leading to a significant reduction in time complexity.

```cpp
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 0));
        
        dp[0][0] = grid[0][0];
        for (int i = 1; i < m; i++) {
            dp[i][0] = dp[i-1][0] + grid[i][0];
        }
        for (int j = 1; j < n; j++) {
            dp[0][j] = dp[0][j-1] + grid[0][j];
        }
        
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j];
            }
        }
        
        return dp[m-1][n-1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$ because we fill the `dp` table once, visiting each cell exactly once.
> - **Space Complexity:** $O(m \cdot n)$ for the `dp` table.
> - **Optimality proof:** This dynamic programming approach is optimal because it minimizes the number of operations required to find the minimum path sum, avoiding the exponential time complexity of the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, memoization, and path finding.
- Problem-solving patterns identified: Breaking down problems into smaller sub-problems and solving them efficiently.
- Optimization techniques learned: Avoiding redundant calculations and using memoization.
- Similar problems to practice: Other dynamic programming problems, such as the `Longest Common Subsequence` or `Knapsack Problem`.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` table correctly or not handling edge cases.
- Edge cases to watch for: Empty grids, grids with a single row or column, and grids with negative numbers.
- Performance pitfalls: Using the brute force approach for large grids.
- Testing considerations: Testing with different grid sizes, shapes, and values to ensure the solution is robust.