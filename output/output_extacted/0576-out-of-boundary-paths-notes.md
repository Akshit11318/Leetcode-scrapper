## Out of Boundary Paths
**Problem Link:** https://leetcode.com/problems/out-of-boundary-paths/description

**Problem Statement:**
- Input format and constraints: The problem takes in four parameters: `m`, `n`, `maxMove`, and `startRow`, `startColumn`. Here, `m` and `n` represent the number of rows and columns in a grid, `maxMove` is the maximum number of moves allowed, and `startRow` and `startColumn` are the starting coordinates.
- Expected output format: The function should return the number of paths that lead out of the boundary after `maxMove` moves.
- Key requirements and edge cases to consider: The grid is 0-indexed, and movements can be in any of the four directions (up, down, left, right).
- Example test cases with explanations: For example, given `m = 2`, `n = 2`, `maxMove = 2`, and `startRow = 0`, `startColumn = 0`, the function should return `2` because there are two paths that lead out of the boundary after two moves.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The first approach that comes to mind is to simulate all possible moves from the starting position and count how many of them lead out of the boundary after `maxMove` moves.
- Step-by-step breakdown of the solution:
  1. Start at the given position (`startRow`, `startColumn`).
  2. For each possible move (up, down, left, right), recursively explore all paths that can be taken from the new position.
  3. If a move leads out of the boundary, increment the count of paths.
  4. If `maxMove` moves have been made, stop exploring further and return to the previous position.
- Why this approach comes to mind first: It's straightforward to understand and implement but lacks efficiency for large inputs.

```cpp
class Solution {
public:
    int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        int count = 0;
        vector<vector<int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        function<void(int, int, int)> dfs = [&](int row, int col, int moves) {
            if (moves > maxMove) return;
            if (row < 0 || row >= m || col < 0 || col >= n) {
                count++;
                return;
            }
            for (auto& dir : directions) {
                dfs(row + dir[0], col + dir[1], moves + 1);
            }
        };
        dfs(startRow, startColumn, 0);
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(4^{maxMove})$, because in the worst case, we explore all four directions for each move up to `maxMove` times.
> - **Space Complexity:** $O(maxMove)$, due to the recursion stack.
> - **Why these complexities occur:** The brute force approach leads to exponential time complexity due to the recursive exploration of all possible paths. The space complexity is linear with respect to the recursion depth, which is bounded by `maxMove`.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Utilize dynamic programming to store and reuse the results of subproblems. Specifically, we can use a 3D DP table `dp[m][n][maxMove + 1]` where `dp[i][j][k]` represents the number of paths that lead out of the boundary starting from position `(i, j)` with `k` moves remaining.
- Detailed breakdown of the approach:
  1. Initialize the DP table with zeros.
  2. Fill the DP table in a bottom-up manner, considering all possible moves from each position and updating the counts accordingly.
  3. Use the filled DP table to find the number of paths leading out of the boundary from the starting position with `maxMove` moves.
- Proof of optimality: This approach ensures that each subproblem is solved only once and stored for future reference, avoiding redundant computations and achieving optimal time complexity.

```cpp
class Solution {
public:
    int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        int mod = 1e9 + 7;
        vector<vector<int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        vector<vector<vector<int>>> dp(m, vector<vector<int>>(n, vector<int>(maxMove + 1, 0)));
        
        for (int moves = 1; moves <= maxMove; moves++) {
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    for (auto& dir : directions) {
                        int ni = i + dir[0], nj = j + dir[1];
                        if (ni < 0 || ni >= m || nj < 0 || nj >= n) {
                            dp[i][j][moves] = (dp[i][j][moves] + 1) % mod;
                        } else {
                            dp[i][j][moves] = (dp[i][j][moves] + dp[ni][nj][moves - 1]) % mod;
                        }
                    }
                }
            }
        }
        return dp[startRow][startColumn][maxMove];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot maxMove)$, because we fill the DP table once.
> - **Space Complexity:** $O(m \cdot n \cdot maxMove)$, for storing the DP table.
> - **Optimality proof:** This dynamic programming approach ensures that we solve each subproblem exactly once, leading to a significant reduction in time complexity compared to the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming and recursion.
- Problem-solving patterns identified: Breaking down problems into smaller subproblems and reusing solutions to these subproblems.
- Optimization techniques learned: Memoization and dynamic programming to avoid redundant computations.
- Similar problems to practice: Other dynamic programming problems involving grids or paths.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize the DP table or to update the counts correctly.
- Edge cases to watch for: Handling boundary conditions and avoiding overflows.
- Performance pitfalls: Failing to optimize the solution, leading to high time or space complexity.
- Testing considerations: Thoroughly testing the solution with various inputs, including edge cases.