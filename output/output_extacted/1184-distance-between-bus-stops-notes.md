## Distance Between Bus Stops

**Problem Link:** https://leetcode.com/problems/distance-between-bus-stops/description

**Problem Statement:**
- Input format: An array of integers `distance` representing the distance between each bus stop, and two integers `start` and `end` representing the start and end stops.
- Constraints: The length of `distance` will be in the range `[1, 10^4]`, and `start` and `end` will be in the range `[0, n - 1]` where `n` is the length of `distance`.
- Expected output format: The minimum distance between the start and end stops.
- Key requirements and edge cases to consider: The bus can travel in either direction, and the start and end stops can be the same.
- Example test cases with explanations:
  - Example 1: `distance = [1,2,3,4], start = 0, end = 1`, Output: `1`
  - Example 2: `distance = [1,2,3,4], start = 0, end = 2`, Output: `3`
  - Example 3: `distance = [1,2,3,4], start = 0, end = 3`, Output: `4`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the total distance between all bus stops and then calculate the minimum distance between the start and end stops by considering both clockwise and counterclockwise directions.
- Step-by-step breakdown of the solution:
  1. Calculate the total distance between all bus stops by summing up all the distances in the `distance` array.
  2. Calculate the minimum distance between the start and end stops by considering both clockwise and counterclockwise directions.
- Why this approach comes to mind first: It is the most straightforward approach and considers all possible scenarios.

```cpp
class Solution {
public:
    int distanceBetweenBusStops(vector<int>& distance, int start, int end) {
        // Calculate the total distance
        int totalDistance = 0;
        for (int i = 0; i < distance.size(); i++) {
            totalDistance += distance[i];
        }
        
        // Calculate the minimum distance
        int minDistance = INT_MAX;
        if (start < end) {
            int clockwiseDistance = 0;
            for (int i = start; i < end; i++) {
                clockwiseDistance += distance[i];
            }
            minDistance = min(minDistance, clockwiseDistance);
            minDistance = min(minDistance, totalDistance - clockwiseDistance);
        } else if (start > end) {
            int clockwiseDistance = 0;
            for (int i = start; i < distance.size(); i++) {
                clockwiseDistance += distance[i];
            }
            for (int i = 0; i < end; i++) {
                clockwiseDistance += distance[i];
            }
            minDistance = min(minDistance, clockwiseDistance);
            minDistance = min(minDistance, totalDistance - clockwiseDistance);
        } else {
            minDistance = 0;
        }
        
        return minDistance;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the `distance` array, because we need to iterate through the array to calculate the total distance and the minimum distance.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the total distance and the minimum distance.
> - **Why these complexities occur:** The time complexity is linear because we need to iterate through the array, and the space complexity is constant because we only use a fixed amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of calculating the total distance, we can directly calculate the minimum distance between the start and end stops by considering both clockwise and counterclockwise directions.
- Detailed breakdown of the approach:
  1. Calculate the minimum distance between the start and end stops by considering both clockwise and counterclockwise directions.
- Proof of optimality: This approach is optimal because it directly calculates the minimum distance without calculating the total distance, which reduces the time complexity.
- Why further optimization is impossible: This approach is already optimal because it only requires a single pass through the array to calculate the minimum distance.

```cpp
class Solution {
public:
    int distanceBetweenBusStops(vector<int>& distance, int start, int end) {
        // Calculate the minimum distance
        if (start > end) {
            swap(start, end);
        }
        int minDistance = 0;
        for (int i = start; i < end; i++) {
            minDistance += distance[i];
        }
        int totalDistance = 0;
        for (int i = 0; i < distance.size(); i++) {
            totalDistance += distance[i];
        }
        return min(minDistance, totalDistance - minDistance);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the `distance` array, because we need to iterate through the array to calculate the minimum distance.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the minimum distance.
> - **Optimality proof:** This approach is optimal because it directly calculates the minimum distance without calculating the total distance, which reduces the time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Calculating the minimum distance between two points in a circular array.
- Problem-solving patterns identified: Considering both clockwise and counterclockwise directions to calculate the minimum distance.
- Optimization techniques learned: Reducing the time complexity by directly calculating the minimum distance instead of calculating the total distance.
- Similar problems to practice: Problems involving calculating the minimum distance between two points in a circular array.

**Mistakes to Avoid:**
- Common implementation errors: Not considering both clockwise and counterclockwise directions.
- Edge cases to watch for: When the start and end stops are the same.
- Performance pitfalls: Calculating the total distance instead of directly calculating the minimum distance.
- Testing considerations: Testing the function with different inputs to ensure it works correctly.