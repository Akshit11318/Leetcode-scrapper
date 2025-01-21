## Employees with Missing Information

**Problem Link:** https://leetcode.com/problems/employees-with-missing-information/description

**Problem Statement:**
- Input format and constraints: The problem involves two tables, `Employees` and `Salaries`. The `Employees` table contains columns `employee_id`, `name`, and `month`, while the `Salaries` table contains columns `employee_id`, `salary`, and `month`. The task is to find the employee IDs of employees who have missing information.
- Expected output format: A table with one column, `employee_id`, containing the IDs of employees with missing information.
- Key requirements and edge cases to consider: An employee is considered to have missing information if there is a month in the `Salaries` table where the employee's salary is not listed, or if there is a month in the `Employees` table where the employee's name is not listed.
- Example test cases with explanations: For example, if an employee has a salary listed for January but not for February, or if an employee has a name listed for January but not for February, they would be considered to have missing information.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to iterate through each employee and each month, checking if the employee has a salary listed for that month and if the employee has a name listed for that month.
- Step-by-step breakdown of the solution:
  1. Create a set of all employee IDs.
  2. Create a set of all months.
  3. Iterate through each employee ID and each month.
  4. For each employee ID and month, check if the employee has a salary listed for that month and if the employee has a name listed for that month.
  5. If the employee is missing information for a month, add the employee ID to the result set.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it may not be the most efficient.

```cpp
SELECT e1.employee_id
FROM Employees e1
LEFT JOIN Salaries e2
ON e1.employee_id = e2.employee_id AND e1.month = e2.month
WHERE e2.salary IS NULL
UNION
SELECT e2.employee_id
FROM Salaries e2
LEFT JOIN Employees e1
ON e2.employee_id = e1.employee_id AND e2.month = e1.month
WHERE e1.name IS NULL
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of employees and $m$ is the number of months. This is because we are iterating through each employee and each month.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of employees and $m$ is the number of months. This is because we are storing the result set, which can contain up to $n \cdot m$ employee IDs.
> - **Why these complexities occur:** These complexities occur because we are using a brute force approach, which involves iterating through each employee and each month.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a SQL query to find the employee IDs of employees who have missing information.
- Detailed breakdown of the approach:
  1. Use a `LEFT JOIN` to join the `Employees` table with the `Salaries` table on the `employee_id` and `month` columns.
  2. Use a `WHERE` clause to filter out rows where the `salary` is not `NULL`.
  3. Use a `UNION` operator to combine the result with another query that finds employee IDs of employees who have missing information in the `Employees` table.
- Proof of optimality: This approach is optimal because it uses a single SQL query to find the employee IDs of employees who have missing information, which is more efficient than iterating through each employee and each month.

```cpp
SELECT e1.employee_id
FROM Employees e1
LEFT JOIN Salaries e2
ON e1.employee_id = e2.employee_id AND e1.month = e2.month
WHERE e2.salary IS NULL
UNION
SELECT e2.employee_id
FROM Salaries e2
LEFT JOIN Employees e1
ON e2.employee_id = e1.employee_id AND e2.month = e1.month
WHERE e1.name IS NULL
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of employees and $m$ is the number of months. This is because we are using a SQL query to find the employee IDs of employees who have missing information.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of employees and $m$ is the number of months. This is because we are storing the result set, which can contain up to $n + m$ employee IDs.
> - **Optimality proof:** This approach is optimal because it uses a single SQL query to find the employee IDs of employees who have missing information, which is more efficient than iterating through each employee and each month.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using SQL queries to find employee IDs of employees who have missing information.
- Problem-solving patterns identified: Using a `LEFT JOIN` and a `WHERE` clause to filter out rows where the `salary` is not `NULL`.
- Optimization techniques learned: Using a single SQL query to find the employee IDs of employees who have missing information.
- Similar problems to practice: Finding employee IDs of employees who have missing information in other tables.

**Mistakes to Avoid:**
- Common implementation errors: Using a brute force approach instead of a SQL query.
- Edge cases to watch for: Employees who have missing information in both the `Employees` table and the `Salaries` table.
- Performance pitfalls: Using a brute force approach, which can be slow for large datasets.
- Testing considerations: Testing the query with different datasets to ensure it returns the correct results.