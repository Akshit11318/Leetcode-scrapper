## Employees With Deductions
**Problem Link:** https://leetcode.com/problems/employees-with-deductions/description

**Problem Statement:**
- Input format and constraints: The problem involves a table `Deductions` with columns `employee_id` and `deduction`. The goal is to find the total deductions for each employee and determine which employees have deductions greater than or equal to the average of all deductions.
- Expected output format: The output should be a table with `employee_id` and `total_deductions` columns, where `total_deductions` is the sum of all deductions for each employee.
- Key requirements and edge cases to consider: Handle cases where an employee has no deductions, and ensure the calculation of average deductions is correct even if there are no deductions.
- Example test cases with explanations:
  - Test case 1: An employee with multiple deductions should have the total deductions calculated correctly.
  - Test case 2: An employee with no deductions should not be included in the output.
  - Test case 3: If all employees have no deductions, the output should be empty.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Start by calculating the total deductions for each employee by summing up all deductions in the `Deductions` table. Then, calculate the average of all deductions by summing up all deductions and dividing by the total number of deductions. Finally, compare each employee's total deductions to the average and include them in the output if their total deductions are greater than or equal to the average.
- Step-by-step breakdown of the solution:
  1. Calculate the total deductions for each employee.
  2. Calculate the average of all deductions.
  3. Compare each employee's total deductions to the average and include them in the output if necessary.
- Why this approach comes to mind first: It directly addresses the problem statement by following the steps outlined in the requirements.

```cpp
SELECT 
    employee_id, 
    SUM(deduction) AS total_deductions
FROM 
    Deductions
GROUP BY 
    employee_id
HAVING 
    SUM(deduction) >= (SELECT AVG(deduction) FROM Deductions);
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the grouping and sorting required for the `HAVING` clause, where $n$ is the number of rows in the `Deductions` table.
> - **Space Complexity:** $O(n)$ for storing the intermediate results of the grouping operation.
> - **Why these complexities occur:** The grouping operation requires sorting, which has a time complexity of $O(n \log n)$. The space complexity is due to the need to store the intermediate results of the grouping operation.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Use a single SQL query with a subquery to calculate the average deduction, and then use this average in the `HAVING` clause to filter the results.
- Detailed breakdown of the approach:
  1. Calculate the average deduction using a subquery.
  2. Use the subquery result in the `HAVING` clause to filter the employees based on their total deductions.
- Proof of optimality: This approach is optimal because it only requires a single pass through the data to calculate the total deductions and the average deduction.
- Why further optimization is impossible: This approach already minimizes the number of database operations required to solve the problem.

```cpp
SELECT 
    employee_id, 
    SUM(deduction) AS total_deductions
FROM 
    Deductions
GROUP BY 
    employee_id
HAVING 
    SUM(deduction) >= (SELECT AVG(deduction) FROM Deductions);
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the grouping and sorting required for the `HAVING` clause, where $n$ is the number of rows in the `Deductions` table.
> - **Space Complexity:** $O(n)$ for storing the intermediate results of the grouping operation.
> - **Optimality proof:** The time complexity is optimal because it only requires a single pass through the data. The space complexity is also optimal because it only requires storing the intermediate results of the grouping operation.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Grouping, aggregation, and filtering.
- Problem-solving patterns identified: Using subqueries to calculate aggregate values and then using these values in the main query.
- Optimization techniques learned: Minimizing the number of database operations required to solve the problem.
- Similar problems to practice: Problems involving grouping, aggregation, and filtering, such as calculating the average salary for each department in a company.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to include the `GROUP BY` clause when using aggregation functions.
- Edge cases to watch for: Handling cases where an employee has no deductions.
- Performance pitfalls: Using subqueries that are not optimized, leading to poor performance.
- Testing considerations: Testing the query with different input data to ensure it produces the correct results.