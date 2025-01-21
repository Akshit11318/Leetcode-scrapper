## The Number of Passengers in Each Bus I

**Problem Link:** https://leetcode.com/problems/the-number-of-passengers-in-each-bus-i/description

**Problem Statement:**
- Input format and constraints: The problem requires finding the number of passengers that will board each bus, given the arrival and departure times of `n` buses and the arrival times of `m` passengers.
- Expected output format: The output should be an array of integers where each integer represents the number of passengers that will board the corresponding bus.
- Key requirements and edge cases to consider: 
    * Each bus will depart at its scheduled departure time, regardless of the number of passengers on board.
    * Each passenger will board the first bus that they can catch (i.e., the first bus that departs after their arrival time).
    * If a passenger arrives at the same time as a bus departs, they will not be able to board that bus.
- Example test cases with explanations:
    * `bus = [1, 4, 7], passengers = [6, 8]` should return `[2, 0, 1]`, because the first two passengers will board the second bus, and the third passenger will board the third bus.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can iterate over each passenger and find the first bus that they can catch.
- Step-by-step breakdown of the solution: 
    1. Sort the buses by their departure times.
    2. Iterate over each passenger and find the first bus that they can catch by iterating over the sorted buses.
    3. Keep track of the number of passengers that will board each bus.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it may not be efficient for large inputs.

```cpp
vector<int> numOfPassengers(int n, int m, vector<int>& stations, vector<int>& passengers) {
    vector<int> result(n, 0);
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (stations[j] >= passengers[i]) {
                result[j]++;
                break;
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of passengers and $n$ is the number of buses, because we are iterating over each passenger and each bus.
> - **Space Complexity:** $O(n)$, where $n$ is the number of buses, because we need to store the result for each bus.
> - **Why these complexities occur:** The time complexity is high because we are using nested loops to find the first bus that each passenger can catch. The space complexity is low because we only need to store the result for each bus.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a two-pointer technique to find the first bus that each passenger can catch.
- Detailed breakdown of the approach: 
    1. Sort the buses by their departure times.
    2. Initialize two pointers, one for the buses and one for the passengers.
    3. Iterate over the passengers and find the first bus that they can catch by moving the bus pointer forward until we find a bus that departs after the passenger arrives.
    4. Keep track of the number of passengers that will board each bus.
- Proof of optimality: This approach is optimal because we are only iterating over the passengers and the buses once, resulting in a time complexity of $O(n + m)$.

```cpp
vector<int> numOfPassengers(int n, int m, vector<int>& stations, vector<int>& passengers) {
    vector<int> result(n, 0);
    sort(stations.begin(), stations.end());
    sort(passengers.begin(), passengers.end());
    int busIndex = 0;
    for (int i = 0; i < m; i++) {
        while (busIndex < n && stations[busIndex] < passengers[i]) {
            busIndex++;
        }
        if (busIndex < n) {
            result[busIndex]++;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n + m \log m)$, where $n$ is the number of buses and $m$ is the number of passengers, because we are sorting the buses and the passengers.
> - **Space Complexity:** $O(n)$, where $n$ is the number of buses, because we need to store the result for each bus.
> - **Optimality proof:** This approach is optimal because we are only iterating over the passengers and the buses once, resulting in a time complexity of $O(n \log n + m \log m)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two-pointer technique, sorting.
- Problem-solving patterns identified: Finding the first bus that each passenger can catch.
- Optimization techniques learned: Using a two-pointer technique to reduce the time complexity.

**Mistakes to Avoid:**
- Common implementation errors: Not sorting the buses and the passengers, not using a two-pointer technique.
- Edge cases to watch for: When a passenger arrives at the same time as a bus departs, when there are no buses or passengers.
- Performance pitfalls: Using a brute force approach with a high time complexity.
- Testing considerations: Testing with different inputs, including edge cases.