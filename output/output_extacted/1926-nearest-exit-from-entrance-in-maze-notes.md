## Nearest Exit from Entrance in Maze
**Problem Link:** https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/description

**Problem Statement:**
- Input: A 2D grid `maze` and a starting point `entrance`.
- Constraints: The maze is represented as a grid of `+`, `-`, `|`, and empty spaces. The entrance is a position on the boundary of the maze.
- Expected Output: The minimum number of steps to reach an exit from the entrance.
- Key Requirements: The maze may contain obstacles, and we can only move horizontally or vertically. An exit is any position on the boundary of the maze that is not the entrance.
- Example Test Cases:
  - `maze = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", ""]], entrance = [1, 0]`
  - `maze = [["+", "+", "+"], [".", "."], ["+", "+", ""]], entrance = [0, 1]`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: We can use a depth-first search (DFS) to explore all possible paths from the entrance.
- Step-by-step breakdown of the solution:
  1. Start at the entrance and mark it as visited.
  2. Explore all neighboring cells that are not obstacles and have not been visited.
  3. For each neighboring cell, recursively call the DFS function.
  4. If we reach a cell that is on the boundary of the maze and is not the entrance, return the number of steps taken.
- Why this approach comes to mind first: It's a straightforward way to explore all possible paths in the maze.

```cpp
#include <vector>
using namespace std;

int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
    int m = maze.size();
    int n = maze[0].size();
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    int minSteps = INT_MAX;

    function<void(int, int, int)> dfs = [&](int x, int y, int steps) {
        if (x < 0 || x >= m || y < 0 || y >= n || maze[x][y] == '+' || visited[x][y]) return;
        if ((x == 0 || x == m - 1 || y == 0 || y == n - 1) && (x != entrance[0] || y != entrance[1])) {
            minSteps = min(minSteps, steps);
            return;
        }
        visited[x][y] = true;
        dfs(x - 1, y, steps + 1);
        dfs(x + 1, y, steps + 1);
        dfs(x, y - 1, steps + 1);
        dfs(x, y + 1, steps + 1);
        visited[x][y] = false;
    };

    dfs(entrance[0], entrance[1], 0);
    return minSteps == INT_MAX ? -1 : minSteps;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot 4^d)$, where $d$ is the maximum depth of the DFS. This is because in the worst case, we might need to explore all possible paths of length $d$.
> - **Space Complexity:** $O(m \cdot n)$, as we need to store the visited cells.
> - **Why these complexities occur:** The DFS approach explores all possible paths, which can lead to exponential time complexity in the worst case.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: We can use a breadth-first search (BFS) to find the shortest path to an exit.
- Detailed breakdown of the approach:
  1. Start at the entrance and add it to a queue.
  2. Mark the entrance as visited.
  3. While the queue is not empty, dequeue a cell and explore its neighbors.
  4. If a neighbor is on the boundary of the maze and is not the entrance, return the number of steps taken.
- Proof of optimality: BFS is guaranteed to find the shortest path to an exit, as it explores all cells at a given distance before moving on to the next distance level.

```cpp
#include <vector>
#include <queue>
using namespace std;

int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
    int m = maze.size();
    int n = maze[0].size();
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    queue<pair<int, int>> q;
    q.push({entrance[0], entrance[1]});
    visited[entrance[0]][entrance[1]] = true;
    int steps = 0;

    vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    while (!q.empty()) {
        int size = q.size();
        for (int i = 0; i < size; i++) {
            int x = q.front().first;
            int y = q.front().second;
            q.pop();
            if ((x == 0 || x == m - 1 || y == 0 || y == n - 1) && (x != entrance[0] || y != entrance[1])) return steps;
            for (auto& dir : directions) {
                int nx = x + dir.first;
                int ny = y + dir.second;
                if (nx >= 0 && nx < m && ny >= 0 && ny < n && maze[nx][ny] != '+' && !visited[nx][ny]) {
                    q.push({nx, ny});
                    visited[nx][ny] = true;
                }
            }
        }
        steps++;
    }

    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, as we visit each cell at most once.
> - **Space Complexity:** $O(m \cdot n)$, as we need to store the visited cells and the queue.
> - **Optimality proof:** BFS is guaranteed to find the shortest path to an exit, as it explores all cells at a given distance before moving on to the next distance level.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS, DFS, and shortest path finding.
- Problem-solving patterns identified: Using BFS to find the shortest path in an unweighted graph.
- Optimization techniques learned: Using a queue to keep track of cells to visit next.
- Similar problems to practice: Finding the shortest path in a weighted graph using Dijkstra's algorithm.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for boundary conditions or not marking visited cells.
- Edge cases to watch for: The entrance being on the boundary of the maze or the maze containing no exits.
- Performance pitfalls: Using a DFS instead of BFS, which can lead to exponential time complexity.
- Testing considerations: Test the code with different maze configurations and entrance points.