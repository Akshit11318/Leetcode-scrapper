## Determine if a Cell is Reachable at a Given Time

**Problem Link:** https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/description

**Problem Statement:**
- Input format and constraints: Given an `m x n` grid, where each cell contains a `1` or a `0`. The `1` represents an open cell and the `0` represents a closed cell. The grid also contains a starting cell and a target cell, both represented by their coordinates `(x, y)`. The goal is to determine if it is possible to reach the target cell from the starting cell at a given time `t`.
- Expected output format: Return `true` if the target cell is reachable at the given time, otherwise return `false`.
- Key requirements and edge cases to consider: The movement is restricted to adjacent cells (up, down, left, right) and the time `t` is the number of steps taken to reach the target cell.
- Example test cases with explanations: 
    - If the grid is `[[0, 0, 0], [1, 0, 1], [0, 0, 0]]`, the starting cell is `(1, 1)`, the target cell is `(1, 2)`, and the time `t` is `2`, then the output is `false` because it takes at least 3 steps to reach the target cell from the starting cell.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves trying all possible paths from the starting cell to the target cell and checking if the target cell can be reached within the given time `t`.
- Step-by-step breakdown of the solution:
    1. Initialize a queue with the starting cell and the current time `0`.
    2. Perform a breadth-first search (BFS) to explore all adjacent cells.
    3. For each cell, check if it is the target cell and if the current time is less than or equal to `t`. If so, return `true`.
    4. If the BFS is completed and the target cell is not reached within the given time, return `false`.
- Why this approach comes to mind first: The brute force approach is often the simplest and most intuitive solution, as it involves trying all possible solutions and selecting the best one.

```cpp
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

bool isReachable(vector<vector<int>>& grid, int x, int y, int t) {
    int m = grid.size();
    int n = grid[0].size();
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    queue<pair<int, int>> q;
    q.push({x, y});
    visited[x][y] = true;
    int time = 0;

    while (!q.empty()) {
        int size = q.size();
        for (int i = 0; i < size; i++) {
            int currX = q.front().first;
            int currY = q.front().second;
            q.pop();

            if (currX == x && currY == y && time == t) {
                return true;
            }

            vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
            for (auto& dir : directions) {
                int newX = currX + dir.first;
                int newY = currY + dir.second;

                if (newX >= 0 && newX < m && newY >= 0 && newY < n && !visited[newX][newY] && grid[newX][newY] == 1) {
                    q.push({newX, newY});
                    visited[newX][newY] = true;
                }
            }
        }
        time++;
    }

    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot t)$, where $m$ and $n$ are the dimensions of the grid and $t$ is the given time. This is because in the worst case, we need to explore all cells in the grid for each time step.
> - **Space Complexity:** $O(m \cdot n)$, as we need to store the visited cells in the queue.
> - **Why these complexities occur:** The time complexity is high because we are trying all possible paths from the starting cell to the target cell, and the space complexity is due to the need to store the visited cells.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of trying all possible paths, we can use a BFS to explore the grid level by level. This way, we can stop the search as soon as we reach the target cell or the given time `t`.
- Detailed breakdown of the approach:
    1. Initialize a queue with the starting cell and the current time `0`.
    2. Perform a BFS to explore all adjacent cells.
    3. For each cell, check if it is the target cell and if the current time is less than or equal to `t`. If so, return `true`.
    4. If the BFS is completed and the target cell is not reached within the given time, return `false`.
- Why further optimization is impossible: This approach is already optimal because we are exploring the grid level by level, which ensures that we reach the target cell in the minimum time possible.

```cpp
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

bool isReachable(vector<vector<int>>& grid, int x, int y, int t) {
    int m = grid.size();
    int n = grid[0].size();
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    queue<pair<pair<int, int>, int>> q;
    q.push({{x, y}, 0});
    visited[x][y] = true;

    while (!q.empty()) {
        int currX = q.front().first.first;
        int currY = q.front().first.second;
        int time = q.front().second;
        q.pop();

        if (currX == x && currY == y && time == t) {
            return true;
        }

        if (time > t) {
            continue;
        }

        vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        for (auto& dir : directions) {
            int newX = currX + dir.first;
            int newY = currY + dir.second;

            if (newX >= 0 && newX < m && newY >= 0 && newY < n && !visited[newX][newY] && grid[newX][newY] == 1) {
                q.push({{newX, newY}, time + 1});
                visited[newX][newY] = true;
            }
        }
    }

    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot t)$, where $m$ and $n$ are the dimensions of the grid and $t$ is the given time. This is because in the worst case, we need to explore all cells in the grid for each time step.
> - **Space Complexity:** $O(m \cdot n)$, as we need to store the visited cells in the queue.
> - **Optimality proof:** This approach is optimal because we are exploring the grid level by level, which ensures that we reach the target cell in the minimum time possible.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS, queue data structure, and time complexity analysis.
- Problem-solving patterns identified: The problem can be solved by exploring the grid level by level and checking if the target cell is reached within the given time.
- Optimization techniques learned: The optimal approach uses a BFS to explore the grid level by level, which ensures that we reach the target cell in the minimum time possible.
- Similar problems to practice: Other problems that involve exploring a grid or graph and checking if a target cell is reachable within a given time.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the current cell is the target cell and if the current time is less than or equal to the given time.
- Edge cases to watch for: The grid may contain closed cells, and the target cell may not be reachable within the given time.
- Performance pitfalls: The brute force approach has a high time complexity, which can lead to performance issues for large grids.
- Testing considerations: The solution should be tested with different grid sizes, target cell locations, and given times to ensure that it works correctly in all cases.