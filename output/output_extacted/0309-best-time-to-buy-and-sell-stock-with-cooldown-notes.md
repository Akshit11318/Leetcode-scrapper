## Best Time to Buy and Sell Stock with Cooldown
**Problem Link:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description

**Problem Statement:**
- Input format and constraints: Given an array of integers `prices` where `prices[i]` is the price of a given stock on the `i-th` day. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:
  - You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
  - After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day).
- Expected output format: The maximum profit that can be achieved.
- Key requirements and edge cases to consider: 
  - The input array `prices` is non-empty and contains at least one price.
  - The length of `prices` is less than or equal to 5000.
  - All elements in `prices` are non-negative integers.
- Example test cases with explanations:
  - `prices = [1, 2, 3, 0, 2]`: The maximum profit is `3`, achieved by buying on the first day and selling on the third day, then buying on the fifth day and selling on the same day.
  - `prices = [1]`: The maximum profit is `0`, since there is only one day and no transaction can be made.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The problem can be solved by considering all possible buy and sell combinations while taking into account the cooldown period.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `maxProfit` to store the maximum achievable profit.
  2. Iterate through all possible buy days.
  3. For each buy day, iterate through all possible sell days that are at least two days after the buy day (to account for the cooldown period).
  4. For each sell day, calculate the profit and update `maxProfit` if the calculated profit is higher.
- Why this approach comes to mind first: It is a straightforward and intuitive approach that considers all possible scenarios.

```cpp
int maxProfit(vector<int>& prices) {
    int maxProfit = 0;
    int n = prices.size();
    for (int i = 0; i < n; i++) {
        for (int j = i + 2; j < n; j++) {
            if (prices[j] > prices[i]) {
                maxProfit = max(maxProfit, prices[j] - prices[i]);
            }
        }
    }
    return maxProfit;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of days. This is because we are using nested loops to iterate through all possible buy and sell days.
> - **Space Complexity:** $O(1)$, since we are only using a constant amount of space to store the maximum profit.
> - **Why these complexities occur:** The time complexity is high due to the nested loops, while the space complexity is low because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to solve this problem more efficiently. We can maintain three variables: `buy`, `sell`, and `cooldown`, which represent the maximum profit we can get when we are in the state of buying, selling, or cooling down, respectively.
- Detailed breakdown of the approach:
  1. Initialize `buy`, `sell`, and `cooldown` to negative infinity, 0, and 0, respectively.
  2. Iterate through each day.
  3. For each day, update `buy`, `sell`, and `cooldown` based on the current price and the previous states.
- Proof of optimality: This approach is optimal because it considers all possible states and transitions between them, and it uses dynamic programming to avoid redundant calculations.

```cpp
int maxProfit(vector<int>& prices) {
    int buy = INT_MIN, sell = 0, cooldown = 0;
    for (int price : prices) {
        int newBuy = max(buy, cooldown - price);
        int newSell = max(sell, buy + price);
        int newCooldown = max(cooldown, sell);
        buy = newBuy;
        sell = newSell;
        cooldown = newCooldown;
    }
    return max(sell, cooldown);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of days. This is because we are using a single loop to iterate through all days.
> - **Space Complexity:** $O(1)$, since we are only using a constant amount of space to store the maximum profit.
> - **Optimality proof:** This approach is optimal because it considers all possible states and transitions between them, and it uses dynamic programming to avoid redundant calculations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, state machines.
- Problem-solving patterns identified: Using dynamic programming to solve problems with overlapping subproblems.
- Optimization techniques learned: Avoiding redundant calculations using dynamic programming.
- Similar problems to practice: Other dynamic programming problems, such as the knapsack problem or the Fibonacci sequence.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing variables correctly, not considering all possible states and transitions.
- Edge cases to watch for: Handling the case where the input array is empty or contains only one element.
- Performance pitfalls: Using nested loops or recursive functions without considering the time complexity.
- Testing considerations: Testing the function with different input arrays, including edge cases.