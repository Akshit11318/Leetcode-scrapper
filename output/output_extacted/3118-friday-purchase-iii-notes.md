## Friday Purchase III

**Problem Link:** https://leetcode.com/problems/friday-purchase-iii/description

**Problem Statement:**
- Input format and constraints: Given a list of integers `prices` representing the prices of items on different days and an integer `k` representing the maximum number of items that can be purchased.
- Expected output format: The maximum number of items that can be purchased within the budget of `k` dollars on a Friday.
- Key requirements and edge cases to consider: The prices list can be empty, `k` can be 0, and prices can be negative.
- Example test cases with explanations: 
    - For `prices = [1, 2, 3, 4, 5]` and `k = 10`, the maximum number of items that can be purchased is 3 (items with prices 1, 2, and 3).
    - For `prices = [1, 1, 1, 1, 1]` and `k = 3`, the maximum number of items that can be purchased is 3 (any 3 items).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of items to find the maximum number of items that can be purchased within the budget.
- Step-by-step breakdown of the solution:
    1. Sort the prices in ascending order.
    2. Initialize a variable to store the maximum number of items that can be purchased.
    3. Iterate over all possible combinations of items.
    4. For each combination, calculate the total cost and check if it is within the budget.
    5. Update the maximum number of items if a combination with a higher number of items is found.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible solutions, making it easy to understand and implement.

```cpp
#include <vector>
#include <algorithm>

int maxItems(std::vector<int>& prices, int k) {
    std::sort(prices.begin(), prices.end());
    int maxItems = 0;
    int totalCost = 0;
    for (int i = 0; i < prices.size(); i++) {
        if (totalCost + prices[i] <= k) {
            totalCost += prices[i];
            maxItems++;
        } else {
            break;
        }
    }
    return maxItems;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting of prices, where $n$ is the number of prices.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space to store the maximum number of items and the total cost.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, while the space complexity is constant because we only use a fixed amount of space to store the variables.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a greedy approach to find the maximum number of items that can be purchased within the budget. We sort the prices in ascending order and then iterate over the sorted prices, adding each price to the total cost until the budget is exceeded.
- Detailed breakdown of the approach:
    1. Sort the prices in ascending order.
    2. Initialize variables to store the maximum number of items and the total cost.
    3. Iterate over the sorted prices, adding each price to the total cost and incrementing the maximum number of items until the budget is exceeded.
- Proof of optimality: This approach is optimal because it always chooses the item with the lowest price first, which maximizes the number of items that can be purchased within the budget.

```cpp
#include <vector>
#include <algorithm>

int maxItems(std::vector<int>& prices, int k) {
    std::sort(prices.begin(), prices.end());
    int maxItems = 0;
    int totalCost = 0;
    for (int price : prices) {
        if (totalCost + price <= k) {
            totalCost += price;
            maxItems++;
        } else {
            break;
        }
    }
    return maxItems;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting of prices, where $n$ is the number of prices.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space to store the maximum number of items and the total cost.
> - **Optimality proof:** The greedy approach ensures that we always choose the item with the lowest price first, which maximizes the number of items that can be purchased within the budget.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy algorithm, sorting.
- Problem-solving patterns identified: Finding the maximum number of items that can be purchased within a budget.
- Optimization techniques learned: Using a greedy approach to find the optimal solution.
- Similar problems to practice: Other problems that involve finding the maximum number of items that can be purchased within a budget.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for the case where the prices list is empty or the budget is 0.
- Edge cases to watch for: Negative prices, prices that are greater than the budget.
- Performance pitfalls: Using a brute force approach that tries all possible combinations of items.
- Testing considerations: Testing the function with different inputs, including edge cases, to ensure that it works correctly.