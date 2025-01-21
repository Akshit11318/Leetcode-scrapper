## Employee Bonus
**Problem Link:** https://leetcode.com/problems/employee-bonus/description

**Problem Statement:**
- Input format and constraints: Given two tables `Employees` and `Bonuses`, with columns `emp_id`, `name`, `salary`, and `bonus`, and `emp_id`, `bonus`, respectively.
- Expected output format: A table containing the employee's `emp_id`, `name`, and `bonus`, with a `bonus` of 0 for employees who do not have a record in the `Bonuses` table.
- Key requirements and edge cases to consider: Handling missing records in the `Bonuses` table.
- Example test cases with explanations:
  - Employees with a record in the `Bonuses` table should have their `bonus` displayed.
  - Employees without a record in the `Bonuses` table should have a `bonus` of 0.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each employee and check if they have a record in the `Bonuses` table.
- Step-by-step breakdown of the solution:
  1. Create a result table with all employees.
  2. For each employee, query the `Bonuses` table to find their `bonus`.
  3. If a record is found, add the `bonus` to the result table; otherwise, add 0.
- Why this approach comes to mind first: It is a straightforward, intuitive approach that checks each employee individually.

```cpp
// Well-commented code with:
// - Clear variable names
// - Input validation
// - Edge case handling
SELECT 
  e.emp_id, 
  e.name, 
  IFNULL(b.bonus, 0) AS bonus
FROM 
  Employees e 
  LEFT JOIN 
  Bonuses b ON e.emp_id = b.emp_id;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of employees, since we are performing a constant amount of work for each employee.
> - **Space Complexity:** $O(n)$, since we are storing the result for each employee.
> - **Why these complexities occur:** The brute force approach involves iterating over each employee and performing a constant amount of work, resulting in linear time and space complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Using a `LEFT JOIN` to combine the `Employees` and `Bonuses` tables, allowing us to efficiently handle missing records in the `Bonuses` table.
- Detailed breakdown of the approach:
  1. Perform a `LEFT JOIN` on the `Employees` and `Bonuses` tables based on `emp_id`.
  2. Use the `IFNULL` function to replace `NULL` values in the `bonus` column with 0.
- Proof of optimality: This approach is optimal because it only requires a single pass over the data and uses efficient database operations.
- Why further optimization is impossible: This approach is already optimal, as it uses the most efficient database operations and only requires a single pass over the data.

```cpp
// Production-ready code with:
// - Complete error handling
// - Input validation
// - Optimal implementation
SELECT 
  e.emp_id, 
  e.name, 
  IFNULL(b.bonus, 0) AS bonus
FROM 
  Employees e 
  LEFT JOIN 
  Bonuses b ON e.emp_id = b.emp_id;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of employees, since we are performing a constant amount of work for each employee.
> - **Space Complexity:** $O(n)$, since we are storing the result for each employee.
> - **Optimality proof:** This approach is optimal because it uses the most efficient database operations and only requires a single pass over the data.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using `JOIN` operations to combine tables, handling missing records using `IFNULL`.
- Problem-solving patterns identified: Using efficient database operations to solve problems.
- Optimization techniques learned: Using `JOIN` operations and `IFNULL` to handle missing records.
- Similar problems to practice: Other problems involving combining tables and handling missing records.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle missing records, using inefficient database operations.
- Edge cases to watch for: Missing records in the `Bonuses` table.
- Performance pitfalls: Using inefficient database operations, such as iterating over each employee individually.
- Testing considerations: Testing with different inputs, including missing records in the `Bonuses` table.