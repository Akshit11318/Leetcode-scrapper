## Island Perimeter

**Problem Link:** https://leetcode.com/problems/island-perimeter/description

**Problem Statement:**
- Input: A 2D array of integers `grid` where `0` represents water and `1` represents land.
- Constraints: The input grid is rectangular and has at least one row and one column. The grid only contains `0`s and `1`s.
- Expected Output: The perimeter of the island in the grid.
- Key Requirements: The perimeter is calculated by counting the number of edges of land cells that are adjacent to water cells or the boundary of the grid.
- Edge Cases: An empty grid, a grid with no island, or a grid with multiple islands.

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each cell in the grid. For each land cell, check all four directions (up, down, left, right) to see if it's adjacent to a water cell or the boundary. If so, increment the perimeter counter.
- Step-by-step breakdown:
  1. Initialize a perimeter counter to `0`.
  2. Iterate over each cell in the grid.
  3. For each land cell, check the four directions.
  4. If a direction is out of bounds or is a water cell, increment the perimeter counter.

```cpp
int islandPerimeter(vector<vector<int>>& grid) {
    int perimeter = 0;
    int rows = grid.size();
    int cols = grid[0].size();
    
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            if (grid[i][j] == 1) {
                // Check up
                if (i == 0 || grid[i-1][j] == 0) perimeter++;
                // Check down
                if (i == rows - 1 || grid[i+1][j] == 0) perimeter++;
                // Check left
                if (j == 0 || grid[i][j-1] == 0) perimeter++;
                // Check right
                if (j == cols - 1 || grid[i][j+1] == 0) perimeter++;
            }
        }
    }
    return perimeter;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns in the grid. This is because we are iterating over each cell in the grid once.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input grid. This is because we are using a constant amount of space to store the perimeter counter and other variables.
> - **Why these complexities occur:** The time complexity is linear with respect to the size of the input grid because we are performing a constant amount of work for each cell. The space complexity is constant because we are not using any data structures that scale with the size of the input.

### Optimal Approach (Required)

The brute force approach is already optimal for this problem because we must check every cell in the grid to calculate the perimeter. However, the same code provided in the brute force approach is also the optimal approach.

```cpp
int islandPerimeter(vector<vector<int>>& grid) {
    int perimeter = 0;
    int rows = grid.size();
    int cols = grid[0].size();
    
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            if (grid[i][j] == 1) {
                // Check up
                if (i == 0 || grid[i-1][j] == 0) perimeter++;
                // Check down
                if (i == rows - 1 || grid[i+1][j] == 0) perimeter++;
                // Check left
                if (j == 0 || grid[i][j-1] == 0) perimeter++;
                // Check right
                if (j == cols - 1 || grid[i][j+1] == 0) perimeter++;
            }
        }
    }
    return perimeter;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns in the grid.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input grid.
> - **Optimality proof:** This is the best possible time complexity because we must check every cell in the grid to calculate the perimeter.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration over a 2D grid, checking boundary conditions.
- Problem-solving patterns identified: Checking all four directions for each cell.
- Optimization techniques learned: None, because the brute force approach is already optimal.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to check boundary conditions, incrementing the perimeter counter incorrectly.
- Edge cases to watch for: Empty grid, grid with no island, grid with multiple islands.
- Performance pitfalls: Using a data structure that scales with the size of the input grid unnecessarily.
- Testing considerations: Test with different grid sizes, different island shapes, and different boundary conditions.