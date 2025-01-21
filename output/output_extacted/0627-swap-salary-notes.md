## Swap Salary
**Problem Link:** https://leetcode.com/problems/swap-salary/description

**Problem Statement:**
- Input format and constraints: The problem requires writing a SQL query to update the `salary` column in the `salary` table based on the `sex` column. The table has two columns: `id` and `sex`, and the query should swap the `sex` column values.
- Expected output format: The query should return the updated table with swapped `sex` values.
- Key requirements and edge cases to consider: The query should update the `sex` column without creating a new table or using a temporary table.
- Example test cases with explanations:
  - If the input table is:
    | id | sex |
    |----|-----|
    | 1  | m   |
    | 2  | f   |
  - The expected output should be:
    | id | sex |
    |----|-----|
    | 1  | f   |
    | 2  | m   |

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One might think of using a temporary table or a subquery to achieve this, but these approaches are not necessary.
- Step-by-step breakdown of the solution: The query can be achieved using a simple `UPDATE` statement with a `CASE` expression to swap the `sex` values.
- Why this approach comes to mind first: It is a straightforward solution that uses basic SQL syntax.

```sql
UPDATE salary
SET sex = 
    CASE 
        WHEN sex = 'm' THEN 'f'
        ELSE 'm'
    END;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the table, because the query updates each row once.
> - **Space Complexity:** $O(1)$, because the query does not use any additional space that scales with the input size.
> - **Why these complexities occur:** The time complexity is linear because the query updates each row, and the space complexity is constant because no additional data structures are used.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is the same as the brute force approach because it is already efficient and does not use any unnecessary operations.
- Detailed breakdown of the approach: The `UPDATE` statement with a `CASE` expression is the most efficient way to swap the `sex` values in the table.
- Proof of optimality: This solution is optimal because it only requires a single pass through the table and does not use any additional space that scales with the input size.
- Why further optimization is impossible: Further optimization is impossible because the query must update each row, and this solution already achieves that in the most efficient way possible.

```sql
UPDATE salary
SET sex = 
    CASE 
        WHEN sex = 'm' THEN 'f'
        ELSE 'm'
    END;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the table, because the query updates each row once.
> - **Space Complexity:** $O(1)$, because the query does not use any additional space that scales with the input size.
> - **Optimality proof:** This solution is optimal because it only requires a single pass through the table and does not use any additional space that scales with the input size.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of `CASE` expressions in SQL queries.
- Problem-solving patterns identified: The problem requires identifying the most efficient way to update a table based on a condition.
- Optimization techniques learned: The problem teaches the importance of minimizing the number of passes through the table and avoiding unnecessary operations.
- Similar problems to practice: Other problems that involve updating tables based on conditions, such as updating a column based on a join or a subquery.

**Mistakes to Avoid:**
- Common implementation errors: Using a temporary table or a subquery when a simple `UPDATE` statement is sufficient.
- Edge cases to watch for: Handling `NULL` values in the `sex` column.
- Performance pitfalls: Using inefficient queries that require multiple passes through the table.
- Testing considerations: Testing the query with different input data to ensure it works correctly in all cases.