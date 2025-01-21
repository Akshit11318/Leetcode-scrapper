## Minimize Manhattan Distances
**Problem Link:** https://leetcode.com/problems/minimize-manhattan-distances/description

**Problem Statement:**
- Input format and constraints: The problem involves `n` points in a 2D plane, where each point is represented as `(x, y)`. The goal is to find a point `(a, b)` that minimizes the sum of Manhattan distances to all `n` points.
- Expected output format: The output should be a point `(a, b)` that minimizes the sum of Manhattan distances.
- Key requirements and edge cases to consider: The problem statement does not specify any particular constraints on the input points, so the solution should be able to handle any set of points in the 2D plane.
- Example test cases with explanations: For example, given points `(1, 1)`, `(2, 2)`, and `(3, 3)`, the optimal point would be `(2, 2)`, as it has the minimum sum of Manhattan distances to all three points.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One possible approach is to try all possible points in the 2D plane and calculate the sum of Manhattan distances for each point.
- Step-by-step breakdown of the solution: 
  1. Define the search space for possible points.
  2. For each point in the search space, calculate the sum of Manhattan distances to all `n` points.
  3. Keep track of the point with the minimum sum of Manhattan distances.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient for large inputs.

```cpp
#include <iostream>
#include <vector>
#include <climits>

using namespace std;

struct Point {
    int x, y;
};

int calculateManhattanDistance(const Point& p1, const Point& p2) {
    return abs(p1.x - p2.x) + abs(p1.y - p2.y);
}

Point minimizeManhattanDistancesBruteForce(vector<Point>& points) {
    int minX = INT_MAX, minY = INT_MAX, maxX = INT_MIN, maxY = INT_MIN;
    
    // Find the bounding box of the points
    for (const auto& point : points) {
        minX = min(minX, point.x);
        minY = min(minY, point.y);
        maxX = max(maxX, point.x);
        maxY = max(maxY, point.y);
    }
    
    int minSum = INT_MAX;
    Point optimalPoint;
    
    // Try all points in the bounding box
    for (int x = minX; x <= maxX; x++) {
        for (int y = minY; y <= maxY; y++) {
            Point currentPoint = {x, y};
            int sum = 0;
            for (const auto& point : points) {
                sum += calculateManhattanDistance(currentPoint, point);
            }
            if (sum < minSum) {
                minSum = sum;
                optimalPoint = currentPoint;
            }
        }
    }
    
    return optimalPoint;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot (maxX - minX) \cdot (maxY - minY))$, where `n` is the number of points and `(maxX - minX)` and `(maxY - minY)` are the dimensions of the bounding box.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the optimal point and other variables.
> - **Why these complexities occur:** The time complexity is due to the nested loops that try all points in the bounding box, and the space complexity is due to the fact that we only use a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal point is the median of the x-coordinates and the median of the y-coordinates.
- Detailed breakdown of the approach:
  1. Sort the x-coordinates and find the median.
  2. Sort the y-coordinates and find the median.
  3. The optimal point is the median of the x-coordinates and the median of the y-coordinates.
- Proof of optimality: This approach is optimal because the Manhattan distance is a linear function, and the median is the point that minimizes the sum of absolute differences.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Point {
    int x, y;
};

Point minimizeManhattanDistancesOptimal(vector<Point>& points) {
    vector<int> xCoords, yCoords;
    
    // Separate the x and y coordinates
    for (const auto& point : points) {
        xCoords.push_back(point.x);
        yCoords.push_back(point.y);
    }
    
    // Sort the x and y coordinates
    sort(xCoords.begin(), xCoords.end());
    sort(yCoords.begin(), yCoords.end());
    
    // Find the median of the x and y coordinates
    int medianX = xCoords[points.size() / 2];
    int medianY = yCoords[points.size() / 2];
    
    return {medianX, medianY};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where `n` is the number of points.
> - **Space Complexity:** $O(n)$, where `n` is the number of points.
> - **Optimality proof:** This approach is optimal because it finds the median of the x-coordinates and the median of the y-coordinates, which is the point that minimizes the sum of Manhattan distances.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the concept of Manhattan distance and the importance of finding the median of a set of points.
- Problem-solving patterns identified: The problem requires finding the optimal point that minimizes the sum of Manhattan distances, which involves sorting and finding the median of the x and y coordinates.
- Optimization techniques learned: The problem demonstrates the importance of using efficient algorithms, such as sorting and finding the median, to solve optimization problems.
- Similar problems to practice: Other problems that involve finding the optimal point or minimizing the sum of distances, such as the geometric median problem.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty set of points, or not handling the case where the number of points is even.
- Edge cases to watch for: The problem requires handling the case where the number of points is even or odd, and finding the median of the x and y coordinates.
- Performance pitfalls: Using inefficient algorithms, such as trying all possible points, can lead to poor performance for large inputs.
- Testing considerations: The problem requires testing the solution with different sets of points, including edge cases, to ensure that it produces the correct output.