## Number of Islands
**Problem Link:** https://leetcode.com/problems/number-of-islands/description

**Problem Statement:**
- Input format: A 2D array `grid` of size `m x n`, where each cell is either `0` (water) or `1` (land).
- Constraints: `m` and `n` are integers in the range `[1, 200]`.
- Expected output format: The number of islands in the grid, where an island is a group of connected land cells (horizontally or vertically).
- Key requirements and edge cases to consider: 
  - Handling empty grids or grids with no land cells.
  - Identifying and counting separate islands correctly.
- Example test cases with explanations:
  - A grid with a single island: `[[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]]`.
  - A grid with multiple islands: `[[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through each cell in the grid and perform a depth-first search (DFS) or breadth-first search (BFS) to find all connected land cells.
- Step-by-step breakdown of the solution:
  1. Iterate through each cell in the grid.
  2. If a land cell is found, perform DFS or BFS to mark all connected land cells as visited.
  3. Increment the island count each time a new group of connected land cells is found.
- Why this approach comes to mind first: It's a straightforward way to ensure that all connected land cells are identified and counted correctly.

```cpp
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty() || grid[0].empty()) return 0;
        
        int m = grid.size();
        int n = grid[0].size();
        int count = 0;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    dfs(grid, i, j);
                    count++;
                }
            }
        }
        
        return count;
    }
    
    void dfs(vector<vector<char>>& grid, int i, int j) {
        if (i < 0 || j < 0 || i >= grid.size() || j >= grid[0].size() || grid[i][j] != '1') return;
        
        grid[i][j] = '0'; // Mark as visited
        
        dfs(grid, i - 1, j); // Up
        dfs(grid, i + 1, j); // Down
        dfs(grid, i, j - 1); // Left
        dfs(grid, i, j + 1); // Right
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the grid. This is because in the worst case, we might need to visit every cell in the grid.
> - **Space Complexity:** $O(m \cdot n)$ in the worst case, due to the recursive call stack for DFS.
> - **Why these complexities occur:** The time complexity is due to the iteration over the grid and the potential DFS from each land cell. The space complexity is due to the recursive call stack used by DFS.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal approach is essentially the same as the brute force approach for this problem, as we must visit each cell at least once to determine if it's part of an island or not.
- Detailed breakdown of the approach: The provided brute force approach is already optimal because it visits each cell exactly once and uses DFS to efficiently mark connected land cells as visited.
- Proof of optimality: This approach is optimal because it achieves a time complexity of $O(m \cdot n)$, which is the minimum required to examine every cell in the grid at least once.

```cpp
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty() || grid[0].empty()) return 0;
        
        int m = grid.size();
        int n = grid[0].size();
        int count = 0;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    dfs(grid, i, j);
                    count++;
                }
            }
        }
        
        return count;
    }
    
    void dfs(vector<vector<char>>& grid, int i, int j) {
        if (i < 0 || j < 0 || i >= grid.size() || j >= grid[0].size() || grid[i][j] != '1') return;
        
        grid[i][j] = '0'; // Mark as visited
        
        dfs(grid, i - 1, j); // Up
        dfs(grid, i + 1, j); // Down
        dfs(grid, i, j - 1); // Left
        dfs(grid, i, j + 1); // Right
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the grid.
> - **Space Complexity:** $O(m \cdot n)$ in the worst case, due to the recursive call stack for DFS.
> - **Optimality proof:** This is the optimal solution because it achieves the minimum time complexity required to visit each cell in the grid.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, iteration over a grid, marking visited cells.
- Problem-solving patterns identified: The importance of iterating over all elements in a grid, using DFS or BFS for connected component problems.
- Optimization techniques learned: Ensuring that each cell is visited exactly once to minimize time complexity.
- Similar problems to practice: Other connected component problems, such as finding the number of connected components in a graph.

**Mistakes to Avoid:**
- Common implementation errors: Not marking visited cells correctly, not handling edge cases (like empty grids).
- Edge cases to watch for: Grids with no land cells, grids with a single island, grids with multiple islands.
- Performance pitfalls: Using an inefficient algorithm that visits cells multiple times unnecessarily.
- Testing considerations: Ensure to test with various grid sizes, including edge cases like empty grids or grids with a single cell.