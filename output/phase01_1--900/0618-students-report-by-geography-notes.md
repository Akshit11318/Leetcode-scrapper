## Students Report by Geography

**Problem Link:** https://leetcode.com/problems/students-report-by-geography/description

**Problem Statement:**
- Input format and constraints: The problem involves three tables: `Student`, `Mailing`, and `Apply`. The `Student` table contains student information, the `Mailing` table contains mailing addresses, and the `Apply` table contains information about students applying to universities. We need to find the number of students from each region of the world.
- Expected output format: The result should be a table with two columns: `name` and `count`, where `name` represents the region and `count` represents the number of students from that region.
- Key requirements and edge cases to consider: We need to handle cases where a student does not have a mailing address or an application.
- Example test cases with explanations: 
    - If there are no students, the result should be an empty table.
    - If there are students but no mailing addresses, the result should be an empty table.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can start by joining the three tables based on the student ID and then grouping the result by region.
- Step-by-step breakdown of the solution: 
    1. Join the `Student`, `Mailing`, and `Apply` tables based on the student ID.
    2. Extract the region from the mailing address.
    3. Group the result by region and count the number of students in each region.
- Why this approach comes to mind first: This approach is straightforward and involves basic SQL operations.

```cpp
// SQL query
SELECT 
    c.name, 
    COUNT(s.id) as count
FROM 
    Student s
JOIN 
    Mailing m ON s.id = m.id
JOIN 
    Apply a ON s.id = a.id
JOIN 
    City c ON m.city = c.code
GROUP BY 
    c.name
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where n is the number of rows in the `Student` table, because we are joining three tables and then grouping the result.
> - **Space Complexity:** $O(n)$, because we need to store the joined table and the grouped result.
> - **Why these complexities occur:** The time complexity is linear because we are performing a constant amount of work for each row in the `Student` table. The space complexity is also linear because we need to store the joined table and the grouped result.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use the same approach as the brute force solution, but we can optimize the query by using indexes on the join columns.
- Detailed breakdown of the approach: 
    1. Create indexes on the join columns.
    2. Join the `Student`, `Mailing`, and `Apply` tables based on the student ID.
    3. Extract the region from the mailing address.
    4. Group the result by region and count the number of students in each region.
- Proof of optimality: This approach is optimal because it involves the minimum number of operations required to solve the problem.
- Why further optimization is impossible: Further optimization is impossible because we need to perform the joins and grouping to get the desired result.

```cpp
// SQL query
CREATE INDEX idx_student_id ON Student (id);
CREATE INDEX idx_mailing_id ON Mailing (id);
CREATE INDEX idx_apply_id ON Apply (id);
CREATE INDEX idx_city_code ON City (code);

SELECT 
    c.name, 
    COUNT(s.id) as count
FROM 
    Student s
JOIN 
    Mailing m ON s.id = m.id
JOIN 
    Apply a ON s.id = a.id
JOIN 
    City c ON m.city = c.code
GROUP BY 
    c.name
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where n is the number of rows in the `Student` table, because we are joining three tables and then grouping the result.
> - **Space Complexity:** $O(n)$, because we need to store the joined table and the grouped result.
> - **Optimality proof:** The time complexity is linear because we are performing a constant amount of work for each row in the `Student` table. The space complexity is also linear because we need to store the joined table and the grouped result.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Joining tables, grouping, and counting.
- Problem-solving patterns identified: Using indexes to optimize queries.
- Optimization techniques learned: Creating indexes on join columns.
- Similar problems to practice: Other SQL problems involving joins and grouping.

**Mistakes to Avoid:**
- Common implementation errors: Not creating indexes on join columns.
- Edge cases to watch for: Handling cases where a student does not have a mailing address or an application.
- Performance pitfalls: Not optimizing queries with indexes.
- Testing considerations: Testing the query with different inputs and edge cases.