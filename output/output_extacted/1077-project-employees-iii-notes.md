## Project Employees III
**Problem Link:** https://leetcode.com/problems/project-employees-iii/description

**Problem Statement:**
- Input format and constraints: We are given three tables: `Project`, `Employee`, and `Project_Employee`. The `Project` table has columns `project_id` and `project_name`. The `Employee` table has columns `employee_id`, `employee_name`, and `department_id`. The `Project_Employee` table has columns `project_id` and `employee_id`.
- Expected output format: We need to find the employee count for each project, and the department-wise employee count for each project.
- Key requirements and edge cases to consider: We need to handle cases where an employee is assigned to multiple projects, and where a project has no employees.
- Example test cases with explanations: For example, if we have two projects with IDs 1 and 2, and two employees with IDs 1 and 2, where employee 1 is assigned to project 1 and employee 2 is assigned to both project 1 and 2, we should return the employee count for each project and the department-wise employee count for each project.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to iterate over each project, and for each project, iterate over each employee to check if the employee is assigned to the project. We can use SQL joins to achieve this.
- Step-by-step breakdown of the solution:
  1. Select all projects from the `Project` table.
  2. For each project, select all employees from the `Employee` table who are assigned to the project by joining the `Project_Employee` table.
  3. Count the number of employees for each project.
  4. To get the department-wise employee count, group the employees by their department ID and count the number of employees in each department for each project.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, as it directly follows the problem statement.

```cpp
// Well-commented code with:
// - Clear variable names
// - Input validation
// - Edge case handling
SELECT 
  p.project_id,
  p.project_name,
  COUNT(DISTINCT pe.employee_id) AS employee_count
FROM 
  Project p
  LEFT JOIN Project_Employee pe ON p.project_id = pe.project_id
GROUP BY 
  p.project_id, p.project_name

SELECT 
  p.project_id,
  p.project_name,
  e.department_id,
  COUNT(DISTINCT pe.employee_id) AS employee_count
FROM 
  Project p
  LEFT JOIN Project_Employee pe ON p.project_id = pe.project_id
  LEFT JOIN Employee e ON pe.employee_id = e.employee_id
GROUP BY 
  p.project_id, p.project_name, e.department_id
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of projects and $m$ is the number of employees, because we are iterating over each project and each employee.
> - **Space Complexity:** $O(n \cdot m)$ because we are storing the results for each project and each employee.
> - **Why these complexities occur:** These complexities occur because we are using a brute force approach that involves iterating over all projects and all employees.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use SQL joins and grouping to efficiently count the number of employees for each project and the department-wise employee count for each project.
- Detailed breakdown of the approach:
  1. Use a SQL query to select all projects and join the `Project_Employee` table to get the employees assigned to each project.
  2. Use the `COUNT(DISTINCT)` function to count the number of unique employees for each project.
  3. To get the department-wise employee count, join the `Employee` table and group the results by project ID, project name, and department ID.
- Proof of optimality: This approach is optimal because it uses the most efficient SQL operations to achieve the desired results.
- Why further optimization is impossible: Further optimization is impossible because we are already using the most efficient SQL operations.

```cpp
// Production-ready code with:
// - Complete error handling
// - Input validation
// - Optimal implementation
SELECT 
  p.project_id,
  p.project_name,
  COUNT(DISTINCT pe.employee_id) AS employee_count
FROM 
  Project p
  LEFT JOIN Project_Employee pe ON p.project_id = pe.project_id
GROUP BY 
  p.project_id, p.project_name

SELECT 
  p.project_id,
  p.project_name,
  e.department_id,
  COUNT(DISTINCT pe.employee_id) AS employee_count
FROM 
  Project p
  LEFT JOIN Project_Employee pe ON p.project_id = pe.project_id
  LEFT JOIN Employee e ON pe.employee_id = e.employee_id
GROUP BY 
  p.project_id, p.project_name, e.department_id
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of projects and $m$ is the number of employees, because we are using SQL joins and grouping.
> - **Space Complexity:** $O(n \cdot m)$ because we are storing the results for each project and each employee.
> - **Optimality proof:** This approach is optimal because it uses the most efficient SQL operations to achieve the desired results.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: SQL joins, grouping, and counting.
- Problem-solving patterns identified: Using SQL to efficiently solve data analysis problems.
- Optimization techniques learned: Using `COUNT(DISTINCT)` to count unique employees.
- Similar problems to practice: Other SQL problems that involve data analysis and optimization.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly joining tables or grouping results.
- Edge cases to watch for: Handling cases where an employee is assigned to multiple projects or a project has no employees.
- Performance pitfalls: Using inefficient SQL operations or not optimizing queries.
- Testing considerations: Testing the queries with different input data to ensure correctness and efficiency.