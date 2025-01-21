## Largest 1-Bordered Square

**Problem Link:** https://leetcode.com/problems/largest-1-bordered-square/description

**Problem Statement:**
- Input: A 2D binary array `grid` where `grid[i][j]` is either 0 or 1.
- Expected Output: The side length of the largest square with a border of 1s that can be formed in the grid.
- Key Requirements:
  - The square must have a border of 1s.
  - The inner cells of the square can be either 0s or 1s.
- Edge Cases:
  - The input grid can be empty.
  - The input grid can have no 1s.

**Example Test Cases:**
- `grid = [[1,1,1],[1,0,1],[1,1,1]]` should return 2.
- `grid = [[1,1,0],[1,0,1],[0,1,1]]` should return 1.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to check every possible square in the grid to see if it has a border of 1s.
- We start by iterating over every cell in the grid.
- For each cell, we consider all possible square sizes that can be formed with the cell as the top-left corner.
- We then check each square to see if it has a border of 1s by checking the cells on the border.

```cpp
class Solution {
public:
    int largest1BorderedSquare(vector<vector<int>>& grid) {
        int rows = grid.size();
        if (rows == 0) return 0;
        int cols = grid[0].size();
        
        int maxSide = 0;
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                for (int side = 1; i + side <= rows && j + side <= cols; side++) {
                    if (hasBorder(grid, i, j, side)) {
                        maxSide = max(maxSide, side);
                    }
                }
            }
        }
        
        return maxSide;
    }
    
    bool hasBorder(vector<vector<int>>& grid, int i, int j, int side) {
        // Check top and bottom borders
        for (int k = 0; k < side; k++) {
            if (grid[i][j + k] != 1 || grid[i + side - 1][j + k] != 1) {
                return false;
            }
        }
        
        // Check left and right borders
        for (int k = 0; k < side; k++) {
            if (grid[i + k][j] != 1 || grid[i + k][j + side - 1] != 1) {
                return false;
            }
        }
        
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^4)$, where $n$ is the number of rows (or columns) in the grid. This is because we are iterating over every cell in the grid, and for each cell, we are checking all possible square sizes.
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with the input size.
> - **Why these complexities occur:** The time complexity is high because we are using a brute force approach that checks every possible square in the grid. The space complexity is low because we are not using any additional data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a prefix sum array to store the sum of 1s in each row and column.
- We can then use this prefix sum array to quickly check if a square has a border of 1s.
- We start by initializing the prefix sum array.
- We then iterate over every cell in the grid and consider all possible square sizes that can be formed with the cell as the top-left corner.
- We use the prefix sum array to quickly check if the square has a border of 1s.

```cpp
class Solution {
public:
    int largest1BorderedSquare(vector<vector<int>>& grid) {
        int rows = grid.size();
        if (rows == 0) return 0;
        int cols = grid[0].size();
        
        vector<vector<int>> rowSum(rows, vector<int>(cols + 1, 0));
        vector<vector<int>> colSum(cols, vector<int>(rows + 1, 0));
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                rowSum[i][j + 1] = rowSum[i][j] + grid[i][j];
                colSum[j][i + 1] = colSum[j][i] + grid[i][j];
            }
        }
        
        int maxSide = 0;
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                for (int side = 1; i + side <= rows && j + side <= cols; side++) {
                    if (hasBorder(grid, rowSum, colSum, i, j, side)) {
                        maxSide = max(maxSide, side);
                    }
                }
            }
        }
        
        return maxSide;
    }
    
    bool hasBorder(vector<vector<int>>& grid, vector<vector<int>>& rowSum, vector<vector<int>>& colSum, int i, int j, int side) {
        // Check top and bottom borders
        if (rowSum[i][j + side] - rowSum[i][j] != side || rowSum[i + side - 1][j + side] - rowSum[i + side - 1][j] != side) {
            return false;
        }
        
        // Check left and right borders
        if (colSum[j][i + side] - colSum[j][i] != side || colSum[j + side - 1][i + side] - colSum[j + side - 1][i] != side) {
            return false;
        }
        
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of rows (or columns) in the grid. This is because we are iterating over every cell in the grid, and for each cell, we are checking all possible square sizes.
> - **Space Complexity:** $O(n^2)$, as we are using additional space to store the prefix sum array.
> - **Optimality proof:** This is the optimal solution because we are using a prefix sum array to quickly check if a square has a border of 1s, which reduces the time complexity from $O(n^4)$ to $O(n^3)$.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the use of prefix sum arrays to quickly check if a square has a border of 1s.
- The problem-solving pattern identified is to use a brute force approach first and then optimize it using a prefix sum array.
- The optimization technique learned is to use a prefix sum array to reduce the time complexity of the algorithm.

**Mistakes to Avoid:**
- A common implementation error is to forget to initialize the prefix sum array correctly.
- An edge case to watch for is when the input grid is empty.
- A performance pitfall is to use a brute force approach without optimizing it using a prefix sum array.