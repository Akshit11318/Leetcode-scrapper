## Find Right Interval

**Problem Link:** https://leetcode.com/problems/find-right-interval/description

**Problem Statement:**
- Given a set of intervals, for each interval `i`, find the interval `j` for which `intervals[j][0] >= intervals[i][1]` is true and `j` is minimum.
- Input format: An array of intervals where each interval is an array of two integers.
- Constraints: The input array will contain between 1 and 1000 intervals.
- Expected output format: An array of integers where the `i-th` integer corresponds to the index of the interval `j` that meets the condition for interval `i`, or -1 if no such interval exists.
- Key requirements and edge cases to consider:
  - Intervals are not necessarily sorted.
  - There can be duplicate intervals.
  - The end of one interval may match the start of another.
- Example test cases:
  - `[[3,4],[2,3],[1,2],[4,5]]` should return `[1,-1,0,-1]`.
  - `[[1,4],[2,3],[3,4]]` should return `[2,-1,1]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate over each interval and then compare its end with the start of every other interval to find the smallest one that is greater or equal.
- This approach is straightforward but inefficient due to its nested loop structure.

```cpp
vector<int> findRightInterval(vector<vector<int>>& intervals) {
    int n = intervals.size();
    vector<int> result(n, -1);
    for (int i = 0; i < n; i++) {
        int minIndex = -1;
        for (int j = 0; j < n; j++) {
            if (intervals[j][0] >= intervals[i][1]) {
                if (minIndex == -1 || j < minIndex) {
                    minIndex = j;
                }
            }
        }
        result[i] = minIndex;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of intervals. This is because for each interval, we are potentially checking all other intervals.
> - **Space Complexity:** $O(n)$, for storing the result array.
> - **Why these complexities occur:** The brute force approach involves a nested loop, leading to quadratic time complexity. The space complexity is linear because we need to store the result for each interval.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a hash map to store the start of each interval as the key and its index as the value. Then, sort the intervals by their start value.
- Iterate over the sorted intervals and for each one, find the smallest start value in the hash map that is greater or equal to its end.
- This approach reduces the time complexity significantly by avoiding the nested loop structure.

```cpp
vector<int> findRightInterval(vector<vector<int>>& intervals) {
    int n = intervals.size();
    vector<int> result(n, -1);
    unordered_map<int, int> startToIndex;
    for (int i = 0; i < n; i++) {
        startToIndex[intervals[i][0]] = i;
    }
    sort(intervals.begin(), intervals.end());
    for (int i = 0; i < n; i++) {
        auto it = startToIndex.lower_bound(intervals[i][1]);
        if (it != startToIndex.end()) {
            result[intervals[i][2]] = it->second;
        }
    }
    return result;
}
```

However, the above approach is incorrect because it does not properly utilize the `lower_bound` function with the `startToIndex` map and does not correctly update the result array based on the original indices of the intervals.

Let's correct the approach by using a different data structure that allows us to find the next interval with a start value greater or equal to the end of the current interval more efficiently. We can use a binary search approach but need to keep track of the original indices.

A correct optimal approach would involve using a sorted data structure to efficiently find the next interval that meets the condition for each given interval.

```cpp
vector<int> findRightInterval(vector<vector<int>>& intervals) {
    int n = intervals.size();
    vector<int> result(n, -1);
    vector<pair<int, int>> starts;
    for (int i = 0; i < n; i++) {
        starts.push_back({intervals[i][0], i});
    }
    sort(starts.begin(), starts.end());
    for (int i = 0; i < n; i++) {
        int end = intervals[i][1];
        auto it = lower_bound(starts.begin(), starts.end(), pair<int, int>{end, -1});
        if (it != starts.end()) {
            result[i] = it->second;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, due to the sorting of intervals and the use of `lower_bound` which performs a binary search.
> - **Space Complexity:** $O(n)$, for storing the `starts` array and the result.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity from $O(n^2)$ to $O(n \log n)$ by utilizing sorting and binary search, which are more efficient operations for finding the next interval that meets the condition.

---

### Final Notes

**Learning Points:**
- The importance of utilizing data structures like hash maps and sorted arrays to improve efficiency.
- The use of binary search (`lower_bound`) to find elements in a sorted array.
- How to approach problems that require finding the next or previous element that meets a certain condition in a set of intervals.

**Mistakes to Avoid:**
- Incorrectly implementing the optimal approach by not properly utilizing the `lower_bound` function or not correctly updating the result array based on the original indices of the intervals.
- Not considering the impact of sorting on the original indices of the intervals.
- Failing to validate the input and handle edge cases, such as empty intervals or intervals with duplicate start values.