## Product Price at a Given Date

**Problem Link:** https://leetcode.com/problems/product-price-at-a-given-date/description

**Problem Statement:**
- Input format and constraints: You are given a table `Products` with columns `product_id`, `new_price`, `change_date`. The table contains historical price changes for each product. 
- Expected output format: Write a SQL query to find the price of each product at a given date `date`.
- Key requirements and edge cases to consider: 
    * If a product's price is not updated at the given date, return the most recent price before the given date.
    * If a product has no price history before the given date, return `NULL`.
- Example test cases with explanations:
    * If the given date is `2020-01-01`, and the product `1` has price changes at `2019-12-31` and `2020-01-15`, the query should return the price at `2019-12-31`.
    * If the given date is `2020-01-01`, and the product `2` has no price history before `2020-01-01`, the query should return `NULL`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can iterate over each product and find the most recent price change before or at the given date.
- Step-by-step breakdown of the solution:
    1. For each product, find all price changes with a date less than or equal to the given date.
    2. Sort these price changes by date in descending order.
    3. Return the price of the first price change (i.e., the most recent one).
- Why this approach comes to mind first: It is a straightforward and intuitive approach to solve the problem.

```cpp
// This problem requires SQL query, not C++ code.
// However, for the sake of following the template, here's a pseudo-code in C++ style:
// Note: This is not a real SQL query, but a pseudo-code to demonstrate the thought process.
SELECT 
    p1.product_id,
    p2.new_price
FROM 
    (SELECT DISTINCT product_id FROM Products) p1
LEFT JOIN 
    (SELECT 
         product_id, 
         new_price, 
         change_date
     FROM 
         Products
     WHERE 
         (product_id, change_date) IN (
             SELECT 
                 product_id, 
                 MAX(change_date) 
             FROM 
                 Products
             WHERE 
                 change_date <= '2020-01-01'
             GROUP BY 
                 product_id
         )
    ) p2
ON 
    p1.product_id = p2.product_id
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting of price changes for each product, where $n$ is the number of price changes for a product.
> - **Space Complexity:** $O(n)$ for storing the price changes for each product.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, and the space complexity is due to storing the price changes.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a SQL query with a subquery to find the most recent price change for each product before or at the given date.
- Detailed breakdown of the approach:
    1. Use a subquery to find the maximum `change_date` for each product that is less than or equal to the given date.
    2. Join this result with the `Products` table to find the corresponding `new_price`.
- Proof of optimality: This approach is optimal because it only requires a single pass over the `Products` table and uses efficient SQL operations.

```sql
SELECT 
    p1.product_id,
    p2.new_price
FROM 
    (SELECT DISTINCT product_id FROM Products) p1
LEFT JOIN 
    Products p2
ON 
    p1.product_id = p2.product_id
    AND p2.change_date = (
        SELECT 
            MAX(change_date) 
        FROM 
            Products p3
        WHERE 
            p3.product_id = p1.product_id 
            AND p3.change_date <= '2020-01-01'
    )
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the `Products` table, because we are using efficient SQL operations.
> - **Space Complexity:** $O(n)$ for storing the intermediate results.
> - **Optimality proof:** This approach is optimal because it uses efficient SQL operations and only requires a single pass over the `Products` table.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Efficient SQL operations, subqueries, and joins.
- Problem-solving patterns identified: Using subqueries to find the most recent price change for each product.
- Optimization techniques learned: Using efficient SQL operations and avoiding unnecessary sorting or iteration.
- Similar problems to practice: Other SQL problems that require finding the most recent or maximum value for each group.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly using subqueries or joins, or not handling `NULL` values properly.
- Edge cases to watch for: Handling products with no price history before the given date.
- Performance pitfalls: Using inefficient SQL operations or iterating over the `Products` table unnecessarily.
- Testing considerations: Testing the query with different input data and edge cases to ensure correctness and efficiency.