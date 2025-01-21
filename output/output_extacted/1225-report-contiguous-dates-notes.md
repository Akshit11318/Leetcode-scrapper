## Report Contiguous Dates

**Problem Link:** https://leetcode.com/problems/report-contiguous-dates/description

**Problem Statement:**
- Input format and constraints: Given a table `Failed` with columns `id` and `day`, write a SQL query to report all the contiguous dates in the table.
- Expected output format: The output should be a table with a single column `period_state`, where each row represents a contiguous date range in the format 'YYYY-MM-DD' to 'YYYY-MM-DD'.
- Key requirements and edge cases to consider: The date range should be contiguous, and there should be no gaps in the dates.
- Example test cases with explanations:
  - If the table contains dates '2020-01-01', '2020-01-02', '2020-01-03', the output should be '2020-01-01' to '2020-01-03'.
  - If the table contains dates '2020-01-01', '2020-01-03', '2020-01-04', the output should be two rows: '2020-01-01' to '2020-01-01' and '2020-01-03' to '2020-01-04'.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find contiguous dates, we can sort the dates and then iterate through them to find the contiguous ranges.
- Step-by-step breakdown of the solution:
  1. Sort the dates in ascending order.
  2. Initialize variables to keep track of the start and end of the current contiguous range.
  3. Iterate through the sorted dates, and for each date, check if it is contiguous with the previous date.
  4. If it is contiguous, update the end of the current contiguous range.
  5. If it is not contiguous, add the current contiguous range to the result and start a new range.
- Why this approach comes to mind first: It is a simple and intuitive approach that is easy to understand and implement.

```sql
SELECT 
  MIN(day) AS start_date,
  MAX(day) AS end_date
FROM 
  (
    SELECT 
      day,
      day - ROW_NUMBER() OVER (ORDER BY day) AS diff
    FROM 
      Failed
  ) AS subquery
GROUP BY 
  diff
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting of dates.
> - **Space Complexity:** $O(n)$ for storing the sorted dates.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, and the space complexity is due to the storage of the sorted dates.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a single SQL query with window functions to find the contiguous dates.
- Detailed breakdown of the approach:
  1. Use the `ROW_NUMBER()` function to assign a unique number to each row in the sorted order of dates.
  2. Calculate the difference between the date and the row number.
  3. Group the dates by the difference, which will group contiguous dates together.
  4. Select the minimum and maximum dates for each group to get the start and end of the contiguous range.
- Proof of optimality: This approach has a time complexity of $O(n \log n)$ due to the sorting, which is optimal for this problem.
- Why further optimization is impossible: The sorting operation is necessary to find the contiguous dates, and any further optimization would require a different approach that does not involve sorting.

```sql
SELECT 
  CONCAT(MIN(day), ' to ', MAX(day)) AS period_state
FROM 
  (
    SELECT 
      day,
      day - ROW_NUMBER() OVER (ORDER BY day) AS diff
    FROM 
      Failed
  ) AS subquery
GROUP BY 
  diff
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting of dates.
> - **Space Complexity:** $O(n)$ for storing the sorted dates.
> - **Optimality proof:** The time complexity is optimal because sorting is necessary to find contiguous dates.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Window functions, grouping, and sorting.
- Problem-solving patterns identified: Using window functions to find contiguous ranges.
- Optimization techniques learned: Using a single SQL query to reduce complexity.
- Similar problems to practice: Finding contiguous ranges in other types of data.

**Mistakes to Avoid:**
- Common implementation errors: Not sorting the dates before finding contiguous ranges.
- Edge cases to watch for: Handling dates with gaps or duplicates.
- Performance pitfalls: Using inefficient algorithms or queries that do not scale well.
- Testing considerations: Testing with different types of input data, including edge cases.