## Median Employee Salary

**Problem Link:** https://leetcode.com/problems/median-employee-salary/description

**Problem Statement:**
- Input format and constraints: The input consists of a `Department` table with columns `id` and `name`, and a `Employee` table with columns `id`, `name`, `salary`, and `departmentId`. The `departmentId` in the `Employee` table references the `id` in the `Department` table.
- Expected output format: The output should be the median salary for each department.
- Key requirements and edge cases to consider: The solution should handle cases where the number of employees in a department is even or odd, and it should also handle cases where there are no employees in a department.
- Example test cases with explanations:
  - If the `Employee` table contains the following rows: `(1, 'John', 30000, 1)`, `(2, 'Jane', 40000, 1)`, `(3, 'Bob', 50000, 2)`, the output should be: `(1, 35000.0)`, `(2, 50000.0)`.
  - If the `Employee` table contains the following rows: `(1, 'John', 30000, 1)`, `(2, 'Jane', 40000, 1)`, `(3, 'Bob', 50000, 1)`, the output should be: `(1, 40000.0)`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the median salary for each department, we need to first group the employees by their department, then sort the salaries within each group, and finally calculate the median.
- Step-by-step breakdown of the solution:
  1. Group the employees by their department using a `GROUP BY` clause.
  2. Sort the salaries within each group using an `ORDER BY` clause.
  3. Calculate the median for each group.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, as it involves simple grouping, sorting, and calculation steps.

```cpp
SELECT 
  d.name AS Department,
  AVG(e1.salary) AS MedianSalary
FROM 
  Employee e1
JOIN 
  Employee e2 ON e1.departmentId = e2.departmentId
  AND e1.salary = e2.salary
JOIN 
  Department d ON e1.departmentId = d.id
GROUP BY 
  d.name
HAVING 
  COUNT(e2.salary) = (SELECT COUNT(*) FROM Employee e3 WHERE e3.departmentId = e1.departmentId) / 2
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of rows in the `Employee` table. This is because we are joining the `Employee` table with itself, which results in a quadratic time complexity.
> - **Space Complexity:** $O(n)$, where $n$ is the number of rows in the `Employee` table. This is because we need to store the joined table in memory.
> - **Why these complexities occur:** The time complexity occurs because of the self-join, and the space complexity occurs because of the need to store the joined table.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a window function to calculate the median salary for each department.
- Detailed breakdown of the approach:
  1. Use a window function to calculate the median salary for each department.
  2. Use a `ROW_NUMBER` function to assign a row number to each employee within their department.
  3. Use a `COUNT` function to count the number of employees in each department.
  4. Calculate the median salary for each department.
- Proof of optimality: This approach is optimal because it uses a window function, which is more efficient than a self-join.
- Why further optimization is impossible: This approach is already optimal because it uses a window function, which is the most efficient way to calculate the median salary for each department.

```sql
WITH ranked_employees AS (
  SELECT 
    departmentId,
    salary,
    ROW_NUMBER() OVER (PARTITION BY departmentId ORDER BY salary) AS row_num,
    COUNT(*) OVER (PARTITION BY departmentId) AS total_count
  FROM 
    Employee
)
SELECT 
  d.name AS Department,
  AVG(r.salary) AS MedianSalary
FROM 
  ranked_employees r
JOIN 
  Department d ON r.departmentId = d.id
WHERE 
  r.row_num = (r.total_count + 1) / 2 OR r.row_num = (r.total_count + 2) / 2
GROUP BY 
  d.name
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of rows in the `Employee` table. This is because we are using a window function, which involves sorting the rows.
> - **Space Complexity:** $O(n)$, where $n$ is the number of rows in the `Employee` table. This is because we need to store the ranked employees in memory.
> - **Optimality proof:** This approach is optimal because it uses a window function, which is more efficient than a self-join.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Window functions, row numbering, and median calculation.
- Problem-solving patterns identified: Using window functions to calculate aggregate values.
- Optimization techniques learned: Using window functions instead of self-joins.
- Similar problems to practice: Calculating the median of a large dataset, using window functions to calculate aggregate values.

**Mistakes to Avoid:**
- Common implementation errors: Using self-joins instead of window functions, not handling edge cases.
- Edge cases to watch for: Handling cases where the number of employees in a department is even or odd.
- Performance pitfalls: Using self-joins instead of window functions.
- Testing considerations: Testing the solution with different datasets, including edge cases.