## As Far From Land as Possible

**Problem Link:** https://leetcode.com/problems/as-far-from-land-as-possible/description

**Problem Statement:**
- Input format and constraints: Given an `n x m` grid, where each cell can have one of two values: `0` (water) or `1` (land). 
- Expected output format: The task is to find the cell that is farthest from any land cell, i.e., the cell with the maximum distance from any land cell. 
- Key requirements and edge cases to consider: If there are multiple cells with the same maximum distance, return any one of them. 
- Example test cases with explanations: For example, given the grid `[[1,0,1],[0,0,0],[1,0,1]]`, the output should be `[1, 1]`, which is the cell at row `1` and column `1`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to calculate the distance from each water cell to the nearest land cell. 
- Step-by-step breakdown of the solution: 
    1. Iterate over each cell in the grid.
    2. If the cell is a water cell, calculate its distance to the nearest land cell by iterating over all land cells and finding the minimum distance.
    3. Keep track of the water cell with the maximum distance to any land cell.
- Why this approach comes to mind first: This approach is straightforward and directly addresses the problem statement.

```cpp
#include <vector>
#include <climits>

std::vector<int> maxDistance(std::vector<std::vector<int>>& grid) {
    int n = grid.size();
    int m = grid[0].size();
    std::vector<int> maxDistCell = {-1, -1};
    int maxDist = 0;
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == 0) {
                int minDist = INT_MAX;
                for (int x = 0; x < n; x++) {
                    for (int y = 0; y < m; y++) {
                        if (grid[x][y] == 1) {
                            int dist = abs(x - i) + abs(y - j);
                            minDist = std::min(minDist, dist);
                        }
                    }
                }
                if (minDist > maxDist) {
                    maxDist = minDist;
                    maxDistCell = {i, j};
                }
            }
        }
    }
    return maxDistCell;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m^2)$, where $n$ is the number of rows and $m$ is the number of columns in the grid. This is because for each cell, we potentially iterate over all other cells to find the nearest land cell.
> - **Space Complexity:** $O(1)$, not including the input grid, as we only use a constant amount of space to store the maximum distance and the corresponding cell coordinates.
> - **Why these complexities occur:** The brute force approach has high time complexity due to the nested iterations over the grid for each cell.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a **Breadth-First Search (BFS)** approach, starting from all land cells simultaneously. This way, we can efficiently find the distance from each water cell to the nearest land cell.
- Detailed breakdown of the approach: 
    1. Initialize a queue with all land cells.
    2. Perform BFS, where at each step, we move to all adjacent (up, down, left, right) water cells and update their distance if it's less than the current distance.
    3. Keep track of the water cell with the maximum distance.
- Proof of optimality: This approach is optimal because it ensures that we visit each cell in the grid only once, resulting in a significant reduction in time complexity compared to the brute force approach.

```cpp
#include <vector>
#include <queue>

std::vector<int> maxDistance(std::vector<std::vector<int>>& grid) {
    int n = grid.size();
    int m = grid[0].size();
    std::vector<std::vector<int>> dist(n, std::vector<int>(m, -1));
    std::queue<std::pair<int, int>> q;
    
    // Initialize queue with land cells
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == 1) {
                dist[i][j] = 0;
                q.push({i, j});
            }
        }
    }
    
    int maxDist = 0;
    std::vector<int> maxDistCell = {-1, -1};
    
    // Directions for moving up, down, left, right
    std::vector<std::pair<int, int>> dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        
        for (const auto& dir : dirs) {
            int nx = x + dir.first;
            int ny = y + dir.second;
            
            if (nx >= 0 && nx < n && ny >= 0 && ny < m && dist[nx][ny] == -1) {
                dist[nx][ny] = dist[x][y] + 1;
                q.push({nx, ny});
                
                if (dist[nx][ny] > maxDist) {
                    maxDist = dist[nx][ny];
                    maxDistCell = {nx, ny};
                }
            }
        }
    }
    return maxDistCell;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of rows and $m$ is the number of columns in the grid. This is because we visit each cell at most once during the BFS.
> - **Space Complexity:** $O(n \cdot m)$, for storing the distance matrix and the queue.
> - **Optimality proof:** This approach is optimal because it ensures that we visit each cell in the grid only once, resulting in a significant reduction in time complexity compared to the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS, distance calculation, and optimization techniques.
- Problem-solving patterns identified: Using BFS to efficiently calculate distances in a grid.
- Optimization techniques learned: Reducing time complexity by avoiding redundant calculations and using efficient data structures.
- Similar problems to practice: Other grid-based problems that involve distance calculations or BFS.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases, such as cells on the grid boundaries.
- Edge cases to watch for: Grids with no land cells or no water cells.
- Performance pitfalls: Using inefficient algorithms or data structures, such as the brute force approach.
- Testing considerations: Thoroughly testing the solution with different grid sizes and configurations to ensure correctness and efficiency.