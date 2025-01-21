## Count Lattice Points Inside a Circle
**Problem Link:** https://leetcode.com/problems/count-lattice-points-inside-a-circle/description

**Problem Statement:**
- Input format: `circles` - a list of arrays representing the circle equations in the form `[x, y, r]` where `(x, y)` is the center of the circle and `r` is the radius.
- Constraints: 
  - `1 <= circles.length <= 200`
  - `circles[i].length == 3`
  - `-100 <= circles[i][0], circles[i][1], circles[i][2] <= 100`
  - `1 <= circles[i][2] <= 100`
- Expected output format: The number of lattice points that are strictly inside at least one of the given circles.
- Key requirements and edge cases to consider: 
  - A lattice point `(x, y)` is inside a circle with equation `[cx, cy, r]` if `(x - cx)^2 + (y - cy)^2 < r^2`.
  - Points on the border of a circle are not considered inside the circle.
- Example test cases with explanations:
  - Example 1: Input: `circles = [[2,2,1]]`, Output: `5`. Explanation: There are five lattice points `(1, 1)`, `(1, 2)`, `(1, 3)`, `(2, 1)`, and `(2, 2)` that are inside the circle centered at `(2, 2)` with radius `1`.
  - Example 2: Input: `circles = [[2,2,2],[3,4,1]]`, Output: `16`. Explanation: There are sixteen lattice points that are inside at least one of the given circles.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The problem asks for lattice points strictly inside at least one circle. A brute force approach would involve checking every possible lattice point within the bounds defined by the circles.
- Step-by-step breakdown of the solution:
  1. Determine the bounds of the lattice points to check. This can be done by finding the minimum and maximum x and y coordinates of all circle centers and then extending these bounds by the maximum radius.
  2. Iterate over all lattice points within these bounds.
  3. For each lattice point, check if it is inside any of the given circles by using the circle equation.
  4. Count the number of lattice points that are inside at least one circle.
- Why this approach comes to mind first: It is a straightforward, intuitive method that directly addresses the problem statement without requiring complex optimizations.

```cpp
int countLatticePoints(vector<vector<int>>& circles) {
    int minX = INT_MAX, maxX = INT_MIN, minY = INT_MAX, maxY = INT_MIN;
    for (auto& circle : circles) {
        minX = min(minX, circle[0] - circle[2]);
        maxX = max(maxX, circle[0] + circle[2]);
        minY = min(minY, circle[1] - circle[2]);
        maxY = max(maxY, circle[1] + circle[2]);
    }

    int count = 0;
    for (int x = minX; x <= maxX; ++x) {
        for (int y = minY; y <= maxY; ++y) {
            for (auto& circle : circles) {
                if ((x - circle[0]) * (x - circle[0]) + (y - circle[1]) * (y - circle[1]) < circle[2] * circle[2]) {
                    count++;
                    break; // Break the loop if the point is inside any circle
                }
            }
        }
    }

    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$, where $n$ is the range of x coordinates, $m$ is the range of y coordinates, and $k$ is the number of circles. This is because for each lattice point, we potentially check against all circles.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input, as we only use a constant amount of space to store the count and the bounds.
> - **Why these complexities occur:** The brute force approach involves iterating over all possible lattice points within the bounds and checking each point against all circles, leading to a cubic time complexity in the worst case.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking every possible lattice point, we can iterate over all given circles and for each circle, we can calculate the lattice points that are strictly inside it. This approach avoids redundant checks and focuses on the areas where lattice points are guaranteed to be inside a circle.
- Detailed breakdown of the approach:
  1. Initialize a set to store unique lattice points that are inside at least one circle.
  2. Iterate over each circle.
  3. For each circle, iterate over the possible lattice points within its bounds (i.e., within `radius` distance from the center).
  4. Check if a lattice point is strictly inside the current circle. If it is, add it to the set.
  5. After checking all circles, the size of the set represents the number of unique lattice points inside at least one circle.
- Proof of optimality: This approach is optimal because it ensures that each lattice point is checked exactly once against the circles that could potentially contain it, minimizing unnecessary checks.

```cpp
int countLatticePoints(vector<vector<int>>& circles) {
    set<pair<int, int>> latticePoints;
    for (auto& circle : circles) {
        int x = circle[0], y = circle[1], r = circle[2];
        for (int dx = -r; dx <= r; ++dx) {
            for (int dy = -r; dy <= r; ++dy) {
                if (dx * dx + dy * dy < r * r) {
                    latticePoints.insert({x + dx, y + dy});
                }
            }
        }
    }

    return latticePoints.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k \cdot r^2)$, where $k$ is the number of circles and $r$ is the maximum radius. This is because for each circle, we potentially check all lattice points within its radius.
> - **Space Complexity:** $O(k \cdot r^2)$, for storing the lattice points in the set.
> - **Optimality proof:** This approach is optimal because it directly calculates the lattice points inside each circle without redundant checks, achieving the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, set usage for uniqueness, and optimization by focusing on relevant areas (in this case, the areas around each circle).
- Problem-solving patterns identified: Breaking down the problem into smaller, manageable parts (each circle), and using data structures (sets) to efficiently store and count unique elements.
- Optimization techniques learned: Avoiding redundant checks by focusing on the most relevant data (lattice points near each circle) and using efficient data structures.

**Mistakes to Avoid:**
- Common implementation errors: Failing to break the loop once a lattice point is found to be inside any circle (in the brute force approach), or incorrectly calculating the bounds for checking lattice points.
- Edge cases to watch for: Circles with radius 0, or circles that do not overlap with any lattice points.
- Performance pitfalls: Using inefficient algorithms or data structures that lead to high time or space complexity.
- Testing considerations: Ensure to test with various inputs, including edge cases like circles with small radii, large radii, and non-overlapping circles.