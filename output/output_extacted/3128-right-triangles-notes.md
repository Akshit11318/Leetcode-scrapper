## Right Triangles
**Problem Link:** https://leetcode.com/problems/right-triangles/description

**Problem Statement:**
- Input format: You are given a list of `points` where each point is an array of two integers representing the coordinates of a point in the plane.
- Constraints: $1 \leq points.length \leq 15$ and $0 \leq points[i][0], points[i][1] \leq 100$.
- Expected output format: Return the number of right triangles with non-zero area that can be formed using the given points.
- Key requirements and edge cases to consider: A right triangle is formed when the slopes of two lines formed by connecting the points are negative reciprocals of each other, or when one of the lines is vertical and the other is horizontal.
- Example test cases with explanations: For example, given points [[1,1],[2,2],[3,3],[4,4]], we can form a right triangle with points [1,1], [2,2], and [3,3].

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We need to consider all possible combinations of three points to form a triangle.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of three points.
  2. For each combination, calculate the slopes of the lines formed by connecting the points.
  3. Check if the slopes are negative reciprocals of each other or if one of the lines is vertical and the other is horizontal.
  4. If the conditions are met, increment the count of right triangles.
- Why this approach comes to mind first: It's a straightforward approach that considers all possible combinations of points.

```cpp
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int countRightTriangles(vector<vector<int>>& points) {
    int count = 0;
    for (int i = 0; i < points.size(); i++) {
        for (int j = i + 1; j < points.size(); j++) {
            for (int k = j + 1; k < points.size(); k++) {
                int x1 = points[i][0], y1 = points[i][1];
                int x2 = points[j][0], y2 = points[j][1];
                int x3 = points[k][0], y3 = points[k][1];
                
                // Check if the points are collinear
                if ((y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1)) continue;
                
                // Calculate the slopes
                double slope12 = (x2 == x1) ? INFINITY : (double)(y2 - y1) / (x2 - x1);
                double slope23 = (x3 == x2) ? INFINITY : (double)(y3 - y2) / (x3 - x2);
                double slope13 = (x3 == x1) ? INFINITY : (double)(y3 - y1) / (x3 - x1);
                
                // Check if the slopes are negative reciprocals of each other
                if (slope12 * slope23 == -1 || slope12 * slope13 == -1 || slope23 * slope13 == -1) {
                    count++;
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ where $n$ is the number of points. This is because we are considering all possible combinations of three points.
> - **Space Complexity:** $O(1)$ as we are not using any additional space that scales with the input size.
> - **Why these complexities occur:** The brute force approach has a high time complexity because it considers all possible combinations of points, resulting in a cubic time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use the same approach as the brute force solution but with a more efficient way of calculating the slopes and checking for right triangles.
- Detailed breakdown of the approach:
  1. Generate all possible combinations of three points.
  2. For each combination, calculate the slopes of the lines formed by connecting the points.
  3. Check if the slopes are negative reciprocals of each other or if one of the lines is vertical and the other is horizontal.
  4. If the conditions are met, increment the count of right triangles.
- Proof of optimality: This approach is optimal because it considers all possible combinations of points and checks for right triangles in a efficient way.

```cpp
int countRightTriangles(vector<vector<int>>& points) {
    int count = 0;
    for (int i = 0; i < points.size(); i++) {
        for (int j = i + 1; j < points.size(); j++) {
            for (int k = j + 1; k < points.size(); k++) {
                int x1 = points[i][0], y1 = points[i][1];
                int x2 = points[j][0], y2 = points[j][1];
                int x3 = points[k][0], y3 = points[k][1];
                
                // Check if the points are collinear
                if ((y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1)) continue;
                
                // Calculate the slopes
                double slope12 = (x2 == x1) ? INFINITY : (double)(y2 - y1) / (x2 - x1);
                double slope23 = (x3 == x2) ? INFINITY : (double)(y3 - y2) / (x3 - x2);
                double slope13 = (x3 == x1) ? INFINITY : (double)(y3 - y1) / (x3 - x1);
                
                // Check if the slopes are negative reciprocals of each other
                if (slope12 * slope23 == -1 || slope12 * slope13 == -1 || slope23 * slope13 == -1) {
                    count++;
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ where $n$ is the number of points. This is because we are considering all possible combinations of three points.
> - **Space Complexity:** $O(1)$ as we are not using any additional space that scales with the input size.
> - **Optimality proof:** This approach is optimal because it considers all possible combinations of points and checks for right triangles in a efficient way.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of combinatorics and geometry to solve a problem.
- Problem-solving patterns identified: The problem requires the use of a brute force approach to consider all possible combinations of points.
- Optimization techniques learned: The problem does not require any optimization techniques beyond the brute force approach.
- Similar problems to practice: Other problems that involve combinatorics and geometry, such as finding the number of triangles in a graph.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for collinear points before calculating the slopes.
- Edge cases to watch for: Points with the same coordinates.
- Performance pitfalls: Using a naive approach to calculate the slopes, resulting in a high time complexity.
- Testing considerations: Testing the solution with different inputs, including edge cases and large inputs.