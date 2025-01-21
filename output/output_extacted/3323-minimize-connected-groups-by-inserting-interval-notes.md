## Minimize Connected Groups by Inserting Interval

**Problem Link:** https://leetcode.com/problems/minimize-connected-groups-by-inserting-interval/description

**Problem Statement:**
- Input: An array of integers representing the end times of intervals and a positive integer representing the duration of the interval to be inserted.
- Constraints: The end times are non-negative integers, and the duration is a positive integer.
- Expected Output: The minimum number of connected groups after inserting the interval.
- Key Requirements: The goal is to minimize the number of connected groups by strategically inserting the given interval.
- Edge Cases: Consider cases where the input array is empty, contains a single element, or has multiple elements with the same end time.

**Example Test Cases:**
- Example 1: Input: `endTimes = [1, 3, 4, 6], duration = 2`, Output: `2`. Explanation: Insert the interval at time 2 to cover the intervals ending at times 1 and 3, and another interval at time 5 to cover the intervals ending at times 4 and 6.
- Example 2: Input: `endTimes = [1, 2, 3], duration = 1`, Output: `2`. Explanation: Insert the interval at time 1 to cover the interval ending at time 1, and another interval at time 2 to cover the intervals ending at times 2 and 3.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible insertion points for the interval and calculate the number of connected groups after each insertion.
- Step-by-step breakdown:
  1. Generate all possible insertion points based on the end times and the duration of the interval to be inserted.
  2. For each insertion point, simulate the insertion of the interval and count the number of connected groups.
  3. Keep track of the minimum number of connected groups found across all insertion points.

```cpp
class Solution {
public:
    int minimizeConnectedGroups(vector<int>& endTimes, int duration) {
        int n = endTimes.size();
        sort(endTimes.begin(), endTimes.end());
        
        int minGroups = INT_MAX;
        
        for (int i = 0; i < n; ++i) {
            int groups = 0;
            int lastEndTime = -1;
            
            for (int j = 0; j < n; ++j) {
                if (endTimes[j] > lastEndTime + duration) {
                    groups++;
                    lastEndTime = endTimes[j];
                }
            }
            
            minGroups = min(minGroups, groups);
        }
        
        return minGroups;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of end times. The reason is that for each possible insertion point, we iterate through all end times to count connected groups.
> - **Space Complexity:** $O(1)$, excluding the input array, as we only use a constant amount of space to store variables like `minGroups`, `groups`, and `lastEndTime`.
> - **Why these complexities occur:** The brute force approach involves nested iterations over the input array, leading to quadratic time complexity. The space complexity is constant because we only use a fixed amount of space to store our variables, regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a greedy approach to insert the interval at the earliest possible time that covers the maximum number of intervals.
- Detailed breakdown:
  1. Sort the end times in ascending order.
  2. Initialize the count of connected groups and the end time of the last inserted interval.
  3. Iterate through the sorted end times. For each end time, check if it is not covered by the last inserted interval. If not, increment the count of connected groups and update the end time of the last inserted interval.

```cpp
class Solution {
public:
    int minimizeConnectedGroups(vector<int>& endTimes, int duration) {
        int n = endTimes.size();
        sort(endTimes.begin(), endTimes.end());
        
        int groups = 0;
        int lastEndTime = -1;
        
        for (int i = 0; i < n; ++i) {
            if (endTimes[i] > lastEndTime + duration) {
                groups++;
                lastEndTime = endTimes[i];
            }
        }
        
        return groups;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of end times. The reason is that we first sort the end times, which takes $O(n \log n)$ time, and then iterate through them once, which takes $O(n)$ time.
> - **Space Complexity:** $O(1)$, excluding the input array, as we only use a constant amount of space to store variables like `groups` and `lastEndTime`.
> - **Optimality proof:** This approach is optimal because it ensures that each interval is covered by the earliest possible insertion point, minimizing the number of connected groups.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy algorithm, sorting.
- Problem-solving patterns identified: Finding the optimal insertion point for an interval to minimize connected groups.
- Optimization techniques learned: Using a greedy approach to solve the problem efficiently.
- Similar problems to practice: Other problems involving interval scheduling and greedy algorithms.

**Mistakes to Avoid:**
- Common implementation errors: Failing to sort the end times or not updating the last end time correctly.
- Edge cases to watch for: Handling empty input arrays or arrays with a single element.
- Performance pitfalls: Using a brute force approach that leads to high time complexity.
- Testing considerations: Thoroughly testing the solution with different input scenarios, including edge cases.