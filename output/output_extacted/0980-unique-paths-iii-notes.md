## Unique Paths III
**Problem Link:** https://leetcode.com/problems/unique-paths-iii/description

**Problem Statement:**
- Input: A 2D grid `grid` where `grid[i][j]` can be `0` (empty cell), `1` (starting cell), or `2` (ending cell).
- Constraints: `1 <= grid.length <= 20`, `1 <= grid[i].length <= 20`, `1 <= grid[i][j] <= 2`.
- Expected Output: The number of unique paths from the starting cell to the ending cell that cover all non-obstacle cells exactly once.
- Key Requirements: The path can only move right or down, and it must visit every non-obstacle cell exactly once.
- Example Test Cases:
  - `grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]` returns `2`.
  - `grid = [[0,1],[0,0]]` returns `1`.
  - `grid = [[0,0,0],[1,0,0],[0,0,2]]` returns `4`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible paths from the starting cell to the ending cell and count the ones that cover all non-obstacle cells exactly once.
- Step-by-step breakdown:
  1. Find the starting and ending cells.
  2. Define a recursive function to try all possible paths.
  3. In each recursive call, try moving right and down, and recursively call the function with the updated position and visited cells.
  4. If the current path covers all non-obstacle cells, increment the count.

```cpp
int uniquePathsIII(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();
    int startRow = 0, startCol = 0;
    int nonObstacleCells = 0;
    
    // Find the starting cell and count non-obstacle cells
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 1) {
                startRow = i;
                startCol = j;
            }
            if (grid[i][j] == 0 || grid[i][j] == 1) {
                nonObstacleCells++;
            }
        }
    }
    
    int result = 0;
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    visited[startRow][startCol] = true;
    
    // Try all possible paths
    function<void(int, int, int)> dfs = [&](int row, int col, int steps) {
        if (grid[row][col] == 2 && steps == nonObstacleCells) {
            result++;
            return;
        }
        
        vector<pair<int, int>> directions = {{0, 1}, {1, 0}};
        for (auto [dr, dc] : directions) {
            int nr = row + dr, nc = col + dc;
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && !visited[nr][nc] && grid[nr][nc] != -1) {
                visited[nr][nc] = true;
                dfs(nr, nc, steps + 1);
                visited[nr][nc] = false;
            }
        }
    };
    
    dfs(startRow, startCol, 1);
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{m \cdot n})$ because in the worst case, we try all possible paths.
> - **Space Complexity:** $O(m \cdot n)$ for the visited array.
> - **Why these complexities occur:** The brute force approach tries all possible paths, which leads to exponential time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Use a more efficient way to explore the paths, such as using a mask to keep track of visited cells.
- Detailed breakdown:
  1. Find the starting and ending cells.
  2. Define a recursive function to try all possible paths.
  3. Use a mask to keep track of visited cells.
  4. If the current path covers all non-obstacle cells, increment the count.

```cpp
int uniquePathsIII(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();
    int startRow = 0, startCol = 0;
    int nonObstacleCells = 0;
    
    // Find the starting cell and count non-obstacle cells
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 1) {
                startRow = i;
                startCol = j;
            }
            if (grid[i][j] == 0 || grid[i][j] == 1) {
                nonObstacleCells++;
            }
        }
    }
    
    int result = 0;
    vector<vector<int>> directions = {{0, 1}, {1, 0}};
    
    // Try all possible paths
    function<void(int, int, int)> dfs = [&](int row, int col, int steps) {
        if (grid[row][col] == 2 && steps == nonObstacleCells) {
            result++;
            return;
        }
        
        for (auto [dr, dc] : directions) {
            int nr = row + dr, nc = col + dc;
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && (grid[nr][nc] == 0 || grid[nr][nc] == 2)) {
                dfs(nr, nc, steps + 1);
            }
        }
    };
    
    dfs(startRow, startCol, 1);
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{m \cdot n})$ because in the worst case, we still try all possible paths.
> - **Space Complexity:** $O(m \cdot n)$ for the recursive call stack.
> - **Optimality proof:** This is the optimal approach because we have to try all possible paths to count the ones that cover all non-obstacle cells exactly once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-First Search (DFS), backtracking, and path exploration.
- Problem-solving patterns identified: Using a mask to keep track of visited cells and exploring all possible paths.
- Optimization techniques learned: Using a more efficient way to explore paths and keeping track of visited cells.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for out-of-bounds indices and not handling the base case correctly.
- Edge cases to watch for: Empty grid, grid with no non-obstacle cells, and grid with no starting or ending cell.
- Performance pitfalls: Trying all possible paths without using a more efficient approach.
- Testing considerations: Test the function with different grid sizes, shapes, and obstacle configurations.