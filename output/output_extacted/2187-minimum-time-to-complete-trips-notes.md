## Minimum Time to Complete Trips
**Problem Link:** https://leetcode.com/problems/minimum-time-to-complete-trips/description

**Problem Statement:**
- Input: An array `time` where `time[i]` is the time it takes for the `i`-th bus to complete one trip, and an integer `totalTrips`.
- Output: The minimum time required to complete at least `totalTrips` trips.
- Key requirements: Find the minimum time that allows for the completion of the specified number of trips considering the time each bus takes for one trip.
- Edge cases: Handling cases where the total trips can be completed before all buses have finished their first trip, and ensuring the search space is correctly defined.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The brute force approach involves simulating the trips of all buses over time, incrementing time one unit at a time, and checking after each increment how many trips have been completed by all buses.
- Step-by-step breakdown:
  1. Initialize a variable `timeElapsed` to 0.
  2. Initialize a variable `tripsCompleted` to 0.
  3. For each bus, calculate how many trips it can complete in the current `timeElapsed`.
  4. Increment `tripsCompleted` by the number of trips each bus can complete.
  5. If `tripsCompleted` is greater than or equal to `totalTrips`, return `timeElapsed`.
  6. Otherwise, increment `timeElapsed` by 1 and repeat steps 3-5.

```cpp
int minimumTime(vector<int>& time, int totalTrips) {
    int timeElapsed = 0;
    while (true) {
        int tripsCompleted = 0;
        for (int t : time) {
            tripsCompleted += timeElapsed / t;
        }
        if (tripsCompleted >= totalTrips) {
            return timeElapsed;
        }
        timeElapsed++;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot t)$, where $n$ is the number of buses and $t$ is the time when the `totalTrips` are completed. This is because in the worst case, for each unit of time, we are iterating over all buses.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store our variables.
> - **Why these complexities occur:** The brute force approach simulates each unit of time, checking every bus, which leads to linear time complexity with respect to the number of buses and the total time.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: The minimum time required to complete at least `totalTrips` trips can be found using a binary search approach. The idea is to find the minimum time `t` such that the total number of trips completed by all buses is at least `totalTrips`.
- Detailed breakdown:
  1. Define the search space: The minimum possible time is 1, and the maximum possible time is the total number of trips times the maximum time a bus takes to complete one trip.
  2. Perform binary search within this range.
  3. For each mid-point `t`, calculate the total number of trips that can be completed by all buses.
  4. If the total trips are greater than or equal to `totalTrips`, update the upper bound of the search space to `t`.
  5. Otherwise, update the lower bound to `t + 1`.
- Proof of optimality: This approach is optimal because it uses binary search to find the minimum time, reducing the search space by half at each step.

```cpp
int minimumTime(vector<int>& time, int totalTrips) {
    int low = 1, high = 1e14; // Assuming a reasonable upper limit
    while (low < high) {
        long long mid = low + (high - low) / 2;
        long long trips = 0;
        for (int t : time) {
            trips += mid / t;
        }
        if (trips < totalTrips) {
            low = mid + 1;
        } else {
            high = mid;
        }
    }
    return low;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot log(t))$, where $n$ is the number of buses and $t$ is the upper limit of the search space. This is because we perform a binary search over the possible times and for each time, we iterate over all buses.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space.
> - **Optimality proof:** This approach is optimal because it minimizes the number of times we need to calculate the total trips by using binary search, significantly reducing the search space at each step.

---

### Final Notes
**Learning Points:**
- The importance of understanding the search space and defining it correctly.
- Using binary search to optimize the search for a minimum or maximum value within a defined range.
- The trade-off between the brute force approach's simplicity and its inefficiency for large inputs.

**Mistakes to Avoid:**
- Not correctly defining the search space, which can lead to incorrect results or infinite loops.
- Not considering the data types for the variables, especially when dealing with large numbers.
- Failing to validate the input and handle edge cases properly.