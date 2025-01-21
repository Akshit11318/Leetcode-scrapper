## Walls and Gates
**Problem Link:** https://leetcode.com/problems/walls-and-gates/description

**Problem Statement:**
- Input format and constraints: The input is a 2D grid `rooms` where each cell can be an integer representing the number of steps from the nearest gate (`0`), an empty room (`2147483647`), or a wall (`-1`). The grid dimensions are within the range of $1 \leq m, n \leq 2147483647$ where $m$ and $n$ are the number of rows and columns respectively.
- Expected output format: The function should modify the input grid in-place such that each cell contains the minimum number of steps from the nearest gate. If a cell is a gate, it remains `0`.
- Key requirements and edge cases to consider: All cells must be reachable from at least one gate, and there are no cycles or disconnected components that could affect the distance calculation.
- Example test cases with explanations:
  - A grid with a single gate and empty rooms should fill the rooms with distances from the gate.
  - A grid with multiple gates should fill the rooms with the minimum distance from any gate.
  - A grid with walls should not fill the walls and should correctly calculate distances around them.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each cell in the grid, perform a breadth-first search (BFS) to find the nearest gate.
- Step-by-step breakdown of the solution:
  1. Iterate over each cell in the grid.
  2. For each cell, if it is an empty room, perform a BFS to find the nearest gate.
  3. During the BFS, keep track of the distance from the starting cell.
  4. Once a gate is found, update the distance in the starting cell if it's less than the current distance.
- Why this approach comes to mind first: It's a straightforward way to solve the problem by considering each cell individually and using a standard algorithm for finding shortest paths.

```cpp
void wallsAndGates(vector<vector<int>>& rooms) {
    int m = rooms.size();
    int n = rooms[0].size();
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (rooms[i][j] == 2147483647) { // Empty room
                queue<pair<int, int>> q;
                q.push({i, j});
                int distance = 0;
                bool foundGate = false;
                
                while (!q.empty() && !foundGate) {
                    int size = q.size();
                    for (int k = 0; k < size; k++) {
                        int x = q.front().first;
                        int y = q.front().second;
                        q.pop();
                        
                        if (rooms[x][y] == 0) { // Found a gate
                            rooms[i][j] = distance;
                            foundGate = true;
                            break;
                        }
                        
                        // Explore neighbors
                        vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
                        for (auto& dir : directions) {
                            int nx = x + dir.first;
                            int ny = y + dir.second;
                            
                            if (nx >= 0 && nx < m && ny >= 0 && ny < n && rooms[nx][ny] != -1 && rooms[nx][ny] != distance) {
                                q.push({nx, ny});
                            }
                        }
                    }
                    distance++;
                }
            }
        }
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot (m + n))$ because in the worst case, each cell performs a BFS that could potentially explore the entire grid.
> - **Space Complexity:** $O(m \cdot n)$ for the queue used in BFS.
> - **Why these complexities occur:** The brute force approach is inefficient because it performs a separate BFS for each cell, leading to redundant explorations and high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of performing BFS from each empty room, start BFS from all gates simultaneously. This way, each cell is visited only once, and the distance from the nearest gate is determined in a single pass.
- Detailed breakdown of the approach:
  1. Identify all gates in the grid and add them to a queue.
  2. Perform BFS from the gates, exploring all reachable cells.
  3. For each cell visited, update its distance if it's an empty room.
- Proof of optimality: This approach ensures that each cell is visited exactly once, resulting in the minimum number of operations required to solve the problem.
- Why further optimization is impossible: The problem requires visiting each cell at least once to determine its distance from the nearest gate, making the optimal approach's time complexity of $O(m \cdot n)$ the best achievable.

```cpp
void wallsAndGates(vector<vector<int>>& rooms) {
    int m = rooms.size();
    int n = rooms[0].size();
    queue<pair<int, int>> q;
    
    // Add all gates to the queue
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (rooms[i][j] == 0) {
                q.push({i, j});
            }
        }
    }
    
    int distance = 1; // Start with distance 1 from gates
    
    while (!q.empty()) {
        int size = q.size();
        for (int k = 0; k < size; k++) {
            int x = q.front().first;
            int y = q.front().second;
            q.pop();
            
            // Explore neighbors
            vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
            for (auto& dir : directions) {
                int nx = x + dir.first;
                int ny = y + dir.second;
                
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && rooms[nx][ny] == 2147483647) {
                    rooms[nx][ny] = distance; // Update distance
                    q.push({nx, ny}); // Add to queue for further exploration
                }
            }
        }
        distance++; // Increment distance for next level of neighbors
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$ because each cell is visited at most once.
> - **Space Complexity:** $O(m \cdot n)$ for the queue in the worst case when all cells are reachable from gates.
> - **Optimality proof:** The optimal approach achieves the best possible time complexity by ensuring that each cell is visited exactly once, making it impossible to further reduce the number of operations required to solve the problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS, grid traversal, and distance calculation.
- Problem-solving patterns identified: Starting from sources (gates) instead of targets (empty rooms) can simplify the problem and reduce computational complexity.
- Optimization techniques learned: Avoiding redundant calculations and ensuring each cell is visited only once.
- Similar problems to practice: Other grid traversal problems, such as finding the shortest path in a maze or calculating distances in a graph.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases, such as cells outside the grid boundaries or cells that are not reachable from any gate.
- Edge cases to watch for: Grids with no gates, grids with all walls, and grids with a single gate.
- Performance pitfalls: Using inefficient algorithms that lead to high time complexity, such as the brute force approach.
- Testing considerations: Thoroughly testing the solution with various grid configurations, including different sizes, numbers of gates, and arrangements of walls and empty rooms.