## Spiral Matrix III
**Problem Link:** https://leetcode.com/problems/spiral-matrix-iii/description

**Problem Statement:**
- Input format and constraints: The problem takes in three parameters: `rows`, `cols`, and `r0`, `c0`, representing the number of rows and columns in the matrix and the starting position of the spiral, respectively.
- Expected output format: The function should return a vector of pairs, where each pair represents the coordinates of a cell in the spiral order.
- Key requirements and edge cases to consider: The spiral should start from the top-left corner and move clockwise. The input values of `rows`, `cols`, `r0`, and `c0` are guaranteed to be non-negative.
- Example test cases with explanations:
  - For `rows = 5`, `cols = 6`, `r0 = 1`, and `c0 = 4`, the output should be `[[0,2],[0,3],[0,4],[3,4],[3,5],[3,2],[2,2],[1,2],[2,0],[2,1],[1,1],[2,3],[1,3],[0,1],[0,0],[0,4],[3,3],[1,4],[3,1],[2,5],[1,5],[3,0]]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over the entire matrix in a spiral order. We can achieve this by maintaining four pointers to represent the boundaries of the matrix and moving them inward as we fill the cells.
- Step-by-step breakdown of the solution:
  1. Initialize the result vector and the four pointers (`top`, `bottom`, `left`, and `right`) to the boundaries of the matrix.
  2. Start from the top-left corner and move right, then down, then left, and finally up, filling the cells in the spiral order.
  3. After each iteration, move the corresponding pointer inward.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, as it involves simple iterations and pointer updates.

```cpp
vector<vector<int>> spiralMatrixIII(int rows, int cols, int r0, int c0) {
    vector<vector<int>> result;
    result.reserve(rows * cols); // Preallocate space for the result vector
    int top = r0, bottom = r0, left = c0, right = c0;
    int steps = 1; // Number of steps to move in the current direction
    int direction = 0; // Current direction (0: right, 1: down, 2: left, 3: up)
    while (result.size() < rows * cols) {
        for (int i = 0; i < steps; ++i) {
            if (direction == 0) { // Move right
                if (left <= right && top >= 0 && top < rows && left >= 0 && left < cols) {
                    result.push_back({top, left});
                }
                left++;
            } else if (direction == 1) { // Move down
                if (top <= bottom && left >= 0 && left < cols && top >= 0 && top < rows) {
                    result.push_back({top, left});
                }
                top++;
            } else if (direction == 2) { // Move left
                if (right >= left && bottom >= 0 && bottom < rows && right >= 0 && right < cols) {
                    result.push_back({bottom, right});
                }
                right--;
            } else if (direction == 3) { // Move up
                if (bottom >= top && right >= 0 && right < cols && bottom >= 0 && bottom < rows) {
                    result.push_back({bottom, right});
                }
                bottom--;
            }
        }
        direction = (direction + 1) % 4; // Update direction
        if (direction % 2 == 0) { // Increase the number of steps every two directions
            steps++;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(rows \times cols)$, as we visit each cell in the matrix once.
> - **Space Complexity:** $O(rows \times cols)$, as we store the coordinates of all cells in the result vector.
> - **Why these complexities occur:** The time complexity is linear with respect to the total number of cells, as we perform a constant amount of work for each cell. The space complexity is also linear, as we store the coordinates of all cells.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using the same spiral iteration approach as the brute force solution. However, we can optimize the code by removing redundant checks and using more efficient data structures.
- Detailed breakdown of the approach:
  1. Initialize the result vector and the four pointers (`top`, `bottom`, `left`, and `right`) to the boundaries of the matrix.
  2. Start from the top-left corner and move right, then down, then left, and finally up, filling the cells in the spiral order.
  3. After each iteration, move the corresponding pointer inward.
- Proof of optimality: The time complexity of this approach is optimal, as we must visit each cell in the matrix at least once to fill it in the spiral order.

```cpp
vector<vector<int>> spiralMatrixIII(int rows, int cols, int r0, int c0) {
    vector<vector<int>> result;
    result.reserve(rows * cols); // Preallocate space for the result vector
    int top = r0, bottom = r0, left = c0, right = c0;
    int steps = 1; // Number of steps to move in the current direction
    int direction = 0; // Current direction (0: right, 1: down, 2: left, 3: up)
    while (result.size() < rows * cols) {
        for (int i = 0; i < steps; ++i) {
            if (direction == 0) { // Move right
                if (left < cols && top >= 0 && top < rows) {
                    result.push_back({top, left});
                }
                left++;
            } else if (direction == 1) { // Move down
                if (top < rows && left >= 0 && left < cols) {
                    result.push_back({top, left});
                }
                top++;
            } else if (direction == 2) { // Move left
                if (right >= 0 && bottom >= 0 && bottom < rows) {
                    result.push_back({bottom, right});
                }
                right--;
            } else if (direction == 3) { // Move up
                if (bottom >= 0 && right >= 0 && right < cols) {
                    result.push_back({bottom, right});
                }
                bottom--;
            }
        }
        direction = (direction + 1) % 4; // Update direction
        if (direction % 2 == 0) { // Increase the number of steps every two directions
            steps++;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(rows \times cols)$, as we visit each cell in the matrix once.
> - **Space Complexity:** $O(rows \times cols)$, as we store the coordinates of all cells in the result vector.
> - **Optimality proof:** The time complexity is optimal, as we must visit each cell in the matrix at least once to fill it in the spiral order. The space complexity is also optimal, as we must store the coordinates of all cells in the result vector.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Spiral iteration, boundary updates, and direction changes.
- Problem-solving patterns identified: Using a brute force approach as a starting point and optimizing it to achieve the optimal solution.
- Optimization techniques learned: Removing redundant checks, using efficient data structures, and preallocating space for the result vector.
- Similar problems to practice: Other spiral iteration problems, such as generating a spiral matrix or finding the spiral order of a matrix.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to update the direction or steps, or not checking the boundaries of the matrix.
- Edge cases to watch for: Handling cases where the input values are zero or negative.
- Performance pitfalls: Using inefficient data structures or algorithms that result in high time or space complexities.
- Testing considerations: Thoroughly testing the solution with different input values and edge cases to ensure correctness.