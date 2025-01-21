## Minimum Cost of Buying Candies with Discount
**Problem Link:** https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/description

**Problem Statement:**
- Input format and constraints: Given an array of integers `cost` where `cost[i]` is the cost of the `i-th` candy, and two integers `cash` and `discount`, find the minimum cost of buying `n` candies.
- Expected output format: Return the minimum cost as an integer.
- Key requirements and edge cases to consider:
  - The array `cost` is non-empty and has at least `n` elements.
  - `n` is the number of candies to buy, which is equal to the length of the `cost` array.
  - `cash` is the amount of cash available, and `discount` is the discount percentage.
- Example test cases with explanations:
  - If `cost = [1,2,3]`, `cash = 10`, `discount = 4`, the output should be `5`.
  - If `cost = [2,3,1]`, `cash = 10`, `discount = 3`, the output should be `5`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Sort the array of costs in ascending order.
- Step-by-step breakdown of the solution:
  1. Sort the array `cost` in ascending order.
  2. Initialize a variable `totalCost` to 0.
  3. Iterate over the sorted array `cost` and add each cost to `totalCost`.
  4. Apply the discount to `totalCost` by subtracting `discount` percent of `totalCost` from `totalCost`.
  5. Return `totalCost` as the minimum cost.

```cpp
#include <algorithm>

int minCost(vector<int>& cost, int cash, int discount) {
    // Sort the array in ascending order
    sort(cost.begin(), cost.end());
    
    // Initialize totalCost to 0
    int totalCost = 0;
    
    // Iterate over the sorted array and add each cost to totalCost
    for (int i = 0; i < cost.size(); i++) {
        totalCost += cost[i];
    }
    
    // Apply the discount to totalCost
    totalCost -= (totalCost * discount) / 100;
    
    return totalCost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of elements in the `cost` array, due to the sorting operation.
> - **Space Complexity:** $O(1)$, as no additional space is used.
> - **Why these complexities occur:** The time complexity is dominated by the sorting operation, and the space complexity is constant because no additional space is used.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved by sorting the array and then applying the discount.
- Detailed breakdown of the approach:
  1. Sort the array `cost` in ascending order.
  2. Initialize a variable `totalCost` to 0.
  3. Iterate over the sorted array `cost` and add each cost to `totalCost`.
  4. Apply the discount to `totalCost` by subtracting `discount` percent of `totalCost` from `totalCost`.
  5. Return `totalCost` as the minimum cost.

```cpp
#include <algorithm>

int minCost(vector<int>& cost, int cash, int discount) {
    // Sort the array in ascending order
    sort(cost.begin(), cost.end());
    
    // Initialize totalCost to 0
    int totalCost = 0;
    
    // Iterate over the sorted array and add each cost to totalCost
    for (int i = 0; i < cost.size(); i++) {
        totalCost += cost[i];
    }
    
    // Apply the discount to totalCost
    totalCost -= (totalCost * discount) / 100;
    
    return totalCost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of elements in the `cost` array, due to the sorting operation.
> - **Space Complexity:** $O(1)$, as no additional space is used.
> - **Optimality proof:** This is the optimal solution because it uses the most efficient sorting algorithm and applies the discount in a single operation.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting and discount application.
- Problem-solving patterns identified: Using sorting to optimize the solution.
- Optimization techniques learned: Applying discounts in a single operation.
- Similar problems to practice: Other problems involving sorting and discount application.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty input array.
- Edge cases to watch for: Empty input array, negative costs, and invalid discount values.
- Performance pitfalls: Using inefficient sorting algorithms or applying discounts multiple times.
- Testing considerations: Test the solution with different input sizes, costs, and discount values.