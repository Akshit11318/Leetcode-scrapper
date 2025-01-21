## Most Expensive Item That Can Not Be Bought
**Problem Link:** https://leetcode.com/problems/most-expensive-item-that-can-not-be-bought/description

**Problem Statement:**
- Input format: You are given an integer array `prices` where `prices[i]` is the price of the `i-th` item and an integer `budget`.
- Constraints: `1 <= prices.length <= 10^5`, `0 <= prices[i] <= 10^6`, `0 <= budget <= 10^6`.
- Expected output format: Return the maximum price of an item that can not be bought within the given `budget`.
- Key requirements and edge cases to consider: The maximum price might be the largest price if it exceeds the budget, or it could be the largest price among items that cannot be bought if multiple items exceed the budget when combined.
- Example test cases with explanations:
  - If `prices = [1,2,3]` and `budget = 5`, the maximum price that can not be bought is `0` because all items can be bought.
  - If `prices = [1,2,3]` and `budget = 2`, the maximum price that can not be bought is `3` because only the item with price `3` cannot be bought.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Sort the prices in ascending order and then try to buy items from the cheapest to the most expensive until the budget is exhausted.
- Step-by-step breakdown of the solution: 
  1. Sort the `prices` array in ascending order.
  2. Initialize a variable `remainingBudget` to the given `budget`.
  3. Iterate through the sorted `prices` array. For each price, check if buying the item at that price would exceed the `remainingBudget`.
  4. If it does, return the current price as it is the first item that cannot be bought.
  5. If it doesn't, subtract the price from `remainingBudget` and continue to the next item.
- Why this approach comes to mind first: It's straightforward and ensures we consider buying items in the most cost-effective order.

```cpp
#include <algorithm>
int mostExpensiveItemThatCanNotBeBought(vector<int>& prices, int budget) {
    // Sort prices in ascending order
    sort(prices.begin(), prices.end());
    
    int remainingBudget = budget;
    for (int price : prices) {
        if (price > remainingBudget) {
            return price;
        }
        remainingBudget -= price;
    }
    // If all items can be bought, return 0
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of items. This is because we sort the prices array, which takes $O(n \log n)$ time.
> - **Space Complexity:** $O(1)$, assuming the sorting is done in-place. Otherwise, it could be $O(n)$ depending on the sorting algorithm used.
> - **Why these complexities occur:** The sorting operation dominates the time complexity. The space complexity is minimal because we only use a constant amount of space to store the remaining budget and iterate through the array.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of sorting the entire array, we can find the maximum price that cannot be bought by checking if the sum of all prices except the maximum price exceeds the budget.
- Detailed breakdown of the approach:
  1. Calculate the total sum of all prices.
  2. If the total sum exceeds the budget, find the maximum price that cannot be bought by checking each price from highest to lowest.
  3. If the total sum does not exceed the budget, all items can be bought, so return 0.
- Proof of optimality: This approach is optimal because it directly addresses the problem by considering the maximum price that cannot be bought based on the budget constraint, without needing to sort the entire array.
- Why further optimization is impossible: This approach has a linear time complexity, which is the best we can achieve because we must at least consider each price once.

```cpp
int mostExpensiveItemThatCanNotBeBought(vector<int>& prices, int budget) {
    int totalSum = 0;
    int maxPrice = 0;
    for (int price : prices) {
        totalSum += price;
        maxPrice = max(maxPrice, price);
    }
    
    if (totalSum <= budget) {
        return 0; // All items can be bought
    }
    
    sort(prices.rbegin(), prices.rend());
    for (int price : prices) {
        if (totalSum - price <= budget) {
            return price;
        }
        totalSum -= price;
    }
    
    // Should not reach here
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation. However, this is the most efficient approach because we must consider each item's price in relation to the budget.
> - **Space Complexity:** $O(1)$ if sorting is done in-place; otherwise, $O(n)$.
> - **Optimality proof:** This is the optimal approach because it directly addresses the problem statement with the minimum necessary operations, avoiding unnecessary comparisons or iterations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, iteration, and budget constraint checking.
- Problem-solving patterns identified: Checking for the maximum price that cannot be bought based on the budget constraint.
- Optimization techniques learned: Avoiding unnecessary sorting or comparisons.
- Similar problems to practice: Other problems involving budget constraints and item prices.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases like an empty prices array or a budget of 0.
- Edge cases to watch for: When all items can be bought, or when the budget is insufficient for any item.
- Performance pitfalls: Using inefficient sorting algorithms or unnecessary iterations.
- Testing considerations: Ensure to test with various budgets and price arrays to cover all scenarios.