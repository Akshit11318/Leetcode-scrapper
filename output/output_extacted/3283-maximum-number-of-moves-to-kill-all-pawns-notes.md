## Maximum Number of Moves to Kill All Pawns
**Problem Link:** https://leetcode.com/problems/maximum-number-of-moves-to-kill-all-pawns/description

**Problem Statement:**
- Input format and constraints: Given a grid of size `n x n` and an integer `k`, determine the maximum number of moves required to kill all pawns, where each pawn can move in one of eight possible directions (horizontally, vertically, or diagonally) and can only kill one pawn per move.
- Expected output format: The maximum number of moves as an integer.
- Key requirements and edge cases to consider: The grid may contain empty cells, and the number of pawns may be less than or equal to `k`.
- Example test cases with explanations:
  - A grid with no pawns should return 0.
  - A grid with one pawn should return 0 if `k` is greater than 0.
  - A grid with multiple pawns should return the maximum number of moves required to kill all pawns.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible moves for each pawn and keep track of the maximum number of moves.
- Step-by-step breakdown of the solution:
  1. Initialize a variable to store the maximum number of moves.
  2. Iterate over each cell in the grid.
  3. If the cell contains a pawn, try all possible moves and update the maximum number of moves.
  4. Repeat steps 2-3 until all pawns have been killed.
- Why this approach comes to mind first: It is a straightforward and intuitive approach, but it has a high time complexity due to the large number of possible moves.

```cpp
int maxMoves(vector<vector<char>>& grid, int k) {
    int n = grid.size();
    int maxMoves = 0;
    vector<vector<bool>> visited(n, vector<bool>(n, false));
    
    function<void(int, int, int)> dfs = [&](int x, int y, int moves) {
        if (moves > maxMoves) maxMoves = moves;
        for (int dx = -1; dx <= 1; dx++) {
            for (int dy = -1; dy <= 1; dy++) {
                if (dx == 0 && dy == 0) continue;
                int nx = x + dx;
                int ny = y + dy;
                if (nx < 0 || nx >= n || ny < 0 || ny >= n || visited[nx][ny]) continue;
                if (grid[nx][ny] == 'P') {
                    visited[nx][ny] = true;
                    dfs(nx, ny, moves + 1);
                    visited[nx][ny] = false;
                }
            }
        }
    };
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 'P') {
                visited[i][j] = true;
                dfs(i, j, 1);
                visited[i][j] = false;
            }
        }
    }
    
    return maxMoves;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot 8^k)$, where $n$ is the size of the grid and $k$ is the number of pawns. This is because we are trying all possible moves for each pawn.
> - **Space Complexity:** $O(n^2)$, where $n$ is the size of the grid. This is because we are using a visited matrix to keep track of the cells that have been visited.
> - **Why these complexities occur:** The high time complexity is due to the large number of possible moves, and the space complexity is due to the visited matrix.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a breadth-first search (BFS) algorithm to find the maximum number of moves required to kill all pawns.
- Detailed breakdown of the approach:
  1. Initialize a queue to store the cells that need to be visited.
  2. Initialize a variable to store the maximum number of moves.
  3. Iterate over each cell in the grid.
  4. If the cell contains a pawn, add it to the queue.
  5. Perform BFS to find the maximum number of moves required to kill all pawns.
- Proof of optimality: The BFS algorithm is guaranteed to find the shortest path to the goal, which in this case is the maximum number of moves required to kill all pawns.

```cpp
int maxMoves(vector<vector<char>>& grid, int k) {
    int n = grid.size();
    int maxMoves = 0;
    queue<pair<int, int>> q;
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 'P') {
                q.push({i, j});
            }
        }
    }
    
    vector<pair<int, int>> directions = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};
    
    while (!q.empty()) {
        int size = q.size();
        for (int i = 0; i < size; i++) {
            auto [x, y] = q.front();
            q.pop();
            for (auto [dx, dy] : directions) {
                int nx = x + dx;
                int ny = y + dy;
                if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
                if (grid[nx][ny] == 'P') {
                    grid[nx][ny] = '.';
                    q.push({nx, ny});
                }
            }
        }
        maxMoves++;
    }
    
    return maxMoves - 1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot k)$, where $n$ is the size of the grid and $k$ is the number of pawns. This is because we are using a BFS algorithm to find the maximum number of moves.
> - **Space Complexity:** $O(n^2)$, where $n$ is the size of the grid. This is because we are using a queue to store the cells that need to be visited.
> - **Optimality proof:** The BFS algorithm is guaranteed to find the shortest path to the goal, which in this case is the maximum number of moves required to kill all pawns.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS algorithm, queue data structure.
- Problem-solving patterns identified: Using a BFS algorithm to find the shortest path to the goal.
- Optimization techniques learned: Using a queue to store the cells that need to be visited, reducing the time complexity from $O(n^2 \cdot 8^k)$ to $O(n^2 \cdot k)$.
- Similar problems to practice: Other problems that involve finding the shortest path to the goal, such as the "Shortest Path in a Grid" problem.

**Mistakes to Avoid:**
- Common implementation errors: Not checking the boundaries of the grid, not handling the case where there are no pawns.
- Edge cases to watch for: The grid may contain empty cells, the number of pawns may be less than or equal to $k$.
- Performance pitfalls: Using a recursive function instead of a BFS algorithm, which can lead to a high time complexity.
- Testing considerations: Test the function with different inputs, including edge cases, to ensure that it is working correctly.