## Count Number of Rectangles Containing Each Point

**Problem Link:** https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/description

**Problem Statement:**
- Input format and constraints: Given a list of rectangles and a list of points, count the number of rectangles that contain each point. Each rectangle is represented by two points: the bottom-left corner and the top-right corner. The points are represented by their x and y coordinates.
- Expected output format: Return a list of counts, where each count represents the number of rectangles that contain the corresponding point.
- Key requirements and edge cases to consider: The rectangles and points are given as lists of pairs of integers, and the coordinates of the points and rectangles are within the range $[-10^4, 10^4]$.
- Example test cases with explanations: For example, given rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[2,3,4,4]] and points = [[2,3],[2,2],[3,4],[1,1]], the output should be [3,2,2,0], because there are 3 rectangles that contain the point (2,3), 2 rectangles that contain the point (2,2), 2 rectangles that contain the point (3,4), and 0 rectangles that contain the point (1,1).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we need to iterate over each point and check if it is contained within each rectangle.
- Step-by-step breakdown of the solution:
  1. Initialize a list to store the count of rectangles that contain each point.
  2. Iterate over each point.
  3. For each point, iterate over each rectangle.
  4. Check if the point is contained within the rectangle by comparing the x and y coordinates.
  5. If the point is contained within the rectangle, increment the count for that point.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it may not be efficient for large inputs because it has a high time complexity.

```cpp
vector<int> countRectangles(vector<vector<int>>& rectangles, vector<vector<int>>& points) {
    vector<int> result(points.size(), 0);
    for (int i = 0; i < points.size(); i++) {
        for (auto& rectangle : rectangles) {
            if (rectangle[0] <= points[i][0] && points[i][0] <= rectangle[2] && rectangle[1] <= points[i][1] && points[i][1] <= rectangle[3]) {
                result[i]++;
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of points and $m$ is the number of rectangles, because we iterate over each point and each rectangle.
> - **Space Complexity:** $O(n)$, because we store the count of rectangles that contain each point.
> - **Why these complexities occur:** The time complexity is high because we use nested loops to iterate over each point and each rectangle. The space complexity is moderate because we only store the count of rectangles that contain each point.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a similar approach to the brute force solution, but with some minor optimizations to improve the code quality and readability.
- Detailed breakdown of the approach:
  1. Initialize a list to store the count of rectangles that contain each point.
  2. Iterate over each point.
  3. For each point, iterate over each rectangle.
  4. Check if the point is contained within the rectangle by comparing the x and y coordinates.
  5. If the point is contained within the rectangle, increment the count for that point.
- Proof of optimality: This approach is optimal because we must iterate over each point and each rectangle to determine if the point is contained within the rectangle.
- Why further optimization is impossible: We cannot further optimize this solution because we must perform the same number of comparisons to determine if a point is contained within a rectangle.

```cpp
vector<int> countRectangles(vector<vector<int>>& rectangles, vector<vector<int>>& points) {
    vector<int> result(points.size(), 0);
    for (int i = 0; i < points.size(); i++) {
        for (const auto& rectangle : rectangles) {
            if (points[i][0] >= rectangle[0] && points[i][0] <= rectangle[2] && points[i][1] >= rectangle[1] && points[i][1] <= rectangle[3]) {
                result[i]++;
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of points and $m$ is the number of rectangles, because we iterate over each point and each rectangle.
> - **Space Complexity:** $O(n)$, because we store the count of rectangles that contain each point.
> - **Optimality proof:** This solution is optimal because we must perform the same number of comparisons to determine if a point is contained within a rectangle.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, comparison, and increment.
- Problem-solving patterns identified: We can use a brute force approach to solve this problem, but we can also optimize the solution by improving the code quality and readability.
- Optimization techniques learned: We can optimize the solution by using const references and improving the code quality.
- Similar problems to practice: Other problems that involve iteration, comparison, and increment.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the result vector, not iterating over each point and rectangle, and not checking if the point is contained within the rectangle.
- Edge cases to watch for: Points and rectangles with coordinates outside the range $[-10^4, 10^4]$.
- Performance pitfalls: Using a high time complexity solution for large inputs.
- Testing considerations: Test the solution with different inputs, including edge cases, to ensure it works correctly.