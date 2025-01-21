## Find Expensive Cities
**Problem Link:** https://leetcode.com/problems/find-expensive-cities/description

**Problem Statement:**
- Input format and constraints: The problem requires finding cities with costs greater than or equal to the average cost of all cities, given a table `Cities` with columns `City`, `Cost`.
- Expected output format: The output should include the `City` and `Cost` for each city that meets the condition, ordered by `Cost` in descending order.
- Key requirements and edge cases to consider: Handling cases where the average cost is zero, or when there are no cities that meet the condition.
- Example test cases with explanations: 
    - Example 1: Given a table with cities and their costs, find the cities where the cost is greater than or equal to the average cost.
    - Example 2: Handle the case when the average cost is zero.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the average cost of all cities, then iterate through each city to find those with costs greater than or equal to the average.
- Step-by-step breakdown of the solution:
    1. Calculate the sum of costs of all cities.
    2. Calculate the average cost by dividing the sum of costs by the number of cities.
    3. Iterate through each city and check if its cost is greater than or equal to the average cost.
- Why this approach comes to mind first: It directly addresses the problem statement by calculating the average cost and then comparing each city's cost against it.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

struct City {
    std::string name;
    int cost;
};

std::vector<City> findExpensiveCities(std::vector<City>& cities) {
    int sumCost = 0;
    for (const auto& city : cities) {
        sumCost += city.cost;
    }
    double avgCost = (double)sumCost / cities.size();

    std::vector<City> expensiveCities;
    for (const auto& city : cities) {
        if (city.cost >= avgCost) {
            expensiveCities.push_back(city);
        }
    }

    // Sort expensive cities by cost in descending order
    std::sort(expensiveCities.begin(), expensiveCities.end(), [](const City& a, const City& b) {
        return a.cost > b.cost;
    });

    return expensiveCities;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ for calculating the sum of costs, $O(n)$ for finding expensive cities, and $O(n \log n)$ for sorting, where $n$ is the number of cities. Thus, the overall time complexity is $O(n) + O(n) + O(n \log n) = O(n \log n)$.
> - **Space Complexity:** $O(n)$ for storing the expensive cities.
> - **Why these complexities occur:** The time complexity is dominated by the sorting operation, which is necessary to order the expensive cities by their costs in descending order.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved in a single pass through the data by using SQL or a similar query language that allows for aggregation and filtering operations.
- Detailed breakdown of the approach:
    1. Calculate the average cost of all cities using an aggregation function.
    2. Use a filtering condition to select cities where the cost is greater than or equal to the average cost.
- Proof of optimality: This approach is optimal because it minimizes the number of passes through the data and uses efficient aggregation and filtering operations.
- Why further optimization is impossible: Any further optimization would require reducing the number of operations or the amount of data processed, which is not possible given the problem constraints.

```cpp
// Assuming a SQL-like query language
SELECT City, Cost
FROM Cities
WHERE Cost >= (SELECT AVG(Cost) FROM Cities)
ORDER BY Cost DESC;
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ for calculating the average cost and $O(n)$ for filtering and sorting the cities, where $n$ is the number of cities. Thus, the overall time complexity is $O(n) + O(n) = O(n)$.
> - **Space Complexity:** $O(n)$ for storing the filtered cities.
> - **Optimality proof:** The time complexity is optimal because it only requires a single pass through the data to calculate the average cost and filter the cities.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Aggregation, filtering, and sorting.
- Problem-solving patterns identified: Using a single pass through the data to minimize operations.
- Optimization techniques learned: Minimizing the number of passes through the data and using efficient aggregation and filtering operations.
- Similar problems to practice: Other problems involving data aggregation, filtering, and sorting.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty dataset or a dataset with a single element.
- Edge cases to watch for: Handling cases where the average cost is zero or when there are no cities that meet the condition.
- Performance pitfalls: Not optimizing the query to minimize the number of passes through the data.
- Testing considerations: Testing the query with different datasets to ensure correctness and performance.