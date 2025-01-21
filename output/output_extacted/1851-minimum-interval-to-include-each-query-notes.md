## Minimum Interval to Include Each Query
**Problem Link:** https://leetcode.com/problems/minimum-interval-to-include-each-query/description

**Problem Statement:**
- Input format: You are given a 2D integer array `intervals` where `intervals[i] = [start_i, end_i]` and a 2D integer array `queries` where `queries[j] = [start_j, end_j]`.
- Constraints: The number of intervals and queries are both between $1$ and $10^5$.
- Expected output format: Return a list of integers `result` where `result[j]` is the minimum interval length such that the interval `[start_j, end_j]` is contained within an interval in `intervals`.
- Key requirements and edge cases to consider: 
  - The intervals in `intervals` do not overlap.
  - The start and end points of the intervals and queries are between $0$ and $10^9$.
  - For each query, there is at least one interval in `intervals` that contains the query interval.
- Example test cases with explanations:
  - Example 1: intervals = `[[1,4],[2,4],[3,6],[4,4]]`, queries = `[[1,3],[1,4],[2,4],[3,6],[3,5],[3,6],[4,4]]`. Expected output: `[2,3,1,3,2,1,1]`.
  - Example 2: intervals = `[[2,3],[2,5],[1,8],[20,25]]`, queries = `[[1,3],[10,11],[2,5],[20,25]]`. Expected output: `[2,-1,3,5]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each query, iterate over all intervals to find the first one that contains the query interval. Then, calculate the length of the found interval.
- Step-by-step breakdown of the solution:
  1. Iterate over each query.
  2. For each query, iterate over all intervals.
  3. Check if the current interval contains the query interval.
  4. If it does, calculate the length of the current interval and store it as the minimum length for the current query.
  5. If no interval contains the query, mark it as `-1`.
- Why this approach comes to mind first: It's straightforward to understand and implement.

```cpp
vector<int> minInterval(vector<vector<int>>& intervals, vector<vector<int>>& queries) {
    vector<int> result(queries.size());
    for (int i = 0; i < queries.size(); ++i) {
        int min_length = INT_MAX;
        for (const auto& interval : intervals) {
            if (interval[0] <= queries[i][0] && queries[i][1] <= interval[1]) {
                min_length = min(min_length, interval[1] - interval[0] + 1);
            }
        }
        result[i] = (min_length == INT_MAX) ? -1 : min_length;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of queries and $m$ is the number of intervals. This is because for each query, we potentially iterate over all intervals.
> - **Space Complexity:** $O(n)$, where $n$ is the number of queries, for storing the result.
> - **Why these complexities occur:** The brute force approach involves nested loops over queries and intervals, leading to the time complexity. The space complexity is due to the storage of the result for each query.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Sort the intervals and queries by their start points. Then, use a binary search to find the first interval that contains each query interval.
- Detailed breakdown of the approach:
  1. Sort the intervals and queries by their start points.
  2. Iterate over each query.
  3. For each query, perform a binary search over the intervals to find the first interval that contains the query interval.
  4. Calculate the length of the found interval and store it as the minimum length for the current query.
- Proof of optimality: This approach reduces the time complexity by avoiding the need to iterate over all intervals for each query, instead using a binary search which is more efficient for finding the first containing interval.

```cpp
vector<int> minInterval(vector<vector<int>>& intervals, vector<vector<int>>& queries) {
    sort(intervals.begin(), intervals.end());
    sort(queries.begin(), queries.end());
    vector<int> result(queries.size());
    for (int i = 0; i < queries.size(); ++i) {
        int left = 0, right = intervals.size() - 1;
        int min_length = INT_MAX;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (intervals[mid][0] <= queries[i][0] && queries[i][1] <= intervals[mid][1]) {
                min_length = min(min_length, intervals[mid][1] - intervals[mid][0] + 1);
                right = mid - 1; // Continue searching for a smaller interval
            } else if (intervals[mid][0] < queries[i][0]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        result[i] = (min_length == INT_MAX) ? -1 : min_length;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log m + m \log m)$, where $n$ is the number of queries and $m$ is the number of intervals. This is because we first sort the intervals and queries ($O(m \log m + n \log n)$), and then for each query, we perform a binary search over the intervals ($O(n \log m)$).
> - **Space Complexity:** $O(n)$, for storing the result.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to find the minimum interval for each query by leveraging the efficiency of binary search.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, binary search.
- Problem-solving patterns identified: Reducing the search space by sorting and using binary search.
- Optimization techniques learned: Avoiding unnecessary iterations by using more efficient algorithms like binary search.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly implementing the binary search or sorting.
- Edge cases to watch for: Queries that are not contained within any interval, or intervals and queries with the same start or end points.
- Performance pitfalls: Using the brute force approach for large inputs due to its high time complexity.
- Testing considerations: Thoroughly test the implementation with various inputs, including edge cases and large datasets.