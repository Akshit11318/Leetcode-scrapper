## Merge Intervals

**Problem Link:** https://leetcode.com/problems/merge-intervals/description

**Problem Statement:**
- Input format: An array of intervals where each interval is an array of two integers, `start` and `end`, representing the start and end of the interval.
- Constraints: The input array `intervals` is not empty and contains at most `10^4` intervals.
- Expected output format: The merged intervals as an array of arrays, where each inner array contains the start and end of a merged interval.
- Key requirements and edge cases to consider:
  - Intervals can be merged if they overlap, i.e., the end of one interval is greater than or equal to the start of another.
  - The start of the merged interval is the minimum of the starts of the two intervals to be merged.
  - The end of the merged interval is the maximum of the ends of the two intervals to be merged.
  - If two intervals do not overlap, they should not be merged.
- Example test cases with explanations:
  - `intervals = [[1,3],[2,6],[8,10],[15,18]]`: Merged intervals should be `[[1,6],[8,10],[15,18]]`.
  - `intervals = [[1,4],[4,5]]`: Merged intervals should be `[[1,5]]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Compare each interval with every other interval to check for overlap.
- Step-by-step breakdown of the solution:
  1. Iterate over each interval in the input array.
  2. For each interval, iterate over the remaining intervals in the array.
  3. Check if the current interval overlaps with the compared interval.
  4. If they overlap, merge them and update the current interval.
  5. After comparing all intervals, add the merged interval to the result array if it's not already included.
- Why this approach comes to mind first: It's the most straightforward way to ensure all intervals are compared for overlap.

```cpp
vector<vector<int>> mergeBrute(vector<vector<int>>& intervals) {
    vector<vector<int>> result;
    for (int i = 0; i < intervals.size(); ++i) {
        bool merged = false;
        for (int j = 0; j < result.size(); ++j) {
            if (intervals[i][0] <= result[j][1] && intervals[i][1] >= result[j][0]) {
                result[j][0] = min(intervals[i][0], result[j][0]);
                result[j][1] = max(intervals[i][1], result[j][1]);
                merged = true;
                break;
            }
        }
        if (!merged) {
            result.push_back(intervals[i]);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the number of intervals, because for each interval, we potentially compare it with every other interval.
> - **Space Complexity:** $O(n)$ for storing the merged intervals in the result array.
> - **Why these complexities occur:** The nested loop structure leads to quadratic time complexity, and we need additional space to store the merged intervals.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Sort the intervals by their start times. This allows us to merge overlapping intervals in a single pass.
- Detailed breakdown of the approach:
  1. Sort the input intervals based on their start times.
  2. Initialize the result array with the first interval.
  3. Iterate through the remaining intervals. For each interval, check if it overlaps with the last interval in the result array.
  4. If they overlap, merge them by updating the end of the last interval in the result array.
  5. If they do not overlap, add the current interval to the result array.
- Proof of optimality: This approach ensures that we only need to compare each interval with the last merged interval, reducing the time complexity to linear after sorting.

```cpp
vector<vector<int>> mergeOptimal(vector<vector<int>>& intervals) {
    if (intervals.empty()) return {};
    sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] < b[0];
    });
    vector<vector<int>> result = {intervals[0]};
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
> - **Time Complexity:** $O(n \log n)$ due to sorting, where $n$ is the number of intervals. The subsequent for loop is $O(n)$, but it's dominated by the sorting step.
> - **Space Complexity:** $O(n)$ for storing the merged intervals in the result array.
> - **Optimality proof:** This is optimal because we must at least look at each interval once, and sorting allows us to do this in a way that minimizes the number of comparisons needed to merge intervals.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting and iterating through sorted data to solve the problem efficiently.
- Problem-solving patterns identified: Recognizing that sorting can simplify the comparison process in problems involving intervals or ranges.
- Optimization techniques learned: Using sorting to reduce the time complexity of comparing intervals.
- Similar problems to practice: Other interval-related problems, such as inserting intervals or finding the intersection of intervals.

**Mistakes to Avoid:**
- Common implementation errors: Not correctly handling edge cases, such as empty input arrays or intervals with the same start and end times.
- Edge cases to watch for: Empty input, single-element input, and intervals that are already merged.
- Performance pitfalls: Using a brute force approach for large inputs, which can lead to high time complexity.
- Testing considerations: Thoroughly testing the function with various inputs, including edge cases, to ensure correctness.