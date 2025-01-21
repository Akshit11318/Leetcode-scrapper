## Friendly Movies Streamed Last Month
**Problem Link:** https://leetcode.com/problems/friendly-movies-streamed-last-month/description

**Problem Statement:**
- Input format and constraints: The problem involves selecting movies from a database based on certain criteria such as `creation_year` and `category`.
- Expected output format: The output should be a list of movie titles that meet the specified conditions, ordered by `creation_year` in descending order and then by `title` in ascending order.
- Key requirements and edge cases to consider: The solution must handle potential `NULL` values in the database and ensure that the output is correctly sorted.
- Example test cases with explanations: Test cases should cover various scenarios, including different `creation_year` values and `category` types.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over all rows in the `tv_programs` table, checking each row against the specified conditions, and then sorting the results.
- Step-by-step breakdown of the solution:
  1. Iterate over each row in the `tv_programs` table.
  2. Check if the `creation_year` is within the last month and if the `category` is 'Movies'.
  3. If the conditions are met, add the `title` to the result list.
  4. Sort the result list by `creation_year` in descending order and then by `title` in ascending order.
- Why this approach comes to mind first: This approach is straightforward and directly addresses the problem statement.

```cpp
SELECT title 
FROM tv_programs 
WHERE creation_year = 2023 
AND category = 'Movies' 
ORDER BY creation_year DESC, title ASC;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation, where $n$ is the number of rows in the `tv_programs` table.
> - **Space Complexity:** $O(n)$ for storing the result list.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, and the space complexity is due to storing the result list.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using SQL queries to directly filter and sort the data, leveraging the database's indexing and query optimization capabilities.
- Detailed breakdown of the approach:
  1. Use a SQL query with a `WHERE` clause to filter rows based on the `creation_year` and `category` conditions.
  2. Use an `ORDER BY` clause to sort the results by `creation_year` in descending order and then by `title` in ascending order.
- Proof of optimality: This approach is optimal because it minimizes the number of operations required to produce the desired output, leveraging the database's native query processing capabilities.

```cpp
SELECT title 
FROM tv_programs 
WHERE creation_year = 2023 
AND category = 'Movies' 
ORDER BY creation_year DESC, title ASC;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation, where $n$ is the number of rows in the `tv_programs` table that match the filter conditions.
> - **Space Complexity:** $O(n)$ for storing the result list.
> - **Optimality proof:** This approach is optimal because it directly filters and sorts the data using the database's query processing capabilities, minimizing the number of operations required.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The importance of leveraging database query processing capabilities to optimize data filtering and sorting operations.
- Problem-solving patterns identified: Using SQL queries to directly filter and sort data can be more efficient than iterating over all rows in a table.
- Optimization techniques learned: Minimizing the number of operations required to produce the desired output by leveraging database indexing and query optimization capabilities.
- Similar problems to practice: Other SQL query optimization problems, such as optimizing queries with joins or subqueries.

**Mistakes to Avoid:**
- Common implementation errors: Failing to properly handle `NULL` values in the database or not using indexing to optimize query performance.
- Edge cases to watch for: Ensuring that the solution correctly handles cases where the `creation_year` or `category` values are missing or invalid.
- Performance pitfalls: Failing to optimize queries can lead to poor performance, especially for large datasets.
- Testing considerations: Thoroughly testing the solution with various input scenarios to ensure correctness and performance.