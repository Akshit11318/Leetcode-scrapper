## Spiral Matrix II

**Problem Link:** https://leetcode.com/problems/spiral-matrix-ii/description

**Problem Statement:**
- Input: An integer `n` representing the size of the square matrix.
- Constraints: `1 <= n <= 20`
- Expected Output: A 2D vector representing the `n x n` spiral matrix filled with numbers from 1 to `n * n`.
- Key Requirements: Fill the matrix in a spiral order, starting from the center and moving outwards in a clockwise direction.
- Example Test Cases:
  - Input: `n = 3`
  - Output: `[[1, 2, 3], [8, 9, 4], [7, 6, 5]]`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to simulate the spiral filling process step by step, keeping track of the current position and direction.
- We start at the center of the matrix and fill the numbers in a spiral order, turning right when we reach a boundary or a filled cell.

```cpp
vector<vector<int>> generateMatrix(int n) {
    vector<vector<int>> matrix(n, vector<int>(n, 0));
    int dir[][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}}; // right, down, left, up
    int dirIndex = 0;
    int x = 0, y = 0;
    for (int i = 1; i <= n * n; i++) {
        matrix[x][y] = i;
        int newX = x + dir[dirIndex][0];
        int newY = y + dir[dirIndex][1];
        if (newX < 0 || newX >= n || newY < 0 || newY >= n || matrix[newX][newY] != 0) {
            dirIndex = (dirIndex + 1) % 4;
        }
        x += dir[dirIndex][0];
        y += dir[dirIndex][1];
    }
    return matrix;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the matrix. This is because we fill each cell once.
> - **Space Complexity:** $O(n^2)$, for the space required to store the matrix.
> - **Why these complexities occur:** The time complexity is due to the single pass through the matrix, and the space complexity is due to the storage of the matrix itself.

---

### Optimal Approach (Required)

The above brute force approach is already optimal for this problem, as we need to fill each cell of the matrix once. However, we can slightly improve the code for readability and maintainability.

```cpp
vector<vector<int>> generateMatrix(int n) {
    vector<vector<int>> matrix(n, vector<int>(n, 0));
    vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}}; // right, down, left, up
    int dirIndex = 0;
    int x = 0, y = 0;
    for (int i = 1; i <= n * n; i++) {
        matrix[x][y] = i;
        int newX = x + directions[dirIndex].first;
        int newY = y + directions[dirIndex].second;
        if (newX < 0 || newX >= n || newY < 0 || newY >= n || matrix[newX][newY] != 0) {
            dirIndex = (dirIndex + 1) % 4;
        }
        x += directions[dirIndex].first;
        y += directions[dirIndex].second;
    }
    return matrix;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$
> - **Space Complexity:** $O(n^2)$
> - **Optimality proof:** This is the optimal solution as we need to fill each cell of the matrix once, and we do it in a single pass.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the use of a spiral filling approach to fill the matrix.
- The problem-solving pattern identified is the use of a direction array to keep track of the current direction.
- The optimization technique learned is the use of a single pass through the matrix to fill all cells.

**Mistakes to Avoid:**
- A common implementation error is not checking for boundary conditions when moving to the next cell.
- An edge case to watch for is when the matrix size is 1, in which case the spiral filling process is trivial.
- A performance pitfall is using a recursive approach, which can lead to stack overflow for large matrix sizes.
- A testing consideration is to test the function with different matrix sizes and verify that the output is correct.