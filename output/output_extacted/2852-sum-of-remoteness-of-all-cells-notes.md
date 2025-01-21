## Sum of Remoteness of All Cells
**Problem Link:** https://leetcode.com/problems/sum-of-remoteness-of-all-cells/description

**Problem Statement:**
- Input format: A 2D grid with `m` rows and `n` columns, where each cell can be either land (represented by 0) or water (represented by 1).
- Expected output format: The sum of remoteness of all cells, which is the sum of the minimum distance from each cell to the nearest water cell.
- Key requirements and edge cases to consider: The input grid is guaranteed to contain at least one water cell. The grid can be empty, and the number of rows and columns can vary.
- Example test cases with explanations:
  - For a grid with a single water cell, the remoteness of all land cells is the distance to that water cell.
  - For a grid with multiple water cells, the remoteness of each land cell is the minimum distance to any of the water cells.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: To calculate the remoteness of each cell, we need to find the minimum distance from each cell to the nearest water cell. This can be done by iterating over all cells and checking the distance to each water cell.
- Step-by-step breakdown of the solution:
  1. Iterate over all cells in the grid.
  2. For each cell, iterate over all water cells and calculate the Manhattan distance (L1 distance) between them.
  3. Keep track of the minimum distance found for each cell.
  4. Sum up the minimum distances for all cells to get the total remoteness.
- Why this approach comes to mind first: It's a straightforward and intuitive approach, but it's not efficient due to its high time complexity.

```cpp
int sumOfRemoteness(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    int totalRemoteness = 0;
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 0) { // Land cell
                int minDistance = INT_MAX;
                for (int x = 0; x < m; x++) {
                    for (int y = 0; y < n; y++) {
                        if (grid[x][y] == 1) { // Water cell
                            int distance = abs(x - i) + abs(y - j);
                            minDistance = min(minDistance, distance);
                        }
                    }
                }
                totalRemoteness += minDistance;
            }
        }
    }
    
    return totalRemoteness;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m^2 \cdot n^2)$, where $m$ and $n$ are the number of rows and columns in the grid, respectively. This is because we're iterating over all cells and for each cell, we're iterating over all water cells.
> - **Space Complexity:** $O(1)$, since we're not using any extra space that scales with the input size.
> - **Why these complexities occur:** The high time complexity is due to the nested loops that iterate over all cells and water cells.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of iterating over all cells and checking the distance to each water cell, we can use a breadth-first search (BFS) approach to calculate the remoteness of each cell.
- Detailed breakdown of the approach:
  1. Initialize a queue with all water cells and their distances (which are all 0).
  2. Perform BFS from each water cell, incrementing the distance as we move to adjacent cells.
  3. For each cell, keep track of the minimum distance found.
  4. Sum up the minimum distances for all cells to get the total remoteness.
- Proof of optimality: This approach is optimal because it only visits each cell once and uses a queue to efficiently explore the grid.

```cpp
int sumOfRemoteness(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    int totalRemoteness = 0;
    vector<vector<int>> distances(m, vector<int>(n, INT_MAX));
    queue<pair<int, int>> q;
    
    // Initialize queue with water cells
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 1) {
                distances[i][j] = 0;
                q.push({i, j});
            }
        }
    }
    
    // Perform BFS
    vector<int> dx = {-1, 1, 0, 0};
    vector<int> dy = {0, 0, -1, 1};
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && distances[nx][ny] > distances[x][y] + 1) {
                distances[nx][ny] = distances[x][y] + 1;
                q.push({nx, ny});
            }
        }
    }
    
    // Calculate total remoteness
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 0) {
                totalRemoteness += distances[i][j];
            }
        }
    }
    
    return totalRemoteness;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the number of rows and columns in the grid, respectively. This is because we're performing BFS from each water cell.
> - **Space Complexity:** $O(m \cdot n)$, since we're using a queue to store cells and their distances.
> - **Optimality proof:** This approach is optimal because it only visits each cell once and uses a queue to efficiently explore the grid.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS, queue data structure, and distance calculation.
- Problem-solving patterns identified: Using BFS to calculate distances in a grid.
- Optimization techniques learned: Reducing time complexity by avoiding redundant calculations.
- Similar problems to practice: Other grid-based problems that involve distance calculations or BFS.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for out-of-bounds cells or not handling edge cases correctly.
- Edge cases to watch for: Empty grids, grids with no water cells, or grids with a single water cell.
- Performance pitfalls: Using a brute force approach with high time complexity.
- Testing considerations: Test the solution with different grid sizes, water cell distributions, and edge cases.