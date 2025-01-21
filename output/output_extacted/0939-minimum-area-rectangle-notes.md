## Minimum Area Rectangle

**Problem Link:** https://leetcode.com/problems/minimum-area-rectangle/description

**Problem Statement:**
- Input: A list of `points` where each point is represented as a list of two integers `[x, y]`.
- Constraints: `1 <= points.length <= 200`, `0 <= x, y <= 4e4`, All points are distinct.
- Expected Output: The minimum area of a rectangle that can be formed by connecting two pairs of points, or `0` if no rectangle can be formed.
- Key Requirements:
  - The sides of the rectangle must be parallel to the x-axis and y-axis.
  - The points must form two pairs of points with the same x-coordinate and two pairs with the same y-coordinate.
- Edge Cases:
  - If there are less than 4 points, no rectangle can be formed.
  - If all points have the same x-coordinate or the same y-coordinate, no rectangle can be formed.

**Example Test Cases:**
- `points = [[1,1],[1,3],[3,1],[3,3],[2,2]]`, Output: `2`
- `points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]`, Output: `2`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to check every possible combination of 4 points to see if they can form a rectangle.
- The brute force approach involves generating all possible combinations of 4 points from the given list of points.
- For each combination, check if the points can form a rectangle by comparing their x and y coordinates.

```cpp
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int minAreaRect(vector<vector<int>>& points) {
    int n = points.size();
    int minArea = INT_MAX;

    // Generate all possible combinations of 4 points
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            for (int k = j + 1; k < n; k++) {
                for (int l = k + 1; l < n; l++) {
                    // Check if points can form a rectangle
                    if ((points[i][0] == points[j][0] && points[k][0] == points[l][0] && 
                         points[i][1] == points[k][1] && points[j][1] == points[l][1]) ||
                        (points[i][0] == points[k][0] && points[j][0] == points[l][0] && 
                         points[i][1] == points[j][1] && points[k][1] == points[l][1]) ||
                        (points[i][0] == points[l][0] && points[j][0] == points[k][0] && 
                         points[i][1] == points[j][1] && points[k][1] == points[l][1])) {
                        // Calculate the area of the rectangle
                        int area = abs(points[i][0] - points[j][0]) * abs(points[i][1] - points[k][1]);
                        // Update the minimum area
                        minArea = min(minArea, area);
                    }
                }
            }
        }
    }

    // Return 0 if no rectangle can be formed
    return minArea == INT_MAX ? 0 : minArea;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^4)$, where $n$ is the number of points. This is because we are generating all possible combinations of 4 points.
> - **Space Complexity:** $O(1)$, as we are not using any extra space that scales with the input size.
> - **Why these complexities occur:** The brute force approach involves checking every possible combination of 4 points, which leads to a time complexity of $O(n^4)$. The space complexity is $O(1)$ because we are not using any extra space that scales with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a `set` to store the points and then check for each pair of points if the other two points that would form a rectangle exist in the set.
- We can use a `set` of pairs to store the points, where each pair represents a point in the 2D plane.
- For each pair of points, we can check if the other two points that would form a rectangle exist in the set.

```cpp
#include <vector>
#include <set>
#include <climits>

using namespace std;

int minAreaRect(vector<vector<int>>& points) {
    set<pair<int, int>> pointSet;
    for (auto& point : points) {
        pointSet.insert({point[0], point[1]});
    }

    int minArea = INT_MAX;
    for (int i = 0; i < points.size(); i++) {
        for (int j = i + 1; j < points.size(); j++) {
            // Check if points can form a rectangle
            if (points[i][0] != points[j][0] && points[i][1] != points[j][1]) {
                // Check if the other two points exist in the set
                if (pointSet.count({points[i][0], points[j][1]}) && 
                    pointSet.count({points[j][0], points[i][1]})) {
                    // Calculate the area of the rectangle
                    int area = abs(points[i][0] - points[j][0]) * abs(points[i][1] - points[j][1]);
                    // Update the minimum area
                    minArea = min(minArea, area);
                }
            }
        }
    }

    // Return 0 if no rectangle can be formed
    return minArea == INT_MAX ? 0 : minArea;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of points. This is because we are iterating over each pair of points.
> - **Space Complexity:** $O(n)$, as we are using a `set` to store the points.
> - **Optimality proof:** This is the optimal solution because we are only checking each pair of points once and using a `set` to efficiently check if the other two points exist. This reduces the time complexity from $O(n^4)$ to $O(n^2)$.

---

### Final Notes

**Learning Points:**
- The importance of using the right data structures, such as `set`, to improve efficiency.
- How to reduce the time complexity of a problem by using a more efficient algorithm.
- The importance of checking for edge cases and handling them correctly.

**Mistakes to Avoid:**
- Not using the right data structures, such as `set`, to improve efficiency.
- Not checking for edge cases and handling them correctly.
- Not reducing the time complexity of a problem by using a more efficient algorithm.