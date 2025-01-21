## Convex Polygon
**Problem Link:** https://leetcode.com/problems/convex-polygon/description

**Problem Statement:**
- Input format and constraints: The input is an array of points in 2D space, where each point is an array of two integers representing the x and y coordinates.
- Expected output format: The function should return `true` if the given points form a convex polygon and `false` otherwise.
- Key requirements and edge cases to consider: 
  - The polygon should have at least 3 points.
  - The points should not be collinear.
- Example test cases with explanations:
  - `[[0,0],[0,1],[1,1],[1,0]]` returns `true` because these points form a square, which is a convex polygon.
  - `[[0,0],[0,10],[10,10],[10,0],[5,5]]` returns `false` because the point `(5,5)` is inside the square formed by the first four points, making the polygon non-convex.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To check if a polygon is convex, we can calculate the cross product of vectors formed by consecutive points. If all cross products have the same sign, the polygon is convex.
- Step-by-step breakdown of the solution:
  1. Calculate the cross product of vectors formed by consecutive points.
  2. Check if all cross products have the same sign.
- Why this approach comes to mind first: It is based on the definition of a convex polygon and is straightforward to implement.

```cpp
#include <vector>

bool isConvex(vector<vector<int>>& points) {
    int n = points.size();
    if (n < 3) return false;
    
    int sign = 0;
    for (int i = 0; i < n; i++) {
        int x1 = points[(i-1+n)%n][0] - points[i][0];
        int y1 = points[(i-1+n)%n][1] - points[i][1];
        int x2 = points[(i+1)%n][0] - points[i][0];
        int y2 = points[(i+1)%n][1] - points[i][1];
        
        int crossProduct = x1*y2 - x2*y1;
        if (sign == 0) {
            sign = crossProduct;
        } else if (sign * crossProduct < 0) {
            return false;
        }
    }
    
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of points, because we are iterating through each point once.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the sign and other variables.
> - **Why these complexities occur:** The time complexity is linear because we are checking each point once, and the space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same approach as the brute force solution is already optimal, because we must check each point at least once to determine if the polygon is convex.
- Detailed breakdown of the approach: The same as the brute force approach.
- Proof of optimality: This approach is optimal because it has a linear time complexity, and we must check each point at least once.
- Why further optimization is impossible: Further optimization is impossible because we must check each point at least once, and this approach already does that in linear time.

```cpp
#include <vector>

bool isConvex(vector<vector<int>>& points) {
    int n = points.size();
    if (n < 3) return false;
    
    int sign = 0;
    for (int i = 0; i < n; i++) {
        int x1 = points[(i-1+n)%n][0] - points[i][0];
        int y1 = points[(i-1+n)%n][1] - points[i][1];
        int x2 = points[(i+1)%n][0] - points[i][0];
        int y2 = points[(i+1)%n][1] - points[i][1];
        
        int crossProduct = x1*y2 - x2*y1;
        if (sign == 0) {
            sign = crossProduct;
        } else if (sign * crossProduct < 0) {
            return false;
        }
    }
    
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of points, because we are iterating through each point once.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the sign and other variables.
> - **Optimality proof:** This approach is optimal because it has a linear time complexity, and we must check each point at least once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Checking the cross product of vectors to determine if a polygon is convex.
- Problem-solving patterns identified: Using a linear scan to check each point in the polygon.
- Optimization techniques learned: None, because the brute force approach is already optimal.
- Similar problems to practice: Other problems involving geometric shapes, such as checking if a point is inside a polygon.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle the case where the polygon has less than 3 points.
- Edge cases to watch for: Points that are collinear, or points that are not in general position.
- Performance pitfalls: Using a data structure that has a high time complexity, such as a tree or a graph.
- Testing considerations: Testing the function with a variety of inputs, including convex and non-convex polygons, and polygons with different numbers of points.