## Year on Year Growth Rate
**Problem Link:** https://leetcode.com/problems/year-on-year-growth-rate/description

**Problem Statement:**
- Input format and constraints: Given a table `growth` with columns `id`, `year`, and `value`, calculate the year-on-year growth rate for each `id`.
- Expected output format: A table with `id` and `growth` columns.
- Key requirements and edge cases to consider: Handle cases where an `id` has no previous year's data.
- Example test cases with explanations:
    - For an `id` with consecutive years, calculate the growth rate as `(current_year_value - previous_year_value) / previous_year_value`.
    - For an `id` without consecutive years, do not calculate the growth rate for the first year.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each row in the table, and for each `id`, find the previous year's value to calculate the growth rate.
- Step-by-step breakdown of the solution:
    1. Sort the table by `id` and `year`.
    2. Iterate over each row in the sorted table.
    3. For each row, find the previous year's value for the same `id`.
    4. Calculate the growth rate using the formula `(current_year_value - previous_year_value) / previous_year_value`.
- Why this approach comes to mind first: It directly implements the definition of year-on-year growth rate.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

struct Growth {
    int id;
    int year;
    double value;
};

// Function to calculate year-on-year growth rate
std::vector<std::pair<int, double>> calculateGrowthRate(std::vector<Growth>& growth) {
    // Sort the table by id and year
    std::sort(growth.begin(), growth.end(), [](const Growth& a, const Growth& b) {
        if (a.id == b.id) {
            return a.year < b.year;
        }
        return a.id < b.id;
    });

    std::vector<std::pair<int, double>> result;
    for (int i = 0; i < growth.size(); ++i) {
        // Find the previous year's value for the same id
        double prevValue = -1.0;
        for (int j = i - 1; j >= 0; --j) {
            if (growth[j].id == growth[i].id && growth[j].year == growth[i].year - 1) {
                prevValue = growth[j].value;
                break;
            }
        }

        // Calculate the growth rate
        if (prevValue != -1.0) {
            double growthRate = (growth[i].value - prevValue) / prevValue;
            result.push_back({growth[i].id, growthRate});
        }
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of rows in the table. This is because for each row, we potentially iterate over all previous rows to find the previous year's value.
> - **Space Complexity:** $O(n)$, as we store the result in a vector of pairs.
> - **Why these complexities occur:** The nested loop structure leads to the quadratic time complexity, while the space complexity is linear due to the storage of the result.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a hash map to store the previous year's value for each `id`, allowing for constant time lookup.
- Detailed breakdown of the approach:
    1. Sort the table by `id` and `year`.
    2. Iterate over each row in the sorted table.
    3. For each row, use the hash map to find the previous year's value for the same `id`.
    4. Calculate the growth rate using the formula `(current_year_value - previous_year_value) / previous_year_value`.
- Proof of optimality: This approach minimizes the time complexity by avoiding the need for nested loops.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>

struct Growth {
    int id;
    int year;
    double value;
};

// Function to calculate year-on-year growth rate
std::vector<std::pair<int, double>> calculateGrowthRate(std::vector<Growth>& growth) {
    // Sort the table by id and year
    std::sort(growth.begin(), growth.end(), [](const Growth& a, const Growth& b) {
        if (a.id == b.id) {
            return a.year < b.year;
        }
        return a.id < b.id;
    });

    std::unordered_map<int, double> prevValues;
    std::vector<std::pair<int, double>> result;
    for (const auto& g : growth) {
        // Check if we have the previous year's value
        if (prevValues.find(g.id) != prevValues.end()) {
            double growthRate = (g.value - prevValues[g.id]) / prevValues[g.id];
            result.push_back({g.id, growthRate});
        }

        // Update the previous year's value for the current id
        prevValues[g.id] = g.value;
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of rows in the table. This is because we sort the table first, and then iterate over it once.
> - **Space Complexity:** $O(n)$, as we store the result and use a hash map to store the previous year's values.
> - **Optimality proof:** This approach is optimal because it minimizes the time complexity by avoiding nested loops and using a hash map for constant time lookup.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, hash maps, and iteration.
- Problem-solving patterns identified: Using hash maps to store and look up values efficiently.
- Optimization techniques learned: Minimizing time complexity by avoiding nested loops and using efficient data structures.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as missing previous year's values.
- Edge cases to watch for: Handling cases where an `id` has no previous year's data.
- Performance pitfalls: Using inefficient data structures or algorithms, leading to high time complexity.
- Testing considerations: Thoroughly testing the implementation with various input scenarios to ensure correctness.