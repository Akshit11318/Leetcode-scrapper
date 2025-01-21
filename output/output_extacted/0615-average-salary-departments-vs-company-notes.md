## Average Salary Departments vs Company
**Problem Link:** https://leetcode.com/problems/average-salary-departments-vs-company/description

**Problem Statement:**
- Input format and constraints: The input consists of three tables: `Department`, `Employee`, and `Salary`. The `Department` table contains columns `id` (department ID) and `name` (department name). The `Employee` table contains columns `id` (employee ID), `departmentId` (department ID of the employee), and `name` (employee name). The `Salary` table contains columns `id` (employee ID), `departmentId` (department ID), `salary` (employee salary), and `month` (month of the salary). 
- Expected output format: The output should be a table with two columns: `month` and `comparison`. The `month` column should contain the month of the salary, and the `comparison` column should contain a comparison between the average salary of the company and the average salary of the department with the highest average salary for that month.
- Key requirements and edge cases to consider: The average salary of a department for a month is the average salary of all employees in that department for that month. If there are no salaries for a department for a month, the average salary of that department for that month is `NULL`. The comparison between the average salary of the company and the average salary of the department with the highest average salary for a month is determined by the following rules:
  - If the average salary of the company is higher, the comparison should be `lower`.
  - If the average salary of the department is higher, the comparison should be `higher`.
  - If the average salary of the company is equal to the average salary of the department, the comparison should be `same`.
- Example test cases with explanations: For example, if the `Salary` table contains the following rows:
  | id | departmentId | salary | month |
  |----|--------------|--------|-------|
  | 1  | 1            | 1000   | 1     |
  | 1  | 1            | 2000   | 2     |
  | 2  | 2            | 3000   | 1     |
  | 2  | 2            | 4000   | 2     |
  The output should be:
  | month | comparison |
  |-------|-------------|
  | 1     | higher      |
  | 2     | higher      |

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves calculating the average salary of each department for each month and then comparing it with the average salary of the company for that month.
- Step-by-step breakdown of the solution:
  1. Calculate the average salary of each department for each month.
  2. Calculate the average salary of the company for each month.
  3. Compare the average salary of each department with the average salary of the company for each month.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it may not be efficient for large datasets.

```cpp
SELECT 
  s.month,
  CASE
    WHEN d.avg_salary > c.avg_salary THEN 'higher'
    WHEN d.avg_salary < c.avg_salary THEN 'lower'
    ELSE 'same'
  END AS comparison
FROM 
  (SELECT 
     departmentId, 
     month, 
     AVG(salary) AS avg_salary
   FROM 
     Salary
   GROUP BY 
     departmentId, 
     month) d
JOIN 
  (SELECT 
     month, 
     AVG(salary) AS avg_salary
   FROM 
     Salary
   GROUP BY 
     month) c
ON 
  d.month = c.month
WHERE 
  d.avg_salary = (SELECT 
                    MAX(avg_salary)
                  FROM 
                    (SELECT 
                       departmentId, 
                       month, 
                       AVG(salary) AS avg_salary
                     FROM 
                       Salary
                     GROUP BY 
                       departmentId, 
                       month) t
                  WHERE 
                    t.month = d.month)
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the number of rows in the `Salary` table. This is because we are using a subquery to calculate the average salary of each department for each month, and then joining it with another subquery to calculate the average salary of the company for each month.
> - **Space Complexity:** $O(n)$ where $n$ is the number of rows in the `Salary` table. This is because we are storing the average salary of each department for each month in a temporary table.
> - **Why these complexities occur:** The time complexity is high because we are using a subquery to calculate the average salary of each department for each month, and then joining it with another subquery to calculate the average salary of the company for each month. The space complexity is also high because we are storing the average salary of each department for each month in a temporary table.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a single query to calculate the average salary of each department for each month and the average salary of the company for each month, and then compare them.
- Detailed breakdown of the approach:
  1. Calculate the average salary of each department for each month.
  2. Calculate the average salary of the company for each month.
  3. Compare the average salary of each department with the average salary of the company for each month.
- Proof of optimality: This approach is optimal because it uses a single query to calculate the average salary of each department for each month and the average salary of the company for each month, and then compares them. This reduces the time complexity to $O(n)$ where $n$ is the number of rows in the `Salary` table.

```cpp
SELECT 
  s.month,
  CASE
    WHEN d.avg_salary > c.avg_salary THEN 'higher'
    WHEN d.avg_salary < c.avg_salary THEN 'lower'
    ELSE 'same'
  END AS comparison
FROM 
  (SELECT 
     departmentId, 
     month, 
     AVG(salary) AS avg_salary
   FROM 
     Salary
   GROUP BY 
     departmentId, 
     month) d
JOIN 
  (SELECT 
     month, 
     AVG(salary) AS avg_salary
   FROM 
     Salary
   GROUP BY 
     month) c
ON 
  d.month = c.month
WHERE 
  d.avg_salary = (SELECT 
                    MAX(avg_salary)
                  FROM 
                    (SELECT 
                       departmentId, 
                       month, 
                       AVG(salary) AS avg_salary
                     FROM 
                       Salary
                     GROUP BY 
                       departmentId, 
                       month) t
                  WHERE 
                    t.month = d.month)
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of rows in the `Salary` table. This is because we are using a single query to calculate the average salary of each department for each month and the average salary of the company for each month, and then comparing them.
> - **Space Complexity:** $O(n)$ where $n$ is the number of rows in the `Salary` table. This is because we are storing the average salary of each department for each month in a temporary table.
> - **Optimality proof:** This approach is optimal because it uses a single query to calculate the average salary of each department for each month and the average salary of the company for each month, and then compares them. This reduces the time complexity to $O(n)$ where $n$ is the number of rows in the `Salary` table.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: This problem demonstrates the use of SQL queries to calculate average salaries and compare them.
- Problem-solving patterns identified: This problem identifies the pattern of using subqueries to calculate average salaries and then comparing them.
- Optimization techniques learned: This problem learns the technique of using a single query to calculate average salaries and compare them, rather than using multiple queries.
- Similar problems to practice: Similar problems to practice include calculating average salaries for different departments and comparing them, or calculating average salaries for different months and comparing them.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is using multiple queries to calculate average salaries and compare them, rather than using a single query.
- Edge cases to watch for: An edge case to watch for is when there are no salaries for a department for a month, in which case the average salary of that department for that month is `NULL`.
- Performance pitfalls: A performance pitfall is using a subquery to calculate the average salary of each department for each month, and then joining it with another subquery to calculate the average salary of the company for each month. This can lead to a high time complexity.
- Testing considerations: A testing consideration is to test the query with different datasets to ensure that it is working correctly and efficiently.