## Path with Maximum Gold
**Problem Link:** https://leetcode.com/problems/path-with-maximum-gold/description

**Problem Statement:**
- Input format and constraints: The input is a 2D grid where each cell represents the amount of gold in that cell. The grid is represented as a vector of vectors of integers. The constraints are that the grid is not empty, and the number of rows and columns are within the range of [1, 50].
- Expected output format: The output is the maximum amount of gold that can be collected.
- Key requirements and edge cases to consider: The path can only be constructed by moving down, right, or left, and each cell can only be visited once.
- Example test cases with explanations: For example, given the grid `[[0,6,0],[5,8,7],[0,9,1]]`, the maximum path with gold is `5 -> 8 -> 7 -> 9`, and the output is `24`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to try all possible paths and keep track of the maximum gold collected.
- Step-by-step breakdown of the solution: We can use a recursive function to try all possible paths. For each cell, we can move down, right, or left, and recursively call the function to try all possible paths from the new cell.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it has a high time complexity due to the recursive nature and the fact that we are trying all possible paths.

```cpp
class Solution {
public:
    int getMaximumGold(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        int maxGold = 0;
        vector<vector<bool>> visited(rows, vector<bool>(cols, false));
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] != 0) {
                    maxGold = max(maxGold, dfs(grid, i, j, visited));
                }
            }
        }
        
        return maxGold;
    }
    
    int dfs(vector<vector<int>>& grid, int i, int j, vector<vector<bool>>& visited) {
        int rows = grid.size();
        int cols = grid[0].size();
        if (i < 0 || i >= rows || j < 0 || j >= cols || visited[i][j] || grid[i][j] == 0) {
            return 0;
        }
        
        visited[i][j] = true;
        int maxGold = grid[i][j];
        maxGold = max(maxGold, grid[i][j] + dfs(grid, i + 1, j, visited));
        maxGold = max(maxGold, grid[i][j] + dfs(grid, i, j + 1, visited));
        maxGold = max(maxGold, grid[i][j] + dfs(grid, i, j - 1, visited));
        visited[i][j] = false;
        
        return maxGold;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(3^{rows \cdot cols})$ because in the worst case, we are trying all possible paths.
> - **Space Complexity:** $O(rows \cdot cols)$ because we need to store the visited cells.
> - **Why these complexities occur:** The time complexity is high because we are using a recursive function to try all possible paths, and the space complexity is due to the visited array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a depth-first search (DFS) with backtracking to try all possible paths and keep track of the maximum gold collected.
- Detailed breakdown of the approach: We start from each cell that contains gold and try all possible paths. We use a visited array to keep track of the cells that have been visited.
- Proof of optimality: This approach is optimal because we are trying all possible paths, and we are using a visited array to avoid revisiting the same cell.
- Why further optimization is impossible: This approach is already optimal because we are trying all possible paths, and we are using a visited array to avoid revisiting the same cell.

```cpp
class Solution {
public:
    int getMaximumGold(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        int maxGold = 0;
        vector<vector<bool>> visited(rows, vector<bool>(cols, false));
        vector<vector<int>> directions = {{0, 1}, {0, -1}, {1, 0}};
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] != 0) {
                    maxGold = max(maxGold, dfs(grid, i, j, visited, directions));
                }
            }
        }
        
        return maxGold;
    }
    
    int dfs(vector<vector<int>>& grid, int i, int j, vector<vector<bool>>& visited, vector<vector<int>>& directions) {
        int rows = grid.size();
        int cols = grid[0].size();
        if (i < 0 || i >= rows || j < 0 || j >= cols || visited[i][j] || grid[i][j] == 0) {
            return 0;
        }
        
        visited[i][j] = true;
        int maxGold = grid[i][j];
        for (auto& direction : directions) {
            maxGold = max(maxGold, grid[i][j] + dfs(grid, i + direction[0], j + direction[1], visited, directions));
        }
        visited[i][j] = false;
        
        return maxGold;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(3^{rows \cdot cols})$ because in the worst case, we are trying all possible paths.
> - **Space Complexity:** $O(rows \cdot cols)$ because we need to store the visited cells.
> - **Optimality proof:** This approach is optimal because we are trying all possible paths, and we are using a visited array to avoid revisiting the same cell.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-first search, backtracking, and optimization techniques.
- Problem-solving patterns identified: Using a visited array to avoid revisiting the same cell, and trying all possible paths.
- Optimization techniques learned: Using a visited array to avoid revisiting the same cell, and trying all possible paths.
- Similar problems to practice: Other problems that involve trying all possible paths, such as the "Longest Increasing Path in a Matrix" problem.

**Mistakes to Avoid:**
- Common implementation errors: Not using a visited array to avoid revisiting the same cell, and not trying all possible paths.
- Edge cases to watch for: The case where the grid is empty, and the case where the grid contains only zeros.
- Performance pitfalls: Not using a visited array to avoid revisiting the same cell, and not trying all possible paths.
- Testing considerations: Testing the function with different inputs, including edge cases, to ensure that it works correctly.