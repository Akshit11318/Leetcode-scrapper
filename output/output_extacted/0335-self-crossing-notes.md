## Self-Crossing
**Problem Link:** https://leetcode.com/problems/self-crossing/description

**Problem Statement:**
- Input format: An array of integers `x` representing the lengths of line segments.
- Constraints: $1 \leq x.length \leq 1000$ and $1 \leq x[i] \leq 1000$.
- Expected output format: A boolean indicating whether the line segments cross themselves.
- Key requirements and edge cases to consider: The line segments are connected head to tail, and we need to determine if they intersect at any point.
- Example test cases with explanations: 
  - `[2,1,1,2]` returns `true` because the line segments intersect.
  - `[1,2,3,4]` returns `false` because the line segments do not intersect.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can simulate the drawing of the line segments and check for intersections at each step.
- Step-by-step breakdown of the solution:
  1. Initialize a set to store the points that have been visited.
  2. Iterate through the line segments and draw each one.
  3. For each new point, check if it intersects with any previous points.
  4. If an intersection is found, return `true`.
- Why this approach comes to mind first: It is a straightforward and intuitive approach that simulates the problem.

```cpp
bool isSelfCrossing(vector<int>& x) {
    int n = x.size();
    vector<pair<int, int>> points;
    int x1 = 0, y1 = 0;
    for (int i = 0; i < n; i++) {
        int x2 = x1, y2 = y1;
        if (i % 4 == 0 || i % 4 == 2) {
            x2 += x[i];
        } else {
            y2 += x[i];
        }
        for (auto point : points) {
            if (doIntersect(point.first, point.second, x1, y1, x2, y2)) {
                return true;
            }
        }
        points.push_back({x1, y1});
        x1 = x2, y1 = y2;
    }
    return false;
}

bool doIntersect(pair<int, int> p1, pair<int, int> q1, pair<int, int> p2, pair<int, int> q2) {
    int o1 = orientation(p1, q1, p2);
    int o2 = orientation(p1, q1, q2);
    int o3 = orientation(p2, q2, p1);
    int o4 = orientation(p2, q2, q1);

    if (o1 != o2 && o3 != o4) return true;

    if (o1 == 0 && onSegment(p1, p2, q1)) return true;
    if (o2 == 0 && onSegment(p1, q2, q1)) return true;
    if (o3 == 0 && onSegment(p2, p1, q2)) return true;
    if (o4 == 0 && onSegment(p2, q1, q2)) return true;

    return false;
}

int orientation(pair<int, int> p, pair<int, int> q, pair<int, int> r) {
    int val = (q.second - p.second) * (r.first - q.first) - (q.first - p.first) * (r.second - q.second);
    if (val == 0) return 0;
    return (val > 0) ? 1 : 2;
}

bool onSegment(pair<int, int> p, pair<int, int> q, pair<int, int> r) {
    if (q.first <= max(p.first, r.first) && q.first >= min(p.first, r.first) &&
        q.second <= max(p.second, r.second) && q.second >= min(p.second, r.second))
        return true;
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of line segments. This is because we are checking for intersections between each new point and all previous points.
> - **Space Complexity:** $O(n)$, where $n$ is the number of line segments. This is because we are storing all previous points in a set.
> - **Why these complexities occur:** The brute force approach has a high time complexity because it checks for intersections between each new point and all previous points. The space complexity is also high because we are storing all previous points.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a mathematical approach to determine if the line segments intersect.
- Detailed breakdown of the approach:
  1. Initialize variables to keep track of the lengths of the line segments.
  2. Iterate through the line segments and check for intersections using the mathematical approach.
- Proof of optimality: This approach is optimal because it has a lower time complexity than the brute force approach and does not require storing all previous points.

```cpp
bool isSelfCrossing(vector<int>& x) {
    int n = x.size();
    for (int i = 3; i < n; i++) {
        if (x[i] >= x[i-2] && x[i-1] <= x[i-3]) return true;
        if (i >= 4 && x[i-1] == x[i-3] && x[i] + x[i-4] >= x[i-2]) return true;
    }
    for (int i = 5; i < n; i++) {
        if (x[i-2] >= x[i] && x[i-3] >= x[i-1] && x[i-4] + x[i] >= x[i-2] && x[i-1] <= x[i-3]) return true;
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of line segments. This is because we are iterating through the line segments once.
> - **Space Complexity:** $O(1)$, where $n$ is the number of line segments. This is because we are not storing any additional data structures.
> - **Optimality proof:** This approach is optimal because it has a lower time complexity than the brute force approach and does not require storing all previous points.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Mathematical approach to solving problems.
- Problem-solving patterns identified: Using mathematical insights to reduce the time complexity of a problem.
- Optimization techniques learned: Reducing the time complexity of a problem by using a mathematical approach.
- Similar problems to practice: Other problems that involve using mathematical insights to solve a problem.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, not using the correct mathematical formulas.
- Edge cases to watch for: Line segments with zero length, line segments with the same length.
- Performance pitfalls: Using a brute force approach instead of a mathematical approach.
- Testing considerations: Testing the function with different inputs to ensure it is working correctly.