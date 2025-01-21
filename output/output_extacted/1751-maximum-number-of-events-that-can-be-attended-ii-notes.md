## Maximum Number of Events That Can Be Attended II

**Problem Link:** https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/description

**Problem Statement:**
- Input format: An array of events where each event is an array of two integers, `startDay` and `endDay`, representing the start and end days of the event, respectively.
- Constraints: $1 \leq events.length \leq 5 \times 10^5$, $1 \leq startDay \leq endDay \le 10^9$, and all `startDay` and `endDay` are unique.
- Expected output format: The maximum number of events that can be attended.
- Key requirements and edge cases to consider: The events are sorted by their start days, and each event can only be attended once.
- Example test cases with explanations:
  - Input: `[[1,2],[2,3],[3,4]]`
    Output: `3`
    Explanation: Attend all three events.
  - Input: `[[1,3],[1,3]]`
    Output: `1`
    Explanation: Only attend one of the events.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of events to find the maximum number of events that can be attended.
- Step-by-step breakdown of the solution:
  1. Sort the events by their end days.
  2. Iterate over all possible subsets of events.
  3. For each subset, check if the events are non-overlapping.
  4. If they are non-overlapping, update the maximum number of events.
- Why this approach comes to mind first: It's a straightforward way to consider all possible scenarios.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int maxTwoEvents(std::vector<std::vector<int>>& events) {
    int n = events.size();
    int maxEvents = 0;
    for (int i = 0; i < (1 << n); i++) {
        std::vector<int> subset;
        for (int j = 0; j < n; j++) {
            if (i & (1 << j)) {
                subset.push_back(j);
            }
        }
        bool isNonOverlapping = true;
        for (int j = 0; j < subset.size(); j++) {
            for (int k = j + 1; k < subset.size(); k++) {
                if (events[subset[j]][1] >= events[subset[k]][0] && events[subset[k]][1] >= events[subset[j]][0]) {
                    isNonOverlapping = false;
                    break;
                }
            }
            if (!isNonOverlapping) {
                break;
            }
        }
        if (isNonOverlapping) {
            maxEvents = std::max(maxEvents, (int)subset.size());
        }
    }
    return maxEvents;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n^2)$, where $n$ is the number of events. This is because we're generating all possible subsets of events and checking each subset for non-overlapping events.
> - **Space Complexity:** $O(n)$, where $n$ is the number of events. This is because we're storing the current subset of events.
> - **Why these complexities occur:** The brute force approach generates all possible subsets of events, resulting in exponential time complexity. The space complexity is linear because we only need to store the current subset of events.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a priority queue to store the end days of the events and iterate over the events in order of their start days.
- Detailed breakdown of the approach:
  1. Sort the events by their start days.
  2. Initialize a priority queue to store the end days of the events.
  3. Iterate over the events in order of their start days.
  4. For each event, remove all end days from the priority queue that are less than or equal to the start day of the current event.
  5. Add the end day of the current event to the priority queue.
  6. Update the maximum number of events that can be attended.
- Why further optimization is impossible: This approach has a time complexity of $O(n \log n)$, which is optimal because we need to iterate over all events and perform a comparison-based sorting.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

int maxTwoEvents(std::vector<std::vector<int>>& events) {
    std::sort(events.begin(), events.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
        return a[0] < b[0];
    });
    std::priority_queue<int, std::vector<int>, std::greater<int>> pq;
    int maxEvents = 0;
    for (const auto& event : events) {
        while (!pq.empty() && pq.top() < event[0]) {
            pq.pop();
        }
        pq.push(event[1]);
        maxEvents = std::max(maxEvents, (int)pq.size());
    }
    return maxEvents;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of events. This is because we're sorting the events and using a priority queue to store the end days of the events.
> - **Space Complexity:** $O(n)$, where $n$ is the number of events. This is because we're storing the end days of the events in the priority queue.
> - **Optimality proof:** This approach is optimal because we need to iterate over all events and perform a comparison-based sorting. The use of a priority queue allows us to efficiently remove end days that are less than or equal to the start day of the current event.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, priority queues, and iteration over events.
- Problem-solving patterns identified: Using a priority queue to store end days and iterating over events in order of their start days.
- Optimization techniques learned: Using a priority queue to efficiently remove end days that are less than or equal to the start day of the current event.
- Similar problems to practice: Problems involving sorting, priority queues, and iteration over events.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty input array.
- Edge cases to watch for: Events with the same start day, events with the same end day.
- Performance pitfalls: Using a brute force approach with exponential time complexity.
- Testing considerations: Test the solution with different input arrays, including edge cases.