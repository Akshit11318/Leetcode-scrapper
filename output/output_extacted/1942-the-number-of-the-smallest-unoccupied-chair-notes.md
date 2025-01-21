## The Number of the Smallest Unoccupied Chair

**Problem Link:** https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/description

**Problem Statement:**
- Input format and constraints: The input consists of a list of events where each event is represented as a pair `[arrivalTime, leaveTime]`, and a target time `targetTime`.
- Expected output format: The function should return the number of the smallest unoccupied chair at the target time.
- Key requirements and edge cases to consider: All arrival and leave times are distinct, and there are no more than 50 chairs.
- Example test cases with explanations:
    - Example 1: `[[1,4],[3,6],[0,6]]`, `4` should return `1` because the smallest unoccupied chair at time 4 is chair 1.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Simulate the arrival and departure of each person and keep track of the occupied chairs at each time step.
- Step-by-step breakdown of the solution:
    1. Sort the events by time.
    2. Iterate through the sorted events and update the occupied chairs.
    3. At the target time, find the smallest unoccupied chair.
- Why this approach comes to mind first: It is a straightforward simulation of the problem.

```cpp
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

int smallestChair(std::vector<std::vector<int>>& events, int targetTime) {
    std::set<int> occupiedChairs;
    int nextChair = 0;

    // Sort the events by time
    std::sort(events.begin(), events.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
        return a[0] < b[0];
    });

    for (int time = 0; time <= targetTime; time++) {
        // Remove the chairs that are no longer occupied
        for (auto it = occupiedChairs.begin(); it != occupiedChairs.end();) {
            if (it == occupiedChairs.end()) break;
            bool found = false;
            for (const auto& event : events) {
                if (event[0] <= time && event[1] > time && event[2] == *it) {
                    found = true;
                    break;
                }
            }
            if (!found) {
                it = occupiedChairs.erase(it);
            } else {
                ++it;
            }
        }

        // Add the new occupied chairs
        for (const auto& event : events) {
            if (event[0] == time) {
                occupiedChairs.insert(nextChair);
                event[2] = nextChair;
                nextChair++;
            }
        }
    }

    // Find the smallest unoccupied chair
    for (int i = 0; ; i++) {
        if (occupiedChairs.find(i) == occupiedChairs.end()) {
            return i;
        }
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of events. The reason for this complexity is the nested loop structure in the code.
> - **Space Complexity:** $O(n)$, where $n$ is the number of events. This is because in the worst case, all events could be stored in the `occupiedChairs` set.
> - **Why these complexities occur:** The brute force approach has high time complexity due to the simulation of each time step and the nested loop structure. The space complexity is linear because we store all occupied chairs in a set.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a priority queue to keep track of the chairs that will be available soonest.
- Detailed breakdown of the approach:
    1. Sort the events by arrival time.
    2. Initialize a priority queue to store the chairs that will be available soonest.
    3. Iterate through the sorted events and update the priority queue.
    4. At the target time, find the smallest unoccupied chair.
- Why further optimization is impossible: This approach has a time complexity of $O(n \log n)$ due to the sorting and priority queue operations, which is optimal for this problem.

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

int smallestChair(std::vector<std::vector<int>>& events, int targetTime) {
    std::sort(events.begin(), events.end());
    std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<>> pq;
    std::vector<int> chairs(events.size());
    int nextChair = 0;

    for (int i = 0; i < events.size(); i++) {
        while (!pq.empty() && pq.top().first <= events[i][0]) {
            nextChair = std::min(nextChair, pq.top().second);
            pq.pop();
        }
        chairs[i] = nextChair++;
        pq.push({events[i][1], chairs[i]});
    }

    int smallestUnoccupied = INT_MAX;
    for (int i = 0; i < events.size(); i++) {
        if (events[i][0] <= targetTime && events[i][1] > targetTime) {
            smallestUnoccupied = std::min(smallestUnoccupied, chairs[i]);
        }
    }

    return smallestUnoccupied;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of events. The reason for this complexity is the sorting and priority queue operations.
> - **Space Complexity:** $O(n)$, where $n$ is the number of events. This is because we store all events in the priority queue and the `chairs` vector.
> - **Optimality proof:** This approach is optimal because it uses a priority queue to efficiently keep track of the chairs that will be available soonest, resulting in a time complexity of $O(n \log n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Priority queue, sorting.
- Problem-solving patterns identified: Using a priority queue to keep track of the smallest unoccupied chair.
- Optimization techniques learned: Using a priority queue to reduce the time complexity.
- Similar problems to practice: Problems involving priority queues and sorting.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, not handling the priority queue correctly.
- Edge cases to watch for: Empty input, target time outside the range of arrival and departure times.
- Performance pitfalls: Using a brute force approach with high time complexity.
- Testing considerations: Test the function with different inputs, including edge cases.