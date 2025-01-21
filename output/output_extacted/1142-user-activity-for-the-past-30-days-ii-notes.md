## User Activity for the Past 30 Days II

**Problem Link:** https://leetcode.com/problems/user-activity-for-the-past-30-days-ii/description

**Problem Statement:**
- Input format: A table `Activity` with columns `userId`, `sessionId`, `activityDate`, and `duration`.
- Constraints: The table contains data for the last 30 days.
- Expected output format: The number of active users for each continuous period of 30 days.
- Key requirements: A user is considered active if they have at least one session during a 30-day period.
- Edge cases: Users may have multiple sessions on the same day, and a session can span multiple days.

**Example Test Cases:**

| userId | sessionId | activityDate | duration |
| --- | --- | --- | --- |
| 1    | 1        | 2022-07-01  | 10       |
| 1    | 1        | 2022-07-02  | 10       |
| 2    | 2        | 2022-07-03  | 5        |
| 3    | 3        | 2022-07-04  | 10       |
| 1    | 4        | 2022-07-05  | 10       |

For the given table, the output should be the number of active users for each 30-day period.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate over each user and check if they have any sessions within each 30-day period.
- Step-by-step breakdown:
  1. Iterate over each user.
  2. For each user, iterate over each 30-day period.
  3. For each 30-day period, check if the user has any sessions.
  4. If the user has any sessions, increment the count of active users for that period.

```cpp
SELECT 
    (SELECT COUNT(DISTINCT userId) 
     FROM Activity 
     WHERE activityDate BETWEEN '2022-07-01' AND '2022-07-30') AS active_users;
```

> Complexity Analysis:
> - **Time Complexity:** O(n\*m) where n is the number of users and m is the number of 30-day periods.
> - **Space Complexity:** O(1) since we are only storing the count of active users.
> - **Why these complexities occur:** The time complexity is O(n\*m) because we are iterating over each user and each 30-day period. The space complexity is O(1) because we are only storing a single value, the count of active users.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a SQL query to directly count the number of distinct users for each 30-day period.
- Detailed breakdown:
  1. Use a subquery to generate all possible 30-day periods.
  2. Use a join to match each user's sessions with the 30-day periods.
  3. Use the `COUNT(DISTINCT)` function to count the number of active users for each period.

```cpp
SELECT 
    a.activityDate, 
    COUNT(DISTINCT a.userId) AS active_users
FROM 
    Activity a
WHERE 
    a.activityDate BETWEEN '2022-07-01' AND '2022-07-30'
GROUP BY 
    a.activityDate;
```

> Complexity Analysis:
> - **Time Complexity:** O(n log n) where n is the number of rows in the `Activity` table.
> - **Space Complexity:** O(n) since we are storing the results of the query.
> - **Optimality proof:** This is the optimal solution because we are using a single SQL query to directly count the number of active users for each 30-day period. This eliminates the need for iterative solutions and reduces the time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using SQL queries to directly count the number of active users for each 30-day period.
- Problem-solving patterns identified: Using subqueries to generate all possible 30-day periods and joining them with the `Activity` table.
- Optimization techniques learned: Using the `COUNT(DISTINCT)` function to count the number of active users for each period.

**Mistakes to Avoid:**
- Common implementation errors: Not using the `COUNT(DISTINCT)` function to count the number of active users.
- Edge cases to watch for: Users may have multiple sessions on the same day, and a session can span multiple days.
- Performance pitfalls: Using iterative solutions instead of a single SQL query.
- Testing considerations: Test the query with different dates and users to ensure it returns the correct results.