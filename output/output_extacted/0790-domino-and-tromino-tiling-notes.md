## Domino and Tromino Tiling

**Problem Link:** https://leetcode.com/problems/domino-and-tromino-tiling/description

**Problem Statement:**
- Input: An integer `N`, representing the number of tiles in a row.
- Constraints: `1 <= N <= 1000`
- Expected Output: The number of ways to tile an `N x 2` grid with dominoes (2x1 tiles) and trominoes (3x2 tiles).
- Key Requirements:
  - Each tile must be used exactly once.
  - No tile can overlap with another tile.
- Edge Cases:
  - When `N` is odd, it is impossible to tile the grid with only dominoes and trominoes.
- Example Test Cases:
  - For `N = 3`, the output is `5`, as there are 5 ways to tile the grid: 
    1. 3 dominoes
    2. 1 tromino and 1 domino (in 4 different positions)

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible combinations of dominoes and trominoes to tile the grid.
- Step-by-step breakdown:
  1. Start with an empty grid.
  2. Try to place a domino or tromino at each position in the grid.
  3. Recursively try to fill the remaining grid with dominoes and trominoes.
  4. Count the number of successful tilings.

```cpp
int numTilings(int N) {
    if (N % 2 == 1) return 0; // If N is odd, it's impossible to tile
    int count = 0;
    vector<vector<bool>> grid(N, vector<bool>(2, false));
    function<void(int, int)> dfs = [&](int row, int col) {
        if (row == N) {
            count++;
            return;
        }
        if (col == 2) {
            dfs(row + 1, 0);
            return;
        }
        if (!grid[row][col]) {
            // Try to place a domino
            if (col == 0 && row < N - 1 && !grid[row + 1][col]) {
                grid[row][col] = true;
                grid[row + 1][col] = true;
                dfs(row, col + 1);
                grid[row][col] = false;
                grid[row + 1][col] = false;
            }
            // Try to place a tromino
            if (col == 0 && row < N - 2 && !grid[row + 1][col] && !grid[row + 2][col]) {
                grid[row][col] = true;
                grid[row + 1][col] = true;
                grid[row + 2][col] = true;
                dfs(row, col + 1);
                grid[row][col] = false;
                grid[row + 1][col] = false;
                grid[row + 2][col] = false;
            }
            dfs(row, col + 1);
        } else {
            dfs(row, col + 1);
        }
    };
    dfs(0, 0);
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{N})$, where `N` is the number of rows. This is because in the worst case, we try all possible combinations of dominoes and trominoes.
> - **Space Complexity:** $O(N)$, for the recursive call stack.
> - **Why these complexities occur:** The brute force approach tries all possible combinations, resulting in an exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use dynamic programming to store the number of ways to tile the grid up to each row.
- Detailed breakdown:
  1. Initialize a `dp` array of size `N + 1`, where `dp[i]` represents the number of ways to tile the grid up to row `i`.
  2. For each row `i`, try to place a domino or tromino, and update `dp[i]` accordingly.
  3. The final answer is `dp[N]`.

```cpp
int numTilings(int N) {
    if (N % 2 == 1) return 0; // If N is odd, it's impossible to tile
    vector<int> dp(N + 1, 0);
    dp[0] = 1; // Base case: 1 way to tile an empty grid
    dp[1] = 1; // Base case: 1 way to tile a grid with 1 row
    dp[2] = 2; // Base case: 2 ways to tile a grid with 2 rows
    for (int i = 3; i <= N; i++) {
        dp[i] = (2 * dp[i - 1] + dp[i - 3]) % 1000000007; // Use modulo to avoid overflow
    }
    return dp[N];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where `N` is the number of rows. This is because we only need to iterate up to `N` to fill the `dp` array.
> - **Space Complexity:** $O(N)$, for the `dp` array.
> - **Optimality proof:** This approach is optimal because it uses dynamic programming to store the number of ways to tile the grid up to each row, avoiding redundant calculations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, recursive backtracking.
- Problem-solving patterns identified: using a `dp` array to store intermediate results, avoiding redundant calculations.
- Optimization techniques learned: using modulo to avoid overflow, avoiding unnecessary recursive calls.
- Similar problems to practice: other dynamic programming problems, such as Fibonacci sequence, Longest Common Subsequence.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases, not using modulo to avoid overflow.
- Edge cases to watch for: when `N` is odd, when `N` is very large.
- Performance pitfalls: using a brute force approach, not using dynamic programming.
- Testing considerations: testing with small inputs to verify correctness, testing with large inputs to verify performance.