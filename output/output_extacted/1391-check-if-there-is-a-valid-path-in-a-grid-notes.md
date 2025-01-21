## Check if There is a Valid Path in a Grid

**Problem Link:** https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/description

**Problem Statement:**
- Input: `m x n` grid, where each cell can have a gate (`0`), or a wall (`1`), or empty space (`2`), and `source` and `destination` coordinates.
- Expected output: `true` if there is a valid path from the source to the destination, `false` otherwise.
- Key requirements and edge cases to consider: 
  - A valid path can only be formed by moving up, down, left, or right.
  - The path cannot pass through a wall (`1`).
  - The path can pass through empty spaces (`2`) and gates (`0`).
  - The source and destination coordinates are valid and within the grid boundaries.
- Example test cases with explanations:
  - A grid with no walls and the source and destination in the same row or column.
  - A grid with walls blocking the direct path from the source to the destination.
  - A grid with gates that allow for a valid path.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible paths from the source to the destination and check if any of them are valid.
- Step-by-step breakdown of the solution:
  1. Start at the source coordinate.
  2. Explore all possible directions (up, down, left, right) from the current cell.
  3. If the adjacent cell is within the grid boundaries and is not a wall (`1`), move to that cell.
  4. Repeat steps 2-3 until the destination is reached or all possible paths have been explored.
- Why this approach comes to mind first: It is a straightforward and intuitive approach to solving the problem, but it is not efficient for large grids.

```cpp
#include <vector>
using namespace std;

bool hasValidPath(vector<vector<int>>& grid, vector<int>& source, vector<int>& destination) {
    int m = grid.size();
    int n = grid[0].size();
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    
    function<bool(int, int)> dfs = [&](int x, int y) {
        if (x == destination[0] && y == destination[1]) return true;
        visited[x][y] = true;
        
        vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        for (auto& dir : directions) {
            int nx = x + dir.first;
            int ny = y + dir.second;
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && !visited[nx][ny] && grid[nx][ny] != 1) {
                if (dfs(nx, ny)) return true;
            }
        }
        return false;
    };
    
    return dfs(source[0], source[1]);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot 4^d)$, where $d$ is the length of the shortest path from the source to the destination, and $m$ and $n$ are the dimensions of the grid. This is because in the worst case, we explore all possible paths of length $d$.
> - **Space Complexity:** $O(m \cdot n)$, for the `visited` matrix and the recursive call stack.
> - **Why these complexities occur:** The brute force approach explores all possible paths from the source to the destination, which leads to exponential time complexity. The space complexity is due to the need to keep track of visited cells to avoid infinite loops.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a breadth-first search (BFS) algorithm to explore the grid, which is more efficient than the brute force approach.
- Detailed breakdown of the approach:
  1. Start at the source coordinate.
  2. Explore all possible directions (up, down, left, right) from the current cell using a queue.
  3. If the adjacent cell is within the grid boundaries and is not a wall (`1`), add it to the queue.
  4. Repeat steps 2-3 until the destination is reached or the queue is empty.
- Proof of optimality: BFS is guaranteed to find the shortest path to the destination if one exists, and it does so in linear time with respect to the number of cells in the grid.

```cpp
#include <vector>
#include <queue>
using namespace std;

bool hasValidPath(vector<vector<int>>& grid, vector<int>& source, vector<int>& destination) {
    int m = grid.size();
    int n = grid[0].size();
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    queue<pair<int, int>> q;
    q.push({source[0], source[1]});
    visited[source[0]][source[1]] = true;
    
    vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    while (!q.empty()) {
        auto [x, y] = q.front();
        q.pop();
        
        if (x == destination[0] && y == destination[1]) return true;
        
        for (auto& dir : directions) {
            int nx = x + dir.first;
            int ny = y + dir.second;
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && !visited[nx][ny] && grid[nx][ny] != 1) {
                q.push({nx, ny});
                visited[nx][ny] = true;
            }
        }
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the grid. This is because we visit each cell at most once.
> - **Space Complexity:** $O(m \cdot n)$, for the `visited` matrix and the queue.
> - **Optimality proof:** BFS is guaranteed to find the shortest path to the destination if one exists, and it does so in linear time with respect to the number of cells in the grid.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS, DFS, and grid traversal.
- Problem-solving patterns identified: Using BFS to find the shortest path in an unweighted graph.
- Optimization techniques learned: Avoiding unnecessary exploration using a `visited` matrix.
- Similar problems to practice: Other grid traversal problems, such as finding the shortest path in a weighted grid.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for grid boundaries, not handling edge cases, and not using a `visited` matrix to avoid infinite loops.
- Edge cases to watch for: Grids with no valid path, grids with multiple valid paths, and grids with walls blocking the direct path.
- Performance pitfalls: Using an inefficient algorithm, such as the brute force approach, for large grids.
- Testing considerations: Test the function with different grid sizes, different source and destination coordinates, and different wall configurations.