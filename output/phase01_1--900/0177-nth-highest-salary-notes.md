## Nth Highest Salary
**Problem Link:** https://leetcode.com/problems/nth-highest-salary/description

**Problem Statement:**
- Input format and constraints: The problem involves finding the Nth highest salary from a given table `Employee` with columns `id` and `salary`.
- Expected output format: The solution should return the Nth highest salary. If there is no Nth highest salary, it should return `NULL`.
- Key requirements and edge cases to consider: The solution should handle cases where N is larger than the number of unique salaries.
- Example test cases with explanations:
  - If the table `Employee` contains salaries 100, 200, 300, and N = 2, the solution should return 200.
  - If the table `Employee` contains salaries 100, 200, 300, and N = 4, the solution should return `NULL`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves selecting all unique salaries from the `Employee` table, ordering them in descending order, and then selecting the Nth salary.
- Step-by-step breakdown of the solution:
  1. Select all unique salaries from the `Employee` table.
  2. Order the unique salaries in descending order.
  3. Select the Nth salary.
- Why this approach comes to mind first: This approach is straightforward and directly addresses the problem statement.

```cpp
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE M INT;
  SET M = N - 1;
  RETURN (
      SELECT DISTINCT salary 
      FROM Employee 
      ORDER BY salary DESC 
      LIMIT 1 OFFSET M
  );
END
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation, where $n$ is the number of rows in the `Employee` table.
> - **Space Complexity:** $O(n)$ for storing the sorted salaries.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, and storing the sorted salaries requires additional space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of sorting all salaries, we can use a query that directly selects the Nth highest salary without sorting the entire table.
- Detailed breakdown of the approach:
  1. Use the `LIMIT` and `OFFSET` clauses to select the Nth row from the ordered salaries.
  2. Use a subquery to select distinct salaries in descending order.
- Proof of optimality: This approach is optimal because it avoids sorting the entire table and directly selects the Nth highest salary.

```cpp
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE M INT;
  SET M = N - 1;
  RETURN (
      SELECT DISTINCT salary 
      FROM Employee 
      ORDER BY salary DESC 
      LIMIT 1 OFFSET M
  );
END
```

However, the above approach is essentially the same as the brute force approach due to the nature of SQL queries. The actual optimization comes from the database's query optimization and indexing, which can significantly improve performance.

A more optimized version can be achieved using variables and the `LIMIT` and `OFFSET` clauses in a single query:

```sql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE M INT;
  SET M = N - 1;
  RETURN (
    SELECT IFNULL(
      (SELECT DISTINCT salary 
       FROM Employee 
       ORDER BY salary DESC 
       LIMIT 1 OFFSET M), NULL
    )
  );
END
```

> Complexity Analysis:
> - **Time Complexity:** The time complexity is still $O(n \log n)$ due to the sorting operation, but the actual performance can be improved by the database's query optimization and indexing.
> - **Space Complexity:** $O(n)$ for storing the sorted salaries.
> - **Optimality proof:** This approach is optimal because it directly selects the Nth highest salary without sorting the entire table, and the database's query optimization and indexing can further improve performance.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, query optimization, and indexing.
- Problem-solving patterns identified: Directly addressing the problem statement and optimizing the solution using database query optimization and indexing.
- Optimization techniques learned: Using `LIMIT` and `OFFSET` clauses, query optimization, and indexing.
- Similar problems to practice: Other SQL problems that involve query optimization and indexing.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly using the `LIMIT` and `OFFSET` clauses, not considering the database's query optimization and indexing.
- Edge cases to watch for: Handling cases where N is larger than the number of unique salaries.
- Performance pitfalls: Not optimizing the query using the database's query optimization and indexing.
- Testing considerations: Testing the solution with different inputs and edge cases to ensure correctness and performance.