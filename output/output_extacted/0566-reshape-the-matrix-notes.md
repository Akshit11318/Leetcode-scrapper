## Reshape the Matrix
**Problem Link:** https://leetcode.com/problems/reshape-the-matrix/description

**Problem Statement:**
- Input format and constraints: The input is a 2D vector `nums` representing the matrix and two integers `r` and `c` representing the number of rows and columns in the reshaped matrix. The constraints are that `r` and `c` must be positive integers and `r * c` must equal the total number of elements in `nums`.
- Expected output format: The output is a 2D vector representing the reshaped matrix.
- Key requirements and edge cases to consider: The reshaped matrix must have `r` rows and `c` columns, and the elements must be filled in row-major order.
- Example test cases with explanations:
  - Input: `nums = [[1,2],[3,4]]`, `r = 1`, `c = 4`
    Output: `[[1,2,3,4]]`
  - Input: `nums = [[1,2],[3,4]]`, `r = 2`, `c = 2`
    Output: `[[1,2],[3,4]]`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The first approach that comes to mind is to iterate through the input matrix and manually copy the elements into a new matrix with the desired shape.
- Step-by-step breakdown of the solution:
  1. Calculate the total number of elements in the input matrix.
  2. Check if the reshaped matrix has the same total number of elements.
  3. Initialize a new matrix with the desired shape.
  4. Iterate through the input matrix and copy the elements into the new matrix in row-major order.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it may not be the most efficient solution.

```cpp
vector<vector<int>> matrixReshape(vector<vector<int>>& nums, int r, int c) {
    int rows = nums.size();
    int cols = nums[0].size();
    if (rows * cols != r * c) return nums;
    vector<vector<int>> reshaped(r, vector<int>(c));
    int index = 0;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            reshaped[index / c][index % c] = nums[i][j];
            index++;
        }
    }
    return reshaped;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the number of rows and columns in the input matrix, respectively. This is because we iterate through the entire input matrix once.
> - **Space Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the number of rows and columns in the input matrix, respectively. This is because we create a new matrix with the same total number of elements.
> - **Why these complexities occur:** The time complexity occurs because we iterate through the entire input matrix, and the space complexity occurs because we create a new matrix with the same total number of elements.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is to use a single loop to iterate through the input matrix and copy the elements into the new matrix in row-major order.
- Detailed breakdown of the approach:
  1. Calculate the total number of elements in the input matrix.
  2. Check if the reshaped matrix has the same total number of elements.
  3. Initialize a new matrix with the desired shape.
  4. Use a single loop to iterate through the input matrix and copy the elements into the new matrix in row-major order.
- Proof of optimality: This solution is optimal because it only requires a single loop to iterate through the input matrix, and it does not require any additional data structures or operations.
- Why further optimization is impossible: Further optimization is impossible because we must iterate through the entire input matrix to copy the elements into the new matrix.

```cpp
vector<vector<int>> matrixReshape(vector<vector<int>>& nums, int r, int c) {
    int rows = nums.size();
    int cols = nums[0].size();
    if (rows * cols != r * c) return nums;
    vector<vector<int>> reshaped(r, vector<int>(c));
    int index = 0;
    for (int i = 0; i < rows * cols; i++) {
        reshaped[index / c][index % c] = nums[i / cols][i % cols];
        index++;
    }
    return reshaped;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the number of rows and columns in the input matrix, respectively. This is because we iterate through the entire input matrix once.
> - **Space Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the number of rows and columns in the input matrix, respectively. This is because we create a new matrix with the same total number of elements.
> - **Optimality proof:** This solution is optimal because it only requires a single loop to iterate through the input matrix, and it does not require any additional data structures or operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, indexing, and matrix manipulation.
- Problem-solving patterns identified: Using a single loop to iterate through a matrix and copying elements into a new matrix.
- Optimization techniques learned: Eliminating unnecessary loops and data structures.
- Similar problems to practice: Matrix rotation, matrix transpose, and matrix multiplication.

**Mistakes to Avoid:**
- Common implementation errors: Off-by-one errors, incorrect indexing, and incorrect matrix initialization.
- Edge cases to watch for: Empty input matrix, invalid input dimensions, and non-rectangular input matrix.
- Performance pitfalls: Using unnecessary loops or data structures, and not checking for edge cases.
- Testing considerations: Test with different input sizes, shapes, and edge cases to ensure correctness and performance.