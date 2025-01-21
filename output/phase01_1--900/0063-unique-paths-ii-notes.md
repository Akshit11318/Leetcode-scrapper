## Unique Paths II
**Problem Link:** https://leetcode.com/problems/unique-paths-ii/description

**Problem Statement:**
- Input format: A 2D vector `obstacleGrid` representing a grid where `obstacleGrid[i][j]` is either `0` (no obstacle) or `1` (obstacle).
- Constraints: The grid can have any number of rows and columns, but it's guaranteed to have at least one cell.
- Expected output format: The number of unique paths from the top-left corner to the bottom-right corner, avoiding obstacles.
- Key requirements and edge cases to consider:
  - The robot can only move either down or right at any point in time.
  - The starting point (top-left corner) and the ending point (bottom-right corner) are always accessible.
  - Example test cases:
    - `obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]` should return `2`, as there are two unique paths around the obstacle.
    - `obstacleGrid = [[0,1],[1,0]]` should return `0`, as there's no way to reach the bottom-right corner.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To calculate the number of unique paths, we could try all possible combinations of moves (down or right) and count how many of them successfully reach the bottom-right corner without hitting an obstacle.
- Step-by-step breakdown of the solution:
  1. Start at the top-left corner.
  2. At each step, try moving down and right if possible (i.e., if the destination cell is within the grid boundaries and not an obstacle).
  3. Recursively explore all possible paths.
  4. Count the number of paths that successfully reach the bottom-right corner.
- Why this approach comes to mind first: It's a straightforward, exhaustive search that guarantees finding all possible paths, but it's inefficient due to the overlapping subproblems and the potential for exploring the same paths multiple times.

```cpp
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        return dfs(obstacleGrid, 0, 0, m, n);
    }
    
    int dfs(vector<vector<int>>& obstacleGrid, int i, int j, int m, int n) {
        if (i == m - 1 && j == n - 1) return 1 - obstacleGrid[i][j];
        if (i >= m || j >= n || obstacleGrid[i][j] == 1) return 0;
        
        int right = dfs(obstacleGrid, i, j + 1, m, n);
        int down = dfs(obstacleGrid, i + 1, j, m, n);
        return right + down;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{m+n})$, where $m$ and $n$ are the number of rows and columns, respectively. This is because in the worst case, we might explore all possible combinations of moves.
> - **Space Complexity:** $O(m+n)$ due to the recursion stack.
> - **Why these complexities occur:** The brute force approach involves exploring all possible paths, leading to exponential time complexity. The space complexity is linear due to the recursion stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of exploring all possible paths, we can use dynamic programming to store and reuse the results of subproblems. This approach avoids the redundancy of recalculating the same paths multiple times.
- Detailed breakdown of the approach:
  1. Create a 2D array `dp` of the same size as `obstacleGrid`, where `dp[i][j]` represents the number of unique paths from the top-left corner to the cell at `(i, j)`.
  2. Initialize the first cell `dp[0][0]` based on whether the top-left corner is an obstacle.
  3. Fill in the first row and first column of `dp`, considering obstacles.
  4. For each remaining cell, calculate `dp[i][j]` as the sum of `dp[i-1][j]` and `dp[i][j-1]`, unless the cell is an obstacle, in which case `dp[i][j] = 0`.
- Proof of optimality: This approach ensures that each subproblem is solved only once and stored in `dp`, avoiding redundant calculations. The final result is stored in `dp[m-1][n-1]`.

```cpp
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 0));
        
        // Initialize the first cell
        dp[0][0] = 1 - obstacleGrid[0][0];
        
        // Fill the first row
        for (int i = 1; i < n; i++) {
            dp[0][i] = dp[0][i-1] * (1 - obstacleGrid[0][i]);
        }
        
        // Fill the first column
        for (int i = 1; i < m; i++) {
            dp[i][0] = dp[i-1][0] * (1 - obstacleGrid[i][0]);
        }
        
        // Fill the rest of the dp table
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = (1 - obstacleGrid[i][j]) * (dp[i-1][j] + dp[i][j-1]);
            }
        }
        
        return dp[m-1][n-1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the number of rows and columns, respectively. This is because we fill in the `dp` table once.
> - **Space Complexity:** $O(m \cdot n)$ for the `dp` table.
> - **Optimality proof:** This approach ensures that each subproblem is solved only once, avoiding redundant calculations and achieving the optimal time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, memoization, and avoiding redundant calculations.
- Problem-solving patterns identified: Breaking down problems into smaller subproblems and storing results for reuse.
- Optimization techniques learned: Using a `dp` table to store and reuse results of subproblems.
- Similar problems to practice: Unique Paths, Longest Increasing Subsequence, and Edit Distance.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, such as obstacles in the first row or column.
- Edge cases to watch for: Obstacles in the top-left or bottom-right corners.
- Performance pitfalls: Using a brute force approach that leads to exponential time complexity.
- Testing considerations: Test cases with obstacles in different positions, including the first and last rows and columns.