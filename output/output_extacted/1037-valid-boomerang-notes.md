## Valid Boomerang
**Problem Link:** [https://leetcode.com/problems/valid-boomerang/description](https://leetcode.com/problems/valid-boomerang/description)

**Problem Statement:**
- Input format: Three points in a 2D plane, each represented as an array of two integers, `[x, y]`.
- Constraints: The input points are guaranteed to be distinct.
- Expected output format: A boolean indicating whether the three points form a valid boomerang.
- Key requirements: A valid boomerang is formed if the points are not collinear (i.e., they do not lie on the same line).
- Example test cases:
  - Input: `[[1,1],[2,3],[3,2]]`
    - Output: `true`
    - Explanation: The points do not lie on the same line.
  - Input: `[[1,1],[2,2],[3,3]]`
    - Output: `false`
    - Explanation: The points lie on the same line.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To determine if three points are collinear, we can calculate the slopes of the lines formed by each pair of points. If the slopes are equal, then the points are collinear.
- Step-by-step breakdown:
  1. Calculate the slopes of the lines formed by each pair of points.
  2. Compare the slopes to determine if the points are collinear.

```cpp
bool isBoomerang(vector<vector<int>>& points) {
    // Calculate the slopes
    int x1 = points[0][0], y1 = points[0][1];
    int x2 = points[1][0], y2 = points[1][1];
    int x3 = points[2][0], y3 = points[2][1];

    // Check for division by zero
    if (x2 - x1 == 0 && x3 - x1 == 0) {
        return false;  // Points are collinear (vertical line)
    }

    // Calculate the slopes
    double slope12 = (y2 - y1) / (double)(x2 - x1);
    double slope13 = (y3 - y1) / (double)(x3 - x1);

    // Compare the slopes
    return slope12 != slope13;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, since we are performing a constant number of operations.
> - **Space Complexity:** $O(1)$, since we are using a constant amount of space.
> - **Why these complexities occur:** The time complexity is constant because we are performing a fixed number of calculations, and the space complexity is constant because we are using a fixed amount of space to store the points and slopes.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of calculating the slopes, we can use the cross product of the vectors formed by the points to determine if they are collinear.
- Detailed breakdown:
  1. Calculate the vectors formed by the points.
  2. Calculate the cross product of the vectors.
  3. If the cross product is non-zero, the points are not collinear.

```cpp
bool isBoomerang(vector<vector<int>>& points) {
    int x1 = points[0][0], y1 = points[0][1];
    int x2 = points[1][0], y2 = points[1][1];
    int x3 = points[2][0], y3 = points[2][1];

    // Calculate the cross product
    int crossProduct = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1);

    // Check if the cross product is non-zero
    return crossProduct != 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, since we are performing a constant number of operations.
> - **Space Complexity:** $O(1)$, since we are using a constant amount of space.
> - **Optimality proof:** This approach is optimal because we are performing the minimum number of calculations required to determine if the points are collinear.

---

### Final Notes

**Learning Points:**
- Key algorithmic concept: Using the cross product to determine if points are collinear.
- Problem-solving pattern: Using vector operations to simplify calculations.
- Optimization technique: Avoiding division by zero by using the cross product instead of slopes.

**Mistakes to Avoid:**
- Common implementation error: Forgetting to check for division by zero when calculating slopes.
- Edge case to watch for: Points that lie on the same vertical line.
- Performance pitfall: Using a more complex algorithm than necessary.
- Testing consideration: Testing with points that are collinear, as well as points that are not collinear.