## Android Unlock Patterns
**Problem Link:** https://leetcode.com/problems/android-unlock-patterns/description

**Problem Statement:**
- Input format: Given an integer `m` and `n`, return the number of unlock patterns of length `n` using `m x m` grid, where each cell can be visited at most once.
- Constraints: `1 <= m <= 3`, `1 <= n <= 9`.
- Expected output format: The number of unlock patterns.
- Key requirements and edge cases to consider: The unlock pattern should not visit the same cell more than once, and it should be a valid sequence of moves (i.e., it should not jump over other cells).
- Example test cases with explanations:
  - For `m = 3` and `n = 4`, there are `368` possible unlock patterns.
  - For `m = 2` and `n = 2`, there are `2` possible unlock patterns.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To generate all possible unlock patterns, we can use a recursive approach to try all possible moves from each cell.
- Step-by-step breakdown of the solution:
  1. Start from each cell in the grid.
  2. For each cell, try all possible moves (up, down, left, right, and diagonals).
  3. If the move is valid (i.e., it does not visit the same cell more than once), recursively try all possible moves from the new cell.
  4. If the length of the pattern reaches `n`, increment the count of unlock patterns.
- Why this approach comes to mind first: It is a straightforward way to generate all possible unlock patterns.

```cpp
int numberOfPatterns(int m, int n) {
    int count = 0;
    vector<vector<bool>> visited(m, vector<bool>(m, false));
    vector<vector<int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}, {-1, -1}, {-1, 1}, {1, -1}, {1, 1}};

    function<void(int, int, int)> dfs = [&](int x, int y, int length) {
        if (length == n) {
            count++;
            return;
        }
        visited[x][y] = true;
        for (auto& dir : directions) {
            int nx = x + dir[0];
            int ny = y + dir[1];
            if (nx >= 0 && nx < m && ny >= 0 && ny < m && !visited[nx][ny]) {
                dfs(nx, ny, length + 1);
            }
        }
        visited[x][y] = false;
    };

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < m; j++) {
            dfs(i, j, 1);
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m^2 \cdot 8^n)$, where $m$ is the size of the grid and $n$ is the length of the pattern. This is because we try all possible moves from each cell, and there are $8$ possible moves from each cell.
> - **Space Complexity:** $O(m^2)$, where $m$ is the size of the grid. This is because we need to keep track of the visited cells.
> - **Why these complexities occur:** The time complexity occurs because we try all possible moves from each cell, and the space complexity occurs because we need to keep track of the visited cells.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to store the number of unlock patterns for each cell and each length.
- Detailed breakdown of the approach:
  1. Create a 3D array `dp` of size `m x m x n`, where `dp[i][j][k]` represents the number of unlock patterns of length `k` starting from cell `(i, j)`.
  2. Initialize `dp[i][j][1] = 1` for all cells `(i, j)`, because there is only one way to start from each cell.
  3. For each length `k` from `2` to `n`, for each cell `(i, j)`, try all possible moves from cell `(i, j)` and update `dp[i][j][k]` with the sum of `dp[nx][ny][k-1]` for all valid moves `(nx, ny)`.
  4. The final answer is the sum of `dp[i][j][n]` for all cells `(i, j)`.
- Proof of optimality: This approach is optimal because it uses dynamic programming to avoid redundant calculations.

```cpp
int numberOfPatterns(int m, int n) {
    int count = 0;
    vector<vector<vector<int>>> dp(m, vector<vector<int>>(m, vector<int>(n + 1, 0)));
    vector<vector<int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}, {-1, -1}, {-1, 1}, {1, -1}, {1, 1}};

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < m; j++) {
            dp[i][j][1] = 1;
        }
    }

    for (int k = 2; k <= n; k++) {
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < m; j++) {
                for (auto& dir : directions) {
                    int ni = i + dir[0];
                    int nj = j + dir[1];
                    if (ni >= 0 && ni < m && nj >= 0 && nj < m) {
                        dp[i][j][k] += dp[ni][nj][k - 1];
                    }
                }
            }
        }
    }

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < m; j++) {
            count += dp[i][j][n];
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m^2 \cdot 8n)$, where $m$ is the size of the grid and $n$ is the length of the pattern. This is because we try all possible moves from each cell for each length.
> - **Space Complexity:** $O(m^2n)$, where $m$ is the size of the grid and $n$ is the length of the pattern. This is because we need to store the number of unlock patterns for each cell and each length.
> - **Optimality proof:** This approach is optimal because it uses dynamic programming to avoid redundant calculations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, recursive approach.
- Problem-solving patterns identified: Using dynamic programming to avoid redundant calculations.
- Optimization techniques learned: Using dynamic programming to reduce time complexity.
- Similar problems to practice: Other problems that involve dynamic programming and recursive approach.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` array correctly, not updating the `dp` array correctly.
- Edge cases to watch for: The case where `m = 1` and `n = 1`, the case where `m = 3` and `n = 9`.
- Performance pitfalls: Not using dynamic programming, using a recursive approach without memoization.
- Testing considerations: Test the function with different values of `m` and `n`, test the function with edge cases.