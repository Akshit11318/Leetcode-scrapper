## Select Cells in Grid with Maximum Score
**Problem Link:** https://leetcode.com/problems/select-cells-in-grid-with-maximum-score/description

**Problem Statement:**
- Input: You are given a `rows x cols` grid, where each cell contains a non-negative integer score.
- Constraints: `1 <= rows <= 10^5`, `1 <= cols <= 10^5`, and `0 <= score <= 10^6`.
- Expected Output: Return the maximum score you can get.
- Key Requirements: You can start from any cell and move either horizontally or vertically to any adjacent cell.
- Edge Cases: The grid can contain zeros, and the score of each cell is non-negative.

**Example Test Cases:**

- Example 1: `grid = [[1,2,3],[4,5,6]]`, the maximum score is `21`.
- Example 2: `grid = [[1,1,1],[1,1,1]]`, the maximum score is `9`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible paths from each cell and calculate the sum of scores for each path.
- We can use a depth-first search (DFS) to explore all possible paths.

```cpp
class Solution {
public:
    int maxScore(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        int maxScore = 0;
        
        // Define DFS function
        function<void(int, int, int, int)> dfs = 
            [&](int row, int col, int score, int visited) {
                maxScore = max(maxScore, score);
                for (auto [dr, dc] : vector<pair<int, int>>{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}) {
                    int nr = row + dr;
                    int nc = col + dc;
                    if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && !(visited & (1 << (nr * cols + nc)))) {
                        dfs(nr, nc, score + grid[nr][nc], visited | (1 << (nr * cols + nc)));
                    }
                }
            };
        
        // Start DFS from each cell
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                dfs(i, j, grid[i][j], 1 << (i * cols + j));
            }
        }
        
        return maxScore;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(4^{rows \times cols})$, as in the worst case, we might explore all possible paths.
> - **Space Complexity:** $O(rows \times cols)$, for the recursive call stack.
> - **Why these complexities occur:** The brute force approach tries all possible paths, leading to exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- We can observe that the problem can be solved using dynamic programming.
- The idea is to maintain a `dp` table where `dp[i][j]` represents the maximum score that can be obtained by starting from cell `(i, j)`.
- We can fill the `dp` table by iterating over the grid and for each cell, we try to move to its adjacent cells and update the maximum score.

```cpp
class Solution {
public:
    int maxScore(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        vector<vector<int>> dp(rows, vector<int>(cols, 0));
        
        // Initialize dp table
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                dp[i][j] = grid[i][j];
            }
        }
        
        // Fill dp table
        for (int i = 1; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                dp[i][j] = max(dp[i][j], dp[i-1][j] + grid[i][j]);
            }
        }
        for (int i = 0; i < rows; i++) {
            for (int j = 1; j < cols; j++) {
                dp[i][j] = max(dp[i][j], dp[i][j-1] + grid[i][j]);
            }
        }
        
        int maxScore = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                maxScore = max(maxScore, dp[i][j]);
            }
        }
        
        return maxScore;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(rows \times cols)$, as we need to fill the `dp` table.
> - **Space Complexity:** $O(rows \times cols)$, for the `dp` table.
> - **Optimality proof:** The dynamic programming approach ensures that we consider all possible paths and obtain the maximum score.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, depth-first search.
- Problem-solving patterns identified: exploring all possible paths, using a `dp` table to store intermediate results.
- Optimization techniques learned: using dynamic programming to avoid redundant calculations.
- Similar problems to practice: longest increasing subsequence, shortest path problems.

**Mistakes to Avoid:**
- Common implementation errors: not initializing the `dp` table correctly, not considering all possible paths.
- Edge cases to watch for: handling zeros in the grid, ensuring that the `dp` table is filled correctly.
- Performance pitfalls: using a brute force approach, not using dynamic programming to optimize the solution.
- Testing considerations: testing the solution with different grid sizes, testing the solution with different score values.