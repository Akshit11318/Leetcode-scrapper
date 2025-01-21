## Find Cities in Each State
**Problem Link:** https://leetcode.com/problems/find-cities-in-each-state/description

**Problem Statement:**
- Input format and constraints: The problem takes a list of `cities` where each city is represented by a unique `city_id`, a `state_id`, and a `name`. The goal is to find all cities in each state and return them as a list of lists, where each sublist contains the names of cities in a particular state, sorted in ascending order.
- Expected output format: A list of lists, where each sublist contains city names.
- Key requirements and edge cases to consider: Handling cases where there are no cities in a state, or where there are multiple cities with the same name but in different states.
- Example test cases with explanations:
  - Example 1: Input: `cities = [["1","1","City A"],["2","1","City B"],["3","2","City C"]]`, Expected Output: `[["City A","City B"],["City C"]]`
  - Example 2: Input: `cities = [["1","1","City A"],["2","2","City B"],["3","3","City C"]]`, Expected Output: `[["City A"],["City B"],["City C"]]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this, we need to group cities by their `state_id` and then sort the city names within each group.
- Step-by-step breakdown of the solution:
  1. Create a dictionary where the keys are `state_id`s and the values are lists of city names.
  2. Iterate through each city in the input list.
  3. For each city, append its name to the list of the corresponding `state_id` in the dictionary.
  4. Sort the list of city names for each `state_id`.
  5. Convert the dictionary values into a list of lists and return it.

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

vector<vector<string>> findCities(vector<vector<string>>& cities) {
    map<string, vector<string>> stateCities;
    for (auto& city : cities) {
        stateCities[city[1]].push_back(city[2]);
    }
    
    for (auto& pair : stateCities) {
        sort(pair.second.begin(), pair.second.end());
    }
    
    vector<vector<string>> result;
    for (auto& pair : stateCities) {
        result.push_back(pair.second);
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the total number of cities. This is because for each state, we sort the list of its cities, and the sorting operation dominates the complexity.
> - **Space Complexity:** $O(n)$, as in the worst case, we might end up storing all cities in the dictionary.
> - **Why these complexities occur:** The sorting operation for each state contributes to the time complexity, and storing all cities in the dictionary contributes to the space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved more efficiently by utilizing a `map` to group cities by their `state_id` and then sorting the city names for each state in a single pass.
- Detailed breakdown of the approach:
  1. Create a `map` where the keys are `state_id`s and the values are vectors of city names.
  2. Iterate through the input list of cities, grouping them by their `state_id` in the `map`.
  3. For each group of cities (i.e., for each `state_id`), sort the vector of city names.
  4. Convert the `map` values into a list of lists, ensuring each list is sorted.
- Proof of optimality: This approach is optimal because it minimizes the number of operations required to group and sort the cities. It uses a single pass through the input data and sorts each group of cities only once.

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

vector<vector<string>> findCities(vector<vector<string>>& cities) {
    map<string, vector<string>> stateCities;
    for (auto& city : cities) {
        stateCities[city[1]].push_back(city[2]);
    }
    
    for (auto& pair : stateCities) {
        sort(pair.second.begin(), pair.second.end());
    }
    
    vector<vector<string>> result;
    for (auto& pair : stateCities) {
        result.push_back(pair.second);
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the total number of cities. This is because for each state, we sort the list of its cities.
> - **Space Complexity:** $O(n)$, as in the worst case, we might end up storing all cities in the `map`.
> - **Optimality proof:** This is the optimal solution because it achieves the grouping and sorting in a single pass through the data, with the minimum necessary operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Grouping data by a key and sorting within groups.
- Problem-solving patterns identified: Utilizing `map` for efficient grouping and sorting for ordering.
- Optimization techniques learned: Minimizing the number of passes through the data and using built-in sorting functions for efficiency.
- Similar problems to practice: Other grouping and sorting problems, such as grouping people by age and then sorting them by name.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly using `map` or failing to sort the groups.
- Edge cases to watch for: Handling empty input or input with duplicate city names.
- Performance pitfalls: Using inefficient sorting algorithms or making unnecessary passes through the data.
- Testing considerations: Ensuring to test with various input sizes and edge cases.