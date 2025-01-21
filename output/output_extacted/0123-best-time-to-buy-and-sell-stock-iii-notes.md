## Best Time to Buy and Sell Stock III
**Problem Link:** [https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description)

**Problem Statement:**
- Input: An array `prices` of integers representing the daily stock prices.
- Output: The maximum possible profit after at most two transactions (i.e., buying and selling).
- Key requirements and edge cases to consider: 
  - The stock can only be sold after it is bought.
  - There can be at most two transactions.
  - No stock is owned at the beginning and end.
- Example test cases with explanations:
  - `prices = [3,3,5,0,0,3,1,4]`: The maximum profit is `6`, achieved by buying at `3`, selling at `5`, buying at `0`, and selling at `4`.
  - `prices = [1,2,3,4,5]`: The maximum profit is `4`, achieved by buying at `1` and selling at `5`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to try all possible combinations of buying and selling.
- Step-by-step breakdown:
  1. Generate all possible buy-sell pairs for the first transaction.
  2. For each pair, generate all possible buy-sell pairs for the second transaction, ensuring the second buy is after the first sell.
  3. Calculate the profit for each combination and keep track of the maximum.

```cpp
int maxProfit(vector<int>& prices) {
    int n = prices.size();
    int maxProfit = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int profit1 = prices[j] - prices[i];
            if (profit1 > 0) {
                for (int k = j + 1; k < n; k++) {
                    for (int l = k + 1; l < n; l++) {
                        int profit2 = prices[l] - prices[k];
                        if (profit2 > 0) {
                            maxProfit = max(maxProfit, profit1 + profit2);
                        }
                    }
                }
            }
        }
    }
    return maxProfit;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^4)$, where $n$ is the number of days, due to four nested loops.
> - **Space Complexity:** $O(1)$, as only a constant amount of space is used.
> - **Why these complexities occur:** The brute force approach tries all possible combinations of buying and selling, leading to an exponential time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use dynamic programming to keep track of the maximum profit after the first buy, first sell, second buy, and second sell.
- Detailed breakdown:
  1. Initialize variables to store the maximum profit after the first buy (`buy1`), first sell (`sell1`), second buy (`buy2`), and second sell (`sell2`).
  2. Iterate through the prices, updating `buy1`, `sell1`, `buy2`, and `sell2` based on the maximum profit that can be achieved at each step.
  3. Return `sell2`, which represents the maximum possible profit after at most two transactions.

```cpp
int maxProfit(vector<int>& prices) {
    int buy1 = INT_MIN, sell1 = 0, buy2 = INT_MIN, sell2 = 0;
    for (int price : prices) {
        buy1 = max(buy1, -price);
        sell1 = max(sell1, buy1 + price);
        buy2 = max(buy2, sell1 - price);
        sell2 = max(sell2, buy2 + price);
    }
    return sell2;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of days, due to a single pass through the prices.
> - **Space Complexity:** $O(1)$, as only a constant amount of space is used.
> - **Optimality proof:** This approach is optimal because it considers all possible buy-sell combinations and keeps track of the maximum profit that can be achieved at each step.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, greedy algorithm.
- Problem-solving patterns identified: Using variables to keep track of the maximum profit after each step.
- Optimization techniques learned: Reducing the time complexity from $O(n^4)$ to $O(n)$ by using dynamic programming.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing variables correctly, not considering all possible buy-sell combinations.
- Edge cases to watch for: Handling empty input arrays, ensuring the stock is not sold before it is bought.
- Performance pitfalls: Using brute force approaches for large inputs, not optimizing the time complexity.
- Testing considerations: Testing with different input sizes, testing with edge cases.