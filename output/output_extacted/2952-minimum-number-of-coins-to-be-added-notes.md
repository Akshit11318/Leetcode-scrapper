## Minimum Number of Coins to be Added
**Problem Link:** https://leetcode.com/problems/minimum-number-of-coins-to-be-added/description

**Problem Statement:**
- Input: An integer array `coins` representing the denominations of coins available and an integer `amount` representing the target amount.
- Constraints: $1 \leq coins.length \leq 12$, $1 \leq coins[i] \leq 2^{31} - 1$, $coins$ is guaranteed to be a distinct array, and $0 \leq amount \leq 10^4$.
- Expected Output: The minimum number of coins that need to be added to make the total amount possible to achieve using the given coins.
- Key Requirements: Find the minimum number of additional coins required to make every amount from 0 to the target amount achievable.
- Example Test Cases:
  - Input: `coins = [1,2,5], amount = 3`
    - Output: `0` because you can already make every amount from 0 to 3.
  - Input: `coins = [2], amount = 3`
    - Output: `2` because you need 2 additional coins of denomination 1 to make every amount from 0 to 3.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of adding coins to the existing set and check if all amounts can be achieved.
- Step-by-step breakdown of the solution:
  1. Start with the given set of coins.
  2. For each possible additional coin denomination from 1 to the target amount, add it to the set of coins.
  3. Check if all amounts from 0 to the target amount can be achieved with the updated set of coins.
  4. If yes, keep track of the minimum number of additional coins added.
- Why this approach comes to mind first: It's a straightforward way to ensure all amounts can be made by systematically adding coins and checking.

```cpp
class Solution {
public:
    int minCoins(vector<int>& coins, int amount) {
        int minCoinsAdded = INT_MAX;
        for (int i = 1; i <= amount; ++i) {
            vector<bool> canMake(amount + 1, false);
            canMake[0] = true;
            for (int coin : coins) {
                for (int j = coin; j <= amount; ++j) {
                    if (canMake[j - coin]) {
                        canMake[j] = true;
                    }
                }
            }
            int coinsAdded = 0;
            for (int j = 1; j <= amount; ++j) {
                if (!canMake[j]) {
                    coinsAdded++;
                    canMake[j] = true;
                    for (int k = j; k <= amount; ++k) {
                        if (canMake[k - j]) {
                            canMake[k] = true;
                        }
                    }
                }
            }
            minCoinsAdded = min(minCoinsAdded, coinsAdded);
        }
        return minCoinsAdded;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot amount^2)$, where $n$ is the number of coins. This is because for each possible additional coin, we're iterating over all amounts and updating the `canMake` array.
> - **Space Complexity:** $O(amount)$, for storing the `canMake` array.
> - **Why these complexities occur:** The brute force approach involves nested loops over the amounts and coins, leading to a high time complexity, and we need to store the `canMake` array to keep track of achievable amounts.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use dynamic programming to efficiently calculate the minimum number of coins needed to make each amount from 0 to the target amount.
- Detailed breakdown of the approach:
  1. Initialize a dynamic programming array `dp` of size `amount + 1`, where `dp[i]` represents the minimum number of coins needed to make amount `i`.
  2. Initialize all values in `dp` to `amount + 1`, except `dp[0] = 0`, since we need 0 coins to make 0 amount.
  3. Iterate over each coin and update `dp` accordingly. For each coin `c`, iterate from `c` to `amount` and update `dp[i] = min(dp[i], dp[i - c] + 1)`.
  4. The minimum number of coins needed to make the target amount is stored in `dp[amount]`.
- Proof of optimality: This approach ensures we consider the minimum number of coins for each amount, avoiding redundant calculations and ensuring we find the optimal solution.

```cpp
class Solution {
public:
    int minCoins(vector<int>& coins, int amount) {
        vector<int> dp(amount + 1, amount + 1);
        dp[0] = 0;
        for (int coin : coins) {
            for (int i = coin; i <= amount; ++i) {
                dp[i] = min(dp[i], dp[i - coin] + 1);
            }
        }
        if (dp[amount] > amount) return -1; // If cannot make up to amount
        int result = 0;
        for (int i = 1; i <= amount; ++i) {
            if (dp[i] > i) {
                result += dp[i] - i;
            }
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot amount)$, where $n$ is the number of coins. This is because we're iterating over each coin and then over the amounts.
> - **Space Complexity:** $O(amount)$, for storing the `dp` array.
> - **Optimality proof:** This approach ensures we consider the minimum number of coins for each amount, avoiding redundant calculations and ensuring we find the optimal solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming for efficient calculation of minimum coins.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems and solving them efficiently.
- Optimization techniques learned: Using dynamic programming to avoid redundant calculations.
- Similar problems to practice: Other coin change problems, such as the classic coin change problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the dynamic programming array correctly, or not updating it correctly.
- Edge cases to watch for: Handling cases where the target amount cannot be made with the given coins.
- Performance pitfalls: Using a brute force approach that leads to high time complexity.
- Testing considerations: Testing with different inputs, including edge cases, to ensure the solution works correctly.