## Rising Temperature

**Problem Link:** https://leetcode.com/problems/rising-temperature/description

**Problem Statement:**
- Input format and constraints: Given a table `Weather` with columns `id`, `recordDate`, and `temperature`, write a SQL query to find all `id`s where the temperature was higher than the previous day.
- Expected output format: Return a table with a single column `id`.
- Key requirements and edge cases to consider: The previous day's temperature should be compared with the current day's temperature for each `id`. If there is no previous day's temperature for an `id`, it should not be included in the result.
- Example test cases with explanations: 
  - For example, if the table contains the following rows:
    | id | recordDate | temperature |
    |----|------------|-------------|
    | 1  | 2015-01-01 | 10          |
    | 1  | 2015-01-02 | 20          |
    | 1  | 2015-01-03 | 15          |
    | 2  | 2015-01-01 | 25          |
    | 2  | 2015-01-02 | 30          |
  - The output should be:
    | id |
    |----|
    | 1  |
    | 2  |

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves comparing each row's temperature with the previous day's temperature for the same `id`. This can be achieved by using a self-join or a subquery to get the previous day's temperature.
- Step-by-step breakdown of the solution: 
  1. For each row in the table, get the previous day's temperature for the same `id`.
  2. Compare the current day's temperature with the previous day's temperature.
  3. If the current day's temperature is higher, include the `id` in the result.

```cpp
SELECT w1.id 
FROM Weather w1 
JOIN Weather w2 
ON w1.id = w2.id 
AND w1.recordDate = w2.recordDate + INTERVAL 1 DAY 
WHERE w1.temperature > w2.temperature;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of rows in the table. This is because for each row, we are potentially joining with every other row.
> - **Space Complexity:** $O(n)$, as we need to store the joined rows.
> - **Why these complexities occur:** The join operation causes the time complexity to be quadratic, and the space complexity is linear because we need to store the joined rows.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a subquery or a window function to get the previous day's temperature for each `id`. This approach avoids the self-join and reduces the time complexity.
- Detailed breakdown of the approach: 
  1. Use a subquery or a window function to get the previous day's temperature for each `id`.
  2. Compare the current day's temperature with the previous day's temperature.
  3. If the current day's temperature is higher, include the `id` in the result.

```sql
SELECT w1.id 
FROM Weather w1 
WHERE w1.temperature > (SELECT w2.temperature 
                         FROM Weather w2 
                         WHERE w2.id = w1.id 
                         AND w2.recordDate = (SELECT MAX(recordDate) 
                                               FROM Weather w3 
                                               WHERE w3.id = w1.id 
                                               AND w3.recordDate < w1.recordDate));
```

Alternatively, using a window function:

```sql
SELECT id 
FROM (SELECT id, 
             temperature, 
             LAG(temperature) OVER (PARTITION BY id ORDER BY recordDate) AS prev_temp 
      FROM Weather) w 
WHERE temperature > prev_temp AND prev_temp IS NOT NULL;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of rows in the table. This is because we are using a window function or a subquery to get the previous day's temperature.
> - **Space Complexity:** $O(n)$, as we need to store the intermediate results.
> - **Optimality proof:** This is the optimal solution because we are avoiding the self-join and using a more efficient way to get the previous day's temperature.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Window functions, subqueries, and joins.
- Problem-solving patterns identified: Using window functions or subqueries to avoid self-joins and reduce time complexity.
- Optimization techniques learned: Avoiding self-joins and using more efficient ways to get the previous day's temperature.
- Similar problems to practice: Other problems that involve comparing rows with previous or next rows, such as finding the difference between consecutive rows.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to include the `id` in the join or subquery, or not handling the case where there is no previous day's temperature.
- Edge cases to watch for: Handling the case where there is no previous day's temperature, or where the `id` does not exist in the table.
- Performance pitfalls: Using self-joins or subqueries that are not optimized, leading to high time complexity.
- Testing considerations: Testing the query with different inputs and edge cases to ensure it is working correctly.