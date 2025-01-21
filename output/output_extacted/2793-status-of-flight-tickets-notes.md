## Status of Flight Tickets
**Problem Link:** https://leetcode.com/problems/status-of-flight-tickets/description

**Problem Statement:**
- Input format and constraints: The function takes a `tickets` list of lists where each sublist contains the flight details.
- Expected output format: The function should return a list of integers representing the status of each flight ticket.
- Key requirements and edge cases to consider: Handle cases where the input list is empty or contains invalid data.
- Example test cases with explanations: For example, given `tickets = [[1,2,1],[2,1,1],[1,2,1]]`, the function should return `[1,1,1]` because all flights are booked.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each ticket and check if it's booked.
- Step-by-step breakdown of the solution: 
  1. Initialize an empty list to store the status of each ticket.
  2. Iterate over each ticket in the input list.
  3. For each ticket, check if it's booked by comparing the `from` and `to` airports.
  4. If the ticket is booked, append 1 to the status list; otherwise, append 0.
- Why this approach comes to mind first: It's a straightforward and simple approach that checks each ticket individually.

```cpp
#include <vector>
#include <iostream>

vector<int> findFlightStatus(vector<vector<int>>& tickets) {
    vector<int> status;
    for (auto& ticket : tickets) {
        if (ticket[0] == ticket[1]) {
            status.push_back(1); // booked
        } else {
            status.push_back(0); // not booked
        }
    }
    return status;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of tickets. This is because we iterate over each ticket once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of tickets. This is because we store the status of each ticket in a list.
> - **Why these complexities occur:** The time complexity occurs because we iterate over each ticket, and the space complexity occurs because we store the status of each ticket.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using a simple iteration over the input list.
- Detailed breakdown of the approach: 
  1. Initialize an empty list to store the status of each ticket.
  2. Iterate over each ticket in the input list.
  3. For each ticket, check if it's booked by comparing the `from` and `to` airports.
  4. If the ticket is booked, append 1 to the status list; otherwise, append 0.
- Proof of optimality: This approach is optimal because it only requires a single iteration over the input list, resulting in a time complexity of $O(n)$.

```cpp
#include <vector>
#include <iostream>

vector<int> findFlightStatus(vector<vector<int>>& tickets) {
    vector<int> status;
    for (const auto& ticket : tickets) {
        int from = ticket[0];
        int to = ticket[1];
        int isBooked = ticket[2];
        if (from == to && isBooked == 1) {
            status.push_back(1); // booked
        } else {
            status.push_back(0); // not booked
        }
    }
    return status;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of tickets. This is because we iterate over each ticket once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of tickets. This is because we store the status of each ticket in a list.
> - **Optimality proof:** This approach is optimal because it only requires a single iteration over the input list, resulting in a time complexity of $O(n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration over a list, conditional checks, and list manipulation.
- Problem-solving patterns identified: Simple iteration over a list to solve a problem.
- Optimization techniques learned: None, as the problem is already solved optimally.
- Similar problems to practice: Other problems that involve iterating over a list and performing conditional checks.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty input list.
- Edge cases to watch for: Empty input list, invalid data in the input list.
- Performance pitfalls: Not using a simple iteration over the list, resulting in a higher time complexity.
- Testing considerations: Test the function with different input lists, including edge cases.