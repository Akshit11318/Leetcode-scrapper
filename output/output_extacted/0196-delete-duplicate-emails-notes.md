## Delete Duplicate Emails

**Problem Link:** https://leetcode.com/problems/delete-duplicate-emails/description

**Problem Statement:**
- Input format and constraints: The problem involves deleting duplicate emails from a table `Person` based on the `Email` column. The table has columns `Id`, `Email`, and `Name`.
- Expected output format: After deleting duplicates, the resulting table should contain unique emails.
- Key requirements and edge cases to consider: 
    - The table may have duplicate emails.
    - The `Id` column is unique.
    - The solution should delete rows with duplicate emails, keeping only one instance of each email.
- Example test cases with explanations:
    - If the table contains two rows with the same email, only one should remain after deletion.
    - If the table contains no duplicate emails, no rows should be deleted.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first step is to identify all duplicate emails in the table. This can be achieved by grouping the rows by the `Email` column and counting the number of occurrences for each email. Then, for each duplicate email, delete all but one instance.
- Step-by-step breakdown of the solution:
    1. Create a temporary table to store the count of each email.
    2. Group the `Person` table by `Email` and count the occurrences.
    3. For each email that appears more than once, delete all but one instance from the `Person` table.
- Why this approach comes to mind first: It directly addresses the problem statement by identifying and removing duplicates.

```cpp
-- SQL query for brute force approach
DELETE p1
FROM Person p1, Person p2
WHERE p1.Email = p2.Email AND p1.Id > p2.Id;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ due to the self-join operation, where $n$ is the number of rows in the table.
> - **Space Complexity:** $O(1)$ as no additional space is used that scales with input size.
> - **Why these complexities occur:** The self-join operation compares each row with every other row, leading to a quadratic time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Utilize a subquery to select the minimum `Id` for each group of duplicate emails and then delete rows that do not match these minimum `Id`s.
- Detailed breakdown of the approach:
    1. Use a subquery to group the `Person` table by `Email` and find the minimum `Id` for each group.
    2. Delete rows from the `Person` table where the `Id` is not in the set of minimum `Id`s found in step 1.
- Proof of optimality: This approach ensures that only one instance of each email remains, and it does so in a way that minimizes the number of operations, making it optimal.

```cpp
-- SQL query for optimal approach
DELETE FROM Person
WHERE Id NOT IN (
    SELECT MIN(Id)
    FROM Person
    GROUP BY Email
);
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of rows in the table, because we perform a constant amount of work for each row.
> - **Space Complexity:** $O(n)$ for storing the subquery results.
> - **Optimality proof:** This solution has a linear time complexity with respect to the number of rows, which is the best we can achieve for this problem since we must at least read the input.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The importance of indexing, subqueries, and the `MIN` function in SQL.
- Problem-solving patterns identified: The use of subqueries to solve problems involving duplicate data.
- Optimization techniques learned: Avoiding self-joins and instead using subqueries or joins with aggregated values.
- Similar problems to practice: Problems involving duplicate data, aggregation, and subqueries.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly using `JOIN` instead of subqueries, or not properly handling the `MIN` function.
- Edge cases to watch for: Tables with no duplicate emails, tables with all duplicate emails.
- Performance pitfalls: Using self-joins or other inefficient operations.
- Testing considerations: Ensure to test with various scenarios, including tables with and without duplicates, and verify the correctness of the solution.