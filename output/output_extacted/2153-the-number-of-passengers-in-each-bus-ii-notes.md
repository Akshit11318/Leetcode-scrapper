## The Number of Passengers in Each Bus II
**Problem Link:** https://leetcode.com/problems/the-number-of-passengers-in-each-bus-ii/description

**Problem Statement:**
- Input format: An array `arr` of integers representing the time of arrival of each passenger and an integer `k` representing the capacity of each bus.
- Constraints: $1 \leq arr.length \leq 10^5$, $1 \leq k \leq 10^5$, and $1 \leq arr[i] \leq 10^9$ for all $i$.
- Expected output format: An array of integers representing the number of passengers in each bus.
- Key requirements and edge cases to consider: Each bus can hold at most $k$ passengers, and passengers arrive at different times.
- Example test cases with explanations:
  - Example 1: Input: `arr = [1,2,3], k = 1`, Output: `[1,1,1]`. Explanation: Each bus can hold at most 1 passenger.
  - Example 2: Input: `arr = [1,2,3,4,5], k = 2`, Output: `[2,3]`. Explanation: The first bus holds 2 passengers, and the second bus holds 3 passengers.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We need to find the number of passengers in each bus. We can start by sorting the arrival times and then iterating over the sorted array to fill the buses.
- Step-by-step breakdown of the solution:
  1. Sort the arrival times in ascending order.
  2. Initialize an empty bus and a counter for the number of passengers in the current bus.
  3. Iterate over the sorted arrival times. For each arrival time, check if the current bus is full. If it is, add the number of passengers in the current bus to the result and reset the counter and the bus. Otherwise, increment the counter.
  4. After iterating over all arrival times, add the number of passengers in the last bus to the result.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it may not be efficient for large inputs.

```cpp
vector<int> numberOfPassengers(vector<int>& arr, int k) {
    // Sort the arrival times in ascending order
    sort(arr.begin(), arr.end());
    
    vector<int> result;
    int bus = 0;
    
    for (int i = 0; i < arr.size(); i++) {
        // If the current bus is full, add the number of passengers to the result and reset the bus
        if (bus == k) {
            result.push_back(bus);
            bus = 0;
        }
        
        // Increment the counter for the current bus
        bus++;
    }
    
    // Add the number of passengers in the last bus to the result
    if (bus > 0) {
        result.push_back(bus);
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting step, where $n$ is the number of arrival times.
> - **Space Complexity:** $O(n)$ for the result vector, where $n$ is the number of arrival times.
> - **Why these complexities occur:** The sorting step dominates the time complexity, and the space complexity is due to the result vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a single pass through the sorted arrival times to fill the buses.
- Detailed breakdown of the approach:
  1. Sort the arrival times in ascending order.
  2. Initialize an empty result vector and a counter for the number of passengers in the current bus.
  3. Iterate over the sorted arrival times. For each arrival time, increment the counter. If the counter reaches the bus capacity, add the counter to the result and reset the counter.
- Proof of optimality: This approach is optimal because it only requires a single pass through the sorted arrival times, resulting in a time complexity of $O(n \log n)$ due to the sorting step.
- Why further optimization is impossible: The sorting step is necessary to ensure that the arrival times are processed in ascending order, and the single pass through the sorted arrival times is the most efficient way to fill the buses.

```cpp
vector<int> numberOfPassengers(vector<int>& arr, int k) {
    // Sort the arrival times in ascending order
    sort(arr.begin(), arr.end());
    
    vector<int> result;
    int bus = 0;
    
    for (int i = 0; i < arr.size(); i++) {
        // Increment the counter for the current bus
        bus++;
        
        // If the current bus is full, add the number of passengers to the result and reset the bus
        if (bus == k) {
            result.push_back(bus);
            bus = 0;
        }
    }
    
    // Add the number of passengers in the last bus to the result
    if (bus > 0) {
        result.push_back(bus);
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting step, where $n$ is the number of arrival times.
> - **Space Complexity:** $O(n)$ for the result vector, where $n$ is the number of arrival times.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the sorted arrival times, resulting in a time complexity of $O(n \log n)$ due to the sorting step.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, single pass through sorted data.
- Problem-solving patterns identified: Using a counter to keep track of the number of passengers in the current bus.
- Optimization techniques learned: Using a single pass through the sorted arrival times to fill the buses.
- Similar problems to practice: Other problems involving sorting and iterating over sorted data.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to reset the counter when the current bus is full.
- Edge cases to watch for: Handling the case where the number of arrival times is less than the bus capacity.
- Performance pitfalls: Using an inefficient sorting algorithm or iterating over the arrival times multiple times.
- Testing considerations: Testing the solution with different inputs, including edge cases and large inputs.