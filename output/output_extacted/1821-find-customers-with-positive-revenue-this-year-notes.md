## Find Customers With Positive Revenue This Year

**Problem Link:** https://leetcode.com/problems/find-customers-with-positive-revenue-this-year/description

**Problem Statement:**
- Input format and constraints: The problem involves finding customers with positive revenue from the `Customers` and `Orders` tables in a database. The `Customers` table contains customer information, and the `Orders` table contains order information. The `Customers` table has a `customer_id` column, and the `Orders` table has `customer_id` and `order_date` columns.
- Expected output format: The output should be a list of `customer_id` values for customers with positive revenue in the current year.
- Key requirements and edge cases to consider: The current year is determined by the `order_date` column in the `Orders` table. A customer has positive revenue if they have at least one order in the current year.
- Example test cases with explanations:
  - Test case 1: Customers with orders in the current year should be included in the output.
  - Test case 2: Customers without orders in the current year should not be included in the output.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One possible approach is to iterate over all customers, check if they have any orders in the current year, and include them in the output if they do.
- Step-by-step breakdown of the solution:
  1. Get the current year from the `order_date` column in the `Orders` table.
  2. Iterate over all customers in the `Customers` table.
  3. For each customer, check if they have any orders in the current year by joining the `Customers` table with the `Orders` table on the `customer_id` column and filtering by the current year.
  4. If a customer has at least one order in the current year, include their `customer_id` in the output.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it may not be the most efficient solution.

```cpp
SELECT c.customer_id
FROM Customers c
WHERE c.customer_id IN (
  SELECT o.customer_id
  FROM Orders o
  WHERE YEAR(o.order_date) = YEAR(CURDATE())
)
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where $n$ is the number of customers and $m$ is the number of orders. This is because we are iterating over all customers and checking if they have any orders in the current year.
> - **Space Complexity:** $O(n)$, where $n$ is the number of customers. This is because we are storing the output in a list of customer IDs.
> - **Why these complexities occur:** The time complexity is high because we are iterating over all customers and orders, and the space complexity is moderate because we are storing the output in a list.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a single SQL query to find the customers with positive revenue in the current year by joining the `Customers` table with the `Orders` table on the `customer_id` column and filtering by the current year.
- Detailed breakdown of the approach:
  1. Join the `Customers` table with the `Orders` table on the `customer_id` column.
  2. Filter the joined table by the current year using the `order_date` column.
  3. Select the distinct `customer_id` values from the filtered table.
- Proof of optimality: This approach is optimal because it uses a single SQL query to find the customers with positive revenue in the current year, which reduces the time complexity compared to the brute force approach.
- Why further optimization is impossible: Further optimization is impossible because we are already using a single SQL query to find the customers with positive revenue in the current year.

```cpp
SELECT DISTINCT c.customer_id
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
WHERE YEAR(o.order_date) = YEAR(CURDATE())
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where $n$ is the number of customers and $m$ is the number of orders. However, the actual time complexity is lower than the brute force approach because the database can optimize the join operation.
> - **Space Complexity:** $O(n)$, where $n$ is the number of customers. This is because we are storing the output in a list of customer IDs.
> - **Optimality proof:** The optimality of this approach is proven by the fact that it uses a single SQL query to find the customers with positive revenue in the current year, which reduces the time complexity compared to the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of SQL queries to solve a problem, including joining tables and filtering by conditions.
- Problem-solving patterns identified: The problem identifies the pattern of using a single SQL query to solve a problem, which can reduce the time complexity compared to using multiple queries.
- Optimization techniques learned: The problem teaches the optimization technique of using a single SQL query to solve a problem, which can reduce the time complexity compared to using multiple queries.
- Similar problems to practice: Similar problems to practice include finding customers with positive revenue in a given year, finding orders with a total cost greater than a certain amount, and finding customers who have placed orders in a given year.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is to use multiple SQL queries to solve the problem, which can increase the time complexity.
- Edge cases to watch for: An edge case to watch for is when a customer has no orders in the current year, in which case they should not be included in the output.
- Performance pitfalls: A performance pitfall is to use a subquery to find the customers with positive revenue in the current year, which can increase the time complexity.
- Testing considerations: A testing consideration is to test the query with a large dataset to ensure that it performs well and returns the correct results.