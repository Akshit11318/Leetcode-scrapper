## Number of Black Blocks
**Problem Link:** https://leetcode.com/problems/number-of-black-blocks/description

**Problem Statement:**
- Input format and constraints: You are given a 2D grid `grid` where each cell is either a black block (`'B'`) or a white block (`'W'`). The grid has `m` rows and `n` columns.
- Expected output format: Return the number of black blocks in the grid.
- Key requirements and edge cases to consider: 
  - The grid may contain only black blocks or only white blocks.
  - The grid may be empty.
  - The grid may have a single row or column.
- Example test cases with explanations:
  - `grid = [['B', 'W'], ['B', 'B']]`: The expected output is `3` because there are `3` black blocks in the grid.
  - `grid = [['W', 'W'], ['W', 'W']]`: The expected output is `0` because there are no black blocks in the grid.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can iterate through each cell in the grid and count the number of black blocks.
- Step-by-step breakdown of the solution: 
  1. Initialize a variable `count` to `0`.
  2. Iterate through each cell in the grid.
  3. If a cell is a black block (`'B'`), increment `count`.
  4. Return `count` after iterating through all cells.
- Why this approach comes to mind first: It is a straightforward and intuitive approach to count the number of black blocks in the grid.

```cpp
int countBlackBlocks(vector<vector<char>>& grid) {
    int count = 0;
    for (int i = 0; i < grid.size(); i++) {
        for (int j = 0; j < grid[0].size(); j++) {
            if (grid[i][j] == 'B') {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \times n)$, where $m$ is the number of rows and $n$ is the number of columns in the grid. This is because we iterate through each cell in the grid once.
> - **Space Complexity:** $O(1)$, which means the space complexity is constant. This is because we only use a single variable `count` to store the count of black blocks, regardless of the size of the grid.
> - **Why these complexities occur:** The time complexity occurs because we iterate through each cell in the grid, and the space complexity occurs because we only use a constant amount of space to store the count of black blocks.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is the same as the brute force approach because we must iterate through each cell in the grid to count the number of black blocks.
- Detailed breakdown of the approach: 
  1. Initialize a variable `count` to `0`.
  2. Iterate through each cell in the grid.
  3. If a cell is a black block (`'B'`), increment `count`.
  4. Return `count` after iterating through all cells.
- Proof of optimality: This approach is optimal because we must iterate through each cell in the grid to count the number of black blocks. Any other approach would require additional operations, making it less efficient.
- Why further optimization is impossible: Further optimization is impossible because we must iterate through each cell in the grid to count the number of black blocks. Any other approach would require additional operations, making it less efficient.

```cpp
int countBlackBlocks(vector<vector<char>>& grid) {
    int count = 0;
    for (int i = 0; i < grid.size(); i++) {
        for (int j = 0; j < grid[0].size(); j++) {
            if (grid[i][j] == 'B') {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \times n)$, where $m$ is the number of rows and $n$ is the number of columns in the grid. This is because we iterate through each cell in the grid once.
> - **Space Complexity:** $O(1)$, which means the space complexity is constant. This is because we only use a single variable `count` to store the count of black blocks, regardless of the size of the grid.
> - **Optimality proof:** This approach is optimal because we must iterate through each cell in the grid to count the number of black blocks. Any other approach would require additional operations, making it less efficient.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration and counting.
- Problem-solving patterns identified: The need to iterate through each cell in the grid to count the number of black blocks.
- Optimization techniques learned: None, because the optimal solution is the same as the brute force approach.
- Similar problems to practice: Counting the number of elements in a list or array that meet a certain condition.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize the `count` variable or incrementing it incorrectly.
- Edge cases to watch for: An empty grid or a grid with only white blocks.
- Performance pitfalls: Using an inefficient data structure or algorithm to count the number of black blocks.
- Testing considerations: Test the function with different grid sizes and combinations of black and white blocks.