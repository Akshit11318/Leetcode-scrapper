## Two Best Non-Overlapping Events
**Problem Link:** https://leetcode.com/problems/two-best-non-overlapping-events/description

**Problem Statement:**
- Input format: You are given a list of events where each event is an array of two integers, `start` and `end`, representing the start and end times of an event, respectively. Each event is non-overlapping and unique.
- Input constraints: $1 \leq events.length \leq 10^5$
- Expected output format: The maximum sum of two non-overlapping events.
- Key requirements and edge cases to consider: The events are given in no particular order and may overlap, but the maximum sum should come from two non-overlapping events.

**Example Test Cases:**
- Input: `events = [[1,2],[2,3],[3,4],[1,3]]`
- Output: `7`
- Explanation: Choosing the events `[1,3]` and `[3,4]` yields the maximum sum of `6 + 1 = 7`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Iterate through all pairs of events to find the maximum sum of two non-overlapping events.
- Step-by-step breakdown of the solution:
  1. Sort the events based on their end times.
  2. Iterate through each pair of events.
  3. Check if the events do not overlap by comparing the end time of the first event with the start time of the second event.
  4. If the events do not overlap, calculate their sum and update the maximum sum if necessary.

```cpp
int maxTwoNonOverlappingEvents(vector<vector<int>>& events) {
    // Sort the events based on their end times
    sort(events.begin(), events.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[1] < b[1];
    });
    
    int maxSum = 0;
    
    for (int i = 0; i < events.size(); i++) {
        for (int j = i + 1; j < events.size(); j++) {
            // Check if the events do not overlap
            if (events[i][1] <= events[j][0]) {
                // Calculate the sum and update the maximum sum if necessary
                maxSum = max(maxSum, events[i][1] - events[i][0] + events[j][1] - events[j][0]);
            }
        }
    }
    
    return maxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of events, because we are iterating through all pairs of events.
> - **Space Complexity:** $O(1)$, because we are not using any additional data structures that scale with the input size.
> - **Why these complexities occur:** The brute force approach has a high time complexity due to the nested loops, but it has a low space complexity because it only uses a constant amount of space to store the maximum sum.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of checking all pairs of events, we can use a single pass through the sorted events to keep track of the maximum sum of non-overlapping events.
- Detailed breakdown of the approach:
  1. Sort the events based on their end times.
  2. Initialize a variable `maxSum` to store the maximum sum of non-overlapping events.
  3. Initialize a variable `prevEnd` to store the end time of the previous non-overlapping event.
  4. Iterate through the sorted events.
  5. For each event, check if it does not overlap with the previous non-overlapping event.
  6. If it does not overlap, update `maxSum` and `prevEnd` if necessary.

```cpp
int maxTwoNonOverlappingEvents(vector<vector<int>>& events) {
    // Sort the events based on their end times
    sort(events.begin(), events.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[1] < b[1];
    });
    
    int maxSum = 0;
    int prevEnd = -1;
    
    for (const auto& event : events) {
        // Check if the event does not overlap with the previous non-overlapping event
        if (prevEnd == -1 || event[0] >= prevEnd) {
            // Update maxSum and prevEnd if necessary
            maxSum = max(maxSum, event[1] - event[0]);
            prevEnd = event[1];
        }
    }
    
    // Find the maximum sum of two non-overlapping events
    int secondMaxSum = 0;
    for (const auto& event : events) {
        // Check if the event does not overlap with the previous non-overlapping event
        if (prevEnd == -1 || event[0] >= prevEnd) {
            // Update secondMaxSum if necessary
            secondMaxSum = max(secondMaxSum, event[1] - event[0]);
        }
    }
    
    return maxSum + secondMaxSum;
}
```

However, this is not the optimal solution. The optimal solution should use two variables to keep track of the maximum sum of non-overlapping events.

```cpp
int maxTwoNonOverlappingEvents(vector<vector<int>>& events) {
    // Sort the events based on their end times
    sort(events.begin(), events.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[1] < b[1];
    });
    
    int maxSum = 0;
    int prevMaxSum = 0;
    
    for (const auto& event : events) {
        // Update maxSum and prevMaxSum if necessary
        prevMaxSum = max(prevMaxSum, maxSum + event[1] - event[0]);
        maxSum = max(maxSum, event[1] - event[0]);
    }
    
    return prevMaxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of events, because we are sorting the events.
> - **Space Complexity:** $O(1)$, because we are not using any additional data structures that scale with the input size.
> - **Optimality proof:** The optimal solution has a time complexity of $O(n \log n)$ due to the sorting step, and a space complexity of $O(1)$ because it only uses a constant amount of space to store the maximum sums.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sorting, iteration, and dynamic programming.
- Problem-solving patterns identified: using variables to keep track of maximum sums and end times.
- Optimization techniques learned: reducing the number of iterations and using dynamic programming to avoid redundant calculations.

**Mistakes to Avoid:**
- Common implementation errors: incorrect sorting, incorrect iteration, and incorrect updates of maximum sums.
- Edge cases to watch for: events with the same end time, events with the same start time, and events with zero duration.
- Performance pitfalls: using unnecessary data structures, using unnecessary iterations, and not optimizing the solution.
- Testing considerations: testing with different input sizes, testing with different event durations, and testing with different event overlaps.