## Reported Posts II
**Problem Link:** https://leetcode.com/problems/reported-posts-ii/description

**Problem Statement:**
- Input format and constraints: The input is a list of user reports where each report is in the form of `[user_id, report_id]`. The task is to write a SQL query to find the number of active users and the number of reports that are not blocked after a certain date.
- Expected output format: The output should be in the form of two columns, one for the number of active users and the other for the number of reports that are not blocked.
- Key requirements and edge cases to consider: The query should consider only reports that are not blocked and users who have not been blocked.
- Example test cases with explanations: The query should return the correct number of active users and reports that are not blocked based on the given data.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The first step is to identify the reports that are not blocked and the users who are active.
- Step-by-step breakdown of the solution: 
    1. Filter the reports to only include those that are not blocked.
    2. Count the number of distinct users in the filtered reports.
    3. Count the total number of reports that are not blocked.
- Why this approach comes to mind first: This approach is straightforward and involves simple filtering and counting operations.

```sql
SELECT 
    COUNT(DISTINCT user_id) AS active_users,
    COUNT(report_id) AS not_blocked_reports
FROM 
    Actions
WHERE 
    action_date > '2019-06-30'
    AND action = 'report'
    AND user_id NOT IN (
        SELECT 
            user_id
        FROM 
            Actions
        WHERE 
            action_date > '2019-06-30'
            AND action = 'block'
    )
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ due to the subquery in the `WHERE` clause.
> - **Space Complexity:** $O(n)$ for storing the results of the subquery.
> - **Why these complexities occur:** The subquery in the `WHERE` clause has to iterate over the entire table for each row, resulting in a quadratic time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a `JOIN` operation to combine the reports and blocked users tables.
- Detailed breakdown of the approach: 
    1. Create a derived table that contains the user IDs of blocked users.
    2. Join the reports table with the derived table on the `user_id` column.
    3. Filter the joined table to only include reports that are not blocked.
    4. Count the number of distinct users and reports in the filtered table.
- Proof of optimality: This approach has a linear time complexity because it only involves a single pass over the data.
- Why further optimization is impossible: This approach is already optimized because it only involves a single pass over the data.

```sql
SELECT 
    COUNT(DISTINCT a1.user_id) AS active_users,
    COUNT(a1.report_id) AS not_blocked_reports
FROM 
    Actions a1
WHERE 
    a1.action_date > '2019-06-30'
    AND a1.action = 'report'
    AND a1.user_id NOT IN (
        SELECT 
            a2.user_id
        FROM 
            Actions a2
        WHERE 
            a2.action_date > '2019-06-30'
            AND a2.action = 'block'
    )
```

However, the above query still has a time complexity of $O(n^2)$. To optimize it further, we can use a `LEFT JOIN` instead of a subquery.

```sql
SELECT 
    COUNT(DISTINCT a1.user_id) AS active_users,
    COUNT(a1.report_id) AS not_blocked_reports
FROM 
    Actions a1
LEFT JOIN 
    Actions a2 ON a1.user_id = a2.user_id AND a2.action = 'block' AND a2.action_date > '2019-06-30'
WHERE 
    a1.action_date > '2019-06-30'
    AND a1.action = 'report'
    AND a2.user_id IS NULL
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ due to the `JOIN` operation.
> - **Space Complexity:** $O(n)$ for storing the results of the `JOIN` operation.
> - **Optimality proof:** This approach is optimal because it only involves a single pass over the data.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The importance of using `JOIN` operations instead of subqueries to improve performance.
- Problem-solving patterns identified: Using derived tables and `JOIN` operations to simplify complex queries.
- Optimization techniques learned: Avoiding subqueries and using `JOIN` operations instead.
- Similar problems to practice: Other problems that involve combining multiple tables and filtering data.

**Mistakes to Avoid:**
- Common implementation errors: Using subqueries instead of `JOIN` operations.
- Edge cases to watch for: Handling cases where the data is missing or null.
- Performance pitfalls: Using subqueries or other operations that have a high time complexity.
- Testing considerations: Testing the query with different datasets and edge cases to ensure it works correctly.