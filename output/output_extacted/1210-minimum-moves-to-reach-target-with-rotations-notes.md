## Minimum Moves to Reach Target with Rotations

**Problem Link:** https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/description

**Problem Statement:**
- Given a grid with `m` rows and `n` columns, where each cell can be either `0` (empty) or `1` (obstacle), and a starting position `start`, find the minimum number of moves required to reach the target position `target`.
- The movement can be done in four directions: up, down, left, and right. Additionally, the grid can be rotated clockwise or counterclockwise by 90 degrees.
- Input format: `m`, `n`, `start`, `target`, and the grid.
- Constraints: `1 <= m, n <= 50`, `0 <= start[0], start[1] < m`, `0 <= target[0], target[1] < m`, and the grid contains only `0` and `1`.
- Expected output: The minimum number of moves required to reach the target position from the start position.

**Key Requirements and Edge Cases:**
- The grid can be rotated, which means the movement can be done in all four directions (up, down, left, and right) after each rotation.
- The start and target positions are given as coordinates in the grid.
- The grid can contain obstacles (represented by `1`), which cannot be traversed.

**Example Test Cases:**
- A simple grid with no obstacles and a direct path from start to target.
- A grid with obstacles that require rotation to reach the target.
- A grid with no possible path from start to target.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible movements (up, down, left, and right) from the start position and then rotate the grid and try all possible movements again.
- The brute force approach involves using a queue to keep track of all possible positions and their corresponding number of moves.
- The algorithm checks for each position if it is the target position and returns the number of moves if it is.

```cpp
#include <queue>
#include <vector>

using namespace std;

struct Position {
    int x, y, moves;
    vector<vector<int>> grid;
};

int minMoves(vector<vector<int>>& grid, vector<int>& start, vector<int>& target) {
    int m = grid.size(), n = grid[0].size();
    queue<Position> q;
    q.push({start[0], start[1], 0, grid});
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    
    while (!q.empty()) {
        Position pos = q.front();
        q.pop();
        
        if (pos.x == target[0] && pos.y == target[1]) {
            return pos.moves;
        }
        
        if (visited[pos.x][pos.y]) {
            continue;
        }
        
        visited[pos.x][pos.y] = true;
        
        // Try all possible movements
        vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        for (auto dir : directions) {
            int nx = pos.x + dir.first, ny = pos.y + dir.second;
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && !pos.grid[nx][ny]) {
                Position new_pos = {nx, ny, pos.moves + 1, pos.grid};
                q.push(new_pos);
            }
        }
        
        // Rotate the grid and try all possible movements again
        vector<vector<int>> rotated_grid(m, vector<int>(n, 0));
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                rotated_grid[j][m - i - 1] = pos.grid[i][j];
            }
        }
        Position new_pos = {pos.x, pos.y, pos.moves + 1, rotated_grid};
        q.push(new_pos);
    }
    
    return -1;  // No possible path
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m^2 \cdot n^2 \cdot 4^d)$, where $d$ is the number of rotations required to reach the target position. This is because in the worst case, we need to try all possible movements and rotations for each position.
> - **Space Complexity:** $O(m \cdot n)$, which is the space required to store the visited positions.
> - **Why these complexities occur:** The brute force approach involves trying all possible movements and rotations, which leads to an exponential time complexity. The space complexity is linear because we only need to store the visited positions.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a breadth-first search (BFS) algorithm to explore all possible positions and rotations in a level-order manner.
- We use a queue to keep track of all possible positions and their corresponding number of moves.
- We also use a set to keep track of visited positions to avoid revisiting the same position.

```cpp
#include <queue>
#include <vector>
#include <set>

using namespace std;

struct Position {
    int x, y, moves;
    vector<vector<int>> grid;
};

int minMoves(vector<vector<int>>& grid, vector<int>& start, vector<int>& target) {
    int m = grid.size(), n = grid[0].size();
    queue<Position> q;
    q.push({start[0], start[1], 0, grid});
    set<vector<vector<int>>> visited;
    visited.insert(grid);
    
    while (!q.empty()) {
        Position pos = q.front();
        q.pop();
        
        if (pos.x == target[0] && pos.y == target[1]) {
            return pos.moves;
        }
        
        // Try all possible movements
        vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        for (auto dir : directions) {
            int nx = pos.x + dir.first, ny = pos.y + dir.second;
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && !pos.grid[nx][ny]) {
                Position new_pos = {nx, ny, pos.moves + 1, pos.grid};
                q.push(new_pos);
            }
        }
        
        // Rotate the grid and try all possible movements again
        vector<vector<int>> rotated_grid(m, vector<int>(n, 0));
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                rotated_grid[j][m - i - 1] = pos.grid[i][j];
            }
        }
        if (visited.find(rotated_grid) == visited.end()) {
            visited.insert(rotated_grid);
            Position new_pos = {pos.x, pos.y, pos.moves + 1, rotated_grid};
            q.push(new_pos);
        }
    }
    
    return -1;  // No possible path
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m^2 \cdot n^2 \cdot d)$, where $d$ is the number of rotations required to reach the target position. This is because we use a BFS algorithm to explore all possible positions and rotations in a level-order manner.
> - **Space Complexity:** $O(m \cdot n)$, which is the space required to store the visited positions.
> - **Optimality proof:** The optimal approach uses a BFS algorithm to explore all possible positions and rotations in a level-order manner, which ensures that we find the shortest path to the target position. The use of a set to keep track of visited positions avoids revisiting the same position, which reduces the time complexity.

---

### Final Notes

**Learning Points:**
- The use of BFS algorithm to explore all possible positions and rotations in a level-order manner.
- The use of a set to keep track of visited positions to avoid revisiting the same position.
- The importance of using a level-order search to find the shortest path to the target position.

**Mistakes to Avoid:**
- Not using a set to keep track of visited positions, which can lead to revisiting the same position and increasing the time complexity.
- Not using a level-order search, which can lead to finding a longer path to the target position.
- Not considering all possible rotations, which can lead to missing the shortest path to the target position.