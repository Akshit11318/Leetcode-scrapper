## Minimum Moves to Move a Box to Their Target Location

**Problem Link:** https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/description

**Problem Statement:**
- Input format and constraints: Given a grid with dimensions `m x n`, where each cell can have one of three values: `0` (empty), `1` (wall), and `2` (target). A box is initially placed at a given position `(x, y)`. The goal is to move the box to the target location.
- Expected output format: The minimum number of moves required to move the box to the target location.
- Key requirements and edge cases to consider: The box can only be moved up, down, left, or right. The box cannot be moved through walls. If there is no possible path to the target location, return `-1`.
- Example test cases with explanations:
  - Example 1:
    - Input: `grid = [[1,0,0,0,1],[0,0,0,0,1],[0,0,2,0,1],[0,1,1,0,0]]`, `x = 0`, `y = 0`
    - Output: `6`
    - Explanation: The box needs to be moved 6 times to reach the target location.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible moves from the initial position and explore the grid recursively.
- Step-by-step breakdown of the solution:
  1. Define a recursive function to explore all possible moves from a given position.
  2. Check if the current position is the target location. If so, return the number of moves made so far.
  3. Check if the current position is a wall or has been visited before. If so, return `-1`.
  4. Explore all possible moves (up, down, left, right) from the current position and recursively call the function.
  5. Keep track of the minimum number of moves required to reach the target location.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible moves and explores the grid recursively.

```cpp
int minMovesToTarget(vector<vector<int>>& grid, int x, int y) {
    int m = grid.size();
    int n = grid[0].size();
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    int minMoves = INT_MAX;

    function<int(int, int, int)> dfs = [&](int x, int y, int moves) {
        if (x < 0 || x >= m || y < 0 || y >= n || grid[x][y] == 1 || visited[x][y]) {
            return -1;
        }
        if (grid[x][y] == 2) {
            minMoves = min(minMoves, moves);
            return moves;
        }
        visited[x][y] = true;
        int res = INT_MAX;
        res = min(res, dfs(x - 1, y, moves + 1));
        res = min(res, dfs(x + 1, y, moves + 1));
        res = min(res, dfs(x, y - 1, moves + 1));
        res = min(res, dfs(x, y + 1, moves + 1));
        visited[x][y] = false;
        return res == INT_MAX ? -1 : res;
    };

    int res = dfs(x, y, 0);
    return res == INT_MAX ? -1 : res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(4^{m \times n})$, where $m$ and $n$ are the dimensions of the grid. This is because in the worst case, we might need to explore all possible moves from each cell.
> - **Space Complexity:** $O(m \times n)$, where $m$ and $n$ are the dimensions of the grid. This is because we need to keep track of visited cells.
> - **Why these complexities occur:** The brute force approach tries all possible moves from each cell, resulting in exponential time complexity. The space complexity is due to the recursion stack and the visited array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a breadth-first search (BFS) algorithm to explore the grid level by level, starting from the initial position.
- Detailed breakdown of the approach:
  1. Define a queue to store cells to be visited, along with the number of moves required to reach each cell.
  2. Enqueue the initial position with 0 moves.
  3. Dequeue a cell and explore its neighbors (up, down, left, right).
  4. If a neighbor is the target location, return the number of moves.
  5. If a neighbor is a wall or has been visited before, skip it.
  6. Enqueue the neighbor with the updated number of moves.
- Why further optimization is impossible: The BFS algorithm explores the grid level by level, ensuring that we find the shortest path to the target location.

```cpp
int minMovesToTarget(vector<vector<int>>& grid, int x, int y) {
    int m = grid.size();
    int n = grid[0].size();
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    queue<pair<int, int>> q;
    q.push({x, y});
    visited[x][y] = true;
    int moves = 0;

    while (!q.empty()) {
        int size = q.size();
        for (int i = 0; i < size; i++) {
            auto [x, y] = q.front();
            q.pop();
            if (grid[x][y] == 2) {
                return moves;
            }
            vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
            for (auto [dx, dy] : directions) {
                int nx = x + dx;
                int ny = y + dy;
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] != 1 && !visited[nx][ny]) {
                    q.push({nx, ny});
                    visited[nx][ny] = true;
                }
            }
        }
        moves++;
    }
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \times n)$, where $m$ and $n$ are the dimensions of the grid. This is because we visit each cell at most once.
> - **Space Complexity:** $O(m \times n)$, where $m$ and $n$ are the dimensions of the grid. This is because we need to keep track of visited cells and the queue.
> - **Optimality proof:** The BFS algorithm explores the grid level by level, ensuring that we find the shortest path to the target location. This is because we visit cells in increasing order of distance from the initial position.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS algorithm, grid traversal, and shortest path finding.
- Problem-solving patterns identified: Using BFS to find the shortest path in an unweighted graph.
- Optimization techniques learned: Avoiding unnecessary exploration by using a visited array.
- Similar problems to practice: Other grid traversal problems, such as finding the shortest path in a weighted graph.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for wall cells or visited cells before exploring neighbors.
- Edge cases to watch for: Handling the case where the target location is not reachable.
- Performance pitfalls: Using a recursive approach with excessive function calls.
- Testing considerations: Testing the algorithm with different grid sizes, wall placements, and target locations.