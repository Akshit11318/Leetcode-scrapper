## Number of Ways to Reach Destination in the Grid

**Problem Link:** https://leetcode.com/problems/number-of-ways-to-reach-destination-in-the-grid/description

**Problem Statement:**
- Input format: A grid of size `m x n`, where `m` is the number of rows and `n` is the number of columns.
- Constraints: `1 <= m, n <= 100`.
- Expected output format: The number of ways to reach the destination `(m - 1, n - 1)` from the source `(0, 0)`.
- Key requirements and edge cases to consider:
  - The destination is the bottom-right cell of the grid.
  - The source is the top-left cell of the grid.
  - Only right and down movements are allowed.
  - Example test cases:
    - `m = 3`, `n = 3`: The output should be `6`.
    - `m = 2`, `n = 2`: The output should be `2`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The problem can be solved by trying all possible paths from the source to the destination.
- Step-by-step breakdown of the solution:
  1. Start at the source `(0, 0)`.
  2. Try moving right or down at each step.
  3. If the destination is reached, count the path as a valid solution.
- Why this approach comes to mind first: It is a straightforward solution that tries all possible paths, but it is inefficient for large grids.

```cpp
int uniquePaths(int m, int n) {
    int count = 0;
    vector<vector<bool>> visited(m, vector<bool>(n, false));
    function<void(int, int)> dfs = [&](int x, int y) {
        if (x == m - 1 && y == n - 1) {
            count++;
            return;
        }
        if (x >= m || y >= n || visited[x][y]) {
            return;
        }
        visited[x][y] = true;
        dfs(x + 1, y);
        dfs(x, y + 1);
        visited[x][y] = false;
    };
    dfs(0, 0);
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{m + n - 2})$, because in the worst case, we try all possible paths.
> - **Space Complexity:** $O(m + n)$, because of the recursion stack.
> - **Why these complexities occur:** The brute force approach tries all possible paths, resulting in exponential time complexity. The space complexity is due to the recursion stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using dynamic programming, where we store the number of ways to reach each cell.
- Detailed breakdown of the approach:
  1. Create a 2D array `dp` of size `m x n`, where `dp[i][j]` stores the number of ways to reach cell `(i, j)`.
  2. Initialize the first row and column of `dp` to 1, because there is only one way to reach each cell in the first row and column (by always moving right or always moving down).
  3. For each cell `(i, j)` in the grid, calculate `dp[i][j]` as the sum of `dp[i - 1][j]` and `dp[i][j - 1]`, because we can reach cell `(i, j)` by moving down from cell `(i - 1, j)` or by moving right from cell `(i, j - 1)`.
- Proof of optimality: This approach is optimal because it uses dynamic programming to store the number of ways to reach each cell, avoiding redundant calculations.

```cpp
int uniquePaths(int m, int n) {
    vector<vector<int>> dp(m, vector<int>(n, 1));
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
        }
    }
    return dp[m - 1][n - 1];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, because we fill in the `dp` array once.
> - **Space Complexity:** $O(m \cdot n)$, because of the `dp` array.
> - **Optimality proof:** This approach is optimal because it uses dynamic programming to store the number of ways to reach each cell, avoiding redundant calculations.

---

### Alternative Approach

**Explanation:**
- Different perspective or technique: We can use combinatorial mathematics to solve this problem.
- Unique trade-offs: This approach is more mathematical and less computational.
- Scenarios where this approach might be preferred: When the grid size is very large, and we want to avoid computational complexity.
- Comparison with optimal approach: This approach is more efficient in terms of computational complexity, but it requires a deeper understanding of combinatorial mathematics.

```cpp
int uniquePaths(int m, int n) {
    int N = m + n - 2;
    int k = m - 1;
    long long ans = 1;
    for (int i = 1; i <= k; i++) {
        ans = ans * (N - i + 1) / i;
    }
    return ans;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m + n)$, because we calculate the binomial coefficient.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space.
> - **Trade-off analysis:** This approach is more efficient in terms of computational complexity, but it requires a deeper understanding of combinatorial mathematics.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, combinatorial mathematics.
- Problem-solving patterns identified: Using dynamic programming to store intermediate results, using combinatorial mathematics to solve problems.
- Optimization techniques learned: Avoiding redundant calculations, using mathematical formulas to reduce computational complexity.
- Similar problems to practice: Other problems that involve dynamic programming or combinatorial mathematics, such as the "Climbing Stairs" problem or the "Combinations" problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` array correctly, not calculating the binomial coefficient correctly.
- Edge cases to watch for: Grid sizes of 1 or 0, negative grid sizes.
- Performance pitfalls: Using a brute force approach for large grid sizes, not optimizing the calculation of the binomial coefficient.
- Testing considerations: Testing the function with different grid sizes, testing the function with edge cases.