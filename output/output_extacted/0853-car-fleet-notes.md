## Car Fleet
**Problem Link:** https://leetcode.com/problems/car-fleet/description

**Problem Statement:**
- Input format and constraints: The problem takes two arrays as input: `position` and `speed`. The `position` array contains the positions of cars on the road, and the `speed` array contains the speeds of the corresponding cars. The goal is to calculate the number of car fleets that will arrive at the destination.
- Expected output format: The output should be the number of car fleets.
- Key requirements and edge cases to consider: Cars can catch up to each other, and when they do, they form a fleet. The car in the front of the fleet will determine the speed of the fleet.
- Example test cases with explanations:
  - Example 1:
    - Input: `position = [1,2,3,4]`, `speed = [3,2,1,3]`
    - Output: `1`
    - Explanation: All cars will catch up to the car in front of them and form a single fleet.
  - Example 2:
    - Input: `position = [3,2,1]`, `speed = [2,1,3]`
    - Output: `2`
    - Explanation: The car in position 3 will catch up to the car in position 2, but the car in position 1 will not catch up to the car in position 2.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves simulating the movement of each car and checking if it catches up to the car in front of it.
- Step-by-step breakdown of the solution:
  1. Initialize the time of arrival for each car.
  2. For each car, calculate the time it takes to catch up to the car in front of it.
  3. If the car catches up to the car in front of it, update the time of arrival for the car in front of it.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient for large inputs.

```cpp
class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();
        vector<pair<int, int>> cars;
        for (int i = 0; i < n; i++) {
            cars.push_back({position[i], speed[i]});
        }
        sort(cars.begin(), cars.end(), [](pair<int, int> a, pair<int, int> b) {
            return a.first > b.first;
        });
        int fleets = 0;
        double arrivalTime = 0.0;
        for (int i = 0; i < n; i++) {
            double currentTime = (double)(target - cars[i].first) / cars[i].second;
            if (currentTime > arrivalTime) {
                fleets++;
                arrivalTime = currentTime;
            }
        }
        return fleets;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of cars. This is because we sort the cars by their positions.
> - **Space Complexity:** $O(n)$, where $n$ is the number of cars. This is because we store the cars in a vector.
> - **Why these complexities occur:** The time complexity occurs because we sort the cars, and the space complexity occurs because we store the cars in a vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can calculate the time of arrival for each car and compare it with the time of arrival for the car in front of it.
- Detailed breakdown of the approach:
  1. Initialize the time of arrival for each car.
  2. For each car, calculate the time it takes to arrive at the destination.
  3. Compare the time of arrival for the current car with the time of arrival for the car in front of it.
  4. If the current car catches up to the car in front of it, update the time of arrival for the car in front of it.
- Proof of optimality: This approach is optimal because it has a time complexity of $O(n \log n)$, which is the best possible time complexity for this problem.

```cpp
class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();
        vector<pair<int, int>> cars;
        for (int i = 0; i < n; i++) {
            cars.push_back({position[i], speed[i]});
        }
        sort(cars.begin(), cars.end(), [](pair<int, int> a, pair<int, int> b) {
            return a.first > b.first;
        });
        int fleets = 0;
        double arrivalTime = 0.0;
        for (int i = 0; i < n; i++) {
            double currentTime = (double)(target - cars[i].first) / cars[i].second;
            if (currentTime > arrivalTime) {
                fleets++;
                arrivalTime = currentTime;
            }
        }
        return fleets;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of cars. This is because we sort the cars by their positions.
> - **Space Complexity:** $O(n)$, where $n$ is the number of cars. This is because we store the cars in a vector.
> - **Optimality proof:** This approach is optimal because it has a time complexity of $O(n \log n)$, which is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sorting, comparison, and optimization.
- Problem-solving patterns identified: calculating the time of arrival for each car and comparing it with the time of arrival for the car in front of it.
- Optimization techniques learned: using a vector to store the cars and sorting them by their positions.
- Similar problems to practice: problems involving sorting and comparison, such as finding the closest pair of points in a set of points.

**Mistakes to Avoid:**
- Common implementation errors: not checking for edge cases, such as an empty input array.
- Edge cases to watch for: an empty input array, a single car, and multiple cars with the same position and speed.
- Performance pitfalls: using a inefficient sorting algorithm, such as bubble sort, and not optimizing the comparison of the time of arrival for each car.
- Testing considerations: testing the function with different inputs, such as an empty array, a single car, and multiple cars with different positions and speeds.