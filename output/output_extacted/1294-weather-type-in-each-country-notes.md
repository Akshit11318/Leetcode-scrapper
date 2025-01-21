## Weather Type in Each Country

**Problem Link:** https://leetcode.com/problems/weather-type-in-each-country/description

**Problem Statement:**
- The input consists of two tables: `Country` and `Weather`.
- The `Country` table has columns `id` and `country_name`.
- The `Weather` table has columns `id`, `country_id`, and `weather_state`.
- The task is to find the type of weather in each country.
- The expected output should include the country name and the corresponding weather type.
- Key requirements include handling different weather states and country names.
- Example test cases will demonstrate how to match weather states with country names.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves iterating through each row in the `Weather` table to find the corresponding country name in the `Country` table.
- For each match, we would then determine the weather type based on the `weather_state` value.
- This approach comes to mind first because it directly addresses the requirement of matching weather states with country names.

```cpp
SELECT 
    c.country_name, 
    CASE 
        WHEN w.weather_state = 'Sunny' THEN 'Sunny'
        WHEN w.weather_state = 'Rainy' THEN 'Rainy'
        WHEN w.weather_state = 'Cloudy' THEN 'Cloudy'
        ELSE 'Unknown'
    END AS weather_type
FROM 
    Weather w
JOIN 
    Country c ON w.country_id = c.id;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the `Weather` table, because we are performing a constant amount of work for each row.
> - **Space Complexity:** $O(n)$, because in the worst-case scenario, we might need to store all rows in the result set.
> - **Why these complexities occur:** These complexities occur because we are iterating through each row in the `Weather` table and performing a join operation with the `Country` table.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is recognizing that we can use a `JOIN` operation to combine the `Weather` and `Country` tables based on the `country_id`.
- We then use a `CASE` statement to determine the weather type based on the `weather_state` value.
- This approach is optimal because it directly addresses the requirement of matching weather states with country names in a single query.

```cpp
SELECT 
    c.country_name, 
    CASE 
        WHEN w.weather_state = 'Sunny' THEN 'Sunny'
        WHEN w.weather_state = 'Rainy' THEN 'Rainy'
        WHEN w.weather_state = 'Cloudy' THEN 'Cloudy'
        ELSE 'Unknown'
    END AS weather_type
FROM 
    Weather w
JOIN 
    Country c ON w.country_id = c.id;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the `Weather` table, because we are performing a constant amount of work for each row.
> - **Space Complexity:** $O(n)$, because in the worst-case scenario, we might need to store all rows in the result set.
> - **Optimality proof:** This approach is optimal because it uses a single query to combine the tables and determine the weather type, resulting in the minimum possible time and space complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated include using `JOIN` operations to combine tables and `CASE` statements to determine values based on conditions.
- Problem-solving patterns identified include recognizing the need to combine tables based on a common column and using conditional statements to determine values.
- Optimization techniques learned include using a single query to combine tables and determine values, resulting in minimum time and space complexity.
- Similar problems to practice include other SQL queries that involve combining tables and determining values based on conditions.

**Mistakes to Avoid:**
- Common implementation errors include using incorrect `JOIN` operations or conditional statements.
- Edge cases to watch for include handling `NULL` or unknown values in the `weather_state` column.
- Performance pitfalls include using subqueries or multiple queries instead of a single query to combine tables and determine values.
- Testing considerations include verifying that the query returns the correct results for different input scenarios.