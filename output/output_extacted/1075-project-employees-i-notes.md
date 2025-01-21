## Project Employees I
**Problem Link:** https://leetcode.com/problems/project-employees-i/description

**Problem Statement:**
- Input format: A table `project` with columns `project_id` and `employee_id`, representing the projects each employee is working on.
- Constraints: The table contains at least one row, and each row has unique combinations of `project_id` and `employee_id`.
- Expected output format: A table with columns `project_id` and `count`, where `count` represents the number of employees working on each project.
- Key requirements and edge cases to consider: Handling projects with no employees, ensuring accurate counts, and avoiding duplicate counts for employees working on multiple projects.
- Example test cases with explanations:
  - A project with multiple employees should return the total count of employees.
  - A project with no employees should not be included in the results.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Iterate through each project and count the employees working on it.
- Step-by-step breakdown of the solution:
  1. Select distinct `project_id` from the `project` table.
  2. For each `project_id`, count the number of rows (i.e., employees) in the `project` table.
  3. Return a table with `project_id` and the corresponding count of employees.
- Why this approach comes to mind first: It directly addresses the problem by counting employees for each project.

```cpp
SELECT project_id, COUNT(employee_id) as count
FROM project
GROUP BY project_id;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the `project` table, because we're scanning the table once.
> - **Space Complexity:** $O(n)$, for storing the results.
> - **Why these complexities occur:** The time complexity is linear because we're performing a single pass through the data, and the space complexity is also linear because we're storing the results for each project.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The SQL query from the brute force approach is already optimized for this problem, as it uses a `GROUP BY` clause which is designed for aggregating data by groups.
- Detailed breakdown of the approach: The query groups the rows of the `project` table by `project_id` and then counts the number of rows in each group, effectively counting the employees per project.
- Proof of optimality: This query is optimal because it minimizes the number of database operations required to solve the problem. It scans the table once and uses an efficient grouping mechanism.
- Why further optimization is impossible: Any attempt to optimize further would likely involve additional database operations or more complex queries, which would not improve performance.

```cpp
SELECT project_id, COUNT(employee_id) as count
FROM project
GROUP BY project_id;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the `project` table.
> - **Space Complexity:** $O(n)$, for storing the results.
> - **Optimality proof:** This approach is optimal because it leverages the database's built-in grouping functionality, which is highly efficient.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Grouping and aggregating data.
- Problem-solving patterns identified: Using SQL's built-in functions for efficient data processing.
- Optimization techniques learned: Leveraging database capabilities to minimize operations.
- Similar problems to practice: Other SQL problems involving aggregation and grouping.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to use `GROUP BY` when aggregating data, or incorrectly using aggregate functions.
- Edge cases to watch for: Projects with no employees, duplicate employee-project combinations.
- Performance pitfalls: Using subqueries or joins when simpler aggregation methods are available.
- Testing considerations: Ensure the query works correctly for projects with multiple employees, single employees, and no employees.