## Rectangle Area II
**Problem Link:** https://leetcode.com/problems/rectangle-area-ii/description

**Problem Statement:**
- Input format: A list of rectangles where each rectangle is represented as `[x, y, x', y']`, denoting a rectangle with its bottom-left corner at `(x, y)` and top-right corner at `(x', y')`.
- Expected output format: The total area of all rectangles.
- Key requirements and edge cases to consider: Overlapping rectangles, rectangles with zero area, and rectangles with negative coordinates.
- Example test cases with explanations:
  - `rectangles = [[0,0,2,2],[1,0,2,1],[1,1,2,2]]` should return `6`, which is the total area of all rectangles.
  - `rectangles = [[0,0,1000000000,1000000000]]` should return `1000000000000000000`, which is the area of a single large rectangle.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the total area, we can calculate the area of each rectangle and then add them together. However, we need to consider overlapping areas to avoid double-counting.
- Step-by-step breakdown of the solution:
  1. Calculate the area of each rectangle.
  2. Identify overlapping rectangles by checking if the x and y coordinates of one rectangle fall within the bounds of another rectangle.
  3. Calculate the overlapping area between two rectangles by finding the intersection of their x and y coordinates.
  4. Subtract the overlapping area from the total area to avoid double-counting.
- Why this approach comes to mind first: It is a straightforward approach that involves calculating the area of each rectangle and then adjusting for overlaps.

```cpp
int rectangleArea(vector<vector<int>>& rectangles) {
    long long totalArea = 0;
    for (int i = 0; i < rectangles.size(); i++) {
        int x1 = rectangles[i][0], y1 = rectangles[i][1], x2 = rectangles[i][2], y2 = rectangles[i][3];
        long long area = (long long)(x2 - x1) * (y2 - y1);
        for (int j = 0; j < i; j++) {
            int x3 = rectangles[j][0], y3 = rectangles[j][1], x4 = rectangles[j][2], y4 = rectangles[j][3];
            int overlapX = max(0, min(x2, x4) - max(x1, x3));
            int overlapY = max(0, min(y2, y4) - max(y1, y3));
            area -= (long long)overlapX * overlapY;
        }
        totalArea += area;
    }
    return (int)(totalArea % 1000000007);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the number of rectangles. This is because we are comparing each rectangle with every other rectangle to find overlaps.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input. This is because we are only using a constant amount of space to store the total area and other variables.
> - **Why these complexities occur:** The time complexity is quadratic due to the nested loop structure, and the space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a sweep line approach to efficiently calculate the area of all rectangles. This involves sorting the x-coordinates of all rectangles and then sweeping through them to calculate the area.
- Detailed breakdown of the approach:
  1. Sort the x-coordinates of all rectangles along with their corresponding y-coordinates.
  2. Initialize an empty set to store the active y-coordinates.
  3. Iterate through the sorted x-coordinates and update the active y-coordinates.
  4. Calculate the area of the rectangles by multiplying the width of the current x-coordinate with the sum of the lengths of the active y-coordinates.
- Proof of optimality: This approach is optimal because it avoids the need to compare each rectangle with every other rectangle, reducing the time complexity to $O(n \log n)$.

```cpp
int rectangleArea(vector<vector<int>>& rectangles) {
    vector<int> xCoords;
    for (auto& rect : rectangles) {
        xCoords.push_back(rect[0]);
        xCoords.push_back(rect[2]);
    }
    sort(xCoords.begin(), xCoords.end());
    xCoords.erase(unique(xCoords.begin(), xCoords.end()), xCoords.end());
    
    long long totalArea = 0;
    for (int i = 0; i < xCoords.size() - 1; i++) {
        int x1 = xCoords[i], x2 = xCoords[i + 1];
        set<int> activeY;
        for (auto& rect : rectangles) {
            if (rect[0] <= x1 && x2 <= rect[2]) {
                activeY.insert(rect[1]);
                activeY.insert(rect[3]);
            }
        }
        vector<int> yCoords(activeY.begin(), activeY.end());
        long long area = 0;
        for (int j = 0; j < yCoords.size() - 1; j++) {
            area += (long long)(yCoords[j + 1] - yCoords[j]) * (x2 - x1);
        }
        totalArea += area;
    }
    return (int)(totalArea % 1000000007);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ where $n$ is the number of rectangles. This is because we are sorting the x-coordinates and then iterating through them.
> - **Space Complexity:** $O(n)$, excluding the space needed for the input. This is because we are using a set to store the active y-coordinates.
> - **Optimality proof:** This approach is optimal because it uses a sweep line approach to efficiently calculate the area of all rectangles, reducing the time complexity to $O(n \log n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sweep line approach, sorting, and set operations.
- Problem-solving patterns identified: Breaking down complex problems into smaller sub-problems and using efficient algorithms to solve them.
- Optimization techniques learned: Using a sweep line approach to reduce the time complexity.
- Similar problems to practice: Other problems that involve calculating areas or volumes, such as `Container With Most Water` or `Volume of Histogram`.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, such as rectangles with zero area or negative coordinates.
- Edge cases to watch for: Rectangles with zero area, negative coordinates, or overlapping rectangles.
- Performance pitfalls: Using a brute force approach that has a high time complexity.
- Testing considerations: Testing the code with different inputs, including edge cases and large inputs, to ensure correctness and efficiency.