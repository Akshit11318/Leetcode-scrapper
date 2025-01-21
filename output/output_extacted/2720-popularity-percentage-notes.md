## Popularity Percentage

**Problem Link:** [https://leetcode.com/problems/popularity-percentage/description](https://leetcode.com/problems/popularity-percentage/description)

**Problem Statement:**
- Input format: A table `Views` with columns `id` and `article_id`.
- Constraints: `id` is the primary key, and `article_id` is a foreign key referencing the `Articles` table.
- Expected output format: A table with `article_id` and `percentage` columns, where `percentage` is the popularity of each article as a percentage of the total views.
- Key requirements and edge cases to consider: Handling cases where an article has no views, and ensuring the `percentage` column is rounded to two decimal places.
- Example test cases with explanations:
  - Test case 1: An article with 10 views and a total of 100 views across all articles should have a popularity of 10.00%.
  - Test case 2: An article with no views should have a popularity of 0.00%.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the total views for each article and then calculate the percentage of total views for each article.
- Step-by-step breakdown of the solution:
  1. Calculate the total views for each article.
  2. Calculate the total views across all articles.
  3. For each article, calculate the percentage of total views.
- Why this approach comes to mind first: It is a straightforward approach that directly calculates the required metrics.

```cpp
SELECT 
  a.id AS id,
  ROUND(
    SUM(CASE WHEN v.article_id = a.id THEN 1 ELSE 0 END) * 100.0 / 
    (SELECT COUNT(*) FROM Views), 
    2
  ) AS percentage
FROM 
  Articles a
  LEFT JOIN Views v ON a.id = v.article_id
GROUP BY 
  a.id
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of articles and $m$ is the number of views. This is because we are joining the `Articles` and `Views` tables.
> - **Space Complexity:** $O(n + m)$, as we are storing the results of the join operation.
> - **Why these complexities occur:** The join operation causes the time complexity to be $O(n \cdot m)$, and the space complexity is due to the storage of the join results.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a subquery to calculate the total views across all articles and then join this result with the `Articles` table to calculate the percentage of total views for each article.
- Detailed breakdown of the approach:
  1. Calculate the total views across all articles using a subquery.
  2. Join the `Articles` table with the subquery result to calculate the percentage of total views for each article.
- Proof of optimality: This approach is optimal because it only requires a single pass over the `Views` table to calculate the total views, and then a single pass over the `Articles` table to calculate the percentage of total views for each article.

```cpp
SELECT 
  a.id,
  IFNULL(ROUND(v.views * 100.0 / t.total_views, 2), 0.00) AS percentage
FROM 
  Articles a
  LEFT JOIN (
    SELECT 
      article_id, 
      COUNT(*) AS views
    FROM 
      Views
    GROUP BY 
      article_id
  ) v ON a.id = v.article_id
  CROSS JOIN (
    SELECT 
      COUNT(*) AS total_views
    FROM 
      Views
  ) t
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of articles and $m$ is the number of views. This is because we are performing two separate aggregate operations.
> - **Space Complexity:** $O(n + m)$, as we are storing the results of the aggregate operations.
> - **Optimality proof:** The time complexity is optimal because we are only performing two separate aggregate operations, and the space complexity is optimal because we are only storing the necessary results.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Aggregate operations, subqueries, and joins.
- Problem-solving patterns identified: Breaking down complex problems into simpler sub-problems and using subqueries to calculate intermediate results.
- Optimization techniques learned: Using subqueries to reduce the number of join operations and optimizing aggregate operations.
- Similar problems to practice: Other problems involving aggregate operations and subqueries.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly using aggregate operations or subqueries.
- Edge cases to watch for: Handling cases where an article has no views.
- Performance pitfalls: Using inefficient join operations or aggregate operations.
- Testing considerations: Testing the solution with different input data to ensure correctness and performance.