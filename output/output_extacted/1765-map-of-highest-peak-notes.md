## Map of Highest Peak

**Problem Link:** [https://leetcode.com/problems/map-of-highest-peak/description](https://leetcode.com/problems/map-of-highest-peak/description)

**Problem Statement:**
- Input format and constraints: The input is a 2D grid `isWater` of size `m x n`, where `isWater[i][j]` is `1` if the cell is water and `0` otherwise. The task is to return a new 2D grid `heights` of the same size, where `heights[i][j]` represents the highest peak's height that the water at cell `(i, j)` can flow to. If the cell is water, the height is `0`.
- Expected output format: A 2D grid `heights` of size `m x n`, where each cell represents the height of the highest peak that the water at the corresponding cell in the input grid can flow to.
- Key requirements and edge cases to consider: The input grid can contain water cells (`1`) and land cells (`0`). The height of a cell is determined by the number of steps it takes to reach the nearest water cell.
- Example test cases with explanations: 
    - For the input `isWater = [[0,1],[1,0]]`, the output should be `heights = [[1,0],[0,1]]`, because the water at cell `(0,1)` can flow to the peak at cell `(0,0)` with a height of `1`, and the water at cell `(1,0)` can flow to the peak at cell `(1,1)` with a height of `1`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over each cell in the grid and performing a breadth-first search (BFS) to find the nearest water cell.
- Step-by-step breakdown of the solution: 
    1. Iterate over each cell in the grid.
    2. If the cell is water, set its height to `0`.
    3. If the cell is land, perform a BFS to find the nearest water cell.
    4. The height of the land cell is the number of steps it takes to reach the nearest water cell.
- Why this approach comes to mind first: The brute force approach is straightforward and easy to implement, but it has a high time complexity due to the repeated BFS operations.

```cpp
using namespace std;
vector<vector<int>> highestPeak(vector<vector<int>>& isWater) {
    int m = isWater.size();
    int n = isWater[0].size();
    vector<vector<int>> heights(m, vector<int>(n, -1));
    
    // Perform BFS for each cell
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (isWater[i][j] == 1) {
                heights[i][j] = 0;
                queue<pair<int, int>> q;
                q.push({i, j});
                while (!q.empty()) {
                    int x = q.front().first;
                    int y = q.front().second;
                    q.pop();
                    vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
                    for (auto& dir : directions) {
                        int nx = x + dir.first;
                        int ny = y + dir.second;
                        if (nx >= 0 && nx < m && ny >= 0 && ny < n && heights[nx][ny] == -1) {
                            heights[nx][ny] = heights[x][y] + 1;
                            q.push({nx, ny});
                        }
                    }
                }
            }
        }
    }
    return heights;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot (m + n))$ because in the worst case, we perform a BFS for each cell, and each BFS operation can take up to $O(m + n)$ time.
> - **Space Complexity:** $O(m \cdot n)$ because we need to store the heights of all cells.
> - **Why these complexities occur:** The brute force approach has a high time complexity due to the repeated BFS operations, and the space complexity is linear because we need to store the heights of all cells.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of performing a BFS for each cell, we can perform a single BFS operation that starts from all water cells simultaneously.
- Detailed breakdown of the approach: 
    1. Initialize a queue with all water cells.
    2. Set the height of each water cell to `0`.
    3. Perform a BFS operation that starts from all water cells simultaneously.
    4. For each cell that is visited during the BFS, set its height to the number of steps it takes to reach the nearest water cell.
- Proof of optimality: The optimal approach has a time complexity of $O(m \cdot n)$ because we only need to visit each cell once during the BFS operation.

```cpp
using namespace std;
vector<vector<int>> highestPeak(vector<vector<int>>& isWater) {
    int m = isWater.size();
    int n = isWater[0].size();
    vector<vector<int>> heights(m, vector<int>(n, -1));
    queue<pair<int, int>> q;
    
    // Initialize queue with all water cells
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (isWater[i][j] == 1) {
                heights[i][j] = 0;
                q.push({i, j});
            }
        }
    }
    
    // Perform BFS operation
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        for (auto& dir : directions) {
            int nx = x + dir.first;
            int ny = y + dir.second;
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && heights[nx][ny] == -1) {
                heights[nx][ny] = heights[x][y] + 1;
                q.push({nx, ny});
            }
        }
    }
    return heights;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$ because we only need to visit each cell once during the BFS operation.
> - **Space Complexity:** $O(m \cdot n)$ because we need to store the heights of all cells.
> - **Optimality proof:** The optimal approach is optimal because we only need to visit each cell once during the BFS operation, and we use a queue to keep track of the cells to visit next.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS, queue data structure.
- Problem-solving patterns identified: Using a queue to perform a BFS operation.
- Optimization techniques learned: Reducing the number of BFS operations by starting from all water cells simultaneously.
- Similar problems to practice: Problems that involve performing a BFS operation, such as finding the shortest path between two nodes in a graph.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize the queue with all water cells, or forgetting to set the height of each water cell to `0`.
- Edge cases to watch for: Cells that are on the boundary of the grid, or cells that are not reachable from any water cell.
- Performance pitfalls: Using a brute force approach that performs a BFS operation for each cell, instead of using a single BFS operation that starts from all water cells simultaneously.
- Testing considerations: Testing the implementation with different input grids, including grids with different sizes and shapes, and grids with different numbers of water cells.