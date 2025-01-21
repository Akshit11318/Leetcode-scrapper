## Minimum Cost to Buy Apples
**Problem Link:** https://leetcode.com/problems/minimum-cost-to-buy-apples/description

**Problem Statement:**
- Input format: An integer `n`, representing the number of apples to buy.
- Constraints: `1 <= n <= 10^6`.
- Expected output format: The minimum cost to buy `n` apples.
- Key requirements: Calculate the minimum cost to buy `n` apples, considering the cost of buying apples in batches of 6 or individually.
- Example test cases:
  - `n = 6`, minimum cost = 6 (buy one batch of 6 apples)
  - `n = 7`, minimum cost = 7 (buy one batch of 6 apples and one individual apple)

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves trying all possible combinations of buying apples in batches and individually to find the minimum cost.
- Step-by-step breakdown:
  1. Initialize the minimum cost to infinity.
  2. Iterate over all possible numbers of batches (from 0 to `n/6`).
  3. For each number of batches, calculate the remaining number of apples to buy individually.
  4. Calculate the cost for the current combination (6 * number of batches + remaining apples).
  5. Update the minimum cost if the current cost is smaller.
- Why this approach comes to mind first: It's a straightforward, exhaustive search approach.

```cpp
int minCost(int n) {
    int minCost = INT_MAX;
    for (int batches = 0; batches <= n / 6; batches++) {
        int remaining = n - batches * 6;
        int cost = batches * 6 + remaining;
        minCost = min(minCost, cost);
    }
    return minCost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\frac{n}{6})$, as we iterate over all possible numbers of batches.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space to store the minimum cost.
> - **Why these complexities occur:** The time complexity is due to the iteration over all possible numbers of batches, and the space complexity is constant because we only use a fixed amount of space to store the minimum cost.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: We can use dynamic programming to store the minimum cost for each number of apples up to `n`.
- Detailed breakdown:
  1. Initialize a dynamic programming array `dp` of size `n + 1`, where `dp[i]` represents the minimum cost to buy `i` apples.
  2. Initialize the base case: `dp[0] = 0`, as the minimum cost to buy 0 apples is 0.
  3. Iterate over each number of apples `i` from 1 to `n`.
  4. For each `i`, calculate the minimum cost by considering two options: buying `i` apples individually or buying a batch of 6 apples and the remaining apples individually.
  5. Update `dp[i]` with the minimum cost.
- Proof of optimality: This approach is optimal because it considers all possible combinations of buying apples in batches and individually and uses dynamic programming to store the minimum cost for each number of apples.

```cpp
int minCost(int n) {
    vector<int> dp(n + 1);
    dp[0] = 0;
    for (int i = 1; i <= n; i++) {
        int cost = i; // buying i apples individually
        if (i >= 6) {
            cost = min(cost, dp[i - 6] + 6); // buying a batch of 6 apples and the remaining apples individually
        }
        dp[i] = cost;
    }
    return dp[n];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, as we iterate over each number of apples up to `n`.
> - **Space Complexity:** $O(n)$, as we use a dynamic programming array of size `n + 1`.
> - **Optimality proof:** This approach is optimal because it considers all possible combinations of buying apples in batches and individually and uses dynamic programming to store the minimum cost for each number of apples.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Dynamic programming, exhaustive search.
- Problem-solving patterns: Considering all possible combinations, using dynamic programming to store minimum costs.
- Optimization techniques: Using dynamic programming to avoid redundant calculations.
- Similar problems to practice: Other dynamic programming problems, such as the Fibonacci sequence or the knapsack problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the base case correctly, not considering all possible combinations.
- Edge cases to watch for: Handling the case where `n` is 0 or negative.
- Performance pitfalls: Using an inefficient algorithm, such as an exhaustive search without dynamic programming.
- Testing considerations: Testing the function with different inputs, including edge cases.