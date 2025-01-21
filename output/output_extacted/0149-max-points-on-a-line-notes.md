## Max Points on a Line

**Problem Link:** https://leetcode.com/problems/max-points-on-a-line/description

**Problem Statement:**
- Input format: A list of points where each point is represented as an array of two integers.
- Constraints: The input list will have at least one point and at most 300 points.
- Expected output format: The maximum number of points that lie on the same straight line.
- Key requirements and edge cases to consider: Handling duplicate points, vertical lines, and points with the same slope.
- Example test cases with explanations:
  - For the input `[[1,1],[2,2],[3,3]]`, the output should be `3` because all three points lie on the same line.
  - For the input `[[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]`, the output should be `4` because there are four points that lie on the same line.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the slope of the line passing through each pair of points and store the slopes in a hashmap.
- Step-by-step breakdown of the solution:
  1. Iterate through each point in the list.
  2. For each point, iterate through the remaining points in the list.
  3. Calculate the slope of the line passing through the two points.
  4. Store the slope in a hashmap and increment the count of points with the same slope.
- Why this approach comes to mind first: It is a straightforward approach that considers all possible pairs of points.

```cpp
int maxPoints(vector<vector<int>>& points) {
    int n = points.size();
    int maxPoints = 0;
    for (int i = 0; i < n; i++) {
        unordered_map<double, int> slopeCount;
        int samePoint = 1;
        for (int j = i + 1; j < n; j++) {
            if (points[i] == points[j]) {
                samePoint++;
                continue;
            }
            double slope = calculateSlope(points[i], points[j]);
            slopeCount[slope]++;
        }
        maxPoints = max(maxPoints, *max_element(slopeCount.begin(), slopeCount.end(), [](auto& a, auto& b) { return a.second < b.second; }) + samePoint);
    }
    return maxPoints;
}

double calculateSlope(vector<int>& point1, vector<int>& point2) {
    int x1 = point1[0], y1 = point1[1];
    int x2 = point2[0], y2 = point2[1];
    if (x1 == x2) return numeric_limits<double>::infinity();
    double slope = (double)(y2 - y1) / (x2 - x1);
    return slope;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the number of points. This is because we are iterating through each pair of points.
> - **Space Complexity:** $O(n)$ where $n$ is the number of points. This is because we are storing the slope counts in a hashmap.
> - **Why these complexities occur:** The brute force approach has a high time complexity because it considers all possible pairs of points. The space complexity is relatively low because we are only storing the slope counts.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of calculating the slope for each pair of points, we can calculate the slope for each point with respect to all other points.
- Detailed breakdown of the approach:
  1. Iterate through each point in the list.
  2. For each point, calculate the slope with respect to all other points.
  3. Store the slope counts in a hashmap and increment the count of points with the same slope.
- Proof of optimality: This approach is optimal because we are only considering each point once and calculating the slope with respect to all other points.

```cpp
int maxPoints(vector<vector<int>>& points) {
    int n = points.size();
    int maxPoints = 0;
    for (int i = 0; i < n; i++) {
        unordered_map<double, int> slopeCount;
        int samePoint = 1;
        int localMax = 0;
        for (int j = i + 1; j < n; j++) {
            if (points[i] == points[j]) {
                samePoint++;
                continue;
            }
            double slope = calculateSlope(points[i], points[j]);
            slopeCount[slope]++;
            localMax = max(localMax, slopeCount[slope]);
        }
        maxPoints = max(maxPoints, localMax + samePoint);
    }
    return maxPoints;
}

double calculateSlope(vector<int>& point1, vector<int>& point2) {
    int x1 = point1[0], y1 = point1[1];
    int x2 = point2[0], y2 = point2[1];
    if (x1 == x2) return numeric_limits<double>::infinity();
    double slope = (double)(y2 - y1) / (x2 - x1);
    return slope;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the number of points. This is because we are iterating through each point and calculating the slope with respect to all other points.
> - **Space Complexity:** $O(n)$ where $n$ is the number of points. This is because we are storing the slope counts in a hashmap.
> - **Optimality proof:** This approach is optimal because we are only considering each point once and calculating the slope with respect to all other points.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Slope calculation, hashmap usage, and iteration through points.
- Problem-solving patterns identified: Considering all possible pairs of points and calculating the slope for each pair.
- Optimization techniques learned: Instead of calculating the slope for each pair of points, calculate the slope for each point with respect to all other points.
- Similar problems to practice: Other problems involving slope calculation and hashmap usage.

**Mistakes to Avoid:**
- Common implementation errors: Not handling duplicate points and not considering vertical lines.
- Edge cases to watch for: Points with the same slope and points with the same coordinates.
- Performance pitfalls: Using a brute force approach with a high time complexity.
- Testing considerations: Test the solution with different inputs, including duplicate points and points with the same slope.