## Count Ways to Distribute Candies

**Problem Link:** https://leetcode.com/problems/count-ways-to-distribute-candies/description

**Problem Statement:**
- Input: `n` (number of candies) and `k` (number of bags)
- Constraints: `1 <= k <= n <= 2000`
- Expected Output: Number of ways to distribute `n` candies into `k` bags, where each bag can contain 0 or more candies
- Key Requirements:
  - Each bag can contain any number of candies (including 0), but the total number of candies must be `n`.
  - The order of the bags does not matter, meaning that the distribution `[a, b, c]` is the same as `[c, b, a]`.
- Edge Cases:
  - If `k > n`, there are `0` ways to distribute the candies because we cannot have more bags than candies.
  - If `k == n`, there is `1` way to distribute the candies, where each bag contains exactly `1` candy.
- Example Test Cases:
  - `n = 3`, `k = 2`: There are `3` ways to distribute: `[0, 3]`, `[1, 2]`, and `[2, 1]`.
  - `n = 3`, `k = 3`: There are `10` ways to distribute: `[0, 0, 3]`, `[0, 1, 2]`, `[0, 2, 1]`, `[0, 3, 0]`, `[1, 0, 2]`, `[1, 1, 1]`, `[1, 2, 0]`, `[2, 0, 1]`, `[2, 1, 0]`, and `[3, 0, 0]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves generating all possible combinations of distributing `n` candies into `k` bags.
- We can use nested loops to generate all combinations, where each loop represents the number of candies in a bag.
- However, this approach is inefficient because it generates many duplicate distributions (due to the order of bags not mattering).

```cpp
int countWaysToDistributeCandies(int n, int k) {
    int count = 0;
    // Generate all possible combinations
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= n - i; j++) {
            for (int l = 0; l <= n - i - j; l++) {
                // ... and so on for k bags
                if (i + j + l + ... == n) {
                    count++;
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k^n)$, because we have `k` nested loops, each iterating up to `n` times.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the count.
> - **Why these complexities occur:** The brute force approach is highly inefficient due to the exponential number of iterations.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use dynamic programming to store and reuse the results of subproblems.
- We can define a 2D array `dp` where `dp[i][j]` represents the number of ways to distribute `i` candies into `j` bags.
- We can fill up the `dp` array using the following recurrence relation: `dp[i][j] = dp[i][j-1] + dp[i-j][j]`.

```cpp
int countWaysToDistributeCandies(int n, int k) {
    vector<vector<int>> dp(n + 1, vector<int>(k + 1, 0));
    dp[0][0] = 1;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= min(i, k); j++) {
            dp[i][j] = dp[i][j - 1] + dp[i - j][j];
        }
    }
    return dp[n][k];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(nk)$, because we have two nested loops, each iterating up to `n` and `k` times.
> - **Space Complexity:** $O(nk)$, because we use a 2D array to store the `dp` values.
> - **Optimality proof:** This approach is optimal because it uses dynamic programming to avoid redundant calculations and has a polynomial time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, recurrence relations.
- Problem-solving patterns identified: using a 2D array to store subproblem results.
- Optimization techniques learned: avoiding redundant calculations using dynamic programming.

**Mistakes to Avoid:**
- Common implementation errors: incorrect initialization of the `dp` array, incorrect recurrence relation.
- Edge cases to watch for: handling cases where `k > n`, `k == n`, or `n == 0`.
- Performance pitfalls: using a brute force approach with exponential time complexity.
- Testing considerations: testing the function with different inputs, including edge cases.