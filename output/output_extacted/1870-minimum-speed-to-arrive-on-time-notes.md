## Minimum Speed to Arrive On Time
**Problem Link:** https://leetcode.com/problems/minimum-speed-to-arrive-on-time/description

**Problem Statement:**
- Input format and constraints: The problem takes in a list of distances `dist` and times `speed` for each segment of a trip and a maximum time `hoursBefore` allowed to reach the destination. The goal is to find the minimum speed required to complete the trip within the given time.
- Expected output format: The output should be the minimum speed required, rounded up to the nearest integer.
- Key requirements and edge cases to consider: The input lists are non-empty and contain only positive integers. The maximum time `hoursBefore` is also a positive integer.
- Example test cases with explanations: For example, given `dist = [1, 3, 2]`, `speed = [2, 1, 1]`, and `hoursBefore = 6`, the minimum speed required is 3.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves checking all possible speeds from 1 to the maximum possible speed, which is the sum of all distances divided by the minimum time.
- Step-by-step breakdown of the solution:
  1. Calculate the maximum possible speed.
  2. Iterate over all possible speeds from 1 to the maximum possible speed.
  3. For each speed, calculate the total time taken to complete the trip.
  4. If the total time is less than or equal to the given maximum time, return the current speed as the minimum speed required.
- Why this approach comes to mind first: This approach is straightforward and ensures that we find the minimum speed required.

```cpp
#include <iostream>
#include <vector>
#include <cmath>

int minSpeedOnTime(std::vector<int>& dist, std::vector<int>& speed, int hoursBefore) {
    int n = dist.size();
    int maxSpeed = 0;
    for (int i = 0; i < n; i++) {
        maxSpeed = std::max(maxSpeed, dist[i]);
    }
    for (int sp = 1; sp <= maxSpeed + hoursBefore; sp++) {
        double totalTime = 0;
        for (int i = 0; i < n; i++) {
            totalTime += std::ceil((double)dist[i] / sp);
        }
        if (totalTime <= hoursBefore) {
            return sp;
        }
    }
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times (maxSpeed + hoursBefore))$, where $n$ is the number of segments in the trip.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum possible speed and the current speed.
> - **Why these complexities occur:** The time complexity occurs because we iterate over all possible speeds for each segment of the trip. The space complexity is constant because we only use a fixed amount of space to store the maximum possible speed and the current speed.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use binary search to find the minimum speed required. We can use binary search because the problem has the following properties:
  - The minimum speed required is a monotonic function of the input parameters.
  - We can efficiently calculate the total time taken to complete the trip for a given speed.
- Detailed breakdown of the approach:
  1. Calculate the minimum and maximum possible speeds.
  2. Perform binary search between the minimum and maximum possible speeds.
  3. For each speed in the binary search range, calculate the total time taken to complete the trip.
  4. If the total time is less than or equal to the given maximum time, update the minimum possible speed.
- Proof of optimality: The binary search approach is optimal because it reduces the search space by half at each step, resulting in a logarithmic time complexity.
- Why further optimization is impossible: The binary search approach is impossible to optimize further because it already has the best possible time complexity for this problem.

```cpp
#include <iostream>
#include <vector>
#include <cmath>

int minSpeedOnTime(std::vector<int>& dist, std::vector<int>& speed, int hoursBefore) {
    int n = dist.size();
    int maxSpeed = 1e9;
    int minSpeed = 1;
    while (minSpeed < maxSpeed) {
        int midSpeed = minSpeed + (maxSpeed - minSpeed) / 2;
        double totalTime = 0;
        for (int i = 0; i < n; i++) {
            totalTime += std::ceil((double)dist[i] / midSpeed);
        }
        if (totalTime <= hoursBefore) {
            maxSpeed = midSpeed;
        } else {
            minSpeed = midSpeed + 1;
        }
    }
    return minSpeed > 1e9 ? -1 : minSpeed;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times log(maxSpeed))$, where $n$ is the number of segments in the trip.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum and maximum possible speeds.
> - **Optimality proof:** The binary search approach is optimal because it reduces the search space by half at each step, resulting in a logarithmic time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search, monotonic functions, and efficient calculation of total time.
- Problem-solving patterns identified: Using binary search to find the minimum or maximum value of a monotonic function.
- Optimization techniques learned: Reducing the search space by half at each step using binary search.
- Similar problems to practice: Finding the minimum or maximum value of a function using binary search.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty input list or a maximum time of 0.
- Edge cases to watch for: Handling cases where the minimum speed required is greater than the maximum possible speed.
- Performance pitfalls: Using a brute force approach instead of binary search, resulting in a much higher time complexity.
- Testing considerations: Testing the function with different input parameters, including edge cases, to ensure correctness and performance.