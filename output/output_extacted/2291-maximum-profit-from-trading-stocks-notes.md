## Maximum Profit from Trading Stocks
**Problem Link:** https://leetcode.com/problems/maximum-profit-from-trading-stocks/description

**Problem Statement:**
- Input: An array of integers representing stock prices over time, with constraints on the number of transactions allowed (e.g., at most one or two transactions).
- Expected Output: The maximum possible profit from buying and selling stocks, given the constraints.
- Key Requirements: Identify the optimal buy and sell points to maximize profit, considering the constraints on transactions.
- Edge Cases: Handle scenarios with no profit possible (e.g., prices always decreasing), and consider the impact of transaction limits.

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible combinations of buy and sell points, considering the constraints on transactions.
- Step-by-step breakdown: Iterate over all possible buy points, then for each buy point, iterate over all possible sell points that come after it, and calculate the profit for each combination.
- Why this approach comes to mind first: It's straightforward and ensures all possibilities are considered, but it's inefficient due to its exhaustive nature.

```cpp
int maxProfit(vector<int>& prices) {
    int max_profit = 0;
    for (int i = 0; i < prices.size(); ++i) {
        for (int j = i + 1; j < prices.size(); ++j) {
            int profit = prices[j] - prices[i];
            if (profit > max_profit) {
                max_profit = profit;
            }
        }
    }
    return max_profit;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of days (prices), because we have two nested loops iterating over the prices.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum profit.
> - **Why these complexities occur:** The brute force approach is inherently inefficient due to its exhaustive search, leading to a quadratic time complexity.

### Optimal Approach (Required)
**Explanation:**
- Key insight: We only need to keep track of the minimum price seen so far and the maximum profit that can be achieved by selling at the current price.
- Detailed breakdown: Initialize `min_price` to the first price and `max_profit` to 0. Iterate over the prices; for each price, update `min_price` if the current price is lower, and update `max_profit` if selling at the current price (after buying at `min_price`) would yield a higher profit.
- Proof of optimality: This approach is optimal because it ensures we consider the best possible buy point for every potential sell point, without needing to exhaustively compare all pairs of prices.

```cpp
int maxProfit(vector<int>& prices) {
    if (prices.empty()) return 0;
    int min_price = prices[0];
    int max_profit = 0;
    for (int price : prices) {
        if (price < min_price) {
            min_price = price;
        } else if (price - min_price > max_profit) {
            max_profit = price - min_price;
        }
    }
    return max_profit;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of days (prices), because we make a single pass through the prices.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space to store `min_price` and `max_profit`.
> - **Optimality proof:** This approach is optimal because it achieves the best possible time complexity for this problem by only requiring a single pass through the data and using a constant amount of extra space.

### Final Notes
**Learning Points:**
- Key algorithmic concept: Greedy algorithms can be used to solve problems where the optimal solution can be constructed from locally optimal choices.
- Problem-solving pattern: Look for opportunities to reduce the problem size or complexity by making a single pass through the data.
- Optimization technique: Avoid unnecessary comparisons by keeping track of the minimum or maximum values seen so far.

**Mistakes to Avoid:**
- Common implementation error: Failing to handle edge cases, such as an empty input array.
- Performance pitfall: Using a brute force approach for problems that can be solved more efficiently with a greedy algorithm or dynamic programming.
- Testing consideration: Ensure to test the solution with various inputs, including edge cases, to verify its correctness and robustness.