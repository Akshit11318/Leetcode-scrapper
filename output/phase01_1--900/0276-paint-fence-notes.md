## Paint Fence
**Problem Link:** https://leetcode.com/problems/paint-fence/description

**Problem Statement:**
- Input format and constraints: The problem takes two parameters: `n`, the number of fence posts, and `k`, the number of colors available. The constraints are `1 <= n <= 5 * 10^4` and `1 <= k <= 10^5`.
- Expected output format: The function should return the total number of ways to paint the fence.
- Key requirements and edge cases to consider: The key requirement is that no more than two consecutive fence posts can have the same color.
- Example test cases with explanations: For example, if `n = 3` and `k = 2`, the function should return `6`, because the possible ways to paint the fence are `001, 010, 011, 100, 101, 110`, where `0` and `1` represent the two colors.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The initial thought process is to use recursion to try all possible combinations of colors for each fence post.
- Step-by-step breakdown of the solution: Start with the first fence post and try all possible colors. For each color, recursively try all possible colors for the next fence post, and so on.
- Why this approach comes to mind first: This approach comes to mind first because it is a straightforward way to solve the problem, but it is not efficient.

```cpp
int numWays(int n, int k) {
    if (n == 0) return 0;
    if (n == 1) return k;
    vector<vector<int>> dp(n, vector<int>(k, -1));
    function<int(int, int)> dfs = [&](int i, int prev) {
        if (i == n) return 1;
        if (dp[i][prev] != -1) return dp[i][prev];
        int res = 0;
        for (int j = 0; j < k; j++) {
            if (j != prev) {
                res += dfs(i + 1, j);
            }
        }
        return dp[i][prev] = res;
    };
    int res = 0;
    for (int i = 0; i < k; i++) {
        res += dfs(1, i);
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the number of fence posts and $k$ is the number of colors. This is because in the worst case, we need to try all possible colors for each fence post.
> - **Space Complexity:** $O(n \cdot k)$, where $n$ is the number of fence posts and $k$ is the number of colors. This is because we need to store the results of subproblems in the `dp` array.
> - **Why these complexities occur:** These complexities occur because we are using a recursive approach with memoization to solve the problem.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The key insight is that we only need to keep track of the number of ways to paint the previous two fence posts.
- Detailed breakdown of the approach: We can use a dynamic programming approach to solve the problem. Let `dp[i][0]` be the number of ways to paint the first `i` fence posts such that the last two fence posts are different colors, and `dp[i][1]` be the number of ways to paint the first `i` fence posts such that the last two fence posts are the same color.
- Proof of optimality: This approach is optimal because we are only keeping track of the necessary information to compute the next state.
- Why further optimization is impossible: Further optimization is impossible because we need to keep track of the number of ways to paint the previous two fence posts to compute the next state.

```cpp
int numWays(int n, int k) {
    if (n == 0) return 0;
    if (n == 1) return k;
    int same = k;
    int diff = k * (k - 1);
    for (int i = 2; i < n; i++) {
        int temp = diff;
        diff = (same + diff) * (k - 1);
        same = temp;
    }
    return same + diff;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of fence posts. This is because we are using a dynamic programming approach to solve the problem.
> - **Space Complexity:** $O(1)$, because we are only keeping track of a constant amount of information.
> - **Optimality proof:** This approach is optimal because we are only keeping track of the necessary information to compute the next state.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, memoization.
- Problem-solving patterns identified: Using a dynamic programming approach to solve problems that have overlapping subproblems.
- Optimization techniques learned: Using memoization to avoid recomputing the same subproblems.
- Similar problems to practice: Other dynamic programming problems, such as the Fibonacci sequence or the knapsack problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` array correctly, not handling the base cases correctly.
- Edge cases to watch for: The case where `n` is 0 or 1, the case where `k` is 1.
- Performance pitfalls: Using a recursive approach without memoization, using a dynamic programming approach with too much extra space.
- Testing considerations: Testing the function with different values of `n` and `k`, testing the function with edge cases.