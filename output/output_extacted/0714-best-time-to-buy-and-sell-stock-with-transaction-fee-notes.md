## Best Time to Buy and Sell Stock with Transaction Fee
**Problem Link:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description

**Problem Statement:**
- Input format: An array of integers `prices` representing the stock price on each day and an integer `fee` representing the transaction fee.
- Constraints: `1 <= prices.length <= 5 * 10^4`, `1 <= prices[i] <= 10^9`, `0 <= fee <= 10^9`.
- Expected output format: The maximum profit that can be achieved.
- Key requirements: Buy and sell stock with a transaction fee, find the maximum possible profit.
- Example test cases:
  - `prices = [1, 3, 2, 8, 4, 9], fee = 2`, expected output: `8`.
  - `prices = [1, 3, 7, 5, 10, 3], fee = 3`, expected output: `6`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible buy and sell combinations to find the maximum profit.
- Step-by-step breakdown:
  1. Iterate over each day to buy the stock.
  2. For each buy day, iterate over the remaining days to sell the stock.
  3. Calculate the profit for each buy-sell combination, considering the transaction fee.
  4. Update the maximum profit if the current profit is higher.
- Why this approach comes to mind first: It's the most straightforward way to solve the problem, but it's inefficient due to the nested loops.

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        int maxProfit = 0;
        for (int i = 0; i < prices.size(); i++) {
            for (int j = i + 1; j < prices.size(); j++) {
                int profit = prices[j] - prices[i] - fee;
                if (profit > 0) {
                    maxProfit = max(maxProfit, profit);
                }
            }
        }
        return maxProfit;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of days, because of the nested loops.
> - **Space Complexity:** $O(1)$, as only a constant amount of space is used.
> - **Why these complexities occur:** The nested loops cause the time complexity to be quadratic, while the space complexity is constant because no additional data structures are used.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use dynamic programming to keep track of the maximum profit at each day, considering two states: holding the stock and not holding the stock.
- Detailed breakdown:
  1. Initialize two variables: `cash` to store the maximum profit when not holding the stock, and `hold` to store the maximum profit when holding the stock.
  2. Iterate over each day, updating `cash` and `hold` based on the current price and the previous state.
  3. At each step, choose the maximum profit between the current state and the new state after buying or selling the stock.
- Proof of optimality: This approach has a linear time complexity and considers all possible buy and sell combinations, making it optimal.

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        int cash = 0, hold = -prices[0];
        for (int i = 1; i < prices.size(); i++) {
            cash = max(cash, hold + prices[i] - fee);
            hold = max(hold, cash - prices[i]);
        }
        return cash;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of days, because of the single loop.
> - **Space Complexity:** $O(1)$, as only a constant amount of space is used.
> - **Optimality proof:** This approach has a linear time complexity and considers all possible buy and sell combinations, making it optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming and state machines.
- Problem-solving patterns identified: Using dynamic programming to solve problems with overlapping subproblems.
- Optimization techniques learned: Reducing time complexity from quadratic to linear using dynamic programming.
- Similar problems to practice: Other dynamic programming problems, such as the knapsack problem or the longest common subsequence problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing variables correctly or not considering all possible states.
- Edge cases to watch for: Handling cases where the input array is empty or the transaction fee is zero.
- Performance pitfalls: Using nested loops instead of dynamic programming, leading to a higher time complexity.
- Testing considerations: Testing the solution with different input cases, including edge cases and large inputs.