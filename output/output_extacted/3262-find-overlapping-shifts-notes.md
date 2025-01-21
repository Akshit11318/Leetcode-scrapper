## Find Overlapping Shifts

**Problem Link:** https://leetcode.com/problems/find-overlapping-shifts/description

**Problem Statement:**
- Input format and constraints: Given a list of shifts where each shift is a tuple of `(start_time, end_time)`, find all overlapping shifts.
- Expected output format: Return a list of overlapping shift pairs.
- Key requirements and edge cases to consider: Shifts can be of any duration and can overlap at any point.
- Example test cases with explanations:
  - Example 1: `[(0, 1), (1, 2), (2, 3)]` returns an empty list because there are no overlapping shifts.
  - Example 2: `[(0, 2), (1, 3), (2, 4)]` returns `[(0, 2), (1, 3)]` and `[(1, 3), (2, 4)]` because these shifts overlap.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find overlapping shifts, we need to compare each shift with every other shift.
- Step-by-step breakdown of the solution:
  1. Iterate over each shift in the list.
  2. For each shift, compare it with every other shift in the list.
  3. Check if the current shift overlaps with the compared shift by checking if the start time of one shift is less than the end time of the other shift.
  4. If the shifts overlap, add the pair to the result list.
- Why this approach comes to mind first: It's straightforward and ensures we check every possible pair of shifts.

```cpp
vector<vector<int>> findOverlappingShifts(vector<vector<int>>& shifts) {
    vector<vector<int>> overlappingShifts;
    for (int i = 0; i < shifts.size(); i++) {
        for (int j = i + 1; j < shifts.size(); j++) {
            if (shifts[i][0] < shifts[j][1] && shifts[j][0] < shifts[i][1]) {
                overlappingShifts.push_back({shifts[i][0], shifts[i][1]});
                overlappingShifts.push_back({shifts[j][0], shifts[j][1]});
            }
        }
    }
    return overlappingShifts;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the number of shifts. This is because we have two nested loops that iterate over the shifts.
> - **Space Complexity:** $O(n)$ for storing the overlapping shifts.
> - **Why these complexities occur:** The time complexity is quadratic due to the nested loops, and the space complexity is linear because in the worst case, we might store every shift as an overlapping pair.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can sort the shifts by their start times and then iterate over them to find overlaps. This is because if a shift starts after another shift ends, they cannot overlap.
- Detailed breakdown of the approach:
  1. Sort the shifts based on their start times.
  2. Initialize the result list.
  3. Iterate over the sorted shifts. For each shift, compare it with the next shifts to find overlaps.
- Proof of optimality: This approach is optimal because it reduces the number of comparisons needed by leveraging the sorted order of the shifts.
- Why further optimization is impossible: This approach has a linear time complexity for the sorting step and a linear time complexity for the iteration step, making it optimal for this problem.

```cpp
vector<vector<int>> findOverlappingShifts(vector<vector<int>>& shifts) {
    sort(shifts.begin(), shifts.end());
    vector<vector<int>> overlappingShifts;
    for (int i = 0; i < shifts.size() - 1; i++) {
        if (shifts[i][1] > shifts[i + 1][0]) {
            overlappingShifts.push_back(shifts[i]);
            overlappingShifts.push_back(shifts[i + 1]);
        }
    }
    return overlappingShifts;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting step, where $n$ is the number of shifts.
> - **Space Complexity:** $O(n)$ for storing the overlapping shifts.
> - **Optimality proof:** The sorting step is necessary to efficiently find overlapping shifts, and the subsequent iteration is linear, making this approach optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting and iteration to find overlapping intervals.
- Problem-solving patterns identified: Using sorting to reduce the complexity of comparisons.
- Optimization techniques learned: Leveraging the properties of sorted data to reduce the number of comparisons.
- Similar problems to practice: Finding overlapping intervals in other contexts, such as scheduling meetings or allocating resources.

**Mistakes to Avoid:**
- Common implementation errors: Not properly handling edge cases, such as shifts with the same start or end times.
- Edge cases to watch for: Shifts that overlap at their boundaries (e.g., one shift ends at the same time another starts).
- Performance pitfalls: Using a brute force approach for large inputs, leading to inefficient time complexity.
- Testing considerations: Thoroughly testing the solution with various inputs, including edge cases and large datasets.