## Not Boring Movies

**Problem Link:** https://leetcode.com/problems/not-boring-movies/description

**Problem Statement:**
- Input format and constraints: The problem requires writing a SQL query to select all `id`, `movie_title`, and `description` columns from the `cinema` table where the `description` does not contain the word "boring".
- Expected output format: A table with the specified columns for movies that are not boring.
- Key requirements and edge cases to consider: Case sensitivity and the exact word "boring" should be considered.
- Example test cases with explanations: 
  - If a movie's description contains the word "boring", it should not be included in the results.
  - Movies with descriptions that do not contain the word "boring" should be included.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to manually filter each movie based on its description.
- Step-by-step breakdown of the solution: 
  1. Select all rows from the `cinema` table.
  2. For each row, check if the `description` contains the word "boring".
  3. If it does, skip this row; otherwise, include it in the result set.
- Why this approach comes to mind first: It directly addresses the problem statement by checking each movie's description.

```cpp
// Since this problem involves SQL, the brute force approach is more conceptual
// and less about code. However, the idea translates to a straightforward SQL query:
SELECT id, movie_title, description
FROM cinema
WHERE description NOT LIKE '%boring%';
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of rows in the `cinema` table, because we're potentially scanning each row once.
> - **Space Complexity:** $O(n)$ for storing the result set in the worst case (if all movies are not boring).
> - **Why these complexities occur:** The time complexity is linear because we're checking each row once. The space complexity is also linear because, in the worst case, we might store all rows in the result set.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is essentially the same as the brute force approach because we must check each movie's description to determine if it's boring or not. However, the optimal approach recognizes that SQL's built-in string functions can efficiently handle this task without needing to manually iterate over each row in the application code.
- Detailed breakdown of the approach: Use SQL's `NOT LIKE` operator with a wildcard (`%`) to match any characters before and after the word "boring" in the `description` field.
- Proof of optimality: This is optimal because it leverages the database's native capabilities for string matching, which are highly optimized for performance.
- Why further optimization is impossible: Further optimization is not possible because we must at least read each row's description once to determine if it contains the word "boring".

```sql
SELECT id, movie_title, description
FROM cinema
WHERE LOWER(description) NOT LIKE '%boring%';
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of rows in the `cinema` table, because we're still scanning each row.
> - **Space Complexity:** $O(n)$ for storing the result set in the worst case.
> - **Optimality proof:** The database's query optimizer will choose the most efficient plan, likely involving an index scan or a full table scan, depending on the table's size and indexing. The use of `LOWER` function ensures the query is case-insensitive.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: String matching, filtering data based on conditions.
- Problem-solving patterns identified: Directly addressing the problem statement with the most straightforward solution often leads to an optimal or near-optimal solution.
- Optimization techniques learned: Leveraging native database functions for optimized performance.
- Similar problems to practice: Other SQL problems involving string manipulation and filtering.

**Mistakes to Avoid:**
- Common implementation errors: Not considering case sensitivity, not using wildcards correctly in SQL's `LIKE` operator.
- Edge cases to watch for: Movies with descriptions that contain the word "boring" in different cases (e.g., "Boring", "BORING").
- Performance pitfalls: Not using indexes when applicable, although in this case, a full table scan might be the most efficient approach due to the nature of the query.
- Testing considerations: Ensure to test with a variety of movie descriptions, including those that contain the word "boring" in different cases and positions.