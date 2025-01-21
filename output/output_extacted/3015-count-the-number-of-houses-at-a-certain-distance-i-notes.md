## Count the Number of Houses at a Certain Distance I

**Problem Link:** https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/description

**Problem Statement:**
- Input format: `houses` and `heaters` are arrays of integers representing house and heater positions.
- Constraints: $1 \leq houses.length, heaters.length \leq 10^5$, $1 \leq houses[i], heaters[i] \leq 10^9$.
- Expected output: An integer array where each element is the number of houses that are at a certain distance from a heater.
- Key requirements: For each house, find the closest heater and calculate the distance.
- Edge cases: Consider cases where a house has two closest heaters at the same distance.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves iterating over each house and for each house, iterating over all heaters to find the closest one.
- This approach involves calculating the distance between each house and every heater, which leads to a high time complexity.
- Step-by-step breakdown:
  1. Iterate over each house.
  2. For each house, iterate over all heaters.
  3. Calculate the distance between the house and the current heater.
  4. Update the minimum distance if a closer heater is found.
  5. After finding the closest heater for a house, increment the count for that distance.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> countHouses(vector<int>& houses, vector<int>& heaters) {
    vector<int> distances(houses.size(), 0);
    for (int i = 0; i < houses.size(); i++) {
        int minDistance = INT_MAX;
        for (int j = 0; j < heaters.size(); j++) {
            int distance = abs(houses[i] - heaters[j]);
            minDistance = min(minDistance, distance);
        }
        distances[i] = minDistance;
    }
    return distances;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of houses and $m$ is the number of heaters. This is because for each house, we are iterating over all heaters.
> - **Space Complexity:** $O(n)$ for storing the distances of houses from their closest heaters.
> - **Why these complexities occur:** The brute force approach involves nested loops over houses and heaters, leading to high time complexity. The space complexity is linear because we only need to store the distances for each house.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to sort both houses and heaters arrays and then use two pointers to find the closest heater for each house efficiently.
- This approach takes advantage of the fact that if a house is closer to a heater than another house, it will also be closer to the next heater if the heaters are sorted.
- Step-by-step breakdown:
  1. Sort both houses and heaters arrays.
  2. Initialize two pointers, one for houses and one for heaters.
  3. For each house, move the heater pointer until we find the closest heater or until we reach a heater that is farther than the current one.
  4. Calculate the distance between the house and its closest heater.
  5. Store the count of houses at each distance.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> countHouses(vector<int>& houses, vector<int>& heaters) {
    sort(houses.begin(), houses.end());
    sort(heaters.begin(), heaters.end());
    vector<int> distances(houses.size(), 0);
    int heaterIndex = 0;
    for (int i = 0; i < houses.size(); i++) {
        while (heaterIndex < heaters.size() - 1 && abs(houses[i] - heaters[heaterIndex + 1]) <= abs(houses[i] - heaters[heaterIndex])) {
            heaterIndex++;
        }
        distances[i] = abs(houses[i] - heaters[heaterIndex]);
    }
    return distances;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n + m \log m)$ due to sorting houses and heaters. The subsequent loop is $O(n + m)$ but dominated by the sorting.
> - **Space Complexity:** $O(n)$ for storing the distances of houses from their closest heaters.
> - **Optimality proof:** This approach is optimal because it minimizes the number of comparisons needed to find the closest heater for each house by leveraging the sorted order of both arrays.

---

### Final Notes

**Learning Points:**
- The importance of sorting in reducing the complexity of problems.
- Using two pointers to efficiently traverse two sorted arrays.
- The trade-off between time and space complexity in algorithm design.

**Mistakes to Avoid:**
- Not considering the impact of sorting on the overall time complexity.
- Failing to initialize pointers or variables correctly.
- Not handling edge cases, such as when a house has two closest heaters at the same distance.