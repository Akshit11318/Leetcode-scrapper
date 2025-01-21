## My Calendar II
**Problem Link:** https://leetcode.com/problems/my-calendar-ii/description

**Problem Statement:**
- Input format: You are given a list of events where each event is a pair of integers representing the start and end time of the event.
- Constraints: Each event is of the form `[start, end]` where `start` and `end` are integers and `start < end`.
- Expected output format: You need to determine the number of events that have a triple booking, i.e., there is at least one time interval where three events overlap.
- Key requirements and edge cases to consider:
  - Handling overlapping events.
  - Counting the number of triple bookings.
- Example test cases with explanations:
  - Input: `[[10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]`
  - Output: `3`
  - Explanation: There are three intervals where three events overlap: `[10, 15]`, `[10, 20]`, and `[25, 40]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible pair of events to see if they overlap, and then check each pair of overlapping events to see if there's a third event that overlaps with both.
- Step-by-step breakdown of the solution:
  1. Iterate through each event.
  2. For each event, iterate through every other event to check for overlap.
  3. For each pair of overlapping events, iterate through all events again to check for a third overlapping event.
- Why this approach comes to mind first: It's straightforward and ensures we don't miss any potential overlaps.

```cpp
class MyCalendarTwo {
public:
    vector<vector<int>> events;
    vector<vector<int>> overlaps;
    
    bool isOverlap(vector<int>& event1, vector<int>& event2) {
        return event1[0] < event2[1] && event2[0] < event1[1];
    }
    
    int book(int start, int end) {
        vector<int> newEvent = {start, end};
        for (auto& event : events) {
            if (isOverlap(newEvent, event)) {
                vector<int> overlap = {max(newEvent[0], event[0]), min(newEvent[1], event[1])};
                for (auto& overlapEvent : overlaps) {
                    if (isOverlap(overlap, overlapEvent)) {
                        return 0;
                    }
                }
                overlaps.push_back(overlap);
            }
        }
        events.push_back(newEvent);
        return 1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ where $n$ is the number of events. This is because for each event, we potentially iterate through all other events twice.
> - **Space Complexity:** $O(n)$ for storing all events and overlaps.
> - **Why these complexities occur:** The brute force approach involves nested iterations through the list of events, leading to cubic time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking every event against every other event, we can use a sweep line algorithm or a similar approach that takes advantage of the fact that we're dealing with intervals on a line.
- Detailed breakdown of the approach:
  1. Store the start and end times of all events in a single list, marking each time as either a start or an end time.
  2. Sort this list of times.
  3. Iterate through the sorted list, maintaining a count of active events.
  4. When we encounter a start time, increment the count. When we encounter an end time, decrement the count.
  5. If the count ever reaches 3, we've found a triple booking.
- Proof of optimality: This approach ensures we don't miss any overlaps and only requires a single pass through the sorted list of times, making it more efficient than the brute force approach.

```cpp
class MyCalendarTwo {
public:
    vector<vector<int>> events;
    vector<vector<int>> overlaps;
    
    int book(int start, int end) {
        for (auto& event : events) {
            if (start < event[1] && end > event[0]) {
                vector<int> overlap = {max(start, event[0]), min(end, event[1])};
                for (auto& overlapEvent : overlaps) {
                    if (overlapEvent[0] < overlap[1] && overlap[0] < overlapEvent[1]) {
                        return 0;
                    }
                }
                overlaps.push_back(overlap);
            }
        }
        events.push_back({start, end});
        return 1;
    }
};
```

However, for optimal solution we need to implement a different approach using a data structure like a `set` or `map` to keep track of the events.

```cpp
class MyCalendarTwo {
public:
    map<int, int> count;
    
    int book(int start, int end) {
        count[start]++;
        count[end]--;
        int active = 0, ans = 0;
        for (auto& it : count) {
            active += it.second;
            if (active >= 3) ans++;
        }
        count.clear();
        return ans;
    }
};
```
> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of events. This is because we make a single pass through the events.
> - **Space Complexity:** $O(n)$ for storing the count of events.
> - **Optimality proof:** This approach ensures we correctly identify all triple bookings in a single pass, making it optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sweep line algorithm, interval overlap detection.
- Problem-solving patterns identified: Using a data structure to keep track of events, avoiding unnecessary iterations.
- Optimization techniques learned: Reducing the number of iterations, using efficient data structures.
- Similar problems to practice: Other interval-related problems, such as finding the maximum number of non-overlapping intervals.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases, such as events that start and end at the same time.
- Edge cases to watch for: Events that overlap at their start or end times.
- Performance pitfalls: Using inefficient algorithms or data structures, leading to high time or space complexity.
- Testing considerations: Thoroughly testing the implementation with a variety of inputs, including edge cases.