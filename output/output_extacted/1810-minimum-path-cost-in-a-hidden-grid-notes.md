## Minimum Path Cost in a Hidden Grid
**Problem Link:** https://leetcode.com/problems/minimum-path-cost-in-a-hidden-grid/description

**Problem Statement:**
- Input format: A 2D grid where each cell represents a cost, and a starting position.
- Constraints: The grid can be of any size, and the starting position is within the grid boundaries.
- Expected output format: The minimum cost to reach the target position from the starting position.
- Key requirements and edge cases to consider: The grid can be empty, and the starting position can be the same as the target position.
- Example test cases with explanations:
    - A simple grid with a clear path to the target position.
    - A grid with obstacles or high-cost cells that require a longer path.
    - An edge case where the starting position is the same as the target position.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible paths from the starting position to the target position and calculate the total cost for each path.
- Step-by-step breakdown of the solution:
    1. Define a recursive function that tries all possible movements (up, down, left, right) from the current position.
    2. For each movement, calculate the new position and the new cost.
    3. If the new position is the target position, return the new cost.
    4. If the new position is out of bounds or has been visited before, return infinity.
    5. Otherwise, recursively try all possible movements from the new position and return the minimum cost.
- Why this approach comes to mind first: It's a straightforward way to explore all possible paths and find the minimum cost.

```cpp
#include <vector>
#include <climits>
using namespace std;

int minPathCost(vector<vector<int>>& grid, int startRow, int startCol, int endRow, int endCol) {
    int rows = grid.size();
    int cols = grid[0].size();
    vector<vector<bool>> visited(rows, vector<bool>(cols, false));

    int dfs(int row, int col) {
        if (row == endRow && col == endCol) return grid[row][col];
        if (row < 0 || row >= rows || col < 0 || col >= cols || visited[row][col]) return INT_MAX;

        visited[row][col] = true;
        int minCost = INT_MAX;
        minCost = min(minCost, dfs(row - 1, col) + grid[row][col]);
        minCost = min(minCost, dfs(row + 1, col) + grid[row][col]);
        minCost = min(minCost, dfs(row, col - 1) + grid[row][col]);
        minCost = min(minCost, dfs(row, col + 1) + grid[row][col]);
        visited[row][col] = false;

        return minCost;
    }

    return dfs(startRow, startCol);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(4^{rows \times cols})$ because in the worst case, we try all possible movements for each cell.
> - **Space Complexity:** $O(rows \times cols)$ because we use a visited matrix to keep track of visited cells.
> - **Why these complexities occur:** The brute force approach tries all possible paths, which leads to exponential time complexity. The space complexity is due to the visited matrix.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use dynamic programming to store the minimum cost to reach each cell.
- Detailed breakdown of the approach:
    1. Create a 2D array `dp` where `dp[row][col]` stores the minimum cost to reach the cell at `(row, col)`.
    2. Initialize the first row and column of `dp` based on the costs in the grid.
    3. Fill in the rest of `dp` by trying all possible movements from the previous cells and taking the minimum cost.
- Proof of optimality: The dynamic programming approach ensures that we only try each cell once and store the minimum cost to reach it, which leads to optimal time complexity.
- Why further optimization is impossible: The dynamic programming approach already has optimal time complexity.

```cpp
#include <vector>
#include <climits>
using namespace std;

int minPathCost(vector<vector<int>>& grid, int startRow, int startCol, int endRow, int endCol) {
    int rows = grid.size();
    int cols = grid[0].size();
    vector<vector<int>> dp(rows, vector<int>(cols, INT_MAX));

    dp[startRow][startCol] = grid[startRow][startCol];
    for (int row = startRow; row <= endRow; row++) {
        for (int col = startCol; col <= endCol; col++) {
            if (row == startRow && col == startCol) continue;
            int minCost = INT_MAX;
            if (row > 0) minCost = min(minCost, dp[row - 1][col] + grid[row][col]);
            if (row < rows - 1) minCost = min(minCost, dp[row + 1][col] + grid[row][col]);
            if (col > 0) minCost = min(minCost, dp[row][col - 1] + grid[row][col]);
            if (col < cols - 1) minCost = min(minCost, dp[row][col + 1] + grid[row][col]);
            dp[row][col] = minCost;
        }
    }

    return dp[endRow][endCol];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(rows \times cols)$ because we fill in the `dp` array once.
> - **Space Complexity:** $O(rows \times cols)$ because we use the `dp` array to store the minimum costs.
> - **Optimality proof:** The dynamic programming approach ensures that we only try each cell once and store the minimum cost to reach it, which leads to optimal time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, recursive functions.
- Problem-solving patterns identified: Trying all possible paths, using dynamic programming to store minimum costs.
- Optimization techniques learned: Using dynamic programming to avoid redundant calculations.
- Similar problems to practice: Other dynamic programming problems, such as the `Longest Common Subsequence` problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` array correctly, not handling edge cases.
- Edge cases to watch for: The grid can be empty, the starting position can be the same as the target position.
- Performance pitfalls: Using a brute force approach instead of dynamic programming.
- Testing considerations: Test the function with different grid sizes, starting and target positions.