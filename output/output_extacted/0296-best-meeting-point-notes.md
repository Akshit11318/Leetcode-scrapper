## Best Meeting Point
**Problem Link:** [https://leetcode.com/problems/best-meeting-point/description](https://leetcode.com/problems/best-meeting-point/description)

**Problem Statement:**
- Input format: A 2D grid of integers representing the coordinates of houses, where `grid[i][j] == 1` indicates a house.
- Constraints: `1 <= m, n <= 100`, where `m` and `n` are the dimensions of the grid.
- Expected output format: The coordinates `[x, y]` of the best meeting point, which minimizes the sum of Manhattan distances to all houses.
- Key requirements: Find the point that minimizes the total Manhattan distance to all houses.
- Example test cases:
  - Input: `[[1,0,0],[0,0,0],[0,0,1]]`
  - Output: `[1,2]`
  - Explanation: The best meeting point is at `[1,2]`, which has a total Manhattan distance of `4` to all houses.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over all possible points in the grid and calculate the Manhattan distance to each house.
- Step-by-step breakdown of the solution:
  1. Initialize the minimum total distance to infinity.
  2. Iterate over all points `(x, y)` in the grid.
  3. For each point, calculate the Manhattan distance to each house.
  4. Calculate the total distance by summing the Manhattan distances to all houses.
  5. Update the minimum total distance and the best meeting point if the current point has a smaller total distance.
- Why this approach comes to mind first: It is a straightforward approach that checks all possible solutions.

```cpp
vector<int> bestMeetingPoint(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    int minDistance = INT_MAX;
    vector<int> bestPoint;
    
    for (int x = 0; x < m; x++) {
        for (int y = 0; y < n; y++) {
            int totalDistance = 0;
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (grid[i][j] == 1) {
                        totalDistance += abs(x - i) + abs(y - j);
                    }
                }
            }
            if (totalDistance < minDistance) {
                minDistance = totalDistance;
                bestPoint = {x, y};
            }
        }
    }
    return bestPoint;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m^2 \cdot n^2)$, where $m$ and $n$ are the dimensions of the grid. This is because we iterate over all points in the grid and for each point, we iterate over all houses.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum total distance and the best meeting point.
> - **Why these complexities occur:** The time complexity is high because we use nested loops to iterate over all points and houses, resulting in a quadratic time complexity. The space complexity is low because we only use a constant amount of space to store the minimum total distance and the best meeting point.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The best meeting point is the median of the x-coordinates and the median of the y-coordinates of all houses.
- Detailed breakdown of the approach:
  1. Collect all x-coordinates and y-coordinates of houses in separate vectors.
  2. Sort the vectors of x-coordinates and y-coordinates.
  3. Find the median of the x-coordinates and the median of the y-coordinates.
  4. The best meeting point is the point with the median x-coordinate and the median y-coordinate.
- Proof of optimality: This approach is optimal because the Manhattan distance is minimized when the meeting point is at the median of the x-coordinates and the median of the y-coordinates.

```cpp
vector<int> bestMeetingPoint(vector<vector<int>>& grid) {
    vector<int> xCoords;
    vector<int> yCoords;
    
    for (int i = 0; i < grid.size(); i++) {
        for (int j = 0; j < grid[0].size(); j++) {
            if (grid[i][j] == 1) {
                xCoords.push_back(i);
                yCoords.push_back(j);
            }
        }
    }
    
    sort(xCoords.begin(), xCoords.end());
    sort(yCoords.begin(), yCoords.end());
    
    int x = xCoords[xCoords.size() / 2];
    int y = yCoords[yCoords.size() / 2];
    
    return {x, y};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot \log(m \cdot n))$, where $m$ and $n$ are the dimensions of the grid. This is because we iterate over all houses and sort the vectors of x-coordinates and y-coordinates.
> - **Space Complexity:** $O(m \cdot n)$, as we store the x-coordinates and y-coordinates of all houses in separate vectors.
> - **Optimality proof:** This approach is optimal because it finds the median of the x-coordinates and the median of the y-coordinates, which minimizes the Manhattan distance to all houses.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Sorting, median finding, Manhattan distance calculation.
- Problem-solving patterns: Finding the optimal solution by identifying the key insight that the best meeting point is the median of the x-coordinates and the median of the y-coordinates.
- Optimization techniques: Using sorting to find the median of the x-coordinates and the median of the y-coordinates.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty grid or a grid with no houses.
- Edge cases to watch for: Handling cases where the number of houses is odd or even.
- Performance pitfalls: Using a brute force approach that has a high time complexity.
- Testing considerations: Testing the solution with different grid sizes, house locations, and edge cases.