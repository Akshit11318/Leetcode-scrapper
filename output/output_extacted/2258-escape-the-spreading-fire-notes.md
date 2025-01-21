## Escape the Spreading Fire

**Problem Link:** https://leetcode.com/problems/escape-the-spreading-fire/description

**Problem Statement:**
- Input format and constraints: Given a grid of size `m x n`, where each cell can have one of three values: `0` (empty), `1` (fire), or `2` (person). The person can move in four directions (up, down, left, right) from an empty cell to another empty cell. The fire spreads in all four directions from a cell with fire to an adjacent empty cell. The goal is to determine if the person can escape the spreading fire.
- Expected output format: Return `true` if the person can escape, and `false` otherwise.
- Key requirements and edge cases to consider:
  - The person can only move to empty cells.
  - The fire spreads to all adjacent empty cells.
  - The grid can have multiple cells with fire or person.
- Example test cases with explanations:
  - A grid with a person surrounded by fire has no escape route.
  - A grid with a person and an empty path to the boundary has an escape route.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Simulate the movement of the person and the spread of the fire at each time step.
- Step-by-step breakdown of the solution:
  1. Initialize the current state of the grid with the person's and fire's positions.
  2. At each time step, try to move the person in all four directions.
  3. If the person can move to an empty cell, update the person's position.
  4. Spread the fire to all adjacent empty cells.
  5. Repeat steps 2-4 until the person escapes or is trapped.
- Why this approach comes to mind first: It directly simulates the problem's scenario, making it easy to understand and implement.

```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

bool escape(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    queue<pair<int, int>> personQueue;
    queue<pair<int, int>> fireQueue;

    // Find the person's and fire's initial positions
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 2) {
                personQueue.push({i, j});
                visited[i][j] = true;
            } else if (grid[i][j] == 1) {
                fireQueue.push({i, j});
            }
        }
    }

    vector<int> dx = {-1, 1, 0, 0};
    vector<int> dy = {0, 0, -1, 1};

    while (!personQueue.empty()) {
        int personSize = personQueue.size();
        for (int i = 0; i < personSize; i++) {
            int x = personQueue.front().first;
            int y = personQueue.front().second;
            personQueue.pop();

            // Check if the person can escape
            if (x == 0 || x == m - 1 || y == 0 || y == n - 1) {
                return true;
            }

            // Try to move the person in all four directions
            for (int j = 0; j < 4; j++) {
                int newX = x + dx[j];
                int newY = y + dy[j];
                if (newX >= 0 && newX < m && newY >= 0 && newY < n && grid[newX][newY] == 0 && !visited[newX][newY]) {
                    personQueue.push({newX, newY});
                    visited[newX][newY] = true;
                }
            }
        }

        int fireSize = fireQueue.size();
        for (int i = 0; i < fireSize; i++) {
            int x = fireQueue.front().first;
            int y = fireQueue.front().second;
            fireQueue.pop();

            // Spread the fire in all four directions
            for (int j = 0; j < 4; j++) {
                int newX = x + dx[j];
                int newY = y + dy[j];
                if (newX >= 0 && newX < m && newY >= 0 && newY < n && grid[newX][newY] == 0) {
                    grid[newX][newY] = 1;
                    fireQueue.push({newX, newY});
                }
            }
        }
    }

    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the grid, because in the worst case, we need to visit every cell.
> - **Space Complexity:** $O(m \cdot n)$, because we need to store the visited cells and the queues for the person and fire.
> - **Why these complexities occur:** The brute force approach simulates the movement of the person and the spread of the fire, which requires visiting every cell in the worst case.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a **_Breadth-First Search (BFS)_** to simulate the movement of the person and the spread of the fire simultaneously.
- Detailed breakdown of the approach:
  1. Initialize the current state of the grid with the person's and fire's positions.
  2. Use two queues, one for the person and one for the fire, to simulate their movement and spread.
  3. At each time step, try to move the person in all four directions and spread the fire to all adjacent empty cells.
  4. Repeat step 3 until the person escapes or is trapped.
- Proof of optimality: The optimal approach has the same time complexity as the brute force approach but is more efficient in practice because it uses a more efficient data structure (queues) to simulate the movement and spread.

```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

bool escape(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    queue<pair<int, int>> personQueue;
    queue<pair<int, int>> fireQueue;

    // Find the person's and fire's initial positions
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 2) {
                personQueue.push({i, j});
                visited[i][j] = true;
            } else if (grid[i][j] == 1) {
                fireQueue.push({i, j});
            }
        }
    }

    vector<int> dx = {-1, 1, 0, 0};
    vector<int> dy = {0, 0, -1, 1};

    while (!personQueue.empty()) {
        int personSize = personQueue.size();
        for (int i = 0; i < personSize; i++) {
            int x = personQueue.front().first;
            int y = personQueue.front().second;
            personQueue.pop();

            // Check if the person can escape
            if (x == 0 || x == m - 1 || y == 0 || y == n - 1) {
                return true;
            }

            // Try to move the person in all four directions
            for (int j = 0; j < 4; j++) {
                int newX = x + dx[j];
                int newY = y + dy[j];
                if (newX >= 0 && newX < m && newY >= 0 && newY < n && grid[newX][newY] == 0 && !visited[newX][newY]) {
                    personQueue.push({newX, newY});
                    visited[newX][newY] = true;
                }
            }
        }

        int fireSize = fireQueue.size();
        for (int i = 0; i < fireSize; i++) {
            int x = fireQueue.front().first;
            int y = fireQueue.front().second;
            fireQueue.pop();

            // Spread the fire in all four directions
            for (int j = 0; j < 4; j++) {
                int newX = x + dx[j];
                int newY = y + dy[j];
                if (newX >= 0 && newX < m && newY >= 0 && newY < n && grid[newX][newY] == 0) {
                    grid[newX][newY] = 1;
                    fireQueue.push({newX, newY});
                }
            }
        }
    }

    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the grid, because in the worst case, we need to visit every cell.
> - **Space Complexity:** $O(m \cdot n)$, because we need to store the visited cells and the queues for the person and fire.
> - **Optimality proof:** The optimal approach has the same time complexity as the brute force approach but is more efficient in practice because it uses a more efficient data structure (queues) to simulate the movement and spread.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: **_Breadth-First Search (BFS)_**, simulation of movement and spread.
- Problem-solving patterns identified: Using queues to simulate movement and spread, checking for escape conditions.
- Optimization techniques learned: Using more efficient data structures (queues) to simulate movement and spread.
- Similar problems to practice: **_Escape from Prison_**, **_Fire Spread_**.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for boundary conditions, not updating the visited cells correctly.
- Edge cases to watch for: Grids with multiple cells with fire or person, grids with no escape route.
- Performance pitfalls: Using inefficient data structures to simulate movement and spread.
- Testing considerations: Test the function with different grid sizes, different initial positions of the person and fire, and different escape conditions.