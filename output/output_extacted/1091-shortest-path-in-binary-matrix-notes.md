## Shortest Path in Binary Matrix
**Problem Link:** https://leetcode.com/problems/shortest-path-in-binary-matrix/description

**Problem Statement:**
- Input format: A binary matrix `grid` where `grid[i][j]` is either 0 or 1.
- Constraints: The grid is a square matrix with dimensions $n \times n$, where $1 \leq n \leq 100$. The top-left cell is at position $(0, 0)$, and the bottom-right cell is at position $(n - 1, n - 1)$.
- Expected output format: The length of the shortest path from the top-left cell to the bottom-right cell if it exists, otherwise return -1.
- Key requirements and edge cases to consider: The path can only be constructed out of cells that have a value of 0, and only if there is a path from the top-left cell to the bottom-right cell.
- Example test cases with explanations:
  - `grid = [[0,1],[1,0]]` returns `2` because the shortest path is from `(0,0)` to `(0,1)` to `(1,1)`.
  - `grid = [[0,0,0],[1,1,0],[1,1,0]]` returns `4` because the shortest path is from `(0,0)` to `(1,0)` to `(1,1)` to `(2,1)` to `(2,2)`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward approach is to try all possible paths from the top-left cell to the bottom-right cell and keep track of the shortest one.
- Step-by-step breakdown of the solution:
  1. Define a function to check if a cell is valid (within the grid boundaries and has a value of 0).
  2. Use a depth-first search (DFS) algorithm to explore all possible paths.
  3. Keep track of the current path length and update the shortest path length if a shorter path is found.
- Why this approach comes to mind first: It's the most intuitive way to solve the problem, as it tries all possible solutions.

```cpp
#include <vector>
using namespace std;

int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
    int n = grid.size();
    vector<pair<int, int>> directions = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};
    vector<vector<bool>> visited(n, vector<bool>(n, false));
    
    int dfs(int x, int y, int pathLength) {
        if (x < 0 || x >= n || y < 0 || y >= n || grid[x][y] == 1 || visited[x][y]) {
            return INT_MAX;
        }
        if (x == n - 1 && y == n - 1) {
            return pathLength;
        }
        visited[x][y] = true;
        int shortest = INT_MAX;
        for (auto& dir : directions) {
            shortest = min(shortest, dfs(x + dir.first, y + dir.second, pathLength + 1));
        }
        visited[x][y] = false;
        return shortest;
    }
    
    int shortest = dfs(0, 0, 1);
    return shortest == INT_MAX ? -1 : shortest;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(8^{n^2})$ because in the worst case, we might have to explore all possible paths, and there are $8^{n^2}$ possible paths.
> - **Space Complexity:** $O(n^2)$ because we need to store the visited cells.
> - **Why these complexities occur:** The brute force approach tries all possible paths, resulting in exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a breadth-first search (BFS) algorithm to explore all possible paths level by level, which guarantees that we find the shortest path first.
- Detailed breakdown of the approach:
  1. Define a function to check if a cell is valid (within the grid boundaries and has a value of 0).
  2. Use a BFS algorithm to explore all possible paths level by level.
  3. Keep track of the current path length and return it as soon as we reach the bottom-right cell.
- Why further optimization is impossible: BFS guarantees that we find the shortest path first, so we can't do better than this.

```cpp
#include <vector>
#include <queue>
using namespace std;

int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
    int n = grid.size();
    vector<pair<int, int>> directions = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};
    vector<vector<bool>> visited(n, vector<bool>(n, false));
    queue<pair<pair<int, int>, int>> q;
    
    if (grid[0][0] == 0) {
        q.push({{0, 0}, 1});
        visited[0][0] = true;
    }
    
    while (!q.empty()) {
        auto [x, y] = q.front().first;
        int pathLength = q.front().second;
        q.pop();
        
        if (x == n - 1 && y == n - 1) {
            return pathLength;
        }
        
        for (auto& dir : directions) {
            int newX = x + dir.first;
            int newY = y + dir.second;
            
            if (newX >= 0 && newX < n && newY >= 0 && newY < n && grid[newX][newY] == 0 && !visited[newX][newY]) {
                q.push({{newX, newY}, pathLength + 1});
                visited[newX][newY] = true;
            }
        }
    }
    
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ because in the worst case, we might have to explore all cells in the grid.
> - **Space Complexity:** $O(n^2)$ because we need to store the visited cells and the queue.
> - **Optimality proof:** BFS guarantees that we find the shortest path first, so we can't do better than this.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS, DFS, and path finding.
- Problem-solving patterns identified: Using BFS to find the shortest path in an unweighted graph.
- Optimization techniques learned: Using a queue to explore all possible paths level by level.
- Similar problems to practice: Other path finding problems, such as finding the shortest path in a weighted graph.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to check if a cell is valid before exploring it.
- Edge cases to watch for: Handling the case where the top-left cell or the bottom-right cell is blocked.
- Performance pitfalls: Using a DFS algorithm instead of a BFS algorithm, which can result in exponential time complexity.
- Testing considerations: Testing the function with different inputs, including edge cases and large inputs.