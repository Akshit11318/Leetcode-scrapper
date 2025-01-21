## Find Cities in Each State II
**Problem Link:** https://leetcode.com/problems/find-cities-in-each-state-ii/description

**Problem Statement:**
- Input format and constraints: The problem provides a table `City`, which contains columns `id`, `name`, `state_id`, and `capital`, where `id` is the unique identifier for each city, `name` is the name of the city, `state_id` represents the state to which the city belongs, and `capital` indicates whether the city is a capital (`1`) or not (`0`). The task is to find all capital cities in each state.
- Expected output format: The output should be a list of city names, which are capitals of their respective states, sorted by the state's `id`.
- Key requirements and edge cases to consider:
  - A city can only be the capital of one state.
  - There might be states without capital cities.
- Example test cases with explanations:
  - For example, given the table:
    ```markdown
    +----+----------+---------+--------+
    | id | name     | state_id | capital |
    +----+----------+---------+--------+
    | 1  | New York | 21      | 1      |
    | 2  | Los Angeles | 21    | 0      |
    | 3  | Chicago  | 22      | 1      |
    +----+----------+---------+--------+
    ```
    The expected output would be:
    ```markdown
    +----------+
    | name     |
    +----------+
    | New York |
    | Chicago  |
    +----------+
    ```

### Brute Force Approach
**Explanation:**
- Initial thought process: To solve this problem, we first need to identify which cities are capitals. Then, we need to ensure these cities are grouped by their state and sorted accordingly.
- Step-by-step breakdown of the solution:
  1. Iterate through the `City` table to identify capital cities (where `capital = 1`).
  2. For each capital city, retrieve its `state_id`.
  3. Sort the capital cities by their `state_id`.
- Why this approach comes to mind first: This approach is straightforward and involves basic database operations like filtering and sorting.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

struct City {
    int id;
    std::string name;
    int state_id;
    int capital;
};

std::vector<std::string> findCapitalCities(std::vector<City>& cities) {
    std::vector<std::string> capitalCities;
    
    // Filter capital cities
    for (const auto& city : cities) {
        if (city.capital == 1) {
            capitalCities.push_back(city.name);
        }
    }
    
    // Sort by state_id (assuming state_id is available for sorting)
    // Note: This step requires additional information about state_id for sorting.
    // For simplicity, assume we have a way to map city names to their state_id.
    std::sort(capitalCities.begin(), capitalCities.end(), [](const std::string& a, const std::string& b) {
        // Hypothetical function to get state_id from city name
        return getStateId(a) < getStateId(b);
    });
    
    return capitalCities;
}

// Hypothetical function to get state_id from city name
int getStateId(const std::string& cityName) {
    // Implementation depends on actual data structure and database schema
    // For demonstration purposes, assume a direct mapping is available
    // In real scenarios, this could involve a database query or lookup in a data structure
}

```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation, where $n$ is the number of capital cities.
> - **Space Complexity:** $O(n)$ for storing the capital cities.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, and storing the capital cities requires additional space.

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Utilize SQL queries to directly filter and sort the cities from the database, leveraging the database's efficiency in handling data.
- Detailed breakdown of the approach:
  1. Use a SQL `SELECT` statement to filter cities where `capital = 1`.
  2. Use the `ORDER BY` clause to sort the results by `state_id`.
- Proof of optimality: This approach is optimal because it minimizes the amount of data transferred and processed, leveraging the database's capabilities for filtering and sorting.

```sql
SELECT name
FROM City
WHERE capital = 1
ORDER BY state_id;
```

> Complexity Analysis:
> - **Time Complexity:** This depends on the database's efficiency and indexing but is generally $O(n \log n)$ for sorting, where $n$ is the number of rows in the result set.
> - **Space Complexity:** Minimal, as the database handles the data internally.
> - **Optimality proof:** The direct use of database queries minimizes unnecessary data processing and transfer, making it the most efficient approach for this problem.

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Filtering and sorting.
- Problem-solving patterns identified: Leveraging the strengths of the tools at hand (in this case, database queries).
- Optimization techniques learned: Minimizing data transfer and processing by utilizing database capabilities.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly assuming the availability of certain data or functionality.
- Edge cases to watch for: States without capital cities, duplicate capital designations.
- Performance pitfalls: Transferring unnecessary data or performing operations that could be handled more efficiently by the database.
- Testing considerations: Ensure coverage of various scenarios, including edge cases and performance tests under different data volumes.