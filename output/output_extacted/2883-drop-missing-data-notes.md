## Drop Missing Data
**Problem Link:** https://leetcode.com/problems/drop-missing-data/description

**Problem Statement:**
- Input format and constraints: The problem takes a table `t1` with columns `id` and `value` as input. The `id` is of type `int` and the `value` is of type `int`. The table `t1` can have any number of rows.
- Expected output format: The problem requires us to return a table with the same columns as `t1` but with all rows that have `NULL` values in the `value` column dropped.
- Key requirements and edge cases to consider: The problem requires us to write a SQL query to drop rows with `NULL` values in the `value` column.
- Example test cases with explanations: 
    - If the input table `t1` is:
        | id | value |
        |----|-------|
        | 1  | 10    |
        | 2  | NULL  |
        | 3  | 30    |
    - The output should be:
        | id | value |
        |----|-------|
        | 1  | 10    |
        | 3  | 30    |

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves selecting all rows from the table `t1` where the `value` is not `NULL`.
- Step-by-step breakdown of the solution: 
    1. Select all columns (`id` and `value`) from the table `t1`.
    2. Use a `WHERE` clause to filter out rows where `value` is `NULL`.
- Why this approach comes to mind first: This approach is straightforward and directly addresses the problem statement.

```cpp
// SQL query
SELECT id, value
FROM t1
WHERE value IS NOT NULL;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of rows in the table `t1`. This is because the query needs to scan all rows in the table.
> - **Space Complexity:** $O(n)$ where $n$ is the number of rows in the table `t1`. This is because the query needs to store all the rows that are not `NULL` in the result set.
> - **Why these complexities occur:** These complexities occur because the query needs to scan all rows in the table and store the result set.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is the same as the brute force approach because the problem requires us to scan all rows in the table and filter out the rows where `value` is `NULL`.
- Detailed breakdown of the approach: 
    1. Select all columns (`id` and `value`) from the table `t1`.
    2. Use a `WHERE` clause to filter out rows where `value` is `NULL`.
- Proof of optimality: This approach is optimal because it has a time complexity of $O(n)$ where $n$ is the number of rows in the table `t1`. This is the best possible time complexity because we need to scan all rows in the table.
- Why further optimization is impossible: Further optimization is impossible because we need to scan all rows in the table to filter out the rows where `value` is `NULL`.

```cpp
// SQL query
SELECT id, value
FROM t1
WHERE value IS NOT NULL;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of rows in the table `t1`. This is because the query needs to scan all rows in the table.
> - **Space Complexity:** $O(n)$ where $n$ is the number of rows in the table `t1`. This is because the query needs to store all the rows that are not `NULL` in the result set.
> - **Optimality proof:** This approach is optimal because it has a time complexity of $O(n)$ where $n$ is the number of rows in the table `t1`. This is the best possible time complexity because we need to scan all rows in the table.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of SQL queries to filter out rows from a table.
- Problem-solving patterns identified: The problem requires us to scan all rows in the table and filter out the rows where `value` is `NULL`.
- Optimization techniques learned: The problem requires us to optimize the SQL query to achieve the best possible time complexity.
- Similar problems to practice: Similar problems include filtering out rows from a table based on different conditions.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is to use `value != NULL` instead of `value IS NOT NULL` in the `WHERE` clause.
- Edge cases to watch for: An edge case to watch for is when the table `t1` is empty.
- Performance pitfalls: A performance pitfall is to use a subquery instead of a `WHERE` clause to filter out rows.
- Testing considerations: We should test the query with different inputs to ensure that it works correctly.