## Count Houses in a Circular Street II

**Problem Link:** https://leetcode.com/problems/count-houses-in-a-circular-street-ii/description

**Problem Statement:**
- Input format and constraints: The problem involves counting the number of ways to paint houses in a circular street with `n` houses, each of which can be painted with one of `k` colors. The constraint is that no two adjacent houses can have the same color.
- Expected output format: The expected output is the total number of ways to paint the houses.
- Key requirements and edge cases to consider: The key requirement is to ensure that no two adjacent houses have the same color. Edge cases include when `n` is 0 or `k` is 1.
- Example test cases with explanations:
  - If `n = 3` and `k = 2`, there are 2 ways to paint the houses: (1, 2, 1) and (2, 1, 2).
  - If `n = 3` and `k = 3`, there are 6 ways to paint the houses: (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), and (3, 2, 1).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves trying all possible combinations of colors for the houses and counting the valid combinations.
- Step-by-step breakdown of the solution:
  1. Initialize a counter for the number of valid combinations.
  2. Iterate over all possible combinations of colors for the houses.
  3. For each combination, check if it is valid (i.e., no two adjacent houses have the same color).
  4. If the combination is valid, increment the counter.
- Why this approach comes to mind first: The brute force approach is often the most straightforward solution, but it can be inefficient for large inputs.

```cpp
int countWays(int n, int k) {
    int count = 0;
    for (int i = 0; i < pow(k, n); i++) {
        vector<int> colors(n);
        for (int j = 0; j < n; j++) {
            colors[j] = (i / pow(k, j)) % k;
        }
        bool valid = true;
        for (int j = 0; j < n; j++) {
            if (colors[j] == colors[(j + 1) % n]) {
                valid = false;
                break;
            }
        }
        if (valid) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k^n)$, where $n$ is the number of houses and $k$ is the number of colors. This is because we are trying all possible combinations of colors.
> - **Space Complexity:** $O(n)$, where $n$ is the number of houses. This is because we need to store the colors of the houses.
> - **Why these complexities occur:** The time complexity occurs because we are trying all possible combinations of colors, and the space complexity occurs because we need to store the colors of the houses.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is that we can use dynamic programming to solve the problem. We can keep track of the number of ways to paint the houses up to each position, and use this information to calculate the number of ways to paint the houses up to the next position.
- Detailed breakdown of the approach:
  1. Initialize a 2D array `dp` of size `(n + 1) x k`, where `dp[i][j]` represents the number of ways to paint the first `i` houses with the last house painted with color `j`.
  2. Initialize the base case: `dp[1][j] = 1` for all `j`, because there is only one way to paint the first house with each color.
  3. Iterate over the houses from the second house to the last house.
  4. For each house, iterate over all possible colors.
  5. For each color, calculate the number of ways to paint the house with that color by summing the number of ways to paint the previous house with all other colors.
  6. Store the result in `dp[i][j]`.
  7. Finally, calculate the total number of ways to paint all houses by summing the number of ways to paint the last house with all colors.
- Proof of optimality: The dynamic programming approach is optimal because it avoids recalculating the same subproblems multiple times, which reduces the time complexity from exponential to polynomial.

```cpp
int countWays(int n, int k) {
    if (n == 0) {
        return 0;
    }
    if (k == 1) {
        return n == 1 ? 1 : 0;
    }
    vector<vector<int>> dp(n + 1, vector<int>(k, 0));
    for (int j = 0; j < k; j++) {
        dp[1][j] = 1;
    }
    for (int i = 2; i <= n; i++) {
        for (int j = 0; j < k; j++) {
            for (int prev = 0; prev < k; prev++) {
                if (prev != j) {
                    dp[i][j] += dp[i - 1][prev];
                }
            }
        }
    }
    if (n == 1) {
        return k;
    }
    int total = 0;
    for (int j = 0; j < k; j++) {
        for (int prev = 0; prev < k; prev++) {
            if (prev != j) {
                total += dp[n - 1][prev];
            }
        }
    }
    return total / k;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k^2)$, where $n$ is the number of houses and $k$ is the number of colors. This is because we are using dynamic programming to avoid recalculating the same subproblems multiple times.
> - **Space Complexity:** $O(n \cdot k)$, where $n$ is the number of houses and $k$ is the number of colors. This is because we need to store the number of ways to paint the houses up to each position.
> - **Optimality proof:** The dynamic programming approach is optimal because it avoids recalculating the same subproblems multiple times, which reduces the time complexity from exponential to polynomial.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, which is used to avoid recalculating the same subproblems multiple times.
- Problem-solving patterns identified: The problem can be solved by breaking it down into smaller subproblems and solving each subproblem only once.
- Optimization techniques learned: Dynamic programming is used to optimize the solution by avoiding redundant calculations.
- Similar problems to practice: Other problems that can be solved using dynamic programming, such as the Fibonacci sequence or the knapsack problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the base case correctly, or not updating the `dp` array correctly.
- Edge cases to watch for: The case where `n` is 0 or `k` is 1, which requires special handling.
- Performance pitfalls: Not using dynamic programming to avoid recalculating the same subproblems multiple times, which can lead to exponential time complexity.
- Testing considerations: Testing the solution with different inputs, including edge cases, to ensure that it works correctly.