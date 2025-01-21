## Count Unguarded Cells in the Grid
**Problem Link:** https://leetcode.com/problems/count-unguarded-cells-in-the-grid/description

**Problem Statement:**
- Input format: A 2D grid represented as a vector of vectors (`m x n`), and a vector of guards and walls (`guards` and `walls` are not directly provided but are represented within the grid).
- Constraints: `m == grid.length`, `n == grid[0].length`, `1 <= m, n <= 100`, `1 <= m * n <= 100`.
- Expected output: The number of unguarded cells in the grid.
- Key requirements and edge cases: The grid contains only three types of cells: empty cells (`0`), guards (`1`), and walls (`-1`). We need to count the number of empty cells that are not guarded by any guard.
- Example test cases with explanations:
    - An example grid with guards and walls, and the expected output showing the number of unguarded cells.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: For each cell in the grid, check if it is an empty cell. If it is, then for each guard in the grid, check if there is a line of sight from the guard to the empty cell. If there is no line of sight for any guard, then the cell is unguarded.
- Step-by-step breakdown of the solution:
    1. Iterate through each cell in the grid.
    2. If the cell is empty (`0`), then for each guard in the grid, check for line of sight.
    3. To check for line of sight, move in all four directions (up, down, left, right) from the guard towards the cell. If a wall (`-1`) is encountered before reaching the cell, then there is no line of sight.
    4. If no line of sight is found from any guard to the cell, then increment the count of unguarded cells.
- Why this approach comes to mind first: It directly addresses the problem statement by checking each cell's status and its visibility from all guards.

```cpp
int countUnguardedCells(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    int unguarded = 0;
    
    // Function to check if there's a line of sight from a guard to a cell
    bool hasLineOfSight(int x1, int y1, int x2, int y2) {
        int dx = x2 - x1;
        int dy = y2 - y1;
        int steps = max(abs(dx), abs(dy));
        
        for (int i = 1; i <= steps; i++) {
            int newX = x1 + dx * i / steps;
            int newY = y1 + dy * i / steps;
            if (grid[newX][newY] == -1) return false; // Wall blocks line of sight
        }
        return true;
    }
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 0) { // Empty cell
                bool isGuarded = false;
                for (int k = 0; k < m; k++) {
                    for (int l = 0; l < n; l++) {
                        if (grid[k][l] == 1 && hasLineOfSight(k, l, i, j)) {
                            isGuarded = true;
                            break;
                        }
                    }
                    if (isGuarded) break;
                }
                if (!isGuarded) unguarded++;
            }
        }
    }
    
    return unguarded;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m^2 * n^2)$ because for each cell, we potentially check all other cells for guards and line of sight.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space to store variables like `m`, `n`, `unguarded`, and loop indices.
> - **Why these complexities occur:** The brute force approach involves nested iterations over the grid for both checking each cell and then checking for line of sight from each guard, leading to high time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Instead of checking for line of sight from each cell to all guards, we can iterate through the grid once to mark cells that are directly visible from each guard. This approach significantly reduces the number of checks needed.
- Detailed breakdown of the approach:
    1. Create a copy of the grid to mark visible cells without modifying the original grid.
    2. Iterate through the grid to find guards.
    3. For each guard, check in all four directions (up, down, left, right) and mark the first cell in each direction that is not a wall as visible.
    4. After marking all visible cells, iterate through the grid again to count the number of unmarked empty cells, which are the unguarded cells.
- Proof of optimality: This approach has a lower time complexity because it only requires a constant number of passes through the grid, rather than checking each cell against all guards.

```cpp
int countUnguardedCells(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    vector<vector<int>> visible(m, vector<int>(n, 0));
    
    // Mark visible cells from each guard
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 1) { // Guard
                // Check in all four directions
                int[] dx = {-1, 1, 0, 0};
                int[] dy = {0, 0, -1, 1};
                for (int k = 0; k < 4; k++) {
                    int x = i, y = j;
                    while (true) {
                        x += dx[k];
                        y += dy[k];
                        if (x < 0 || x >= m || y < 0 || y >= n || grid[x][y] == -1) break; // Out of bounds or wall
                        if (grid[x][y] == 0 && visible[x][y] == 0) {
                            visible[x][y] = 1; // Mark as visible
                            break;
                        }
                    }
                }
            }
        }
    }
    
    // Count unguarded cells
    int unguarded = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 0 && visible[i][j] == 0) unguarded++;
        }
    }
    
    return unguarded;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m * n)$ because we make a constant number of passes through the grid.
> - **Space Complexity:** $O(m * n)$ for the `visible` grid.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to solve the problem, avoiding unnecessary checks by only considering the visibility from each guard once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Grid traversal, visibility checking, and optimization through reducing unnecessary checks.
- Problem-solving patterns identified: Breaking down complex problems into simpler, more manageable parts (e.g., marking visible cells separately from counting unguarded cells).
- Optimization techniques learned: Reducing the number of iterations and checks by leveraging the properties of the problem (e.g., only checking visibility from guards once).
- Similar problems to practice: Other grid-based problems involving visibility, traversal, or optimization.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases (e.g., guards or walls at the grid boundaries), or failing to mark cells as visible correctly.
- Edge cases to watch for: Grids with no guards, grids with no empty cells, or grids where all empty cells are guarded.
- Performance pitfalls: Using overly complex data structures or algorithms that increase time or space complexity unnecessarily.
- Testing considerations: Ensure to test the solution with various grid sizes, guard placements, and wall configurations to cover all edge cases.