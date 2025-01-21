## Minimum Number of Arrows to Burst Balloons
**Problem Link:** https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description

**Problem Statement:**
- Input format: An array of pairs `points` where each pair represents the start and end of a balloon.
- Constraints: $0 \leq points.length \leq 10^5$, $points[i].length == 2$, $-10^7 \leq points[i] \leq 10^7$.
- Expected output format: The minimum number of arrows required to burst all balloons.
- Key requirements and edge cases to consider: The balloons are burst when an arrow is shot at the point where the maximum number of balloons overlap.
- Example test cases with explanations:
  - Example 1:
    - Input: `points = [[10,16],[2,8],[1,6],[7,12]]`
    - Output: `2`
    - Explanation: One possible solution is to shoot one arrow for the balloons at positions `[2,8]` and another arrow for the balloons at positions `[1,6]` and `[7,12]`.
  - Example 2:
    - Input: `points = [[1,2],[3,4],[5,6],[7,8]]`
    - Output: `4`
    - Explanation: We need to shoot one arrow for each balloon.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The most straightforward approach is to try all possible positions for the arrows and check which positions result in the maximum number of burst balloons.
- Step-by-step breakdown of the solution:
  1. Sort the balloons by their end points.
  2. Iterate over each possible position for the arrow.
  3. For each position, count the number of balloons that can be burst.
  4. Keep track of the position that results in the maximum number of burst balloons.
- Why this approach comes to mind first: This approach is intuitive because it tries all possible solutions and selects the best one.

```cpp
int findMinArrowShots(vector<vector<int>>& points) {
    if (points.size() == 0) return 0;
    sort(points.begin(), points.end(), [](vector<int>& a, vector<int>& b) {
        return a[1] < b[1];
    });
    int res = 1;
    int pos = points[0][1];
    for (int i = 1; i < points.size(); i++) {
        if (points[i][0] > pos) {
            pos = points[i][1];
            res++;
        }
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting, where $n$ is the number of balloons.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space.
> - **Why these complexities occur:** The sorting step dominates the time complexity, while the space complexity is constant because we only use a few variables to store the result and the current position.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a greedy approach to find the minimum number of arrows required. The idea is to always shoot an arrow at the position where the maximum number of balloons overlap.
- Detailed breakdown of the approach:
  1. Sort the balloons by their end points.
  2. Initialize the result and the current position.
  3. Iterate over the sorted balloons. If a balloon's start point is greater than the current position, update the current position and increment the result.
- Proof of optimality: This approach is optimal because it always chooses the position that results in the maximum number of burst balloons.

```cpp
int findMinArrowShots(vector<vector<int>>& points) {
    if (points.size() == 0) return 0;
    sort(points.begin(), points.end(), [](vector<int>& a, vector<int>& b) {
        return a[1] < b[1];
    });
    int res = 1;
    int pos = points[0][1];
    for (int i = 1; i < points.size(); i++) {
        if (points[i][0] > pos) {
            pos = points[i][1];
            res++;
        }
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting, where $n$ is the number of balloons.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space.
> - **Optimality proof:** This approach is optimal because it always chooses the position that results in the maximum number of burst balloons.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy approach, sorting.
- Problem-solving patterns identified: Finding the minimum number of operations required to achieve a goal.
- Optimization techniques learned: Using a greedy approach to find the optimal solution.
- Similar problems to practice: Other problems that involve finding the minimum number of operations required, such as the `Minimum Number of Arrows to Burst Balloons II` problem.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty input array.
- Edge cases to watch for: Empty input array, balloons with the same end point.
- Performance pitfalls: Using a brute force approach, which can result in a time complexity of $O(n^2)$.
- Testing considerations: Test the function with different input arrays, including edge cases.