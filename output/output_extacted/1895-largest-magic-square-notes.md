## Largest Magic Square

**Problem Link:** https://leetcode.com/problems/largest-magic-square/description

**Problem Statement:**
- Input format: A 2D array `grid` of integers, representing a grid of numbers.
- Constraints: The grid size is at most 8x8, and each number in the grid is between 1 and 65.
- Expected output format: The size of the largest magic square that can be formed using the numbers in the grid.
- Key requirements and edge cases to consider: A magic square is a square grid filled with distinct positive integers in the range from 1 to n^2 such that each cell contains a different integer and the sum of the integers in each row, column, and diagonal is equal.
- Example test cases with explanations:
  - For the input `[[4,3,8,4],[9,5,1,9],[2,7,6,2]]`, the output should be `3`, because the largest magic square that can be formed is `[[4,9,2],[3,5,7],[8,1,6]]`.
  - For the input `[[5,5,5],[5,5,5],[5,5,5]]`, the output should be `1`, because the largest magic square that can be formed is a single cell with the value `5`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the largest magic square, we need to check all possible sub-grids of the given grid.
- Step-by-step breakdown of the solution:
  1. Generate all possible sub-grids of the given grid.
  2. For each sub-grid, check if it is a magic square.
  3. Keep track of the largest magic square found so far.
- Why this approach comes to mind first: It is a straightforward and intuitive approach to solve the problem, but it can be inefficient for large grids.

```cpp
class Solution {
public:
    int largestMagicSquare(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        int max_size = min(n, m);
        
        for (int size = max_size; size >= 1; size--) {
            for (int i = 0; i <= n - size; i++) {
                for (int j = 0; j <= m - size; j++) {
                    if (isMagicSquare(grid, i, j, size)) {
                        return size;
                    }
                }
            }
        }
        
        return 0;
    }
    
    bool isMagicSquare(vector<vector<int>>& grid, int x, int y, int size) {
        int expected_sum = 0;
        vector<bool> seen(size * size + 1, false);
        
        for (int i = x; i < x + size; i++) {
            int row_sum = 0;
            for (int j = y; j < y + size; j++) {
                int num = grid[i][j];
                if (seen[num]) {
                    return false;
                }
                seen[num] = true;
                row_sum += num;
            }
            if (expected_sum == 0) {
                expected_sum = row_sum;
            } else if (expected_sum != row_sum) {
                return false;
            }
        }
        
        for (int j = y; j < y + size; j++) {
            int col_sum = 0;
            for (int i = x; i < x + size; i++) {
                col_sum += grid[i][j];
            }
            if (col_sum != expected_sum) {
                return false;
            }
        }
        
        int diagonal1_sum = 0;
        int diagonal2_sum = 0;
        for (int i = x, j = y; i < x + size && j < y + size; i++, j++) {
            diagonal1_sum += grid[i][j];
        }
        for (int i = x + size - 1, j = y; i >= x && j < y + size; i--, j++) {
            diagonal2_sum += grid[i][j];
        }
        if (diagonal1_sum != expected_sum || diagonal2_sum != expected_sum) {
            return false;
        }
        
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^4)$, where $n$ is the size of the grid, because we are generating all possible sub-grids and checking if each one is a magic square.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the seen numbers and the expected sum.
> - **Why these complexities occur:** The time complexity is high because we are generating all possible sub-grids, and the space complexity is low because we are using a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible sub-grids, we can start from the largest possible size and check if it is a magic square.
- Detailed breakdown of the approach:
  1. Start from the largest possible size of the magic square, which is the minimum of the number of rows and columns in the grid.
  2. For each size, check all possible sub-grids of that size.
  3. If a sub-grid is a magic square, return its size.
  4. If no magic square is found, decrease the size by 1 and repeat the process.
- Proof of optimality: This approach is optimal because it checks all possible sub-grids of the largest size first, and then decreases the size until it finds a magic square.

```cpp
class Solution {
public:
    int largestMagicSquare(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        int max_size = min(n, m);
        
        for (int size = max_size; size >= 2; size--) {
            for (int i = 0; i <= n - size; i++) {
                for (int j = 0; j <= m - size; j++) {
                    if (isMagicSquare(grid, i, j, size)) {
                        return size;
                    }
                }
            }
        }
        
        return 1;
    }
    
    bool isMagicSquare(vector<vector<int>>& grid, int x, int y, int size) {
        int expected_sum = 0;
        vector<bool> seen(size * size + 1, false);
        
        for (int i = x; i < x + size; i++) {
            int row_sum = 0;
            for (int j = y; j < y + size; j++) {
                int num = grid[i][j];
                if (seen[num]) {
                    return false;
                }
                seen[num] = true;
                row_sum += num;
            }
            if (expected_sum == 0) {
                expected_sum = row_sum;
            } else if (expected_sum != row_sum) {
                return false;
            }
        }
        
        for (int j = y; j < y + size; j++) {
            int col_sum = 0;
            for (int i = x; i < x + size; i++) {
                col_sum += grid[i][j];
            }
            if (col_sum != expected_sum) {
                return false;
            }
        }
        
        int diagonal1_sum = 0;
        int diagonal2_sum = 0;
        for (int i = x, j = y; i < x + size && j < y + size; i++, j++) {
            diagonal1_sum += grid[i][j];
        }
        for (int i = x + size - 1, j = y; i >= x && j < y + size; i--, j++) {
            diagonal2_sum += grid[i][j];
        }
        if (diagonal1_sum != expected_sum || diagonal2_sum != expected_sum) {
            return false;
        }
        
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^4)$, where $n$ is the size of the grid, because we are checking all possible sub-grids of the largest size first.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the seen numbers and the expected sum.
> - **Optimality proof:** This approach is optimal because it checks all possible sub-grids of the largest size first, and then decreases the size until it finds a magic square.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: generating all possible sub-grids, checking if a sub-grid is a magic square.
- Problem-solving patterns identified: starting from the largest possible size and decreasing it until a magic square is found.
- Optimization techniques learned: using a constant amount of space to store the seen numbers and the expected sum.
- Similar problems to practice: finding the largest rectangle in a grid, finding the largest square in a grid.

**Mistakes to Avoid:**
- Common implementation errors: not checking if a sub-grid is a magic square, not using a constant amount of space.
- Edge cases to watch for: when the grid is empty, when the grid has only one cell.
- Performance pitfalls: generating all possible sub-grids without checking if they are magic squares.
- Testing considerations: testing the function with different grid sizes, testing the function with different magic square sizes.