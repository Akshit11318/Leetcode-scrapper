## Department Top Three Salaries

**Problem Link:** https://leetcode.com/problems/department-top-three-salaries/description

**Problem Statement:**
- Input format and constraints: The problem provides three tables: `Employee`, `Department`, and a desired output table. The `Employee` table contains columns `id`, `name`, `salary`, and `departmentId`. The `Department` table contains columns `id` and `name`. The goal is to write a SQL query that returns the top three salaries for each department.
- Expected output format: The output should be a table with columns `Department`, `Employee`, and `Salary`, where each row represents one of the top three salaries in a department.
- Key requirements and edge cases to consider: Handling cases where a department has less than three employees, and ensuring the top three salaries are correctly identified.
- Example test cases with explanations: For example, given two departments, "Sales" and "Engineering", with employees having different salaries, the query should return the top three salaries for each department.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to use a subquery to get the top three salaries for each department, and then use the `JOIN` operation to combine the results with the `Department` table.
- Step-by-step breakdown of the solution:
  1. Use a subquery to get the top three salaries for each department.
  2. Use the `JOIN` operation to combine the results with the `Department` table.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it may not be the most efficient solution.

```cpp
-- SQL query using a subquery and JOIN
SELECT D.name AS Department, E1.name AS Employee, E1.salary AS Salary
FROM Employee E1
JOIN Department D ON E1.departmentId = D.id
WHERE (
  SELECT COUNT(*)
  FROM Employee E2
  WHERE E2.departmentId = E1.departmentId AND E2.salary > E1.salary
) < 3;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of rows in the `Employee` table, because the subquery is executed for each row in the `Employee` table.
> - **Space Complexity:** $O(n)$, where $n$ is the number of rows in the `Employee` table, because we need to store the results of the subquery.
> - **Why these complexities occur:** The subquery is executed for each row in the `Employee` table, which leads to a high time complexity. The space complexity is also high because we need to store the results of the subquery.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use the `DENSE_RANK()` function to assign a rank to each employee in each department based on their salary.
- Detailed breakdown of the approach:
  1. Use the `DENSE_RANK()` function to assign a rank to each employee in each department based on their salary.
  2. Use a `WHERE` clause to filter the results to only include the top three salaries for each department.
- Proof of optimality: This approach is optimal because it only requires a single pass through the `Employee` table, and the `DENSE_RANK()` function is efficient.

```sql
-- SQL query using DENSE_RANK()
SELECT D.name AS Department, E1.name AS Employee, E1.salary AS Salary
FROM (
  SELECT departmentId, name, salary,
         DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rank
  FROM Employee
) E1
JOIN Department D ON E1.departmentId = D.id
WHERE E1.rank <= 3;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of rows in the `Employee` table, because the `DENSE_RANK()` function requires sorting the data.
> - **Space Complexity:** $O(n)$, where $n$ is the number of rows in the `Employee` table, because we need to store the results of the `DENSE_RANK()` function.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the `Employee` table, and the `DENSE_RANK()` function is efficient.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The use of window functions, such as `DENSE_RANK()`, to assign a rank to each row in a partition.
- Problem-solving patterns identified: The use of subqueries and `JOIN` operations to combine data from multiple tables.
- Optimization techniques learned: The use of efficient window functions to reduce the time complexity of the query.
- Similar problems to practice: Other problems that involve ranking or aggregating data, such as finding the top N salaries for each department.

**Mistakes to Avoid:**
- Common implementation errors: Using a subquery instead of a window function, which can lead to high time complexity.
- Edge cases to watch for: Handling cases where a department has less than three employees.
- Performance pitfalls: Using inefficient window functions or subqueries, which can lead to high time complexity.
- Testing considerations: Testing the query with different inputs and edge cases to ensure it produces the correct results.