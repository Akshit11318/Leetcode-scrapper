## Spiral Matrix
**Problem Link:** https://leetcode.com/problems/spiral-matrix/description

**Problem Statement:**
- Input format: A 2D vector `matrix` containing integers.
- Constraints: `m == matrix.length`, `n == matrix[0].length`, `1 <= m, n <= 10^3`, `-(10^3) <= matrix[i][j] <= 10^3`.
- Expected output format: A 1D vector `result` containing all elements of the input matrix in spiral order.
- Key requirements and edge cases to consider: Handling empty matrices, matrices with a single row or column, and matrices with an odd or even number of rows and columns.
- Example test cases:
  - `matrix = [[1,2,3],[4,5,6],[7,8,9]]` should return `[1,2,3,6,9,8,7,4,5]`.
  - `matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]` should return `[1,2,3,4,8,12,11,10,9,5,6,7]`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Iterate through each element in the matrix in a spiral order.
- Step-by-step breakdown of the solution:
  1. Initialize four pointers to track the current boundaries of the matrix: `top`, `bottom`, `left`, and `right`.
  2. Initialize an empty vector `result` to store the spiral order of elements.
  3. While the boundaries have not collapsed, iterate through the elements in a spiral order and append them to `result`.
- Why this approach comes to mind first: It directly addresses the problem statement by simulating the spiral traversal process.

```cpp
vector<int> spiralOrder(vector<vector<int>>& matrix) {
    if (matrix.empty()) return {};
    int m = matrix.size(), n = matrix[0].size();
    vector<int> result;
    int top = 0, bottom = m - 1, left = 0, right = n - 1;
    while (top <= bottom && left <= right) {
        // Traverse from left to right
        for (int i = left; i <= right; i++) {
            result.push_back(matrix[top][i]);
        }
        top++;
        
        // Traverse from top to bottom
        for (int i = top; i <= bottom; i++) {
            result.push_back(matrix[i][right]);
        }
        right--;
        
        // Traverse from right to left
        if (top <= bottom) {
            for (int i = right; i >= left; i--) {
                result.push_back(matrix[bottom][i]);
            }
            bottom--;
        }
        
        // Traverse from bottom to top
        if (left <= right) {
            for (int i = bottom; i >= top; i--) {
                result.push_back(matrix[i][left]);
            }
            left++;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the matrix. This is because we visit each element exactly once.
> - **Space Complexity:** $O(m \cdot n)$, as we need to store all elements of the matrix in the `result` vector.
> - **Why these complexities occur:** The brute force approach iterates through the entire matrix, resulting in a linear time complexity with respect to the total number of elements. The space complexity is also linear because we need to store all elements in the output vector.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The same insight as the brute force approach, as the problem requires a straightforward traversal of the matrix in a spiral order.
- Detailed breakdown of the approach: The provided brute force approach is already optimal, as it visits each element exactly once and uses a minimal amount of extra space to store the output.
- Proof of optimality: Any algorithm must visit each element at least once to produce the correct output. Therefore, the time complexity of $O(m \cdot n)$ is optimal. The space complexity of $O(m \cdot n)$ is also optimal, as we need to store all elements in the output vector.

```cpp
// The optimal approach is the same as the brute force approach
vector<int> spiralOrder(vector<vector<int>>& matrix) {
    if (matrix.empty()) return {};
    int m = matrix.size(), n = matrix[0].size();
    vector<int> result;
    int top = 0, bottom = m - 1, left = 0, right = n - 1;
    while (top <= bottom && left <= right) {
        // Traverse from left to right
        for (int i = left; i <= right; i++) {
            result.push_back(matrix[top][i]);
        }
        top++;
        
        // Traverse from top to bottom
        for (int i = top; i <= bottom; i++) {
            result.push_back(matrix[i][right]);
        }
        right--;
        
        // Traverse from right to left
        if (top <= bottom) {
            for (int i = right; i >= left; i--) {
                result.push_back(matrix[bottom][i]);
            }
            bottom--;
        }
        
        // Traverse from bottom to top
        if (left <= right) {
            for (int i = bottom; i >= top; i--) {
                result.push_back(matrix[i][left]);
            }
            left++;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the matrix.
> - **Space Complexity:** $O(m \cdot n)$, as we need to store all elements of the matrix in the `result` vector.
> - **Optimality proof:** The optimal approach has the same time and space complexities as the brute force approach, which are already optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Spiral traversal of a 2D matrix.
- Problem-solving patterns identified: Using boundary pointers to track the current boundaries of the matrix.
- Optimization techniques learned: The optimal approach is already the brute force approach, as it has the minimum possible time and space complexities.
- Similar problems to practice: Other matrix traversal problems, such as rotating a matrix or finding the maximum sum of a submatrix.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for empty matrices or matrices with a single row or column.
- Edge cases to watch for: Matrices with an odd or even number of rows and columns.
- Performance pitfalls: Using unnecessary extra space or iterating through the matrix multiple times.
- Testing considerations: Test the function with different types of matrices, including empty matrices, matrices with a single row or column, and matrices with an odd or even number of rows and columns.