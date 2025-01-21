## Where Will the Ball Fall

**Problem Link:** https://leetcode.com/problems/where-will-the-ball-fall/description

**Problem Statement:**
- Input format: `grid` - a 2D array of integers, where `grid[i][j]` is either 1 (right) or -1 (left), representing the direction of the ball.
- Constraints: `m == grid.length`, `n == grid[0].length`, `1 <= m, n <= 100`, `grid[i][j]` is either 1 or -1.
- Expected output format: An array of integers, where the `i-th` integer represents the column index (0-indexed) where the ball placed at the `i-th` column will fall.
- Key requirements and edge cases to consider:
  - The ball will always fall down.
  - If the ball is at a position where it can move to the right, it will move to the right.
  - If the ball is at a position where it can move to the left, it will move to the left.
  - If the ball is at a position where it cannot move to either side, it will fall down.
- Example test cases with explanations:
  - `grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]` should return `[1,2,2,3,0]`.
  - `grid = [[-1]]` should return `[0]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Simulate the movement of the ball for each column and track where it ends up.
- Step-by-step breakdown of the solution:
  1. Iterate over each column in the grid.
  2. For each column, simulate the movement of the ball from the top to the bottom.
  3. At each step, check the direction of the ball and move it accordingly.
  4. If the ball reaches the bottom, record the column index where it fell.
- Why this approach comes to mind first: It's the most straightforward way to solve the problem, as it directly simulates the movement of the ball.

```cpp
vector<int> findBall(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    vector<int> result;
    
    for (int j = 0; j < n; j++) {
        int col = j;
        for (int i = 0; i < m; i++) {
            if (grid[i][col] == 1) { // move to the right
                if (col == n - 1 || grid[i][col + 1] == -1) {
                    break; // cannot move further
                }
                col++;
            } else { // move to the left
                if (col == 0 || grid[i][col - 1] == 1) {
                    break; // cannot move further
                }
                col--;
            }
        }
        result.push_back(col);
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns in the grid. This is because we simulate the movement of the ball for each column, and in the worst case, the ball moves through all rows.
> - **Space Complexity:** $O(n)$, where $n$ is the number of columns in the grid. This is because we store the result for each column.
> - **Why these complexities occur:** The time complexity is due to the simulation of the ball's movement for each column, and the space complexity is due to the storage of the results.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of simulating the movement of the ball for each column, we can use a more efficient approach by iterating over the grid row by row and updating the result accordingly.
- Detailed breakdown of the approach:
  1. Initialize a vector `result` to store the column index where each ball falls.
  2. Iterate over each column in the grid.
  3. For each column, iterate over each row in the grid.
  4. At each step, check the direction of the ball and update the column index accordingly.
  5. If the ball reaches the bottom, record the column index where it fell.
- Proof of optimality: This approach is optimal because it has the same time complexity as the brute force approach but is more efficient in practice due to the reduced number of operations.
- Why further optimization is impossible: This approach is already optimal because it has to simulate the movement of the ball for each column, and any further optimization would require a different approach.

```cpp
vector<int> findBall(vector<vector<int>>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    vector<int> result(n, -1);
    
    for (int j = 0; j < n; j++) {
        int col = j;
        bool valid = true;
        for (int i = 0; i < m; i++) {
            if (grid[i][col] == 1) { // move to the right
                if (col == n - 1 || grid[i][col + 1] == -1) {
                    valid = false;
                    break; // cannot move further
                }
                col++;
            } else { // move to the left
                if (col == 0 || grid[i][col - 1] == 1) {
                    valid = false;
                    break; // cannot move further
                }
                col--;
            }
        }
        if (valid) {
            result[j] = col;
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns in the grid. This is because we simulate the movement of the ball for each column, and in the worst case, the ball moves through all rows.
> - **Space Complexity:** $O(n)$, where $n$ is the number of columns in the grid. This is because we store the result for each column.
> - **Optimality proof:** This approach is optimal because it has the same time complexity as the brute force approach but is more efficient in practice due to the reduced number of operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Simulation, iteration, and conditional statements.
- Problem-solving patterns identified: The problem can be solved by simulating the movement of the ball for each column.
- Optimization techniques learned: The optimal approach is more efficient than the brute force approach due to the reduced number of operations.
- Similar problems to practice: Other problems that involve simulation and iteration, such as the "Where Will the Ball Fall?" problem.

**Mistakes to Avoid:**
- Common implementation errors: Not checking the boundaries of the grid, not handling the case where the ball cannot move further.
- Edge cases to watch for: The case where the ball is at the edge of the grid, the case where the ball cannot move further.
- Performance pitfalls: Using an inefficient algorithm that has a high time complexity.
- Testing considerations: Testing the function with different inputs, including edge cases, to ensure that it works correctly.