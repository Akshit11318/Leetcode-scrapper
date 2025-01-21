## Movie Rating
**Problem Link:** https://leetcode.com/problems/movie-rating/description

**Problem Statement:**
- Input format and constraints: You are given a table `movie_rating` with columns `movie_id`, `user_id`, and `rating`, where `rating` is an integer between 1 and 5. The table has no duplicates and does not contain any NULL values. The goal is to write a SQL query to find the `movie_id` and corresponding average `rating` for each movie.
- Expected output format: The result should be ordered by the `movie_id`.
- Key requirements and edge cases to consider: All `movie_id`s should be included in the output, even if a movie has no ratings. The average rating should be rounded to two decimal places.
- Example test cases with explanations: 
  - For a table with a single movie and a single rating, the output should be the movie's ID and the rating.
  - For a table with multiple movies, each with multiple ratings, the output should be each movie's ID and its average rating.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the average rating for each movie, we can use a SQL query with a `GROUP BY` clause to group the ratings by movie ID and then calculate the average rating for each group.
- Step-by-step breakdown of the solution:
  1. Select the `movie_id` and `rating` from the `movie_rating` table.
  2. Group the selected rows by the `movie_id`.
  3. Calculate the average `rating` for each group.
- Why this approach comes to mind first: It directly addresses the problem statement by grouping the ratings by movie ID and calculating the average.

```sql
SELECT 
  movie_id,
  ROUND(AVG(rating), 2) AS avg_rating
FROM 
  movie_rating
GROUP BY 
  movie_id
ORDER BY 
  movie_id;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of rows in the `movie_rating` table, because we are scanning the table once.
> - **Space Complexity:** $O(n)$ for storing the intermediate results of the `GROUP BY` operation.
> - **Why these complexities occur:** The time complexity is linear because we are performing a single pass through the data. The space complexity is also linear because in the worst case, we might need to store every row in the intermediate results.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal approach is essentially the same as the brute force approach because the problem requires us to examine every row in the table at least once to calculate the average ratings. However, we should also consider including movies with no ratings in the output.
- Detailed breakdown of the approach:
  1. Select the distinct `movie_id`s from the `movie_rating` table.
  2. Left join this result with the average ratings calculated from the `movie_rating` table.
- Proof of optimality: This approach is optimal because it only requires a single pass through the data and it includes all movies, even those without ratings.

```sql
SELECT 
  m.movie_id,
  COALESCE(ROUND(AVG(r.rating), 2), 0.00) AS avg_rating
FROM 
  (SELECT DISTINCT movie_id FROM movie_rating) m
  LEFT JOIN movie_rating r ON m.movie_id = r.movie_id
GROUP BY 
  m.movie_id
ORDER BY 
  m.movie_id;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of rows in the `movie_rating` table.
> - **Space Complexity:** $O(n)$ for storing the intermediate results.
> - **Optimality proof:** This is the best possible complexity because we must examine every row at least once to calculate the average ratings.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Grouping and aggregation in SQL.
- Problem-solving patterns identified: Using `GROUP BY` and aggregate functions to solve problems involving averages and other summary statistics.
- Optimization techniques learned: Considering the inclusion of all relevant data points, even those without ratings.
- Similar problems to practice: Other SQL problems involving grouping, aggregation, and joining tables.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to round the average rating to two decimal places, or not including movies without ratings in the output.
- Edge cases to watch for: Handling movies with no ratings, and ensuring that the output includes all movies.
- Performance pitfalls: Using inefficient joins or subqueries that could increase the time complexity of the query.
- Testing considerations: Testing the query with different datasets, including edge cases like movies with no ratings, to ensure it produces the correct output.