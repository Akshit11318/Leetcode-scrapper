## Maximum Number of Visible Points
**Problem Link:** https://leetcode.com/problems/maximum-number-of-visible-points/description

**Problem Statement:**
- Input format: You are given an array of points `locations` where `locations[i] = [x, y]` and an integer `k`.
- Constraints: `1 <= locations.length <= 10^5`, `0 <= x, y <= 10^6`, `1 <= k <= locations.length`.
- Expected output format: The maximum number of points that can be seen by looking in the same direction.
- Key requirements and edge cases to consider:
  - Points at the same location should be considered as one point.
  - Points with the same slope from the origin should be considered as visible in the same direction.
- Example test cases with explanations:
  - For `locations = [[2,1],[2,2],[3,3],[4,5],[1,5],[5,5]]` and `k = 3`, the maximum number of visible points is `5`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the slope of each point with respect to every other point and count the number of points that have the same slope.
- Step-by-step breakdown of the solution:
  1. Initialize a map to store the count of points for each slope.
  2. Iterate over each point and calculate its slope with respect to every other point.
  3. Increment the count for the slope in the map.
  4. Find the maximum count in the map.
- Why this approach comes to mind first: It's a straightforward approach to calculate the slope of each point with respect to every other point and count the number of points that have the same slope.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

int maxVisiblePoints(std::vector<std::vector<int>>& locations, int k) {
    int n = locations.size();
    int maxVisible = 0;
    for (int i = 0; i < n; i++) {
        std::unordered_map<double, int> slopeCount;
        int samePoint = 1;
        for (int j = 0; j < n; j++) {
            if (i == j) continue;
            double slope = locations[j][1] * 1.0 / locations[j][0] - locations[i][1] * 1.0 / locations[i][0];
            if (slope == 0) {
                slopeCount[0]++;
            } else {
                slopeCount[slope]++;
            }
            if (locations[i][0] == locations[j][0] && locations[i][1] == locations[j][1]) {
                samePoint++;
            }
        }
        int maxSlopeCount = 0;
        for (auto& pair : slopeCount) {
            maxSlopeCount = std::max(maxSlopeCount, pair.second);
        }
        maxVisible = std::max(maxVisible, maxSlopeCount + samePoint);
    }
    return std::min(maxVisible, k);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of locations. This is because we are iterating over each point and calculating its slope with respect to every other point.
> - **Space Complexity:** $O(n)$, where $n$ is the number of locations. This is because we are using a map to store the count of points for each slope.
> - **Why these complexities occur:** The time complexity is $O(n^2)$ because we are iterating over each point and calculating its slope with respect to every other point. The space complexity is $O(n)$ because we are using a map to store the count of points for each slope.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of calculating the slope of each point with respect to every other point, we can calculate the slope of each point with respect to the origin and use a map to store the count of points for each slope.
- Detailed breakdown of the approach:
  1. Initialize a map to store the count of points for each slope.
  2. Iterate over each point and calculate its slope with respect to the origin.
  3. Increment the count for the slope in the map.
  4. Find the maximum count in the map.
- Proof of optimality: This approach is optimal because we are only iterating over each point once and using a map to store the count of points for each slope, which reduces the time complexity to $O(n)$.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

int maxVisiblePoints(std::vector<std::vector<int>>& locations, int k) {
    int n = locations.size();
    int maxVisible = 0;
    for (int i = 0; i < n; i++) {
        std::unordered_map<double, int> slopeCount;
        int samePoint = 1;
        for (int j = 0; j < n; j++) {
            if (i == j) continue;
            double slope = locations[j][1] * 1.0 / locations[j][0];
            if (locations[j][0] == 0) {
                slope = INT_MAX;
            }
            slopeCount[slope]++;
            if (locations[i][0] == locations[j][0] && locations[i][1] == locations[j][1]) {
                samePoint++;
            }
        }
        int maxSlopeCount = 0;
        for (auto& pair : slopeCount) {
            maxSlopeCount = std::max(maxSlopeCount, pair.second);
        }
        maxVisible = std::max(maxVisible, maxSlopeCount + samePoint);
    }
    return std::min(maxVisible, k);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of locations. This is because we are iterating over each point and calculating its slope with respect to the origin.
> - **Space Complexity:** $O(n)$, where $n$ is the number of locations. This is because we are using a map to store the count of points for each slope.
> - **Optimality proof:** This approach is optimal because we are only iterating over each point once and using a map to store the count of points for each slope, which reduces the time complexity to $O(n^2)$.

However, we can further optimize the solution using a technique called **hashing**. We can use a hashmap to store the count of points for each slope.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

int maxVisiblePoints(std::vector<std::vector<int>>& locations, int k) {
    int n = locations.size();
    int maxVisible = 0;
    for (int i = 0; i < n; i++) {
        std::unordered_map<std::pair<int, int>, int> slopeCount;
        int samePoint = 1;
        for (int j = 0; j < n; j++) {
            if (i == j) continue;
            int dx = locations[j][0] - locations[i][0];
            int dy = locations[j][1] - locations[i][1];
            int gcd = std::__gcd(dx, dy);
            dx /= gcd;
            dy /= gcd;
            slopeCount[{dx, dy}]++;
            if (locations[i][0] == locations[j][0] && locations[i][1] == locations[j][1]) {
                samePoint++;
            }
        }
        int maxSlopeCount = 0;
        for (auto& pair : slopeCount) {
            maxSlopeCount = std::max(maxSlopeCount, pair.second);
        }
        maxVisible = std::max(maxVisible, maxSlopeCount + samePoint);
    }
    return std::min(maxVisible, k);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of locations. This is because we are iterating over each point and calculating its slope with respect to the origin.
> - **Space Complexity:** $O(n)$, where $n$ is the number of locations. This is because we are using a map to store the count of points for each slope.
> - **Optimality proof:** This approach is optimal because we are only iterating over each point once and using a map to store the count of points for each slope, which reduces the time complexity to $O(n^2)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: **hashing**, **gcd**, **slope calculation**.
- Problem-solving patterns identified: **iterating over each point**, **using a map to store the count of points for each slope**.
- Optimization techniques learned: **using a hashmap to store the count of points for each slope**, **calculating the gcd of two numbers**.
- Similar problems to practice: **[Maximum Number of Points with the Same Slope](https://leetcode.com/problems/max-points-on-a-line/)**.

**Mistakes to Avoid:**
- Common implementation errors: **not handling the case where the denominator is zero**, **not using a hashmap to store the count of points for each slope**.
- Edge cases to watch for: **points with the same coordinates**, **points with the same slope**.
- Performance pitfalls: **not using a hashmap to store the count of points for each slope**, **not calculating the gcd of two numbers**.
- Testing considerations: **testing with different inputs**, **testing with edge cases**.