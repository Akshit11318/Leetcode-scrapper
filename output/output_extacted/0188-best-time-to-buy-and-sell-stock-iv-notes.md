## Best Time to Buy and Sell Stock IV
**Problem Link:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description

**Problem Statement:**
- Input format and constraints: The problem takes an array of integers representing the prices of a stock on different days and an integer `k` representing the maximum number of transactions allowed. The constraints are that the length of the prices array is between 1 and $2 \times 10^5$, and `k` is between 1 and $2 \times 10^5$. The expected output is the maximum profit that can be achieved.
- Expected output format: The maximum possible profit.
- Key requirements and edge cases to consider: The stock can only be bought and sold on the same day if it's the last day of the allowed transactions, and the stock must be sold before buying again.
- Example test cases with explanations:
  - For `prices = [2,4,1]` and `k = 2`, the maximum profit is `2`, achieved by buying on the second day and selling on the third day.
  - For `prices = [3,2,6,5,0,3]` and `k = 2`, the maximum profit is `7`, achieved by buying on the second day, selling on the third day, buying on the fifth day, and selling on the sixth day.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of buying and selling.
- Step-by-step breakdown of the solution:
  1. Generate all possible sequences of buy and sell transactions up to `k` transactions.
  2. For each sequence, calculate the profit.
  3. Keep track of the maximum profit found.
- Why this approach comes to mind first: It's a straightforward way to ensure all possibilities are considered.

```cpp
class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        int n = prices.size();
        int maxProfit = 0;
        vector<vector<int>> transactions;
        
        // Generate all possible sequences of transactions
        generateTransactions(transactions, k, 0, prices);
        
        // Calculate the profit for each sequence and update maxProfit
        for (auto& transaction : transactions) {
            int profit = 0;
            for (int i = 0; i < transaction.size(); i += 2) {
                profit += prices[transaction[i + 1]] - prices[transaction[i]];
            }
            maxProfit = max(maxProfit, profit);
        }
        
        return maxProfit;
    }
    
    void generateTransactions(vector<vector<int>>& transactions, int k, int start, vector<int>& prices) {
        if (k == 0) {
            transactions.push_back({});
            return;
        }
        
        for (int i = start; i < prices.size(); i++) {
            for (int j = i + 1; j < prices.size(); j++) {
                vector<int> transaction;
                transaction.push_back(i);
                transaction.push_back(j);
                generateTransactionsHelper(transactions, k - 1, j + 1, prices, transaction);
            }
        }
    }
    
    void generateTransactionsHelper(vector<vector<int>>& transactions, int k, int start, vector<int>& prices, vector<int>& currentTransaction) {
        if (k == 0) {
            transactions.push_back(currentTransaction);
            return;
        }
        
        for (int i = start; i < prices.size(); i++) {
            for (int j = i + 1; j < prices.size(); j++) {
                currentTransaction.push_back(i);
                currentTransaction.push_back(j);
                generateTransactionsHelper(transactions, k - 1, j + 1, prices, currentTransaction);
                currentTransaction.pop_back();
                currentTransaction.pop_back();
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{n})$, where $n$ is the number of days. This is because in the worst case, we are generating all possible sequences of buy and sell transactions.
> - **Space Complexity:** $O(2^{n})$, as we are storing all possible sequences of transactions.
> - **Why these complexities occur:** The brute force approach tries all possible combinations of buying and selling, leading to exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to keep track of the maximum profit for each subproblem.
- Detailed breakdown of the approach:
  1. Initialize a 2D array `dp` where `dp[i][j]` represents the maximum profit for `i` transactions and `j` days.
  2. Fill the `dp` array using the recurrence relation: `dp[i][j] = max(dp[i][j - 1], prices[j] - prices[k] + dp[i - 1][k])` for all `k < j`.
  3. The final answer is stored in `dp[k][n - 1]`.
- Proof of optimality: This approach ensures that we consider all possible sequences of transactions and keep track of the maximum profit for each subproblem, leading to a time complexity of $O(nk)$.

```cpp
class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        int n = prices.size();
        if (n < 2) return 0;
        
        // If k is greater than or equal to n/2, we can simply consider every peak and valley
        if (k >= n / 2) {
            int maxProfit = 0;
            for (int i = 1; i < n; i++) {
                if (prices[i] > prices[i - 1]) {
                    maxProfit += prices[i] - prices[i - 1];
                }
            }
            return maxProfit;
        }
        
        // Initialize dp array
        vector<vector<int>> dp(k + 1, vector<int>(n, 0));
        
        // Fill dp array
        for (int i = 1; i <= k; i++) {
            int maxDiff = -prices[0];
            for (int j = 1; j < n; j++) {
                dp[i][j] = max(dp[i][j - 1], prices[j] + maxDiff);
                maxDiff = max(maxDiff, dp[i - 1][j] - prices[j]);
            }
        }
        
        return dp[k][n - 1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(nk)$, where $n$ is the number of days and $k$ is the maximum number of transactions.
> - **Space Complexity:** $O(nk)$, as we are storing the `dp` array.
> - **Optimality proof:** This approach ensures that we consider all possible sequences of transactions and keep track of the maximum profit for each subproblem, leading to a time complexity of $O(nk)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming and optimization.
- Problem-solving patterns identified: Breaking down the problem into subproblems and using recurrence relations to solve them.
- Optimization techniques learned: Using dynamic programming to avoid redundant calculations and reduce time complexity.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, such as when `k` is greater than or equal to `n/2`.
- Edge cases to watch for: When `n` is less than 2, the maximum profit is 0.
- Performance pitfalls: Using brute force approaches that lead to exponential time complexity.
- Testing considerations: Test the solution with different values of `k` and `n` to ensure it works correctly for all edge cases.