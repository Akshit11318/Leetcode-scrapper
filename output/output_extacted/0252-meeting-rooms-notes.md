## Meeting Rooms

**Problem Link:** https://leetcode.com/problems/meeting-rooms/description

**Problem Statement:**
- Input format: An array of `intervals` where each interval is a pair of start and end times for a meeting.
- Constraints: The number of meetings is in the range `[0, 1000]`, and each meeting starts and ends at a distinct time.
- Expected output format: A boolean indicating whether the meetings can be held without conflicts.
- Key requirements and edge cases to consider: 
    - Overlapping meetings (e.g., a meeting from 9:00 to 10:00 and another from 9:30 to 11:00).
    - Adjacent meetings (e.g., a meeting from 9:00 to 10:00 and another from 10:00 to 11:00).
    - Empty input or no meetings.
- Example test cases with explanations:
    - `intervals = [[0, 30], [5, 10], [15, 20]]`: Returns `false` because there are overlapping meetings.
    - `intervals = [[7, 10], [2, 4]]`: Returns `true` because there are no overlapping meetings.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every pair of meetings to see if they overlap.
- Step-by-step breakdown of the solution:
    1. Iterate over each meeting in the `intervals` array.
    2. For each meeting, iterate over the remaining meetings.
    3. Check if the current meeting overlaps with the other meeting.
    4. If an overlap is found, return `false`.
- Why this approach comes to mind first: It's straightforward to compare each pair of meetings to check for overlaps.

```cpp
bool canAttendMeetings(vector<vector<int>>& intervals) {
    // Iterate over each meeting
    for (int i = 0; i < intervals.size(); i++) {
        // Iterate over the remaining meetings
        for (int j = i + 1; j < intervals.size(); j++) {
            // Check if the current meeting overlaps with the other meeting
            if (intervals[i][0] < intervals[j][1] && intervals[j][0] < intervals[i][1]) {
                return false;
            }
        }
    }
    // If no overlaps are found, return true
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of meetings. This is because we're iterating over each pair of meetings.
> - **Space Complexity:** $O(1)$, as we're only using a constant amount of space to store the indices.
> - **Why these complexities occur:** The brute force approach has a high time complexity because it checks every pair of meetings, resulting in a quadratic number of comparisons.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: If we sort the meetings by their start times, we only need to compare each meeting with the previous one to check for overlaps.
- Detailed breakdown of the approach:
    1. Sort the `intervals` array by the start time of each meeting.
    2. Iterate over the sorted meetings.
    3. For each meeting, check if it overlaps with the previous meeting.
    4. If an overlap is found, return `false`.
- Proof of optimality: This approach is optimal because we're only comparing each meeting with the previous one, resulting in a linear number of comparisons.

```cpp
bool canAttendMeetings(vector<vector<int>>& intervals) {
    // Sort the meetings by their start times
    sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] < b[0];
    });
    
    // Iterate over the sorted meetings
    for (int i = 1; i < intervals.size(); i++) {
        // Check if the current meeting overlaps with the previous meeting
        if (intervals[i][0] < intervals[i - 1][1]) {
            return false;
        }
    }
    // If no overlaps are found, return true
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of meetings. This is because we're sorting the meetings.
> - **Space Complexity:** $O(1)$, as we're only using a constant amount of space to store the indices.
> - **Optimality proof:** This approach is optimal because we're only comparing each meeting with the previous one, resulting in a linear number of comparisons after sorting.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting and iterating over an array to check for overlaps.
- Problem-solving patterns identified: Using a sorted array to reduce the number of comparisons.
- Optimization techniques learned: Sorting the input to reduce the time complexity.
- Similar problems to practice: Other problems involving sorting and iterating over an array, such as checking for duplicate elements.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty input array.
- Edge cases to watch for: Meetings with the same start time, meetings with the same end time.
- Performance pitfalls: Using a brute force approach with a high time complexity.
- Testing considerations: Test the function with different input arrays, including edge cases.