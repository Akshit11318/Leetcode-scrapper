## Check If There Is a Path with Equal Number of 0s and 1s

**Problem Link:** https://leetcode.com/problems/check-if-there-is-a-path-with-equal-number-of-0s-and-1s/description

**Problem Statement:**
- Input format: A 2D binary array `grid` with `m` rows and `n` columns.
- Constraints: `1 <= m, n <= 100`, `grid[i][j]` is either `0` or `1`.
- Expected output format: `true` if there exists a path from the top-left corner to the bottom-right corner with an equal number of `0s` and `1s`, `false` otherwise.
- Key requirements: The path can only move right or down at any point.
- Edge cases: An empty grid, a grid with only one row or one column, or a grid where it's impossible to reach the bottom-right corner with an equal number of `0s` and `1s`.

**Example Test Cases:**
- `grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,1,1,1,1]]`, return `true`.
- `grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]`, return `false`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to explore all possible paths from the top-left corner to the bottom-right corner.
- We can use a depth-first search (DFS) to traverse the grid and count the number of `0s` and `1s` along each path.
- We will stop exploring a path as soon as the difference between the counts of `0s` and `1s` exceeds the remaining number of cells to visit.

```cpp
class Solution {
public:
    bool pathsWithEqualZeroAndOne(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        return dfs(grid, visited, 0, 0, 0, 0);
    }
    
    bool dfs(vector<vector<int>>& grid, vector<vector<bool>>& visited, int x, int y, int zeros, int ones) {
        int m = grid.size();
        int n = grid[0].size();
        if (x == m - 1 && y == n - 1) {
            return zeros == ones;
        }
        if (visited[x][y] || abs(zeros - ones) > m + n - x - y - 1) {
            return false;
        }
        visited[x][y] = true;
        if (grid[x][y] == 0) {
            zeros++;
        } else {
            ones++;
        }
        bool found = false;
        if (x + 1 < m) {
            found = found || dfs(grid, visited, x + 1, y, zeros, ones);
        }
        if (y + 1 < n) {
            found = found || dfs(grid, visited, x, y + 1, zeros, ones);
        }
        visited[x][y] = false;
        return found;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{m+n})$, because in the worst case, we might need to explore all possible paths.
> - **Space Complexity:** $O(m+n)$, due to the recursion stack.
> - **Why these complexities occur:** The brute force approach explores all possible paths, leading to exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a more efficient algorithm to explore the grid.
- We can use a dynamic programming approach to store the counts of `0s` and `1s` for each cell.
- We will use a memoization table to store the results of subproblems to avoid redundant computations.

```cpp
class Solution {
public:
    bool pathsWithEqualZeroAndOne(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> dp(m, vector<int>(n, -1));
        return dfs(grid, dp, 0, 0, 0, 0);
    }
    
    bool dfs(vector<vector<int>>& grid, vector<vector<int>>& dp, int x, int y, int zeros, int ones) {
        int m = grid.size();
        int n = grid[0].size();
        if (x == m - 1 && y == n - 1) {
            return zeros == ones;
        }
        if (dp[x][y] != -1) {
            return dp[x][y];
        }
        bool found = false;
        if (x + 1 < m) {
            if (grid[x][y] == 0) {
                found = found || dfs(grid, dp, x + 1, y, zeros + 1, ones);
            } else {
                found = found || dfs(grid, dp, x + 1, y, zeros, ones + 1);
            }
        }
        if (y + 1 < n) {
            if (grid[x][y] == 0) {
                found = found || dfs(grid, dp, x, y + 1, zeros + 1, ones);
            } else {
                found = found || dfs(grid, dp, x, y + 1, zeros, ones + 1);
            }
        }
        dp[x][y] = found;
        return found;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, because we visit each cell at most once.
> - **Space Complexity:** $O(m \cdot n)$, due to the memoization table.
> - **Optimality proof:** This is the optimal solution because we use memoization to avoid redundant computations and explore the grid efficiently.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: depth-first search, memoization, and dynamic programming.
- Problem-solving patterns identified: using a memoization table to store the results of subproblems.
- Optimization techniques learned: avoiding redundant computations using memoization.

**Mistakes to Avoid:**
- Common implementation errors: not checking the base cases correctly, not updating the memoization table correctly.
- Edge cases to watch for: an empty grid, a grid with only one row or one column.
- Performance pitfalls: not using memoization, leading to exponential time complexity.
- Testing considerations: testing the function with different grid sizes, testing the function with different values of `0s` and `1s`.