## Max Increase to Keep City Skyline

**Problem Link:** https://leetcode.com/problems/max-increase-to-keep-city-skyline/description

**Problem Statement:**
- Input: A 2D `grid` representing the heights of buildings in a city, where `grid[i][j]` is the height of the building at the `i-th` row and `j-th` column.
- Output: The maximum total sum of the heights of the buildings that can be achieved without changing the city's skyline.
- Key requirements:
  - The city's skyline is defined as the row and column maximum heights.
  - The height of each building can be increased by any amount.
- Example test cases:
  - `grid = [[1,0,0],[0,0,1]]` should return `3`.
  - `grid = [[0,0,0],[0,0,0]]` should return `0`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each cell in the grid and calculate the maximum possible height increase for each cell without changing the skyline.
- Step-by-step breakdown of the solution:
  1. Initialize variables to store the row and column maximum heights.
  2. Iterate over each cell in the grid to find the row and column maximum heights.
  3. For each cell, calculate the maximum possible height increase without changing the skyline.
  4. Calculate the total sum of the heights of the buildings with the maximum possible increases.
- Why this approach comes to mind first: It is the most straightforward way to solve the problem, but it may not be the most efficient.

```cpp
int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
    int n = grid.size();
    int m = grid[0].size();
    
    // Initialize variables to store the row and column maximum heights
    vector<int> rowMax(n, 0);
    vector<int> colMax(m, 0);
    
    // Find the row and column maximum heights
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            rowMax[i] = max(rowMax[i], grid[i][j]);
            colMax[j] = max(colMax[j], grid[i][j]);
        }
    }
    
    int totalSum = 0;
    
    // Calculate the total sum of the heights of the buildings with the maximum possible increases
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            totalSum += min(rowMax[i], colMax[j]) - grid[i][j];
        }
    }
    
    return totalSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of rows and $m$ is the number of columns in the grid. This is because we iterate over each cell in the grid twice.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of rows and $m$ is the number of columns in the grid. This is because we store the row and column maximum heights in separate vectors.
> - **Why these complexities occur:** These complexities occur because we need to iterate over each cell in the grid to find the row and column maximum heights, and we need to store the row and column maximum heights in separate vectors.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can calculate the maximum possible height increase for each cell without changing the skyline by finding the minimum of the row and column maximum heights.
- Detailed breakdown of the approach:
  1. Initialize variables to store the row and column maximum heights.
  2. Iterate over each cell in the grid to find the row and column maximum heights.
  3. For each cell, calculate the maximum possible height increase without changing the skyline by finding the minimum of the row and column maximum heights.
  4. Calculate the total sum of the heights of the buildings with the maximum possible increases.
- Proof of optimality: This approach is optimal because we are calculating the maximum possible height increase for each cell without changing the skyline, and we are doing so in a way that minimizes the number of iterations over the grid.

```cpp
int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
    int n = grid.size();
    int m = grid[0].size();
    
    // Initialize variables to store the row and column maximum heights
    vector<int> rowMax(n, 0);
    vector<int> colMax(m, 0);
    
    // Find the row and column maximum heights
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            rowMax[i] = max(rowMax[i], grid[i][j]);
            colMax[j] = max(colMax[j], grid[i][j]);
        }
    }
    
    int totalSum = 0;
    
    // Calculate the total sum of the heights of the buildings with the maximum possible increases
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            totalSum += min(rowMax[i], colMax[j]) - grid[i][j];
        }
    }
    
    return totalSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of rows and $m$ is the number of columns in the grid. This is because we iterate over each cell in the grid twice.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of rows and $m$ is the number of columns in the grid. This is because we store the row and column maximum heights in separate vectors.
> - **Optimality proof:** This approach is optimal because we are calculating the maximum possible height increase for each cell without changing the skyline, and we are doing so in a way that minimizes the number of iterations over the grid.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration over a grid, finding maximum heights, and calculating the total sum of height increases.
- Problem-solving patterns identified: Finding the row and column maximum heights, and calculating the maximum possible height increase for each cell without changing the skyline.
- Optimization techniques learned: Minimizing the number of iterations over the grid by calculating the row and column maximum heights in a single pass.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing variables to store the row and column maximum heights, or not calculating the maximum possible height increase for each cell correctly.
- Edge cases to watch for: Grids with zero rows or columns, or grids with all zeros.
- Performance pitfalls: Iterating over the grid more than twice, or not using the minimum of the row and column maximum heights to calculate the maximum possible height increase for each cell.