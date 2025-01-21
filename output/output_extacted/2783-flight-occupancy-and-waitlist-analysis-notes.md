## Flight Occupancy and Waitlist Analysis
**Problem Link:** https://leetcode.com/problems/flight-occupancy-and-waitlist-analysis/description

**Problem Statement:**
- Input format and constraints: Given a list of flights with their corresponding seat capacities and the number of passengers on each flight.
- Expected output format: Calculate the flight occupancy and waitlist for each flight.
- Key requirements and edge cases to consider: 
    - Handle cases where the number of passengers exceeds the seat capacity.
    - Consider cases where the number of passengers is less than the seat capacity.
- Example test cases with explanations:
    - For a flight with a seat capacity of 100 and 120 passengers, the occupancy should be 100% and the waitlist should be 20.
    - For a flight with a seat capacity of 100 and 80 passengers, the occupancy should be 80% and the waitlist should be 0.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the occupancy and waitlist for each flight by comparing the number of passengers to the seat capacity.
- Step-by-step breakdown of the solution:
    1. Initialize variables to store the occupancy and waitlist for each flight.
    2. Iterate over each flight and calculate the occupancy by dividing the number of passengers by the seat capacity.
    3. If the number of passengers exceeds the seat capacity, calculate the waitlist by subtracting the seat capacity from the number of passengers.
- Why this approach comes to mind first: It is a straightforward approach that directly calculates the occupancy and waitlist for each flight.

```cpp
#include <iostream>
#include <vector>

struct Flight {
    int seatCapacity;
    int passengers;
};

void calculateOccupancyAndWaitlist(std::vector<Flight>& flights) {
    for (auto& flight : flights) {
        double occupancy = static_cast<double>(flight.passengers) / flight.seatCapacity * 100;
        if (flight.passengers > flight.seatCapacity) {
            int waitlist = flight.passengers - flight.seatCapacity;
            std::cout << "Flight occupancy: " << occupancy << "%, Waitlist: " << waitlist << std::endl;
        } else {
            std::cout << "Flight occupancy: " << occupancy << "%, Waitlist: 0" << std::endl;
        }
    }
}

int main() {
    std::vector<Flight> flights = {{100, 120}, {100, 80}};
    calculateOccupancyAndWaitlist(flights);
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of flights. This is because we iterate over each flight once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the occupancy and waitlist for each flight.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each flight. The space complexity is constant because we do not use any data structures that grow with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal in terms of time complexity, as we must iterate over each flight at least once to calculate the occupancy and waitlist.
- Detailed breakdown of the approach:
    1. Initialize variables to store the occupancy and waitlist for each flight.
    2. Iterate over each flight and calculate the occupancy by dividing the number of passengers by the seat capacity.
    3. If the number of passengers exceeds the seat capacity, calculate the waitlist by subtracting the seat capacity from the number of passengers.
- Proof of optimality: The time complexity of $O(n)$ is optimal because we must perform at least one operation for each flight.
- Why further optimization is impossible: We cannot improve the time complexity because we must iterate over each flight at least once.

```cpp
#include <iostream>
#include <vector>

struct Flight {
    int seatCapacity;
    int passengers;
};

void calculateOccupancyAndWaitlist(std::vector<Flight>& flights) {
    for (auto& flight : flights) {
        double occupancy = static_cast<double>(flight.passengers) / flight.seatCapacity * 100;
        if (flight.passengers > flight.seatCapacity) {
            int waitlist = flight.passengers - flight.seatCapacity;
            std::cout << "Flight occupancy: " << occupancy << "%, Waitlist: " << waitlist << std::endl;
        } else {
            std::cout << "Flight occupancy: " << occupancy << "%, Waitlist: 0" << std::endl;
        }
    }
}

int main() {
    std::vector<Flight> flights = {{100, 120}, {100, 80}};
    calculateOccupancyAndWaitlist(flights);
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of flights. This is because we iterate over each flight once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the occupancy and waitlist for each flight.
> - **Optimality proof:** The time complexity is optimal because we must perform at least one operation for each flight.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional statements, and basic arithmetic operations.
- Problem-solving patterns identified: Calculating occupancy and waitlist for each flight based on the number of passengers and seat capacity.
- Optimization techniques learned: None, as the brute force approach is already optimal.
- Similar problems to practice: Other problems involving iteration and basic arithmetic operations, such as calculating averages or sums.

**Mistakes to Avoid:**
- Common implementation errors: Not handling cases where the number of passengers exceeds the seat capacity.
- Edge cases to watch for: Cases where the number of passengers is less than the seat capacity.
- Performance pitfalls: Not using efficient data structures or algorithms.
- Testing considerations: Test cases where the number of passengers exceeds the seat capacity, as well as cases where the number of passengers is less than the seat capacity.