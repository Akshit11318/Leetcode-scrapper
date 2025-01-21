## Maximize the Profit as the Salesman

**Problem Link:** https://leetcode.com/problems/maximize-the-profit-as-the-salesman/description

**Problem Statement:**
- Input format and constraints: Given a list of `prices` of length `n`, find the maximum possible profit that can be achieved by selling the items at the given prices, considering that we can only sell each item once and we have a limit on the number of items we can sell, which is `k`.
- Expected output format: The maximum possible profit as an integer.
- Key requirements and edge cases to consider:
  - Each item can only be sold once.
  - We can only sell up to `k` items.
  - Prices can be any non-negative integer.
- Example test cases with explanations:
  - For `prices = [10, 20, 30, 40]` and `k = 2`, the maximum profit is `50` by selling items at indices `1` and `3`.
  - For `prices = [1, 2, 3, 4]` and `k = 4`, the maximum profit is `10` by selling all items.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of selling items and calculate the profit for each combination.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of selling up to `k` items from the `prices` list.
  2. For each combination, calculate the total profit by summing the prices of the items in the combination.
  3. Keep track of the maximum profit found so far.
- Why this approach comes to mind first: It is a straightforward way to ensure we consider all possible ways to sell items, but it is inefficient due to its exponential time complexity.

```cpp
#include <vector>
#include <algorithm>

int maxProfit(std::vector<int>& prices, int k) {
    int n = prices.size();
    int maxProfit = 0;
    
    // Generate all possible combinations of selling up to k items
    for (int mask = 0; mask < (1 << n); mask++) {
        int currentProfit = 0;
        int itemsSold = 0;
        
        // Calculate profit for the current combination
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                currentProfit += prices[i];
                itemsSold++;
            }
        }
        
        // Update maxProfit if the current combination sells up to k items and has a higher profit
        if (itemsSold <= k && currentProfit > maxProfit) {
            maxProfit = currentProfit;
        }
    }
    
    return maxProfit;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, because we generate all possible subsets of the `prices` list, which has $2^n$ possible subsets.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the current combination and the maximum profit found so far.
> - **Why these complexities occur:** The exponential time complexity comes from generating all possible subsets, which grows exponentially with the size of the input. The constant space complexity is due to only using a fixed amount of space, regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to solve this problem more efficiently. The idea is to build up a table where each cell represents the maximum profit that can be achieved by selling a certain number of items up to a certain index.
- Detailed breakdown of the approach:
  1. Create a 2D table `dp` where `dp[i][j]` represents the maximum profit that can be achieved by selling `j` items up to index `i`.
  2. Initialize the table by setting `dp[0][0] = 0` and `dp[0][j] = 0` for all `j > 0`, because we cannot sell any items at index 0.
  3. Fill in the table by iterating over each index `i` and each possible number of items `j` that can be sold. For each cell, calculate the maximum profit by considering two options: selling the current item or not selling it.
- Proof of optimality: This approach ensures that we consider all possible ways to sell items while avoiding the exponential time complexity of the brute force approach.

```cpp
#include <vector>
#include <algorithm>

int maxProfit(std::vector<int>& prices, int k) {
    int n = prices.size();
    std::vector<std::vector<int>> dp(n + 1, std::vector<int>(k + 1, 0));
    
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= k; j++) {
            // Calculate maximum profit by considering two options: selling the current item or not selling it
            dp[i][j] = std::max(dp[i - 1][j], dp[i - 1][j - 1] + prices[i - 1]);
        }
    }
    
    return dp[n][k];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(nk)$, because we fill in a table of size $(n + 1) \times (k + 1)$.
> - **Space Complexity:** $O(nk)$, because we need to store the table of size $(n + 1) \times (k + 1)$.
> - **Optimality proof:** This approach is optimal because it ensures that we consider all possible ways to sell items while avoiding the exponential time complexity of the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, memoization.
- Problem-solving patterns identified: Breaking down the problem into smaller subproblems, using a table to store intermediate results.
- Optimization techniques learned: Using dynamic programming to avoid exponential time complexity.
- Similar problems to practice: Other dynamic programming problems, such as the knapsack problem or the Fibonacci sequence.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the table correctly, not considering the base cases.
- Edge cases to watch for: Handling the case where `k` is 0 or `n` is 0.
- Performance pitfalls: Using an exponential time complexity approach, not using memoization to avoid redundant calculations.
- Testing considerations: Testing the function with different inputs, including edge cases and large inputs.