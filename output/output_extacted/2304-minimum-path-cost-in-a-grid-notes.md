## Minimum Path Cost in a Grid

**Problem Link:** https://leetcode.com/problems/minimum-path-cost-in-a-grid/description

**Problem Statement:**
- Input format: A 2D grid of integers, where each cell represents a cost.
- Constraints: The grid is non-empty and contains at least one row and one column.
- Expected output format: The minimum path cost from the top-left cell to the bottom-right cell.
- Key requirements: The path can only move either down or right at any point in time.
- Edge cases: The grid may contain negative numbers, and the minimum path cost may not be the shortest path.

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible paths from the top-left cell to the bottom-right cell.
- Step-by-step breakdown of the solution:
  1. Start at the top-left cell.
  2. At each cell, try moving down and right.
  3. Recursively explore all possible paths.
  4. Keep track of the minimum path cost.
- Why this approach comes to mind first: It's a straightforward way to solve the problem, but it's inefficient due to the large number of possible paths.

```cpp
class Solution {
public:
    int minPathCost(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int minCost = INT_MAX;
        
        function<void(int, int, int)> dfs = [&](int i, int j, int cost) {
            if (i == m - 1 && j == n - 1) {
                minCost = min(minCost, cost + grid[i][j]);
                return;
            }
            
            if (i < m - 1) {
                dfs(i + 1, j, cost + grid[i][j]);
            }
            if (j < n - 1) {
                dfs(i, j + 1, cost + grid[i][j]);
            }
        };
        
        dfs(0, 0, 0);
        return minCost;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{m+n})$, where $m$ is the number of rows and $n$ is the number of columns. This is because in the worst case, we try all possible paths.
> - **Space Complexity:** $O(m+n)$, due to the recursive call stack.
> - **Why these complexities occur:** The brute force approach tries all possible paths, resulting in exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use dynamic programming to store the minimum path cost to each cell.
- Detailed breakdown of the approach:
  1. Create a 2D array `dp` to store the minimum path cost to each cell.
  2. Initialize the first cell of `dp` with the cost of the first cell in the grid.
  3. For each cell in the grid, calculate the minimum path cost by considering the minimum path cost of the cell above it and the cell to its left.
  4. The minimum path cost to the bottom-right cell is stored in the bottom-right cell of `dp`.
- Proof of optimality: This approach is optimal because it only considers the minimum path cost to each cell, avoiding redundant calculations.

```cpp
class Solution {
public:
    int minPathCost(vector<vector<int>>& grid) {
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
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns. This is because we only need to iterate through the grid once.
> - **Space Complexity:** $O(m \cdot n)$, due to the `dp` array.
> - **Optimality proof:** This approach is optimal because it only considers the minimum path cost to each cell, avoiding redundant calculations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, memoization.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems, using a bottom-up approach.
- Optimization techniques learned: Avoiding redundant calculations, using memoization to store intermediate results.
- Similar problems to practice: Other dynamic programming problems, such as the **_Longest Common Subsequence_** or **_Edit Distance_** problems.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize the `dp` array, not considering the base case.
- Edge cases to watch for: Negative numbers in the grid, empty grid.
- Performance pitfalls: Using a recursive approach without memoization, resulting in exponential time complexity.
- Testing considerations: Testing the function with different grid sizes, testing the function with negative numbers in the grid.