## Max Value of Equation

**Problem Link:** https://leetcode.com/problems/max-value-of-equation/description

**Problem Statement:**
- Input format: `points` - a list of pairs of integers representing points in a 2D plane, where each point is in the format `[x, y]`.
- Constraints: `1 <= points.length <= 10^5`, `points[i].length == 2`, `-10^5 <= points[i][0] <= 10^5`, `-10^5 <= points[i][1] <= 10^5`.
- Expected output format: The maximum value of the equation `y = mx + b` for any point in `points`.
- Key requirements: Find the maximum value of the equation for any point in `points` given the constraints on `x` and `y`.
- Edge cases: Empty input list, single element list, and lists with duplicate points.
- Example test cases:
  - `points = [[1,3],[-2,2]]`, `k = 5` should return `11`.
  - `points = [[0,0],[3,3]]`, `k = 1` should return `4`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to calculate the value of the equation for each point in `points` and for each possible slope `m` and intercept `b`.
- We then need to find the maximum value of the equation among all points and all possible `m` and `b`.
- This approach comes to mind first because it involves checking every possible combination of points and slopes.

```cpp
int findMaxValueOfEquation(vector<vector<int>>& points, int k) {
    int maxValue = INT_MIN;
    for (int i = 0; i < points.size(); i++) {
        for (int j = i + 1; j < points.size(); j++) {
            int slope = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0]);
            if (abs(slope) <= k) {
                int intercept = points[i][1] - slope * points[i][0];
                for (int l = 0; l < points.size(); l++) {
                    int value = slope * points[l][0] + intercept;
                    maxValue = max(maxValue, value);
                }
            }
        }
    }
    return maxValue;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of points. This is because we have three nested loops.
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with the input size.
> - **Why these complexities occur:** The brute force approach involves checking every possible combination of points and slopes, resulting in a cubic time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a `multiset` to store the values of `y - x` for each point.
- We then iterate over each point and for each point, we find the maximum value of `y + x` in the `multiset` that is within the range of `k`.
- This approach is optimal because it reduces the time complexity to $O(n^2 \log n)$.

```cpp
int findMaxValueOfEquation(vector<vector<int>>& points, int k) {
    multiset<int> values;
    int maxValue = INT_MIN;
    for (auto& point : points) {
        for (auto& other : points) {
            if (abs(point[0] - other[0]) <= k) {
                int value = other[1] + other[0];
                values.insert(value);
                auto it = values.upper_bound(value + k);
                if (it != values.end()) {
                    maxValue = max(maxValue, *it);
                }
            }
        }
        values.clear();
    }
    return maxValue;
}
```

However, the optimal approach can still be optimized by using a single loop and maintaining a `multiset` of lines in the form of `y = mx + b` and then finding the maximum value for each point.

```cpp
int findMaxValueOfEquation(vector<vector<int>>& points, int k) {
    multiset<pair<int, int>> lines;
    int maxValue = INT_MIN;
    for (auto& point : points) {
        while (!lines.empty() && point[0] - lines.begin()->first > k) {
            lines.erase(lines.begin());
        }
        if (!lines.empty()) {
            maxValue = max(maxValue, point[1] + lines.begin()->second);
        }
        for (auto& other : points) {
            if (other[0] != point[0]) {
                int m = (other[1] - point[1]) / (other[0] - point[0]);
                int b = point[1] - m * point[0];
                lines.insert({other[0], b});
            }
        }
    }
    return maxValue;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \log n)$, where $n$ is the number of points. This is because we have two nested loops and a `multiset` operation.
> - **Space Complexity:** $O(n)$, as we are using a `multiset` to store the lines.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity to $O(n^2 \log n)$, which is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- The importance of using the right data structure (e.g., `multiset`) to optimize the solution.
- How to reduce the time complexity by using a single loop and maintaining a `multiset` of lines.
- The importance of handling edge cases and boundary conditions.

**Mistakes to Avoid:**
- Not considering the edge cases and boundary conditions.
- Not using the right data structure to optimize the solution.
- Not reducing the time complexity by using a single loop and maintaining a `multiset` of lines.