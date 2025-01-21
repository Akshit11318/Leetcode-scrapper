## Countries You Can Safely Invest In
**Problem Link:** https://leetcode.com/problems/countries-you-can-safely-invest-in/description

**Problem Statement:**
- Input format and constraints: The problem requires finding countries where the average population in 2020 is greater than or equal to the average population in 2021, from a given table `population` with columns `id`, `country_code`, and `year`.
- Expected output format: A table with the `country_code` of countries where the average population in 2020 is greater than or equal to the average population in 2021.
- Key requirements and edge cases to consider: Handling cases where there might be no population data for a country in either 2020 or 2021.
- Example test cases with explanations: For instance, if a country has a population of 1000 in 2020 and 900 in 2021, it should be included in the result because its average population in 2020 is greater than or equal to its average population in 2021.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The first approach that comes to mind is to calculate the average population for each country in both 2020 and 2021 and then compare these averages.
- Step-by-step breakdown of the solution:
  1. Group the population data by `country_code`.
  2. For each group (country), filter the data to get populations for 2020 and 2021 separately.
  3. Calculate the average population for each year for each country.
  4. Compare the average populations for 2020 and 2021 for each country.
- Why this approach comes to mind first: It directly addresses the problem statement by calculating and comparing the required averages.

```cpp
SELECT country_code
FROM (
  SELECT country_code,
         AVG(CASE WHEN year = 2020 THEN population END) AS avg_2020,
         AVG(CASE WHEN year = 2021 THEN population END) AS avg_2021
  FROM population
  GROUP BY country_code
) AS subquery
WHERE avg_2020 >= avg_2021;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the `population` table, because we're performing a constant amount of work for each row.
> - **Space Complexity:** $O(n)$, because in the worst case, we might need to store all rows in the subquery result.
> - **Why these complexities occur:** The time complexity is linear because we process each row once, and the space complexity is linear because we store the results for each country.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The same insight as the brute force approach, but recognizing that the SQL query can be optimized by directly filtering and comparing within a single query without needing to store intermediate results.
- Detailed breakdown of the approach:
  1. Use conditional aggregation to calculate the average population for 2020 and 2021 for each country.
  2. Use a `WHERE` clause to filter the results to include only countries where the average population in 2020 is greater than or equal to the average population in 2021.
- Proof of optimality: This approach is optimal because it minimizes the amount of data that needs to be processed and stored, directly calculating the required averages and comparisons in a single pass.
- Why further optimization is impossible: Further optimization is impossible because we must at least read the input data once to solve the problem, and this approach does so in a single pass.

```cpp
SELECT country_code
FROM population
GROUP BY country_code
HAVING AVG(CASE WHEN year = 2020 THEN population END) >= AVG(CASE WHEN year = 2021 THEN population END);
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the `population` table, because we process each row once.
> - **Space Complexity:** $O(1)$, because we only store a constant amount of information for each group (country), regardless of the input size.
> - **Optimality proof:** This is the most efficient solution because it achieves the required comparison with a single pass through the data, minimizing both time and space complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Conditional aggregation, filtering, and comparison in SQL.
- Problem-solving patterns identified: Direct calculation and comparison can often lead to more efficient solutions.
- Optimization techniques learned: Minimizing the amount of data stored and processed can significantly improve performance.
- Similar problems to practice: Other problems involving aggregation, filtering, and comparison in SQL.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly specifying the `GROUP BY` or `HAVING` clauses.
- Edge cases to watch for: Countries with no population data in either 2020 or 2021.
- Performance pitfalls: Using subqueries or temporary tables unnecessarily.
- Testing considerations: Ensure that the solution works correctly for countries with varying numbers of population records in 2020 and 2021.