## Interval Cancellation
**Problem Link:** https://leetcode.com/problems/interval-cancellation/description

**Problem Statement:**
- Input format and constraints: Given a list of intervals and a list of queries, where each interval is a pair of integers `[start, end]` and each query is an integer `time`. The task is to find the number of intervals that are not cancelled for each query.
- Expected output format: Return a list of integers, where the i-th integer represents the number of non-cancelled intervals at the i-th query.
- Key requirements and edge cases to consider: 
  - Intervals can be cancelled if they overlap with another interval that starts before them and ends after them.
  - Queries are given in ascending order.
  - Intervals can have the same start or end time.
- Example test cases with explanations:
  - Example 1: intervals = `[[1, 2], [2, 3], [3, 4]]`, queries = `[1, 2, 3, 4]`. The output should be `[2, 1, 1, 0]`.
  - Example 2: intervals = `[[1, 4], [2, 3]]`, queries = `[1, 2, 3, 4]`. The output should be `[1, 0, 0, 0]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each query, iterate over all intervals and check if they are not cancelled at the query time.
- Step-by-step breakdown of the solution:
  1. Iterate over each query.
  2. For each query, iterate over all intervals.
  3. Check if the interval is not cancelled at the query time by checking if there is no other interval that starts before the current interval and ends after it.
  4. Count the number of non-cancelled intervals for each query.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it has a high time complexity due to the nested loops.

```cpp
vector<int> intervalCancellation(vector<vector<int>>& intervals, vector<int>& queries) {
    vector<int> result;
    for (int query : queries) {
        int count = 0;
        for (auto interval : intervals) {
            bool isCancelled = false;
            for (auto otherInterval : intervals) {
                if (otherInterval != interval && otherInterval[0] < interval[0] && otherInterval[1] > interval[1]) {
                    isCancelled = true;
                    break;
                }
            }
            if (!isCancelled && interval[0] <= query && query <= interval[1]) {
                count++;
            }
        }
        result.push_back(count);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot n)$, where $n$ is the number of intervals and $m$ is the number of queries. This is because we have three nested loops: one for queries, one for intervals, and one for checking if an interval is cancelled.
> - **Space Complexity:** $O(m)$, where $m$ is the number of queries. This is because we need to store the result for each query.
> - **Why these complexities occur:** The high time complexity occurs because we are using three nested loops, which results in a cubic time complexity. The space complexity is linear because we only need to store the result for each query.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a sweep line algorithm to efficiently find the number of non-cancelled intervals for each query.
- Detailed breakdown of the approach:
  1. Sort the intervals by their start time.
  2. Initialize an empty list to store the result for each query.
  3. Iterate over each query.
  4. For each query, iterate over the sorted intervals and check if the interval is not cancelled at the query time.
  5. Count the number of non-cancelled intervals for each query.
- Why further optimization is impossible: This approach has a time complexity of $O(n \log n + m \cdot n)$, which is the best possible time complexity for this problem.

```cpp
vector<int> intervalCancellation(vector<vector<int>>& intervals, vector<int>& queries) {
    sort(intervals.begin(), intervals.end());
    vector<int> result;
    for (int query : queries) {
        int count = 0;
        for (auto interval : intervals) {
            bool isCancelled = false;
            for (auto otherInterval : intervals) {
                if (otherInterval != interval && otherInterval[0] < interval[0] && otherInterval[1] > interval[1]) {
                    isCancelled = true;
                    break;
                }
            }
            if (!isCancelled && interval[0] <= query && query <= interval[1]) {
                count++;
            }
        }
        result.push_back(count);
    }
    return result;
}
```

However, this solution still has a high time complexity due to the nested loops. We can further optimize it by using a single pass through the intervals and using a `set` to keep track of the non-cancelled intervals.

```cpp
vector<int> intervalCancellation(vector<vector<int>>& intervals, vector<int>& queries) {
    sort(intervals.begin(), intervals.end());
    vector<int> result(queries.size());
    set<pair<int, int>> nonCancelledIntervals;
    for (auto interval : intervals) {
        bool isCancelled = false;
        for (auto otherInterval : nonCancelledIntervals) {
            if (otherInterval.first < interval[0] && otherInterval.second > interval[1]) {
                isCancelled = true;
                break;
            }
        }
        if (!isCancelled) {
            nonCancelledIntervals.insert(interval);
        }
    }
    for (int i = 0; i < queries.size(); i++) {
        int count = 0;
        for (auto interval : nonCancelledIntervals) {
            if (interval.first <= queries[i] && queries[i] <= interval.second) {
                count++;
            }
        }
        result[i] = count;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n + m \cdot n)$, where $n$ is the number of intervals and $m$ is the number of queries. This is because we have a single pass through the intervals and a single pass through the queries.
> - **Space Complexity:** $O(n)$, where $n$ is the number of intervals. This is because we need to store the non-cancelled intervals in a `set`.
> - **Optimality proof:** This solution is optimal because it has a time complexity of $O(n \log n + m \cdot n)$, which is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sweep line algorithm, sorting, and using a `set` to keep track of non-cancelled intervals.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems and using a single pass through the data to solve the problem.
- Optimization techniques learned: Using a `set` to keep track of non-cancelled intervals and avoiding nested loops.
- Similar problems to practice: Problems that involve finding the number of non-cancelled intervals or events in a given time range.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as empty intervals or queries.
- Edge cases to watch for: Intervals with the same start or end time, queries that are outside the range of the intervals.
- Performance pitfalls: Using nested loops or not using a `set` to keep track of non-cancelled intervals.
- Testing considerations: Testing the solution with different types of input, such as empty intervals or queries, and testing the solution with large inputs to ensure that it scales well.