## Tasks Count in the Weekend

**Problem Link:** https://leetcode.com/problems/tasks-count-in-the-weekend/description

**Problem Statement:**
- Given a table `Tasks` with columns `task_id`, `task_name`, `start_date`, and `end_date`, find the number of tasks that occur during the weekend.
- The `start_date` and `end_date` are inclusive, and a task is considered to occur during the weekend if any part of the task overlaps with a weekend.
- The weekend is defined as Saturday and Sunday.
- Input format: A table `Tasks` with the specified columns.
- Expected output format: The number of tasks that occur during the weekend.
- Key requirements and edge cases to consider:
  - Tasks that start on a weekend and end on a weekend.
  - Tasks that start on a weekday and end on a weekend.
  - Tasks that start on a weekend and end on a weekday.
  - Tasks with the same start and end dates.

**Example Test Cases:**
- A task with `start_date` as Saturday and `end_date` as Sunday should be counted.
- A task with `start_date` as Friday and `end_date` as Monday should be counted.
- A task with `start_date` as Monday and `end_date` as Friday should not be counted.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate over each task and check if any part of the task overlaps with a weekend.
- We can use the `DAYOFWEEK` function in SQL to get the day of the week for the `start_date` and `end_date`.
- We can then check if the day of the week is Saturday (6) or Sunday (7) for either the `start_date` or the `end_date`, or if the task spans a weekend.

```sql
SELECT 
    COUNT(task_id) 
FROM 
    Tasks 
WHERE 
    DAYOFWEEK(start_date) = 6 
    OR DAYOFWEEK(start_date) = 7 
    OR DAYOFWEEK(end_date) = 6 
    OR DAYOFWEEK(end_date) = 7 
    OR (DAYOFWEEK(start_date) < 6 AND DAYOFWEEK(end_date) > 6);
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of tasks, because we are iterating over each task once.
> - **Space Complexity:** $O(1)$, because we are not using any additional space that scales with the input size.
> - **Why these complexities occur:** The time complexity occurs because we are iterating over each task, and the space complexity occurs because we are not using any additional space that scales with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach is to use a similar query as the brute force approach, but with a more efficient way to check if a task overlaps with a weekend.
- We can use the `DAYOFWEEK` function in SQL to get the day of the week for the `start_date` and `end_date`, and then use a single condition to check if the task overlaps with a weekend.

```sql
SELECT 
    COUNT(task_id) 
FROM 
    Tasks 
WHERE 
    (start_date + INTERVAL 1 DAY - INTERVAL 1 DAY) <= '2024-03-31' 
    AND (end_date + INTERVAL 1 DAY - INTERVAL 1 DAY) >= '2024-03-25' 
    AND (DAYOFWEEK(start_date) = 6 
    OR DAYOFWEEK(start_date) = 7 
    OR DAYOFWEEK(end_date) = 6 
    OR DAYOFWEEK(end_date) = 7 
    OR (DAYOFWEEK(start_date) < 6 AND DAYOFWEEK(end_date) > 6));
```

However, considering the constraints and the problem description provided, it seems like we're trying to count tasks that occur during the weekend within a specific date range (not explicitly provided in the problem description). Assuming we are looking for tasks that overlap with weekends in general, a more optimal query considering SQL would focus on the date range of interest.

For a general solution that counts tasks overlapping with weekends without a specific date range, the optimal SQL query can be simplified as follows:

```sql
SELECT 
    COUNT(task_id) 
FROM 
    Tasks 
WHERE 
    DAYOFWEEK(start_date) IN (6, 7) 
    OR DAYOFWEEK(end_date) IN (6, 7) 
    OR (DAYOFWEEK(start_date) < 6 AND DAYOFWEEK(end_date) > 6);
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of tasks, because we are iterating over each task once.
> - **Space Complexity:** $O(1)$, because we are not using any additional space that scales with the input size.
> - **Optimality proof:** This is the most efficient solution because we are only iterating over each task once, and we are using a single query to get the count of tasks that overlap with weekends.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using SQL to solve problems involving dates and counting tasks that overlap with specific conditions.
- Problem-solving patterns identified: Using the `DAYOFWEEK` function in SQL to get the day of the week for dates, and using conditions to check if tasks overlap with weekends.
- Optimization techniques learned: Simplifying queries to reduce complexity and improve efficiency.
- Similar problems to practice: Other problems involving dates and counting tasks that meet specific conditions.

**Mistakes to Avoid:**
- Common implementation errors: Not considering all possible cases for tasks overlapping with weekends, such as tasks that start on a weekend and end on a weekday.
- Edge cases to watch for: Tasks with the same start and end dates, tasks that span multiple weekends.
- Performance pitfalls: Using inefficient queries that iterate over tasks multiple times.
- Testing considerations: Testing the query with different date ranges and task overlaps to ensure correctness.