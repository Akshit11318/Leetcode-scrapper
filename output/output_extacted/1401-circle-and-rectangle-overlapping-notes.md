## Circle and Rectangle Overlapping

**Problem Link:** https://leetcode.com/problems/circle-and-rectangle-overlapping/description

**Problem Statement:**
- Input format: The function takes in two parameters: `circle` which is an array of three integers representing the center and radius of a circle `[x, y, r]`, and `rectangle` which is an array of four integers representing the top-left and bottom-right corners of a rectangle `[x1, y1, x2, y2]`.
- Constraints: The circle and rectangle are non-empty.
- Expected output format: The function should return `true` if the circle and rectangle overlap, and `false` otherwise.
- Key requirements and edge cases to consider: The circle and rectangle can overlap in various ways, including the circle being entirely inside the rectangle, the rectangle being entirely inside the circle, or the circle and rectangle intersecting at one or more points.

**Example Test Cases:**
- `circle = [0,0,1]`, `rectangle = [1,0,-1,0]`: Returns `true` because the circle and rectangle overlap.
- `circle = [0,0,1]`, `rectangle = [1,1,2,2]`: Returns `false` because the circle and rectangle do not overlap.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We need to check if the circle and rectangle overlap. We can do this by checking if the distance from the center of the circle to any point on the rectangle is less than or equal to the radius of the circle.
- Step-by-step breakdown of the solution:
  1. Calculate the distance from the center of the circle to each corner of the rectangle.
  2. Check if the distance is less than or equal to the radius of the circle.
  3. If the distance is less than or equal to the radius, return `true` because the circle and rectangle overlap.
- Why this approach comes to mind first: This approach is straightforward and easy to understand. It involves calculating distances and checking if they are within a certain range.

```cpp
bool checkOverlap(vector<int>& circle, vector<int>& rectangle) {
    int cx = circle[0], cy = circle[1], r = circle[2];
    int x1 = rectangle[0], y1 = rectangle[1], x2 = rectangle[2], y2 = rectangle[3];
    
    // Calculate distance from center of circle to each corner of rectangle
    double d1 = sqrt(pow(cx - x1, 2) + pow(cy - y1, 2));
    double d2 = sqrt(pow(cx - x2, 2) + pow(cy - y1, 2));
    double d3 = sqrt(pow(cx - x1, 2) + pow(cy - y2, 2));
    double d4 = sqrt(pow(cx - x2, 2) + pow(cy - y2, 2));
    
    // Check if distance is less than or equal to radius
    if (d1 <= r || d2 <= r || d3 <= r || d4 <= r) {
        return true;
    }
    
    // If none of the corners are within the circle, check if the circle is within the rectangle
    if (cx - r >= x1 && cx + r <= x2 && cy - r >= y1 && cy + r <= y2) {
        return true;
    }
    
    // If none of the above conditions are met, the circle and rectangle do not overlap
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because we are performing a constant number of operations.
> - **Space Complexity:** $O(1)$ because we are using a constant amount of space to store the distances and other variables.
> - **Why these complexities occur:** These complexities occur because we are not using any data structures that scale with the input size, and we are not performing any loops that depend on the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking the distance from the center of the circle to each corner of the rectangle, we can check if the center of the circle is within the rectangle, or if the rectangle is within the circle.
- Detailed breakdown of the approach:
  1. Check if the center of the circle is within the rectangle.
  2. Check if the rectangle is within the circle.
  3. If neither of the above conditions are met, check if the circle intersects with the rectangle.
- Proof of optimality: This approach is optimal because it reduces the number of calculations required to check for overlap.
- Why further optimization is impossible: This approach is already optimal because it only requires a constant number of calculations.

```cpp
bool checkOverlap(vector<int>& circle, vector<int>& rectangle) {
    int cx = circle[0], cy = circle[1], r = circle[2];
    int x1 = rectangle[0], y1 = rectangle[1], x2 = rectangle[2], y2 = rectangle[3];
    
    // Check if center of circle is within rectangle
    if (cx - r >= x1 && cx + r <= x2 && cy - r >= y1 && cy + r <= y2) {
        return true;
    }
    
    // Check if rectangle is within circle
    if (x1 >= cx - r && x2 <= cx + r && y1 >= cy - r && y2 <= cy + r) {
        return true;
    }
    
    // Check if circle intersects with rectangle
    if (cx - r <= x2 && cx + r >= x1 && cy - r <= y2 && cy + r >= y1) {
        return true;
    }
    
    // If none of the above conditions are met, the circle and rectangle do not overlap
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because we are performing a constant number of operations.
> - **Space Complexity:** $O(1)$ because we are using a constant amount of space to store the variables.
> - **Optimality proof:** This approach is optimal because it reduces the number of calculations required to check for overlap.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Checking for overlap between geometric shapes.
- Problem-solving patterns identified: Reducing the number of calculations required to solve a problem.
- Optimization techniques learned: Simplifying the problem by reducing the number of calculations required.
- Similar problems to practice: Checking for overlap between other geometric shapes, such as triangles or polygons.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for all possible cases of overlap.
- Edge cases to watch for: When the circle or rectangle is degenerate (i.e., has zero area).
- Performance pitfalls: Using an excessive number of calculations to check for overlap.
- Testing considerations: Testing the function with a variety of inputs, including edge cases.