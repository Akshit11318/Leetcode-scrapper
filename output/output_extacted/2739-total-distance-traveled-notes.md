## Total Distance Traveled
**Problem Link:** https://leetcode.com/problems/total-distance-traveled/description

**Problem Statement:**
- Input format and constraints: You are given two arrays, `position` and `speed`, where `position[i]` is the position of the `i-th` car and `speed[i]` is the speed of the `i-th` car.
- Expected output format: The total distance traveled by all cars.
- Key requirements and edge cases to consider: All cars start at the same time and travel at constant speeds. If a car catches up to another car, they will travel together from then on.
- Example test cases with explanations: For example, if `position = [1,2,3]` and `speed = [2,1,2]`, then the total distance traveled will be the sum of the distances traveled by each car.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One way to solve this problem is to simulate the movement of each car over time.
- Step-by-step breakdown of the solution:
  1. Initialize the total distance traveled to 0.
  2. For each time unit, calculate the new position of each car.
  3. If a car catches up to another car, they will travel together from then on.
  4. Update the total distance traveled by each car.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it may not be efficient for large inputs.

```cpp
#include <vector>
#include <algorithm>

int calculateTotalDistance(std::vector<int>& position, std::vector<int>& speed) {
    int totalTime = 0;
    for (int i = 0; i < position.size(); i++) {
        for (int j = i + 1; j < position.size(); j++) {
            if (position[i] < position[j] && speed[i] > speed[j]) {
                int time = (position[j] - position[i]) / (speed[i] - speed[j]);
                totalTime = std::max(totalTime, time);
            }
        }
    }
    int totalDistance = 0;
    for (int i = 0; i < position.size(); i++) {
        totalDistance += speed[i] * (totalTime + (position[i] - position[0]) / speed[i]);
    }
    return totalDistance;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of cars. This is because we are using two nested loops to simulate the movement of each car.
> - **Space Complexity:** $O(1)$, which means the space required does not change with the size of the input array, so it is constant.
> - **Why these complexities occur:** The time complexity is quadratic because we are using two nested loops to simulate the movement of each car. The space complexity is constant because we are only using a fixed amount of space to store the total distance traveled.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of simulating the movement of each car over time, we can calculate the time it takes for each car to catch up to the car in front of it.
- Detailed breakdown of the approach:
  1. Initialize the total distance traveled to 0.
  2. For each car, calculate the time it takes to catch up to the car in front of it.
  3. Update the total distance traveled by each car.
- Proof of optimality: This approach is optimal because it avoids simulating the movement of each car over time, which reduces the time complexity.

```cpp
#include <vector>
#include <algorithm>

int calculateTotalDistance(std::vector<int>& position, std::vector<int>& speed) {
    int n = position.size();
    std::vector<int> times(n, 0);
    for (int i = 1; i < n; i++) {
        if (speed[i] <= speed[i-1]) {
            continue;
        }
        times[i] = (position[i] - position[i-1]) / (speed[i] - speed[i-1]);
        times[i] = std::max(times[i], times[i-1]);
    }
    int totalDistance = 0;
    for (int i = 0; i < n; i++) {
        totalDistance += speed[i] * times[i];
    }
    return totalDistance;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of cars. This is because we are using a single loop to calculate the time it takes for each car to catch up to the car in front of it.
> - **Space Complexity:** $O(n)$, which means the space required grows linearly with the size of the input array.
> - **Optimality proof:** This approach is optimal because it avoids simulating the movement of each car over time, which reduces the time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: This problem demonstrates the importance of avoiding unnecessary simulations and using mathematical insights to simplify the problem.
- Problem-solving patterns identified: This problem requires the use of mathematical insights to simplify the problem and avoid unnecessary simulations.
- Optimization techniques learned: This problem demonstrates the importance of avoiding unnecessary simulations and using mathematical insights to simplify the problem.
- Similar problems to practice: Other problems that involve simulating the movement of objects over time, such as the "Meeting Rooms" problem.

**Mistakes to Avoid:**
- Common implementation errors: One common mistake is to simulate the movement of each car over time, which can lead to a time complexity of $O(n^2)$.
- Edge cases to watch for: One edge case is when two cars have the same speed, in which case they will never catch up to each other.
- Performance pitfalls: One performance pitfall is to use a brute force approach, which can lead to a time complexity of $O(n^2)$.
- Testing considerations: When testing this problem, it's important to consider a variety of inputs, including cases where two cars have the same speed and cases where a car catches up to another car.