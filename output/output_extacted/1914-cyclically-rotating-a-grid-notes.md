## Cyclically Rotating a Grid

**Problem Link:** https://leetcode.com/problems/cyclically-rotating-a-grid/description

**Problem Statement:**
- Input format and constraints: The input grid is a 2D array of integers with dimensions `m x n`. The number of rotations `k` is also provided.
- Expected output format: The function should return the rotated grid after `k` rotations.
- Key requirements and edge cases to consider:
  - The grid is rotated in a cyclic manner, meaning that the top row becomes the rightmost column, the rightmost column becomes the bottom row, the bottom row becomes the leftmost column, and the leftmost column becomes the top row.
  - The number of rotations `k` can be greater than the number of layers in the grid.
- Example test cases with explanations:
  - For example, given a grid `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]` and `k = 1`, the output should be `[[7, 4, 1], [8, 5, 2], [9, 6, 3]]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves simulating the rotation process `k` times. In each rotation, we iterate over the grid and update the values according to the rotation rules.
- Step-by-step breakdown of the solution:
  1. Create a copy of the input grid to store the rotated values.
  2. Iterate over the grid `k` times, applying the rotation rules in each iteration.
  3. In each iteration, update the values in the copy of the grid according to the rotation rules.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, as it directly simulates the rotation process.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> rotateGrid(vector<vector<int>>& grid, int k) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> rotatedGrid(m, vector<int>(n, 0));
        
        for (int layer = 0; layer < min(m, n) / 2; layer++) {
            int first = layer;
            int last = m - layer - 1;
            for (int i = 0; i < k; i++) {
                // Save the top row
                vector<int> topRow;
                for (int j = first; j <= last; j++) {
                    topRow.push_back(grid[first][j]);
                }
                
                // Left column becomes top row
                for (int j = first; j <= last; j++) {
                    grid[first][j] = grid[last - j + first][first];
                }
                
                // Bottom row becomes left column
                for (int j = first; j <= last; j++) {
                    grid[last - j + first][first] = grid[last][last - j + first];
                }
                
                // Right column becomes bottom row
                for (int j = first; j <= last; j++) {
                    grid[last][last - j + first] = grid[j][last];
                }
                
                // Top row becomes right column
                for (int j = first; j <= last; j++) {
                    grid[j][last] = topRow[j - first];
                }
            }
        }
        
        return grid;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(k \cdot (m + n))$ where $m$ and $n$ are the dimensions of the grid. This is because we are simulating the rotation process $k$ times, and in each rotation, we iterate over the grid.
> - **Space Complexity:** $O(1)$ because we are modifying the input grid in-place.
> - **Why these complexities occur:** The time complexity is high because we are simulating the rotation process $k$ times, which can be inefficient for large grids. The space complexity is low because we are modifying the input grid in-place.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of simulating the rotation process $k$ times, we can calculate the final position of each element after $k$ rotations.
- Detailed breakdown of the approach:
  1. Calculate the number of rotations required to return to the original position for each layer.
  2. Calculate the final position of each element after $k$ rotations.
- Proof of optimality: This approach is optimal because it avoids simulating the rotation process $k$ times, which reduces the time complexity significantly.
- Why further optimization is impossible: This approach has a time complexity of $O(m \cdot n)$, which is the minimum required to iterate over the grid.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> rotateGrid(vector<vector<int>>& grid, int k) {
        int m = grid.size();
        int n = grid[0].size();
        
        for (int layer = 0; layer < min(m, n) / 2; layer++) {
            int first = layer;
            int last = m - layer - 1;
            int size = (last - first + 1) * 4;
            k %= size;
            
            for (int i = 0; i < k; i++) {
                int temp = grid[first][first];
                
                // Left column becomes top row
                for (int j = first; j <= last; j++) {
                    grid[first][j] = grid[last - j + first][first];
                }
                
                // Bottom row becomes left column
                for (int j = first; j <= last; j++) {
                    grid[last - j + first][first] = grid[last][last - j + first];
                }
                
                // Right column becomes bottom row
                for (int j = first; j <= last; j++) {
                    grid[last][last - j + first] = grid[j][last];
                }
                
                // Top row becomes right column
                for (int j = first; j <= last; j++) {
                    grid[j][last] = grid[first][j];
                }
                
                grid[first][first] = temp;
            }
        }
        
        return grid;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$ where $m$ and $n$ are the dimensions of the grid. This is because we are iterating over the grid once.
> - **Space Complexity:** $O(1)$ because we are modifying the input grid in-place.
> - **Optimality proof:** This approach is optimal because it has a time complexity of $O(m \cdot n)$, which is the minimum required to iterate over the grid.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Simulation, iteration, and optimization.
- Problem-solving patterns identified: Reducing the number of operations by calculating the final position of each element.
- Optimization techniques learned: Avoiding unnecessary operations by calculating the final position of each element.
- Similar problems to practice: Other grid rotation problems, such as rotating a grid by 90 degrees.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as when the grid has an odd number of rows or columns.
- Edge cases to watch for: When the grid has an odd number of rows or columns, the middle row or column should be handled separately.
- Performance pitfalls: Simulating the rotation process $k$ times, which can be inefficient for large grids.
- Testing considerations: Test the function with different grid sizes, rotation counts, and edge cases to ensure it works correctly.