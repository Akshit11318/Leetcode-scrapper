## Calculate Product Final Prices
**Problem Link:** https://leetcode.com/problems/calculate-product-final-price/description

**Problem Statement:**
- Input format and constraints: Given a list of prices and a list of discounts, calculate the final price of each product after applying the discounts. The prices and discounts are represented as lists of integers, where each integer represents the price or discount of a product.
- Expected output format: A list of integers representing the final prices of the products after applying the discounts.
- Key requirements and edge cases to consider: 
  - The discounts are applied in the order they are given.
  - A discount is applied to the product at the same index.
  - If the discount is greater than the price, the price becomes 0.
- Example test cases with explanations:
  - Example 1: Input: prices = [100, 200, 300], discounts = [10, 20, 30]. Output: [90, 160, 210].
  - Example 2: Input: prices = [100, 200, 300], discounts = [10, 20, 50]. Output: [90, 160, 150].

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to solve this problem is to iterate over the prices and discounts, applying each discount to the corresponding price.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list to store the final prices.
  2. Iterate over the prices and discounts.
  3. For each price and discount, calculate the final price by subtracting the discount from the price.
  4. If the final price is less than 0, set it to 0.
  5. Append the final price to the list of final prices.
- Why this approach comes to mind first: This approach is the most straightforward because it directly applies the discounts to the prices without any additional complexity.

```cpp
vector<int> finalPrices(vector<int>& prices, vector<int>& discounts) {
    vector<int> finalPrices;
    for (int i = 0; i < prices.size(); i++) {
        int finalPrice = prices[i] - discounts[i];
        if (finalPrice < 0) {
            finalPrice = 0;
        }
        finalPrices.push_back(finalPrice);
    }
    return finalPrices;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where n is the number of products. This is because we are iterating over the prices and discounts once.
> - **Space Complexity:** $O(n)$, where n is the number of products. This is because we are storing the final prices in a separate list.
> - **Why these complexities occur:** These complexities occur because we are performing a constant amount of work for each product, and we are storing the final prices in a separate list.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is the same as the brute force approach because the problem requires us to apply each discount to the corresponding price, which is a linear operation.
- Detailed breakdown of the approach:
  1. Initialize an empty list to store the final prices.
  2. Iterate over the prices and discounts.
  3. For each price and discount, calculate the final price by subtracting the discount from the price.
  4. If the final price is less than 0, set it to 0.
  5. Append the final price to the list of final prices.
- Proof of optimality: This approach is optimal because it has a time complexity of $O(n)$, which is the minimum time complexity required to solve this problem. This is because we must at least read the input prices and discounts once.
- Why further optimization is impossible: Further optimization is impossible because we must perform at least a constant amount of work for each product to calculate the final price.

```cpp
vector<int> finalPrices(vector<int>& prices, vector<int>& discounts) {
    vector<int> finalPrices;
    for (int i = 0; i < prices.size(); i++) {
        int finalPrice = max(0, prices[i] - discounts[i]);
        finalPrices.push_back(finalPrice);
    }
    return finalPrices;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where n is the number of products. This is because we are iterating over the prices and discounts once.
> - **Space Complexity:** $O(n)$, where n is the number of products. This is because we are storing the final prices in a separate list.
> - **Optimality proof:** This approach is optimal because it has a time complexity of $O(n)$, which is the minimum time complexity required to solve this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the concept of linear iteration and the importance of checking for edge cases.
- Problem-solving patterns identified: The problem requires a straightforward iteration over the input data, which is a common pattern in many problems.
- Optimization techniques learned: The problem does not require any optimization techniques beyond the brute force approach.
- Similar problems to practice: Other problems that involve linear iteration and edge case checking, such as calculating the sum of an array or finding the maximum value in an array.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to check for edge cases, such as negative prices or discounts.
- Edge cases to watch for: Prices or discounts that are negative or zero.
- Performance pitfalls: Using unnecessary loops or data structures that can increase the time or space complexity of the solution.
- Testing considerations: Testing the solution with different input sizes and edge cases to ensure that it works correctly and efficiently.