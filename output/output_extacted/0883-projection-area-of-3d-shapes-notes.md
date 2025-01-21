## Projection Area of 3D Shapes
**Problem Link:** https://leetcode.com/problems/projection-area-of-3d-shapes/description

**Problem Statement:**
- Input format: A 2D array `grid` representing the shape, where `grid[i][j]` is either 0 or 1.
- Constraints: The grid will have a size of `m x n` where `1 <= m, n <= 50`.
- Expected output format: The total projection area of the shape.
- Key requirements and edge cases to consider: The grid can contain only 0s and 1s, and the shape can have varying sizes and orientations.
- Example test cases with explanations:
    - `[[1,0],[0,1]]` returns 8 because the shape has a projection area of 8 when projected onto the x-y, y-z, and x-z planes.
    - `[[1,1,1],[1,1,1],[1,1,1]]` returns 21 because the shape has a projection area of 21 when projected onto the x-y, y-z, and x-z planes.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To calculate the projection area, we need to consider the projections onto the x-y, y-z, and x-z planes.
- Step-by-step breakdown of the solution:
    1. Initialize variables to store the projection areas for each plane.
    2. Iterate over the grid to calculate the projection area for the x-y plane by counting the number of 1s in each row.
    3. Iterate over the grid to calculate the projection area for the y-z plane by counting the number of 1s in each column.
    4. Iterate over the grid to calculate the projection area for the x-z plane by counting the number of 1s in each cell and adding 1 for each cell that has a value of 1.
- Why this approach comes to mind first: It is a straightforward approach that directly calculates the projection areas for each plane.

```cpp
int projectionArea(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    int xy = 0, yz = 0, xz = 0;
    
    // Calculate the projection area for the x-y plane
    for (int i = 0; i < m; i++) {
        int rowMax = 0;
        for (int j = 0; j < n; j++) {
            rowMax = max(rowMax, grid[i][j]);
        }
        xy += rowMax;
    }
    
    // Calculate the projection area for the y-z plane
    for (int j = 0; j < n; j++) {
        int colMax = 0;
        for (int i = 0; i < m; i++) {
            colMax = max(colMax, grid[i][j]);
        }
        yz += colMax;
    }
    
    // Calculate the projection area for the x-z plane
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] > 0) {
                xz++;
            }
        }
    }
    
    return xy + yz + xz;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$ where $m$ and $n$ are the dimensions of the grid, because we iterate over the grid three times to calculate the projection areas for each plane.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store the projection areas.
> - **Why these complexities occur:** The time complexity occurs because we need to iterate over the grid to calculate the projection areas, and the space complexity occurs because we only need a constant amount of space to store the results.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can calculate the projection areas for all three planes in a single pass over the grid.
- Detailed breakdown of the approach:
    1. Initialize variables to store the projection areas for each plane.
    2. Iterate over the grid to calculate the projection areas for all three planes in a single pass.
- Proof of optimality: This approach is optimal because we only need to iterate over the grid once to calculate the projection areas for all three planes.

```cpp
int projectionArea(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    int xy = 0, yz = 0, xz = 0;
    
    // Calculate the projection areas for all three planes in a single pass
    for (int i = 0; i < m; i++) {
        int rowMax = 0, colMax = 0;
        for (int j = 0; j < n; j++) {
            rowMax = max(rowMax, grid[i][j]);
            if (i == 0) {
                colMax = grid[i][j];
            } else {
                colMax = max(colMax, grid[i][j]);
            }
            if (grid[i][j] > 0) {
                xz++;
            }
        }
        xy += rowMax;
        if (i == m - 1) {
            for (int j = 0; j < n; j++) {
                yz += colMax;
                colMax = 0;
                for (int k = 0; k < m; k++) {
                    colMax = max(colMax, grid[k][j]);
                }
            }
        }
    }
    yz = yz / m;
    return xy + yz + xz;
}
```
However the optimal solution can be simplified even further as below:
```cpp
int projectionArea(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    int xy = 0, yz = 0, xz = 0;
    
    vector<int> rowMax(m, 0), colMax(n, 0);
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            rowMax[i] = max(rowMax[i], grid[i][j]);
            colMax[j] = max(colMax[j], grid[i][j]);
            if (grid[i][j] > 0) {
                xz++;
            }
        }
    }
    
    for (int i = 0; i < m; i++) {
        xy += rowMax[i];
    }
    
    for (int j = 0; j < n; j++) {
        yz += colMax[j];
    }
    
    return xy + yz + xz;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$ where $m$ and $n$ are the dimensions of the grid, because we iterate over the grid once to calculate the projection areas for all three planes.
> - **Space Complexity:** $O(m + n)$ because we use additional space to store the row and column maxima.
> - **Optimality proof:** This approach is optimal because we only need to iterate over the grid once to calculate the projection areas for all three planes.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration over a 2D grid, calculation of row and column maxima.
- Problem-solving patterns identified: Using a single pass over the grid to calculate multiple quantities.
- Optimization techniques learned: Reducing the number of iterations over the grid.
- Similar problems to practice: Other problems involving iteration over a grid and calculation of quantities.

**Mistakes to Avoid:**
- Common implementation errors: Failing to initialize variables, incorrect indexing.
- Edge cases to watch for: Grids with zero rows or columns, grids with all zeros.
- Performance pitfalls: Using unnecessary iterations or recursive calls.
- Testing considerations: Test cases with different grid sizes and values.