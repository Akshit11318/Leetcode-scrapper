## Department Highest Salary
**Problem Link:** https://leetcode.com/problems/department-highest-salary/description

**Problem Statement:**
- Input format and constraints: The problem involves a table `Employee` with columns `id`, `name`, `salary`, and `departmentId`, and a table `Department` with columns `id` and `name`. The task is to find the department with the highest salary and return the department name.
- Expected output format: A table with the department name.
- Key requirements and edge cases to consider: Handling cases where multiple departments have the same highest salary, ensuring correct join operations between tables, and optimizing queries for performance.
- Example test cases with explanations:
  - Example 1: 
    - Input: 
      ```
      +----+----------+--------+--------------+
      | id | name     | salary | departmentId |
      +----+----------+--------+--------------+
      | 1  | John     | 5000   | 1            |
      | 2  | Alice    | 6000   | 1            |
      | 3  | Bob      | 7000   | 2            |
      +----+----------+--------+--------------+
      ```
      ```
      +----+----------+
      | id | name     |
      +----+----------+
      | 1  | Sales    |
      | 2  | IT       |
      +----+----------+
      ```
    - Output: 
      ```
      +----------+
      | name     |
      +----------+
      | IT       |
      +----------+
      ```
  - Example 2: 
    - Input: 
      ```
      +----+----------+--------+--------------+
      | id | name     | salary | departmentId |
      +----+----------+--------+--------------+
      | 1  | John     | 5000   | 1            |
      | 2  | Alice    | 6000   | 1            |
      +----+----------+--------+--------------+
      ```
      ```
      +----+----------+
      | id | name     |
      +----+----------+
      | 1  | Sales    |
      +----+----------+
      ```
    - Output: 
      ```
      +----------+
      | name     |
      +----------+
      | Sales    |
      +----------+
      ```

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the department with the highest salary, we first need to calculate the maximum salary for each department. Then, we compare these maximum salaries to find the department(s) with the highest salary.
- Step-by-step breakdown of the solution:
  1. **Calculate Maximum Salary per Department:** Query the `Employee` table to find the maximum salary for each department.
  2. **Find the Highest Salary:** From the result of step 1, find the maximum salary across all departments.
  3. **Identify the Department(s):** Query the `Employee` table again to find the department(s) where the salary matches the highest salary found in step 2.
  4. **Return Department Name(s):** Join the identified department(s) with the `Department` table to return the department name(s).

```cpp
// Assuming we have a function to execute SQL queries
void findDepartmentHighestSalary() {
    // Query to find the maximum salary for each department
    string queryMaxSalaries = "SELECT departmentId, MAX(salary) as max_salary FROM Employee GROUP BY departmentId";
    
    // Execute the query and store the results in a map or similar data structure
    map<int, int> maxSalariesPerDept;
    // Assume we have a way to execute the query and populate maxSalariesPerDept
    
    // Find the highest salary across all departments
    int highestSalary = 0;
    for (auto& pair : maxSalariesPerDept) {
        if (pair.second > highestSalary) {
            highestSalary = pair.second;
        }
    }
    
    // Identify the department(s) with the highest salary
    vector<int> highestDeptIds;
    for (auto& pair : maxSalariesPerDept) {
        if (pair.second == highestSalary) {
            highestDeptIds.push_back(pair.first);
        }
    }
    
    // Return the department name(s)
    string queryDeptName = "SELECT name FROM Department WHERE id IN (";
    for (int i = 0; i < highestDeptIds.size(); ++i) {
        queryDeptName += to_string(highestDeptIds[i]);
        if (i < highestDeptIds.size() - 1) {
            queryDeptName += ", ";
        }
    }
    queryDeptName += ")";
    
    // Execute the final query and print the result
    // Assume we have a way to execute the query and print the department name(s)
}

```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of rows in the `Employee` table, because we potentially scan the table twice: once to find the maximum salaries per department and again to find the departments with the highest salary. The join operation with the `Department` table adds a constant factor but does not change the overall time complexity.
> - **Space Complexity:** $O(n)$ for storing the maximum salaries per department and potentially the department names.
> - **Why these complexities occur:** The need to scan the `Employee` table to calculate maximum salaries and then again to identify the departments with the highest salary leads to the linear time complexity. The space complexity arises from storing the intermediate results.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of querying the database multiple times, we can use a single SQL query that combines the operations of finding the maximum salary per department and identifying the department(s) with the highest salary.
- Detailed breakdown of the approach:
  1. **Subquery to Find Maximum Salaries per Department:** Use a subquery to calculate the maximum salary for each department.
  2. **Find the Highest Salary:** Use the `MAX` function on the subquery results to find the highest salary across all departments.
  3. **Identify the Department(s):** Use a `WHERE` clause to filter the results to only include departments where the salary matches the highest salary.
  4. **Join with Department Table:** Join the filtered results with the `Department` table to return the department name(s).

```cpp
void findDepartmentHighestSalaryOptimal() {
    // Optimal SQL query
    string optimalQuery = 
        "SELECT D.name "
        "FROM Department D "
        "JOIN Employee E ON D.id = E.departmentId "
        "WHERE (E.departmentId, E.salary) IN ( "
        "    SELECT departmentId, MAX(salary) "
        "    FROM Employee "
        "    GROUP BY departmentId "
        ") "
        "AND E.salary = ( "
        "    SELECT MAX(salary) "
        "    FROM Employee "
        ")";
    
    // Execute the query and print the result
    // Assume we have a way to execute the query and print the department name(s)
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the `Employee` table. Although we use subqueries and joins, the database can optimize these operations, and the overall time complexity remains linear with respect to the size of the input data.
> - **Space Complexity:** $O(n)$, for storing the intermediate results of the subqueries and the final join operation.
> - **Optimality proof:** This approach is optimal because it minimizes the number of database queries required to solve the problem. By combining the necessary operations into a single query, we reduce the overhead of multiple queries and improve performance.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Subqueries, joins, and aggregation functions like `MAX`.
- Problem-solving patterns identified: Breaking down complex queries into simpler subqueries and using joins to combine data from multiple tables.
- Optimization techniques learned: Minimizing the number of database queries and using efficient query structures.
- Similar problems to practice: Other SQL problems involving subqueries, joins, and aggregation functions.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect use of subqueries, joins, or aggregation functions.
- Edge cases to watch for: Handling cases where multiple departments have the same highest salary or where a department has no employees.
- Performance pitfalls: Using inefficient query structures or executing too many separate queries.
- Testing considerations: Thoroughly testing the query with different input data to ensure correctness and performance.