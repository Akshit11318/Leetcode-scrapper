## Interval List Intersections

**Problem Link:** https://leetcode.com/problems/interval-list-intersections/description

**Problem Statement:**
- Input format: Two lists of intervals, `A` and `B`, where each interval is a list of two integers, `[start, end]`.
- Constraints: Each interval in `A` and `B` is non-empty and `start <= end`. The intervals in `A` are sorted by their start time, and the intervals in `B` are sorted by their start time.
- Expected output format: A list of intervals that represent the intersection of the intervals in `A` and `B`.
- Key requirements: The output intervals should not overlap and should be sorted by their start time.
- Edge cases to consider: Empty input lists, intervals with no intersection, and intervals that are completely contained within another interval.

Example test cases:
- `A = [[0,2],[5,10],[13,23],[24,25]]`, `B = [[1,5],[8,12],[15,24],[25,26]]`
- `A = [[1,3],[5,7],[9,12]]`, `B = [[5,10]]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each interval in `A` and `B`, and check if they intersect. If they do, add the intersection to the result list.
- Step-by-step breakdown of the solution:
  1. Iterate over each interval in `A`.
  2. For each interval in `A`, iterate over each interval in `B`.
  3. Check if the current intervals in `A` and `B` intersect. If they do, calculate the intersection and add it to the result list.
  4. Sort the result list by the start time of each interval.

```cpp
vector<vector<int>> intervalIntersection(vector<vector<int>>& A, vector<vector<int>>& B) {
    vector<vector<int>> result;
    for (auto& a : A) {
        for (auto& b : B) {
            int start = max(a[0], b[0]);
            int end = min(a[1], b[1]);
            if (start <= end) {
                result.push_back({start, end});
            }
        }
    }
    sort(result.begin(), result.end());
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot \log(n \cdot m))$, where $n$ is the number of intervals in `A` and $m$ is the number of intervals in `B`. This is because we are iterating over each interval in `A` and `B`, and then sorting the result list.
> - **Space Complexity:** $O(n \cdot m)$, as we are storing the intersection of each pair of intervals in the result list.
> - **Why these complexities occur:** The time complexity occurs because we are using a nested loop to iterate over each pair of intervals, and then sorting the result list. The space complexity occurs because we are storing the intersection of each pair of intervals in the result list.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Since the intervals in `A` and `B` are sorted by their start time, we can use a two-pointer technique to find the intersection of the intervals in `A` and `B`.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `i` and `j`, to the first interval in `A` and `B`, respectively.
  2. Iterate until one of the pointers reaches the end of its respective list.
  3. For each iteration, calculate the intersection of the current intervals in `A` and `B`. If they intersect, add the intersection to the result list.
  4. Move the pointer of the interval with the earlier end time to the next interval.

```cpp
vector<vector<int>> intervalIntersection(vector<vector<int>>& A, vector<vector<int>>& B) {
    vector<vector<int>> result;
    int i = 0, j = 0;
    while (i < A.size() && j < B.size()) {
        int start = max(A[i][0], B[j][0]);
        int end = min(A[i][1], B[j][1]);
        if (start <= end) {
            result.push_back({start, end});
        }
        if (A[i][1] < B[j][1]) {
            i++;
        } else {
            j++;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of intervals in `A` and $m$ is the number of intervals in `B`. This is because we are using a two-pointer technique to iterate over the intervals in `A` and `B`.
> - **Space Complexity:** $O(n + m)$, as we are storing the intersection of the intervals in the result list.
> - **Optimality proof:** This is the optimal solution because we are using a two-pointer technique to iterate over the intervals in `A` and `B`, which has a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two-pointer technique, interval intersection.
- Problem-solving patterns identified: Using a two-pointer technique to iterate over two sorted lists.
- Optimization techniques learned: Using a two-pointer technique to reduce the time complexity from $O(n \cdot m)$ to $O(n + m)$.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for the intersection of the intervals correctly.
- Edge cases to watch for: Empty input lists, intervals with no intersection, and intervals that are completely contained within another interval.
- Performance pitfalls: Using a nested loop to iterate over the intervals in `A` and `B`, which has a high time complexity.
- Testing considerations: Testing the function with different input cases, including empty lists, lists with no intersection, and lists with intervals that are completely contained within another interval.