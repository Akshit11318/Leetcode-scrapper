## Shortest Path to Get Food

**Problem Link:** https://leetcode.com/problems/shortest-path-to-get-food/description

**Problem Statement:**
- Input: A 2D grid where each cell can be one of four values:
  - `0` representing an empty cell
  - `1` representing an obstacle
  - `2` representing the food
  - `3` representing the cell the character is initially at
- Constraints: The input grid will have at least one `2` and one `3`, and the grid will be surrounded by obstacles (i.e., all cells on the border will be `1`).
- Expected Output: The minimum number of steps required to reach the food (`2`) from the character's initial position (`3`). If it's impossible to reach the food, return `-1`.
- Key Requirements and Edge Cases:
  - The character can only move up, down, left, or right.
  - The character cannot move through obstacles (`1`).
  - The character can only reach the food (`2`) if there is a path without obstacles.
- Example Test Cases:
  - Given grid: `[[1,0,0,0,0,0],[1,0,1,0,0,0],[1,0,0,0,0,0],[1,0,0,0,0,0],[1,0,0,0,0,0],[1,0,0,0,0,2],[1,0,0,0,0,0],[1,0,0,0,0,0],[1,0,0,0,0,0],[1,0,0,0,0,0],[1,0,0,0,0,0],[3,0,0,0,0,0]]`
    - Expected Output: `16`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves exploring all possible paths from the character's initial position to the food.
- This approach involves using a depth-first search (DFS) or breadth-first search (BFS) algorithm to explore all reachable cells.
- However, this brute force approach is inefficient because it does not utilize any optimization techniques and can result in redundant explorations.

```cpp
#include <vector>
#include <queue>
using namespace std;

int getFood(vector<vector<int>>& grid) {
    int rows = grid.size();
    int cols = grid[0].size();
    int startX, startY;
    int foodX, foodY;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (grid[i][j] == 3) {
                startX = i;
                startY = j;
            } else if (grid[i][j] == 2) {
                foodX = i;
                foodY = j;
            }
        }
    }

    queue<pair<int, int>> q;
    q.push({startX, startY});
    vector<vector<bool>> visited(rows, vector<bool>(cols, false));
    visited[startX][startY] = true;
    int steps = 0;
    vector<int> dx = {-1, 1, 0, 0};
    vector<int> dy = {0, 0, -1, 1};
    while (!q.empty()) {
        int size = q.size();
        for (int i = 0; i < size; i++) {
            auto [x, y] = q.front();
            q.pop();
            if (x == foodX && y == foodY) return steps;
            for (int j = 0; j < 4; j++) {
                int nx = x + dx[j];
                int ny = y + dy[j];
                if (nx >= 0 && nx < rows && ny >= 0 && ny < cols && grid[nx][ny] != 1 && !visited[nx][ny]) {
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
> - **Time Complexity:** $O(R \cdot C)$ where $R$ is the number of rows and $C$ is the number of columns in the grid, because in the worst case, we might need to visit every cell.
> - **Space Complexity:** $O(R \cdot C)$ due to the `visited` matrix and the queue.
> - **Why these complexities occur:** The brute force approach explores all possible paths without any optimization, resulting in high time and space complexities.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight to the optimal solution is using BFS to explore all reachable cells level by level.
- This approach ensures that we find the shortest path to the food as soon as possible.
- We start from the character's initial position and explore all its neighbors, then their neighbors, and so on, until we find the food or exhaust all reachable cells.

```cpp
#include <vector>
#include <queue>
using namespace std;

int getFood(vector<vector<int>>& grid) {
    int rows = grid.size();
    int cols = grid[0].size();
    int startX, startY;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (grid[i][j] == 3) {
                startX = i;
                startY = j;
            }
        }
    }

    queue<pair<int, int>> q;
    q.push({startX, startY});
    vector<vector<bool>> visited(rows, vector<bool>(cols, false));
    visited[startX][startY] = true;
    int steps = 0;
    vector<int> dx = {-1, 1, 0, 0};
    vector<int> dy = {0, 0, -1, 1};
    while (!q.empty()) {
        int size = q.size();
        for (int i = 0; i < size; i++) {
            auto [x, y] = q.front();
            q.pop();
            if (grid[x][y] == 2) return steps;
            for (int j = 0; j < 4; j++) {
                int nx = x + dx[j];
                int ny = y + dy[j];
                if (nx >= 0 && nx < rows && ny >= 0 && ny < cols && grid[nx][ny] != 1 && !visited[nx][ny]) {
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
> - **Time Complexity:** $O(R \cdot C)$ where $R$ is the number of rows and $C$ is the number of columns in the grid.
> - **Space Complexity:** $O(R \cdot C)$ due to the `visited` matrix and the queue.
> - **Optimality proof:** This approach is optimal because it explores all reachable cells level by level, ensuring that we find the shortest path to the food as soon as possible.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS, grid traversal, and shortest path finding.
- Problem-solving patterns identified: exploring all reachable cells level by level to find the shortest path.
- Optimization techniques learned: using BFS to avoid redundant explorations and find the shortest path as soon as possible.
- Similar problems to practice: other grid traversal and shortest path finding problems.

**Mistakes to Avoid:**
- Common implementation errors: not checking for out-of-bounds cells or not marking visited cells correctly.
- Edge cases to watch for: handling the case where the food is not reachable.
- Performance pitfalls: using a brute force approach that explores all possible paths without optimization.
- Testing considerations: testing the solution with different grid sizes and configurations to ensure correctness and efficiency.