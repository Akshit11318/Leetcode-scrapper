## Top Three Wineries
**Problem Link:** https://leetcode.com/problems/top-three-wineries/description

**Problem Statement:**
- Input format and constraints: You are given a table `Wine` with columns `id` (integer) and `points` (integer).
- Expected output format: Return a table with the top three wineries based on the points they have.
- Key requirements and edge cases to consider: If there are less than three wineries, return all of them. If there are ties in points, return all wineries with the same points.
- Example test cases with explanations:
  - Example 1: 
    - Input: `Wine` table with rows (1, 10), (2, 20), (3, 30)
    - Output: (1, 10), (2, 20), (3, 30)
  - Example 2: 
    - Input: `Wine` table with rows (1, 10), (2, 20), (3, 20)
    - Output: (2, 20), (3, 20), (1, 10)

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can simply sort the wineries based on their points in descending order and return the top three.
- Step-by-step breakdown of the solution:
  1. Select all rows from the `Wine` table.
  2. Sort the rows based on the `points` column in descending order.
  3. Return the top three rows.
- Why this approach comes to mind first: It is a straightforward and simple solution.

```cpp
SELECT id, points
FROM Wine
ORDER BY points DESC
LIMIT 3
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation, where $n$ is the number of rows in the `Wine` table.
> - **Space Complexity:** $O(n)$ for storing the sorted rows.
> - **Why these complexities occur:** Sorting requires comparing and swapping elements, resulting in a time complexity of $O(n \log n)$. The space complexity is $O(n)$ because we need to store the sorted rows.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use the `DENSE_RANK()` function to assign a rank to each row based on the `points` column. This allows us to handle ties correctly.
- Detailed breakdown of the approach:
  1. Select all rows from the `Wine` table.
  2. Use the `DENSE_RANK()` function to assign a rank to each row based on the `points` column in descending order.
  3. Return the rows with a rank of 1, 2, or 3.
- Proof of optimality: This approach correctly handles ties and returns the top three wineries with the most points.

```sql
SELECT id, points
FROM (
  SELECT id, points,
  DENSE_RANK() OVER (ORDER BY points DESC) as rank
  FROM Wine
) AS ranked_wine
WHERE rank <= 3
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation, where $n$ is the number of rows in the `Wine` table.
> - **Space Complexity:** $O(n)$ for storing the ranked rows.
> - **Optimality proof:** This approach correctly handles ties and returns the top three wineries with the most points, making it the optimal solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, ranking, and handling ties.
- Problem-solving patterns identified: Using window functions to assign ranks.
- Optimization techniques learned: Using `DENSE_RANK()` to handle ties correctly.
- Similar problems to practice: Other ranking and sorting problems.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle ties, using the wrong ranking function.
- Edge cases to watch for: Ties in points, less than three wineries.
- Performance pitfalls: Using inefficient sorting algorithms.
- Testing considerations: Test with different input sizes, ties, and edge cases.