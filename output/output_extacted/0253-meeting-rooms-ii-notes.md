## Meeting Rooms II

**Problem Link:** https://leetcode.com/problems/meeting-rooms-ii/description

**Problem Statement:**
- Input format and constraints: Given an array of meeting time intervals `intervals` where `intervals[i] = [starti, endi]`, the start and end times of the i-th meeting, return the minimum number of conference rooms required.
- Expected output format: Integer representing the minimum number of rooms required.
- Key requirements and edge cases to consider:
  - The number of meetings can be up to 1000.
  - Each meeting time interval is in the format `[start, end]`.
  - Meetings can overlap.
  - A meeting room can be used for multiple meetings if there's no overlap.
- Example test cases with explanations:
  - Example 1: Input: `[[0,30],[5,10],[15,20]]`, Output: `2`, Explanation: We need two rooms. One room for [0,30] and another room for [5,10] and [15,20].
  - Example 2: Input: `[[7,10],[2,4]]`, Output: `1`, Explanation: One room is enough since the meetings do not overlap.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we might first think of checking every possible combination of meetings to see which ones can be in the same room and which cannot. However, this approach quickly becomes impractical due to its high time complexity.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of meetings.
  2. For each permutation, try to assign meetings to rooms one by one.
  3. If a meeting cannot be assigned to any existing room (because it overlaps with all meetings in those rooms), create a new room.
  4. Keep track of the minimum number of rooms required across all permutations.
- Why this approach comes to mind first: It's a straightforward, albeit inefficient, way to ensure we consider all possibilities.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

int minMeetingRooms(vector<vector<int>>& intervals) {
    if (intervals.empty()) return 0;
    
    // Sort intervals by start time
    sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] < b[0];
    });
    
    vector<vector<int>> rooms = {intervals[0]};
    
    for (int i = 1; i < intervals.size(); ++i) {
        bool assigned = false;
        for (auto& room : rooms) {
            if (intervals[i][0] >= room[1]) {
                room = intervals[i];
                assigned = true;
                break;
            }
        }
        if (!assigned) {
            rooms.push_back(intervals[i]);
        }
    }
    
    return rooms.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \log N)$ due to sorting, where $N$ is the number of intervals. The subsequent loop has a linear complexity but is dominated by the sorting operation.
> - **Space Complexity:** $O(N)$ for storing the rooms.
> - **Why these complexities occur:** Sorting is necessary to ensure meetings are processed in chronological order, allowing for efficient assignment to rooms. The space complexity is due to the storage of rooms, which in the worst case could be equal to the number of meetings if no meetings overlap.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Utilize a priority queue to keep track of the end times of the meetings. This allows us to efficiently determine when a room becomes available.
- Detailed breakdown of the approach:
  1. Sort the meetings by their start times.
  2. Initialize a priority queue with the end time of the first meeting.
  3. Iterate through the rest of the meetings. For each meeting:
     - If the start time of the current meeting is greater than or equal to the smallest end time in the queue (i.e., a room is available), remove that end time from the queue.
     - Add the end time of the current meeting to the queue.
  4. The size of the queue at the end represents the minimum number of rooms required.
- Proof of optimality: This approach ensures that we always utilize the available rooms first before opening new ones, thus minimizing the total number of rooms needed.
- Why further optimization is impossible: The use of a priority queue allows for the most efficient management of room assignments, given the need to constantly check for room availability and assign meetings to rooms.

```cpp
#include <vector>
#include <queue>
using namespace std;

int minMeetingRooms(vector<vector<int>>& intervals) {
    if (intervals.empty()) return 0;
    
    sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] < b[0];
    });
    
    priority_queue<int, vector<int>, greater<int>> endTimes;
    endTimes.push(intervals[0][1]);
    
    for (int i = 1; i < intervals.size(); ++i) {
        if (intervals[i][0] >= endTimes.top()) {
            endTimes.pop();
        }
        endTimes.push(intervals[i][1]);
    }
    
    return endTimes.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \log N)$ due to sorting and priority queue operations, where $N$ is the number of intervals.
> - **Space Complexity:** $O(N)$ for the priority queue in the worst case.
> - **Optimality proof:** This approach is optimal because it ensures that meetings are assigned to rooms in the most efficient manner possible, minimizing the number of rooms required at any given time.

---

### Final Notes

**Learning Points:**
- The importance of sorting in algorithmic problems to establish a basis for further operations.
- The utility of priority queues in managing dynamic resources, such as meeting rooms, where efficiency of allocation is key.
- The concept of minimizing resources (in this case, rooms) by optimizing their usage based on the temporal relationships between events (meetings).

**Mistakes to Avoid:**
- Not considering the temporal relationship between meetings, leading to incorrect room assignments.
- Failing to utilize data structures like priority queues that can significantly reduce computational complexity.
- Overlooking the need for sorting as a preliminary step to simplify the problem and enable efficient solutions.