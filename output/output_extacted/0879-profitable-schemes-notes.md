## Profitable Schemes

**Problem Link:** [https://leetcode.com/problems/profitable-schemes/description](https://leetcode.com/problems/profitable-schemes/description)

**Problem Statement:**
- Input format: `n`, `minProfit`, `group`, `profit`
- Constraints: `1 <= n <= 100`, `0 <= minProfit <= 100`, `1 <= group.length == profit.length <= 100`, `1 <= group[i] <= 100`, `0 <= profit[i] <= 100`
- Expected output format: The number of ways to make a profit of at least `minProfit`
- Key requirements and edge cases to consider: Consider all possible combinations of jobs to maximize profit
- Example test cases with explanations:
  - Example 1: `n = 5`, `minProfit = 3`, `group = [2,2]`, `profit = [2,3]`. There are 2 ways to make a profit of at least 3.
  - Example 2: `n = 10`, `minProfit = 5`, `group = [2,3,5]`, `profit = [6,7,8]`. There are 7 ways to make a profit of at least 5.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of jobs to maximize profit
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of jobs
  2. For each combination, calculate the total profit and the number of people required
  3. If the total profit is greater than or equal to `minProfit` and the number of people required is less than or equal to `n`, increment the count of ways to make a profit of at least `minProfit`
- Why this approach comes to mind first: It is a straightforward approach to try all possible combinations of jobs to maximize profit

```cpp
#include <iostream>
#include <vector>

int profitableSchemes(int n, int minProfit, std::vector<int>& group, std::vector<int>& profit) {
    int count = 0;
    int totalWays = 1 << group.size();
    for (int i = 0; i < totalWays; i++) {
        int totalProfit = 0;
        int totalPeople = 0;
        for (int j = 0; j < group.size(); j++) {
            if ((i & (1 << j)) != 0) {
                totalProfit += profit[j];
                totalPeople += group[j];
            }
        }
        if (totalProfit >= minProfit && totalPeople <= n) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^m)$, where $m$ is the number of jobs. This is because we are generating all possible combinations of jobs.
> - **Space Complexity:** $O(1)$, as we are not using any extra space that scales with the input size.
> - **Why these complexities occur:** The time complexity occurs because we are trying all possible combinations of jobs, and the space complexity occurs because we are not using any extra space that scales with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use dynamic programming to store the number of ways to make a profit of at least `minProfit` for each possible number of people
- Detailed breakdown of the approach:
  1. Create a 2D array `dp` of size `(n + 1) x (minProfit + 1)` to store the number of ways to make a profit of at least `minProfit` for each possible number of people
  2. Initialize the base case where the number of people is 0
  3. For each job, update the `dp` array by adding the number of ways to make a profit of at least `minProfit` for the current number of people
- Proof of optimality: This approach is optimal because it uses dynamic programming to store the number of ways to make a profit of at least `minProfit` for each possible number of people, avoiding redundant calculations
- Why further optimization is impossible: This approach is already optimal because it uses dynamic programming to store the number of ways to make a profit of at least `minProfit` for each possible number of people

```cpp
#include <iostream>
#include <vector>

int profitableSchemes(int n, int minProfit, std::vector<int>& group, std::vector<int>& profit) {
    const int MOD = 1e9 + 7;
    int m = group.size();
    std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1, 0));
    dp[0][0] = 1;
    for (int i = 1; i <= m; i++) {
        for (int j = 0; j <= n; j++) {
            dp[i][j] = dp[i - 1][j];
            if (j >= group[i - 1]) {
                dp[i][j] = (dp[i][j] + dp[i - 1][j - group[i - 1]]) % MOD;
            }
        }
    }
    int count = 0;
    for (int i = 0; i <= n; i++) {
        if (i >= minProfit) {
            count = (count + dp[m][i]) % MOD;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of jobs and $n$ is the number of people. This is because we are using dynamic programming to store the number of ways to make a profit of at least `minProfit` for each possible number of people.
> - **Space Complexity:** $O(m \cdot n)$, as we are using a 2D array to store the number of ways to make a profit of at least `minProfit` for each possible number of people.
> - **Optimality proof:** This approach is optimal because it uses dynamic programming to store the number of ways to make a profit of at least `minProfit` for each possible number of people, avoiding redundant calculations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, combinatorics
- Problem-solving patterns identified: Using dynamic programming to store the number of ways to make a profit of at least `minProfit` for each possible number of people
- Optimization techniques learned: Using dynamic programming to avoid redundant calculations
- Similar problems to practice: [Knapsack Problem](https://leetcode.com/problems/combination-sum-iv/), [Coin Change Problem](https://leetcode.com/problems/coin-change/)

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the base case correctly, not updating the `dp` array correctly
- Edge cases to watch for: When the number of people is 0, when the number of jobs is 0
- Performance pitfalls: Not using dynamic programming to store the number of ways to make a profit of at least `minProfit` for each possible number of people
- Testing considerations: Test the function with different inputs, including edge cases and large inputs.