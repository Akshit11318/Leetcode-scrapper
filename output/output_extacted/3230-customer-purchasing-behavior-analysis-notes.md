## Customer Purchasing Behavior Analysis
**Problem Link:** https://leetcode.com/problems/customer-purchasing-behavior-analysis/description

**Problem Statement:**
- Input format and constraints: We have three tables: `Customers`, `Orders`, and `OrderDetails`. The `Customers` table contains customer information, the `Orders` table contains order information, and the `OrderDetails` table contains order item information. The goal is to analyze customer purchasing behavior.
- Expected output format: The output should be a table that includes the customer ID and the number of orders they have made.
- Key requirements and edge cases to consider: We need to handle cases where a customer has made no orders, and we should only count distinct orders.
- Example test cases with explanations:
  - If a customer has made multiple orders with the same order ID, we should only count it once.
  - If a customer has made no orders, they should still be included in the output with a count of 0.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can start by selecting all customers from the `Customers` table. Then, for each customer, we can count the number of distinct orders they have made by joining the `Orders` table with the `OrderDetails` table.
- Step-by-step breakdown of the solution:
  1. Select all customers from the `Customers` table.
  2. For each customer, join the `Orders` table with the `OrderDetails` table on the `order_id` column.
  3. Count the number of distinct orders for each customer.
- Why this approach comes to mind first: This approach is straightforward and involves a simple join and count operation.

```sql
SELECT 
  c.customer_id,
  COUNT(DISTINCT o.order_id) AS count
FROM 
  Customers c
  LEFT JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY 
  c.customer_id
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the total number of rows in the `Customers` and `Orders` tables. This is because we are performing a join operation, which has a time complexity of $O(n \log n)$ in the worst case.
> - **Space Complexity:** $O(n)$, where $n$ is the total number of rows in the `Customers` and `Orders` tables. This is because we need to store the results of the join operation in memory.
> - **Why these complexities occur:** The time complexity occurs because we are performing a join operation, which involves sorting and merging the rows of the two tables. The space complexity occurs because we need to store the results of the join operation in memory.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can optimize the query by using a `LEFT JOIN` instead of a regular `JOIN`. This allows us to include customers who have made no orders in the output.
- Detailed breakdown of the approach:
  1. Select all customers from the `Customers` table.
  2. Perform a `LEFT JOIN` with the `Orders` table on the `customer_id` column.
  3. Count the number of distinct orders for each customer.
- Proof of optimality: This approach is optimal because it only requires a single pass through the data and does not involve any unnecessary operations.

```sql
SELECT 
  c.customer_id,
  COUNT(DISTINCT o.order_id) AS count
FROM 
  Customers c
  LEFT JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY 
  c.customer_id
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the total number of rows in the `Customers` and `Orders` tables. This is because we are performing a join operation, which has a time complexity of $O(n \log n)$ in the worst case.
> - **Space Complexity:** $O(n)$, where $n$ is the total number of rows in the `Customers` and `Orders` tables. This is because we need to store the results of the join operation in memory.
> - **Optimality proof:** The time complexity is optimal because we are only performing a single pass through the data. The space complexity is optimal because we are only storing the results of the join operation in memory.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Join operations, count operations, and group by operations.
- Problem-solving patterns identified: Using a `LEFT JOIN` to include customers who have made no orders in the output.
- Optimization techniques learned: Using a `LEFT JOIN` instead of a regular `JOIN` to optimize the query.
- Similar problems to practice: Other problems that involve join operations and count operations, such as counting the number of orders for each customer or counting the number of products in each order.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to use a `LEFT JOIN` to include customers who have made no orders in the output.
- Edge cases to watch for: Customers who have made no orders, customers who have made multiple orders with the same order ID.
- Performance pitfalls: Using a regular `JOIN` instead of a `LEFT JOIN`, which can result in slower performance.
- Testing considerations: Testing the query with different inputs, such as customers who have made no orders or customers who have made multiple orders with the same order ID.