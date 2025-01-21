## Number of Comments per Post
**Problem Link:** https://leetcode.com/problems/number-of-comments-per-post/description

**Problem Statement:**
- Input format and constraints: The problem involves three tables: `Submissions`, `Comments`, and `Questions`. The `Submissions` table contains information about posts, the `Comments` table contains information about comments made on those posts, and the `Questions` table contains information about questions. The goal is to find the number of comments per post.
- Expected output format: The output should be a table with two columns: `id` (the post ID) and `num_comments` (the number of comments for that post).
- Key requirements and edge cases to consider: We need to handle cases where a post has no comments, and we need to ensure that we're counting comments correctly.
- Example test cases with explanations: For example, if we have a post with ID 1 and two comments with IDs 1 and 2, both referencing post ID 1, the output should show post ID 1 with 2 comments.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can start by joining the `Submissions` and `Comments` tables on the `id` column to link each post with its comments.
- Step-by-step breakdown of the solution: 
  1. Join the `Submissions` and `Comments` tables.
  2. Group the results by post ID.
  3. Count the number of comments for each post ID.
- Why this approach comes to mind first: This approach is straightforward and directly addresses the problem by linking posts with their comments and then counting those comments.

```cpp
SELECT S.id, COUNT(C.id) as num_comments
FROM Submissions S
LEFT JOIN Comments C ON S.id = C.comment_id
GROUP BY S.id
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting required for grouping.
> - **Space Complexity:** $O(n)$ for storing the joined table.
> - **Why these complexities occur:** The time complexity is due to the grouping operation, which requires sorting the data. The space complexity is due to the need to store the joined table in memory.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of joining the entire `Submissions` table, we can directly count the comments for each post ID from the `Comments` table.
- Detailed breakdown of the approach: 
  1. Select distinct post IDs from the `Comments` table.
  2. Count the number of comments for each post ID.
  3. Use a `LEFT JOIN` or `UNION` to include posts with no comments.
- Proof of optimality: This approach is optimal because it only requires accessing the `Comments` table and then joining or unioning with the `Submissions` table to include posts with no comments, reducing unnecessary data processing.

```cpp
SELECT S.id, IFNULL(C.num_comments, 0) as num_comments
FROM Submissions S
LEFT JOIN (
  SELECT comment_id, COUNT(id) as num_comments
  FROM Comments
  GROUP BY comment_id
) C ON S.id = C.comment_id
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ for selecting and counting comments, and $O(m)$ for the left join, where $n$ is the number of comments and $m$ is the number of submissions.
> - **Space Complexity:** $O(n + m)$ for storing the results of the subquery and the final join.
> - **Optimality proof:** This approach is optimal because it minimizes the amount of data being processed and joined, focusing only on the necessary information from the `Comments` table and then combining it with the `Submissions` table.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Joining tables, grouping, and counting.
- Problem-solving patterns identified: Reducing the problem to a simpler form by focusing on the key information needed (in this case, comment counts per post).
- Optimization techniques learned: Minimizing data processing by only accessing necessary tables and using efficient join operations.
- Similar problems to practice: Other SQL problems involving joins, aggregations, and optimizations.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect join conditions, forgetting to include posts with no comments.
- Edge cases to watch for: Posts with no comments, comments with no associated posts (if such a scenario is possible in the given problem context).
- Performance pitfalls: Joining large tables unnecessarily, not using indexes (if applicable).
- Testing considerations: Ensure that the solution correctly handles posts with and without comments, and that it scales well with large datasets.