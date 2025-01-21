## Paths in Matrix Whose Sum is Divisible by K

**Problem Link:** https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/description

**Problem Statement:**
- Input format: A 2D integer array `grid` and an integer `k`.
- Constraints: The number of rows in the grid is in the range $[1, 30]$, the number of columns in the grid is in the range $[1, 1000]$, $-100 \leq grid[i][j] \leq 100$, and $1 \leq k \leq 100$.
- Expected output format: The number of paths in the matrix whose sum is divisible by `k`.
- Key requirements and edge cases to consider: The sum of each path must be divisible by `k`, and we need to find all possible paths in the matrix.
- Example test cases with explanations: For example, given a grid `[[5,-4],[3,-3]]` and `k = 7`, the output should be `3` because there are three paths whose sum is divisible by `7`: `5`, `5 + (-4) + (-3)`, and `(-4) + (-3)`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to solve this problem is to try all possible paths in the matrix and check if the sum of each path is divisible by `k`.
- Step-by-step breakdown of the solution:
  1. Define a recursive function to explore all possible paths in the matrix.
  2. In each recursive call, add the current cell's value to the current sum and check if it's divisible by `k`.
  3. If the current sum is divisible by `k`, increment the count of valid paths.
  4. Explore all four directions (up, down, left, right) from the current cell.
- Why this approach comes to mind first: It's a natural way to think about the problem, as we need to explore all possible paths in the matrix.

```cpp
int numberOfPaths(vector<vector<int>>& grid, int k) {
    int m = grid.size();
    int n = grid[0].size();
    int count = 0;

    function<void(int, int, int)> dfs = [&](int i, int j, int sum) {
        if (i < 0 || i >= m || j < 0 || j >= n) return;
        sum = (sum + grid[i][j]) % k;
        if (sum == 0) count++;
        dfs(i + 1, j, sum);
        dfs(i - 1, j, sum);
        dfs(i, j + 1, sum);
        dfs(i, j - 1, sum);
    };

    dfs(0, 0, 0);
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(4^{m \cdot n})$, where $m$ and $n$ are the number of rows and columns in the grid, respectively. This is because in the worst case, we need to explore all possible paths in the matrix.
> - **Space Complexity:** $O(m \cdot n)$, which is the maximum depth of the recursive call stack.
> - **Why these complexities occur:** The time complexity is exponential because we're exploring all possible paths in the matrix, and the space complexity is linear because of the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to store the number of paths that end at each cell with a given sum modulo `k`.
- Detailed breakdown of the approach:
  1. Create a 3D DP array `dp` of size $m \times n \times k$, where `dp[i][j][sum]` stores the number of paths that end at cell `(i, j)` with a sum of `sum` modulo `k`.
  2. Initialize the DP array by setting `dp[0][0][grid[0][0] % k] = 1`.
  3. Iterate over each cell in the grid, and for each cell, iterate over all possible sums modulo `k`.
  4. For each sum, update the DP array by adding the number of paths that end at the current cell with the current sum.
- Proof of optimality: This approach is optimal because we're using dynamic programming to store and reuse the results of subproblems, which reduces the time complexity from exponential to polynomial.

```cpp
int numberOfPaths(vector<vector<int>>& grid, int k) {
    int m = grid.size();
    int n = grid[0].size();
    int count = 0;

    vector<vector<vector<int>>> dp(m, vector<vector<int>>(n, vector<int>(k, 0)));
    dp[0][0][grid[0][0] % k] = 1;

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            for (int sum = 0; sum < k; sum++) {
                if (i > 0) dp[i][j][sum] += dp[i - 1][j][sum];
                if (j > 0) dp[i][j][sum] += dp[i][j - 1][sum];
                if (i > 0 && j > 0) dp[i][j][sum] -= dp[i - 1][j - 1][sum];
                if (dp[i][j][sum] > 0 && (grid[i][j] + sum) % k == 0) count++;
            }
        }
    }

    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot k)$, where $m$ and $n$ are the number of rows and columns in the grid, respectively, and $k$ is the modulo value.
> - **Space Complexity:** $O(m \cdot n \cdot k)$, which is the size of the DP array.
> - **Optimality proof:** This approach is optimal because we're using dynamic programming to store and reuse the results of subproblems, which reduces the time complexity from exponential to polynomial.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, recursive functions, and modulo arithmetic.
- Problem-solving patterns identified: Using dynamic programming to store and reuse the results of subproblems, and using recursive functions to explore all possible paths.
- Optimization techniques learned: Using dynamic programming to reduce the time complexity from exponential to polynomial.
- Similar problems to practice: Problems that involve exploring all possible paths in a grid or matrix, such as finding the shortest path or the maximum sum.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the DP array correctly, or not updating the DP array correctly.
- Edge cases to watch for: Handling the case where the grid is empty, or handling the case where the modulo value is 1.
- Performance pitfalls: Not using dynamic programming to store and reuse the results of subproblems, which can lead to exponential time complexity.
- Testing considerations: Testing the function with different inputs, such as different grid sizes and modulo values, to ensure that it works correctly.