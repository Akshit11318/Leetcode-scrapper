## Remove Interval
**Problem Link:** https://leetcode.com/problems/remove-interval/description

**Problem Statement:**
- Input: An array of intervals `intervals` where `intervals[i] = [start_i, end_i]`, and an interval `toBeRemoved`.
- Constraints: `1 <= intervals.length <= 10^5`, `0 <= start_i < end_i <= 10^5`, `0 <= start < end <= 10^5`.
- Expected Output: The array of intervals after removing `toBeRemoved` from `intervals`.
- Key Requirements: Remove the interval `toBeRemoved` from the array of intervals `intervals`. If an interval overlaps with `toBeRemoved`, it should be split into two intervals.
- Example Test Cases:
  - Input: `intervals = [[0,2],[3,4],[5,7]]`, `toBeRemoved = [1,6]`.
    - Output: `[[0,1],[6,7]]`.
  - Input: `intervals = [[0,5]],[2,3]`.
    - Output: `[[0,2],[3,5]]`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to iterate through each interval in `intervals` and check if it overlaps with `toBeRemoved`.
- For each overlapping interval, split it into two intervals: one that starts before `toBeRemoved` and one that ends after `toBeRemoved`.
- If an interval does not overlap with `toBeRemoved`, add it to the result as is.

```cpp
vector<vector<int>> removeInterval(vector<vector<int>>& intervals, vector<int>& toBeRemoved) {
    vector<vector<int>> result;
    for (auto& interval : intervals) {
        if (interval[1] < toBeRemoved[0] || interval[0] > toBeRemoved[1]) {
            result.push_back(interval);
        } else {
            if (interval[0] < toBeRemoved[0]) {
                result.push_back({interval[0], toBeRemoved[0]});
            }
            if (interval[1] > toBeRemoved[1]) {
                result.push_back({toBeRemoved[1], interval[1]});
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of intervals. This is because we are iterating through each interval once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of intervals. This is because in the worst case, we might have to add every interval to the result.
> - **Why these complexities occur:** These complexities occur because we are doing a constant amount of work for each interval.

---

### Optimal Approach (Required)
The provided brute force approach is actually the optimal solution for this problem. It has a linear time complexity and is straightforward to implement.

```cpp
vector<vector<int>> removeInterval(vector<vector<int>>& intervals, vector<int>& toBeRemoved) {
    vector<vector<int>> result;
    for (auto& interval : intervals) {
        if (interval[1] < toBeRemoved[0] || interval[0] > toBeRemoved[1]) {
            result.push_back(interval);
        } else {
            if (interval[0] < toBeRemoved[0]) {
                result.push_back({interval[0], toBeRemoved[0]});
            }
            if (interval[1] > toBeRemoved[1]) {
                result.push_back({toBeRemoved[1], interval[1]});
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of intervals. This is because we are iterating through each interval once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of intervals. This is because in the worst case, we might have to add every interval to the result.
> - **Optimality proof:** This is the optimal solution because we must examine each interval at least once to determine if it overlaps with `toBeRemoved`.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional statements, and interval manipulation.
- Problem-solving patterns identified: Checking for overlap between intervals and splitting intervals accordingly.
- Optimization techniques learned: The solution is already optimal with a linear time complexity.

**Mistakes to Avoid:**
- Not checking for the case where an interval does not overlap with `toBeRemoved`.
- Not handling the case where an interval overlaps with `toBeRemoved` but does not completely contain it.
- Not considering the edge cases where `toBeRemoved` is completely outside the range of an interval or completely contains an interval.

By following this solution, you should be able to efficiently remove an interval from an array of intervals and handle overlapping intervals correctly.