## Maximize Value of Function in a Ball Passing Game
**Problem Link:** https://leetcode.com/problems/maximize-value-of-function-in-a-ball-passing-game/description

**Problem Statement:**
- Input format and constraints: The game involves passing balls between `n` players, with each player `i` having a value `i`. The game starts with player `1`, and each player can pass the ball to any other player `j` where `j` is not the previous player. The goal is to maximize the sum of the values of the players who receive the ball after `k` passes.
- Expected output format: The maximum possible sum of values after `k` passes.
- Key requirements and edge cases to consider: The number of players `n` and the number of passes `k` are given as inputs. We need to handle cases where `k` is large and `n` is small, as well as cases where `n` is large and `k` is small.
- Example test cases with explanations: For example, if `n = 3` and `k = 2`, the maximum sum can be achieved by passing the ball from player `1` to player `2`, then from player `2` to player `3`, resulting in a sum of `2 + 3 = 5`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible sequences of passes and calculate the sum of values for each sequence.
- Step-by-step breakdown of the solution:
  1. Generate all possible sequences of `k` passes.
  2. For each sequence, calculate the sum of values of the players who receive the ball.
  3. Keep track of the maximum sum found.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible solutions, but it is inefficient for large inputs.

```cpp
int maxSumAfterKPasses(int n, int k) {
    int maxSum = 0;
    // Generate all possible sequences of k passes
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (i == j) continue;
            int sum = j;
            int prev = i;
            int curr = j;
            for (int pass = 1; pass < k; pass++) {
                int next = -1;
                int maxVal = -1;
                for (int player = 1; player <= n; player++) {
                    if (player == prev) continue;
                    if (player > maxVal) {
                        maxVal = player;
                        next = player;
                    }
                }
                sum += next;
                prev = curr;
                curr = next;
            }
            maxSum = max(maxSum, sum);
        }
    }
    return maxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^k)$, where $n$ is the number of players and $k$ is the number of passes. This is because we generate all possible sequences of `k` passes.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum sum and the current sequence.
> - **Why these complexities occur:** The brute force approach tries all possible sequences of passes, resulting in an exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The maximum sum can be achieved by passing the ball to the player with the highest value at each step.
- Detailed breakdown of the approach:
  1. Start with player `1`.
  2. At each step, pass the ball to the player with the highest value that is not the previous player.
  3. Repeat step 2 for `k` passes.
- Proof of optimality: This approach is optimal because it maximizes the sum of values at each step, resulting in the maximum possible sum after `k` passes.

```cpp
int maxSumAfterKPasses(int n, int k) {
    int maxSum = 0;
    int curr = 1;
    for (int pass = 0; pass < k; pass++) {
        int next = -1;
        int maxVal = -1;
        for (int player = 1; player <= n; player++) {
            if (player == curr) continue;
            if (player > maxVal) {
                maxVal = player;
                next = player;
            }
        }
        maxSum += next;
        curr = next;
    }
    return maxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(nk)$, where $n` is the number of players and $k` is the number of passes. This is because we iterate over all players at each step.
> - **Space Complexity:** $O(1)`, as we only use a constant amount of space to store the maximum sum and the current player.
> - **Optimality proof:** This approach is optimal because it maximizes the sum of values at each step, resulting in the maximum possible sum after $k$ passes.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy algorithm, dynamic programming.
- Problem-solving patterns identified: Maximization problem, optimal substructure.
- Optimization techniques learned: Reducing the search space, using greedy choices.
- Similar problems to practice: Other maximization problems, such as the `0/1 Knapsack Problem`.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, using incorrect data structures.
- Edge cases to watch for: Large inputs, small inputs, boundary cases.
- Performance pitfalls: Using inefficient algorithms, not optimizing the solution.
- Testing considerations: Testing with different inputs, testing with edge cases.