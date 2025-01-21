## Sell Diminishing Valued Colored Balls

**Problem Link:** https://leetcode.com/problems/sell-diminishing-valued-colored-balls/description

**Problem Statement:**
- Input: `n` (number of balls) and `orders` (array of orders)
- Constraints: `1 <= n <= 10^6`, `1 <= orders.length <= 10^5`
- Expected Output: Maximum profit achievable
- Key Requirements: Determine the maximum profit that can be obtained by selling `n` balls in decreasing order of their values, given a list of orders where each order specifies the number of balls to sell.
- Edge Cases: Consider cases where `n` is less than or equal to the sum of all orders, and where `n` is greater than the sum of all orders.
- Example Test Cases:
  - `n = 2`, `orders = [2,1,5]`: The maximum profit is `10` because we can sell the balls in decreasing order of their values.
  - `n = 5`, `orders = [3,2]`: The maximum profit is `20` because we can sell the balls in decreasing order of their values.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of selling balls in decreasing order of their values and calculate the profit for each combination.
- Step-by-step breakdown:
  1. Sort the orders in decreasing order.
  2. Iterate over each order and try to sell as many balls as possible.
  3. Calculate the profit for each combination and keep track of the maximum profit.
- Why this approach comes to mind first: It's a straightforward approach that tries to solve the problem by brute force, but it's inefficient and has a high time complexity.

```cpp
int maxProfit(int n, vector<int>& orders) {
    sort(orders.rbegin(), orders.rend());
    int maxProfit = 0;
    for (int i = 0; i < orders.size(); i++) {
        int ballsToSell = min(n, orders[i]);
        maxProfit += (ballsToSell * (ballsToSell + 1)) / 2;
        n -= ballsToSell;
    }
    return maxProfit;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(10^5 \log 10^5)$ due to sorting the orders.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space.
> - **Why these complexities occur:** The time complexity is high because we sort the orders, and the space complexity is low because we only use a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a greedy approach to solve the problem. We should always try to sell the maximum number of balls possible for each order.
- Detailed breakdown:
  1. Sort the orders in decreasing order.
  2. Iterate over each order and calculate the number of balls to sell.
  3. Calculate the profit for each order and add it to the total profit.
- Proof of optimality: This approach is optimal because we always try to sell the maximum number of balls possible for each order, which maximizes the profit.

```cpp
int maxProfit(int n, vector<int>& orders) {
    sort(orders.rbegin(), orders.rend());
    long long maxProfit = 0;
    for (int i = 0; i < orders.size(); i++) {
        int ballsToSell = min(n, orders[i]);
        maxProfit += (long long)(ballsToSell * (ballsToSell + 1)) / 2;
        n -= ballsToSell;
    }
    return (int)maxProfit;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(10^5 \log 10^5)$ due to sorting the orders.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space.
> - **Optimality proof:** This approach is optimal because we always try to sell the maximum number of balls possible for each order, which maximizes the profit.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Greedy algorithm, sorting.
- Problem-solving patterns: Always try to sell the maximum number of balls possible for each order.
- Optimization techniques: Use a greedy approach to maximize the profit.
- Similar problems to practice: Other problems that involve maximizing profit or minimizing cost.

**Mistakes to Avoid:**
- Common implementation errors: Not sorting the orders in decreasing order.
- Edge cases to watch for: Cases where `n` is less than or equal to the sum of all orders, and where `n` is greater than the sum of all orders.
- Performance pitfalls: Using a brute force approach that has a high time complexity.
- Testing considerations: Test the solution with different inputs and edge cases to ensure it works correctly.