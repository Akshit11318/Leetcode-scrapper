## Heaters
**Problem Link:** https://leetcode.com/problems/heaters/description

**Problem Statement:**
- Input format and constraints: Given a list of houses and a list of heaters, return the minimum radius that can cover all houses.
- Expected output format: A single integer representing the minimum radius.
- Key requirements and edge cases to consider: 
  - Each house can be covered by multiple heaters, but we are interested in the minimum radius that can cover all houses.
  - A house is covered if the distance between the house and a heater is less than or equal to the radius.
- Example test cases with explanations: 
  - Input: houses = [1,2,3], heaters = [2]
    Output: 1
    Explanation: Place the only heater in the position 2. Now: 
    1. The distance between the first house and the heater is |1-2| = 1.
    2. The distance between the second house and the heater is |2-2| = 0.
    3. The distance between the third house and the heater is |3-2| = 1.
    So the radius of the heater should be 1.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each possible radius from 0 to the maximum distance between a house and a heater, check if all houses can be covered.
- Step-by-step breakdown of the solution: 
  1. Calculate the maximum distance between a house and a heater.
  2. Iterate over each possible radius from 0 to the maximum distance.
  3. For each radius, check if all houses can be covered by any heater with the current radius.
  4. If all houses can be covered, return the current radius.
- Why this approach comes to mind first: It is a straightforward approach that checks all possible scenarios.

```cpp
class Solution {
public:
    int findRadius(vector<int>& houses, vector<int>& heaters) {
        sort(houses.begin(), houses.end());
        sort(heaters.begin(), heaters.end());
        int maxDistance = 0;
        for (int house : houses) {
            for (int heater : heaters) {
                maxDistance = max(maxDistance, abs(house - heater));
            }
        }
        for (int radius = 0; radius <= maxDistance; radius++) {
            bool covered = true;
            for (int house : houses) {
                bool houseCovered = false;
                for (int heater : heaters) {
                    if (abs(house - heater) <= radius) {
                        houseCovered = true;
                        break;
                    }
                }
                if (!houseCovered) {
                    covered = false;
                    break;
                }
            }
            if (covered) {
                return radius;
            }
        }
        return -1; // This should not happen
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m \cdot d)$, where $n$ is the number of houses, $m$ is the number of heaters, and $d$ is the maximum distance between a house and a heater.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input.
> - **Why these complexities occur:** The time complexity is due to the nested loops that iterate over all possible radii and all houses and heaters.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a binary search approach to find the minimum radius that covers all houses.
- Detailed breakdown of the approach: 
  1. Sort the houses and heaters.
  2. Use binary search to find the minimum radius that covers all houses.
  3. For each radius, check if all houses can be covered by any heater with the current radius.
- Proof of optimality: This approach is optimal because it uses binary search to reduce the number of iterations.

```cpp
class Solution {
public:
    int findRadius(vector<int>& houses, vector<int>& heaters) {
        sort(houses.begin(), houses.end());
        sort(heaters.begin(), heaters.end());
        int left = 0, right = max(*max_element(houses.begin(), houses.end()), *max_element(heaters.begin(), heaters.end()));
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (canCover(houses, heaters, mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
    
    bool canCover(vector<int>& houses, vector<int>& heaters, int radius) {
        for (int house : houses) {
            bool covered = false;
            for (int heater : heaters) {
                if (abs(house - heater) <= radius) {
                    covered = true;
                    break;
                }
            }
            if (!covered) {
                return false;
            }
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot \log d)$, where $n$ is the number of houses, $m$ is the number of heaters, and $d$ is the maximum distance between a house and a heater.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input.
> - **Optimality proof:** This approach is optimal because it uses binary search to reduce the number of iterations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search, sorting, and iteration.
- Problem-solving patterns identified: Using binary search to find the minimum radius that covers all houses.
- Optimization techniques learned: Reducing the number of iterations using binary search.
- Similar problems to practice: Other problems that involve finding the minimum or maximum value using binary search.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty list of houses or heaters.
- Edge cases to watch for: Handling cases where a house is not covered by any heater.
- Performance pitfalls: Using a brute force approach that has a high time complexity.
- Testing considerations: Testing the solution with different inputs, including edge cases.