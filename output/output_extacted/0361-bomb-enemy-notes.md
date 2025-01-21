## Bomb Enemy
**Problem Link:** https://leetcode.com/problems/bomb-enemy/description

**Problem Statement:**
- Input format and constraints: Given a 2D grid, where `0` represents an empty cell, `1` represents a wall, and `E` represents an enemy that can be killed with a bomb. The goal is to find the maximum number of enemies that can be killed by placing a bomb at a particular cell.
- Expected output format: The maximum number of enemies that can be killed by placing a bomb at any cell.
- Key requirements and edge cases to consider: 
  - The bomb can only be placed in an empty cell.
  - The bomb can kill all enemies in the same row and column as the bomb.
  - The bomb cannot kill enemies that are blocked by a wall.
- Example test cases with explanations:
  - For example, given the grid `[['0','E','0','0'],['E','0','W','E'],['0','E','0','0']]`, the maximum number of enemies that can be killed by placing a bomb at any cell is `3`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible positions for the bomb and calculate the number of enemies that can be killed for each position.
- Step-by-step breakdown of the solution:
  1. Iterate over all cells in the grid.
  2. For each cell, check if it is an empty cell. If not, skip to the next cell.
  3. For each empty cell, calculate the number of enemies that can be killed by placing a bomb at that cell.
  4. Update the maximum number of enemies that can be killed if the current cell can kill more enemies than the previous maximum.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it may not be efficient for large grids.

```cpp
#include <vector>
using namespace std;

int maxKilledEnemies(vector<vector<char>>& grid) {
    int maxEnemies = 0;
    for (int i = 0; i < grid.size(); i++) {
        for (int j = 0; j < grid[0].size(); j++) {
            if (grid[i][j] == '0') {
                int enemies = 0;
                // Check row
                for (int k = 0; k < grid[0].size(); k++) {
                    if (grid[i][k] == 'E') {
                        enemies++;
                    } else if (grid[i][k] == 'W') {
                        break;
                    }
                }
                // Check column
                for (int k = 0; k < grid.size(); k++) {
                    if (grid[k][j] == 'E') {
                        enemies++;
                    } else if (grid[k][j] == 'W') {
                        break;
                    }
                }
                maxEnemies = max(maxEnemies, enemies);
            }
        }
    }
    return maxEnemies;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot (m + n))$, where $m$ is the number of rows and $n$ is the number of columns in the grid. This is because for each cell, we are checking all cells in the same row and column.
> - **Space Complexity:** $O(1)$, as we are not using any extra space that scales with the input size.
> - **Why these complexities occur:** The time complexity is high because we are checking all cells in the same row and column for each cell. The space complexity is low because we are not using any extra space that scales with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking all cells in the same row and column for each cell, we can calculate the number of enemies that can be killed by a bomb in each row and column separately.
- Detailed breakdown of the approach:
  1. Calculate the number of enemies that can be killed by a bomb in each row.
  2. Calculate the number of enemies that can be killed by a bomb in each column.
  3. For each cell, calculate the total number of enemies that can be killed by a bomb at that cell by adding the number of enemies that can be killed in the same row and column.
- Proof of optimality: This approach is optimal because it avoids redundant calculations and only checks each row and column once.

```cpp
#include <vector>
using namespace std;

int maxKilledEnemies(vector<vector<char>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    int maxEnemies = 0;
    vector<int> rowEnemies(m, 0);
    vector<int> colEnemies(n, 0);
    
    // Calculate row enemies
    for (int i = 0; i < m; i++) {
        int enemies = 0;
        bool wall = false;
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 'W') {
                wall = true;
                enemies = 0;
            } else if (grid[i][j] == 'E' && !wall) {
                enemies++;
            }
        }
        rowEnemies[i] = enemies;
    }
    
    // Calculate column enemies
    for (int j = 0; j < n; j++) {
        int enemies = 0;
        bool wall = false;
        for (int i = 0; i < m; i++) {
            if (grid[i][j] == 'W') {
                wall = true;
                enemies = 0;
            } else if (grid[i][j] == 'E' && !wall) {
                enemies++;
            }
        }
        colEnemies[j] = enemies;
    }
    
    // Calculate total enemies
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == '0') {
                maxEnemies = max(maxEnemies, rowEnemies[i] + colEnemies[j]);
            }
        }
    }
    
    return maxEnemies;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns in the grid. This is because we are checking each cell once to calculate the row and column enemies, and then once to calculate the total enemies.
> - **Space Complexity:** $O(m + n)$, as we are using extra space to store the row and column enemies.
> - **Optimality proof:** This approach is optimal because it avoids redundant calculations and only checks each row and column once, resulting in a time complexity of $O(m \cdot n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, iteration, and optimization.
- Problem-solving patterns identified: Avoiding redundant calculations and using extra space to store intermediate results.
- Optimization techniques learned: Using iteration to calculate row and column enemies, and then using these values to calculate the total enemies.
- Similar problems to practice: Other problems that involve iteration, dynamic programming, and optimization, such as the "Unique Paths" problem.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as empty rows or columns.
- Edge cases to watch for: Empty rows or columns, and cells that are not '0', 'E', or 'W'.
- Performance pitfalls: Using a brute force approach that results in a high time complexity.
- Testing considerations: Test the solution with different inputs, including edge cases, to ensure that it is working correctly.