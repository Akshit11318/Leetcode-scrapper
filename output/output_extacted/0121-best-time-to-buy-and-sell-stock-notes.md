## Best Time to Buy and Sell Stock
**Problem Link:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description

**Problem Statement:**
- Input format and constraints: Given an array of integers `prices` representing the daily price of a stock, find the maximum possible profit that can be achieved by buying and selling the stock once.
- Expected output format: The maximum possible profit.
- Key requirements and edge cases to consider:
  - The input array is not empty.
  - The input array contains only positive integers.
  - The stock can only be bought and sold once.
  - If the input array is empty or the stock cannot be bought and sold for a profit, return 0.
- Example test cases with explanations:
  - Input: `prices = [7,1,5,3,6,4]`
    - Output: `5`
    - Explanation: Buy on day 2 (price=1) and sell on day 5 (price=6), profit = 6-1 = 5.
  - Input: `prices = [7,6,4,3,1]`
    - Output: `0`
    - Explanation: The stock cannot be bought and sold for a profit, so return 0.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of buying and selling days to find the maximum profit.
- Step-by-step breakdown of the solution:
  1. Initialize the maximum profit to 0.
  2. Iterate over all possible buying days.
  3. For each buying day, iterate over all possible selling days after the buying day.
  4. Calculate the profit for each buying-selling day combination.
  5. Update the maximum profit if the current profit is higher.
- Why this approach comes to mind first: It's a straightforward way to solve the problem by trying all possible combinations.

```cpp
int maxProfit(vector<int>& prices) {
    int max_profit = 0;
    for (int i = 0; i < prices.size(); i++) {
        for (int j = i + 1; j < prices.size(); j++) {
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
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of days. This is because we have two nested loops that iterate over all possible buying-selling day combinations.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum profit.
> - **Why these complexities occur:** The brute force approach has a high time complexity because it tries all possible combinations, resulting in a quadratic number of operations. The space complexity is low because we only need to store a single variable to keep track of the maximum profit.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can keep track of the minimum price seen so far and update the maximum profit whenever we find a higher profit.
- Detailed breakdown of the approach:
  1. Initialize the minimum price to the first price in the array.
  2. Initialize the maximum profit to 0.
  3. Iterate over the prices array.
  4. For each price, update the minimum price if the current price is lower.
  5. Calculate the current profit by subtracting the minimum price from the current price.
  6. Update the maximum profit if the current profit is higher.
- Proof of optimality: This approach is optimal because it only requires a single pass through the prices array, resulting in a linear time complexity.

```cpp
int maxProfit(vector<int>& prices) {
    if (prices.empty()) return 0;
    int min_price = prices[0];
    int max_profit = 0;
    for (int i = 1; i < prices.size(); i++) {
        if (prices[i] < min_price) {
            min_price = prices[i];
        } else if (prices[i] - min_price > max_profit) {
            max_profit = prices[i] - min_price;
        }
    }
    return max_profit;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of days. This is because we only need to make a single pass through the prices array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum price and maximum profit.
> - **Optimality proof:** This approach is optimal because it has a linear time complexity, which is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional statements, and optimization techniques.
- Problem-solving patterns identified: Keeping track of minimum and maximum values to optimize the solution.
- Optimization techniques learned: Reducing the number of operations by avoiding unnecessary comparisons.
- Similar problems to practice: Other optimization problems, such as finding the maximum subarray sum or the minimum window substring.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty input array.
- Edge cases to watch for: Empty input array, single-element input array, and input array with all elements being the same.
- Performance pitfalls: Using a brute force approach with a high time complexity.
- Testing considerations: Test the solution with different input arrays, including edge cases, to ensure it produces the correct output.