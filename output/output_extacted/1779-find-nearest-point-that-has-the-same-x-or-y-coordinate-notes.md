## Find Nearest Point That Has the Same X or Y Coordinate

**Problem Link:** https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/description

**Problem Statement:**
- Input format and constraints: Given a point `(x, y)` and a list of points, find the point from the list that is nearest to `(x, y)`. The nearest point is defined as the point with the minimum Manhattan distance (sum of absolute differences in x and y coordinates) to the given point `(x, y)`, with the additional constraint that the point must share either the x-coordinate or the y-coordinate with `(x, y)`.
- Expected output format: The coordinates of the nearest point.
- Key requirements and edge cases to consider: Handle cases where multiple points have the same minimum Manhattan distance, and cases where there are no points that share the x or y coordinate with the given point.
- Example test cases with explanations: 
    - Example 1: Given `x = 3, y = 4` and `points = [[1,2],[3,1],[2,4],[2,3],[4,4]]`, the nearest point is `[3,1]`.
    - Example 2: Given `x = 3, y = 4` and `points = [[3,4]]`, the nearest point is `[3,4]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The simplest approach is to iterate through all points and calculate the Manhattan distance for each point that shares either the x-coordinate or the y-coordinate with the given point `(x, y)`.
- Step-by-step breakdown of the solution: 
    1. Initialize the minimum distance to infinity and the nearest point to null.
    2. Iterate through each point in the list of points.
    3. For each point, check if it shares either the x-coordinate or the y-coordinate with `(x, y)`.
    4. If it does, calculate the Manhattan distance between the point and `(x, y)`.
    5. If the calculated distance is less than the current minimum distance, update the minimum distance and the nearest point.
- Why this approach comes to mind first: It is the most straightforward way to solve the problem, as it involves checking every possible point and calculating the distance, which directly aligns with the problem's requirements.

```cpp
#include <vector>
#include <climits>

std::vector<int> nearestPoint(int x, int y, std::vector<std::vector<int>>& points) {
    int minDistance = INT_MAX;
    std::vector<int> nearestPoint;
    
    for (const auto& point : points) {
        if (point[0] == x || point[1] == y) {
            int distance = abs(point[0] - x) + abs(point[1] - y);
            if (distance < minDistance) {
                minDistance = distance;
                nearestPoint = point;
            }
        }
    }
    
    return nearestPoint;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of points, because we are potentially checking every point once.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the minimum distance and the nearest point.
> - **Why these complexities occur:** The time complexity is linear because we iterate through the list of points once, and the space complexity is constant because we use a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved with the same approach as the brute force method because we must check every point that shares either the x-coordinate or the y-coordinate with `(x, y)` to find the nearest one.
- Detailed breakdown of the approach: 
    1. Iterate through each point in the list of points.
    2. For each point, check if it shares either the x-coordinate or the y-coordinate with `(x, y)`.
    3. If it does, calculate the Manhattan distance between the point and `(x, y)`.
    4. Keep track of the point with the minimum Manhattan distance found so far.
- Why further optimization is impossible: We must check every relevant point to ensure we find the one with the minimum Manhattan distance, making the linear time complexity optimal for this problem.

```cpp
#include <vector>
#include <climits>

std::vector<int> nearestPoint(int x, int y, std::vector<std::vector<int>>& points) {
    int minDistance = INT_MAX;
    std::vector<int> nearestPoint;
    
    for (const auto& point : points) {
        if (point[0] == x || point[1] == y) {
            int distance = abs(point[0] - x) + abs(point[1] - y);
            if (distance < minDistance) {
                minDistance = distance;
                nearestPoint = point;
            }
        }
    }
    
    return nearestPoint;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of points, because we are potentially checking every point once.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the minimum distance and the nearest point.
> - **Optimality proof:** The time complexity is optimal because we must examine each point to determine if it shares an x or y coordinate with the target point and to calculate its distance, and the space complexity is optimal because we only need a constant amount of space to keep track of the minimum distance and the corresponding point.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional checks, and distance calculation.
- Problem-solving patterns identified: The need to check every possible solution (in this case, every point) to find the optimal one.
- Optimization techniques learned: While the problem does not allow for significant optimization beyond the straightforward approach, it highlights the importance of understanding the problem constraints and requirements.
- Similar problems to practice: Other problems involving point distances, coordinate geometry, and iteration.

**Mistakes to Avoid:**
- Common implementation errors: Failing to initialize variables properly, not checking for edge cases (like an empty list of points), and incorrectly calculating distances.
- Edge cases to watch for: Handling cases where multiple points have the same minimum distance, and cases where there are no points that share the x or y coordinate with the given point.
- Performance pitfalls: Not using the most efficient data structures or algorithms for the problem, which in this case is simply iterating through the list of points.
- Testing considerations: Ensuring that the solution works correctly for various inputs, including edge cases and large datasets.