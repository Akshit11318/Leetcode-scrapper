## Meeting Rooms III

**Problem Link:** https://leetcode.com/problems/meeting-rooms-iii/description

**Problem Statement:**
- Input format: `int[][] intervals`, where `intervals[i] = [start_i, end_i]` and `int n`, the number of meeting rooms.
- Constraints: `1 <= n <= 1000`, `1 <= intervals.length <= 1000`, `0 <= start_i < end_i <= 10^9`.
- Expected output format: The minimum number of meeting rooms required to accommodate all the meetings.
- Key requirements and edge cases to consider: The meetings are non-overlapping within the same room, and we need to find the minimum number of rooms required to accommodate all the meetings.
- Example test cases with explanations:
  - Example 1: `intervals = [[0,30],[5,10],[15,20]]`, `n = 2`. Output: `2`.
  - Example 2: `intervals = [[7,10],[2,4]]`, `n = 1`. Output: `1`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Sort the meetings by their start times and then try to accommodate each meeting in the available rooms.
- Step-by-step breakdown of the solution:
  1. Sort the meetings by their start times.
  2. Initialize an array to store the end times of the meetings in each room.
  3. Iterate through the sorted meetings and try to accommodate each meeting in the available rooms.
  4. If a room is available, update the end time of the meeting in that room.
  5. If no room is available, add a new room and update the end time of the meeting in that room.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it may not be the most efficient solution.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int minMeetingRooms(std::vector<std::vector<int>>& intervals) {
    if (intervals.empty()) return 0;

    std::sort(intervals.begin(), intervals.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
        return a[0] < b[0];
    });

    std::vector<int> endTimes;
    for (const auto& interval : intervals) {
        bool foundRoom = false;
        for (int i = 0; i < endTimes.size(); ++i) {
            if (endTimes[i] <= interval[0]) {
                endTimes[i] = interval[1];
                foundRoom = true;
                break;
            }
        }
        if (!foundRoom) {
            endTimes.push_back(interval[1]);
        }
    }

    return endTimes.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of meetings. This is because we are iterating through the meetings and for each meeting, we are iterating through the available rooms.
> - **Space Complexity:** $O(n)$, where $n$ is the number of meetings. This is because we are storing the end times of the meetings in each room.
> - **Why these complexities occur:** The time complexity occurs because of the nested loops, and the space complexity occurs because we are storing the end times of the meetings in each room.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a priority queue to store the end times of the meetings in each room. This allows us to efficiently find the room with the earliest end time.
- Detailed breakdown of the approach:
  1. Sort the meetings by their start times.
  2. Initialize a priority queue to store the end times of the meetings in each room.
  3. Iterate through the sorted meetings and try to accommodate each meeting in the available rooms.
  4. If the priority queue is not empty and the earliest end time is less than or equal to the start time of the current meeting, remove the earliest end time from the priority queue and update the end time of the meeting in that room.
  5. Add the end time of the current meeting to the priority queue.
- Proof of optimality: This approach is optimal because we are always trying to accommodate the current meeting in the room with the earliest end time.

```cpp
#include <iostream>
#include <vector>
#include <queue>

int minMeetingRooms(std::vector<std::vector<int>>& intervals) {
    if (intervals.empty()) return 0;

    std::sort(intervals.begin(), intervals.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
        return a[0] < b[0];
    });

    std::priority_queue<int, std::vector<int>, std::greater<int>> endTimes;
    for (const auto& interval : intervals) {
        if (!endTimes.empty() && endTimes.top() <= interval[0]) {
            endTimes.pop();
        }
        endTimes.push(interval[1]);
    }

    return endTimes.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of meetings. This is because we are sorting the meetings and using a priority queue to store the end times.
> - **Space Complexity:** $O(n)$, where $n$ is the number of meetings. This is because we are storing the end times of the meetings in the priority queue.
> - **Optimality proof:** This approach is optimal because we are always trying to accommodate the current meeting in the room with the earliest end time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, priority queue, and greedy algorithm.
- Problem-solving patterns identified: Finding the minimum number of resources required to accommodate all the requests.
- Optimization techniques learned: Using a priority queue to efficiently find the room with the earliest end time.
- Similar problems to practice: Scheduling problems, resource allocation problems.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where the input is empty, not checking for edge cases.
- Edge cases to watch for: The case where the input is empty, the case where the meetings are non-overlapping.
- Performance pitfalls: Using a brute force approach, not using a priority queue to store the end times.
- Testing considerations: Testing the function with different inputs, testing the function with edge cases.