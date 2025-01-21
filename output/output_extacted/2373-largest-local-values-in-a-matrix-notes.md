## Largest Local Values in a Matrix

**Problem Link:** https://leetcode.com/problems/largest-local-values-in-a-matrix/description

**Problem Statement:**
- Input: A `3x3` sub-matrix within a larger matrix `grid`.
- Constraints: The grid is a square matrix of size `n x n`, where `n` is odd.
- Expected Output: A matrix of size `(n-2) x (n-2)` containing the largest local values.
- Key Requirements:
  - For each cell in the grid, find the maximum value in its `3x3` neighborhood.
  - The `3x3` neighborhood of a cell includes the cell itself and its eight surrounding cells.
- Edge Cases:
  - The grid has a size of `1x1` or is empty.
- Example Test Cases:
  - Input: `grid = [[1,1,1,1,1],[1,9,9,9,1],[1,9,3,9,1],[1,9,9,9,1],[1,1,1,1,1]]`
    - Expected Output: `[[9,9],[9,9]]`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate over each cell in the grid and find the maximum value in its `3x3` neighborhood.
- This approach involves checking each cell's neighbors and keeping track of the maximum value found.
- The brute force approach comes to mind first because it directly addresses the problem statement without considering any optimizations.

```cpp
vector<vector<int>> largestLocal(vector<vector<int>>& grid) {
    int n = grid.size();
    vector<vector<int>> result(n - 2, vector<int>(n - 2));
    
    for (int i = 1; i < n - 1; i++) {
        for (int j = 1; j < n - 1; j++) {
            int maxVal = 0;
            for (int x = -1; x <= 1; x++) {
                for (int y = -1; y <= 1; y++) {
                    maxVal = max(maxVal, grid[i + x][j + y]);
                }
            }
            result[i - 1][j - 1] = maxVal;
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where `n` is the size of the grid. This is because we iterate over each cell in the grid once.
> - **Space Complexity:** $O(n^2)$, as we need to store the result in a matrix of size `(n-2) x (n-2)`.
> - **Why these complexities occur:** The time complexity is $O(n^2)$ because we have two nested loops that iterate over the grid. The space complexity is also $O(n^2)$ because we need to store the result in a matrix of size `(n-2) x (n-2)`.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to realize that the brute force approach is already optimal in terms of time complexity.
- The detailed breakdown of the approach remains the same as the brute force approach.
- Proof of optimality: We must check each cell's `3x3` neighborhood to find the maximum value, which requires at least $O(n^2)$ time.
- Why further optimization is impossible: We cannot reduce the time complexity below $O(n^2)$ because we must examine each cell in the grid.

```cpp
vector<vector<int>> largestLocal(vector<vector<int>>& grid) {
    int n = grid.size();
    vector<vector<int>> result(n - 2, vector<int>(n - 2));
    
    for (int i = 1; i < n - 1; i++) {
        for (int j = 1; j < n - 1; j++) {
            int maxVal = 0;
            for (int x = -1; x <= 1; x++) {
                for (int y = -1; y <= 1; y++) {
                    maxVal = max(maxVal, grid[i + x][j + y]);
                }
            }
            result[i - 1][j - 1] = maxVal;
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where `n` is the size of the grid.
> - **Space Complexity:** $O(n^2)$, as we need to store the result in a matrix of size `(n-2) x (n-2)`.
> - **Optimality proof:** The time complexity is optimal because we must examine each cell in the grid to find the maximum value in its `3x3` neighborhood.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: iteration, maximum finding, and matrix manipulation.
- Problem-solving patterns identified: brute force approach and optimal solution.
- Optimization techniques learned: none, as the brute force approach is already optimal.
- Similar problems to practice: matrix operations, maximum finding, and iteration.

**Mistakes to Avoid:**
- Common implementation errors: out-of-bounds access, incorrect indexing, and failure to initialize variables.
- Edge cases to watch for: empty grid, grid with size `1x1`, and grid with non-odd size.
- Performance pitfalls: using inefficient algorithms or data structures.
- Testing considerations: test the function with different grid sizes, including edge cases.