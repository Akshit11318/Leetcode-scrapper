## Coin Change
**Problem Link:** https://leetcode.com/problems/coin-change/description

**Problem Statement:**
- Input format: An integer `amount` and a list of integers `coins` representing denominations of coins.
- Constraints: `1 <= coins.length <= 12`, `1 <= coins[i] <= 2^31 - 1`, `coins` contains distinct integers, `1 <= amount <= 2^31 - 1`.
- Expected output format: The fewest number of coins that you need to make up that amount. If that's not possible with the given coin denominations, return `-1`.
- Key requirements: Find the minimum number of coins to make the given amount using the provided denominations.
- Example test cases: 
    - Input: `amount = 11`, `coins = [1,2,5]`
    - Output: `3` (Explanation: `5 + 5 + 1 = 11`)
    - Input: `amount = 3`, `coins = [2]`
    - Output: `-1` (Explanation: It's not possible to make up the amount `3` with the coin denomination `2`)

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible combinations of coins to find the minimum number that sums up to the given amount.
- Step-by-step breakdown of the solution:
    1. Start with an empty set of coins.
    2. Iterate through all possible combinations of coins (using recursion or backtracking).
    3. For each combination, check if the sum equals the given amount.
    4. If a combination sums up to the amount, update the minimum count if this combination uses fewer coins than the current minimum.
- Why this approach comes to mind first: It's the most straightforward way to ensure we consider all possibilities, but it's highly inefficient due to its exponential time complexity.

```cpp
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int minCoins = INT_MAX;
        dfs(coins, amount, 0, minCoins);
        return minCoins == INT_MAX ? -1 : minCoins;
    }
    
    void dfs(vector<int>& coins, int remaining, int count, int& minCoins) {
        if (remaining == 0) {
            minCoins = min(minCoins, count);
            return;
        }
        if (remaining < 0 || count >= minCoins) return;
        
        for (int coin : coins) {
            dfs(coins, remaining - coin, count + 1, minCoins);
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{amount})$, where `amount` is the target amount. This is because in the worst-case scenario, we might have to explore all possible combinations of coins, leading to exponential time complexity.
> - **Space Complexity:** $O(amount)$, due to the recursive call stack. The maximum depth of the recursion tree is `amount`, as we decrease the remaining amount by at least 1 in each recursive call.
> - **Why these complexities occur:** The brute force approach involves exploring all possible combinations of coins, which leads to exponential time complexity. The space complexity is due to the recursive call stack.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Use dynamic programming to store and reuse the results of subproblems, avoiding redundant computations.
- Detailed breakdown of the approach:
    1. Initialize a `dp` array of size `amount + 1` with all elements set to `INT_MAX`, except for `dp[0] = 0`.
    2. Iterate through each coin denomination.
    3. For each coin, iterate from the coin's value up to the target amount.
    4. Update `dp[i]` with the minimum of its current value and `dp[i - coin] + 1`, if `dp[i - coin]` is not `INT_MAX`.
- Proof of optimality: This approach ensures that we consider all possible combinations of coins while avoiding redundant computations, resulting in a significant reduction in time complexity.
- Why further optimization is impossible: This dynamic programming approach has a time complexity of $O(amount \times n)$, where `n` is the number of coin denominations, which is the best we can achieve for this problem.

```cpp
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount + 1, INT_MAX);
        dp[0] = 0;
        
        for (int coin : coins) {
            for (int i = coin; i <= amount; i++) {
                if (dp[i - coin] != INT_MAX) {
                    dp[i] = min(dp[i], dp[i - coin] + 1);
                }
            }
        }
        
        return dp[amount] == INT_MAX ? -1 : dp[amount];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(amount \times n)$, where `amount` is the target amount and `n` is the number of coin denominations. This is because we have two nested loops, one iterating over the coin denominations and the other over the range from the coin's value to the target amount.
> - **Space Complexity:** $O(amount)$, as we need to store the `dp` array of size `amount + 1`.
> - **Optimality proof:** The dynamic programming approach ensures that we consider all possible combinations of coins while avoiding redundant computations, resulting in a significant reduction in time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, memoization, and optimization techniques.
- Problem-solving patterns identified: Breaking down the problem into subproblems, storing and reusing results, and avoiding redundant computations.
- Optimization techniques learned: Using dynamic programming to reduce time complexity.
- Similar problems to practice: Other dynamic programming problems, such as the **0/1 Knapsack Problem** and the **Longest Common Subsequence Problem**.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` array correctly, not handling edge cases, and not updating the `dp` array correctly.
- Edge cases to watch for: When the target amount is 0, when the coin denominations are empty, and when the target amount is negative.
- Performance pitfalls: Using a brute force approach, not using memoization, and not optimizing the dynamic programming approach.
- Testing considerations: Test the solution with different input cases, including edge cases, to ensure correctness and performance.