## Find Overlapping Shifts II

**Problem Link:** https://leetcode.com/problems/find-overlapping-shifts-ii/description

**Problem Statement:**
- Input: An array of intervals representing shifts, where each interval is of the form `[start, end]`.
- Constraints: Each interval is guaranteed to be non-empty, and the start time is always less than or equal to the end time.
- Expected Output: The number of overlapping shifts.
- Key Requirements: A shift is considered overlapping if it shares any part of its duration with another shift.
- Edge Cases: Empty input, single shift, shifts with no overlap, shifts with complete overlap.

Example Test Cases:
- `[[1, 3], [3, 5], [4, 7], [6, 8], [8, 10]]` returns `4`.
- `[[1, 2], [2, 3], [3, 4]]` returns `2`.
- `[[1, 5], [5, 10]]` returns `1`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking each shift against every other shift to determine overlap.
- This approach is intuitive but inefficient due to its quadratic nature.
- We iterate through each pair of shifts and check if they overlap.

```cpp
int findOverlappingShifts(vector<vector<int>>& shifts) {
    int count = 0;
    for (int i = 0; i < shifts.size(); ++i) {
        for (int j = i + 1; j < shifts.size(); ++j) {
            if (shifts[i][0] < shifts[j][1] && shifts[j][0] < shifts[i][1]) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of shifts. This is because we're comparing each shift to every other shift.
> - **Space Complexity:** $O(1)$, not counting the input, because we're using a constant amount of space to store our count.
> - **Why these complexities occur:** The quadratic time complexity comes from the nested loop structure, and the constant space complexity is due to only using a fixed amount of space regardless of input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a sorting-based approach. By sorting the shifts based on their start times, we can then iterate through them to find overlaps.
- We use a `set` to keep track of end times of shifts we've seen so far. For each new shift, we check how many end times it overlaps with by finding the number of end times greater than its start time. We then add its end time to the set.
- This approach significantly reduces the time complexity compared to the brute force method.

```cpp
int findOverlappingShifts(vector<vector<int>>& shifts) {
    if (shifts.empty()) return 0;
    
    sort(shifts.begin(), shifts.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] < b[0];
    });
    
    set<int> endTimes;
    int overlaps = 0;
    
    for (const auto& shift : shifts) {
        overlaps += endTimes.size() - endTimes.lower_bound(shift[0]);
        endTimes.insert(shift[1]);
    }
    
    return overlaps;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, primarily due to the sorting operation and the use of `set` operations which have a logarithmic time complexity.
> - **Space Complexity:** $O(n)$, for storing the end times in the `set`.
> - **Optimality proof:** This approach is optimal because it minimizes the number of comparisons needed to find overlapping shifts, leveraging the efficiency of sorting and set operations.

---

### Final Notes

**Learning Points:**
- The importance of sorting in reducing complexity.
- Using data structures like `set` for efficient lookup and insertion.
- Understanding how to analyze time and space complexity.

**Mistakes to Avoid:**
- Not considering the efficiency of algorithms, leading to quadratic solutions when better ones exist.
- Not validating input or handling edge cases properly.
- Overlooking the use of standard library functions and data structures that can simplify code and improve performance.