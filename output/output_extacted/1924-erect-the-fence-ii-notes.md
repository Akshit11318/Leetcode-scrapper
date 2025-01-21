## Erect the Fence II
**Problem Link:** https://leetcode.com/problems/erect-the-fence-ii/description

**Problem Statement:**
- Input format and constraints: Given a list of `points` representing the coordinates of wooden planks, and an integer `n`, find the length of the fence that can be built using these planks to form a straight line.
- Expected output format: The maximum length of the fence that can be built.
- Key requirements and edge cases to consider: The fence must be a straight line, and the planks can be used in any order.
- Example test cases with explanations:
  - `points = [[0,0],[1,1],[2,2],[3,3],[4,4]]`, `n = 5`. The maximum length of the fence is the distance between `(0,0)` and `(4,4)`, which is `5 * sqrt(2)`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can try all possible pairs of points and calculate the length of the line segment between them. Then, we can try to add more points to this line segment one by one.
- Step-by-step breakdown of the solution:
  1. Generate all possible pairs of points.
  2. For each pair of points, calculate the slope of the line segment between them.
  3. Try to add more points to the line segment with the same slope.
  4. Calculate the total length of the line segment.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible combinations of points.

```cpp
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

double calculateDistance(const vector<int>& p1, const vector<int>& p2) {
    return sqrt(pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2));
}

double bruteForce(vector<vector<int>>& points, int n) {
    double maxLength = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            double length = calculateDistance(points[i], points[j]);
            vector<vector<int>> currentLine = {points[i], points[j]};
            for (int k = 0; k < n; k++) {
                if (k != i && k != j) {
                    double slope = (points[j][1] - points[i][1]) * 1.0 / (points[j][0] - points[i][0]);
                    double newSlope = (points[k][1] - points[i][1]) * 1.0 / (points[k][0] - points[i][0]);
                    if (abs(slope - newSlope) < 1e-9) {
                        length += calculateDistance(currentLine.back(), points[k]);
                        currentLine.push_back(points[k]);
                    }
                }
            }
            maxLength = max(maxLength, length);
        }
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of points. This is because we are trying all possible pairs of points and then trying to add more points to each pair.
> - **Space Complexity:** $O(n)$, where $n$ is the number of points. This is because we are storing the points in a vector.
> - **Why these complexities occur:** The time complexity occurs because we are using three nested loops to try all possible combinations of points. The space complexity occurs because we are storing the points in a vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a hashmap to store the points with the same slope.
- Detailed breakdown of the approach:
  1. Create a hashmap to store the points with the same slope.
  2. Iterate through all points and calculate the slope with respect to each point.
  3. Store the points with the same slope in the hashmap.
  4. Calculate the total length of the line segment for each slope.
- Proof of optimality: This approach is optimal because it tries all possible combinations of points with the same slope, and it does so in a efficient manner using a hashmap.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <cmath>

using namespace std;

double calculateDistance(const vector<int>& p1, const vector<int>& p2) {
    return sqrt(pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2));
}

double optimalSolution(vector<vector<int>>& points, int n) {
    double maxLength = 0;
    for (int i = 0; i < n; i++) {
        unordered_map<double, vector<vector<int>>> slopeMap;
        for (int j = 0; j < n; j++) {
            if (i != j) {
                double slope = (points[j][1] - points[i][1]) * 1.0 / (points[j][0] - points[i][0]);
                slopeMap[slope].push_back(points[j]);
            }
        }
        for (auto& pair : slopeMap) {
            double length = 0;
            for (int k = 1; k < pair.second.size(); k++) {
                length += calculateDistance(pair.second[k-1], pair.second[k]);
            }
            maxLength = max(maxLength, length);
        }
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of points. This is because we are iterating through all points and calculating the slope with respect to each point.
> - **Space Complexity:** $O(n)$, where $n$ is the number of points. This is because we are storing the points in a hashmap.
> - **Optimality proof:** This approach is optimal because it tries all possible combinations of points with the same slope, and it does so in a efficient manner using a hashmap.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a hashmap to store points with the same slope.
- Problem-solving patterns identified: Trying all possible combinations of points and calculating the slope with respect to each point.
- Optimization techniques learned: Using a hashmap to store points with the same slope.
- Similar problems to practice: Problems that involve finding the maximum length of a line segment that can be formed using a set of points.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for division by zero when calculating the slope.
- Edge cases to watch for: When two points have the same x-coordinate, the slope is infinity.
- Performance pitfalls: Using a brute force approach that tries all possible combinations of points.
- Testing considerations: Testing the solution with different sets of points and checking for correctness.