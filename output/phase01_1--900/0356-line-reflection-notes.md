## Line Reflection
**Problem Link:** https://leetcode.com/problems/line-reflection/description

**Problem Statement:**
- Input format: A 2D vector `points` where each point is represented as a pair of integers `[x, y]`.
- Constraints: `1 <= points.length <= 70`, `-100 <= points[i][0] <= 100`, and `points[i][0] == points[j][0]` for all `i` and `j`.
- Expected output format: A boolean indicating whether the points form a line that is reflected around the vertical line `x = -100`.
- Key requirements and edge cases to consider: The points must form a line that can be reflected around `x = -100`, and there must be at least one point on each side of the line.
- Example test cases with explanations:
  - `points = [[1,1],[-1,1]]`: Returns `true` because the points form a line that is reflected around `x = 0`.
  - `points = [[1,1],[-1,-1]]`: Returns `false` because the points do not form a line that is reflected around `x = -100`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To check if the points form a line that is reflected around `x = -100`, we can try all possible pairs of points and check if they are symmetric around the line.
- Step-by-step breakdown of the solution:
  1. Iterate over all pairs of points.
  2. For each pair, check if the points are symmetric around the line `x = -100`.
  3. If we find a pair of points that are not symmetric, return `false`.
- Why this approach comes to mind first: It is a straightforward approach that checks all possible pairs of points.

```cpp
bool isReflected(vector<vector<int>>& points) {
    // Create a set to store the points
    unordered_set<string> pointSet;
    for (auto point : points) {
        pointSet.insert(to_string(point[0]) + "," + to_string(point[1]));
    }

    // Check all pairs of points
    for (auto point : points) {
        int reflectedX = -200 - point[0];
        string reflectedPoint = to_string(reflectedX) + "," + to_string(point[1]);
        if (pointSet.find(reflectedPoint) == pointSet.end()) {
            return false;
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the number of points, because we iterate over all pairs of points.
> - **Space Complexity:** $O(n)$ because we store all points in a set.
> - **Why these complexities occur:** The brute force approach has high time complexity because it checks all pairs of points. The space complexity is moderate because we store all points in a set.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a hashmap to store the points and their reflected points.
- Detailed breakdown of the approach:
  1. Create a hashmap to store the points and their reflected points.
  2. Iterate over all points and check if their reflected points exist in the hashmap.
  3. If we find a point that does not have a reflected point, return `false`.
- Proof of optimality: This approach is optimal because it checks each point only once and uses a hashmap to store the points, which allows for fast lookup.
- Why further optimization is impossible: This approach has the best possible time complexity because it checks each point only once.

```cpp
bool isReflected(vector<vector<int>>& points) {
    // Create a hashmap to store the points and their reflected points
    unordered_map<int, unordered_set<int>> pointMap;
    int minX = INT_MAX, maxX = INT_MIN;
    for (auto point : points) {
        minX = min(minX, point[0]);
        maxX = max(maxX, point[0]);
        pointMap[point[0]].insert(point[1]);
    }

    // Check all points
    for (auto point : points) {
        int reflectedX = minX + maxX - point[0];
        if (pointMap.find(reflectedX) == pointMap.end() || pointMap[reflectedX].find(point[1]) == pointMap[reflectedX].end()) {
            return false;
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of points, because we iterate over all points once.
> - **Space Complexity:** $O(n)$ because we store all points in a hashmap.
> - **Optimality proof:** This approach is optimal because it checks each point only once and uses a hashmap to store the points, which allows for fast lookup.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a hashmap to store points and their reflected points, and checking each point only once.
- Problem-solving patterns identified: Using a hashmap to improve the time complexity of an algorithm.
- Optimization techniques learned: Using a hashmap to reduce the time complexity of an algorithm.
- Similar problems to practice: Other problems that involve checking pairs of points, such as the "Contains Duplicate" problem.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty input.
- Edge cases to watch for: An empty input, or an input with only one point.
- Performance pitfalls: Using a brute force approach that checks all pairs of points.
- Testing considerations: Testing the algorithm with different inputs, including edge cases.