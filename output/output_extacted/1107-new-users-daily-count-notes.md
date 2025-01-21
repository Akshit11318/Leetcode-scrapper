## New Users Daily Count
**Problem Link:** https://leetcode.com/problems/new-users-daily-count/description

**Problem Statement:**
- Input: `createAt` table with `id` and `createAt` columns representing the date of account creation.
- Output: A table with the date and the number of new users who created an account on that date.
- Key requirements: Count the number of new users for each day.
- Example test cases:
    - Input: 
        ```
+------------+
| id | createAt|
+------------+
| 1  | 2019-08-01|
| 2  | 2019-08-02|
| 3  | 2019-08-02|
| 4  | 2019-08-03|
| 5  | 2019-08-03|
+------------+
```
    - Output:
        ```
+------------+------------+
| day        | count      |
+------------+------------+
| 2019-08-01 | 1          |
| 2019-08-02 | 2          |
| 2019-08-03 | 2          |
+------------+------------+
```

---

### Brute Force Approach
**Explanation:**
- This problem can be solved using a simple `GROUP BY` SQL query. 
- The idea is to group the rows by the `createAt` date and then count the number of rows in each group.

```cpp
SELECT 
    createAt AS day, 
    COUNT(id) AS count
FROM 
    createAt
GROUP BY 
    createAt
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the table, because we need to scan each row once.
> - **Space Complexity:** $O(n)$, because in the worst case, we might need to store all rows in memory.
> - **Why these complexities occur:** The time complexity is linear because we only need to scan each row once, and the space complexity is linear because we need to store the results of the `GROUP BY` operation.

---

### Optimal Approach (Required)
**Explanation:**
- The optimal approach is the same as the brute force approach because the problem requires us to count the number of new users for each day, and the `GROUP BY` operation is the most efficient way to do this.
- The key insight is that we can use the `GROUP BY` clause to group the rows by the `createAt` date and then use the `COUNT` function to count the number of rows in each group.

```cpp
SELECT 
    createAt AS day, 
    COUNT(id) AS count
FROM 
    createAt
GROUP BY 
    createAt
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the table, because we need to scan each row once.
> - **Space Complexity:** $O(n)$, because in the worst case, we might need to store all rows in memory.
> - **Optimality proof:** This is the optimal approach because we need to scan each row at least once to count the number of new users for each day, and the `GROUP BY` operation is the most efficient way to do this.

---

### Final Notes

**Learning Points:**
- The `GROUP BY` clause is used to group rows that have the same values in the specified columns.
- The `COUNT` function is used to count the number of rows in each group.
- The optimal approach is often the simplest one, especially when working with SQL.

**Mistakes to Avoid:**
- Forgetting to include the `GROUP BY` clause when using aggregate functions like `COUNT`.
- Not specifying the correct columns in the `GROUP BY` clause.
- Not handling edge cases, such as empty tables or tables with no rows for a particular date.