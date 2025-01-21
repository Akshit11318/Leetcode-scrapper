## Rotting Oranges

**Problem Link:** https://leetcode.com/problems/rotting-oranges/description

**Problem Statement:**
- Input format: A 2D grid of integers where `0` represents an empty cell, `1` represents a fresh orange, and `2` represents a rotten orange.
- Constraints: The grid can have any number of rows and columns, but it is guaranteed to be non-empty.
- Expected output format: The minimum number of minutes until no cell has a fresh orange. If this is impossible, return `-1`.
- Key requirements and edge cases to consider: 
    - The grid can contain no fresh oranges.
    - The grid can contain no rotten oranges.
    - The grid can contain a mix of fresh and rotten oranges.
- Example test cases with explanations:
    - `[[2,1,1],[1,1,0],[0,1,1]]` returns `4`.
    - `[[2,1,1],[0,1,1],[1,0,1]]` returns `-1`.
    - `[[0,2]]` returns `0`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Simulate the process of rotting oranges step by step.
- Step-by-step breakdown of the solution:
    1. Initialize a queue with all rotten oranges.
    2. Initialize a variable to keep track of the number of fresh oranges.
    3. For each minute, pop all rotten oranges from the queue and check their neighbors.
    4. If a neighbor is a fresh orange, mark it as rotten and add it to the queue for the next minute.
    5. Repeat this process until there are no more fresh oranges or the queue is empty.
- Why this approach comes to mind first: It is a straightforward simulation of the problem statement.

```cpp
#include <queue>
#include <vector>

using namespace std;

int orangesRotting(vector<vector<int>>& grid) {
    int rows = grid.size();
    int cols = grid[0].size();
    int fresh = 0;
    queue<pair<int, int>> q;

    // Initialize queue with rotten oranges and count fresh oranges
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (grid[i][j] == 2) {
                q.push({i, j});
            } else if (grid[i][j] == 1) {
                fresh++;
            }
        }
    }

    int minutes = 0;
    vector<int> dx = {-1, 1, 0, 0};
    vector<int> dy = {0, 0, -1, 1};

    while (!q.empty() && fresh > 0) {
        int size = q.size();
        for (int i = 0; i < size; i++) {
            int x = q.front().first;
            int y = q.front().second;
            q.pop();

            for (int j = 0; j < 4; j++) {
                int nx = x + dx[j];
                int ny = y + dy[j];

                if (nx >= 0 && nx < rows && ny >= 0 && ny < cols && grid[nx][ny] == 1) {
                    grid[nx][ny] = 2;
                    q.push({nx, ny});
                    fresh--;
                }
            }
        }
        minutes++;
    }

    return fresh == 0 ? minutes : -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$ where $n$ and $m$ are the dimensions of the grid and $k$ is the number of minutes until all oranges are rotten. This is because in the worst case, we visit each cell in the grid once per minute.
> - **Space Complexity:** $O(n \cdot m)$ for the queue in the worst case when all oranges are rotten and we need to store all of them in the queue.
> - **Why these complexities occur:** The time complexity occurs because we are simulating the process of rotting oranges step by step. The space complexity occurs because we are using a queue to keep track of the rotten oranges.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using a breadth-first search (BFS) algorithm.
- Detailed breakdown of the approach:
    1. Initialize a queue with all rotten oranges.
    2. Initialize a variable to keep track of the number of fresh oranges.
    3. For each minute, pop all rotten oranges from the queue and check their neighbors.
    4. If a neighbor is a fresh orange, mark it as rotten and add it to the queue for the next minute.
    5. Repeat this process until there are no more fresh oranges or the queue is empty.
- Proof of optimality: This approach is optimal because it visits each cell in the grid only once per minute, which is the minimum number of visits required to solve the problem.
- Why further optimization is impossible: This approach is already optimal because it uses the minimum number of visits required to solve the problem.

```cpp
#include <queue>
#include <vector>

using namespace std;

int orangesRotting(vector<vector<int>>& grid) {
    int rows = grid.size();
    int cols = grid[0].size();
    int fresh = 0;
    queue<pair<int, int>> q;

    // Initialize queue with rotten oranges and count fresh oranges
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (grid[i][j] == 2) {
                q.push({i, j});
            } else if (grid[i][j] == 1) {
                fresh++;
            }
        }
    }

    int minutes = 0;
    vector<int> dx = {-1, 1, 0, 0};
    vector<int> dy = {0, 0, -1, 1};

    while (!q.empty() && fresh > 0) {
        int size = q.size();
        for (int i = 0; i < size; i++) {
            int x = q.front().first;
            int y = q.front().second;
            q.pop();

            for (int j = 0; j < 4; j++) {
                int nx = x + dx[j];
                int ny = y + dy[j];

                if (nx >= 0 && nx < rows && ny >= 0 && ny < cols && grid[nx][ny] == 1) {
                    grid[nx][ny] = 2;
                    q.push({nx, ny});
                    fresh--;
                }
            }
        }
        minutes++;
    }

    return fresh == 0 ? minutes : -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$ where $n$ and $m$ are the dimensions of the grid and $k$ is the number of minutes until all oranges are rotten. This is because in the worst case, we visit each cell in the grid once per minute.
> - **Space Complexity:** $O(n \cdot m)$ for the queue in the worst case when all oranges are rotten and we need to store all of them in the queue.
> - **Optimality proof:** This approach is optimal because it uses the minimum number of visits required to solve the problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS, queue data structure.
- Problem-solving patterns identified: Simulating a process step by step.
- Optimization techniques learned: Using a queue to keep track of the rotten oranges.
- Similar problems to practice: Other problems that involve simulating a process step by step.

**Mistakes to Avoid:**
- Common implementation errors: Not checking the boundaries of the grid when checking the neighbors of a cell.
- Edge cases to watch for: The grid can contain no fresh oranges, the grid can contain no rotten oranges.
- Performance pitfalls: Using a recursive approach instead of an iterative approach.
- Testing considerations: Test the function with different inputs, including edge cases.