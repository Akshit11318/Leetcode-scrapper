## Percentage of Users Attended a Contest

**Problem Link:** https://leetcode.com/problems/percentage-of-users-attended-a-contest/description

**Problem Statement:**
- Input: Two tables, `Users` and `Contests`, where `Users` contains information about users and `Contests` contains information about contests.
- Output: The percentage of users who attended a contest for each date.
- Key requirements and edge cases to consider: 
  - Each user can attend multiple contests on different dates.
  - The percentage is calculated based on the total number of users who attended a contest on a particular date.
- Example test cases with explanations: 
  - For a given set of users and contests, calculate the percentage of users who attended a contest on each date.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first step is to join the `Users` and `Contests` tables based on the user ID. Then, for each date, calculate the number of unique users who attended a contest and divide it by the total number of users to get the percentage.
- Step-by-step breakdown of the solution:
  1. Join the `Users` and `Contests` tables on the user ID.
  2. For each date, count the number of unique users who attended a contest.
  3. Calculate the percentage of users who attended a contest for each date.
- Why this approach comes to mind first: It is a straightforward approach that involves simple SQL queries to join the tables and calculate the percentages.

```cpp
// SQL query to solve the problem
SELECT 
    contest_date, 
    ROUND(COUNT(DISTINCT user_id) / (SELECT COUNT(*) FROM Users) * 100, 2) AS percentage
FROM 
    Contests
GROUP BY 
    contest_date
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the grouping and sorting of the data, where $n$ is the number of rows in the `Contests` table.
> - **Space Complexity:** $O(n)$ for storing the intermediate results, where $n$ is the number of rows in the `Contests` table.
> - **Why these complexities occur:** The time complexity is due to the grouping and sorting of the data, while the space complexity is due to the storage of the intermediate results.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves the same steps as the brute force approach, but with a more efficient SQL query.
- Detailed breakdown of the approach:
  1. Join the `Users` and `Contests` tables on the user ID.
  2. For each date, count the number of unique users who attended a contest.
  3. Calculate the percentage of users who attended a contest for each date.
- Proof of optimality: This approach is optimal because it involves a single SQL query that performs the necessary calculations, resulting in a time complexity of $O(n \log n)$.
- Why further optimization is impossible: Further optimization is impossible because the problem requires calculating the percentage of users who attended a contest for each date, which involves grouping and sorting the data.

```cpp
// SQL query to solve the problem
SELECT 
    contest_date, 
    ROUND(COUNT(DISTINCT user_id) / (SELECT COUNT(*) FROM Users) * 100, 2) AS percentage
FROM 
    Contests
GROUP BY 
    contest_date
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the grouping and sorting of the data, where $n$ is the number of rows in the `Contests` table.
> - **Space Complexity:** $O(n)$ for storing the intermediate results, where $n$ is the number of rows in the `Contests` table.
> - **Optimality proof:** This approach is optimal because it involves a single SQL query that performs the necessary calculations, resulting in a time complexity of $O(n \log n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Grouping and sorting data, calculating percentages.
- Problem-solving patterns identified: Using SQL queries to solve problems involving data analysis.
- Optimization techniques learned: Using efficient SQL queries to reduce time complexity.
- Similar problems to practice: Problems involving data analysis and SQL queries.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly joining tables, not handling edge cases.
- Edge cases to watch for: Handling dates with no contests, handling users with no contests.
- Performance pitfalls: Using inefficient SQL queries, not optimizing database queries.
- Testing considerations: Testing with different datasets, testing edge cases.