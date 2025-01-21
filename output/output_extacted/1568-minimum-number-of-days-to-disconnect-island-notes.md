## Minimum Number of Days to Disconnect Island
**Problem Link:** https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/description

**Problem Statement:**
- Input format: A 2D grid `grid` representing an island, where `1` indicates land and `0` indicates water.
- Constraints: The grid contains at least one land cell, and the number of rows and columns is between 1 and 100.
- Expected output format: The minimum number of days to disconnect the island.
- Key requirements and edge cases to consider: 
    - If the island is already disconnected, return 0.
    - If the island cannot be disconnected, return -1.
- Example test cases with explanations:
    - Example 1: Given a grid with one land cell, return 0 because the island is already disconnected.
    - Example 2: Given a grid with multiple land cells that are not connected, return 0 because the island is already disconnected.
    - Example 3: Given a grid with multiple connected land cells, return the minimum number of days to disconnect the island.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of removing land cells to find the minimum number of days to disconnect the island.
- Step-by-step breakdown of the solution:
    1. Generate all possible combinations of land cells.
    2. For each combination, remove the corresponding land cells from the grid.
    3. Check if the island is disconnected by performing a depth-first search (DFS) from an arbitrary land cell.
    4. If the island is disconnected, return the number of days (i.e., the number of removed land cells).
- Why this approach comes to mind first: It's a straightforward approach that tries all possible solutions.

```cpp
class Solution {
public:
    int minDays(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        int totalLand = 0;
        
        // Count the total number of land cells
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 1) {
                    totalLand++;
                }
            }
        }
        
        // Try all possible combinations of removing land cells
        for (int i = 0; i < (1 << totalLand); i++) {
            vector<vector<int>> tempGrid = grid;
            int removedLand = 0;
            
            // Remove land cells according to the current combination
            int index = 0;
            for (int x = 0; x < rows; x++) {
                for (int y = 0; y < cols; y++) {
                    if (tempGrid[x][y] == 1) {
                        if ((i & (1 << index)) != 0) {
                            tempGrid[x][y] = 0;
                            removedLand++;
                        }
                        index++;
                    }
                }
            }
            
            // Check if the island is disconnected
            if (isDisconnected(tempGrid)) {
                return removedLand;
            }
        }
        
        return -1; // If the island cannot be disconnected
    }
    
    bool isDisconnected(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        vector<vector<bool>> visited(rows, vector<bool>(cols, false));
        
        // Perform DFS from an arbitrary land cell
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 1 && !visited[i][j]) {
                    dfs(grid, visited, i, j);
                    return false; // If we can reach all land cells, the island is connected
                }
            }
        }
        
        return true; // If we cannot reach all land cells, the island is disconnected
    }
    
    void dfs(vector<vector<int>>& grid, vector<vector<bool>>& visited, int x, int y) {
        int rows = grid.size();
        int cols = grid[0].size();
        vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        
        visited[x][y] = true;
        
        for (auto& dir : directions) {
            int newX = x + dir.first;
            int newY = y + dir.second;
            
            if (newX >= 0 && newX < rows && newY >= 0 && newY < cols && grid[newX][newY] == 1 && !visited[newX][newY]) {
                dfs(grid, visited, newX, newY);
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{n} \cdot n \cdot m)$, where $n$ is the number of land cells and $m$ is the number of cells in the grid. This is because we try all possible combinations of removing land cells and perform DFS for each combination.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of rows and $m$ is the number of columns in the grid. This is because we need to store the visited status of each cell during DFS.
> - **Why these complexities occur:** The brute force approach tries all possible combinations of removing land cells, which leads to an exponential time complexity. The space complexity is dominated by the visited status of each cell during DFS.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of trying all possible combinations of removing land cells, we can start by removing one land cell and check if the island becomes disconnected.
- Detailed breakdown of the approach:
    1. Find the first land cell and remove it.
    2. Perform DFS from an arbitrary remaining land cell to check if the island is disconnected.
    3. If the island is disconnected, return 1. Otherwise, return 2 if the island can be disconnected by removing one more land cell.
- Proof of optimality: This approach is optimal because we only need to remove at most two land cells to disconnect the island.

```cpp
class Solution {
public:
    int minDays(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        
        // Check if the island is already disconnected
        if (isDisconnected(grid)) {
            return 0;
        }
        
        // Try removing one land cell
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 1) {
                    grid[i][j] = 0;
                    
                    // Check if the island is disconnected
                    if (isDisconnected(grid)) {
                        return 1;
                    }
                    
                    grid[i][j] = 1; // Restore the grid
                }
            }
        }
        
        // If the island cannot be disconnected by removing one land cell, try removing two land cells
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 1) {
                    grid[i][j] = 0;
                    
                    for (int x = 0; x < rows; x++) {
                        for (int y = 0; y < cols; y++) {
                            if (grid[x][y] == 1) {
                                grid[x][y] = 0;
                                
                                // Check if the island is disconnected
                                if (isDisconnected(grid)) {
                                    return 2;
                                }
                                
                                grid[x][y] = 1; // Restore the grid
                            }
                        }
                    }
                    
                    grid[i][j] = 1; // Restore the grid
                }
            }
        }
        
        return -1; // If the island cannot be disconnected
    }
    
    bool isDisconnected(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        vector<vector<bool>> visited(rows, vector<bool>(cols, false));
        
        // Perform DFS from an arbitrary land cell
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 1 && !visited[i][j]) {
                    dfs(grid, visited, i, j);
                    return false; // If we can reach all land cells, the island is connected
                }
            }
        }
        
        return true; // If we cannot reach all land cells, the island is disconnected
    }
    
    void dfs(vector<vector<int>>& grid, vector<vector<bool>>& visited, int x, int y) {
        int rows = grid.size();
        int cols = grid[0].size();
        vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        
        visited[x][y] = true;
        
        for (auto& dir : directions) {
            int newX = x + dir.first;
            int newY = y + dir.second;
            
            if (newX >= 0 && newX < rows && newY >= 0 && newY < cols && grid[newX][newY] == 1 && !visited[newX][newY]) {
                dfs(grid, visited, newX, newY);
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of rows and $m$ is the number of columns in the grid. This is because we perform DFS for each land cell.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of rows and $m$ is the number of columns in the grid. This is because we need to store the visited status of each cell during DFS.
> - **Optimality proof:** This approach is optimal because we only need to remove at most two land cells to disconnect the island, and we try all possible combinations of removing one or two land cells.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, graph traversal, and optimization techniques.
- Problem-solving patterns identified: Trying all possible combinations, using DFS to check connectivity, and optimizing the solution by removing at most two land cells.
- Optimization techniques learned: Reducing the search space by trying only relevant combinations and using DFS to check connectivity.

**Mistakes to Avoid:**
- Common implementation errors: Not restoring the grid after trying a combination, not checking for edge cases, and not optimizing the solution.
- Edge cases to watch for: The island is already disconnected, the island cannot be disconnected, and the grid is empty.
- Performance pitfalls: Trying all possible combinations without optimization, not using DFS to check connectivity, and not reducing the search space.
- Testing considerations: Test the solution with different grid sizes, land cell distributions, and edge cases to ensure correctness and performance.