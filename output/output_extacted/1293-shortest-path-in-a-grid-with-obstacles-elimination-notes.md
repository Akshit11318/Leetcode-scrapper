## Shortest Path in a Grid with Obstacles Elimination
**Problem Link:** https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/description

**Problem Statement:**
- Input format: `grid` (a 2D vector of integers), `k` (an integer representing the number of obstacles that can be eliminated)
- Constraints: `1 <= grid.length <= 100`, `1 <= grid[0].length <= 100`, `0 <= k <= 100`
- Expected output format: The length of the shortest path to the bottom-right cell from the top-left cell, or `-1` if it's impossible to reach the bottom-right cell.
- Key requirements and edge cases to consider:
  - The grid contains only `0`s (empty cells) and `1`s (obstacles).
  - The start cell is always at the top-left corner (`grid[0][0]`).
  - The end cell is always at the bottom-right corner (`grid[n-1][m-1]`).
  - The path can only be constructed by moving right or down.
- Example test cases with explanations:
  - `grid = [[0,0,0],[1,1,0],[0,0,0]]`, `k = 1` => `6`
  - `grid = [[0,1,1],[1,1,1],[0,0,0]]`, `k = 1` => `-1`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible paths from the top-left cell to the bottom-right cell, keeping track of the number of obstacles encountered.
- Step-by-step breakdown of the solution:
  1. Define a recursive function to explore all possible paths.
  2. In each recursive call, check if the current cell is an obstacle. If it is, increment the obstacle count.
  3. If the obstacle count exceeds `k`, return `-1` (or a sentinel value indicating failure).
  4. If the current cell is the bottom-right cell, return the current path length.
  5. Otherwise, recursively explore the neighboring cells (right and down).
- Why this approach comes to mind first: It's a straightforward, exhaustive search approach that considers all possible paths.

```cpp
class Solution {
public:
    int shortestPath(vector<vector<int>>& grid, int k) {
        int n = grid.size();
        int m = grid[0].size();
        vector<vector<int>> dirs = {{0, 1}, {1, 0}};
        function<int(int, int, int)> dfs = [&](int x, int y, int obstacles) {
            if (x == n - 1 && y == m - 1) return 0;
            if (obstacles > k) return INT_MAX;
            int res = INT_MAX;
            for (auto& dir : dirs) {
                int nx = x + dir[0];
                int ny = y + dir[1];
                if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                int nextObstacles = obstacles + grid[nx][ny];
                res = min(res, 1 + dfs(nx, ny, nextObstacles));
            }
            return res;
        };
        int res = dfs(0, 0, grid[0][0]);
        return res == INT_MAX ? -1 : res;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{n \cdot m} \cdot k)$, where $n$ and $m$ are the dimensions of the grid. This is because in the worst case, we might need to explore all possible paths, and each path can have up to $k$ obstacles.
> - **Space Complexity:** $O(n \cdot m)$, due to the recursive call stack.
> - **Why these complexities occur:** The brute force approach explores all possible paths, leading to exponential time complexity. The space complexity is linear due to the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use a queue-based BFS approach with a state `(x, y, obstacles)` to keep track of the current cell and the number of obstacles encountered.
- Detailed breakdown of the approach:
  1. Initialize a queue with the starting state `(0, 0, grid[0][0])`.
  2. Perform BFS, exploring the neighboring cells (right and down) for each state in the queue.
  3. When exploring a neighboring cell, increment the obstacle count if the cell is an obstacle.
  4. If the obstacle count exceeds `k`, skip this state.
  5. If the current cell is the bottom-right cell, return the current path length.
- Proof of optimality: This approach is optimal because it explores all possible paths with the minimum number of obstacles, and it uses a queue to efficiently manage the exploration process.

```cpp
class Solution {
public:
    int shortestPath(vector<vector<int>>& grid, int k) {
        int n = grid.size();
        int m = grid[0].size();
        vector<vector<int>> dirs = {{0, 1}, {1, 0}};
        queue<tuple<int, int, int>> q;
        q.emplace(0, 0, grid[0][0]);
        unordered_set<string> visited;
        int steps = 0;
        while (!q.empty()) {
            int sz = q.size();
            for (int i = 0; i < sz; i++) {
                auto [x, y, obstacles] = q.front();
                q.pop();
                if (x == n - 1 && y == m - 1) return steps;
                if (obstacles > k) continue;
                string key = to_string(x) + "," + to_string(y) + "," + to_string(obstacles);
                if (visited.count(key)) continue;
                visited.insert(key);
                for (auto& dir : dirs) {
                    int nx = x + dir[0];
                    int ny = y + dir[1];
                    if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                    q.emplace(nx, ny, obstacles + grid[nx][ny]);
                }
            }
            steps++;
        }
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$, where $n$ and $m$ are the dimensions of the grid. This is because we explore all possible states with up to `k` obstacles.
> - **Space Complexity:** $O(n \cdot m \cdot k)$, due to the queue and the visited set.
> - **Optimality proof:** This approach is optimal because it explores all possible paths with the minimum number of obstacles, and it uses a queue to efficiently manage the exploration process.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS, queue-based exploration, and state management.
- Problem-solving patterns identified: Using a queue to manage exploration, and keeping track of the minimum number of obstacles.
- Optimization techniques learned: Using a visited set to avoid redundant exploration.
- Similar problems to practice: Other grid-based problems with obstacles or constraints.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for out-of-bounds conditions, or not properly handling the obstacle count.
- Edge cases to watch for: Handling the case where the start cell is an obstacle, or where the end cell is unreachable.
- Performance pitfalls: Not using a visited set to avoid redundant exploration, or not optimizing the queue-based exploration.
- Testing considerations: Testing the implementation with different grid sizes, obstacle counts, and start/end cell positions.