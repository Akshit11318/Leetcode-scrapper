## Rectangle Area

**Problem Link:** https://leetcode.com/problems/rectangle-area/description

**Problem Statement:**
- Input format: Two rectangles defined by their coordinates (x, y) of the bottom-left corner and (x, y) of the top-right corner.
- Constraints: $0 \leq x, y \leq 10^9$.
- Expected output format: The total area of the two rectangles.
- Key requirements and edge cases to consider: The rectangles may overlap, and we need to calculate the total area, subtracting the overlap.
- Example test cases with explanations:
  - Input: `rect1 = [-3,0,3,4]`, `rect2 = [0,-1,9,2]`. Output: `45`.
  - Input: `rect1 = [-2,0,2,2]`, `rect2 = [-2,-2,2,2]`. Output: `16`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can calculate the area of each rectangle and then subtract the overlap area.
- Step-by-step breakdown of the solution:
  1. Calculate the area of each rectangle using the formula `area = width * height`.
  2. Calculate the overlap area by finding the intersection of the two rectangles.
- Why this approach comes to mind first: It's a straightforward approach that involves calculating the areas and subtracting the overlap.

```cpp
int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
    // Calculate the area of each rectangle
    int area1 = (C - A) * (D - B);
    int area2 = (G - E) * (H - F);

    // Calculate the overlap area
    int overlapWidth = max(0, min(C, G) - max(A, E));
    int overlapHeight = max(0, min(D, H) - max(B, F));
    int overlapArea = overlapWidth * overlapHeight;

    // Return the total area
    return area1 + area2 - overlapArea;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, as we are performing a constant number of operations.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the variables.
> - **Why these complexities occur:** The operations are simple arithmetic calculations, and we are not using any data structures that scale with input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is the same as the brute force approach, as we are already performing the minimum number of operations required to calculate the area.
- Detailed breakdown of the approach:
  1. Calculate the area of each rectangle using the formula `area = width * height`.
  2. Calculate the overlap area by finding the intersection of the two rectangles.
- Proof of optimality: We are performing the minimum number of operations required to calculate the area, as we need to calculate the area of each rectangle and subtract the overlap area.
- Why further optimization is impossible: We are already performing the minimum number of operations required, and any further optimization would not reduce the number of operations.

```cpp
int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
    // Calculate the area of each rectangle
    int area1 = (C - A) * (D - B);
    int area2 = (G - E) * (H - F);

    // Calculate the overlap area
    int overlapWidth = max(0, min(C, G) - max(A, E));
    int overlapHeight = max(0, min(D, H) - max(B, F));
    int overlapArea = overlapWidth * overlapHeight;

    // Return the total area
    return area1 + area2 - overlapArea;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, as we are performing a constant number of operations.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the variables.
> - **Optimality proof:** We are performing the minimum number of operations required to calculate the area, and any further optimization would not reduce the number of operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Calculating the area of rectangles and subtracting the overlap area.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems and solving each one separately.
- Optimization techniques learned: Performing the minimum number of operations required to solve the problem.
- Similar problems to practice: Calculating the area of polygons, finding the intersection of two polygons.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for overlap, not calculating the area of each rectangle correctly.
- Edge cases to watch for: Rectangles with zero area, rectangles with negative coordinates.
- Performance pitfalls: Using unnecessary data structures or operations.
- Testing considerations: Testing with different input cases, including edge cases and corner cases.