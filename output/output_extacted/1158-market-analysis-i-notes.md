## Market Analysis I

**Problem Link:** [https://leetcode.com/problems/market-analysis-i/description](https://leetcode.com/problems/market-analysis-i/description)

**Problem Statement:**
- Input format and constraints: The problem requires writing a SQL query to analyze the `Users`, `Orders`, and `Sellers` tables in a database. The `Users` table contains user information, the `Orders` table contains order information, and the `Sellers` table contains seller information. The goal is to calculate the number of buyers and sellers for each month in a specific year.
- Expected output format: The output should be a table with two columns, `month` and `number_of_buyers_and_sellers`, where `month` is the month of the year and `number_of_buyers_and_sellers` is the total number of buyers and sellers for that month.
- Key requirements and edge cases to consider: The query should only consider orders made in a specific year (2019) and should count each buyer and seller only once per month, even if they made multiple orders in the same month.
- Example test cases with explanations: For example, if the input tables contain the following data:
  - `Users`: (1, 'John'), (2, 'Jane')
  - `Orders`: (1, 1, 1, '2019-01-01'), (2, 1, 2, '2019-01-15'), (3, 2, 1, '2019-02-01')
  - `Sellers`: (1, 'Seller1'), (2, 'Seller2')
  Then the output should be:
  - (1, 3), (2, 2)

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves using a SQL query to join the `Orders`, `Users`, and `Sellers` tables and then grouping the results by month and counting the number of unique buyers and sellers.
- Step-by-step breakdown of the solution:
  1. Join the `Orders`, `Users`, and `Sellers` tables on the `buyer_id` and `seller_id` columns.
  2. Filter the results to only include orders made in the year 2019.
  3. Group the results by month and count the number of unique buyers and sellers.
- Why this approach comes to mind first: This approach is straightforward and involves using basic SQL operations to join and group the data.

```sql
SELECT 
  MONTH(o.order_date) AS month,
  COUNT(DISTINCT u.user_id) + COUNT(DISTINCT s.seller_id) AS number_of_buyers_and_sellers
FROM 
  Orders o
  JOIN Users u ON o.buyer_id = u.user_id
  JOIN Sellers s ON o.seller_id = s.seller_id
WHERE 
  o.order_date LIKE '2019-%'
GROUP BY 
  MONTH(o.order_date)
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of rows in the `Orders` table. This is because the query involves joining and grouping the data, which can be done in $O(n \log n)$ time using standard SQL algorithms.
> - **Space Complexity:** $O(n)$, where $n$ is the number of rows in the `Orders` table. This is because the query involves storing the results of the join and group operations in memory.
> - **Why these complexities occur:** The time complexity occurs because the query involves joining and grouping the data, which can be done in $O(n \log n)$ time using standard SQL algorithms. The space complexity occurs because the query involves storing the results of the join and group operations in memory.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a SQL query with a `UNION` operator to combine the results of two separate queries, one for buyers and one for sellers.
- Detailed breakdown of the approach:
  1. Write a query to count the number of unique buyers for each month.
  2. Write a query to count the number of unique sellers for each month.
  3. Use the `UNION` operator to combine the results of the two queries.
- Proof of optimality: This approach is optimal because it avoids the need to join the `Users` and `Sellers` tables, which can be expensive operations. Instead, it uses two separate queries to count the number of unique buyers and sellers, and then combines the results using the `UNION` operator.

```sql
SELECT 
  MONTH(o.order_date) AS month,
  COUNT(DISTINCT o.buyer_id) AS number_of_buyers
FROM 
  Orders o
WHERE 
  o.order_date LIKE '2019-%'
GROUP BY 
  MONTH(o.order_date)

UNION ALL

SELECT 
  MONTH(o.order_date) AS month,
  COUNT(DISTINCT o.seller_id) AS number_of_sellers
FROM 
  Orders o
WHERE 
  o.order_date LIKE '2019-%'
GROUP BY 
  MONTH(o.order_date)
```

However, this query does not provide the exact output required by the problem, as it returns two separate counts for buyers and sellers. To get the total count, we can use the following query:

```sql
SELECT 
  month,
  SUM(number_of_buyers_and_sellers) AS number_of_buyers_and_sellers
FROM 
  (
    SELECT 
      MONTH(o.order_date) AS month,
      COUNT(DISTINCT o.buyer_id) AS number_of_buyers_and_sellers
    FROM 
      Orders o
    WHERE 
      o.order_date LIKE '2019-%'
    GROUP BY 
      MONTH(o.order_date)

    UNION ALL

    SELECT 
      MONTH(o.order_date) AS month,
      COUNT(DISTINCT o.seller_id) AS number_of_buyers_and_sellers
    FROM 
      Orders o
    WHERE 
      o.order_date LIKE '2019-%'
    GROUP BY 
      MONTH(o.order_date)
  ) AS subquery
GROUP BY 
  month
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of rows in the `Orders` table. This is because the query involves grouping and counting the data, which can be done in $O(n \log n)$ time using standard SQL algorithms.
> - **Space Complexity:** $O(n)$, where $n$ is the number of rows in the `Orders` table. This is because the query involves storing the results of the group and count operations in memory.
> - **Optimality proof:** This approach is optimal because it avoids the need to join the `Users` and `Sellers` tables, which can be expensive operations. Instead, it uses two separate queries to count the number of unique buyers and sellers, and then combines the results using the `UNION` operator and a subquery to get the total count.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of SQL queries to analyze and manipulate data.
- Problem-solving patterns identified: The problem requires the use of grouping and counting operations to analyze the data.
- Optimization techniques learned: The optimal solution involves using a `UNION` operator to combine the results of two separate queries, which avoids the need to join the `Users` and `Sellers` tables.
- Similar problems to practice: Other problems that involve analyzing and manipulating data using SQL queries.

**Mistakes to Avoid:**
- Common implementation errors: One common error is to forget to include the `DISTINCT` keyword when counting the number of unique buyers and sellers.
- Edge cases to watch for: The problem requires handling edge cases where there are no buyers or sellers for a particular month.
- Performance pitfalls: The query can be slow if the `Orders` table is very large, so it's important to optimize the query using indexes and other techniques.
- Testing considerations: The query should be tested with different inputs and edge cases to ensure that it produces the correct results.