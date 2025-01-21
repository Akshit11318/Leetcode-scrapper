## Maximum Area Rectangle with Point Constraints I

**Problem Link:** https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-i/description

**Problem Statement:**
- Input: `points` - a 2D array of integers representing points in a plane, where each point is an array `[x, y]`.
- Constraints: `1 <= points.length <= 10^5`, `points[i].length == 2`, `0 <= x, y <= 10^9`.
- Expected output: The maximum area of a rectangle that can be formed using the given points as vertices.
- Key requirements: The rectangle must have its sides parallel to the x and y axes.
- Example test cases:
  - Input: `points = [[1,1],[1,3],[3,1],[3,3],[2,2]]`
  - Output: `4`
  - Explanation: The maximum area rectangle is formed by the points `(1,1)`, `(1,3)`, `(3,1)`, and `(3,3)`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the maximum area rectangle, we can consider all possible pairs of points as potential vertices of the rectangle.
- Step-by-step breakdown:
  1. Generate all possible pairs of points.
  2. For each pair, calculate the coordinates of the other two points that would form a rectangle with the given pair.
  3. Check if these points exist in the given set of points.
  4. If they do, calculate the area of the rectangle.
  5. Keep track of the maximum area found.

```cpp
int maxAreaRectangle(vector<vector<int>>& points) {
    int n = points.size();
    int maxArea = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            // Calculate coordinates of other two points
            int x1 = points[i][0], y1 = points[i][1];
            int x2 = points[j][0], y2 = points[j][1];
            int x3 = x1, y3 = y2;
            int x4 = x2, y4 = y1;
            // Check if these points exist
            bool exists = false;
            for (int k = 0; k < n; k++) {
                if (points[k][0] == x3 && points[k][1] == y3) exists = true;
            }
            for (int k = 0; k < n; k++) {
                if (points[k][0] == x4 && points[k][1] == y4) exists = exists && true;
            }
            if (exists) {
                // Calculate area
                int area = abs(x2 - x1) * abs(y2 - y1);
                maxArea = max(maxArea, area);
            }
        }
    }
    return maxArea;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of points. This is because we are iterating over all pairs of points and then checking for the existence of other points.
> - **Space Complexity:** $O(1)$, as we are not using any extra space that scales with input size.
> - **Why these complexities occur:** The brute force approach involves checking all possible pairs of points and then verifying the existence of the other two points for each pair, leading to a cubic time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of generating all possible pairs of points, we can use a hashmap to store the points and then iterate over all pairs of x-coordinates and y-coordinates to find the maximum area rectangle.
- Detailed breakdown:
  1. Create a hashmap to store the points.
  2. Iterate over all pairs of x-coordinates.
  3. For each pair of x-coordinates, iterate over all pairs of y-coordinates.
  4. Check if the points with the current x and y coordinates exist in the hashmap.
  5. If they do, calculate the area of the rectangle.
  6. Keep track of the maximum area found.

```cpp
int maxAreaRectangle(vector<vector<int>>& points) {
    unordered_map<int, unordered_set<int>> pointMap;
    for (auto& point : points) {
        pointMap[point[0]].insert(point[1]);
    }
    int maxArea = 0;
    for (auto& x1 : pointMap) {
        for (auto& x2 : pointMap) {
            if (x1.first != x2.first) {
                unordered_set<int> yCoords;
                for (auto& y : x1.second) {
                    if (pointMap[x2.first].count(y)) {
                        yCoords.insert(y);
                    }
                }
                if (yCoords.size() >= 2) {
                    int minY = INT_MAX, maxY = INT_MIN;
                    for (auto& y : yCoords) {
                        minY = min(minY, y);
                        maxY = max(maxY, y);
                    }
                    int area = abs(x2.first - x1.first) * abs(maxY - minY);
                    maxArea = max(maxArea, area);
                }
            }
        }
    }
    return maxArea;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of unique x-coordinates. This is because we are iterating over all pairs of x-coordinates and then finding the common y-coordinates.
> - **Space Complexity:** $O(n)$, as we are using a hashmap to store the points.
> - **Optimality proof:** This approach is optimal because it reduces the number of iterations from $O(n^3)$ to $O(n^2)$ by using a hashmap to store the points and then iterating over all pairs of x-coordinates and y-coordinates.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a hashmap to store points and iterating over all pairs of x-coordinates and y-coordinates to find the maximum area rectangle.
- Problem-solving patterns identified: Reducing the number of iterations by using a hashmap to store points.
- Optimization techniques learned: Using a hashmap to store points and iterating over all pairs of x-coordinates and y-coordinates.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for the existence of points in the hashmap before calculating the area.
- Edge cases to watch for: Handling cases where there are less than four points.
- Performance pitfalls: Using a brute force approach that involves checking all possible pairs of points.
- Testing considerations: Testing the solution with different inputs and edge cases to ensure correctness.