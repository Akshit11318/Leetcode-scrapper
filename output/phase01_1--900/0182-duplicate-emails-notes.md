## Duplicate Emails

**Problem Link:** [https://leetcode.com/problems/duplicate-emails/description](https://leetcode.com/problems/duplicate-emails/description)

**Problem Statement:**
- Input format and constraints: You are given a table `Person` with columns `id` and `email`. Your task is to write a SQL query to find all duplicate emails in this table.
- Expected output format: The output should contain a single column `email` with all the emails that appear more than once in the `Person` table.
- Key requirements and edge cases to consider: 
  - The `email` column may contain `NULL` values, which should be ignored.
  - The query should be case-insensitive, i.e., "example@gmail.com" and "EXAMPLE@GMAIL.COM" should be considered the same email.
- Example test cases with explanations:
  - If the `Person` table contains the following data: 
    ```markdown
    +----+---------------+
    | id | email         |
    +----+---------------+
    | 1  | john@example |
    | 2  | john@example |
    | 3  | jane@example  |
    +----+---------------+
    ```
    The output should be: 
    ```markdown
    +---------------+
    | email         |
    +---------------+
    | john@example |
    +---------------+
    ```

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to use a subquery to find all emails that appear more than once in the `Person` table.
- Step-by-step breakdown of the solution: 
  1. Select all distinct emails from the `Person` table.
  2. For each email, use a subquery to count the number of times it appears in the table.
  3. If the count is greater than 1, include the email in the output.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it may not be the most efficient way to solve the problem.

```sql
SELECT email
FROM (
  SELECT email, COUNT(*) as count
  FROM Person
  GROUP BY email
) AS subquery
WHERE count > 1;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the `Person` table. This is because we are using a subquery to count the occurrences of each email.
> - **Space Complexity:** $O(n)$, because we are storing the results of the subquery in memory.
> - **Why these complexities occur:** The subquery needs to iterate over all rows in the table to count the occurrences of each email, resulting in a time complexity of $O(n)$. The space complexity is also $O(n)$ because we need to store the results of the subquery.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a single `GROUP BY` statement to count the occurrences of each email and select only those that appear more than once.
- Detailed breakdown of the approach: 
  1. Use a `GROUP BY` statement to group the rows of the `Person` table by email.
  2. Use the `HAVING` clause to filter the results and only include groups with more than one row.
- Proof of optimality: This approach is optimal because it only requires a single pass over the data and does not use any subqueries.
- Why further optimization is impossible: This approach has a time complexity of $O(n)$, which is the best we can do because we need to examine every row in the table at least once.

```sql
SELECT email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the `Person` table. This is because we are using a single `GROUP BY` statement to count the occurrences of each email.
> - **Space Complexity:** $O(n)$, because we are storing the results of the `GROUP BY` statement in memory.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the data and does not use any subqueries.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: `GROUP BY` and `HAVING` clauses in SQL.
- Problem-solving patterns identified: Using a single `GROUP BY` statement to count the occurrences of each email and filter the results.
- Optimization techniques learned: Avoiding subqueries and using a single pass over the data.
- Similar problems to practice: Other SQL problems that involve counting and filtering data.

**Mistakes to Avoid:**
- Common implementation errors: Using subqueries when a single `GROUP BY` statement will suffice.
- Edge cases to watch for: `NULL` values in the `email` column and case-insensitivity.
- Performance pitfalls: Using subqueries or multiple passes over the data.
- Testing considerations: Make sure to test the query with a variety of input data, including `NULL` values and duplicate emails.