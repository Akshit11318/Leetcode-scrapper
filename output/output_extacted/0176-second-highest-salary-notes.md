## Second Highest Salary
**Problem Link:** https://leetcode.com/problems/second-highest-salary/description

**Problem Statement:**
- Input format and constraints: The problem requires writing a SQL query to find the second-highest salary from the `Employee` table.
- Expected output format: The query should return the second-highest salary. If there is no second-highest salary, it should return `NULL`.
- Key requirements and edge cases to consider:
  - Handling the case where there is only one employee.
  - Handling the case where all employees have the same salary.
- Example test cases with explanations:
  - Test case 1: If the `Employee` table has more than two distinct salaries, the query should return the second-highest salary.
  - Test case 2: If the `Employee` table has only one distinct salary, the query should return `NULL`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The initial approach is to select all distinct salaries from the `Employee` table, order them in descending order, and then limit the result to the second row.
- Step-by-step breakdown of the solution:
  1. Select distinct salaries from the `Employee` table.
  2. Order the salaries in descending order.
  3. Limit the result to the second row.
- Why this approach comes to mind first: This approach is straightforward and directly addresses the problem statement.

```cpp
// Note: Since this is a SQL problem, we will write SQL queries instead of C++ code.
SELECT DISTINCT Salary AS SecondHighestSalary
FROM Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 1;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the `ORDER BY` operation, where $n$ is the number of distinct salaries.
> - **Space Complexity:** $O(n)$ for storing the distinct salaries.
> - **Why these complexities occur:** The `ORDER BY` operation requires sorting the salaries, which has a time complexity of $O(n \log n)$. The `DISTINCT` keyword requires storing unique salaries, which has a space complexity of $O(n)$.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of using `LIMIT` and `OFFSET`, we can use a subquery to select the maximum salary and then select the maximum salary that is less than the maximum salary.
- Detailed breakdown of the approach:
  1. Select the maximum salary from the `Employee` table.
  2. Select the maximum salary that is less than the maximum salary.
- Proof of optimality: This approach is optimal because it only requires two passes over the data: one to find the maximum salary and one to find the second-highest salary.
- Why further optimization is impossible: This approach has a time complexity of $O(n)$, which is the best possible time complexity for this problem.

```sql
SELECT MAX(Salary) AS SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT MAX(Salary) FROM Employee);
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the `Employee` table.
> - **Space Complexity:** $O(1)$, since we are not storing any additional data.
> - **Optimality proof:** This approach is optimal because it only requires two passes over the data, and each pass has a time complexity of $O(n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Subqueries, `MAX` aggregation function, and `WHERE` clause.
- Problem-solving patterns identified: Using subqueries to solve problems that require finding the maximum or minimum value that satisfies a condition.
- Optimization techniques learned: Avoiding unnecessary sorting and using subqueries to reduce the number of passes over the data.
- Similar problems to practice: Finding the third-highest salary, finding the highest salary for each department, etc.

**Mistakes to Avoid:**
- Common implementation errors: Using `LIMIT` and `OFFSET` instead of subqueries, not handling the case where there is no second-highest salary.
- Edge cases to watch for: Handling the case where there is only one employee, handling the case where all employees have the same salary.
- Performance pitfalls: Using unnecessary sorting or joins, not using indexes.
- Testing considerations: Testing the query with different datasets, testing the query with edge cases.