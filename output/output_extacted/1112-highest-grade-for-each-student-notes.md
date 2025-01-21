## Highest Grade for Each Student

**Problem Link:** https://leetcode.com/problems/highest-grade-for-each-student/description

**Problem Statement:**
- Input format: You are given two tables: `Enrollments` and `Courses`. The `Enrollments` table has columns `student_id` and `course_id`, while the `Courses` table has columns `course_id`, `course_name`, and `grade`.
- Constraints: Each student is enrolled in at least one course, and each course has at least one enrolled student. The `student_id` and `course_id` are unique identifiers.
- Expected output format: A table with the `student_id` and the highest grade for each student.
- Key requirements and edge cases to consider:
  - Handling students with multiple enrollments in different courses.
  - Ensuring that the output includes all students from the `Enrollments` table.
- Example test cases with explanations:
  - A simple case where each student is enrolled in only one course.
  - A more complex case where a student is enrolled in multiple courses with different grades.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Join the `Enrollments` and `Courses` tables on `course_id` to get a combined table with all student enrollments and their corresponding grades.
- Step-by-step breakdown of the solution:
  1. Perform an inner join between `Enrollments` and `Courses` on `course_id`.
  2. Group the resulting table by `student_id`.
  3. For each group, find the maximum `grade`.
- Why this approach comes to mind first: It directly addresses the need to combine student enrollment information with course grade information and then find the highest grade for each student.

```cpp
SELECT E.student_id, MAX(C.grade) as grade
FROM Enrollments E
JOIN Courses C ON E.course_id = C.course_id
GROUP BY E.student_id
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting required for grouping and finding the maximum grade for each student, where $n$ is the total number of enrollments.
> - **Space Complexity:** $O(n)$ for storing the joined and grouped data.
> - **Why these complexities occur:** The join operation can be efficient with indexing, but the grouping and finding the maximum grade introduce the need for sorting or using data structures that allow for efficient aggregation.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same approach as the brute force is actually optimal because it directly solves the problem with the necessary join and aggregation operations. However, indexing on `course_id` in both tables can improve the efficiency of the join operation.
- Detailed breakdown of the approach:
  1. Create indexes on `course_id` in both `Enrollments` and `Courses` tables if not already indexed.
  2. Perform the inner join and grouping as described in the brute force approach.
- Proof of optimality: This approach is optimal because it minimizes the number of operations needed to solve the problem. It requires a single pass through the data to join the tables and find the maximum grade for each student.
- Why further optimization is impossible: Without additional constraints or structure in the data, further optimization is not possible because the problem inherently requires examining each enrollment and its corresponding grade.

```cpp
-- Assuming SQL as the query language for this problem
SELECT E.student_id, MAX(C.grade) as grade
FROM Enrollments E
JOIN Courses C ON E.course_id = C.course_id
GROUP BY E.student_id
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the total number of enrollments, due to the need to sort or aggregate the data for grouping and finding the maximum grade.
> - **Space Complexity:** $O(n)$ for storing the joined and grouped data.
> - **Optimality proof:** This approach is optimal because it directly addresses the problem's requirements with the minimum necessary operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Joining tables, grouping data, and finding the maximum value within each group.
- Problem-solving patterns identified: The importance of indexing for efficient join operations and the use of aggregation functions like `MAX` for finding the highest grade.
- Optimization techniques learned: Creating indexes on columns used in join operations.
- Similar problems to practice: Other SQL problems involving joins, aggregations, and optimizations.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to group by `student_id` or incorrectly joining the tables.
- Edge cases to watch for: Handling students with no enrollments or courses with no enrolled students, though the problem statement guarantees at least one enrollment per student and one student per course.
- Performance pitfalls: Not indexing columns used in join operations, which can significantly slow down the query.
- Testing considerations: Ensure that the query correctly handles various scenarios, including students with multiple enrollments and different grades.