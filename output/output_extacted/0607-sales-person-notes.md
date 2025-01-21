## Sales Person
**Problem Link:** https://leetcode.com/problems/sales-person/description

**Problem Statement:**
- Input format and constraints: We have three tables: `sales`, `company`, and `orders`. The `sales` table contains information about salespeople, the `company` table contains information about companies, and the `orders` table contains information about orders. We need to find the names of all salespeople who have not made any sales to a particular company.
- Expected output format: A list of names of salespeople who have not made any sales to a particular company.
- Key requirements and edge cases to consider: We need to consider the case where a salesperson has made sales to multiple companies, but not to the specified company. We also need to consider the case where a salesperson has not made any sales at all.
- Example test cases with explanations: 
  - If we have a salesperson who has made sales to company A and company B, but not to company C, we should include this salesperson in the output if we are looking for salespeople who have not made sales to company C.
  - If we have a salesperson who has not made any sales at all, we should include this salesperson in the output if we are looking for salespeople who have not made sales to any company.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can start by iterating over each salesperson and checking if they have made any sales to the specified company.
- Step-by-step breakdown of the solution: 
  1. Iterate over each salesperson in the `sales` table.
  2. For each salesperson, iterate over each order in the `orders` table.
  3. For each order, check if the salesperson made the sale and if the sale was to the specified company.
  4. If the salesperson made a sale to the specified company, mark them as having made a sale to that company.
  5. After checking all orders for a salesperson, if they have not made any sales to the specified company, add their name to the output list.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient because it involves iterating over the `orders` table for each salesperson.

```cpp
// Brute force approach
SELECT name
FROM sales
WHERE name NOT IN (
  SELECT s.name
  FROM sales s
  JOIN orders o ON s.sales_id = o.sales_id
  JOIN company c ON o.com_id = c.com_id
  WHERE c.name = 'Red'
)
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of rows in the `sales` table, because we are iterating over the `orders` table for each salesperson.
> - **Space Complexity:** $O(n)$, where $n$ is the number of rows in the `sales` table, because we are storing the names of salespeople who have not made any sales to the specified company.
> - **Why these complexities occur:** These complexities occur because we are using a nested loop approach to iterate over the `orders` table for each salesperson.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a single SQL query with a `NOT IN` clause to find the names of salespeople who have not made any sales to the specified company.
- Detailed breakdown of the approach: 
  1. Use a subquery to find the names of salespeople who have made sales to the specified company.
  2. Use a `NOT IN` clause to find the names of salespeople who are not in the subquery result set.
- Proof of optimality: This approach is optimal because it only requires a single pass over the data and uses efficient SQL operations.
- Why further optimization is impossible: Further optimization is impossible because we need to check each salesperson's orders to determine if they have made any sales to the specified company.

```cpp
// Optimal approach
SELECT name
FROM sales
WHERE name NOT IN (
  SELECT s.name
  FROM sales s
  JOIN orders o ON s.sales_id = o.sales_id
  JOIN company c ON o.com_id = c.com_id
  WHERE c.name = 'Red'
)
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the `sales` table, because we are using a single SQL query with a `NOT IN` clause.
> - **Space Complexity:** $O(n)$, where $n$ is the number of rows in the `sales` table, because we are storing the names of salespeople who have not made any sales to the specified company.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the data and uses efficient SQL operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: We demonstrated the use of SQL queries with subqueries and `NOT IN` clauses to solve the problem.
- Problem-solving patterns identified: We identified the pattern of using a subquery to find the names of salespeople who have made sales to the specified company, and then using a `NOT IN` clause to find the names of salespeople who have not made any sales to the specified company.
- Optimization techniques learned: We learned the technique of using a single SQL query with a `NOT IN` clause to optimize the solution.
- Similar problems to practice: We can practice similar problems by finding the names of customers who have not made any purchases from a particular company, or by finding the names of employees who have not worked on a particular project.

**Mistakes to Avoid:**
- Common implementation errors: We should avoid using nested loops to iterate over the `orders` table for each salesperson, because this approach is inefficient.
- Edge cases to watch for: We should watch for edge cases where a salesperson has not made any sales at all, or where a salesperson has made sales to multiple companies but not to the specified company.
- Performance pitfalls: We should avoid using inefficient SQL operations, such as using a `NOT EXISTS` clause instead of a `NOT IN` clause, because this can lead to poor performance.
- Testing considerations: We should test the solution with different input data sets to ensure that it works correctly and efficiently.