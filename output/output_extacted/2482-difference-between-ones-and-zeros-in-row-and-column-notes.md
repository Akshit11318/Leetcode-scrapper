## Difference Between Ones and Zeros in Row and Column

**Problem Link:** https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/description

**Problem Statement:**
- Input: A 2D array `grid` of size `m x n` containing only `0`s and `1`s.
- Constraints: `1 <= m <= 200`, `1 <= n <= 200`.
- Expected output: A 2D array of the same size as `grid`, where each cell at position `(i, j)` contains the absolute difference between the number of `1`s and `0`s in the `i-th` row and the `j-th` column.
- Key requirements: Iterate over each cell in the grid, calculate the difference between `1`s and `0`s for the corresponding row and column, and store this difference in the output grid.
- Example test cases:
  - For `grid = [[0,1,0],[1,0,1],[0,1,0]]`, the output should be `[[0,1,2],[0,1,2],[0,1,2]]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each cell in the grid, count the number of `1`s and `0`s in the corresponding row and column, then calculate the absolute difference.
- Step-by-step breakdown:
  1. Initialize an output grid with the same dimensions as the input grid.
  2. Iterate over each cell in the input grid.
  3. For each cell, iterate over the corresponding row and column to count `1`s and `0`s.
  4. Calculate the absolute difference between the counts of `1`s and `0`s for both the row and the column.
  5. Store these differences in the output grid.

```cpp
vector<vector<int>> onesMinusZeros(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    vector<vector<int>> output(m, vector<int>(n));
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            int rowOnes = 0, rowZeros = 0, colOnes = 0, colZeros = 0;
            
            // Count ones and zeros in the row
            for (int k = 0; k < n; k++) {
                if (grid[i][k] == 1) rowOnes++;
                else rowZeros++;
            }
            
            // Count ones and zeros in the column
            for (int k = 0; k < m; k++) {
                if (grid[k][j] == 1) colOnes++;
                else colZeros++;
            }
            
            // Calculate and store the differences
            output[i][j] = rowOnes - rowZeros + colOnes - colZeros;
        }
    }
    
    return output;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m^2 * n + m * n^2)$, where $m$ is the number of rows and $n$ is the number of columns. This is because for each cell, we potentially scan the entire row and column.
> - **Space Complexity:** $O(m * n)$, for the output grid.
> - **Why these complexities occur:** The brute force approach involves nested loops for counting `1`s and `0`s in rows and columns for each cell, leading to high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of counting `1`s and `0`s for each row and column on the fly for every cell, we can pre-calculate these counts once and store them. This way, we avoid redundant calculations and significantly reduce the time complexity.
- Detailed breakdown:
  1. Initialize arrays to store the counts of `1`s and `0`s for each row and column.
  2. Pre-calculate these counts by iterating over the grid once.
  3. Then, iterate over the grid again to calculate the differences for each cell using the pre-calculated counts.

```cpp
vector<vector<int>> onesMinusZeros(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    vector<vector<int>> output(m, vector<int>(n));
    vector<int> rowOnes(m), rowZeros(m), colOnes(n), colZeros(n);
    
    // Pre-calculate counts of ones and zeros
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 1) {
                rowOnes[i]++;
                colOnes[j]++;
            } else {
                rowZeros[i]++;
                colZeros[j]++;
            }
        }
    }
    
    // Calculate and store the differences using pre-calculated counts
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            output[i][j] = rowOnes[i] - rowZeros[i] + colOnes[j] - colZeros[j];
        }
    }
    
    return output;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m * n)$, where $m$ is the number of rows and $n$ is the number of columns. This is because we make two passes over the grid: one to pre-calculate counts and another to calculate differences.
> - **Space Complexity:** $O(m + n)$, for the arrays storing row and column counts.
> - **Optimality proof:** This approach is optimal because it minimizes redundant calculations by pre-calculating necessary information, reducing the time complexity to linear with respect to the total number of cells in the grid.

---

### Final Notes

**Learning Points:**
- The importance of pre-calculating and storing intermediate results to avoid redundant calculations.
- How to analyze time and space complexity to identify bottlenecks and areas for optimization.
- The value of breaking down complex problems into simpler, more manageable steps.

**Mistakes to Avoid:**
- Failing to consider the impact of nested loops on time complexity.
- Not recognizing opportunities for pre-calculation to reduce redundant work.
- Overlooking the importance of clear, concise variable names and comments for readability and maintainability.