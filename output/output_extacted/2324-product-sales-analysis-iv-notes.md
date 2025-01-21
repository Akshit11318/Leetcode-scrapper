## Product Sales Analysis IV

**Problem Link:** https://leetcode.com/problems/product-sales-analysis-iv/description

**Problem Statement:**
- Input format and constraints: We have two tables, `Sales` and `Product`. The `Sales` table contains sales information with columns `product_id`, `period_start`, `period_end`, and `average_daily_sales`. The `Product` table contains product information with columns `product_id` and `product_name`. We need to find the `product_id` and `product_name` for each product that has higher average daily sales in the period `2020-01-01` to `2020-12-31` than in the period `2019-01-01` to `2019-12-31`.
- Expected output format: A table with `product_id` and `product_name`.
- Key requirements and edge cases to consider: The average daily sales for a product in a period is calculated by summing up the `average_daily_sales` for all sales records of the product in that period and then dividing by the number of days in the period.
- Example test cases with explanations: For example, if a product has two sales records in the year 2020 with `average_daily_sales` of 10 and 20, and the period is from `2020-01-01` to `2020-12-31`, the average daily sales for this product in 2020 is (10 + 20) / 365.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the average daily sales for each product in both periods and then compare them.
- Step-by-step breakdown of the solution:
  1. Calculate the total sales for each product in both periods.
  2. Calculate the number of days in each period.
  3. Calculate the average daily sales for each product in both periods.
  4. Compare the average daily sales for each product in both periods and return the `product_id` and `product_name` for products with higher average daily sales in 2020.
- Why this approach comes to mind first: It directly addresses the problem by calculating the required metrics and comparing them.

```cpp
SELECT 
    p.product_id, 
    p.product_name
FROM 
    Product p
JOIN 
    Sales s ON p.product_id = s.product_id
WHERE 
    (s.product_id, s.period_start) IN (
        SELECT 
            product_id, 
            period_start
        FROM 
            Sales
        WHERE 
            period_start = '2019-01-01' AND period_end = '2019-12-31'
    )
    OR (s.product_id, s.period_start) IN (
        SELECT 
            product_id, 
            period_start
        FROM 
            Sales
        WHERE 
            period_start = '2020-01-01' AND period_end = '2020-12-31'
    )
GROUP BY 
    p.product_id, 
    p.product_name
HAVING 
    SUM(CASE WHEN s.period_start = '2020-01-01' THEN s.average_daily_sales ELSE 0 END) / 365 > 
    SUM(CASE WHEN s.period_start = '2019-01-01' THEN s.average_daily_sales ELSE 0 END) / 365;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of products and $m$ is the number of sales records. This is because we are iterating over all sales records for each product.
> - **Space Complexity:** $O(n \cdot m)$, as in the worst case, we might need to store all sales records in memory.
> - **Why these complexities occur:** The brute force approach requires iterating over all sales records for each product, which leads to high time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use SQL to directly filter and calculate the required metrics without needing to iterate over all sales records manually.
- Detailed breakdown of the approach:
  1. Filter the sales records for the two periods.
  2. Calculate the sum of `average_daily_sales` for each product in both periods.
  3. Calculate the average daily sales for each product in both periods.
  4. Compare the average daily sales for each product in both periods and return the `product_id` and `product_name` for products with higher average daily sales in 2020.
- Proof of optimality: This approach is optimal because it uses SQL to perform the calculations and comparisons in a single query, minimizing the number of operations required.
- Why further optimization is impossible: This approach already uses the most efficient way to perform the calculations and comparisons, and any further optimization would require a different problem formulation or additional constraints.

```cpp
SELECT 
    p.product_id, 
    p.product_name
FROM 
    Product p
JOIN 
    (
        SELECT 
            product_id, 
            SUM(CASE WHEN period_start = '2020-01-01' THEN average_daily_sales ELSE 0 END) / 365 AS avg_2020,
            SUM(CASE WHEN period_start = '2019-01-01' THEN average_daily_sales ELSE 0 END) / 365 AS avg_2019
        FROM 
            Sales
        WHERE 
            (period_start = '2020-01-01' AND period_end = '2020-12-31')
            OR (period_start = '2019-01-01' AND period_end = '2019-12-31')
        GROUP BY 
            product_id
    ) s ON p.product_id = s.product_id
WHERE 
    s.avg_2020 > s.avg_2019;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of products and $m$ is the number of sales records. This is because we are using SQL to perform the calculations and comparisons in a single query.
> - **Space Complexity:** $O(n + m)$, as we need to store the results of the query in memory.
> - **Optimality proof:** This approach is optimal because it uses SQL to perform the calculations and comparisons in a single query, minimizing the number of operations required.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using SQL to perform calculations and comparisons, filtering and grouping data.
- Problem-solving patterns identified: Using a single query to perform multiple calculations and comparisons.
- Optimization techniques learned: Minimizing the number of operations required by using SQL to perform calculations and comparisons.
- Similar problems to practice: Other SQL problems that require filtering, grouping, and comparing data.

**Mistakes to Avoid:**
- Common implementation errors: Not using SQL to perform calculations and comparisons, not filtering and grouping data correctly.
- Edge cases to watch for: Handling null or missing values in the data, handling duplicate values in the data.
- Performance pitfalls: Not using indexes or other optimization techniques to improve query performance.
- Testing considerations: Testing the query with different types of data, testing the query with large amounts of data.