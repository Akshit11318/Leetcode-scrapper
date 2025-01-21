## Grid Game

**Problem Link:** https://leetcode.com/problems/grid-game/description

**Problem Statement:**
- Input format and constraints: Given a 2D grid of size `m x n` containing integers, where each integer represents the value of the cell at that position. The grid is divided into two parts by a `0`-indexed column `k`. The goal is to find the maximum value that can be achieved by selecting a cell from the left part of the grid (cells to the left of column `k`) and a cell from the right part of the grid (cells to the right of column `k`), such that the sum of the values of these two cells is maximized.
- Expected output format: The maximum sum of values of two cells, one from the left part and one from the right part of the grid.
- Key requirements and edge cases to consider: 
  - The grid can contain negative values.
  - The grid can contain zeros.
  - The column `k` is `0`-indexed.
- Example test cases with explanations:
  - Example 1: `grid = [[2,5,4],[1,5,1],[4,5,2]]`, `k = 2`. The maximum sum is `7`, achieved by selecting the cell at position `(0,1)` from the left part and the cell at position `(2,2)` from the right part.

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over all cells in the left part of the grid and for each cell, iterating over all cells in the right part of the grid to find the maximum sum.
- Step-by-step breakdown of the solution:
  1. Initialize the maximum sum to negative infinity.
  2. Iterate over all cells in the left part of the grid.
  3. For each cell in the left part, iterate over all cells in the right part of the grid.
  4. For each pair of cells, calculate the sum of their values.
  5. Update the maximum sum if the current sum is greater.
- Why this approach comes to mind first: This approach is straightforward and ensures that all possible pairs of cells are considered.

```cpp
int maxSum(vector<vector<int>>& grid, int k) {
    int m = grid.size();
    int n = grid[0].size();
    int max_sum = INT_MIN;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < k; j++) {
            for (int p = 0; p < m; p++) {
                for (int q = k; q < n; q++) {
                    max_sum = max(max_sum, grid[i][j] + grid[p][q]);
                }
            }
        }
    }
    return max_sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m^2 \cdot n^2)$, where $m$ is the number of rows and $n$ is the number of columns in the grid. This is because for each cell in the left part, we iterate over all cells in the right part.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum sum.
> - **Why these complexities occur:** The time complexity occurs because we have four nested loops, each iterating over a dimension of the grid. The space complexity is constant because we only use a single variable to store the maximum sum.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can calculate the prefix sum for the left and right parts of the grid separately. Then, for each column in the left part, we find the maximum value in the right part that can be added to the current cell in the left part.
- Detailed breakdown of the approach:
  1. Calculate the prefix sum for the left part of the grid.
  2. Calculate the prefix sum for the right part of the grid.
  3. Initialize the maximum sum to negative infinity.
  4. Iterate over all cells in the left part of the grid.
  5. For each cell in the left part, find the maximum value in the right part that can be added to the current cell.
  6. Update the maximum sum if the current sum is greater.
- Proof of optimality: This approach is optimal because it considers all possible pairs of cells in the left and right parts of the grid, and it does so in a way that minimizes the number of operations required.

```cpp
int maxSum(vector<vector<int>>& grid, int k) {
    int m = grid.size();
    int n = grid[0].size();
    vector<int> left(m), right(m);
    for (int j = 0; j < k; j++) {
        for (int i = 0; i < m; i++) {
            left[i] += grid[i][j];
        }
    }
    for (int j = k; j < n; j++) {
        for (int i = 0; i < m; i++) {
            right[i] += grid[i][j];
        }
    }
    int max_sum = INT_MIN;
    for (int i = 0; i < m; i++) {
        max_sum = max(max_sum, left[i] + *max_element(right.begin(), right.end()));
    }
    return max_sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns in the grid. This is because we iterate over the grid twice to calculate the prefix sums, and then once to find the maximum sum.
> - **Space Complexity:** $O(m)$, as we use two arrays to store the prefix sums for the left and right parts of the grid.
> - **Optimality proof:** This approach is optimal because it has a time complexity of $O(m \cdot n)$, which is the minimum required to iterate over the grid and find the maximum sum.