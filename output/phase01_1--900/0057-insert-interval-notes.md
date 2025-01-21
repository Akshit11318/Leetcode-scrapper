## Insert Interval
**Problem Link:** [https://leetcode.com/problems/insert-interval/description](https://leetcode.com/problems/insert-interval/description)

**Problem Statement:**
- Input: A list of non-overlapping intervals `intervals` and a new interval `newInterval`.
- Constraints: `intervals` is a list of pairs of integers where `intervals[i][0] < intervals[i][1]`, and `newInterval` is also a pair of integers.
- Expected Output: The merged list of intervals after inserting `newInterval` into `intervals`.
- Key Requirements and Edge Cases:
  - Handle overlapping intervals.
  - Consider cases where `newInterval` is before, after, or within `intervals`.
  - Ensure non-overlapping intervals in the result.

Example Test Cases:
- `intervals = [[1,3],[6,9]]`, `newInterval = [2,5]`, result: `[[1,5],[6,9]]`.
- `intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]`, `newInterval = [4,8]`, result: `[[1,2],[3,10],[12,16]]`.
- `intervals = []`, `newInterval = [5,7]`, result: `[[5,7]]`.
- `intervals = [[1,5]]`, `newInterval = [2,3]`, result: `[[1,5]]`.
- `intervals = [[1,5]]`, `newInterval = [6,8]`, result: `[[1,5],[6,8]]`.

---

### Brute Force Approach
**Explanation:**
- Start by adding `newInterval` to `intervals`.
- Then, sort `intervals` based on the start value of each interval.
- Iterate through `intervals` and merge any overlapping intervals.
- This approach comes to mind first because it directly addresses the problem statement without requiring complex optimizations.

```cpp
vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
    intervals.push_back(newInterval);
    sort(intervals.begin(), intervals.end());
    vector<vector<int>> result;
    result.push_back(intervals[0]);
    for (int i = 1; i < intervals.size(); ++i) {
        if (intervals[i][0] <= result.back()[1]) {
            result.back()[1] = max(result.back()[1], intervals[i][1]);
        } else {
            result.push_back(intervals[i]);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation, where $n$ is the number of intervals.
> - **Space Complexity:** $O(n)$ for storing the merged intervals.
> - **Why these complexities occur:** The sorting step dominates the time complexity, while the space complexity comes from storing the result.

---

### Optimal Approach (Required)
**Explanation:**
- The provided brute force approach is already optimal for this problem because it correctly merges intervals in a single pass after sorting, which is necessary for handling overlapping intervals efficiently.
- No further optimization is possible without changing the problem's constraints.

```cpp
// Same as the brute force approach, as it's already optimal.
vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
    intervals.push_back(newInterval);
    sort(intervals.begin(), intervals.end());
    vector<vector<int>> result;
    result.push_back(intervals[0]);
    for (int i = 1; i < intervals.size(); ++i) {
        if (intervals[i][0] <= result.back()[1]) {
            result.back()[1] = max(result.back()[1], intervals[i][1]);
        } else {
            result.push_back(intervals[i]);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting.
> - **Space Complexity:** $O(n)$ for the result.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to merge overlapping intervals after a necessary sorting step.

---

### Final Notes

**Learning Points:**
- Importance of sorting in interval-related problems.
- Merging intervals efficiently.
- Understanding time and space complexities.
- Identifying when a brute force approach is already optimal.

**Mistakes to Avoid:**
- Not handling edge cases, such as an empty `intervals` list.
- Failing to sort intervals before merging.
- Incorrectly merging overlapping intervals.
- Not considering the impact of sorting on time complexity.

---