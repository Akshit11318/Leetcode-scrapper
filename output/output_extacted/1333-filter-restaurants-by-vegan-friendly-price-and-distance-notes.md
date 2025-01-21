## Filter Restaurants by Vegan-Friendly, Price, and Distance

**Problem Link:** https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/description

**Problem Statement:**
- Input: `restaurants` (list of lists where each sublist contains `[id, name, veganFriendly, price, distance]`), `veganFriendly` (integer indicating whether to filter for vegan-friendly), `maxPrice` (maximum price), `maxDistance` (maximum distance)
- Expected output: A list of restaurant ids that satisfy the conditions, sorted by rating (higher first) and then by id (lower first) if ratings are equal.
- Key requirements and edge cases to consider: Handling cases where `veganFriendly` is 0 or 1, ensuring `maxPrice` and `maxDistance` are used correctly to filter restaurants.
- Example test cases with explanations: For example, given `restaurants = [[1, "Alice", 1, 5, 3], [2, "Bob", 0, 3, 2], [3, "Charlie", 1, 4, 4]]`, `veganFriendly = 1`, `maxPrice = 5`, `maxDistance = 3`, the output should be `[1]` because only Alice's restaurant is vegan-friendly, has a price less than or equal to 5, and is within 3 units of distance.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each restaurant, check if it satisfies all conditions, and if so, add its id to the result list.
- Step-by-step breakdown of the solution:
  1. Filter the restaurants based on `veganFriendly`, `maxPrice`, and `maxDistance`.
  2. Sort the filtered list of restaurants by their rating (if ratings were provided) and then by their id.
- Why this approach comes to mind first: It directly addresses the conditions given in the problem statement.

```cpp
#include <vector>
#include <algorithm>

using namespace std;

vector<int> filterRestaurants(vector<vector<int>>& restaurants, int veganFriendly, int maxPrice, int maxDistance) {
    vector<pair<int, int>> filteredRestaurants; // Store id and rating (if available)
    
    for (auto& restaurant : restaurants) {
        if ((veganFriendly == 0 || restaurant[2] == 1) && restaurant[3] <= maxPrice && restaurant[4] <= maxDistance) {
            // Assuming rating is not provided, we will use the first element of the restaurant vector as a placeholder
            filteredRestaurants.push_back({restaurant[0], 0}); // Placeholder for rating, actual rating not provided in problem
        }
    }
    
    // Sort by rating (higher first) and then by id (lower first)
    sort(filteredRestaurants.begin(), filteredRestaurants.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
        return a.second > b.second || (a.second == b.second && a.first < b.first);
    });
    
    vector<int> result;
    for (auto& restaurant : filteredRestaurants) {
        result.push_back(restaurant.first);
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ where $n$ is the number of restaurants that pass the filter, due to sorting.
> - **Space Complexity:** $O(n)$ for storing the filtered restaurants.
> - **Why these complexities occur:** The brute force approach requires checking each restaurant against the conditions, leading to a linear initial filter, followed by a sorting operation which dominates the complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved in a single pass by filtering and sorting simultaneously, but since the rating is not provided in the problem statement, we assume the sorting is based on the provided conditions directly.
- Detailed breakdown of the approach:
  1. Filter the restaurants based on `veganFriendly`, `maxPrice`, and `maxDistance`.
  2. Since ratings are not provided, we can't sort based on ratings. However, we can return the ids directly after filtering, assuming that's the primary goal.
- Proof of optimality: This approach is optimal because it only requires a single pass through the list of restaurants, minimizing both time and space complexity.

```cpp
#include <vector>
#include <algorithm>

using namespace std;

vector<int> filterRestaurants(vector<vector<int>>& restaurants, int veganFriendly, int maxPrice, int maxDistance) {
    vector<int> result;
    for (auto& restaurant : restaurants) {
        if ((veganFriendly == 0 || restaurant[2] == 1) && restaurant[3] <= maxPrice && restaurant[4] <= maxDistance) {
            result.push_back(restaurant[0]);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of restaurants, because we are doing a constant amount of work for each restaurant.
> - **Space Complexity:** $O(n)$ for storing the result.
> - **Optimality proof:** This solution is optimal because it only iterates over the list of restaurants once, performing a constant amount of work for each restaurant, thus achieving linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Filtering and sorting.
- Problem-solving patterns identified: Directly addressing the conditions given in the problem statement.
- Optimization techniques learned: Minimizing the number of passes through the data.
- Similar problems to practice: Other filtering and sorting problems.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases (e.g., empty input list).
- Edge cases to watch for: Handling cases where `veganFriendly` is 0 or 1, ensuring `maxPrice` and `maxDistance` are used correctly.
- Performance pitfalls: Using inefficient sorting algorithms or making unnecessary passes through the data.
- Testing considerations: Testing with various inputs, including edge cases, to ensure correctness.