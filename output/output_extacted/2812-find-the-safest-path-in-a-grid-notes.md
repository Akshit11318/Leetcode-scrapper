## Find the Safest Path in a Grid
**Problem Link:** https://leetcode.com/problems/find-the-safest-path-in-a-grid/description

**Problem Statement:**
- Input: A 2D grid where each cell represents a path with a certain safety score.
- Constraints: The grid size is within a reasonable range (e.g., up to 10x10 for simplicity), and safety scores are non-negative integers.
- Expected Output: The safest path from the top-left to the bottom-right corner, defined as the path with the minimum total safety score.
- Key Requirements: The path must only move right or down from any cell.
- Example Test Cases:
  - A grid with all safety scores being 0 should return a path with a total safety score of 0.
  - A grid with varying safety scores should return the path with the lowest total safety score.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible paths and calculate the total safety score for each.
- Step-by-step breakdown:
  1. Generate all possible paths from the top-left to the bottom-right corner.
  2. For each path, sum the safety scores of all cells in the path.
  3. Find the path with the minimum total safety score.
- Why this approach comes to mind first: It directly addresses the problem statement by considering all possible solutions.

```cpp
#include <vector>
#include <algorithm>

void generatePaths(vector<vector<int>>& grid, int row, int col, vector<pair<int, int>>& currentPath, vector<vector<pair<int, int>>>& allPaths) {
    if (row == grid.size() - 1 && col == grid[0].size() - 1) {
        allPaths.push_back(currentPath);
        return;
    }
    
    currentPath.push_back({row, col});
    
    if (row < grid.size() - 1) {
        generatePaths(grid, row + 1, col, currentPath, allPaths);
    }
    
    if (col < grid[0].size() - 1) {
        generatePaths(grid, row, col + 1, currentPath, allPaths);
    }
    
    currentPath.pop_back();
}

int findSafestPathBruteForce(vector<vector<int>>& grid) {
    vector<vector<pair<int, int>>> allPaths;
    vector<pair<int, int>> currentPath;
    generatePaths(grid, 0, 0, currentPath, allPaths);
    
    int minScore = INT_MAX;
    for (auto& path : allPaths) {
        int score = 0;
        for (auto& cell : path) {
            score += grid[cell.first][cell.second];
        }
        minScore = min(minScore, score);
    }
    
    return minScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{m+n})$ where $m$ and $n$ are the dimensions of the grid, because in the worst case, we explore all possible paths.
> - **Space Complexity:** $O(2^{m+n})$ for storing all paths.
> - **Why these complexities occur:** The brute force approach generates all possible paths, leading to exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use dynamic programming to store and reuse the minimum safety scores for sub-paths.
- Detailed breakdown:
  1. Initialize a 2D array `dp` of the same size as the input grid, where `dp[i][j]` will store the minimum safety score to reach cell `(i, j)` from the top-left corner.
  2. Fill `dp` row by row from left to right and top to bottom, using the minimum safety score from the cell above or to the left, plus the safety score of the current cell.
  3. The minimum safety score to reach the bottom-right corner is stored in `dp[m-1][n-1]`.
- Proof of optimality: This approach ensures that each sub-path's minimum safety score is calculated only once and reused, avoiding redundant calculations.

```cpp
int findSafestPathOptimal(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    vector<vector<int>> dp(m, vector<int>(n, 0));
    
    dp[0][0] = grid[0][0];
    for (int i = 1; i < m; ++i) {
        dp[i][0] = dp[i-1][0] + grid[i][0];
    }
    for (int j = 1; j < n; ++j) {
        dp[0][j] = dp[0][j-1] + grid[0][j];
    }
    
    for (int i = 1; i < m; ++i) {
        for (int j = 1; j < n; ++j) {
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j];
        }
    }
    
    return dp[m-1][n-1];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the grid, because we fill the `dp` array once.
> - **Space Complexity:** $O(m \cdot n)$ for the `dp` array.
> - **Optimality proof:** This approach has a polynomial time complexity, making it much more efficient than the brute force approach for large grids.

---

### Final Notes

**Learning Points:**
- Dynamic programming is crucial for solving problems that have overlapping sub-problems.
- The key to dynamic programming is identifying how to break down the problem into smaller sub-problems and how to store and reuse their solutions efficiently.
- Always consider the trade-offs between time and space complexity when choosing an approach.

**Mistakes to Avoid:**
- Not identifying the overlapping sub-problems in dynamic programming, leading to redundant calculations.
- Not considering the base cases properly in recursive solutions.
- Not validating the input and handling edge cases, which can lead to incorrect results or crashes.