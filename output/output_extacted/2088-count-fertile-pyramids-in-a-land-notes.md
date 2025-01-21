## Count Fertile Pyramids in a Land

**Problem Link:** https://leetcode.com/problems/count-fertile-pyramids-in-a-land/description

**Problem Statement:**
- Input format and constraints: The problem involves a 2D grid representing a land with `m` rows and `n` columns, where each cell can be either fertile (`1`) or not (`0`). The task is to count the number of fertile pyramids in the land. A fertile pyramid is defined as a square shape where the top cell is fertile and all the cells below it in the same column and the cells to the right in the same row are also fertile.
- Expected output format: The function should return the total count of fertile pyramids found in the land.
- Key requirements and edge cases to consider: Handling cases where the input grid is empty, or there are no fertile cells, or when the grid contains only one row or one column.
- Example test cases with explanations: For example, given a grid with two rows and three columns, where the top-left and bottom-right cells are fertile, the function should return the count of fertile pyramids that can be formed.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach to solving this problem might involve checking every possible square sub-grid within the given grid to see if it forms a fertile pyramid.
- Step-by-step breakdown of the solution:
  1. Iterate over each cell in the grid.
  2. For each cell, consider all possible square sizes (from 1x1 to the maximum possible size given the cell's position).
  3. For each square size, check if the top-left cell of the square is fertile and if all cells below it in the same column and to the right in the same row are fertile.
  4. If a fertile pyramid is found, increment the count.
- Why this approach comes to mind first: It's a straightforward method that checks all possibilities, which aligns with the definition of a brute force approach.

```cpp
int countPyramids(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    int count = 0;
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            // Check all possible square sizes starting from the current cell
            for (int size = 1; i + size <= m && j + size <= n; size++) {
                bool isPyramid = true;
                // Check if all cells in the potential pyramid are fertile
                for (int k = 0; k < size; k++) {
                    for (int l = 0; l < size; l++) {
                        if (grid[i + k][j + l] == 0) {
                            isPyramid = false;
                            break;
                        }
                    }
                    if (!isPyramid) break;
                }
                if (isPyramid) count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot min(m, n)^3)$, where $m$ and $n$ are the dimensions of the grid. This is because for each cell, we potentially check all possible square sizes, and for each size, we check all cells within that square.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the count and loop variables.
> - **Why these complexities occur:** The brute force approach involves nested loops that check every possible square sub-grid, leading to a cubic term in the time complexity due to the nested iteration over the grid and potential pyramid sizes.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking all possible squares for each cell, we can start from the smallest possible fertile pyramids (1x1 squares) and expand them as long as all cells below and to the right are fertile. This way, we avoid redundant checks and only consider fertile cells as starting points.
- Detailed breakdown of the approach:
  1. Initialize a count variable to store the number of fertile pyramids.
  2. Iterate over each cell in the grid. If a cell is fertile, consider it as a potential starting point for a fertile pyramid.
  3. For each fertile cell, expand the pyramid size as long as all cells below and to the right are fertile.
  4. Increment the count for each fertile pyramid found.
- Proof of optimality: This approach is optimal because it only checks fertile cells as potential starting points for pyramids and expands them in a way that minimizes redundant checks, thus reducing the time complexity significantly.

```cpp
int countPyramids(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    int count = 0;
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 1) {
                int size = 1;
                while (i + size < m && j + size < n) {
                    bool isPyramid = true;
                    for (int k = 0; k < size; k++) {
                        for (int l = 0; l < size; l++) {
                            if (grid[i + k][j + l] == 0) {
                                isPyramid = false;
                                break;
                            }
                        }
                        if (!isPyramid) break;
                    }
                    if (isPyramid) {
                        count++;
                        size++;
                    } else {
                        break;
                    }
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot min(m, n))$, as we potentially expand each fertile cell into a pyramid of maximum size $min(m, n)$.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Optimality proof:** This approach is optimal because it minimizes the number of checks by only considering fertile cells and expanding them in a single pass, thus achieving a linear time complexity with respect to the grid size and potential pyramid sizes.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional checks, and optimization techniques to reduce redundant computations.
- Problem-solving patterns identified: Starting with a brute force approach and then optimizing based on the problem's specific constraints and properties.
- Optimization techniques learned: Minimizing redundant checks and using the problem's structure to reduce computational complexity.
- Similar problems to practice: Other grid-based problems that involve pattern recognition and optimization.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases, such as grids with zero rows or columns, or not properly checking for fertile cells.
- Edge cases to watch for: Empty grids, grids with only one row or column, and grids with no fertile cells.
- Performance pitfalls: Using a brute force approach without considering optimizations based on the problem's structure.
- Testing considerations: Thoroughly testing the function with various grid sizes, fertile cell distributions, and edge cases to ensure correctness and performance.