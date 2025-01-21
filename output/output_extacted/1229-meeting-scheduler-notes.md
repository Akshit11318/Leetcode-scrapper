## Meeting Scheduler

**Problem Link:** https://leetcode.com/problems/meeting-scheduler/description

**Problem Statement:**
- Input format and constraints: Given the availability of two people, `slots1` and `slots2`, and a duration `duration`, find all common time slots that can accommodate a meeting of the given duration.
- Expected output format: Return a list of all possible meeting time slots in the form of pairs of start and end times.
- Key requirements and edge cases to consider: 
  - A meeting time slot is defined by a start time and an end time.
  - The duration of a meeting time slot must be equal to the given duration.
  - The meeting time slot must be fully contained within the availability of both people.
- Example test cases with explanations:
  - Example 1: `slots1 = [[10,50],[60,120],[140,210]]`, `slots2 = [[0,15],[60,70]]`, `duration = 8`, Output: `[[60,68]]`.
  - Example 2: `slots1 = [[10,50],[60,120],[140,210]]`, `slots2 = [[0,15],[60,70]]`, `duration = 12`, Output: `[]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves checking every possible time slot in the availability of both people to see if it can accommodate a meeting of the given duration.
- Step-by-step breakdown of the solution:
  1. Generate all possible time slots of the given duration within the availability of the first person.
  2. For each time slot, check if it is fully contained within the availability of the second person.
  3. If a time slot is found to be common to both people, add it to the result list.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, as it involves checking every possible time slot.

```cpp
#include <vector>
using namespace std;

vector<vector<int>> meetingScheduler(vector<vector<int>>& slots1, vector<vector<int>>& slots2, int duration) {
    vector<vector<int>> result;
    for (auto& slot1 : slots1) {
        for (int start = slot1[0]; start <= slot1[1] - duration; start++) {
            int end = start + duration;
            for (auto& slot2 : slots2) {
                if (start >= slot2[0] && end <= slot2[1]) {
                    result.push_back({start, end});
                    break;
                }
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot d)$, where $n$ is the number of time slots in `slots1`, $m$ is the number of time slots in `slots2`, and $d$ is the duration of the meeting. This is because we are generating all possible time slots of the given duration within the availability of the first person and then checking each one against the availability of the second person.
> - **Space Complexity:** $O(r)$, where $r$ is the number of common time slots found. This is because we are storing the result in a vector.
> - **Why these complexities occur:** These complexities occur because we are using nested loops to generate and check all possible time slots.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible time slots of the given duration within the availability of the first person, we can use two pointers to find the common time slots.
- Detailed breakdown of the approach:
  1. Sort the time slots in `slots1` and `slots2` by their start times.
  2. Initialize two pointers, one for `slots1` and one for `slots2`.
  3. Move the pointers forward until we find a common time slot that can accommodate a meeting of the given duration.
  4. If a common time slot is found, add it to the result list and move the pointers forward.
- Proof of optimality: This approach is optimal because we are using two pointers to find the common time slots, which reduces the time complexity to $O(n + m)$.

```cpp
#include <vector>
using namespace std;

vector<vector<int>> meetingScheduler(vector<vector<int>>& slots1, vector<vector<int>>& slots2, int duration) {
    vector<vector<int>> result;
    int i = 0, j = 0;
    while (i < slots1.size() && j < slots2.size()) {
        int start = max(slots1[i][0], slots2[j][0]);
        int end = min(slots1[i][1], slots2[j][1]);
        if (end - start >= duration) {
            result.push_back({start, start + duration});
        }
        if (slots1[i][1] < slots2[j][1]) {
            i++;
        } else {
            j++;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of time slots in `slots1` and $m$ is the number of time slots in `slots2`. This is because we are using two pointers to find the common time slots.
> - **Space Complexity:** $O(r)$, where $r$ is the number of common time slots found. This is because we are storing the result in a vector.
> - **Optimality proof:** This approach is optimal because we are using two pointers to find the common time slots, which reduces the time complexity to $O(n + m)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two pointers technique.
- Problem-solving patterns identified: Finding common time slots.
- Optimization techniques learned: Reducing time complexity by using two pointers.
- Similar problems to practice: Finding common elements in two arrays.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases.
- Edge cases to watch for: Empty input arrays.
- Performance pitfalls: Using nested loops to find common time slots.
- Testing considerations: Test the function with different input arrays and durations.