## Article Views I

**Problem Link:** https://leetcode.com/problems/article-views-i/description

**Problem Statement:**
- Input format: A table `Views` with columns `id` and `article_id`, and another table `Downloads` with columns `id`, `article_id`, and `day`.
- Constraints: The `id` in both tables is a unique identifier.
- Expected output format: A table with `article_id` and the number of unique views for each article in the year 2019.
- Key requirements and edge cases to consider:
  - Only consider records from the year 2019.
  - Views and downloads should be counted as separate events.
  - The output should be sorted by `article_id`.
- Example test cases with explanations:
  - For a given set of views and downloads, the output should include the count of unique views for each article.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we need to count the number of unique views for each article in the year 2019. We can start by selecting all records from the `Views` and `Downloads` tables where the `day` is in the year 2019.
- Step-by-step breakdown of the solution:
  1. Select all records from the `Views` table where the `day` is in the year 2019.
  2. Select all records from the `Downloads` table where the `day` is in the year 2019.
  3. Combine the two sets of records.
  4. Group the combined records by `article_id`.
  5. For each group, count the number of unique views.
- Why this approach comes to mind first: This approach is straightforward and involves basic SQL operations such as selecting, combining, and grouping records.

```cpp
// SQL query to solve the problem
SELECT 
    article_id,
    COUNT(DISTINCT id) AS views
FROM 
    (
    SELECT 
        article_id, 
        id, 
        day
    FROM 
        Views
    WHERE 
        day LIKE '2019%'
    UNION ALL
    SELECT 
        article_id, 
        id, 
        day
    FROM 
        Downloads
    WHERE 
        day LIKE '2019%'
    ) AS combined_table
GROUP BY 
    article_id
ORDER BY 
    article_id;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of records in the `Views` table and $m$ is the number of records in the `Downloads` table. This is because we are selecting all records from both tables.
> - **Space Complexity:** $O(n + m)$, as we are storing all records in memory.
> - **Why these complexities occur:** These complexities occur because we are performing a simple selection and combination of records, which requires iterating over all records in both tables.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using a single SQL query that combines the `Views` and `Downloads` tables and counts the number of unique views for each article.
- Detailed breakdown of the approach:
  1. Use a `UNION ALL` operator to combine the `Views` and `Downloads` tables.
  2. Use a `WHERE` clause to filter out records that are not in the year 2019.
  3. Use a `GROUP BY` clause to group the combined records by `article_id`.
  4. Use a `COUNT(DISTINCT id)` function to count the number of unique views for each article.
- Proof of optimality: This approach is optimal because it only requires a single pass over the data and uses efficient SQL operations such as `UNION ALL` and `GROUP BY`.

```cpp
// SQL query to solve the problem
SELECT 
    article_id,
    COUNT(DISTINCT id) AS views
FROM 
    (
    SELECT 
        article_id, 
        id, 
        day
    FROM 
        Views
    WHERE 
        day LIKE '2019%'
    UNION ALL
    SELECT 
        article_id, 
        id, 
        day
    FROM 
        Downloads
    WHERE 
        day LIKE '2019%'
    ) AS combined_table
GROUP BY 
    article_id
ORDER BY 
    article_id;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of records in the `Views` table and $m$ is the number of records in the `Downloads` table.
> - **Space Complexity:** $O(n + m)$, as we are storing all records in memory.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the data and uses efficient SQL operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Efficient use of SQL operations such as `UNION ALL` and `GROUP BY`.
- Problem-solving patterns identified: Combining data from multiple tables and counting unique values.
- Optimization techniques learned: Using efficient SQL operations to reduce the number of passes over the data.
- Similar problems to practice: Other problems that involve combining data from multiple tables and counting unique values.

**Mistakes to Avoid:**
- Common implementation errors: Not filtering out records that are not in the year 2019.
- Edge cases to watch for: Records with missing or null values.
- Performance pitfalls: Using inefficient SQL operations that require multiple passes over the data.
- Testing considerations: Testing the query with different sets of data to ensure it produces the correct results.