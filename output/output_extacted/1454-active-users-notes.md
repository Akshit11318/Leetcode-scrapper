## Active Users
**Problem Link:** https://leetcode.com/problems/active-users/description

**Problem Statement:**
- Input format and constraints: We are given two tables, `Accounts` and `Logs`. The `Accounts` table contains information about each user, with columns `id` and `name`. The `Logs` table contains log records, with columns `id`, `account_id`, and `time`. The task is to find the number of active users for each day.
- Expected output format: The output should be a table with two columns: `day` and `active_users`.
- Key requirements and edge cases to consider: 
    - Active users are those who have logged in at least once on a given day.
    - The `time` column in the `Logs` table is in the format 'YYYY-MM-DD HH:MM:SS'.
    - We need to consider all days from the earliest log time to the latest log time.
- Example test cases with explanations: For example, if we have log records for the same user on '2020-01-01' and '2020-01-02', this user should be counted as an active user for both days.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first step is to extract the date from each log record and then count the number of unique users for each day.
- Step-by-step breakdown of the solution: 
    1. Extract the date from each log record.
    2. For each date, count the number of unique users who have logged in on that day.
    3. Store the count of active users for each day in a result table.
- Why this approach comes to mind first: This approach is straightforward and easy to understand. It involves iterating over each log record, extracting the date, and then counting the number of unique users for each day.

```cpp
SELECT 
    DATE(time) AS day,
    COUNT(DISTINCT account_id) AS active_users
FROM 
    Logs
GROUP BY 
    DATE(time)
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of log records. This is because we need to iterate over each log record once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of log records. This is because in the worst-case scenario, we might need to store all log records in memory.
> - **Why these complexities occur:** These complexities occur because we need to iterate over each log record and store the count of active users for each day.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is to use a SQL query with the `DATE` function to extract the date from each log record, and then use the `GROUP BY` clause to group the log records by date.
- Detailed breakdown of the approach: 
    1. Use the `DATE` function to extract the date from each log record.
    2. Use the `GROUP BY` clause to group the log records by date.
    3. Use the `COUNT(DISTINCT account_id)` function to count the number of unique users for each day.
- Proof of optimality: This solution is optimal because it uses the minimum number of operations required to solve the problem. It only requires a single pass over the log records, and it uses the `GROUP BY` clause to group the log records by date, which is the most efficient way to do so.
- Why further optimization is impossible: Further optimization is impossible because we need to iterate over each log record at least once to extract the date and count the number of unique users.

```cpp
SELECT 
    DATE(time) AS day,
    COUNT(DISTINCT account_id) AS active_users
FROM 
    Logs
GROUP BY 
    DATE(time)
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of log records. This is because we need to iterate over each log record once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of log records. This is because in the worst-case scenario, we might need to store all log records in memory.
> - **Optimality proof:** This solution is optimal because it uses the minimum number of operations required to solve the problem. It only requires a single pass over the log records, and it uses the `GROUP BY` clause to group the log records by date, which is the most efficient way to do so.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The key algorithmic concept demonstrated in this solution is the use of the `GROUP BY` clause to group log records by date.
- Problem-solving patterns identified: The problem-solving pattern identified in this solution is the use of the `DATE` function to extract the date from each log record, and then using the `GROUP BY` clause to group the log records by date.
- Optimization techniques learned: The optimization technique learned in this solution is the use of the `COUNT(DISTINCT account_id)` function to count the number of unique users for each day.
- Similar problems to practice: Similar problems to practice include finding the number of active users for each month, or finding the number of active users for each year.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is to forget to use the `DISTINCT` keyword when counting the number of unique users.
- Edge cases to watch for: An edge case to watch for is when there are no log records for a particular day. In this case, the day should not be included in the result table.
- Performance pitfalls: A performance pitfall is to use a subquery to extract the date from each log record, instead of using the `DATE` function.
- Testing considerations: A testing consideration is to test the solution with a large number of log records, to ensure that it performs well and does not run out of memory.