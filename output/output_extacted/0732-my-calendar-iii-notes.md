## My Calendar III
**Problem Link:** https://leetcode.com/problems/my-calendar-iii/description

**Problem Statement:**
- Input format and constraints: The problem involves designing a calendar system that can handle booking and retrieving the number of triple bookings. The input will include a list of events where each event is represented by a start and end time.
- Expected output format: The output should be the maximum number of triple bookings that occur at any point in time.
- Key requirements and edge cases to consider: The key requirement is to efficiently manage the calendar to find the maximum number of triple bookings. Edge cases include handling overlapping events, non-overlapping events, and events that start and end at the same time.
- Example test cases with explanations: For example, given the events `[[10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]`, the maximum number of triple bookings is 3 because at time 10, there are three overlapping events.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The first approach to solving this problem is to iterate through each event and check for overlaps with all other events. This involves comparing the start and end times of each event with every other event to determine if they overlap.
- Step-by-step breakdown of the solution:
  1. Sort the events by their start time.
  2. Iterate through each event.
  3. For each event, iterate through the remaining events to check for overlaps.
  4. If an overlap is found, increment a counter for the current event's start time.
  5. Keep track of the maximum counter value encountered.
- Why this approach comes to mind first: This approach is straightforward and directly addresses the problem statement by checking every possible overlap.

```cpp
#include <vector>
#include <algorithm>

int maxTripleBookings(std::vector<std::vector<int>>& events) {
    int maxTriple = 0;
    for (int i = 0; i < events.size(); i++) {
        int count = 0;
        for (int j = 0; j < events.size(); j++) {
            if (i != j && events[i][0] < events[j][1] && events[j][0] < events[i][1]) {
                count++;
            }
        }
        if (count >= 2) {
            maxTriple = std::max(maxTriple, count);
        }
    }
    return maxTriple;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of events. This is because for each event, we potentially check every other event for overlaps.
> - **Space Complexity:** $O(1)$, not including the input, because we only use a constant amount of space to store the maximum count and the current count.
> - **Why these complexities occur:** The time complexity is quadratic due to the nested loop structure, and the space complexity is constant because we do not use any data structures that scale with the input size.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of checking every event against every other event, we can use a sweep line approach. This involves treating each event's start and end time as a point on a line and then sweeping across this line, counting the number of active events at any point.
- Detailed breakdown of the approach:
  1. Create a list of all event start and end times, marking each as either a start or an end.
  2. Sort this list by time.
  3. Initialize a counter for active events.
  4. Iterate through the sorted list. For each start time, increment the counter. For each end time, decrement the counter.
  5. Keep track of the maximum counter value encountered.
- Why further optimization is impossible: This approach is optimal because it reduces the time complexity to linear, avoiding unnecessary comparisons by only considering the points in time where the number of active events could change.

```cpp
#include <vector>
#include <algorithm>

struct EventPoint {
    int time;
    bool isStart;
};

int maxTripleBookings(std::vector<std::vector<int>>& events) {
    std::vector<EventPoint> points;
    for (auto& event : events) {
        points.push_back({event[0], true});
        points.push_back({event[1], false});
    }
    
    std::sort(points.begin(), points.end(), [](const EventPoint& a, const EventPoint& b) {
        if (a.time == b.time) {
            return a.isStart > b.isStart; // End times come before start times if they are equal
        }
        return a.time < b.time;
    });
    
    int maxTriple = 0, current = 0;
    for (auto& point : points) {
        if (point.isStart) {
            current++;
            if (current >= 3) {
                maxTriple = std::max(maxTriple, current);
            }
        } else {
            current--;
        }
    }
    return maxTriple;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of events. This is because we sort the event points, which takes $O(n \log n)$ time.
> - **Space Complexity:** $O(n)$, because we create a new list of event points.
> - **Optimality proof:** This is optimal because we only process each event's start and end time once, and we avoid unnecessary comparisons by sorting the points in time order.