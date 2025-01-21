## Minimum Area Rectangle II
**Problem Link:** https://leetcode.com/problems/minimum-area-rectangle-ii/description

**Problem Statement:**
- Input format: A list of points in the plane, where each point is represented as a pair of integers `(x, y)`.
- Constraints: `1 <= points.length <= 5 * 10^4`, `0 <= x, y <= 10^9`.
- Expected output format: The minimum area of a rectangle that can be formed using four points.
- Key requirements and edge cases to consider:
  - The rectangle must have sides parallel to the x and y axes.
  - The rectangle must be non-degenerate (i.e., have a non-zero area).
- Example test cases with explanations:
  - For example, given points `(1,1)`, `(1,3)`, `(3,1)`, and `(3,3)`, the minimum area rectangle is formed by these four points with an area of `4`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Generate all possible combinations of four points and calculate the area of the rectangle formed by each combination.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of four points.
  2. For each combination, calculate the area of the rectangle formed by the points.
  3. Keep track of the minimum area found.
- Why this approach comes to mind first: It is a straightforward and intuitive approach that guarantees finding the minimum area rectangle.

```cpp
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int minAreaRect(vector<vector<int>>& points) {
    int n = points.size();
    int minArea = INT_MAX;
    
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            for (int k = j + 1; k < n; k++) {
                for (int l = k + 1; l < n; l++) {
                    if (points[i][0] == points[j][0] && points[k][0] == points[l][0] &&
                        points[i][1] == points[k][1] && points[j][1] == points[l][1]) {
                        int area = abs(points[i][0] - points[j][0]) * abs(points[i][1] - points[k][1]);
                        minArea = min(minArea, area);
                    }
                }
            }
        }
    }
    
    return minArea == INT_MAX ? 0 : minArea;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^4)$, where $n$ is the number of points. This is because we generate all possible combinations of four points.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum area.
> - **Why these complexities occur:** The brute force approach generates all possible combinations of four points, resulting in a high time complexity. However, the space complexity is low because we only need to store the minimum area.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible combinations of four points, we can use a hashmap to store the points we have seen so far and their corresponding x and y coordinates.
- Detailed breakdown of the approach:
  1. Create a hashmap to store the points we have seen so far.
  2. Iterate through the points and for each point, check if we have seen the other three points that can form a rectangle with it.
  3. If we have seen the other three points, calculate the area of the rectangle and update the minimum area.
- Proof of optimality: This approach is optimal because we only need to iterate through the points once and use a hashmap to store the points we have seen so far, resulting in a much lower time complexity than the brute force approach.

```cpp
#include <vector>
#include <unordered_map>
#include <climits>

using namespace std;

int minAreaRect(vector<vector<int>>& points) {
    int n = points.size();
    int minArea = INT_MAX;
    unordered_map<int, unordered_set<int>> pointSet;
    
    for (int i = 0; i < n; i++) {
        int x = points[i][0];
        int y = points[i][1];
        pointSet[x].insert(y);
    }
    
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int x1 = points[i][0];
            int y1 = points[i][1];
            int x2 = points[j][0];
            int y2 = points[j][1];
            
            if (x1 == x2 || y1 == y2) {
                continue;
            }
            
            if (pointSet[x1].find(y2) != pointSet[x1].end() && pointSet[x2].find(y1) != pointSet[x2].end()) {
                int area = abs(x1 - x2) * abs(y1 - y2);
                minArea = min(minArea, area);
            }
        }
    }
    
    return minArea == INT_MAX ? 0 : minArea;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of points. This is because we iterate through the points and use a hashmap to store the points we have seen so far.
> - **Space Complexity:** $O(n)$, as we use a hashmap to store the points we have seen so far.
> - **Optimality proof:** This approach is optimal because we only need to iterate through the points once and use a hashmap to store the points we have seen so far, resulting in a much lower time complexity than the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a hashmap to store points and their corresponding x and y coordinates, and iterating through the points to find the minimum area rectangle.
- Problem-solving patterns identified: Using a hashmap to store points and their corresponding x and y coordinates, and iterating through the points to find the minimum area rectangle.
- Optimization techniques learned: Using a hashmap to store points and their corresponding x and y coordinates, and iterating through the points to find the minimum area rectangle.
- Similar problems to practice: Finding the maximum area rectangle, finding the minimum perimeter rectangle, etc.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the points are valid, not checking if the rectangle is non-degenerate, etc.
- Edge cases to watch for: When the points are on the same line, when the points are on the same x or y axis, etc.
- Performance pitfalls: Not using a hashmap to store the points, not iterating through the points efficiently, etc.
- Testing considerations: Testing the function with different inputs, testing the function with edge cases, etc.