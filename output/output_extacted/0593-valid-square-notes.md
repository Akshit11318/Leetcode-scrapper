## Valid Square

**Problem Link:** https://leetcode.com/problems/valid-square/description

**Problem Statement:**
- Input: Four points in a 2D plane, represented as an array of four pairs of integers, `p1`, `p2`, `p3`, `p4`.
- Constraints: All points are distinct and lie within the range of $0 \le x, y \le 10000$.
- Expected Output: Determine if the four points form a valid square, returning `true` if they do and `false` otherwise.
- Key Requirements: A valid square has all sides of equal length and all internal angles are right angles (90 degrees).
- Edge Cases: Consider cases where points are collinear, form other shapes, or are not distinct.

**Example Test Cases:**
- `[[0,0],[2,2],[3,10],[5,2]]` should return `false` because the points do not form a square.
- `[[1,1],[3,0],[1,0],[3,1]]` should return `true` because the points form a square.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves calculating the distances between all pairs of points to identify if any four points form a square.
- We can use the distance formula $\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$ to calculate the distance between two points $(x_1, y_1)$ and $(x_2, y_2)$.
- We need to compare all possible pairs of distances to find four equal distances that could represent the sides of a square.
- Additionally, we must verify that the diagonals of the potential square are also of equal length and that their length is $\sqrt{2}$ times the length of a side, as per the properties of a square.

```cpp
#include <vector>
#include <cmath>
using namespace std;

bool validSquare(vector<vector<int>>& p1, vector<vector<int>>& p2, vector<vector<int>>& p3, vector<vector<int>>& p4) {
    vector<vector<int>> points = {p1, p2, p3, p4};
    double dist[6]; // To store distances between all pairs of points
    int index = 0;
    for (int i = 0; i < 4; i++) {
        for (int j = i + 1; j < 4; j++) {
            dist[index++] = sqrt(pow(points[i][0] - points[j][0], 2) + pow(points[i][1] - points[j][1], 2));
        }
    }
    // Sort distances to easily identify equal side lengths
    sort(dist, dist + 6);
    // Check for square properties: four equal sides and two equal diagonals
    return dist[0] == dist[1] && dist[1] == dist[2] && dist[2] == dist[3] && dist[4] == dist[5] && dist[0] != 0 && dist[4] == sqrt(2) * dist[0];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because we are dealing with a fixed number of points (four) and performing a constant number of operations.
> - **Space Complexity:** $O(1)$ as we use a fixed amount of space to store the distances.
> - **Why these complexities occur:** The number of operations does not grow with the size of the input; it remains constant.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight here is to directly calculate the distances between all pairs of points and check if the conditions for a square are met.
- We calculate the distances between all pairs of points and store them in an array.
- Then, we sort the distances and check if the first four distances are equal (representing the sides of the square) and if the last two distances are equal (representing the diagonals).
- Additionally, we verify that the length of the diagonal is $\sqrt{2}$ times the length of a side.

```cpp
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

bool validSquare(vector<vector<int>>& p1, vector<vector<int>>& p2, vector<vector<int>>& p3, vector<vector<int>>& p4) {
    vector<double> dist;
    vector<vector<int>> points = {p1, p2, p3, p4};
    for (int i = 0; i < 4; i++) {
        for (int j = i + 1; j < 4; j++) {
            double d = sqrt(pow(points[i][0] - points[j][0], 2) + pow(points[i][1] - points[j][1], 2));
            dist.push_back(d);
        }
    }
    sort(dist.begin(), dist.end());
    // Check for square properties: four equal sides and two equal diagonals
    return dist[0] == dist[1] && dist[1] == dist[2] && dist[2] == dist[3] && dist[4] == dist[5] && dist[0] != 0 && abs(dist[4] - sqrt(2) * dist[0]) < 1e-7;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because, similar to the brute force approach, we're dealing with a fixed number of points and operations.
> - **Space Complexity:** $O(1)$ for the same reason as the brute force approach.
> - **Optimality proof:** This is optimal because we must calculate the distances between all pairs of points to determine if they form a square, and we do this in constant time due to the fixed number of points.

---

### Final Notes

**Learning Points:**
- The importance of understanding geometric properties, such as those of a square.
- How to calculate distances between points in a 2D plane using the distance formula.
- The value of sorting data to simplify comparisons, as seen with the distances.

**Mistakes to Avoid:**
- Not checking for the distinctness of points and the non-zero length of sides.
- Failing to verify the relationship between the lengths of the sides and diagonals of a square.
- Not considering floating-point precision issues when comparing distances.