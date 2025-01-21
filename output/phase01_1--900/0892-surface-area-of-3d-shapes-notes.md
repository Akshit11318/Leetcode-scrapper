## Surface Area of 3D Shapes
**Problem Link:** https://leetcode.com/problems/surface-area-of-3d-shapes/description

**Problem Statement:**
- Input format and constraints: The input is a 2D array `grid` where each cell represents a 3D cube with a height of 1. The constraints are that the grid size is in the range [1, 50] and each cell's value is in the range [0, 4].
- Expected output format: The function should return the total surface area of the 3D shape.
- Key requirements and edge cases to consider: The surface area of a cube is 6 times the area of one of its faces. When two cubes share a face, the shared face is not part of the surface area.
- Example test cases with explanations:
  - `[[1]]` returns `6` because there is only one cube with a surface area of 6.
  - `[[1,2],[3,4]]` returns `34` because there are four cubes, each with a surface area of 6, minus the areas of the shared faces.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To calculate the surface area of the 3D shape, we need to calculate the surface area of each cube and subtract the areas of the shared faces.
- Step-by-step breakdown of the solution:
  1. Iterate over each cell in the grid.
  2. For each cell, calculate the surface area of the cube.
  3. Check the neighboring cells (up, down, left, right) and subtract the areas of the shared faces.
- Why this approach comes to mind first: It is a straightforward approach that involves iterating over each cell and calculating the surface area.

```cpp
int surfaceArea(vector<vector<int>>& grid) {
    int n = grid.size();
    int m = grid[0].size();
    int area = 0;
    
    // Calculate the surface area of each cube
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] > 0) {
                area += 6 * grid[i][j];
            }
        }
    }
    
    // Subtract the areas of the shared faces
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (i > 0 && grid[i][j] > 0 && grid[i-1][j] > 0) {
                area -= 2 * min(grid[i][j], grid[i-1][j]);
            }
            if (j > 0 && grid[i][j] > 0 && grid[i][j-1] > 0) {
                area -= 2 * min(grid[i][j], grid[i][j-1]);
            }
        }
    }
    
    return area;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ and $m$ are the dimensions of the grid.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space.
> - **Why these complexities occur:** The time complexity is linear because we iterate over each cell in the grid twice. The space complexity is constant because we only use a few variables to store the surface area.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can calculate the surface area in one pass by checking the neighboring cells and subtracting the areas of the shared faces.
- Detailed breakdown of the approach:
  1. Iterate over each cell in the grid.
  2. For each cell, calculate the surface area of the cube.
  3. Check the neighboring cells (up, down, left, right) and subtract the areas of the shared faces.
- Proof of optimality: This approach is optimal because it only requires one pass over the grid.
- Why further optimization is impossible: This approach is already linear in the size of the input, so further optimization is not possible.

```cpp
int surfaceArea(vector<vector<int>>& grid) {
    int n = grid.size();
    int m = grid[0].size();
    int area = 0;
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] > 0) {
                area += 2 + 4 * grid[i][j];
                if (i > 0) area -= min(grid[i][j], grid[i-1][j]);
                if (j > 0) area -= min(grid[i][j], grid[i][j-1]);
            }
        }
    }
    
    return area;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ and $m$ are the dimensions of the grid.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space.
> - **Optimality proof:** This approach is optimal because it only requires one pass over the grid.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional statements, and optimization.
- Problem-solving patterns identified: Checking neighboring cells and subtracting shared areas.
- Optimization techniques learned: Reducing the number of passes over the grid.
- Similar problems to practice: Other problems involving grids and optimization.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect indexing, forgetting to check neighboring cells.
- Edge cases to watch for: Empty grid, grid with only one cell.
- Performance pitfalls: Using unnecessary loops or conditional statements.
- Testing considerations: Test with different grid sizes and values to ensure correctness.