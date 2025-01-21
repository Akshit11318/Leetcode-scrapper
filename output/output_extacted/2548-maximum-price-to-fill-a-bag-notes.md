## Maximum Price to Fill a Bag
**Problem Link:** https://leetcode.com/problems/maximum-price-to-fill-a-bag/description

**Problem Statement:**
- Input format and constraints: Given a list of integers `items` representing the prices of items and an integer `capacity` representing the maximum capacity of the bag, find the maximum price that can be achieved by selecting a subset of items without exceeding the capacity.
- Expected output format: The maximum price as an integer.
- Key requirements and edge cases to consider:
  - The capacity of the bag is a non-negative integer.
  - The prices of items are non-negative integers.
  - The number of items is a non-negative integer.
- Example test cases with explanations:
  - Example 1: `items = [1, 2, 3]`, `capacity = 2`, Output: `3`
  - Example 2: `items = [1, 2, 3]`, `capacity = 3`, Output: `6`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of items and calculate the total price for each combination.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsets of the `items` list.
  2. For each subset, calculate the total price by summing the prices of the items in the subset.
  3. Check if the total price does not exceed the `capacity`.
  4. If it does not exceed the capacity, update the maximum price if the current total price is greater.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible combinations of items.

```cpp
#include <vector>
#include <algorithm>

int maxPrice(std::vector<int>& items, int capacity) {
    int maxPrice = 0;
    int n = items.size();
    for (int mask = 0; mask < (1 << n); mask++) {
        int totalPrice = 0;
        int totalWeight = 0;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                totalPrice += items[i];
                totalWeight += 1; // assuming all items have a weight of 1
            }
        }
        if (totalWeight <= capacity && totalPrice > maxPrice) {
            maxPrice = totalPrice;
        }
    }
    return maxPrice;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the number of items, because we generate all possible subsets of the `items` list.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the maximum price and other variables.
> - **Why these complexities occur:** The time complexity is exponential because we try all possible combinations of items. The space complexity is constant because we only use a fixed amount of space to store the maximum price and other variables.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: This problem can be solved using dynamic programming, where we build up a table of maximum prices for each subproblem.
- Detailed breakdown of the approach:
  1. Create a 2D table `dp` where `dp[i][j]` represents the maximum price that can be achieved using the first `i` items and a capacity of `j`.
  2. Initialize the table by setting `dp[0][j] = 0` for all `j`, because we can achieve a price of 0 using 0 items.
  3. For each item `i` and each capacity `j`, calculate `dp[i][j]` by considering two cases:
    - If the current item has a weight greater than the current capacity `j`, we cannot include it, so `dp[i][j] = dp[i-1][j]`.
    - Otherwise, we can either include the current item or not include it, so `dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + items[i])`.
- Proof of optimality: This approach is optimal because it considers all possible combinations of items and capacities, and it uses dynamic programming to avoid redundant calculations.

```cpp
#include <vector>
#include <algorithm>

int maxPrice(std::vector<int>& items, int capacity) {
    int n = items.size();
    std::vector<std::vector<int>> dp(n + 1, std::vector<int>(capacity + 1, 0));
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= capacity; j++) {
            if (1 > j) { // assuming all items have a weight of 1
                dp[i][j] = dp[i-1][j];
            } else {
                dp[i][j] = std::max(dp[i-1][j], dp[i-1][j-1] + items[i-1]);
            }
        }
    }
    return dp[n][capacity];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot capacity)$, where $n$ is the number of items, because we fill up the `dp` table.
> - **Space Complexity:** $O(n \cdot capacity)$, because we use a 2D table to store the maximum prices for each subproblem.
> - **Optimality proof:** This approach is optimal because it considers all possible combinations of items and capacities, and it uses dynamic programming to avoid redundant calculations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, subset generation.
- Problem-solving patterns identified: Using dynamic programming to solve problems with overlapping subproblems.
- Optimization techniques learned: Using dynamic programming to avoid redundant calculations.
- Similar problems to practice: 0/1 Knapsack problem, Subset Sum problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` table correctly, not considering the base cases correctly.
- Edge cases to watch for: Handling cases where the capacity is 0 or the number of items is 0.
- Performance pitfalls: Using a brute force approach that tries all possible combinations of items.
- Testing considerations: Testing the solution with different inputs, including edge cases.