## Maximum Number of Points from Grid Queries
**Problem Link:** https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/description

**Problem Statement:**
- Input format: A 2D array `points` of size `m x n` where each element is an integer, and a 2D array `queries` of size `q x 2` where each query is in the format `[x, y]`.
- Constraints: `1 <= m, n <= 1000`, `1 <= q <= 1000`, `1 <= x <= m`, `1 <= y <= n`.
- Expected output format: An array of integers, where each integer represents the maximum number of points that can be obtained from the grid for each query.
- Key requirements and edge cases to consider: The maximum number of points that can be obtained from the grid is the sum of all points in the grid that are less than or equal to the query point.
- Example test cases with explanations: 
    - Example 1: `points = [[1,2,3],[4,5,6],[7,8,9]]`, `queries = [[1,1],[2,2],[3,3]]`. The maximum number of points for each query is the sum of all points in the grid that are less than or equal to the query point.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each query, iterate over the entire grid and sum up all points that are less than or equal to the query point.
- Step-by-step breakdown of the solution:
    1. Iterate over each query.
    2. For each query, iterate over the entire grid.
    3. For each point in the grid, check if it is less than or equal to the query point.
    4. If it is, add the point to the sum.
    5. Return the sum as the maximum number of points for the query.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it has a high time complexity.

```cpp
vector<int> maxPoints(vector<vector<int>>& points, vector<vector<int>>& queries) {
    vector<int> result;
    for (auto& query : queries) {
        int sum = 0;
        for (int i = 0; i < points.size(); i++) {
            for (int j = 0; j < points[i].size(); j++) {
                if (points[i][j] <= query[0] * query[1]) {
                    sum += points[i][j];
                }
            }
        }
        result.push_back(sum);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(q \cdot m \cdot n)$, where $q$ is the number of queries, $m$ is the number of rows in the grid, and $n$ is the number of columns in the grid. This is because for each query, we iterate over the entire grid.
> - **Space Complexity:** $O(1)$, excluding the space required for the output. This is because we only use a constant amount of space to store the sum and the current query.
> - **Why these complexities occur:** The time complexity is high because we iterate over the entire grid for each query. The space complexity is low because we only use a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a prefix sum array to store the cumulative sum of the points in the grid. This allows us to calculate the sum of all points that are less than or equal to a query point in $O(1)$ time.
- Detailed breakdown of the approach:
    1. Create a prefix sum array `prefix` of the same size as the grid.
    2. Iterate over the grid and calculate the cumulative sum at each point.
    3. For each query, calculate the sum of all points that are less than or equal to the query point using the prefix sum array.
- Proof of optimality: This approach is optimal because it reduces the time complexity from $O(q \cdot m \cdot n)$ to $O(q + m \cdot n)$.

```cpp
vector<int> maxPoints(vector<vector<int>>& points, vector<vector<int>>& queries) {
    int m = points.size();
    int n = points[0].size();
    vector<vector<int>> prefix(m + 1, vector<int>(n + 1, 0));
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + points[i - 1][j - 1];
        }
    }
    vector<int> result;
    for (auto& query : queries) {
        int sum = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (points[i][j] <= query[0] * query[1]) {
                    sum += points[i][j];
                }
            }
        }
        result.push_back(sum);
    }
    return result;
}
```
However, the optimal solution provided above is still not optimal as we are still iterating over the grid for each query. 

We can further optimize it by using a binary search to find the points that are less than or equal to the query point.

```cpp
vector<int> maxPoints(vector<vector<int>>& points, vector<vector<int>>& queries) {
    int m = points.size();
    int n = points[0].size();
    vector<int> flat_points;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            flat_points.push_back(points[i][j]);
        }
    }
    sort(flat_points.begin(), flat_points.end());
    vector<int> result;
    for (auto& query : queries) {
        int target = query[0] * query[1];
        int idx = upper_bound(flat_points.begin(), flat_points.end(), target) - flat_points.begin();
        int sum = 0;
        for (int i = 0; i < idx; i++) {
            sum += flat_points[i];
        }
        result.push_back(sum);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(q \cdot log(m \cdot n) + m \cdot n \cdot log(m \cdot n))$, where $q$ is the number of queries, $m$ is the number of rows in the grid, and $n$ is the number of columns in the grid. This is because we first sort the flat points array, and then for each query, we use binary search to find the points that are less than or equal to the query point.
> - **Space Complexity:** $O(m \cdot n)$, excluding the space required for the output. This is because we create a flat points array to store all points in the grid.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity from $O(q \cdot m \cdot n)$ to $O(q \cdot log(m \cdot n) + m \cdot n \cdot log(m \cdot n))$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search, prefix sum array, sorting.
- Problem-solving patterns identified: Using a prefix sum array to reduce the time complexity, using binary search to find the points that are less than or equal to the query point.
- Optimization techniques learned: Reducing the time complexity by using a prefix sum array and binary search.
- Similar problems to practice: Problems that involve finding the sum of all points that are less than or equal to a query point, such as finding the sum of all points in a grid that are less than or equal to a query point.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the prefix sum array correctly, not using binary search correctly.
- Edge cases to watch for: When the query point is less than or equal to all points in the grid, when the query point is greater than all points in the grid.
- Performance pitfalls: Not using a prefix sum array, not using binary search.
- Testing considerations: Test the solution with different inputs, such as a grid with all points being the same, a grid with all points being different.