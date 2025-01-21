## Best Time to Buy and Sell Stock II
**Problem Link:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description

**Problem Statement:**
- Input format: An array `prices` where `prices[i]` is the price of a given stock on the `i-th` day.
- Constraints: `1 <= prices.length <= 10^4`, `0 <= prices[i] <= 10^4`.
- Expected output format: The maximum possible profit that can be achieved by buying and selling stocks multiple times.
- Key requirements and edge cases to consider:
  - Buying and selling can be done any number of times.
  - You must sell the stock before you buy again.
  - If the input array is empty or contains only one element, the maximum profit is 0.
- Example test cases with explanations:
  - Example 1: Input: `prices = [7,1,5,3,6,4]`, Output: `7`, Explanation: Buy on day 2 (price=1) and sell on day 3 (price=5), profit = 5-1 = 4. Then buy on day 4 (price=3) and sell on day 5 (price=6), profit = 6-3 = 3. Total profit = 4 + 3 = 7.
  - Example 2: Input: `prices = [1,2,3,4,5]`, Output: `4`, Explanation: Buy on day 1 (price=1) and sell on day 5 (price=5), profit = 5-1 = 4.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Consider all possible combinations of buying and selling days.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsets of the input array representing different buying and selling sequences.
  2. For each subset, calculate the profit by summing the differences between consecutive elements if the difference is positive (selling at a higher price than buying).
  3. Keep track of the maximum profit found across all subsets.
- Why this approach comes to mind first: It's an intuitive way to consider all possibilities, but it's not efficient due to its exponential time complexity.

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxProfit = 0;
        int n = prices.size();
        for (int mask = 0; mask < (1 << n); mask++) {
            int profit = 0;
            bool buying = false;
            int lastPrice = 0;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    if (!buying) {
                        buying = true;
                        lastPrice = prices[i];
                    } else {
                        profit += prices[i] - lastPrice;
                        buying = false;
                    }
                }
            }
            maxProfit = max(maxProfit, profit);
        }
        return maxProfit;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of days, due to generating all subsets and processing each subset.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output, as we only use a constant amount of space to store the maximum profit and other variables.
> - **Why these complexities occur:** The exponential time complexity comes from considering all possible subsets of the input array, and the constant space complexity is because we only use a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of considering all possible subsets, we can take advantage of the fact that we can buy and sell any number of times. The optimal strategy is to accumulate all positive differences between consecutive prices, as each positive difference represents a profitable transaction.
- Detailed breakdown of the approach:
  1. Initialize a variable `maxProfit` to 0.
  2. Iterate through the input array `prices`.
  3. For each pair of consecutive prices, if the difference is positive, add it to `maxProfit`.
- Proof of optimality: This approach is optimal because it accumulates all possible profits without considering unnecessary subsets or transactions.

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxProfit = 0;
        for (int i = 1; i < prices.size(); i++) {
            if (prices[i] > prices[i-1]) {
                maxProfit += prices[i] - prices[i-1];
            }
        }
        return maxProfit;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of days, as we only iterate through the input array once.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output, as we only use a constant amount of space to store the maximum profit.
> - **Optimality proof:** This solution is optimal because it efficiently accumulates all positive differences between consecutive prices in a single pass, resulting in the maximum possible profit.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy algorithms, dynamic programming (implicitly through the optimal approach).
- Problem-solving patterns identified: Accumulating positive differences to find the maximum profit.
- Optimization techniques learned: Avoiding unnecessary subsets and transactions.
- Similar problems to practice: Other stock buying and selling problems, such as "Best Time to Buy and Sell Stock" and "Best Time to Buy and Sell Stock III".

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases (e.g., empty input array or array with a single element).
- Edge cases to watch for: Handling arrays with duplicate prices or arrays where no profitable transactions can be made.
- Performance pitfalls: Using exponential-time algorithms or unnecessary data structures.
- Testing considerations: Thoroughly testing the solution with various input cases, including edge cases and large inputs.