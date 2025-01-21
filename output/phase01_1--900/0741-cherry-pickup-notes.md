## Cherry Pickup
**Problem Link:** https://leetcode.com/problems/cherry-pickup/description

**Problem Statement:**
- Input format: A 2D grid `grid` where each cell represents a tree with a certain number of cherries.
- Constraints: `1 <= grid.length <= 75` and `1 <= grid[i].length <= 75`.
- Expected output format: The maximum number of cherries that can be collected.
- Key requirements and edge cases to consider: The two robots start from the top row, and they can move either down or down and to the side. They can't move up or up and to the side.
- Example test cases with explanations:
  - For the input `grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]`, the output should be `24`. The two robots can move as follows: `R1` moves down to `(0,0)`, `(1,0)`, `(2,0)`, `(3,0)`, and `R2` moves down to `(0,2)`, `(1,2)`, `(2,2)`, `(3,2)`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible moves for both robots and calculate the total number of cherries collected.
- Step-by-step breakdown of the solution:
  1. Initialize the total number of cherries collected to `0`.
  2. Try all possible moves for both robots.
  3. For each move, calculate the number of cherries collected and add it to the total.
- Why this approach comes to mind first: It's a straightforward and intuitive solution that tries all possible combinations.

```cpp
int cherryPickup(vector<vector<int>>& grid) {
    int rows = grid.size();
    int cols = grid[0].size();
    int maxCherries = 0;
    
    // Try all possible moves for both robots
    for (int r1 = 0; r1 < rows; r1++) {
        for (int c1 = 0; c1 < cols; c1++) {
            for (int r2 = 0; r2 < rows; r2++) {
                for (int c2 = 0; c2 < cols; c2++) {
                    int cherries = 0;
                    int r1Temp = r1;
                    int c1Temp = c1;
                    int r2Temp = r2;
                    int c2Temp = c2;
                    
                    // Simulate the movement of both robots
                    for (int i = 0; i < rows; i++) {
                        // Move R1
                        if (r1Temp < rows) {
                            cherries += grid[r1Temp][c1Temp];
                            r1Temp++;
                        }
                        
                        // Move R2
                        if (r2Temp < rows) {
                            cherries += grid[r2Temp][c2Temp];
                            r2Temp++;
                        }
                    }
                    
                    // Update the maximum number of cherries collected
                    maxCherries = max(maxCherries, cherries);
                }
            }
        }
    }
    
    return maxCherries;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(75^4 \times 75)$, where $75$ is the maximum number of rows and columns in the grid, and $75$ is the number of rows.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum number of cherries collected.
> - **Why these complexities occur:** The time complexity occurs because we try all possible moves for both robots, which results in a large number of combinations. The space complexity is low because we only use a constant amount of space to store the maximum number of cherries collected.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to store the maximum number of cherries collected for each subproblem.
- Detailed breakdown of the approach:
  1. Initialize a 3D DP table `dp` where `dp[i][j][k]` represents the maximum number of cherries collected when `R1` is at column `j` and `R2` is at column `k` on row `i`.
  2. Fill the DP table in a bottom-up manner.
  3. For each cell in the DP table, calculate the maximum number of cherries collected by considering all possible moves for both robots.
- Proof of optimality: The DP approach ensures that we consider all possible moves for both robots and store the maximum number of cherries collected for each subproblem.

```cpp
int cherryPickup(vector<vector<int>>& grid) {
    int rows = grid.size();
    int cols = grid[0].size();
    vector<vector<vector<int>>> dp(rows, vector<vector<int>>(cols, vector<int>(cols, 0)));
    
    // Initialize the base case
    for (int j = 0; j < cols; j++) {
        for (int k = 0; k < cols; k++) {
            dp[rows - 1][j][k] = grid[rows - 1][j] + (j != k ? grid[rows - 1][k] : 0);
        }
    }
    
    // Fill the DP table in a bottom-up manner
    for (int i = rows - 2; i >= 0; i--) {
        for (int j = 0; j < cols; j++) {
            for (int k = 0; k < cols; k++) {
                int maxCherries = 0;
                
                // Consider all possible moves for both robots
                for (int j1 = max(0, j - 1); j1 <= min(j + 1, cols - 1); j1++) {
                    for (int k1 = max(0, k - 1); k1 <= min(k + 1, cols - 1); k1++) {
                        maxCherries = max(maxCherries, dp[i + 1][j1][k1]);
                    }
                }
                
                // Update the DP table
                dp[i][j][k] = maxCherries + grid[i][j] + (j != k ? grid[i][k] : 0);
            }
        }
    }
    
    // Find the maximum number of cherries collected
    int maxCherries = 0;
    for (int j = 0; j < cols; j++) {
        for (int k = 0; k < cols; k++) {
            maxCherries = max(maxCherries, dp[0][j][k]);
        }
    }
    
    return maxCherries;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(75^3)$, where $75$ is the maximum number of rows and columns in the grid.
> - **Space Complexity:** $O(75^3)$, as we use a 3D DP table to store the maximum number of cherries collected for each subproblem.
> - **Optimality proof:** The DP approach ensures that we consider all possible moves for both robots and store the maximum number of cherries collected for each subproblem, resulting in an optimal solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, memoization.
- Problem-solving patterns identified: Breaking down the problem into smaller subproblems, using a DP table to store the maximum number of cherries collected for each subproblem.
- Optimization techniques learned: Using a DP table to avoid redundant calculations, considering all possible moves for both robots.
- Similar problems to practice: Other dynamic programming problems, such as the `House Robber` problem or the `Longest Increasing Subsequence` problem.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize the DP table, not considering all possible moves for both robots.
- Edge cases to watch for: When the grid has only one row or one column, when the robots start at the same column.
- Performance pitfalls: Using a naive approach that tries all possible moves for both robots, resulting in a high time complexity.
- Testing considerations: Testing the solution with different grid sizes, testing the solution with different starting positions for the robots.