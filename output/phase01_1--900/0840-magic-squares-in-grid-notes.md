## Magic Squares In Grid

**Problem Link:** [https://leetcode.com/problems/magic-squares-in-grid/description](https://leetcode.com/problems/magic-squares-in-grid/description)

**Problem Statement:**
- Input: A 3x3 `grid` of integers, where each integer is between 1 and 9 (inclusive).
- Expected output: The number of 3x3 `sub-grids` that are magic squares.
- Key requirements: A 3x3 grid is a magic square if the sum of each row, column, and diagonal is the same.
- Example test cases:
  - Input: `grid = [[4,3,8],[9,5,1],[2,7,6]]`
    - Output: `1`
    - Explanation: The sub-grid `[[4,3,8],[9,5,1],[2,7,6]]` is a magic square because the sum of each row, column, and diagonal is `15`.

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible 3x3 sub-grid within the given grid to see if it's a magic square.
- Step-by-step breakdown of the solution:
  1. Iterate over each cell in the grid.
  2. For each cell, check if it's possible to form a 3x3 sub-grid starting from that cell.
  3. If it's possible, calculate the sum of each row, column, and diagonal of the sub-grid.
  4. Check if the sums are equal. If they are, increment the count of magic squares.
- Why this approach comes to mind first: It's a straightforward way to ensure we check every possible sub-grid.

```cpp
int numMagicSquaresInside(vector<vector<int>>& grid) {
    int count = 0;
    int rows = grid.size();
    int cols = grid[0].size();
    
    // Check each possible 3x3 sub-grid
    for (int i = 0; i <= rows - 3; i++) {
        for (int j = 0; j <= cols - 3; j++) {
            // Check if the sub-grid is a magic square
            if (isMagicSquare(grid, i, j)) {
                count++;
            }
        }
    }
    
    return count;
}

bool isMagicSquare(vector<vector<int>>& grid, int row, int col) {
    int sum = 0;
    for (int i = row; i < row + 3; i++) {
        for (int j = col; j < col + 3; j++) {
            if (grid[i][j] < 1 || grid[i][j] > 9) {
                return false;
            }
            sum += grid[i][j];
        }
    }
    
    // Check rows
    for (int i = row; i < row + 3; i++) {
        int rowSum = 0;
        for (int j = col; j < col + 3; j++) {
            rowSum += grid[i][j];
        }
        if (rowSum != sum / 3) {
            return false;
        }
    }
    
    // Check columns
    for (int j = col; j < col + 3; j++) {
        int colSum = 0;
        for (int i = row; i < row + 3; i++) {
            colSum += grid[i][j];
        }
        if (colSum != sum / 3) {
            return false;
        }
    }
    
    // Check diagonals
    int diagonal1 = grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2];
    int diagonal2 = grid[row][col + 2] + grid[row + 1][col + 1] + grid[row + 2][col];
    if (diagonal1 != sum / 3 || diagonal2 != sum / 3) {
        return false;
    }
    
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot 3^2)$, where $m$ and $n$ are the dimensions of the grid. This is because we're checking every possible 3x3 sub-grid, and for each sub-grid, we're checking the sums of rows, columns, and diagonals.
> - **Space Complexity:** $O(1)$, as we're not using any additional space that scales with input size.
> - **Why these complexities occur:** The time complexity is high because we're checking every possible sub-grid, which results in a lot of repeated work.

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of checking every possible sub-grid, we can use a more efficient method to check if a sub-grid is a magic square.
- Detailed breakdown of the approach:
  1. Iterate over each cell in the grid.
  2. For each cell, check if it's possible to form a 3x3 sub-grid starting from that cell.
  3. If it's possible, calculate the sum of the first row of the sub-grid.
  4. Check if the sub-grid is a magic square by comparing the sums of rows, columns, and diagonals to the sum of the first row.
- Proof of optimality: This approach is optimal because it minimizes the number of operations required to check if a sub-grid is a magic square.

```cpp
int numMagicSquaresInside(vector<vector<int>>& grid) {
    int count = 0;
    int rows = grid.size();
    int cols = grid[0].size();
    
    // Check each possible 3x3 sub-grid
    for (int i = 0; i <= rows - 3; i++) {
        for (int j = 0; j <= cols - 3; j++) {
            // Check if the sub-grid is a magic square
            if (isMagicSquare(grid, i, j)) {
                count++;
            }
        }
    }
    
    return count;
}

bool isMagicSquare(vector<vector<int>>& grid, int row, int col) {
    int sum = grid[row][col] + grid[row][col + 1] + grid[row][col + 2];
    
    // Check rows
    for (int i = row; i < row + 3; i++) {
        int rowSum = 0;
        for (int j = col; j < col + 3; j++) {
            if (grid[i][j] < 1 || grid[i][j] > 9) {
                return false;
            }
            rowSum += grid[i][j];
        }
        if (rowSum != sum) {
            return false;
        }
    }
    
    // Check columns
    for (int j = col; j < col + 3; j++) {
        int colSum = 0;
        for (int i = row; i < row + 3; i++) {
            colSum += grid[i][j];
        }
        if (colSum != sum) {
            return false;
        }
    }
    
    // Check diagonals
    int diagonal1 = grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2];
    int diagonal2 = grid[row][col + 2] + grid[row + 1][col + 1] + grid[row + 2][col];
    if (diagonal1 != sum || diagonal2 != sum) {
        return false;
    }
    
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the grid. This is because we're checking every possible 3x3 sub-grid, but we're doing it in a more efficient way.
> - **Space Complexity:** $O(1)$, as we're not using any additional space that scales with input size.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to check if a sub-grid is a magic square.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Checking for magic squares, iterating over sub-grids, and optimizing the checking process.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems (checking each sub-grid) and optimizing the solution by reducing the number of operations required.
- Optimization techniques learned: Using a more efficient method to check if a sub-grid is a magic square by comparing sums of rows, columns, and diagonals to the sum of the first row.
- Similar problems to practice: Checking for other types of patterns in grids, such as checking for Sudoku solutions or finding the maximum sum of a sub-grid.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as sub-grids that are not fully contained within the grid.
- Edge cases to watch for: Sub-grids that are not 3x3, or grids that contain numbers outside the range of 1 to 9.
- Performance pitfalls: Using a brute force approach that checks every possible sub-grid without optimizing the checking process.
- Testing considerations: Testing the solution with different types of input, such as grids with different sizes or grids that contain different types of patterns.