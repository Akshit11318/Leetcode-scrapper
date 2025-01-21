## Minimum Rectangles to Cover Points
**Problem Link:** [https://leetcode.com/problems/minimum-rectangles-to-cover-points/description](https://leetcode.com/problems/minimum-rectangles-to-cover-points/description)

**Problem Statement:**
- Input format: A 2D array `points` where each point is represented as an array of two integers `[x, y]`.
- Constraints: `1 <= points.length <= 5 * 10^4`, `points[i].length == 2`, `0 <= x, y <= 10^9`.
- Expected output format: The minimum number of rectangles needed to cover all points.
- Key requirements and edge cases to consider: Points can have the same x-coordinate or y-coordinate, and rectangles can overlap.
- Example test cases with explanations:
  - Input: `points = [[1,1],[2,2],[3,3],[4,4],[5,5]]`, Output: `2`. We can cover all points with two rectangles: one with top-left corner `(1,1)` and bottom-right corner `(3,3)`, and another with top-left corner `(3,3)` and bottom-right corner `(5,5)`.
  - Input: `points = [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]]`, Output: `3`. We can cover all points with three rectangles: one with top-left corner `(1,1)` and bottom-right corner `(2,2)`, another with top-left corner `(3,3)` and bottom-right corner `(4,4)`, and another with top-left corner `(5,5)` and bottom-right corner `(6,6)`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We need to cover all points with rectangles, so we can start by checking all possible combinations of points and see if they can be covered by a single rectangle.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of points.
  2. For each combination, check if all points can be covered by a single rectangle.
  3. If they can, increment the count of rectangles and remove the covered points from the list.
- Why this approach comes to mind first: It's a straightforward approach that checks all possibilities, but it's not efficient due to the high number of combinations.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int minRectangles(vector<vector<int>>& points) {
    int n = points.size();
    int ans = 0;
    vector<bool> covered(n, false);
    
    while (true) {
        int minX = INT_MAX, minY = INT_MAX, maxX = INT_MIN, maxY = INT_MIN;
        bool hasUncovered = false;
        
        for (int i = 0; i < n; i++) {
            if (!covered[i]) {
                hasUncovered = true;
                minX = min(minX, points[i][0]);
                minY = min(minY, points[i][1]);
                maxX = max(maxX, points[i][0]);
                maxY = max(maxY, points[i][1]);
            }
        }
        
        if (!hasUncovered) break;
        
        ans++;
        
        for (int i = 0; i < n; i++) {
            if (points[i][0] >= minX && points[i][0] <= maxX && points[i][1] >= minY && points[i][1] <= maxY) {
                covered[i] = true;
            }
        }
    }
    
    return ans;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of points. This is because in the worst case, we might need to check all points for each rectangle.
> - **Space Complexity:** $O(n)$, where $n$ is the number of points. This is because we need to store the covered status of each point.
> - **Why these complexities occur:** The brute force approach has high time complexity due to the nested loops and high space complexity due to the additional data structures used.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a sweep line approach to find the minimum number of rectangles needed to cover all points. We first sort the points by their x-coordinates, and then we iterate over the points and maintain a set of active y-coordinates.
- Detailed breakdown of the approach:
  1. Sort the points by their x-coordinates.
  2. Initialize an empty set to store the active y-coordinates.
  3. Initialize the count of rectangles to 0.
  4. Iterate over the points. For each point, add its y-coordinate to the set of active y-coordinates.
  5. If the size of the set of active y-coordinates is greater than the count of rectangles, increment the count of rectangles and reset the set of active y-coordinates.
- Proof of optimality: This approach is optimal because it ensures that we use the minimum number of rectangles needed to cover all points. The sweep line approach allows us to efficiently maintain the set of active y-coordinates and increment the count of rectangles only when necessary.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int minRectangles(vector<vector<int>>& points) {
    int n = points.size();
    sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] < b[0];
    });
    
    int ans = 0;
    set<int> active;
    
    for (const auto& point : points) {
        active.insert(point[1]);
        if (active.size() > ans) {
            ans++;
            active.clear();
            active.insert(point[1]);
        }
    }
    
    return ans;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of points. This is because we sort the points by their x-coordinates and use a set to store the active y-coordinates.
> - **Space Complexity:** $O(n)$, where $n$ is the number of points. This is because we need to store the points and the set of active y-coordinates.
> - **Optimality proof:** The optimal approach has a lower time complexity than the brute force approach and uses less space. It ensures that we use the minimum number of rectangles needed to cover all points.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sweep line approach, sorting, and set data structure.
- Problem-solving patterns identified: Using a sweep line approach to find the minimum number of rectangles needed to cover all points.
- Optimization techniques learned: Using a set to store the active y-coordinates and incrementing the count of rectangles only when necessary.
- Similar problems to practice: Other problems that involve using a sweep line approach, such as finding the maximum number of non-overlapping intervals.

**Mistakes to Avoid:**
- Common implementation errors: Not sorting the points by their x-coordinates, not using a set to store the active y-coordinates, and not incrementing the count of rectangles correctly.
- Edge cases to watch for: Points with the same x-coordinate or y-coordinate, and rectangles that overlap.
- Performance pitfalls: Using a brute force approach that has a high time complexity, not using a set to store the active y-coordinates, and not incrementing the count of rectangles correctly.
- Testing considerations: Testing the code with different inputs, including edge cases, to ensure that it produces the correct output.