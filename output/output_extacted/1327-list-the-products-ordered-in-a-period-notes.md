## List the Products Ordered in a Period
**Problem Link:** https://leetcode.com/problems/list-the-products-ordered-in-a-period/description

**Problem Statement:**
- Input format and constraints: The problem provides two tables, `Products` and `Orders`. The `Products` table has columns `product_id` and `product_name`, while the `Orders` table has columns `product_id`, `order_id`, `order_date`, and `customer_id`. The goal is to find all products that were ordered in a specific period.
- Expected output format: A list of distinct `product_id` and `product_name` that were ordered in the specified period.
- Key requirements and edge cases to consider: The solution must handle cases where a product is ordered multiple times in the period, and it should only return distinct products.
- Example test cases with explanations: For instance, if the period is from '2020-01-01' to '2020-12-31', the solution should return all distinct products ordered during this time.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to iterate over all orders and check if the order date falls within the specified period. If it does, add the product to the result list.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list to store the result.
  2. Iterate over all orders in the `Orders` table.
  3. For each order, check if the `order_date` falls within the specified period.
  4. If it does, retrieve the corresponding `product_id` and `product_name` from the `Products` table.
  5. Add the `product_id` and `product_name` to the result list if they are not already present.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, as it involves a simple iteration over the orders and a basic check for the order date.

```cpp
SELECT DISTINCT p.product_id, p.product_name
FROM Products p
JOIN Orders o ON p.product_id = o.product_id
WHERE o.order_date BETWEEN '2020-01-01' AND '2020-12-31'
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the `Orders` table, because we are iterating over all orders.
> - **Space Complexity:** $O(n)$, where $n$ is the number of distinct products, because we are storing the result in a list.
> - **Why these complexities occur:** The time complexity is linear because we are iterating over all orders, and the space complexity is linear because we are storing the result in a list.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a SQL query with a `JOIN` and a `WHERE` clause to filter the orders based on the order date.
- Detailed breakdown of the approach:
  1. Use a `JOIN` to combine the `Products` and `Orders` tables based on the `product_id`.
  2. Use a `WHERE` clause to filter the orders based on the `order_date`.
  3. Use a `DISTINCT` keyword to retrieve only distinct products.
- Proof of optimality: This approach is optimal because it involves a single database query, which is more efficient than iterating over all orders in the brute force approach.
- Why further optimization is impossible: Further optimization is impossible because we need to iterate over all orders to filter them based on the order date.

```cpp
SELECT DISTINCT p.product_id, p.product_name
FROM Products p
JOIN Orders o ON p.product_id = o.product_id
WHERE o.order_date BETWEEN '2020-01-01' AND '2020-12-31'
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the `Orders` table, because we are iterating over all orders.
> - **Space Complexity:** $O(n)$, where $n$ is the number of distinct products, because we are storing the result in a list.
> - **Optimality proof:** The time complexity is linear because we are iterating over all orders, and the space complexity is linear because we are storing the result in a list.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of SQL queries with `JOIN` and `WHERE` clauses to filter data.
- Problem-solving patterns identified: The problem involves iterating over all orders and filtering them based on the order date.
- Optimization techniques learned: The problem demonstrates the use of a single database query to optimize the solution.
- Similar problems to practice: Other problems that involve filtering data based on specific conditions.

**Mistakes to Avoid:**
- Common implementation errors: Not using a `DISTINCT` keyword to retrieve only distinct products.
- Edge cases to watch for: Not handling cases where a product is ordered multiple times in the period.
- Performance pitfalls: Not using a single database query to optimize the solution.
- Testing considerations: Testing the solution with different input data to ensure it works correctly.