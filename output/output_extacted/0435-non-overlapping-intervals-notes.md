## Non-Overlapping Intervals
**Problem Link:** https://leetcode.com/problems/non-overlapping-intervals/description

**Problem Statement:**
- Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
- Input: `int[][] intervals` where `intervals[i] = [start_i, end_i]`
- Expected output: The minimum number of intervals to remove.
- Key requirements and edge cases to consider: 
  - Empty input
  - Intervals with same start and end
  - Intervals that are fully contained within another interval
- Example test cases with explanations:
  - `intervals = [[1,2],[2,3],[3,4],[1,3]]` should return `1` because removing one interval (`[1,3]`) makes the rest non-overlapping.
  - `intervals = [[1,2],[1,2],[1,2]]` should return `2` because removing two intervals makes the rest non-overlapping.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of removing intervals and check if the remaining intervals are non-overlapping.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsets of intervals.
  2. For each subset, check if the intervals are non-overlapping.
  3. Keep track of the minimum number of removed intervals that result in non-overlapping intervals.
- Why this approach comes to mind first: It's a straightforward, albeit inefficient, way to solve the problem by considering all possibilities.

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int eraseOverlapIntervals(std::vector<std::vector<int>>& intervals) {
        if (intervals.empty()) return 0;
        
        int n = intervals.size();
        std::sort(intervals.begin(), intervals.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            return a[1] < b[1];
        });
        
        int end = intervals[0][1];
        int count = 0;
        
        for (int i = 1; i < n; ++i) {
            if (intervals[i][0] < end) {
                count++;
            } else {
                end = intervals[i][1];
            }
        }
        
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting.
> - **Space Complexity:** $O(1)$ excluding the input, as we only use a constant amount of space.
> - **Why these complexities occur:** Sorting is the dominant operation, and we use a simple loop to iterate through the intervals once they are sorted.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Sort the intervals by their end points, and then iterate through them. If an interval overlaps with the previous one, increment the count of intervals to remove. Otherwise, update the end point.
- Detailed breakdown of the approach:
  1. Sort the intervals by their end points.
  2. Initialize the end point and the count of intervals to remove.
  3. Iterate through the sorted intervals. If an interval overlaps with the previous one, increment the count. Otherwise, update the end point.
- Proof of optimality: This approach ensures that we remove the minimum number of intervals to make the rest non-overlapping, as we always choose to keep the interval with the earliest end point.
- Why further optimization is impossible: We must examine each interval at least once to determine if it overlaps with the previous one, making this approach optimal in terms of time complexity.

```cpp
class Solution {
public:
    int eraseOverlapIntervals(std::vector<std::vector<int>>& intervals) {
        if (intervals.empty()) return 0;
        
        int n = intervals.size();
        std::sort(intervals.begin(), intervals.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            return a[1] < b[1];
        });
        
        int end = intervals[0][1];
        int count = 0;
        
        for (int i = 1; i < n; ++i) {
            if (intervals[i][0] < end) {
                count++;
            } else {
                end = intervals[i][1];
            }
        }
        
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting.
> - **Space Complexity:** $O(1)$ excluding the input, as we only use a constant amount of space.
> - **Optimality proof:** This approach is optimal because it ensures that we remove the minimum number of intervals to make the rest non-overlapping, by always choosing to keep the interval with the earliest end point.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, iteration, and greedy choice.
- Problem-solving patterns identified: Using sorting to simplify the problem and then applying a greedy approach.
- Optimization techniques learned: Choosing the optimal data structure (in this case, sorting the intervals) and applying a greedy algorithm to minimize the number of intervals to remove.
- Similar problems to practice: Other interval-related problems, such as merging intervals or finding the maximum number of non-overlapping intervals.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty input or intervals with the same start and end points.
- Edge cases to watch for: Intervals that are fully contained within another interval, or intervals with the same start and end points.
- Performance pitfalls: Using an inefficient sorting algorithm or not considering the greedy approach.
- Testing considerations: Test the function with various inputs, including edge cases, to ensure it works correctly.