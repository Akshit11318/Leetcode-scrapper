## Cherry Pickup II

**Problem Link:** https://leetcode.com/problems/cherry-pickup-ii/description

**Problem Statement:**
- Input format: A 2D grid `grid` where `grid[i][j]` represents the number of cherries at position `(i, j)`.
- Constraints: The grid is a rectangle with `m` rows and `n` columns, and `1 <= m, n <= 100`.
- Expected output format: The maximum number of cherries that can be collected.
- Key requirements: Two robots start at the top row, and each robot can move either down or right in each step. The robots can move independently.
- Example test cases:
  - `grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]` returns `24`.
  - `grid = [[1,0,0],[0,0,0],[0,0,1]]` returns `1`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible paths for both robots.
- Step-by-step breakdown:
  1. Initialize a recursive function that takes the current positions of both robots and the current row.
  2. For each possible move (down or right) for both robots, recursively call the function and keep track of the maximum cherries collected.
  3. Base case: If the robots reach the bottom row, return the total cherries collected.

```cpp
int cherryPickup(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    int maxCherries = 0;

    function<void(int, int, int, int, int)> dfs = 
        [&dfs, &grid, &maxCherries, m, n](int r1, int c1, int r2, int c2, int cherries) {
            if (r1 >= m || r2 >= m) return;
            cherries += grid[r1][c1] + grid[r2][c2];
            if (r1 == m - 1 && r2 == m - 1) {
                maxCherries = max(maxCherries, cherries);
                return;
            }
            for (int i = 0; i < 2; i++) {
                for (int j = 0; j < 2; j++) {
                    if (i == 0) dfs(r1 + 1, c1, r2 + j, c2 + j, cherries);
                    else dfs(r1 + 1, c1 + i, r2 + 1, c2 + 1, cherries);
                }
            }
        };

    dfs(0, 0, 0, 0, 0);
    return maxCherries;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(4^m)$, where $m$ is the number of rows, since there are $4$ possible moves for both robots at each step.
> - **Space Complexity:** $O(m)$, due to the recursive call stack.
> - **Why these complexities occur:** The brute force approach tries all possible paths, resulting in exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use dynamic programming to store the maximum cherries collected for each position and row.
- Detailed breakdown:
  1. Initialize a 3D DP array `dp` where `dp[i][j][k]` represents the maximum cherries collected when the first robot is at column `j` and the second robot is at column `k` in row `i`.
  2. Fill up the DP array row by row, considering all possible moves for both robots.
  3. The final answer is stored in `dp[m - 1][j][k]`, where `m - 1` is the last row.

```cpp
int cherryPickup(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    vector<vector<vector<int>>> dp(m, vector<vector<int>>(n, vector<int>(n, 0)));

    for (int j = 0; j < n; j++) {
        for (int k = 0; k < n; k++) {
            dp[0][j][k] = grid[0][j] + (j != k ? grid[0][k] : 0);
        }
    }

    for (int i = 1; i < m; i++) {
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                int maxCherries = 0;
                for (int x = max(0, j - 1); x <= min(n - 1, j + 1); x++) {
                    for (int y = max(0, k - 1); y <= min(n - 1, k + 1); y++) {
                        maxCherries = max(maxCherries, dp[i - 1][x][y]);
                    }
                }
                dp[i][j][k] = maxCherries + grid[i][j] + (j != k ? grid[i][k] : 0);
            }
        }
    }

    int maxCherries = 0;
    for (int j = 0; j < n; j++) {
        for (int k = 0; k < n; k++) {
            maxCherries = max(maxCherries, dp[m - 1][j][k]);
        }
    }
    return maxCherries;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n^3)$, where $m$ is the number of rows and $n$ is the number of columns.
> - **Space Complexity:** $O(m \cdot n^2)$, due to the DP array.
> - **Optimality proof:** The DP approach ensures that we consider all possible paths and store the maximum cherries collected for each position and row, resulting in the optimal solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Dynamic programming, recursion, and memoization.
- Problem-solving patterns: Breaking down the problem into smaller sub-problems and using DP to store and reuse solutions.
- Optimization techniques: Using DP to avoid redundant calculations and reduce time complexity.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the DP array correctly or not considering all possible moves for both robots.
- Edge cases to watch for: Handling cases where the robots are at the same position or at the boundary of the grid.
- Performance pitfalls: Using a naive recursive approach without memoization, resulting in exponential time complexity.
- Testing considerations: Testing the solution with different grid sizes and cherry distributions to ensure correctness.