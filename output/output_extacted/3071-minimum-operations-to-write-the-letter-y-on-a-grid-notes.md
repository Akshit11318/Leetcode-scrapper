## Minimum Operations to Write the Letter Y on a Grid

**Problem Link:** https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid/description

**Problem Statement:**
- Input: `grid` - a 2D grid of size `m x n` containing only 0s and 1s, representing empty and filled cells respectively.
- Constraints: `1 <= m, n <= 10^5`.
- Expected Output: The minimum number of operations required to write the letter Y on the grid.
- Key Requirements:
  - The letter Y must be written by filling in cells in the grid.
  - Each operation consists of filling a single empty cell.
- Edge Cases:
  - If the grid is too small to write the letter Y, return -1.
  - If the grid is already filled with the letter Y, return 0.

### Example Test Cases:

1. `grid = [[1,1,1],[0,1,0],[0,0,0]]` -> Output: `2` because we need to fill two empty cells to complete the Y shape.
2. `grid = [[1,1,1],[0,0,0],[0,0,0]]` -> Output: `4` because we need to fill four empty cells to complete the Y shape.

---

### Brute Force Approach

**Explanation:**
- The brute force approach involves checking all possible positions where the Y shape can fit within the grid.
- For each position, count the number of empty cells that need to be filled to complete the Y shape.
- Keep track of the minimum count found across all positions.

```cpp
class Solution {
public:
    int minOperations(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int minOps = INT_MAX;
        
        for (int i = 0; i < m - 2; i++) {
            for (int j = 0; j < n - 2; j++) {
                int ops = 0;
                // Count operations for the top cell of Y
                if (grid[i][j] == 0) ops++;
                // Count operations for the middle cell of Y
                if (grid[i + 1][j] == 0) ops++;
                // Count operations for the bottom left cell of Y
                if (grid[i + 2][j] == 0) ops++;
                // Count operations for the bottom right cell of Y
                if (grid[i + 2][j + 1] == 0) ops++;
                // Count operations for the middle left cell of Y
                if (grid[i + 1][j + 1] == 0) ops++;
                // Update minimum operations
                minOps = min(minOps, ops);
            }
        }
        return minOps == INT_MAX ? -1 : minOps;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \times n)$, where $m$ and $n$ are the dimensions of the grid. This is because we iterate over each cell in the grid once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum operations and the current operations count.
> - **Why these complexities occur:** The brute force approach has a linear time complexity because it checks every possible position in the grid. The space complexity is constant because we only use a fixed amount of space to store the minimum operations and the current operations count.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves observing the pattern of the Y shape and directly counting the number of empty cells that need to be filled.
- We can start by checking if the grid is large enough to fit the Y shape. If not, return -1.
- Then, we can directly count the number of empty cells in the positions where the Y shape would be.

```cpp
class Solution {
public:
    int minOperations(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        if (m < 3 || n < 3) return -1; // Not enough space for Y
        
        int ops = 0;
        // Count operations for the top cell of Y
        if (grid[0][0] == 0) ops++;
        // Count operations for the middle cell of Y
        if (grid[1][0] == 0) ops++;
        // Count operations for the bottom left cell of Y
        if (grid[2][0] == 0) ops++;
        // Count operations for the bottom right cell of Y
        if (grid[2][1] == 0) ops++;
        // Count operations for the middle left cell of Y
        if (grid[1][1] == 0) ops++;
        return ops;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because we only access a constant number of cells in the grid.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the operations count.
> - **Optimality proof:** This approach is optimal because it directly counts the minimum number of operations required to fill the Y shape, without checking every possible position in the grid.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: pattern observation, direct counting.
- Problem-solving patterns identified: checking for sufficient space, counting operations.
- Optimization techniques learned: avoiding unnecessary iterations, using constants.
- Similar problems to practice: other grid-based problems, pattern recognition.

**Mistakes to Avoid:**
- Common implementation errors: not checking for sufficient space, incorrect counting.
- Edge cases to watch for: grids that are too small, grids that are already filled.
- Performance pitfalls: using brute force approaches for large grids.
- Testing considerations: testing with small and large grids, testing with different patterns.