## Minimum Time to Visit a Cell in a Grid
**Problem Link:** https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/description

**Problem Statement:**
- Input format: You are given a grid of size `m x n` and a starting position `(x, y)` at time `0`.
- Constraints: The grid is empty, and you can move up, down, left, or right from any cell to an adjacent cell.
- Expected output format: The minimum time required to visit each cell in the grid.
- Key requirements and edge cases to consider: 
  - You must visit each cell exactly once.
  - You can only move to an adjacent cell (up, down, left, or right).
  - The starting position is given as `(x, y)` at time `0`.
- Example test cases with explanations:
  - If the grid is `[[1, 2], [3, 4]]` and the starting position is `(0, 0)`, the minimum time to visit each cell would be `0` for the first cell, `1` for the second cell, `2` for the third cell, and `3` for the fourth cell.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: One possible approach is to try all possible paths and calculate the time required to visit each cell for each path.
- Step-by-step breakdown of the solution:
  1. Generate all possible paths from the starting position to all other cells.
  2. For each path, calculate the time required to visit each cell.
  3. Keep track of the minimum time required to visit each cell.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it has a high time complexity due to the number of possible paths.

```cpp
#include <vector>
#include <queue>
using namespace std;

int minTimeToVisitCell(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    vector<vector<int>> times(m, vector<int>(n, INT_MAX));
    queue<pair<int, int>> q;
    q.push({0, 0});
    times[0][0] = 0;
    visited[0][0] = true;

    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        // Check all adjacent cells
        for (int dx = -1; dx <= 1; dx++) {
            for (int dy = -1; dy <= 1; dy++) {
                if (abs(dx) + abs(dy) != 1) continue; // Only consider horizontal and vertical moves
                int nx = x + dx;
                int ny = y + dy;

                // Check if the adjacent cell is within the grid boundaries
                if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;

                // If the adjacent cell has not been visited before, mark it as visited and update its time
                if (!visited[nx][ny]) {
                    visited[nx][ny] = true;
                    times[nx][ny] = times[x][y] + 1;
                    q.push({nx, ny});
                }
            }
        }
    }

    int maxTime = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            maxTime = max(maxTime, times[i][j]);
        }
    }

    return maxTime;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns in the grid, because we visit each cell once.
> - **Space Complexity:** $O(m \cdot n)$, because we use a queue to store the cells to be visited and a 2D array to store the times.
> - **Why these complexities occur:** The time complexity is linear because we visit each cell once, and the space complexity is also linear because we store the times for each cell.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is to use a breadth-first search (BFS) algorithm to visit all cells in the grid.
- Detailed breakdown of the approach:
  1. Start from the given position `(x, y)` at time `0`.
  2. Use a queue to store the cells to be visited, and a 2D array to store the times.
  3. For each cell, check all its adjacent cells and update their times if they have not been visited before.
- Proof of optimality: This approach is optimal because it visits each cell exactly once and uses the minimum time required to visit each cell.

```cpp
#include <vector>
#include <queue>
using namespace std;

int minTimeToVisitCell(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    vector<vector<int>> times(m, vector<int>(n, INT_MAX));
    queue<pair<int, int>> q;
    q.push({0, 0});
    times[0][0] = 0;
    visited[0][0] = true;

    int dx[] = {-1, 1, 0, 0};
    int dy[] = {0, 0, -1, 1};

    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;

            if (!visited[nx][ny]) {
                visited[nx][ny] = true;
                times[nx][ny] = times[x][y] + 1;
                q.push({nx, ny});
            }
        }
    }

    int maxTime = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            maxTime = max(maxTime, times[i][j]);
        }
    }

    return maxTime;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns in the grid, because we visit each cell once.
> - **Space Complexity:** $O(m \cdot n)$, because we use a queue to store the cells to be visited and a 2D array to store the times.
> - **Optimality proof:** This approach is optimal because it visits each cell exactly once and uses the minimum time required to visit each cell.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS, queue, and time complexity analysis.
- Problem-solving patterns identified: Using a queue to store cells to be visited and a 2D array to store times.
- Optimization techniques learned: Using a BFS algorithm to visit all cells in the grid.
- Similar problems to practice: Other problems that involve visiting all cells in a grid or matrix.

**Mistakes to Avoid:**
- Common implementation errors: Not checking the boundaries of the grid, not updating the times correctly.
- Edge cases to watch for: The starting position is at the edge of the grid, the grid is empty.
- Performance pitfalls: Using a recursive approach instead of an iterative approach.
- Testing considerations: Test the code with different grid sizes and starting positions.