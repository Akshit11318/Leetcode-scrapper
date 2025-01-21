## Disconnect Path in a Binary Matrix by at Most One Flip
**Problem Link:** https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/description

**Problem Statement:**
- Input format: A binary matrix `mat` of size `m x n`.
- Constraints: `1 <= m, n <= 10^5`, `mat[i][j]` is either `0` or `1`.
- Expected output format: Return `true` if there exists a path from the top-left cell to the bottom-right cell by flipping at most one cell, and `false` otherwise.
- Key requirements and edge cases to consider:
  - The path must consist of adjacent cells (horizontally or vertically) with the same value.
  - The path can be flipped at most once.
  - The input matrix may contain only zeros or only ones.
- Example test cases with explanations:
  - `mat = [[1,1,1],[1,0,1],[1,1,1]]` returns `true` because we can flip the cell at `(1,1)` to connect the path.
  - `mat = [[1,0,1],[0,0,0],[1,0,1]]` returns `false` because we cannot connect the path by flipping at most one cell.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible paths from the top-left cell to the bottom-right cell and check if we can flip at most one cell to connect the path.
- Step-by-step breakdown of the solution:
  1. Define a recursive function to explore all possible paths.
  2. For each cell, check if we can move to an adjacent cell with the same value.
  3. If we encounter a cell with a different value, try flipping it and continue the path.
  4. If we reach the bottom-right cell, return `true`.
- Why this approach comes to mind first: It is a straightforward way to explore all possible paths and check the condition.

```cpp
bool isPossibleToCutPath(vector<vector<int>>& mat) {
    int m = mat.size();
    int n = mat[0].size();
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    
    function<bool(int, int, bool)> dfs = [&](int x, int y, bool flipped) {
        if (x == m - 1 && y == n - 1) return true;
        visited[x][y] = true;
        for (int dx = -1; dx <= 1; dx++) {
            for (int dy = -1; dy <= 1; dy++) {
                if (abs(dx) + abs(dy) != 1) continue;
                int nx = x + dx;
                int ny = y + dy;
                if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                if (visited[nx][ny]) continue;
                if (mat[nx][ny] == mat[x][y] && dfs(nx, ny, flipped)) return true;
                if (!flipped && mat[nx][ny] != mat[x][y] && dfs(nx, ny, true)) return true;
            }
        }
        return false;
    };
    
    return dfs(0, 0, false);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{m \cdot n})$ because in the worst case, we need to explore all possible paths.
> - **Space Complexity:** $O(m \cdot n)$ for the recursion stack and the `visited` matrix.
> - **Why these complexities occur:** The brute force approach tries all possible paths, which leads to exponential time complexity. The space complexity is due to the recursion stack and the `visited` matrix.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of trying all possible paths, we can use a breadth-first search (BFS) to explore the connected components of the matrix.
- Detailed breakdown of the approach:
  1. Perform a BFS from the top-left cell to find all connected cells with the same value.
  2. If the bottom-right cell is connected, return `true`.
  3. Otherwise, try flipping each cell in the connected component and perform another BFS to see if the bottom-right cell becomes connected.
- Proof of optimality: This approach is optimal because it only explores the connected components of the matrix, which reduces the search space significantly.
- Why further optimization is impossible: This approach already explores the minimum necessary search space to solve the problem.

```cpp
bool isPossibleToCutPath(vector<vector<int>>& mat) {
    int m = mat.size();
    int n = mat[0].size();
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    queue<pair<int, int>> q;
    
    // Perform BFS from the top-left cell
    q.push({0, 0});
    visited[0][0] = true;
    bool connected = false;
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        if (x == m - 1 && y == n - 1) connected = true;
        for (int dx = -1; dx <= 1; dx++) {
            for (int dy = -1; dy <= 1; dy++) {
                if (abs(dx) + abs(dy) != 1) continue;
                int nx = x + dx;
                int ny = y + dy;
                if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                if (visited[nx][ny]) continue;
                if (mat[nx][ny] == mat[x][y]) {
                    q.push({nx, ny});
                    visited[nx][ny] = true;
                }
            }
        }
    }
    
    // Try flipping each cell in the connected component
    if (!connected) {
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (visited[i][j]) {
                    mat[i][j] = 1 - mat[i][j];
                    vector<vector<bool>> newVisited(m, vector<bool>(n, false));
                    queue<pair<int, int>> newQ;
                    newQ.push({0, 0});
                    newVisited[0][0] = true;
                    connected = false;
                    while (!newQ.empty()) {
                        int x = newQ.front().first;
                        int y = newQ.front().second;
                        newQ.pop();
                        if (x == m - 1 && y == n - 1) connected = true;
                        for (int dx = -1; dx <= 1; dx++) {
                            for (int dy = -1; dy <= 1; dy++) {
                                if (abs(dx) + abs(dy) != 1) continue;
                                int nx = x + dx;
                                int ny = y + dy;
                                if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                                if (newVisited[nx][ny]) continue;
                                if (mat[nx][ny] == mat[x][y]) {
                                    newQ.push({nx, ny});
                                    newVisited[nx][ny] = true;
                                }
                            }
                        }
                    }
                    mat[i][j] = 1 - mat[i][j];
                    if (connected) return true;
                }
            }
        }
    }
    
    return connected;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$ because we perform a BFS from the top-left cell and try flipping each cell in the connected component.
> - **Space Complexity:** $O(m \cdot n)$ for the `visited` matrix and the queue.
> - **Optimality proof:** This approach is optimal because it only explores the connected components of the matrix, which reduces the search space significantly.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS, connected components, and flipping cells to connect paths.
- Problem-solving patterns identified: Using BFS to explore connected components and trying flipping cells to connect paths.
- Optimization techniques learned: Reducing the search space by exploring connected components and trying flipping cells.
- Similar problems to practice: Problems involving connected components, BFS, and flipping cells to connect paths.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for visited cells, not handling edge cases, and not optimizing the search space.
- Edge cases to watch for: Empty matrix, matrix with only zeros or only ones, and matrix with disconnected components.
- Performance pitfalls: Not using BFS to explore connected components and not trying flipping cells to connect paths.
- Testing considerations: Test the implementation with different input matrices, including edge cases and large matrices.