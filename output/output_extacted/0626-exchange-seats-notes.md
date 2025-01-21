## Exchange Seats
**Problem Link:** https://leetcode.com/problems/exchange-seats/description

**Problem Statement:**
- Input format and constraints: The problem involves a table with `n` seats, and we are given a table `seat` with columns `id` and `student`. The task is to write an SQL query to swap seats for students sitting in seats `id` and `id+1` if the total number of seats is odd.
- Expected output format: The output should be a table with columns `id` and `student`, where each student is assigned to a new seat according to the swapping rule.
- Key requirements and edge cases to consider: 
    - If the total number of seats is odd, the student in the last seat remains in the same seat.
    - If the total number of seats is even, all students are swapped with the student sitting next to them.
- Example test cases with explanations:
    - For example, if we have a table with seats `1`, `2`, `3`, `4`, the students in seats `1` and `2` should be swapped, and the students in seats `3` and `4` should be swapped.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over each row in the table and checking if the seat `id` is odd or even. If it's odd, we swap the student with the student in the next seat. If it's even, we don't swap the student.
- Step-by-step breakdown of the solution:
    1. Create a temporary table to store the swapped seats.
    2. Iterate over each row in the table.
    3. For each row, check if the seat `id` is odd or even.
    4. If the seat `id` is odd and it's not the last seat, swap the student with the student in the next seat.
    5. If the seat `id` is even, don't swap the student.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it may not be the most efficient solution.

```cpp
SELECT 
    (CASE 
        WHEN id % 2 = 1 AND id != (SELECT MAX(id) FROM seat) THEN id + 1
        WHEN id % 2 = 0 THEN id - 1
        ELSE id 
    END) AS id,
    student
FROM seat
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the table, because we are iterating over each row once.
> - **Space Complexity:** $O(n)$, because we are creating a temporary table to store the swapped seats.
> - **Why these complexities occur:** The time complexity occurs because we are iterating over each row in the table, and the space complexity occurs because we are creating a temporary table.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a single SQL query with a `CASE` statement to swap the seats.
- Detailed breakdown of the approach:
    1. Use a `CASE` statement to check if the seat `id` is odd or even.
    2. If the seat `id` is odd and it's not the last seat, swap the student with the student in the next seat.
    3. If the seat `id` is even, don't swap the student.
- Proof of optimality: This approach is optimal because it uses a single SQL query and doesn't require creating a temporary table.

```cpp
SELECT 
    (CASE 
        WHEN id % 2 = 1 AND id != (SELECT MAX(id) FROM seat) THEN id + 1
        WHEN id % 2 = 0 THEN id - 1
        ELSE id 
    END) AS id,
    student
FROM seat
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the table, because we are iterating over each row once.
> - **Space Complexity:** $O(1)$, because we are not creating any additional tables.
> - **Optimality proof:** This approach is optimal because it uses a single SQL query and doesn't require creating a temporary table.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of SQL queries and `CASE` statements to solve a problem.
- Problem-solving patterns identified: The problem requires identifying the seat `id` and swapping the students accordingly.
- Optimization techniques learned: The problem demonstrates the use of a single SQL query to optimize the solution.
- Similar problems to practice: Other problems that involve using SQL queries and `CASE` statements to solve a problem.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the seat `id` is the last seat before swapping the students.
- Edge cases to watch for: The case where the total number of seats is odd and the student in the last seat remains in the same seat.
- Performance pitfalls: Creating a temporary table to store the swapped seats, which can be avoided by using a single SQL query.
- Testing considerations: Testing the query with different inputs and edge cases to ensure it works correctly.