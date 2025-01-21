## Capital Gain/Loss
**Problem Link:** https://leetcode.com/problems/capital-gainloss/description

**Problem Statement:**
- Input format and constraints: Given an integer array `prices` where `prices[i]` is the price of a given stock on the `i-th` day. You are allowed to buy and sell the stock at most once to maximize your profit. However, if you sell the stock before buying it, you incur a penalty of `capital_gain`/2. The goal is to find the maximum possible profit.
- Expected output format: The maximum possible profit after considering the penalty.
- Key requirements and edge cases to consider: 
  - The input array `prices` can be empty.
  - The length of the input array `prices` is guaranteed to be less than or equal to 100,000.
  - All elements in the `prices` array are positive integers.
- Example test cases with explanations: 
  - For the input `prices = [1, 3, 2, 8, 4, 9]`, the maximum possible profit is `8`. We can buy the stock on the first day and sell it on the last day, but we have to pay a penalty of `2` because we sold before buying.
  - For the input `prices = [1, 3, 7, 5, 10, 3]`, the maximum possible profit is `6`. We can buy the stock on the third day and sell it on the fifth day.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to try all possible combinations of buying and selling the stock, and then calculate the profit for each combination.
- Step-by-step breakdown of the solution: 
  1. Initialize the maximum profit to `0`.
  2. Iterate over all possible combinations of buying and selling the stock.
  3. For each combination, calculate the profit and subtract the penalty if we sell the stock before buying it.
  4. Update the maximum profit if the current profit is higher.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient because it has a high time complexity.

```cpp
int maxProfit(vector<int>& prices) {
    int n = prices.size();
    int max_profit = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int profit = prices[j] - prices[i];
            if (j < i) {
                profit -= prices[j] / 2;
            }
            max_profit = max(max_profit, profit);
        }
    }
    return max_profit;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input array `prices`. This is because we are using two nested loops to iterate over all possible combinations of buying and selling the stock.
> - **Space Complexity:** $O(1)$, which means the space complexity is constant. This is because we are only using a constant amount of space to store the maximum profit.
> - **Why these complexities occur:** The time complexity is high because we are trying all possible combinations of buying and selling the stock, and the space complexity is low because we are only using a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a single pass through the input array `prices` to keep track of the maximum profit we can get by selling the stock before buying it, and the maximum profit we can get by selling the stock after buying it.
- Detailed breakdown of the approach: 
  1. Initialize the maximum profit to `0`.
  2. Initialize the minimum price to the first price in the input array `prices`.
  3. Initialize the maximum profit after buying the stock to `0`.
  4. Iterate over the input array `prices`.
  5. For each price, update the minimum price if the current price is lower.
  6. Update the maximum profit after buying the stock if the current profit is higher.
  7. Update the maximum profit if the current profit after buying the stock is higher.
- Proof of optimality: This approach is optimal because it only requires a single pass through the input array `prices`, and it keeps track of the maximum profit we can get by selling the stock before buying it and after buying it.

```cpp
int maxProfit(vector<int>& prices) {
    int n = prices.size();
    if (n == 0) {
        return 0;
    }
    int min_price = prices[0];
    int max_profit_after_buy = 0;
    int max_profit = 0;
    for (int i = 1; i < n; i++) {
        max_profit = max(max_profit, prices[i] / 2);
        min_price = min(min_price, prices[i]);
        max_profit_after_buy = max(max_profit_after_buy, prices[i] - min_price);
        max_profit = max(max_profit, max_profit_after_buy);
    }
    return max_profit;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array `prices`. This is because we are only using a single loop to iterate over the input array `prices`.
> - **Space Complexity:** $O(1)$, which means the space complexity is constant. This is because we are only using a constant amount of space to store the maximum profit, the minimum price, and the maximum profit after buying the stock.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the input array `prices`, and it keeps track of the maximum profit we can get by selling the stock before buying it and after buying it.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The optimal approach demonstrates the use of a single pass through the input array to keep track of the maximum profit, and the use of variables to store the minimum price and the maximum profit after buying the stock.
- Problem-solving patterns identified: The problem requires the use of a greedy approach to keep track of the maximum profit, and the use of variables to store the minimum price and the maximum profit after buying the stock.
- Optimization techniques learned: The optimal approach demonstrates the use of a single pass through the input array to reduce the time complexity from $O(n^2)$ to $O(n)$.
- Similar problems to practice: Other problems that involve finding the maximum profit or minimum cost, such as the "Best Time to Buy and Sell Stock" problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the minimum price and the maximum profit after buying the stock correctly, and not updating the maximum profit correctly.
- Edge cases to watch for: The input array `prices` can be empty, and the length of the input array `prices` can be very large.
- Performance pitfalls: Using a brute force approach that has a high time complexity, and not using variables to store the minimum price and the maximum profit after buying the stock.
- Testing considerations: Testing the optimal approach with different input arrays `prices`, including edge cases such as an empty array and an array with a single element.