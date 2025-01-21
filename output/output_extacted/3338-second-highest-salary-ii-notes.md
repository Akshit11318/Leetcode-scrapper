## Second Highest Salary II

**Problem Link:** https://leetcode.com/problems/second-highest-salary-ii/description

**Problem Statement:**
- Input format and constraints: The problem requires writing a SQL query to find the second-highest salary from the Employee table. If there is no second-highest salary, the query should return `NULL`.
- Expected output format: A single column with a single row containing the second-highest salary or `NULL`.
- Key requirements and edge cases to consider: Handling cases where there are duplicate salaries, no salaries, or only one unique salary.
- Example test cases with explanations:
  - Example 1: 
    ```
    +----+--------+
    | Id | Salary |
    +----+--------+
    | 1  | 100    |
    | 2  | 200    |
    | 3  | 300    |
    +----+--------+
    ```
    Output: `200`
  - Example 2: 
    ```
    +----+--------+
    | Id | Salary |
    +----+--------+
    | 1  | 100    |
    +----+--------+
    ```
    Output: `NULL`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach is to select all unique salaries from the Employee table, order them in descending order, and then select the second row. If there is no second row, return `NULL`.
- Step-by-step breakdown of the solution:
  1. Select distinct salaries from the Employee table.
  2. Order the salaries in descending order.
  3. Select the second salary.
- Why this approach comes to mind first: It's straightforward and aligns with how one might manually solve the problem.

```sql
SELECT
    (SELECT DISTINCT Salary
     FROM Employee
     ORDER BY Salary DESC
     LIMIT 1 OFFSET 1) AS SecondHighestSalary;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation, where $n$ is the number of rows in the Employee table.
> - **Space Complexity:** $O(n)$ for storing the sorted salaries.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, and storing the sorted salaries affects the space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of sorting all salaries, we can use a subquery to find the maximum salary and then select the maximum salary that is less than the maximum salary found. This approach avoids sorting and is more efficient.
- Detailed breakdown of the approach:
  1. Find the maximum salary.
  2. Select the maximum salary that is less than the maximum salary.
- Proof of optimality: This approach has a lower time complexity than the brute force approach because it avoids sorting.
- Why further optimization is impossible: This approach already minimizes the number of operations needed to find the second-highest salary.

```sql
SELECT
    (SELECT MAX(Salary)
     FROM Employee
     WHERE Salary < (SELECT MAX(Salary) FROM Employee)) AS SecondHighestSalary;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the Employee table, because we are scanning the table twice: once to find the maximum salary and once to find the second-highest salary.
> - **Space Complexity:** $O(1)$ because we are only storing a constant amount of information.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations needed to find the second-highest salary.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Subqueries and efficient use of SQL operations.
- Problem-solving patterns identified: Avoiding unnecessary sorting and using subqueries to simplify complex queries.
- Optimization techniques learned: Minimizing the number of operations and avoiding sorting when possible.
- Similar problems to practice: Finding the nth-highest salary, finding the highest salary in a specific department, etc.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle `NULL` values, not considering duplicate salaries, and using inefficient sorting operations.
- Edge cases to watch for: Handling cases where there are no rows, one row, or duplicate rows in the Employee table.
- Performance pitfalls: Using sorting operations when not necessary and not optimizing subqueries.
- Testing considerations: Testing with different input sizes, duplicate salaries, and edge cases to ensure the query is correct and efficient.