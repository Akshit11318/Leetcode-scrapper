## Immediate Food Delivery III
**Problem Link:** https://leetcode.com/problems/immediate-food-delivery-iii/description

**Problem Statement:**
- Input format: You are given a `n x m` grid representing the map of the region, where `grid[i][j]` is either `0` or `1`. `0` represents an empty cell and `1` represents a cell with a restaurant.
- Constraints: The number of rows and columns in the grid will be between `1` and `10^5`.
- Expected output format: The function should return a `2D` array of integers, where each integer represents the minimum number of steps required to reach a restaurant from the corresponding cell.
- Key requirements and edge cases to consider: The grid may contain empty cells, and there may be multiple restaurants in the grid.
- Example test cases with explanations:
  - A grid with a single restaurant in the top-left corner and empty cells everywhere else.
  - A grid with multiple restaurants and empty cells.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over each cell in the grid and performing a breadth-first search (BFS) to find the nearest restaurant.
- Step-by-step breakdown of the solution:
  1. Iterate over each cell in the grid.
  2. For each cell, perform a BFS to find the nearest restaurant.
  3. Keep track of the minimum distance to a restaurant for each cell.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it has a high time complexity due to the repeated BFS operations.

```cpp
#include <vector>
#include <queue>
using namespace std;

vector<vector<int>> updateMatrix(vector<vector<int>>& grid) {
    int n = grid.size();
    int m = grid[0].size();
    vector<vector<int>> res(n, vector<int>(m, INT_MAX));
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == 1) {
                res[i][j] = 0;
            } else {
                queue<pair<int, int>> q;
                q.push({i, j});
                int step = 0;
                bool found = false;
                
                while (!q.empty()) {
                    int size = q.size();
                    for (int k = 0; k < size; k++) {
                        int x = q.front().first;
                        int y = q.front().second;
                        q.pop();
                        
                        if (grid[x][y] == 1) {
                            res[i][j] = step;
                            found = true;
                            break;
                        }
                        
                        if (x > 0) q.push({x - 1, y});
                        if (x < n - 1) q.push({x + 1, y});
                        if (y > 0) q.push({x, y - 1});
                        if (y < m - 1) q.push({x, y + 1});
                    }
                    
                    if (found) break;
                    step++;
                }
            }
        }
    }
    
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot (n + m))$ because in the worst case, we need to perform a BFS operation for each cell in the grid.
> - **Space Complexity:** $O(n \cdot m)$ because we need to store the minimum distance to a restaurant for each cell.
> - **Why these complexities occur:** The high time complexity occurs because we are performing a BFS operation for each cell in the grid, and the space complexity occurs because we need to store the minimum distance to a restaurant for each cell.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a BFS operation starting from all restaurants simultaneously to find the minimum distance to a restaurant for each cell.
- Detailed breakdown of the approach:
  1. Initialize a queue with all restaurants in the grid.
  2. Perform a BFS operation starting from all restaurants simultaneously.
  3. Keep track of the minimum distance to a restaurant for each cell.
- Proof of optimality: This approach is optimal because we are only performing a single BFS operation to find the minimum distance to a restaurant for all cells.

```cpp
#include <vector>
#include <queue>
using namespace std;

vector<vector<int>> updateMatrix(vector<vector<int>>& grid) {
    int n = grid.size();
    int m = grid[0].size();
    vector<vector<int>> res(n, vector<int>(m, INT_MAX));
    queue<pair<int, int>> q;
    
    // Initialize queue with all restaurants
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == 1) {
                res[i][j] = 0;
                q.push({i, j});
            }
        }
    }
    
    // Perform BFS operation starting from all restaurants
    vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    int step = 1;
    
    while (!q.empty()) {
        int size = q.size();
        
        for (int k = 0; k < size; k++) {
            int x = q.front().first;
            int y = q.front().second;
            q.pop();
            
            for (auto& dir : directions) {
                int nx = x + dir.first;
                int ny = y + dir.second;
                
                if (nx < 0 || nx >= n || ny < 0 || ny >= m || res[nx][ny] <= step) continue;
                
                res[nx][ny] = step;
                q.push({nx, ny});
            }
        }
        
        step++;
    }
    
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ because we are only performing a single BFS operation to find the minimum distance to a restaurant for all cells.
> - **Space Complexity:** $O(n \cdot m)$ because we need to store the minimum distance to a restaurant for each cell.
> - **Optimality proof:** This approach is optimal because we are only performing a single BFS operation to find the minimum distance to a restaurant for all cells.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS, queue data structure.
- Problem-solving patterns identified: Using a BFS operation to find the minimum distance to a target.
- Optimization techniques learned: Reducing the number of BFS operations by starting from all targets simultaneously.
- Similar problems to practice: Problems involving finding the minimum distance to a target in a grid or graph.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as cells outside the grid boundaries.
- Edge cases to watch for: Cells with no restaurants in the grid, multiple restaurants in the grid.
- Performance pitfalls: Performing multiple BFS operations for each cell in the grid.
- Testing considerations: Testing the function with different grid sizes, restaurant locations, and cell values.