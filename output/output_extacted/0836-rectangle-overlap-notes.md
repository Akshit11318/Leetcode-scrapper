## Rectangle Overlap

**Problem Link:** https://leetcode.com/problems/rectangle-overlap/description

**Problem Statement:**
- Input format and constraints: The problem takes as input two rectangles defined by their coordinates (x, y, w, h), where (x, y) is the bottom-left corner and (w, h) is the width and height of the rectangle. The goal is to determine if the two rectangles overlap.
- Expected output format: The problem requires a boolean output indicating whether the rectangles overlap.
- Key requirements and edge cases to consider: The rectangles are defined by their coordinates and dimensions. The problem can be solved by checking the overlap of the rectangles' projections on the x and y axes.
- Example test cases with explanations:
  - Input: `rect1 = [0,0,2,2], rect2 = [1,1,3,3]`, Output: `true`
  - Input: `rect1 = [0,0,1,1], rect2 = [1,0,-1,1]`, Output: `false`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To check if two rectangles overlap, we can compare the coordinates of the rectangles' corners.
- Step-by-step breakdown of the solution:
  1. Calculate the x and y coordinates of the rectangles' corners.
  2. Check if any of the corners of one rectangle lie within the other rectangle.
- Why this approach comes to mind first: This approach is straightforward and involves checking all possible corners of the rectangles.

```cpp
bool isRectangleOverlap(vector<int>& rect1, vector<int>& rect2) {
    int x1 = rect1[0], y1 = rect1[1], x2 = rect1[0] + rect1[2], y2 = rect1[1] + rect1[3];
    int x3 = rect2[0], y3 = rect2[1], x4 = rect2[0] + rect2[2], y4 = rect2[1] + rect2[3];

    // Check if any corner of rect1 lies within rect2
    if (x1 >= x3 && x1 <= x4 && y1 >= y3 && y1 <= y4) return true;
    if (x1 >= x3 && x1 <= x4 && y2 >= y3 && y2 <= y4) return true;
    if (x2 >= x3 && x2 <= x4 && y1 >= y3 && y1 <= y4) return true;
    if (x2 >= x3 && x2 <= x4 && y2 >= y3 && y2 <= y4) return true;

    // Check if any corner of rect2 lies within rect1
    if (x3 >= x1 && x3 <= x2 && y3 >= y1 && y3 <= y2) return true;
    if (x3 >= x1 && x3 <= x2 && y4 >= y1 && y4 <= y2) return true;
    if (x4 >= x1 && x4 <= x2 && y3 >= y1 && y3 <= y2) return true;
    if (x4 >= x1 && x4 <= x2 && y4 >= y1 && y4 <= y2) return true;

    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, since we are performing a constant number of operations.
> - **Space Complexity:** $O(1)$, since we are using a constant amount of space.
> - **Why these complexities occur:** The time and space complexities are constant because we are only performing a fixed number of comparisons and using a fixed amount of space to store the coordinates.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Two rectangles overlap if and only if the x-coordinate of the right edge of one rectangle is greater than the x-coordinate of the left edge of the other rectangle, and the y-coordinate of the top edge of one rectangle is greater than the y-coordinate of the bottom edge of the other rectangle.
- Detailed breakdown of the approach:
  1. Calculate the x and y coordinates of the rectangles' edges.
  2. Check if the x and y coordinates satisfy the overlap conditions.
- Proof of optimality: This approach is optimal because it only requires a constant number of comparisons and uses a constant amount of space.
- Why further optimization is impossible: The time and space complexities are already constant, so further optimization is not possible.

```cpp
bool isRectangleOverlap(vector<int>& rect1, vector<int>& rect2) {
    int x1 = rect1[0], y1 = rect1[1], x2 = rect1[0] + rect1[2], y2 = rect1[1] + rect1[3];
    int x3 = rect2[0], y3 = rect2[1], x4 = rect2[0] + rect2[2], y4 = rect2[1] + rect2[3];

    return (x1 < x4 && x3 < x2 && y1 < y4 && y3 < y2);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, since we are performing a constant number of operations.
> - **Space Complexity:** $O(1)$, since we are using a constant amount of space.
> - **Optimality proof:** The time and space complexities are constant because we are only performing a fixed number of comparisons and using a fixed amount of space to store the coordinates.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of geometric reasoning and coordinate comparisons to solve a geometric problem.
- Problem-solving patterns identified: The problem illustrates the importance of identifying key insights and using them to simplify the solution.
- Optimization techniques learned: The problem shows how to optimize a solution by reducing the number of comparisons and using a constant amount of space.
- Similar problems to practice: Other geometric problems, such as checking if a point lies within a polygon or finding the intersection of two lines.

**Mistakes to Avoid:**
- Common implementation errors: Failing to check for edge cases, such as rectangles with zero area or negative coordinates.
- Edge cases to watch for: Rectangles with zero area or negative coordinates, as well as rectangles that overlap at a single point.
- Performance pitfalls: Using an excessive number of comparisons or using too much space.
- Testing considerations: Testing the solution with a variety of input cases, including edge cases and boundary cases.