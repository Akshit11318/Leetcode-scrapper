## Shortest Path to Get All Keys

**Problem Link:** https://leetcode.com/problems/shortest-path-to-get-all-keys/description

**Problem Statement:**
- Input format: A 2D grid `grid`, where each cell can be one of the following: `.` (empty), `#` (wall), a lowercase letter (key), or an uppercase letter (lock).
- Constraints: The grid is guaranteed to be non-empty, and each cell is a single character.
- Expected output format: The minimum number of steps required to collect all keys, or `-1` if it is impossible.
- Key requirements and edge cases to consider: The presence of locks, keys, and walls, and the need to find the shortest path.
- Example test cases with explanations:
  - A grid with a key and no locks.
  - A grid with a lock and no keys.
  - A grid with a key and a corresponding lock.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible paths from each cell to find the shortest path that collects all keys.
- Step-by-step breakdown of the solution:
  1. Iterate over each cell in the grid.
  2. For each cell, perform a depth-first search (DFS) to explore all possible paths.
  3. During the DFS, keep track of the keys collected and the locks encountered.
  4. If a lock is encountered and the corresponding key has not been collected, backtrack and try another path.
  5. If all keys are collected, return the length of the path.
- Why this approach comes to mind first: It is a straightforward way to explore all possible paths and find the shortest one.

```cpp
#include <vector>
#include <unordered_set>
#include <string>

using namespace std;

int shortestPathAllKeys(vector<vector<char>>& grid) {
    int rows = grid.size();
    int cols = grid[0].size();
    int keys = 0;
    int locks = 0;
    int startX = -1;
    int startY = -1;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (grid[i][j] == '@') {
                startX = i;
                startY = j;
            } else if (grid[i][j] >= 'a' && grid[i][j] <= 'f') {
                keys++;
            } else if (grid[i][j] >= 'A' && grid[i][j] <= 'F') {
                locks++;
            }
        }
    }

    unordered_set<string> visited;
    vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    vector<vector<int>> queue = {{startX, startY, 0, 0}};
    while (!queue.empty()) {
        vector<int> current = queue.back();
        queue.pop_back();
        int x = current[0];
        int y = current[1];
        int steps = current[2];
        int collected = current[3];
        string state = to_string(x) + "," + to_string(y) + "," + to_string(collected);
        if (visited.find(state) != visited.end()) {
            continue;
        }
        visited.insert(state);
        if (collected == (1 << keys) - 1) {
            return steps;
        }
        for (auto& direction : directions) {
            int nx = x + direction.first;
            int ny = y + direction.second;
            if (nx >= 0 && nx < rows && ny >= 0 && ny < cols && grid[nx][ny] != '#') {
                int newCollected = collected;
                if (grid[nx][ny] >= 'a' && grid[nx][ny] <= 'f') {
                    newCollected |= 1 << (grid[nx][ny] - 'a');
                } else if (grid[nx][ny] >= 'A' && grid[nx][ny] <= 'F') {
                    if ((collected >> (grid[nx][ny] - 'A')) & 1 == 0) {
                        continue;
                    }
                }
                queue.push_back({nx, ny, steps + 1, newCollected});
            }
        }
    }
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^k \cdot m \cdot n \cdot 4^k)$, where $k$ is the number of keys, $m$ is the number of rows, and $n$ is the number of columns. This is because we are exploring all possible paths and keeping track of the keys collected.
> - **Space Complexity:** $O(2^k \cdot m \cdot n)$, where $k$ is the number of keys, $m$ is the number of rows, and $n$ is the number of columns. This is because we are storing the visited states in a set.
> - **Why these complexities occur:** The time complexity occurs because we are exploring all possible paths and keeping track of the keys collected. The space complexity occurs because we are storing the visited states in a set.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a breadth-first search (BFS) algorithm to explore all possible paths and keep track of the keys collected.
- Detailed breakdown of the approach:
  1. Initialize a queue with the starting position and an empty set of collected keys.
  2. Perform a BFS to explore all possible paths.
  3. During the BFS, keep track of the keys collected and the locks encountered.
  4. If a lock is encountered and the corresponding key has not been collected, skip this path.
  5. If all keys are collected, return the length of the path.
- Proof of optimality: This approach is optimal because it explores all possible paths and keeps track of the keys collected in a efficient manner.

```cpp
#include <vector>
#include <unordered_set>
#include <string>
#include <queue>

using namespace std;

int shortestPathAllKeys(vector<vector<char>>& grid) {
    int rows = grid.size();
    int cols = grid[0].size();
    int keys = 0;
    int locks = 0;
    int startX = -1;
    int startY = -1;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (grid[i][j] == '@') {
                startX = i;
                startY = j;
            } else if (grid[i][j] >= 'a' && grid[i][j] <= 'f') {
                keys++;
            } else if (grid[i][j] >= 'A' && grid[i][j] <= 'F') {
                locks++;
            }
        }
    }

    unordered_set<string> visited;
    vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    queue<vector<int>> q;
    q.push({startX, startY, 0, 0});
    while (!q.empty()) {
        vector<int> current = q.front();
        q.pop();
        int x = current[0];
        int y = current[1];
        int steps = current[2];
        int collected = current[3];
        string state = to_string(x) + "," + to_string(y) + "," + to_string(collected);
        if (visited.find(state) != visited.end()) {
            continue;
        }
        visited.insert(state);
        if (collected == (1 << keys) - 1) {
            return steps;
        }
        for (auto& direction : directions) {
            int nx = x + direction.first;
            int ny = y + direction.second;
            if (nx >= 0 && nx < rows && ny >= 0 && ny < cols && grid[nx][ny] != '#') {
                int newCollected = collected;
                if (grid[nx][ny] >= 'a' && grid[nx][ny] <= 'f') {
                    newCollected |= 1 << (grid[nx][ny] - 'a');
                } else if (grid[nx][ny] >= 'A' && grid[nx][ny] <= 'F') {
                    if ((collected >> (grid[nx][ny] - 'A')) & 1 == 0) {
                        continue;
                    }
                }
                q.push({nx, ny, steps + 1, newCollected});
            }
        }
    }
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^k \cdot m \cdot n)$, where $k$ is the number of keys, $m$ is the number of rows, and $n$ is the number of columns. This is because we are exploring all possible paths and keeping track of the keys collected.
> - **Space Complexity:** $O(2^k \cdot m \cdot n)$, where $k$ is the number of keys, $m$ is the number of rows, and $n$ is the number of columns. This is because we are storing the visited states in a set.
> - **Optimality proof:** This approach is optimal because it explores all possible paths and keeps track of the keys collected in a efficient manner.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS, DFS, and bit manipulation.
- Problem-solving patterns identified: Exploring all possible paths and keeping track of the keys collected.
- Optimization techniques learned: Using a BFS algorithm to explore all possible paths and keeping track of the keys collected.
- Similar problems to practice: Other problems that involve exploring all possible paths and keeping track of certain conditions.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for visited states, not keeping track of the keys collected, and not handling the locks correctly.
- Edge cases to watch for: The presence of locks, keys, and walls, and the need to find the shortest path.
- Performance pitfalls: Not using an efficient algorithm to explore all possible paths and keep track of the keys collected.
- Testing considerations: Testing the algorithm with different inputs and edge cases to ensure correctness and efficiency.