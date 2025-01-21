## Check If It Is a Straight Line

**Problem Link:** https://leetcode.com/problems/check-if-it-is-a-straight-line/description

**Problem Statement:**
- Input: An array of `coordinates` where `coordinates[i] = [x, y]` represents a point in the 2D plane.
- Constraints: `2 <= coordinates.length <= 100`, `coordinates[i].length == 2`, `-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4`.
- Expected Output: Return `true` if all the points lie on the same straight line, otherwise return `false`.
- Key Requirements and Edge Cases: Points can have the same coordinates, and there can be duplicate points. However, if two points have the same x-coordinate, the line is vertical and its slope is undefined.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To check if all points lie on a straight line, we can calculate the slope of the line formed by each pair of points and check if all slopes are the same.
- Step-by-step breakdown:
  1. Choose the first point as a reference.
  2. Calculate the slope of the line formed by the reference point and each of the other points.
  3. If any pair of points has a different slope, return `false`.
  4. If all slopes are the same, return `true`.
- Why this approach comes to mind first: It's straightforward to calculate slopes and compare them.

```cpp
bool checkStraightLine(vector<vector<int>>& coordinates) {
    if (coordinates.size() == 2) return true;
    
    int x0 = coordinates[0][0];
    int y0 = coordinates[0][1];
    int x1 = coordinates[1][0];
    int y1 = coordinates[1][1];
    
    for (int i = 2; i < coordinates.size(); ++i) {
        int x = coordinates[i][0];
        int y = coordinates[i][1];
        
        // Calculate cross product to avoid division by zero
        if ((x - x0) * (y1 - y0) != (y - y0) * (x1 - x0)) {
            return false;
        }
    }
    
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of points, because we iterate through all points once.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store the reference points and the current point.
> - **Why these complexities occur:** We perform a single pass through the points, and our calculations for each point take constant time.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The same approach as the brute force is actually optimal because we must check every point at least once to ensure it lies on the same line.
- Detailed breakdown: The provided code in the brute force section is already optimal because it only requires a single pass through the points and uses a constant amount of space.
- Proof of optimality: Any algorithm must at least read the input, which requires $O(n)$ time for $n$ points. Therefore, the given solution is optimal.

```cpp
// The code remains the same as the brute force approach.
bool checkStraightLine(vector<vector<int>>& coordinates) {
    if (coordinates.size() == 2) return true;
    
    int x0 = coordinates[0][0];
    int y0 = coordinates[0][1];
    int x1 = coordinates[1][0];
    int y1 = coordinates[1][1];
    
    for (int i = 2; i < coordinates.size(); ++i) {
        int x = coordinates[i][0];
        int y = coordinates[i][1];
        
        // Calculate cross product to avoid division by zero
        if ((x - x0) * (y1 - y0) != (y - y0) * (x1 - x0)) {
            return false;
        }
    }
    
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of points.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space.
> - **Optimality proof:** The algorithm is optimal because it achieves the lower bound of $O(n)$ time complexity for reading the input.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Checking for collinearity using cross products.
- Problem-solving patterns: Using a reference point and comparing slopes or cross products to check for collinearity.
- Optimization techniques: Avoiding division by zero by using cross products instead of calculating slopes directly.
- Similar problems to practice: Other problems involving geometric calculations and comparisons.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where two points have the same x-coordinate (vertical line).
- Edge cases to watch for: Duplicate points, vertical lines, and points with the same coordinates.
- Performance pitfalls: Using unnecessary calculations or comparisons.
- Testing considerations: Test with different types of input, including vertical lines, duplicate points, and points with the same coordinates.