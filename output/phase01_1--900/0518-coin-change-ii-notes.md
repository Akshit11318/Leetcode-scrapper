## Coin Change II

**Problem Link:** [https://leetcode.com/problems/coin-change-ii/description](https://leetcode.com/problems/coin-change-ii/description)

**Problem Statement:**
- Input format: `amount` (the target amount) and `coins` (a list of coin denominations)
- Constraints: `1 <= coins.length <= 300`, `1 <= coins[i] <= 5000`, `coins` is sorted in ascending order, `1 <= amount <= 5000`
- Expected output format: The number of combinations that sum up to `amount` using the given `coins`.
- Key requirements: Find the number of ways to make change for the given `amount` using the provided `coins`, allowing each coin to be used any number of times.
- Example test cases:
  - `coins = [1, 2, 5], amount = 5`: The answer is `4` because there are four ways to make change for `5` using `1`, `2`, and `5` coins: `5=5`, `5=2+2+1`, `5=2+1+1+1`, `5=1+1+1+1+1`.
  - `coins = [2], amount = 3`: The answer is `0` because it's impossible to make change for `3` using only `2` coins.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible combinations of coins that sum up to the target `amount`.
- This involves recursive exploration of all possible combinations, which can lead to a lot of repeated work and inefficiency.
- The brute force approach comes to mind first because it directly addresses the problem by trying all possibilities.

```cpp
class Solution {
public:
    int change(int amount, vector<int>& coins) {
        return dfs(coins, amount, 0);
    }
    
    int dfs(vector<int>& coins, int amount, int start) {
        if (amount == 0) return 1; // Found a valid combination
        if (amount < 0) return 0; // Invalid combination
        if (start >= coins.size()) return 0; // No more coins to use
        
        int count = 0;
        // Try using the current coin 0 to amount/coins[start] times
        for (int i = 0; i <= amount / coins[start]; i++) {
            count += dfs(coins, amount - i * coins[start], start + 1);
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$ where $n$ is the number of coins, because in the worst case, we explore all possible combinations of coins.
> - **Space Complexity:** $O(n)$ due to the recursive call stack.
> - **Why these complexities occur:** The brute force approach leads to exponential time complexity due to the recursive exploration of all possible combinations without any optimization to reduce the search space.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is recognizing this problem as a variation of the unbounded knapsack problem, which can be solved using dynamic programming.
- The idea is to build up a table where each cell represents the number of ways to make change for a certain amount using the coins available up to that point.
- This approach avoids the exponential complexity of the brute force method by storing and reusing the results of subproblems.

```cpp
class Solution {
public:
    int change(int amount, vector<int>& coins) {
        vector<int> dp(amount + 1, 0);
        dp[0] = 1; // There is 1 way to make 0 amount: use no coins
        
        for (int coin : coins) {
            for (int i = coin; i <= amount; i++) {
                dp[i] += dp[i - coin];
            }
        }
        
        return dp[amount];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(amount \times n)$ where $n$ is the number of coins, because we fill up the `dp` table in a bottom-up manner.
> - **Space Complexity:** $O(amount)$ for the `dp` table.
> - **Optimality proof:** This dynamic programming approach is optimal because it avoids the redundancy of the brute force method by solving each subproblem only once and storing its result for later use, thus achieving polynomial time complexity.

---

### Final Notes

**Learning Points:**
- The importance of recognizing problem patterns and applying appropriate algorithmic techniques (in this case, dynamic programming for the unbounded knapsack problem).
- The value of optimizing solutions to avoid exponential complexity and improve efficiency.
- The concept of building up solutions from smaller subproblems and storing results to avoid redundant computation.

**Mistakes to Avoid:**
- Failing to recognize the problem as a dynamic programming problem and thus not optimizing the solution.
- Not initializing the base case properly (e.g., `dp[0] = 1`).
- Incorrectly updating the `dp` table, leading to incorrect counts of combinations.
- Not considering the constraints and assumptions of the problem, such as the coins being sorted and the possibility of using each coin any number of times.