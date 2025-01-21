## Remove Covered Intervals

**Problem Link:** https://leetcode.com/problems/remove-covered-intervals/description

**Problem Statement:**
- Input format: A list of intervals where each interval is a list of two integers, `start` and `end`.
- Constraints: Each interval is non-empty and `start` is less than or equal to `end`.
- Expected output format: The number of non-covered intervals.
- Key requirements and edge cases to consider:
  - An interval `(a, b)` is covered by another interval `(c, d)` if `c <= a` and `b <= d`.
  - If an interval is not covered by any other interval, it is considered non-covered.
- Example test cases with explanations:
  - `intervals = [[1,4],[3,6],[2,8]]`, the output is `2`. Intervals `(3, 6)` and `(1, 4)` are covered by `(2, 8)`.
  - `intervals = [[1,4],[2,3]]`, the output is `1`. Interval `(2, 3)` is covered by `(1, 4)`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each interval, check if it is covered by any other interval.
- Step-by-step breakdown of the solution:
  1. Sort the intervals based on their start value.
  2. Iterate through each interval.
  3. For each interval, check if it is covered by any other interval.
  4. Count the intervals that are not covered.
- Why this approach comes to mind first: It directly checks each interval against every other interval, ensuring no covered interval is missed.

```cpp
int removeCoveredIntervals(vector<vector<int>>& intervals) {
    int count = 0;
    for (int i = 0; i < intervals.size(); i++) {
        bool isCovered = false;
        for (int j = 0; j < intervals.size(); j++) {
            if (i != j && intervals[j][0] <= intervals[i][0] && intervals[i][1] <= intervals[j][1]) {
                isCovered = true;
                break;
            }
        }
        if (!isCovered) count++;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of intervals. This is because for each interval, we potentially check every other interval.
> - **Space Complexity:** $O(1)$, excluding the input, as we only use a constant amount of space to store our variables.
> - **Why these complexities occur:** The nested loop structure leads to the quadratic time complexity, while the use of a fixed amount of space for variables results in constant space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Sort the intervals by their start value and then by their end value in descending order. This way, if two intervals have the same start value, the one with the larger end value comes first.
- Detailed breakdown of the approach:
  1. Sort the intervals based on the start value and then by the end value in descending order.
  2. Initialize variables to keep track of the current end value and the count of non-covered intervals.
  3. Iterate through the sorted intervals, updating the current end value and the count as necessary.
- Proof of optimality: This approach ensures that we only need to make one pass through the intervals, resulting in a linear time complexity.

```cpp
int removeCoveredIntervals(vector<vector<int>>& intervals) {
    sort(intervals.begin(), intervals.end(), [](vector<int>& a, vector<int>& b) {
        if (a[0] == b[0]) return a[1] > b[1];
        return a[0] < b[0];
    });
    int count = 0;
    int currEnd = -1;
    for (auto& interval : intervals) {
        if (interval[1] > currEnd) {
            count++;
            currEnd = interval[1];
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, due to the sorting operation.
> - **Space Complexity:** $O(1)$, excluding the input, as we only use a constant amount of space for our variables.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the sorted intervals, minimizing the number of operations needed to find non-covered intervals.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting and iteration through intervals.
- Problem-solving patterns identified: The use of sorting to simplify the problem and reduce the number of operations.
- Optimization techniques learned: Reducing the number of comparisons by sorting intervals based on specific criteria.
- Similar problems to practice: Problems involving intervals and comparisons, such as merging intervals or finding overlapping intervals.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect sorting criteria or failing to update the current end value correctly.
- Edge cases to watch for: Intervals with the same start value but different end values, or intervals that are not covered by any other interval.
- Performance pitfalls: Using a brute force approach that results in quadratic time complexity.
- Testing considerations: Ensuring that the solution works correctly for different input sizes and edge cases.