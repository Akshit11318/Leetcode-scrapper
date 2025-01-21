## Number of Ways to Paint N-3 Grid
**Problem Link:** https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/description

**Problem Statement:**
- Input format and constraints: The input is an integer `n`, representing the number of rows in the grid. Each cell in the grid can be one of three colors.
- Expected output format: The output should be the number of ways to paint the grid such that no two adjacent cells have the same color.
- Key requirements and edge cases to consider: The grid has `n` rows and 3 columns. No two adjacent cells (horizontally or vertically) can have the same color.
- Example test cases with explanations: For `n = 1`, there are 3 ways to paint the grid (each cell can be one of the three colors). For `n = 2`, there are 6 ways to paint the grid.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can start by trying all possible combinations of colors for each cell in the grid.
- Step-by-step breakdown of the solution: For each cell, we try each of the three colors. We then check if the current cell's color is the same as the color of the cell above it (if it exists) or to its left (if it exists). If the colors are the same, we skip this combination.
- Why this approach comes to mind first: This approach is straightforward and simple to implement. However, it is not efficient for large values of `n`.

```cpp
int numWays(int n) {
    int count = 0;
    vector<vector<int>> grid(n, vector<int>(3, 0));
    function<void(int)> dfs = [&](int row) {
        if (row == n) {
            count++;
            return;
        }
        for (int i = 0; i < 3; i++) {
            bool valid = true;
            for (int j = 0; j < 3; j++) {
                if (j != i && (row > 0 && grid[row - 1][j] == i + 1 || j > 0 && grid[row][j - 1] == i + 1)) {
                    valid = false;
                    break;
                }
            }
            if (valid) {
                grid[row][i] = i + 1;
                dfs(row + 1);
                grid[row][i] = 0;
            }
        }
    };
    dfs(0);
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(3^n)$, because we try each of the three colors for each cell.
> - **Space Complexity:** $O(n)$, because we use a recursive function call stack of maximum depth `n`.
> - **Why these complexities occur:** The time complexity occurs because we try all possible combinations of colors for each cell. The space complexity occurs because we use a recursive function call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to store the number of ways to paint each row, given the previous row's colors.
- Detailed breakdown of the approach: We use a 2D array `dp` where `dp[i][j]` represents the number of ways to paint the first `i` rows, with the last row having color `j`. We iterate over each row and update `dp[i][j]` based on the number of ways to paint the previous row.
- Proof of optimality: This approach is optimal because it avoids recalculating the same subproblems multiple times, reducing the time complexity from exponential to linear.
- Why further optimization is impossible: This approach already uses the minimum amount of information necessary to solve the problem, making it impossible to further optimize.

```cpp
int numWays(int n) {
    vector<vector<int>> dp(2, vector<int>(3, 0));
    dp[0][0] = dp[0][1] = dp[0][2] = 1;
    for (int i = 1; i < n; i++) {
        vector<vector<int>> newDp(2, vector<int>(3, 0));
        for (int j = 0; j < 3; j++) {
            for (int k = 0; k < 3; k++) {
                if (j != k) {
                    newDp[i % 2][k] += dp[(i - 1) % 2][j];
                }
            }
        }
        dp = newDp;
    }
    return dp[(n - 1) % 2][0] + dp[(n - 1) % 2][1] + dp[(n - 1) % 2][2];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, because we iterate over each row once.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store the `dp` array.
> - **Optimality proof:** This approach is optimal because it uses dynamic programming to avoid recalculating the same subproblems multiple times.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, recursion, and backtracking.
- Problem-solving patterns identified: Using dynamic programming to store the number of ways to paint each row, given the previous row's colors.
- Optimization techniques learned: Avoiding recalculating the same subproblems multiple times using dynamic programming.
- Similar problems to practice: Other problems that involve painting or coloring, such as the "Paint House" problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` array correctly, or not updating the `dp` array correctly.
- Edge cases to watch for: The base case where `n` is 0 or 1, and the case where `n` is very large.
- Performance pitfalls: Using a recursive approach without memoization, or using a brute force approach that tries all possible combinations of colors.
- Testing considerations: Testing the function with different values of `n`, including edge cases and large values.