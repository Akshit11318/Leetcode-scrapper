## Running Total for Different Genders
**Problem Link:** https://leetcode.com/problems/running-total-for-different-genders/description

**Problem Statement:**
- The input is a table `Scores` with columns `player_id` and `gender`, and a table `Matches` with columns `match_id`, `player_id`, and `score`.
- The goal is to write a SQL query to calculate the running total of scores for each player in each match, considering the gender of the player.
- Expected output format: A table with columns `player_id`, `match_id`, and `running_total`, where `running_total` is the running total of scores for each player in each match.
- Key requirements: The query should consider the gender of the player when calculating the running total.
- Example test cases:
  - For a given `Scores` table with two rows: `(1, 'M', 10)` and `(2, 'F', 20)`, and a `Matches` table with two rows: `(1, 1, 10)` and `(1, 2, 20)`, the output should be a table with two rows: `(1, 1, 10)` and `(1, 2, 30)`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: To calculate the running total of scores for each player in each match, we need to join the `Scores` and `Matches` tables on the `player_id` column.
- Step-by-step breakdown of the solution:
  1. Join the `Scores` and `Matches` tables on the `player_id` column.
  2. Group the joined table by `player_id`, `match_id`, and `gender`.
  3. Calculate the running total of scores for each group using a window function.
- Why this approach comes to mind first: It's a straightforward way to join the two tables and calculate the running total.

```sql
SELECT 
  S.player_id,
  M.match_id,
  SUM(M.score) OVER (PARTITION BY S.player_id, S.gender ORDER BY M.match_id) AS running_total
FROM 
  Scores S
JOIN 
  Matches M ON S.player_id = M.player_id
ORDER BY 
  S.player_id, M.match_id;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of rows in the joined table, due to the sorting required by the window function.
> - **Space Complexity:** $O(n)$, as we need to store the joined table in memory.
> - **Why these complexities occur:** The window function requires sorting the joined table, which has a time complexity of $O(n \log n)$. The space complexity is $O(n)$ because we need to store the joined table in memory.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a window function with a `PARTITION BY` clause to calculate the running total of scores for each player in each match, considering the gender of the player.
- Detailed breakdown of the approach:
  1. Join the `Scores` and `Matches` tables on the `player_id` column.
  2. Use a window function with a `PARTITION BY` clause to calculate the running total of scores for each player in each match, considering the gender of the player.
- Proof of optimality: This approach is optimal because it uses a single window function to calculate the running total, which has a time complexity of $O(n \log n)$.

```sql
SELECT 
  S.player_id,
  M.match_id,
  SUM(M.score) OVER (PARTITION BY S.player_id, S.gender ORDER BY M.match_id) AS running_total
FROM 
  Scores S
JOIN 
  Matches M ON S.player_id = M.player_id
ORDER BY 
  S.player_id, M.match_id;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of rows in the joined table, due to the sorting required by the window function.
> - **Space Complexity:** $O(n)$, as we need to store the joined table in memory.
> - **Optimality proof:** This approach is optimal because it uses a single window function to calculate the running total, which has a time complexity of $O(n \log n)$. This is the best possible time complexity for this problem, as we need to sort the joined table to calculate the running total.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Window functions, joining tables, and calculating running totals.
- Problem-solving patterns identified: Using window functions to calculate running totals, and joining tables to combine data.
- Optimization techniques learned: Using a single window function to calculate the running total, rather than using multiple queries or subqueries.
- Similar problems to practice: Calculating running totals for different groups, or using window functions to calculate other types of aggregations.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to include the `PARTITION BY` clause in the window function, or using the wrong type of join.
- Edge cases to watch for: Handling cases where the `player_id` or `match_id` columns are null, or where the `gender` column has unexpected values.
- Performance pitfalls: Using subqueries or multiple queries to calculate the running total, rather than using a single window function.
- Testing considerations: Testing the query with different types of data, including edge cases and large datasets.