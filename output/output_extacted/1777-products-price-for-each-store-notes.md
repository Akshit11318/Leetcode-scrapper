## Products Price for Each Store

**Problem Link:** https://leetcode.com/problems/products-price-for-each-store/description

**Problem Statement:**
- Input format and constraints: The problem requires you to write a SQL query that calculates the price of each product in each store. The input consists of two tables: `Products` and `Prices`. The `Products` table contains information about each product, including the product ID and product name. The `Prices` table contains the prices of each product in each store, including the product ID, store ID, price, and effective date.
- Expected output format: The output should be a table with the product ID, store ID, and the price of each product in each store.
- Key requirements and edge cases to consider: The price of a product in a store is the latest price in the `Prices` table for that product and store.
- Example test cases with explanations: For example, if there are two products, A and B, and two stores, X and Y, the output should include the price of product A in store X, product A in store Y, product B in store X, and product B in store Y.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The initial thought is to use a SQL query to join the `Products` and `Prices` tables based on the product ID. Then, for each product and store, find the latest price by sorting the prices in descending order of the effective date and selecting the top one.
- Step-by-step breakdown of the solution:
  1. Join the `Products` and `Prices` tables based on the product ID.
  2. For each product and store, sort the prices in descending order of the effective date.
  3. Select the top price for each product and store.
- Why this approach comes to mind first: This approach is straightforward and directly addresses the problem statement.

```cpp
// SQL query
SELECT 
  p1.product_id,
  p1.store_id,
  p2.price
FROM 
  (
    SELECT 
      product_id, 
      store_id, 
      MAX(effective_date) AS max_date
    FROM 
      Prices
    GROUP BY 
      product_id, 
      store_id
  ) p1
JOIN 
  Prices p2 ON p1.product_id = p2.product_id AND p1.store_id = p2.store_id AND p1.max_date = p2.effective_date
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting of prices.
> - **Space Complexity:** $O(n)$ for storing the joined table.
> - **Why these complexities occur:** The sorting of prices is the main contributor to the time complexity, while the space complexity is due to the storage of the joined table.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of sorting all prices, we can use a window function to find the latest price for each product and store.
- Detailed breakdown of the approach:
  1. Use a window function to assign a row number to each price based on the product ID, store ID, and effective date.
  2. Select the prices with row number 1, which correspond to the latest price for each product and store.
- Proof of optimality: This approach is optimal because it avoids the need for sorting and instead uses a more efficient window function.

```cpp
// SQL query
SELECT 
  product_id,
  store_id,
  price
FROM 
  (
    SELECT 
      product_id, 
      store_id, 
      price,
      ROW_NUMBER() OVER (PARTITION BY product_id, store_id ORDER BY effective_date DESC) AS row_num
    FROM 
      Prices
  ) p
WHERE 
  row_num = 1
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ due to the window function.
> - **Space Complexity:** $O(n)$ for storing the result.
> - **Optimality proof:** The window function allows us to find the latest price for each product and store in a single pass, making this approach optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Window functions and row numbering.
- Problem-solving patterns identified: Using window functions to avoid sorting.
- Optimization techniques learned: Avoiding unnecessary sorting and using efficient window functions.
- Similar problems to practice: Other problems involving finding the latest or earliest value in a dataset.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect use of window functions or row numbering.
- Edge cases to watch for: Handling cases where there are multiple prices with the same effective date.
- Performance pitfalls: Using inefficient sorting or joining techniques.
- Testing considerations: Testing the query with different datasets and edge cases.