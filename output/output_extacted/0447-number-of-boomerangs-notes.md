## Number of Boomerangs
**Problem Link:** https://leetcode.com/problems/number-of-boomerangs/description

**Problem Statement:**
- Input format and constraints: The input is an array of pairs representing points in a 2D plane, where each point is a pair of integers.
- Expected output format: The output is the number of boomerangs in the given points.
- Key requirements and edge cases to consider: A boomerang is formed by three points where the distance between the first and second points is equal to the distance between the second and third points.
- Example test cases with explanations:
  - `points = [[0,0],[1,0],[2,0]]`: There is 1 boomerang.
  - `points = [[1,1]]`: There is 0 boomerangs.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach is to iterate over all possible combinations of three points and check if they form a boomerang.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of three points.
  2. For each combination, calculate the distances between the first and second points, and the second and third points.
  3. If the distances are equal, increment the count of boomerangs.
- Why this approach comes to mind first: It is the most straightforward approach, as it checks all possible combinations of points.

```cpp
#include <vector>
#include <cmath>
using namespace std;

int numberOfBoomerangs(vector<vector<int>>& points) {
    int count = 0;
    for (int i = 0; i < points.size(); i++) {
        for (int j = i + 1; j < points.size(); j++) {
            for (int k = j + 1; k < points.size(); k++) {
                int dist1 = pow(points[i][0] - points[j][0], 2) + pow(points[i][1] - points[j][1], 2);
                int dist2 = pow(points[j][0] - points[k][0], 2) + pow(points[j][1] - points[k][1], 2);
                if (dist1 == dist2) {
                    count++;
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where n is the number of points. This is because we have three nested loops that iterate over all points.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the count of boomerangs.
> - **Why these complexities occur:** The time complexity is high because we are generating all possible combinations of three points, and the space complexity is low because we only need to store a single variable.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible combinations of three points, we can iterate over each point and calculate the distances to all other points.
- Detailed breakdown of the approach:
  1. Iterate over each point.
  2. For each point, calculate the distances to all other points and store them in a map.
  3. For each distance, increment the count of boomerangs by the number of pairs of points with the same distance.
- Proof of optimality: This approach has a lower time complexity than the brute force approach because it avoids generating all possible combinations of three points.

```cpp
#include <vector>
#include <unordered_map>
using namespace std;

int numberOfBoomerangs(vector<vector<int>>& points) {
    int count = 0;
    for (int i = 0; i < points.size(); i++) {
        unordered_map<int, int> distCount;
        for (int j = 0; j < points.size(); j++) {
            if (i == j) continue;
            int dist = pow(points[i][0] - points[j][0], 2) + pow(points[i][1] - points[j][1], 2);
            distCount[dist]++;
        }
        for (auto& pair : distCount) {
            count += pair.second * (pair.second - 1);
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where n is the number of points. This is because we have two nested loops that iterate over all points.
> - **Space Complexity:** $O(n)$, as we use a map to store the distances to all other points.
> - **Optimality proof:** This approach is optimal because it has the lowest possible time complexity for this problem, as we must iterate over all points to find all boomerangs.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a map to store distances and count pairs of points with the same distance.
- Problem-solving patterns identified: Avoiding generating all possible combinations of points by iterating over each point and calculating distances to all other points.
- Optimization techniques learned: Using a map to store distances and count pairs of points with the same distance.
- Similar problems to practice: Problems that involve finding pairs or combinations of points with certain properties.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for the case where a point is the same as another point.
- Edge cases to watch for: Points with the same coordinates.
- Performance pitfalls: Generating all possible combinations of points.
- Testing considerations: Testing with points that have the same coordinates and points that form boomerangs.