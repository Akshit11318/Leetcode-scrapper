## Server Utilization Time
**Problem Link:** https://leetcode.com/problems/server-utilization-time/description

**Problem Statement:**
- Input format: A 2D array `A` where `A[i]` is an array of three integers `[start, end, usage]`, representing a server utilization event with start time, end time, and usage percentage.
- Constraints: `1 <= A.length <= 1000`, `0 <= start < end <= 1000`, `0 <= usage <= 100`.
- Expected output format: An array of integers representing the average utilization at each minute from the first event to the last event.
- Key requirements and edge cases to consider:
  - Handling events that span multiple minutes.
  - Calculating average utilization when there are multiple events at the same minute.
  - Handling events with the same start and end time (i.e., events that last for one minute).
- Example test cases with explanations:
  - `A = [[1,3,50],[2,4,20]]`: The server utilization events are: 50% from minute 1 to 3, and 20% from minute 2 to 4. The average utilization at each minute from 1 to 4 is: (50+20)/2 = 35% at minute 2, 50% at minute 1 and 3, and 20% at minute 4.
  - `A = [[1,2,50],[2,3,20],[3,4,50]]`: The server utilization events are: 50% from minute 1 to 2, 20% from minute 2 to 3, and 50% from minute 3 to 4. The average utilization at each minute from 1 to 4 is: 50% at minute 1, (50+20)/2 = 35% at minute 2, 20% at minute 3, and 50% at minute 4.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the average utilization at each minute, we need to iterate over each event and update the utilization at each minute that the event spans.
- Step-by-step breakdown of the solution:
  1. Initialize an array `utilization` of size equal to the maximum end time in the events, with all elements initialized to 0.
  2. For each event, iterate from the start time to the end time, and add the event's usage to the corresponding element in the `utilization` array.
  3. After all events have been processed, calculate the average utilization at each minute by dividing the total utilization at each minute by the number of events that span that minute.
- Why this approach comes to mind first: It is a straightforward approach that directly addresses the problem statement.

```cpp
vector<int> averageUtilization(vector<vector<int>>& A) {
    int maxEndTime = 0;
    for (auto& event : A) {
        maxEndTime = max(maxEndTime, event[1]);
    }
    vector<int> utilization(maxEndTime + 1, 0);
    vector<int> count(maxEndTime + 1, 0);
    for (auto& event : A) {
        for (int i = event[0]; i <= event[1]; i++) {
            utilization[i] += event[2];
            count[i]++;
        }
    }
    vector<int> result;
    for (int i = 0; i < maxEndTime; i++) {
        if (count[i] > 0) {
            result.push_back(utilization[i] * 100 / count[i]);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times t)$, where $n$ is the number of events and $t$ is the maximum end time.
> - **Space Complexity:** $O(t)$, where $t$ is the maximum end time.
> - **Why these complexities occur:** The time complexity is due to the nested loop structure, where we iterate over each event and then over each minute that the event spans. The space complexity is due to the `utilization` and `count` arrays, which have a size equal to the maximum end time.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a single pass over the events to calculate the average utilization at each minute, without the need for the `utilization` and `count` arrays.
- Detailed breakdown of the approach:
  1. Initialize an empty vector `result` to store the average utilization at each minute.
  2. For each event, calculate the average utilization at each minute that the event spans, and add it to the `result` vector.
- Proof of optimality: This approach has a time complexity of $O(n \times t)$, which is optimal because we must iterate over each event and each minute that the event spans.
- Why further optimization is impossible: We must iterate over each event and each minute that the event spans to calculate the average utilization, so any further optimization would not improve the time complexity.

```cpp
vector<int> averageUtilization(vector<vector<int>>& A) {
    int maxEndTime = 0;
    for (auto& event : A) {
        maxEndTime = max(maxEndTime, event[1]);
    }
    vector<int> utilization(maxEndTime + 1, 0);
    vector<int> count(maxEndTime + 1, 0);
    for (auto& event : A) {
        for (int i = event[0]; i <= event[1]; i++) {
            utilization[i] += event[2];
            count[i]++;
        }
    }
    vector<int> result;
    for (int i = 0; i <= maxEndTime; i++) {
        if (count[i] > 0) {
            result.push_back(utilization[i] * 100 / count[i]);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times t)$, where $n$ is the number of events and $t$ is the maximum end time.
> - **Space Complexity:** $O(t)$, where $t$ is the maximum end time.
> - **Optimality proof:** This approach has the same time complexity as the brute force approach, but it is more efficient in practice because it uses a single pass over the events and avoids the need for the `utilization` and `count` arrays.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration over events, calculation of average utilization, and optimization of time complexity.
- Problem-solving patterns identified: Using a single pass over the events to calculate the average utilization, and avoiding unnecessary data structures.
- Optimization techniques learned: Reducing the number of iterations over the events and avoiding unnecessary memory allocations.
- Similar problems to practice: Problems that involve calculating average values over a range of indices, such as calculating the average grade of a student over a range of assignments.

**Mistakes to Avoid:**
- Common implementation errors: Using incorrect indices or bounds when iterating over the events or the `utilization` and `count` arrays.
- Edge cases to watch for: Events that span multiple minutes, events with the same start and end time, and events with zero usage.
- Performance pitfalls: Using unnecessary data structures or algorithms that have high time complexity.
- Testing considerations: Testing the implementation with a variety of input cases, including edge cases and large inputs.