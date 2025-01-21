## Divide Intervals into Minimum Number of Groups
**Problem Link:** https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/description

**Problem Statement:**
- Input: A list of intervals where each interval is a pair of integers `[start, end]`.
- Constraints: `1 <= intervals.length <= 10^5`, `0 <= start < end <= 10^5`.
- Expected Output: The minimum number of groups to divide the intervals such that no two intervals in the same group overlap.
- Key Requirements: Find the minimum number of groups that can be formed without overlapping intervals.
- Edge Cases: Empty input, intervals with the same start and end, overlapping intervals.
- Example Test Cases:
  - Input: `[[5,10],[6,8]]`, Output: `2`
  - Input: `[[1,2],[2,3]]`, Output: `2`
  - Input: `[[1,2],[3,4]]`, Output: `2`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible combination of intervals to see if they can be grouped together without overlapping.
- This approach involves using a recursive function to try all possible groupings and count the minimum number of groups required.

```cpp
#include <vector>
using namespace std;

int minGroups(vector<vector<int>>& intervals) {
    int n = intervals.size();
    int res = n;
    
    // Try all possible groupings
    for (int mask = 0; mask < (1 << n); mask++) {
        vector<vector<int>> groups;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                bool added = false;
                for (auto& group : groups) {
                    if (group.back()[1] <= intervals[i][0]) {
                        group.push_back(intervals[i]);
                        added = true;
                        break;
                    }
                }
                if (!added) {
                    groups.push_back({intervals[i]});
                }
            }
        }
        int curr = groups.size();
        if (curr < res) res = curr;
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of intervals. This is because we are trying all possible combinations of intervals.
> - **Space Complexity:** $O(n)$, as we are storing all intervals in memory.
> - **Why these complexities occur:** The brute force approach tries all possible combinations of intervals, resulting in exponential time complexity. The space complexity is linear because we only need to store the intervals.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves sorting the intervals by their end points and then using a priority queue to keep track of the end points of the groups.
- We start by sorting the intervals by their end points. Then, we iterate through the sorted intervals and try to add each interval to an existing group. If we can't add it to any existing group, we create a new group.
- We use a priority queue to keep track of the end points of the groups. The priority queue is ordered by the end points of the groups, so the group with the earliest end point is always at the top.

```cpp
#include <vector>
#include <queue>
using namespace std;

int minGroups(vector<vector<int>>& intervals) {
    if (intervals.empty()) return 0;
    
    sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[1] < b[1];
    });
    
    priority_queue<int, vector<int>, greater<int>> pq;
    pq.push(intervals[0][1]);
    
    for (int i = 1; i < intervals.size(); i++) {
        if (intervals[i][0] >= pq.top()) {
            pq.pop();
        }
        pq.push(intervals[i][1]);
    }
    
    return pq.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of intervals. This is because we are sorting the intervals and using a priority queue.
> - **Space Complexity:** $O(n)$, as we are storing all intervals in memory and using a priority queue.
> - **Optimality proof:** This approach is optimal because it uses a greedy strategy to minimize the number of groups. By sorting the intervals by their end points and using a priority queue, we ensure that we are always adding intervals to the group with the earliest end point, which minimizes the number of groups.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sorting, priority queues, greedy algorithms.
- Problem-solving patterns identified: using a priority queue to keep track of the end points of the groups.
- Optimization techniques learned: using a greedy strategy to minimize the number of groups.

**Mistakes to Avoid:**
- Common implementation errors: not checking for edge cases, not using a priority queue correctly.
- Edge cases to watch for: empty input, intervals with the same start and end, overlapping intervals.
- Performance pitfalls: using a brute force approach, not using a priority queue.
- Testing considerations: testing with different inputs, testing with edge cases.