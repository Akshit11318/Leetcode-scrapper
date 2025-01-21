## New 21 Game
**Problem Link:** https://leetcode.com/problems/new-21-game/description

**Problem Statement:**
- Input format and constraints: The function `new21Game` takes three integers as input: `n`, `k`, and `maxRoll`. `n` is the number of rounds, `k` is the number of rounds to play before the game ends, and `maxRoll` is the maximum roll of the dice.
- Expected output format: The function returns the probability of winning the game, which is a floating-point number between 0 and 1.
- Key requirements and edge cases to consider: If `k` is 0 or `n` is greater than or equal to `k + maxRoll`, the probability of winning is 1. If `n` is less than `k`, the probability of winning is 0.
- Example test cases with explanations:
  - `new21Game(10, 3, 10)`: The probability of winning is the probability of reaching or exceeding `n` (10) within `k` rounds or less. Since `k` is 3 and `maxRoll` is 10, there are several ways to reach or exceed `n` within `k` rounds.
  - `new21Game(6, 1, 6)`: The probability of winning is the probability of reaching or exceeding `n` (6) within `k` rounds or less. Since `k` is 1 and `maxRoll` is 6, there is only one way to reach or exceed `n` within `k` rounds.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves simulating all possible outcomes of the game and counting the number of outcomes where the player wins.
- Step-by-step breakdown of the solution:
  1. Initialize a variable to store the total number of outcomes.
  2. Initialize a variable to store the number of winning outcomes.
  3. Simulate all possible outcomes of the game by iterating over all possible rolls of the dice for each round.
  4. For each outcome, check if the player wins by reaching or exceeding `n` within `k` rounds or less.
  5. If the player wins, increment the number of winning outcomes.
  6. Calculate the probability of winning by dividing the number of winning outcomes by the total number of outcomes.
- Why this approach comes to mind first: The brute force approach is a straightforward way to solve the problem by simulating all possible outcomes and counting the number of winning outcomes.

```cpp
double new21Game(int n, int k, int maxRoll) {
    if (k == 0 || n >= k + maxRoll) {
        return 1.0;
    }
    if (n < k) {
        return 0.0;
    }

    double totalOutcomes = 0;
    double winningOutcomes = 0;

    for (int i = 1; i <= maxRoll; i++) {
        double probability = 1.0 / maxRoll;
        if (i + k - 1 <= n) {
            winningOutcomes += probability;
        }
        totalOutcomes += probability;
    }

    return winningOutcomes;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(maxRoll)$, where `maxRoll` is the maximum roll of the dice. This is because we iterate over all possible rolls of the dice for each round.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the total number of outcomes and the number of winning outcomes.
> - **Why these complexities occur:** The time complexity occurs because we simulate all possible outcomes of the game, which requires iterating over all possible rolls of the dice for each round. The space complexity occurs because we only use a constant amount of space to store the total number of outcomes and the number of winning outcomes.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use dynamic programming to store the probability of winning for each round.
- Detailed breakdown of the approach:
  1. Initialize a dynamic programming array `dp` of size `n + 1`, where `dp[i]` stores the probability of winning at round `i`.
  2. Initialize `dp[0]` to 1, because the probability of winning at round 0 is 1.
  3. For each round `i` from 1 to `n`, calculate the probability of winning at round `i` by summing the probabilities of winning at previous rounds and dividing by `maxRoll`.
  4. If `i` is greater than or equal to `k`, update `dp[i]` to be the sum of the probabilities of winning at previous rounds divided by `maxRoll`.
- Proof of optimality: The optimal approach is optimal because it uses dynamic programming to store the probability of winning for each round, which reduces the time complexity from exponential to linear.
- Why further optimization is impossible: Further optimization is impossible because the optimal approach already uses dynamic programming to store the probability of winning for each round, which is the most efficient way to solve the problem.

```cpp
double new21Game(int n, int k, int maxRoll) {
    if (k == 0 || n >= k + maxRoll) {
        return 1.0;
    }
    if (n < k) {
        return 0.0;
    }

    double dp[k + maxRoll + 1];
    dp[0] = 1.0;

    double sum = 1.0;
    for (int i = 1; i <= n; i++) {
        dp[i] = sum / maxRoll;
        if (i < k) {
            sum += dp[i];
        }
        if (i - k >= 0) {
            sum -= dp[i - k];
        }
    }

    return dp[n];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + maxRoll)$, where `n` is the number of rounds and `maxRoll` is the maximum roll of the dice. This is because we iterate over all rounds and all possible rolls of the dice.
> - **Space Complexity:** $O(k + maxRoll)$, because we use a dynamic programming array of size `k + maxRoll + 1`.
> - **Optimality proof:** The optimal approach is optimal because it uses dynamic programming to store the probability of winning for each round, which reduces the time complexity from exponential to linear.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, probability calculation.
- Problem-solving patterns identified: Using dynamic programming to store the probability of winning for each round.
- Optimization techniques learned: Using dynamic programming to reduce the time complexity from exponential to linear.
- Similar problems to practice: Other dynamic programming problems, such as the Fibonacci sequence or the knapsack problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the dynamic programming array correctly, not updating the probability of winning correctly.
- Edge cases to watch for: The case where `k` is 0 or `n` is greater than or equal to `k + maxRoll`, the case where `n` is less than `k`.
- Performance pitfalls: Using a brute force approach instead of dynamic programming, which can lead to exponential time complexity.
- Testing considerations: Testing the function with different inputs, such as different values of `n`, `k`, and `maxRoll`.