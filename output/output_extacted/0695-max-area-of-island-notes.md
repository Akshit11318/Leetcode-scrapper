## Max Area of Island
**Problem Link:** [https://leetcode.com/problems/max-area-of-island/description](https://leetcode.com/problems/max-area-of-island/description)

**Problem Statement:**
- Input format and constraints: The input is a 2D array `grid` of size `m x n`, where `m` and `n` are integers, and each cell `grid[i][j]` contains either 0 (water) or 1 (land).
- Expected output format: The maximum area of an island in the grid.
- Key requirements and edge cases to consider: 
  - The grid can be empty.
  - There can be multiple islands in the grid.
  - The area of an island is the number of cells with a value of 1 that are connected by edges.
- Example test cases with explanations:
  - Example 1:
    - Input: `grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]`
    - Output: `6`
    - Explanation: The maximum area of an island in the grid is 6.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves checking every possible subset of cells in the grid to see if they form a connected island.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsets of cells in the grid.
  2. For each subset, check if all cells are connected by edges.
  3. If they are connected, calculate the area of the island.
  4. Keep track of the maximum area found so far.
- Why this approach comes to mind first: This approach is straightforward and does not require any advanced techniques. However, it is inefficient and has a high time complexity.

```cpp
class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int maxArea = 0;
        int m = grid.size();
        int n = grid[0].size();
        
        // Generate all possible subsets of cells
        for (int i = 0; i < (1 << (m * n)); i++) {
            vector<vector<int>> subset(m, vector<int>(n, 0));
            int area = 0;
            for (int j = 0; j < m * n; j++) {
                if ((i & (1 << j)) != 0) {
                    int x = j / n;
                    int y = j % n;
                    subset[x][y] = 1;
                    area++;
                }
            }
            
            // Check if all cells in the subset are connected
            if (isConnected(subset, grid)) {
                maxArea = max(maxArea, area);
            }
        }
        
        return maxArea;
    }
    
    bool isConnected(vector<vector<int>>& subset, vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (subset[i][j] == 1) {
                    queue<pair<int, int>> q;
                    q.push({i, j});
                    subset[i][j] = 0;
                    
                    while (!q.empty()) {
                        int x = q.front().first;
                        int y = q.front().second;
                        q.pop();
                        
                        for (auto& dir : directions) {
                            int nx = x + dir[0];
                            int ny = y + dir[1];
                            
                            if (nx >= 0 && nx < m && ny >= 0 && ny < n && subset[nx][ny] == 1) {
                                q.push({nx, ny});
                                subset[nx][ny] = 0;
                            }
                        }
                    }
                    
                    return true;
                }
            }
        }
        
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{m \cdot n} \cdot m \cdot n)$
> - **Space Complexity:** $O(m \cdot n)$
> - **Why these complexities occur:** The brute force approach generates all possible subsets of cells, which has a time complexity of $O(2^{m \cdot n})$. For each subset, it checks if all cells are connected, which has a time complexity of $O(m \cdot n)$. The space complexity is $O(m \cdot n)$ because it needs to store the subset of cells.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a depth-first search (DFS) algorithm to find the maximum area of an island.
- Detailed breakdown of the approach:
  1. Define a function `dfs` that takes the current cell coordinates and the grid as input.
  2. In the `dfs` function, mark the current cell as visited and add its area to the total area.
  3. Recursively call the `dfs` function for all neighboring cells that are land and have not been visited.
  4. Keep track of the maximum area found so far.
- Why further optimization is impossible: This approach has a time complexity of $O(m \cdot n)$, which is optimal because it needs to visit each cell at least once.

```cpp
class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int maxArea = 0;
        int m = grid.size();
        int n = grid[0].size();
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    maxArea = max(maxArea, dfs(grid, i, j));
                }
            }
        }
        
        return maxArea;
    }
    
    int dfs(vector<vector<int>>& grid, int x, int y) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        int area = 1;
        grid[x][y] = 0;
        
        for (auto& dir : directions) {
            int nx = x + dir[0];
            int ny = y + dir[1];
            
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] == 1) {
                area += dfs(grid, nx, ny);
            }
        }
        
        return area;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$
> - **Space Complexity:** $O(m \cdot n)$
> - **Optimality proof:** This approach has a time complexity of $O(m \cdot n)$, which is optimal because it needs to visit each cell at least once. The space complexity is $O(m \cdot n)$ because it needs to store the recursive call stack.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, recursion, and optimization techniques.
- Problem-solving patterns identified: Using DFS to find the maximum area of an island.
- Optimization techniques learned: Avoiding unnecessary recursive calls and using a visited array to mark visited cells.
- Similar problems to practice: Finding the maximum area of a rectangle in a grid, finding the maximum area of a polygon in a grid.

**Mistakes to Avoid:**
- Common implementation errors: Not marking visited cells, not handling edge cases, and not optimizing the recursive function calls.
- Edge cases to watch for: Empty grid, grid with no land cells, and grid with multiple islands.
- Performance pitfalls: Using an inefficient algorithm, not optimizing the recursive function calls, and not using a visited array to mark visited cells.
- Testing considerations: Testing the function with different grid sizes, testing the function with different island shapes, and testing the function with different edge cases.