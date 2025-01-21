## Toeplitz Matrix

**Problem Link:** https://leetcode.com/problems/toeplitz-matrix/description

**Problem Statement:**
- Input format: A 2D array of integers representing the matrix.
- Constraints: The matrix will have at least 1 row and 1 column.
- Expected output format: A boolean indicating whether the matrix is a Toeplitz matrix.
- Key requirements: A Toeplitz matrix is a matrix in which each descending diagonal from left to right is constant.
- Example test cases:
  - Input: `[[1,2,3,4],[5,1,2,3],[9,5,1,2]]`, Output: `true`
  - Input: `[[1,2],[2,2]]`, Output: `false`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Compare each element with its corresponding element in the next row and previous column.
- Step-by-step breakdown of the solution:
  1. Iterate over each element in the matrix.
  2. For each element, check if the corresponding element in the next row and previous column exists and has the same value.
  3. If any pair of elements does not match, return `false`.
  4. If all elements match, return `true`.

```cpp
class Solution {
public:
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
        int rows = matrix.size();
        int cols = matrix[0].size();
        
        // Iterate over each element in the matrix
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                // Check if the corresponding element in the next row and previous column exists and has the same value
                if (i > 0 && j > 0 && matrix[i][j] != matrix[i - 1][j - 1]) {
                    return false;
                }
            }
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns. This is because we iterate over each element in the matrix once.
> - **Space Complexity:** $O(1)$, which means the space required does not change with the size of the input matrix. This is because we only use a constant amount of space to store the indices and the result.
> - **Why these complexities occur:** The time complexity occurs because we need to check each element in the matrix once. The space complexity occurs because we do not need to store any additional data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same insight as the brute force approach, but we can improve the implementation by directly comparing elements in each diagonal.
- Detailed breakdown of the approach:
  1. Iterate over each element in the first row and first column.
  2. For each element, check the corresponding elements in the diagonals.
  3. If any pair of elements does not match, return `false`.
  4. If all elements match, return `true`.

```cpp
class Solution {
public:
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
        int rows = matrix.size();
        int cols = matrix[0].size();
        
        // Iterate over each element in the first row
        for (int j = 0; j < cols; j++) {
            // Check the corresponding elements in the diagonals
            if (!checkDiagonal(matrix, 0, j)) {
                return false;
            }
        }
        
        // Iterate over each element in the first column
        for (int i = 1; i < rows; i++) {
            // Check the corresponding elements in the diagonals
            if (!checkDiagonal(matrix, i, 0)) {
                return false;
            }
        }
        
        return true;
    }
    
    bool checkDiagonal(vector<vector<int>>& matrix, int i, int j) {
        int rows = matrix.size();
        int cols = matrix[0].size();
        int val = matrix[i][j];
        
        while (i < rows && j < cols) {
            if (matrix[i][j] != val) {
                return false;
            }
            i++;
            j++;
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns. This is because we iterate over each element in the matrix once.
> - **Space Complexity:** $O(1)$, which means the space required does not change with the size of the input matrix. This is because we only use a constant amount of space to store the indices and the result.
> - **Optimality proof:** This is the optimal solution because we need to check each element in the matrix at least once to determine if it is a Toeplitz matrix.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, comparison, and diagonal checking.
- Problem-solving patterns identified: Using a helper function to check the diagonals.
- Optimization techniques learned: Directly comparing elements in each diagonal.
- Similar problems to practice: Checking for symmetric matrices, finding the longest diagonal in a matrix.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for out-of-bounds indices, not handling edge cases.
- Edge cases to watch for: Matrices with only one row or column, matrices with all elements being the same.
- Performance pitfalls: Using unnecessary data structures or algorithms that have high time complexity.
- Testing considerations: Testing with different sizes of matrices, testing with different types of matrices (e.g., symmetric, asymmetric).