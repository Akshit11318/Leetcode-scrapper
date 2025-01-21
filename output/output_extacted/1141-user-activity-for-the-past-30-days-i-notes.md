## User Activity for the Past 30 Days I

**Problem Link:** https://leetcode.com/problems/user-activity-for-the-past-30-days-i/description

**Problem Statement:**
- Input format: A table `Activity` with columns `username`, `activity`, and `time`.
- Constraints: The time is in seconds, and we need to find the number of active users for the past 30 days.
- Expected output format: A single number representing the count of active users.
- Key requirements and edge cases to consider: 
    - Active users are those who have logged in within the past 30 days.
    - If a user has multiple logins within the past 30 days, they should only be counted once.
- Example test cases with explanations:
    - If a user logged in 31 days ago, they should not be counted.
    - If a user logged in yesterday and today, they should only be counted once.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we need to iterate over each user and check if they have logged in within the past 30 days.
- Step-by-step breakdown of the solution:
    1. Create a set to store unique usernames.
    2. Iterate over each row in the `Activity` table.
    3. For each row, calculate the difference between the current time and the `time` column.
    4. If the difference is less than or equal to 30 days (in seconds), add the `username` to the set.
    5. Finally, return the size of the set, which represents the number of active users.
- Why this approach comes to mind first: It is the most straightforward way to solve the problem, as it involves checking each user's login time.

```cpp
SELECT COUNT(DISTINCT username) 
FROM Activity 
WHERE time > (NOW() - INTERVAL 30 DAY);
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the `Activity` table, because we are iterating over each row once.
> - **Space Complexity:** $O(n)$, because in the worst-case scenario, we might need to store all usernames in the set.
> - **Why these complexities occur:** These complexities occur because we are using a set to store unique usernames and iterating over each row in the table.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using a single SQL query with a `DISTINCT` keyword and a `WHERE` clause to filter out users who have not logged in within the past 30 days.
- Detailed breakdown of the approach:
    1. Use the `COUNT(DISTINCT username)` function to count the number of unique usernames.
    2. Use the `WHERE` clause to filter out rows where the `time` column is older than 30 days.
- Proof of optimality: This approach is optimal because it only requires a single pass over the data and uses the database's built-in indexing and optimization capabilities.
- Why further optimization is impossible: This approach is already optimal because it uses the most efficient database operations and does not require any additional processing.

```cpp
SELECT COUNT(DISTINCT username) 
FROM Activity 
WHERE time > (NOW() - INTERVAL 30 DAY);
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the `Activity` table, because we are iterating over each row once.
> - **Space Complexity:** $O(n)$, because in the worst-case scenario, we might need to store all usernames in the set.
> - **Optimality proof:** This approach is optimal because it uses the database's built-in indexing and optimization capabilities, and only requires a single pass over the data.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using `DISTINCT` keyword to count unique values, and using `WHERE` clause to filter out unwanted data.
- Problem-solving patterns identified: Using SQL queries to solve problems that involve data analysis and filtering.
- Optimization techniques learned: Using database's built-in indexing and optimization capabilities to improve query performance.
- Similar problems to practice: Other problems that involve data analysis and filtering, such as finding the number of unique users who have logged in within a certain time period.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to use `DISTINCT` keyword, or using incorrect `WHERE` clause.
- Edge cases to watch for: Users who have logged in exactly 30 days ago, or users who have not logged in at all.
- Performance pitfalls: Using inefficient database operations, such as using `SELECT *` instead of `SELECT COUNT(DISTINCT username)`.
- Testing considerations: Testing the query with different datasets and edge cases to ensure it produces the correct results.