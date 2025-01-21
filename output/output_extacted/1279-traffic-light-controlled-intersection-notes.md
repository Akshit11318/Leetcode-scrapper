## Traffic Light Controlled Intersection

**Problem Link:** https://leetcode.com/problems/traffic-light-controlled-intersection/description

**Problem Statement:**
- Input format and constraints: The input will be an integer array `arr` representing the duration of each car's arrival and an integer `n` representing the number of cars.
- Expected output format: The output should be an integer representing the minimum time required to clear all cars from the intersection.
- Key requirements and edge cases to consider: The traffic light can only change its state at the end of each second, and cars can only enter the intersection when the traffic light is green.
- Example test cases with explanations:
  - Example 1: `arr = [3, 2, 1]`, `n = 3`. The minimum time required is 7.
  - Example 2: `arr = [1, 1, 1]`, `n = 3`. The minimum time required is 5.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can simulate the traffic light and the cars to find the minimum time required.
- Step-by-step breakdown of the solution:
  1. Initialize the current time and the number of cars that have passed the intersection.
  2. Loop through each car in the input array.
  3. For each car, calculate the time when it can enter the intersection based on the traffic light's state.
  4. Update the current time and the number of cars that have passed the intersection.
  5. Repeat steps 2-4 until all cars have passed the intersection.
- Why this approach comes to mind first: It's a straightforward simulation of the problem.

```cpp
int minTime(vector<int>& arr, int n) {
    int currentTime = 0;
    int passedCars = 0;
    int greenTime = 5; // default green time
    int redTime = 5; // default red time
    int trafficLightState = 0; // 0: green, 1: red

    while (passedCars < n) {
        // Check if the traffic light is green
        if (trafficLightState == 0) {
            // Calculate the time when the current car can enter the intersection
            int enterTime = max(currentTime, arr[passedCars]);

            // Update the current time and the number of passed cars
            currentTime = enterTime + 2; // assume it takes 2 seconds to pass the intersection
            passedCars++;

            // Check if the green time is over
            if (currentTime - enterTime >= greenTime) {
                trafficLightState = 1; // switch to red
                currentTime += redTime; // add the red time
            }
        } else {
            // If the traffic light is red, just wait for the red time to end
            currentTime += redTime;
            trafficLightState = 0; // switch to green
        }
    }

    return currentTime;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of cars. We loop through each car once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the current time, the number of passed cars, and the traffic light state.
> - **Why these complexities occur:** The time complexity is linear because we simulate each car once, and the space complexity is constant because we only use a fixed amount of space to store the necessary variables.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a more efficient algorithm to calculate the minimum time required.
- Detailed breakdown of the approach:
  1. Initialize the current time and the number of cars that have passed the intersection.
  2. Loop through each car in the input array.
  3. For each car, calculate the time when it can enter the intersection based on the traffic light's state.
  4. Update the current time and the number of cars that have passed the intersection using a more efficient formula.
- Why further optimization is impossible: This approach has a linear time complexity, which is the best we can achieve for this problem.

```cpp
int minTime(vector<int>& arr, int n) {
    int currentTime = 0;
    int passedCars = 0;
    int greenTime = 5; // default green time
    int redTime = 5; // default red time

    for (int i = 0; i < n; i++) {
        // Calculate the time when the current car can enter the intersection
        int enterTime = max(currentTime, arr[i]);

        // Update the current time and the number of passed cars
        currentTime = max(currentTime, enterTime) + 2; // assume it takes 2 seconds to pass the intersection
        passedCars++;

        // Check if the green time is over
        if ((currentTime - enterTime) % (greenTime + redTime) >= greenTime) {
            currentTime += redTime - ((currentTime - enterTime) % (greenTime + redTime) - greenTime);
        }
    }

    return currentTime;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of cars. We loop through each car once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the current time and the number of passed cars.
> - **Optimality proof:** This approach has a linear time complexity, which is the best we can achieve for this problem. We also use a more efficient formula to update the current time and the number of passed cars.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Simulation, optimization, and efficient formula usage.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems and using a more efficient algorithm to solve them.
- Optimization techniques learned: Using a more efficient formula to update the current time and the number of passed cars.
- Similar problems to practice: Other simulation-based problems, such as traffic flow or resource allocation problems.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty input array or a negative number of cars.
- Edge cases to watch for: Cars arriving at the same time, or the traffic light changing state at the same time as a car arrives.
- Performance pitfalls: Using an inefficient algorithm or data structure, such as a brute force approach or a recursive function call.
- Testing considerations: Testing the function with different input arrays and numbers of cars to ensure it works correctly in all cases.