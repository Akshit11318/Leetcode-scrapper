## Erect the Fence

**Problem Link:** https://leetcode.com/problems/erect-the-fence/description

**Problem Statement:**
- Input format and constraints: Given an array of `points` where `points[i] = [x, y]`, representing a point on the 2D plane, and an integer `n`, the number of points, find the smallest convex hull that encloses all the points.
- Expected output format: Return the points that make up the convex hull in either clockwise or counterclockwise order.
- Key requirements and edge cases to consider: 
  - If the points are not collinear, the convex hull will be a polygon.
  - If all points are collinear, the convex hull will be the line segment connecting the two furthest points.
- Example test cases with explanations: 
  - For points `[[0,0],[2,2],[2,0],[2,2],[0,2],[0,0],[0,0]]`, the convex hull is `[[0,0],[0,2],[2,2],[2,0]]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves checking all possible subsets of points to find the smallest convex hull.
- Step-by-step breakdown of the solution: 
  1. Generate all possible subsets of points.
  2. For each subset, check if it forms a convex hull by verifying that all points are either on or inside the hull.
  3. If a subset forms a convex hull, calculate its perimeter.
  4. Keep track of the subset with the smallest perimeter that encloses all points.
- Why this approach comes to mind first: It is a straightforward, though inefficient, way to ensure that we find the smallest convex hull.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

// Function to calculate the orientation of three points
int orientation(const std::vector<int>& p, const std::vector<int>& q, const std::vector<int>& r) {
    int val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1]);
    if (val == 0) return 0; // Collinear
    return (val > 0) ? 1 : 2; // Clockwise or counterclockwise
}

// Function to calculate the convex hull using the brute force approach
std::vector<std::vector<int>> bruteForceConvexHull(std::vector<std::vector<int>>& points) {
    int n = points.size();
    std::vector<std::vector<int>> hull;
    for (int i = 0; i < (1 << n); ++i) {
        std::vector<std::vector<int>> subset;
        for (int j = 0; j < n; ++j) {
            if (i & (1 << j)) subset.push_back(points[j]);
        }
        if (subset.size() < 3) continue; // Convex hull must have at least 3 points
        bool isConvexHull = true;
        for (const auto& point : points) {
            bool inside = false;
            for (size_t k = 0; k < subset.size(); ++k) {
                int o = orientation(subset[k], subset[(k + 1) % subset.size()], point);
                if (o == 0) { // Point is on the line
                    inside = true;
                    break;
                } else if (o == 2) { // Point is inside
                    inside = true;
                    break;
                }
            }
            if (!inside) {
                isConvexHull = false;
                break;
            }
        }
        if (isConvexHull) {
            hull = subset;
            break;
        }
    }
    return hull;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \cdot m)$, where $n$ is the number of points and $m$ is the number of points in the subset. This is because we generate all possible subsets of points and check each point against the subset.
> - **Space Complexity:** $O(n)$, as we need to store the points and the subset.
> - **Why these complexities occur:** The exponential time complexity comes from generating all possible subsets, and the linear space complexity comes from storing the points and the subset.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use the Graham's scan algorithm to find the convex hull in $O(n \log n)$ time.
- Detailed breakdown of the approach:
  1. Find the point with the lowest y-coordinate (and lowest x-coordinate in case of a tie).
  2. Sort the points by the polar angle they and the lowest point make.
  3. Initialize an empty stack and push the first three points to it.
  4. For each remaining point, while the orientation of the top two points and the current point is not counterclockwise, remove the top point from the stack.
  5. Push the current point to the stack.
- Proof of optimality: The Graham's scan algorithm is known to be optimal for finding the convex hull in the plane.

```cpp
// Function to calculate the convex hull using the Graham's scan algorithm
std::vector<std::vector<int>> grahamScanConvexHull(std::vector<std::vector<int>>& points) {
    int n = points.size();
    if (n < 3) return points;

    // Find the point with the lowest y-coordinate (and lowest x-coordinate in case of a tie)
    int start = 0;
    for (int i = 1; i < n; ++i) {
        if (points[i][1] < points[start][1] || (points[i][1] == points[start][1] && points[i][0] < points[start][0])) {
            start = i;
        }
    }

    // Swap the start point with the first point
    std::swap(points[0], points[start]);

    // Sort the points by the polar angle they and the lowest point make
    std::sort(points.begin() + 1, points.end(), [&points](const std::vector<int>& a, const std::vector<int>& b) {
        int crossProduct = (a[0] - points[0][0]) * (b[1] - points[0][1]) - (a[1] - points[0][1]) * (b[0] - points[0][0]);
        if (crossProduct == 0) {
            int distanceA = (a[0] - points[0][0]) * (a[0] - points[0][0]) + (a[1] - points[0][1]) * (a[1] - points[0][1]);
            int distanceB = (b[0] - points[0][0]) * (b[0] - points[0][0]) + (b[1] - points[0][1]) * (b[1] - points[0][1]);
            return distanceA < distanceB;
        } else {
            return crossProduct > 0;
        }
    });

    // Initialize an empty stack and push the first three points to it
    std::vector<std::vector<int>> stack;
    stack.push_back(points[0]);
    stack.push_back(points[1]);
    stack.push_back(points[2]);

    // For each remaining point, while the orientation of the top two points and the current point is not counterclockwise, remove the top point from the stack
    for (int i = 3; i < n; ++i) {
        while (stack.size() > 1 && orientation(stack[stack.size() - 2], stack[stack.size() - 1], points[i]) != 2) {
            stack.pop_back();
        }
        stack.push_back(points[i]);
    }

    return stack;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of points. This is because we sort the points by the polar angle they and the lowest point make.
> - **Space Complexity:** $O(n)$, as we need to store the points and the stack.
> - **Optimality proof:** The Graham's scan algorithm is known to be optimal for finding the convex hull in the plane.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Convex hull, Graham's scan algorithm, polar angle sorting.
- Problem-solving patterns identified: Finding the smallest convex hull that encloses all points.
- Optimization techniques learned: Using the Graham's scan algorithm to reduce the time complexity from exponential to $O(n \log n)$.
- Similar problems to practice: Finding the convex hull of a set of points in 3D space, finding the smallest enclosing circle of a set of points.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where all points are collinear, not checking for the orientation of the points correctly.
- Edge cases to watch for: Points with the same x or y coordinates, points that are very close to each other.
- Performance pitfalls: Using an inefficient algorithm with high time complexity, not optimizing the code for large inputs.
- Testing considerations: Testing the code with different inputs, including edge cases and large inputs, to ensure that it works correctly and efficiently.