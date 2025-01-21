## Collecting Chocolates
**Problem Link:** https://leetcode.com/problems/collecting-chocolates/description

**Problem Statement:**
- Input format and constraints: Given a grid of size `m x n`, where each cell contains a non-negative integer representing the number of chocolates in that cell. You are also given a list of `k` dirty cells, represented as `(x, y)` coordinates. Your goal is to collect all the chocolates from the grid, but you must start from a dirty cell and end at another dirty cell. The path you take can only move horizontally or vertically.
- Expected output format: Return the maximum number of chocolates you can collect.
- Key requirements and edge cases to consider: The grid may contain obstacles (represented by `-1`), and you cannot move through them. You must start and end at a dirty cell, and you can only move horizontally or vertically.
- Example test cases with explanations:
  - Example 1:
    - Input: `grid = [[1,0,1],[0,5,0],[2,0,1]], dirty = [[0,0],[2,2]]`
    - Output: `9`
    - Explanation: Start at `(0, 0)` and move to `(0, 1)`, then to `(1, 1)`, then to `(2, 1)`, and finally to `(2, 2)`. Collect a total of `1 + 5 + 2 = 8` chocolates.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can try all possible paths from each dirty cell to every other dirty cell, collecting chocolates along the way.
- Step-by-step breakdown of the solution:
  1. Iterate over each dirty cell as the starting point.
  2. For each starting point, iterate over each other dirty cell as the ending point.
  3. For each pair of starting and ending points, use a depth-first search (DFS) to explore all possible paths between them.
  4. During the DFS, collect chocolates from each cell and keep track of the maximum amount collected.
- Why this approach comes to mind first: It is a straightforward, exhaustive approach that considers all possibilities.

```cpp
#include <vector>
#include <queue>

int maxChocolates(std::vector<std::vector<int>>& grid, std::vector<std::vector<int>>& dirty) {
    int m = grid.size();
    int n = grid[0].size();
    int k = dirty.size();

    int maxChocolates = 0;

    // Iterate over each pair of dirty cells
    for (int i = 0; i < k; i++) {
        for (int j = 0; j < k; j++) {
            if (i == j) continue; // Cannot start and end at the same cell

            int chocolates = 0;
            std::queue<std::pair<int, int>> queue;
            std::vector<std::vector<bool>> visited(m, std::vector<bool>(n, false));

            queue.push({dirty[i][0], dirty[i][1]});
            visited[dirty[i][0]][dirty[i][1]] = true;

            while (!queue.empty()) {
                int x = queue.front().first;
                int y = queue.front().second;
                queue.pop();

                // Collect chocolates from the current cell
                if (grid[x][y] != -1) {
                    chocolates += grid[x][y];
                }

                // Check if we have reached the ending cell
                if (x == dirty[j][0] && y == dirty[j][1]) {
                    maxChocolates = std::max(maxChocolates, chocolates);
                }

                // Explore neighboring cells
                int dx[] = {-1, 1, 0, 0};
                int dy[] = {0, 0, -1, 1};
                for (int k = 0; k < 4; k++) {
                    int nx = x + dx[k];
                    int ny = y + dy[k];

                    if (nx >= 0 && nx < m && ny >= 0 && ny < n && !visited[nx][ny] && grid[nx][ny] != -1) {
                        queue.push({nx, ny});
                        visited[nx][ny] = true;
                    }
                }
            }
        }
    }

    return maxChocolates;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k^2 \cdot m \cdot n)$, where $k$ is the number of dirty cells, $m$ is the number of rows, and $n$ is the number of columns. This is because we iterate over each pair of dirty cells and perform a DFS for each pair.
> - **Space Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns. This is because we use a queue and a visited matrix to keep track of the cells we have visited.
> - **Why these complexities occur:** The brute force approach has high time complexity because it explores all possible paths between each pair of dirty cells. The space complexity is moderate because we only need to keep track of the cells we have visited.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a single DFS to explore all possible paths from each dirty cell, and keep track of the maximum amount of chocolates collected.
- Detailed breakdown of the approach:
  1. Iterate over each dirty cell as the starting point.
  2. For each starting point, perform a DFS to explore all possible paths.
  3. During the DFS, collect chocolates from each cell and keep track of the maximum amount collected.
  4. Use a visited matrix to avoid revisiting the same cell.
- Why further optimization is impossible: This approach has the optimal time complexity because we only need to perform a single DFS for each dirty cell.

```cpp
#include <vector>
#include <queue>

int maxChocolates(std::vector<std::vector<int>>& grid, std::vector<std::vector<int>>& dirty) {
    int m = grid.size();
    int n = grid[0].size();
    int k = dirty.size();

    int maxChocolates = 0;

    // Iterate over each dirty cell as the starting point
    for (int i = 0; i < k; i++) {
        std::vector<std::vector<bool>> visited(m, std::vector<bool>(n, false));
        std::queue<std::pair<std::pair<int, int>, int>> queue; // (x, y), chocolates

        queue.push({{dirty[i][0], dirty[i][1]}, 0});
        visited[dirty[i][0]][dirty[i][1]] = true;

        while (!queue.empty()) {
            int x = queue.front().first.first;
            int y = queue.front().first.second;
            int chocolates = queue.front().second;
            queue.pop();

            // Collect chocolates from the current cell
            if (grid[x][y] != -1) {
                chocolates += grid[x][y];
            }

            // Check if we have reached another dirty cell
            for (int j = 0; j < k; j++) {
                if (x == dirty[j][0] && y == dirty[j][1] && i != j) {
                    maxChocolates = std::max(maxChocolates, chocolates);
                }
            }

            // Explore neighboring cells
            int dx[] = {-1, 1, 0, 0};
            int dy[] = {0, 0, -1, 1};
            for (int j = 0; j < 4; j++) {
                int nx = x + dx[j];
                int ny = y + dy[j];

                if (nx >= 0 && nx < m && ny >= 0 && ny < n && !visited[nx][ny] && grid[nx][ny] != -1) {
                    queue.push({{nx, ny}, chocolates});
                    visited[nx][ny] = true;
                }
            }
        }
    }

    return maxChocolates;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k \cdot m \cdot n)$, where $k$ is the number of dirty cells, $m$ is the number of rows, and $n$ is the number of columns. This is because we perform a DFS for each dirty cell.
> - **Space Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns. This is because we use a queue and a visited matrix to keep track of the cells we have visited.
> - **Optimality proof:** This approach has the optimal time complexity because we only need to perform a single DFS for each dirty cell.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, visited matrix, and queue.
- Problem-solving patterns identified: Using a single DFS to explore all possible paths from each starting point.
- Optimization techniques learned: Avoiding revisiting the same cell using a visited matrix.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for out-of-bounds cells, not handling the case where the starting and ending cells are the same.
- Edge cases to watch for: Handling the case where there are no dirty cells, handling the case where there are no chocolates in the grid.
- Performance pitfalls: Using an inefficient data structure, such as a recursive function call stack, instead of a queue.