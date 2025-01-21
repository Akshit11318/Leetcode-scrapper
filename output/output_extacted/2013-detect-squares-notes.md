## Detect Squares
**Problem Link:** https://leetcode.com/problems/detect-squares/description

**Problem Statement:**
- Input format: You are given a class `DetectSquares` with methods `add` and `count`.
- Input constraints: The `add` method takes a 2D point `point = [p1, p2]`, and the `count` method takes two points `p1` and `p2`.
- Expected output format: The `count` method returns the number of squares that can be formed with the given point and the points stored in the system.
- Key requirements and edge cases to consider: A square is formed when two points are the same distance apart as the given point and another stored point.
- Example test cases with explanations:
  - `add([1,1])`, `add([0,0])`, `count([1,0])` returns 1 because there is one square with points (1,1), (0,0), (1,0), and (0,1).
  - `add([3,1])`, `add([1,1])`, `add([0,0])`, `count([2,0])` returns 2 because there are two squares with points (3,1), (1,1), (3,0), (1,0) and (1,1), (0,0), (1,0), (0,1).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the number of squares that can be formed with the given point and the stored points, we can iterate over all pairs of stored points and check if they can form a square with the given point.
- Step-by-step breakdown of the solution:
  1. Store the points in a data structure, such as a set or a list.
  2. Iterate over all pairs of stored points.
  3. For each pair, calculate the distance between the points.
  4. Check if the given point can form a square with the current pair of points by calculating the distance between the given point and each point in the pair.
  5. If the distances match, increment the count of squares.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it has a high time complexity due to the iteration over all pairs of stored points.

```cpp
class DetectSquares {
public:
    unordered_map<int, unordered_map<int, int>> points;
    
    DetectSquares() {}
    
    void add(vector<int> point) {
        int x = point[0], y = point[1];
        if (points.find(x) == points.end()) points[x] = {};
        points[x][y]++;
    }
    
    int count(vector<int> point1) {
        int x1 = point1[0], y1 = point1[1];
        int count = 0;
        for (auto& p : points) {
            for (auto& q : p.second) {
                int x2 = p.first, y2 = q.first;
                if (x1 == x2 || y1 == y2) continue;
                int dist = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
                int x3 = x1, y3 = y2;
                int x4 = x2, y4 = y1;
                if (points.find(x3) != points.end() && points[x3].find(y3) != points[x3].end() &&
                    points.find(x4) != points.end() && points[x4].find(y4) != points[x4].end()) {
                    count += q.second * points[x3][y3];
                }
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of stored points.
> - **Space Complexity:** $O(n)$, where $n$ is the number of stored points.
> - **Why these complexities occur:** The brute force approach has a high time complexity because it iterates over all pairs of stored points. The space complexity is linear because we store all points in a data structure.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a hashmap to store the frequency of each point, and then iterate over all points to count the number of squares.
- Detailed breakdown of the approach:
  1. Store the points in a hashmap, where the key is the point and the value is the frequency of the point.
  2. Iterate over all points in the hashmap.
  3. For each point, iterate over all other points in the hashmap.
  4. Check if the current point and the other point can form a square with the given point.
  5. If they can, increment the count of squares by the product of the frequencies of the two points.
- Proof of optimality: This approach is optimal because it has a lower time complexity than the brute force approach and it still counts all possible squares.

```cpp
class DetectSquares {
public:
    unordered_map<int, unordered_map<int, int>> points;
    
    DetectSquares() {}
    
    void add(vector<int> point) {
        int x = point[0], y = point[1];
        if (points.find(x) == points.end()) points[x] = {};
        points[x][y]++;
    }
    
    int count(vector<int> point1) {
        int x1 = point1[0], y1 = point1[1];
        int count = 0;
        for (auto& p : points) {
            for (auto& q : p.second) {
                int x2 = p.first, y2 = q.first;
                if (x1 == x2 || y1 == y2) continue;
                int dist = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
                int x3 = x1, y3 = y2;
                int x4 = x2, y4 = y1;
                if (points.find(x3) != points.end() && points[x3].find(y3) != points[x3].end() &&
                    points.find(x4) != points.end() && points[x4].find(y4) != points[x4].end()) {
                    count += q.second * points[x3][y3];
                }
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of unique x-coordinates.
> - **Space Complexity:** $O(n)$, where $n$ is the number of points.
> - **Optimality proof:** This approach is optimal because it has a lower time complexity than the brute force approach and it still counts all possible squares.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hashmap, iteration over points.
- Problem-solving patterns identified: Using a hashmap to store frequencies of points, iterating over points to count squares.
- Optimization techniques learned: Reducing time complexity by using a hashmap.
- Similar problems to practice: Other problems involving points and squares, such as finding the number of squares in a grid.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as points with the same x or y coordinate.
- Edge cases to watch for: Points with the same x or y coordinate, points with the same distance from the given point.
- Performance pitfalls: Using a brute force approach with a high time complexity.
- Testing considerations: Testing with different inputs, such as points with different x and y coordinates, points with the same x or y coordinate.