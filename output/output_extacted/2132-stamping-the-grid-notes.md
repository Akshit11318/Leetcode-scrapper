## Stamping the Grid
**Problem Link:** https://leetcode.com/problems/stamping-the-grid/description

**Problem Statement:**
- Input: A 2D grid `grid` consisting of integers, and an integer `stamp`.
- Constraints: The grid size is `m x n`, where `1 <= m, n <= 10^5`. The stamp size is `3 x 3`.
- Expected Output: A boolean indicating whether it's possible to stamp the grid using the given stamp to make all numbers in the grid equal to `stamp`.
- Key Requirements:
  - The stamp can only be applied to the grid if it can cover a `3 x 3` sub-grid.
  - The stamp can only be applied if all numbers in the covered sub-grid are not equal to `stamp`.
  - The stamp can only be applied to the grid if all numbers in the covered sub-grid are changed to `stamp` after application.
- Edge Cases:
  - If the grid is already filled with `stamp`, return `true`.
  - If it's impossible to fill the grid with `stamp`, return `false`.

**Example Test Cases:**
- Example 1:
  - Input: `grid = [[1,1,1],[1,1,1],[1,1,1]]`, `stamp = 0`
  - Output: `false`
- Example 2:
  - Input: `grid = [[1,0,0],[1,0,0],[1,0,0]]`, `stamp = 0`
  - Output: `true`

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves applying the stamp to every possible `3 x 3` sub-grid in the `m x n` grid and checking if all numbers in the sub-grid are not equal to `stamp`.
- If the sub-grid can be stamped, apply the stamp and change all numbers in the sub-grid to `stamp`.
- Repeat this process until no more stamps can be applied or all numbers in the grid are equal to `stamp`.
- Why this approach comes to mind first: It's the most straightforward way to solve the problem by trying all possible stamp applications.

```cpp
bool possibleToStamp(vector<vector<int>>& grid, int stamp) {
    int m = grid.size(), n = grid[0].size();
    bool changed = true;
    while (changed) {
        changed = false;
        for (int i = 0; i < m - 2; i++) {
            for (int j = 0; j < n - 2; j++) {
                bool canStamp = true;
                for (int x = 0; x < 3; x++) {
                    for (int y = 0; y < 3; y++) {
                        if (grid[i + x][j + y] == stamp) {
                            canStamp = false;
                            break;
                        }
                    }
                    if (!canStamp) break;
                }
                if (canStamp) {
                    for (int x = 0; x < 3; x++) {
                        for (int y = 0; y < 3; y++) {
                            grid[i + x][j + y] = stamp;
                        }
                    }
                    changed = true;
                }
            }
        }
    }
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] != stamp) return false;
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot 3 \cdot 3 \cdot k)$, where $k$ is the number of times the stamp can be applied. This is because in the worst case, we have to check every `3 x 3` sub-grid in the `m x n` grid, and apply the stamp if possible.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the variables.
> - **Why these complexities occur:** These complexities occur because we are using a brute force approach that checks every possible `3 x 3` sub-grid in the `m x n` grid.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a `BFS` (Breadth-First Search) approach to apply the stamp to the grid.
- We start by initializing a queue with all the positions in the grid where the stamp can be applied.
- Then, we enter a loop where we dequeue a position, apply the stamp to the corresponding `3 x 3` sub-grid, and enqueue all the positions that become eligible for stamping after the application.
- We repeat this process until the queue is empty, which means that no more stamps can be applied.
- Why further optimization is impossible: This approach is optimal because it ensures that we apply the stamp to the grid in the minimum number of steps possible.

```cpp
bool possibleToStamp(vector<vector<int>>& grid, int stamp) {
    int m = grid.size(), n = grid[0].size();
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    queue<pair<int, int>> q;
    for (int i = 0; i < m - 2; i++) {
        for (int j = 0; j < n - 2; j++) {
            bool canStamp = true;
            for (int x = 0; x < 3; x++) {
                for (int y = 0; y < 3; y++) {
                    if (grid[i + x][j + y] == stamp) {
                        canStamp = false;
                        break;
                    }
                }
                if (!canStamp) break;
            }
            if (canStamp) {
                q.push({i, j});
                visited[i][j] = true;
            }
        }
    }
    while (!q.empty()) {
        int x = q.front().first, y = q.front().second;
        q.pop();
        for (int i = x; i < x + 3; i++) {
            for (int j = y; j < y + 3; j++) {
                grid[i][j] = stamp;
            }
        }
        for (int i = max(0, x - 2); i <= min(m - 3, x + 2); i++) {
            for (int j = max(0, y - 2); j <= min(n - 3, y + 2); j++) {
                if (!visited[i][j]) {
                    bool canStamp = true;
                    for (int dx = 0; dx < 3; dx++) {
                        for (int dy = 0; dy < 3; dy++) {
                            if (grid[i + dx][j + dy] == stamp) {
                                canStamp = false;
                                break;
                            }
                        }
                        if (!canStamp) break;
                    }
                    if (canStamp) {
                        q.push({i, j});
                        visited[i][j] = true;
                    }
                }
            }
        }
    }
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] != stamp) return false;
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot 3 \cdot 3 \cdot k)$, where $k$ is the number of times the stamp can be applied. This is because in the worst case, we have to check every `3 x 3` sub-grid in the `m x n` grid, and apply the stamp if possible.
> - **Space Complexity:** $O(m \cdot n)$, because we use a queue to store the positions that become eligible for stamping after the application.
> - **Optimality proof:** This approach is optimal because it ensures that we apply the stamp to the grid in the minimum number of steps possible.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: `BFS`, stamping the grid.
- Problem-solving patterns identified: using a queue to store the positions that become eligible for stamping after the application.
- Optimization techniques learned: using a `BFS` approach to apply the stamp to the grid in the minimum number of steps possible.
- Similar problems to practice: problems that involve applying a stamp to a grid, such as [Problem Link](https://leetcode.com/problems/stamping-the-grid/description).

**Mistakes to Avoid:**
- Common implementation errors: not checking if a position is eligible for stamping before applying the stamp.
- Edge cases to watch for: the grid is already filled with `stamp`, or it's impossible to fill the grid with `stamp`.
- Performance pitfalls: using a brute force approach that checks every possible `3 x 3` sub-grid in the `m x n` grid.
- Testing considerations: testing the function with different inputs, such as a grid that is already filled with `stamp`, or a grid that cannot be filled with `stamp`.