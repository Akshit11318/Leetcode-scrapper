## Car Pooling
**Problem Link:** https://leetcode.com/problems/car-pooling/description

**Problem Statement:**
- Input format and constraints: The problem involves determining if a car can accommodate all passengers based on their trip details. The input consists of `trips` (a list of trip details where each trip is a list of three integers: `[num_passengers, start_location, end_location]`) and `capacity` (the maximum number of passengers the car can hold).
- Expected output format: A boolean indicating whether the car can accommodate all passengers.
- Key requirements and edge cases to consider: The car starts empty and the trips are sorted by their start location. The passengers leave the car at their end location.
- Example test cases with explanations: 
    - `trips = [[2,1,5],[3,3,7]]`, `capacity = 4`. Output: `False` because the car cannot accommodate all passengers at location 3.
    - `trips = [[2,1,5],[3,3,7]]`, `capacity = 5`. Output: `True` because the car can accommodate all passengers.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Simulate the car's journey, keeping track of the current number of passengers in the car at each location.
- Step-by-step breakdown of the solution: 
    1. Create a list of events where each event is a tuple of `(location, change_in_passengers)`. A positive change indicates passengers getting in, and a negative change indicates passengers getting out.
    2. Sort the events by location.
    3. Iterate through the sorted events, updating the current number of passengers in the car.
    4. If at any point the number of passengers exceeds the car's capacity, return `False`.
- Why this approach comes to mind first: It directly simulates the car's journey, making it easy to understand and implement.

```cpp
bool carPooling(vector<vector<int>>& trips, int capacity) {
    vector<pair<int, int>> events;
    for (auto& trip : trips) {
        int passengers = trip[0], start = trip[1], end = trip[2];
        events.push_back({start, passengers});
        events.push_back({end, -passengers});
    }
    sort(events.begin(), events.end());
    int currentPassengers = 0;
    for (auto& event : events) {
        currentPassengers += event.second;
        if (currentPassengers > capacity) {
            return false;
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of trips, due to sorting the events.
> - **Space Complexity:** $O(n)$ for storing the events.
> - **Why these complexities occur:** Sorting the events by location dominates the time complexity, and storing all events in memory contributes to the space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same insight as the brute force approach, but we can optimize the implementation by using a more efficient data structure to store and update the events.
- Detailed breakdown of the approach: 
    1. Use a `map` to store the events, where the key is the location and the value is the change in passengers. This allows for efficient insertion and sorting of events.
    2. Iterate through the sorted events (locations), updating the current number of passengers.
- Proof of optimality: This approach still simulates the car's journey but does so more efficiently by avoiding the overhead of sorting a vector of pairs.

```cpp
bool carPooling(vector<vector<int>>& trips, int capacity) {
    map<int, int> events;
    for (auto& trip : trips) {
        int passengers = trip[0], start = trip[1], end = trip[2];
        events[start] += passengers;
        events[end] -= passengers;
    }
    int currentPassengers = 0;
    for (auto& event : events) {
        currentPassengers += event.second;
        if (currentPassengers > capacity) {
            return false;
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of unique locations (start and end points of all trips), due to the map's insertion and iteration operations.
> - **Space Complexity:** $O(n)$ for storing the events in the map.
> - **Optimality proof:** This is optimal because we must consider each trip's start and end points at least once to determine if the car can accommodate all passengers.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Simulating the car's journey, using data structures (vectors and maps) for efficient storage and retrieval of events.
- Problem-solving patterns identified: Breaking down complex problems into manageable events and efficiently processing these events.
- Optimization techniques learned: Using appropriate data structures to reduce computational complexity.
- Similar problems to practice: Other problems involving simulating journeys or processes and optimizing resource allocation.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases (e.g., when a trip starts and ends at the same location) or misunderstanding the problem constraints.
- Edge cases to watch for: Trips with zero passengers, trips that start or end at the same location as another trip, and ensuring the car starts empty.
- Performance pitfalls: Using inefficient data structures or algorithms for sorting and iterating over events.
- Testing considerations: Thoroughly testing the function with various inputs, including edge cases and large inputs to ensure correctness and efficiency.