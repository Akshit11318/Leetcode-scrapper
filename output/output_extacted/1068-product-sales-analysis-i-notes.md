## Product Sales Analysis I
**Problem Link:** https://leetcode.com/problems/product-sales-analysis-i/description

**Problem Statement:**
- Input format and constraints: The problem takes two tables as input: `Sales` and `Product`. The `Sales` table contains columns for `sale_id`, `product_id`, `year`, and `quantity`, while the `Product` table contains columns for `product_id` and `product_name`. The goal is to analyze the sales data for each product.
- Expected output format: The output should be a table containing the `product_name` and the corresponding `product_id` for each product, along with the `year` and the total `quantity` sold for that product in that year.
- Key requirements and edge cases to consider: The solution should handle cases where a product may not have any sales data for a particular year.
- Example test cases with explanations: For example, given the `Sales` table with data `{(1, 1, 2018, 100), (2, 1, 2019, 50), (3, 2, 2018, 200)}` and the `Product` table with data `{(1, 'Product A'), (2, 'Product B')}`, the output should be `{('Product A', 1, 2018, 100), ('Product A', 1, 2019, 50), ('Product B', 2, 2018, 200)}`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over each row in the `Sales` table and joining it with the corresponding row in the `Product` table based on the `product_id`.
- Step-by-step breakdown of the solution:
  1. Iterate over each row in the `Sales` table.
  2. For each row, find the corresponding row in the `Product` table with the same `product_id`.
  3. Create a new row in the output table with the `product_name`, `product_id`, `year`, and `quantity`.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, as it involves a simple iteration over the input data.

```cpp
SELECT p.product_name, s.product_id, s.year, s.quantity
FROM Sales s
JOIN Product p ON s.product_id = p.product_id;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the `Sales` table, because we are iterating over each row once.
> - **Space Complexity:** $O(n)$, because we are storing the output in a new table.
> - **Why these complexities occur:** The time complexity is linear because we are performing a constant amount of work for each row in the input table. The space complexity is also linear because we are storing the output in a new table.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a `JOIN` operation to combine the `Sales` and `Product` tables based on the `product_id`. This allows us to avoid iterating over each row in the `Sales` table and instead use the database's optimized join algorithm.
- Detailed breakdown of the approach:
  1. Use a `JOIN` operation to combine the `Sales` and `Product` tables based on the `product_id`.
  2. Select the `product_name`, `product_id`, `year`, and `quantity` columns from the joined table.
- Proof of optimality: This approach is optimal because it uses the database's optimized join algorithm, which is typically faster than iterating over each row in the `Sales` table.
- Why further optimization is impossible: Further optimization is impossible because we are already using the most efficient algorithm available (the database's join algorithm).

```cpp
SELECT p.product_name, s.product_id, s.year, s.quantity
FROM Sales s
JOIN Product p ON s.product_id = p.product_id;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the `Sales` table, because we are using the database's optimized join algorithm.
> - **Space Complexity:** $O(n)$, because we are storing the output in a new table.
> - **Optimality proof:** The time complexity is linear because we are using the database's optimized join algorithm, which is typically faster than iterating over each row in the `Sales` table.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of `JOIN` operations to combine tables based on a common column.
- Problem-solving patterns identified: The problem requires identifying the common column between the two tables and using a `JOIN` operation to combine them.
- Optimization techniques learned: The problem demonstrates the use of the database's optimized join algorithm to improve performance.
- Similar problems to practice: Similar problems include other SQL queries that require combining tables based on common columns.

**Mistakes to Avoid:**
- Common implementation errors: A common error is to forget to specify the `ON` clause in the `JOIN` operation, which can result in a Cartesian product.
- Edge cases to watch for: An edge case to watch for is when a product may not have any sales data for a particular year.
- Performance pitfalls: A performance pitfall is to use a subquery instead of a `JOIN` operation, which can result in slower performance.
- Testing considerations: When testing the solution, make sure to test with different input data to ensure that the solution works correctly in all cases.