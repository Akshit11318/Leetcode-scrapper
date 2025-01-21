## Sales Analysis III
**Problem Link:** https://leetcode.com/problems/sales-analysis-iii/description

**Problem Statement:**
- Input format and constraints: The problem involves two tables, `Sales` and `Product`. The `Sales` table contains columns `sale_id`, `product_id`, `sale_date`, and `quantity`, while the `Product` table contains columns `product_id` and `product_name`. The task is to write a SQL query to find the product names that were sold in the year 2003.
- Expected output format: The output should be a list of `product_name`s.
- Key requirements and edge cases to consider: The query should handle cases where a product was sold multiple times in the year 2003.
- Example test cases with explanations: For example, if the `Sales` table contains the rows `(1, 1, '2003-01-01', 10)` and `(2, 1, '2003-02-01', 20)`, and the `Product` table contains the row `(1, 'Product A')`, the query should return `Product A`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over each row in the `Sales` table, checking if the `sale_date` is in the year 2003, and if so, joining with the `Product` table to get the corresponding `product_name`.
- Step-by-step breakdown of the solution: 
    1. Select all rows from the `Sales` table where the `sale_date` is in the year 2003.
    2. Join the resulting table with the `Product` table on the `product_id` column.
    3. Select the distinct `product_name`s from the joined table.
- Why this approach comes to mind first: This approach is straightforward and involves the basic operations of filtering, joining, and selecting distinct values.

```sql
SELECT DISTINCT p.product_name
FROM Sales s
JOIN Product p ON s.product_id = p.product_id
WHERE YEAR(s.sale_date) = 2003;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the `Sales` table, since we are iterating over each row in the table.
> - **Space Complexity:** $O(n)$, since we are storing the joined table in memory.
> - **Why these complexities occur:** The time complexity occurs because we are iterating over each row in the `Sales` table, and the space complexity occurs because we are storing the joined table in memory.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using the same approach as the brute force solution, but with a more efficient join operation.
- Detailed breakdown of the approach: 
    1. Select all rows from the `Sales` table where the `sale_date` is in the year 2003.
    2. Join the resulting table with the `Product` table on the `product_id` column using an inner join.
    3. Select the distinct `product_name`s from the joined table.
- Proof of optimality: This solution is optimal because it involves the minimum number of operations necessary to solve the problem, and it uses the most efficient join operation.

```sql
SELECT DISTINCT p.product_name
FROM Sales s
INNER JOIN Product p ON s.product_id = p.product_id
WHERE YEAR(s.sale_date) = 2003;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the `Sales` table, since we are iterating over each row in the table.
> - **Space Complexity:** $O(n)$, since we are storing the joined table in memory.
> - **Optimality proof:** This solution is optimal because it involves the minimum number of operations necessary to solve the problem, and it uses the most efficient join operation.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of join operations and filtering.
- Problem-solving patterns identified: The problem involves identifying the minimum number of operations necessary to solve the problem.
- Optimization techniques learned: The problem involves using the most efficient join operation.
- Similar problems to practice: Other problems that involve join operations and filtering.

**Mistakes to Avoid:**
- Common implementation errors: One common implementation error is using a cross join instead of an inner join.
- Edge cases to watch for: One edge case to watch for is when the `Sales` table is empty.
- Performance pitfalls: One performance pitfall is using a subquery instead of a join.
- Testing considerations: One testing consideration is to test the query with a large dataset.