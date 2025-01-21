## Set Matrix Zeroes

**Problem Link:** [https://leetcode.com/problems/set-matrix-zeroes/description](https://leetcode.com/problems/set-matrix-zeroes/description)

**Problem Statement:**
- Given an `m x n` matrix, if an element is `0`, set its entire row and column to `0`. Do this in-place.
- Input format and constraints: The input is a 2D vector `matrix` of size `m x n`, where `m` and `n` are integers and `0 <= m, n <= 200`.
- Expected output format: The function should modify the input matrix in-place.
- Key requirements and edge cases to consider:
  - Handle the case when the input matrix is empty.
  - Handle the case when the input matrix contains only one row or column.
- Example test cases with explanations:
  - For the input `[[1,1,1],[1,0,1],[1,1,1]]`, the output should be `[[1,0,1],[0,0,0],[1,0,1]]`.
  - For the input `[[0,1,2,0],[3,4,5,2],[1,3,1,5]]`, the output should be `[[0,0,0,0],[0,4,5,0],[0,3,1,0]]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward approach is to iterate over the matrix, and whenever we encounter a `0`, we mark its entire row and column as `0`.
- Step-by-step breakdown of the solution:
  1. Create two additional matrices of the same size as the input matrix to keep track of rows and columns that need to be set to `0`.
  2. Iterate over the input matrix. Whenever a `0` is encountered, mark the corresponding row and column in the tracking matrices.
  3. Iterate over the tracking matrices and set the rows and columns marked for zeroing to `0` in the original matrix.

```cpp
void setZeroes(vector<vector<int>>& matrix) {
    int m = matrix.size();
    if (m == 0) return;
    int n = matrix[0].size();
    vector<vector<bool>> rows(m, vector<bool>(1, false));
    vector<vector<bool>> cols(n, vector<bool>(1, false));

    // Mark rows and columns that need to be zeroed
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (matrix[i][j] == 0) {
                rows[i][0] = true;
                cols[j][0] = true;
            }
        }
    }

    // Zero out marked rows and columns
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (rows[i][0] || cols[j][0]) {
                matrix[i][j] = 0;
            }
        }
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$ because we are iterating over the matrix twice: once to mark rows and columns for zeroing, and once to actually zero them out.
> - **Space Complexity:** $O(m + n)$ for the additional space needed to store the tracking matrices.
> - **Why these complexities occur:** The time complexity is linear with respect to the size of the input matrix because we are performing a constant amount of work for each element. The space complexity is also linear with respect to the dimensions of the matrix because we need to store tracking information for each row and column.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of using additional matrices to track rows and columns, we can use the first row and column of the input matrix itself to store this information.
- Detailed breakdown of the approach:
  1. Initialize two flags to track if the first row and column should be zeroed out.
  2. Iterate over the matrix (excluding the first row and column), and whenever a `0` is encountered, mark the corresponding row and column in the first row and column of the matrix.
  3. Iterate over the matrix again (excluding the first row and column), and set the rows and columns marked for zeroing to `0`.
  4. Finally, if the flags indicate that the first row and/or column should be zeroed, do so.
- Proof of optimality: This solution has the same time complexity as the brute force approach but reduces the space complexity to $O(1)$, making it optimal in terms of space usage.

```cpp
void setZeroes(vector<vector<int>>& matrix) {
    int m = matrix.size();
    if (m == 0) return;
    int n = matrix[0].size();
    bool isCol = false;

    for (int i = 0; i < m; i++) {
        // Check if the first column needs to be zeroed
        if (matrix[i][0] == 0) {
            isCol = true;
        }
        for (int j = 1; j < n; j++) {
            if (matrix[i][j] == 0) {
                matrix[i][0] = 0; // Mark row
                matrix[0][j] = 0; // Mark column
            }
        }
    }

    // Zero out marked rows and columns
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                matrix[i][j] = 0;
            }
        }
    }

    // Handle first row
    if (matrix[0][0] == 0) {
        for (int j = 0; j < n; j++) {
            matrix[0][j] = 0;
        }
    }

    // Handle first column
    if (isCol) {
        for (int i = 0; i < m; i++) {
            matrix[i][0] = 0;
        }
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, as we are still iterating over the matrix a constant number of times.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the flags for the first row and column, and we are reusing the first row and column of the input matrix for tracking.
> - **Optimality proof:** This solution is optimal because it achieves the best possible time complexity for this problem (since we must at least read the input once) and reduces the space complexity to a constant, which is the minimum possible space usage for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: In-place modification, using part of the input to store additional information.
- Problem-solving patterns identified: Reducing space complexity by reusing existing data structures.
- Optimization techniques learned: Minimizing additional space usage by leveraging the input itself for tracking purposes.
- Similar problems to practice: Other problems that involve in-place modification and clever use of existing data structures.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle edge cases (e.g., empty matrix, matrix with a single row or column).
- Edge cases to watch for: Matrices with all rows or columns needing to be zeroed, matrices with no rows or columns needing to be zeroed.
- Performance pitfalls: Using unnecessary additional space, failing to optimize the solution for the given constraints.
- Testing considerations: Thoroughly testing the solution with various input sizes and scenarios to ensure correctness and efficiency.