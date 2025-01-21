## Sales Analysis II
**Problem Link:** https://leetcode.com/problems/sales-analysis-ii/description

**Problem Statement:**
- Input format and constraints: The problem requires analyzing sales data from two tables, `Orders` and `Company`. The `Orders` table contains columns for `order_id`, `order_date`, `customer_id`, and `company_id`, while the `Company` table has columns for `company_id` and `name`. The goal is to find the `company_id` and `name` of companies that have no orders placed between the dates '2015-01-01' and '2015-12-31'.
- Expected output format: The output should be a table with two columns, `company_id` and `name`, representing the `company_id` and `name` of companies that did not place any orders during the specified period.
- Key requirements and edge cases to consider: The solution must handle cases where a company has no orders during the specified period and must join the two tables based on `company_id`.
- Example test cases with explanations: 
    - Test case 1: A company with `company_id` = 1 has no orders during the specified period. The expected output should include this company.
    - Test case 2: A company with `company_id` = 2 has orders during the specified period. The expected output should not include this company.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Start by selecting all `company_id` and `name` from the `Company` table. Then, for each company, check if there are any orders in the `Orders` table between '2015-01-01' and '2015-12-31'.
- Step-by-step breakdown of the solution:
    1. Select all `company_id` and `name` from the `Company` table.
    2. For each company, use a subquery to check if there are any orders in the `Orders` table during the specified period.
    3. If no orders are found for a company, include that company in the result set.
- Why this approach comes to mind first: This approach seems straightforward because it directly checks each company against the orders table, ensuring that only companies without orders during the specified period are included in the result.

```cpp
SELECT c.company_id, c.name
FROM Company c
WHERE c.company_id NOT IN (
    SELECT o.company_id
    FROM Orders o
    WHERE o.order_date BETWEEN '2015-01-01' AND '2015-12-31'
)
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of companies and $m$ is the number of orders. This is because for each company, we potentially scan all orders.
> - **Space Complexity:** $O(n + m)$, as we need to store all companies and orders in memory for the subquery.
> - **Why these complexities occur:** The brute force approach involves nested queries, leading to higher time complexity due to the repeated subquery execution for each company.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of using a subquery for each company, we can perform a `LEFT JOIN` between the `Company` and `Orders` tables on the condition that the order date falls within the specified range. Companies without matching orders will have `NULL` in the `Orders` columns, indicating they did not place orders during the period.
- Detailed breakdown of the approach:
    1. Perform a `LEFT JOIN` between `Company` and `Orders` on `company_id` and the condition that `order_date` is between '2015-01-01' and '2015-12-31'.
    2. Select `company_id` and `name` from the joined table where the `order_id` (or any column from the `Orders` table) is `NULL`, indicating no match was found.
- Proof of optimality: This approach is optimal because it avoids the repeated execution of subqueries for each company, reducing the time complexity significantly.

```sql
SELECT c.company_id, c.name
FROM Company c
LEFT JOIN Orders o
ON c.company_id = o.company_id AND o.order_date BETWEEN '2015-01-01' AND '2015-12-31'
WHERE o.order_id IS NULL
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of companies and $m$ is the number of orders. This is because we perform a single join operation.
> - **Space Complexity:** $O(n + m)$, for storing the joined table.
> - **Optimality proof:** The optimal approach achieves a linear time complexity with respect to the total number of companies and orders, which is the best possible time complexity for this problem, as we must at least read the input once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The importance of joining tables efficiently and avoiding nested queries when possible.
- Problem-solving patterns identified: Recognizing when a `LEFT JOIN` can replace a subquery, improving performance.
- Optimization techniques learned: Using `JOIN` operations instead of subqueries to reduce time complexity.
- Similar problems to practice: Other SQL problems involving joins and subqueries, such as finding unmatched records between tables.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect join conditions or forgetting to handle `NULL` values from `LEFT JOIN` operations.
- Edge cases to watch for: Companies with no orders at all, or orders outside the specified date range.
- Performance pitfalls: Using subqueries instead of joins for large datasets.
- Testing considerations: Ensure to test with various datasets, including edge cases like companies with no orders and companies with orders outside the specified period.