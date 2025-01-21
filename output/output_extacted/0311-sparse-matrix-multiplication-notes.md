## Sparse Matrix Multiplication
**Problem Link:** https://leetcode.com/problems/sparse-matrix-multiplication/description

**Problem Statement:**
- Input format: Two 2D integer arrays `mat1` and `mat2` representing sparse matrices.
- Constraints: `mat1` is an `m x n` matrix, and `mat2` is an `n x p` matrix.
- Expected output format: An `m x p` matrix resulting from the multiplication of `mat1` and `mat2`.
- Key requirements: The matrices are sparse, meaning most of their elements are zero.
- Edge cases to consider: Empty input matrices, matrices with different dimensions that cannot be multiplied.
- Example test cases:
  - `mat1 = [[1,0,0],[-1,0,3]]`, `mat2 = [[7,0,0],[0,0,0],[0,0,1]]`, the output should be `[[7,0,0],[-7,0,3]]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to perform standard matrix multiplication, ignoring the fact that the matrices are sparse.
- Step-by-step breakdown:
  1. Check if the input matrices can be multiplied (i.e., the number of columns in `mat1` equals the number of rows in `mat2`).
  2. Initialize a result matrix filled with zeros, with dimensions `m x p`.
  3. Iterate over each element in the result matrix.
  4. For each element, calculate its value by summing the products of corresponding elements from the rows of `mat1` and the columns of `mat2`.

```cpp
vector<vector<int>> multiply(vector<vector<int>>& mat1, vector<vector<int>>& mat2) {
    int m = mat1.size(), n = mat1[0].size(), p = mat2[0].size();
    vector<vector<int>> res(m, vector<int>(p, 0));
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < p; ++j) {
            for (int k = 0; k < n; ++k) {
                res[i][j] += mat1[i][k] * mat2[k][j];
            }
        }
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot p)$, where $m$, $n$, and $p$ are the dimensions of the matrices.
> - **Space Complexity:** $O(m \cdot p)$ for the result matrix.
> - **Why these complexities occur:** The brute force approach involves iterating over each element in the result matrix and for each element, iterating over the entire row of `mat1` and the entire column of `mat2`, resulting in cubic time complexity. The space complexity comes from storing the result matrix.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to take advantage of the sparsity of the matrices. Instead of iterating over all elements, we can only consider non-zero elements.
- Detailed breakdown:
  1. Check if the input matrices can be multiplied.
  2. Initialize a result matrix filled with zeros.
  3. Iterate over each non-zero element in `mat1`.
  4. For each non-zero element in `mat1`, iterate over each non-zero element in the corresponding column of `mat2`.
  5. Update the result matrix accordingly.

```cpp
vector<vector<int>> multiply(vector<vector<int>>& mat1, vector<vector<int>>& mat2) {
    int m = mat1.size(), n = mat1[0].size(), p = mat2[0].size();
    vector<vector<int>> res(m, vector<int>(p, 0));
    for (int i = 0; i < m; ++i) {
        for (int k = 0; k < n; ++k) {
            if (mat1[i][k] != 0) {
                for (int j = 0; j < p; ++j) {
                    if (mat2[k][j] != 0) {
                        res[i][j] += mat1[i][k] * mat2[k][j];
                    }
                }
            }
        }
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n_z \cdot p_z)$, where $n_z$ is the average number of non-zero elements in a row of `mat1`, and $p_z$ is the average number of non-zero elements in a column of `mat2`.
> - **Space Complexity:** $O(m \cdot p)$ for the result matrix.
> - **Optimality proof:** This approach is optimal because it only considers non-zero elements, minimizing the number of operations required for the multiplication. The time complexity is directly related to the sparsity of the matrices, making it efficient for sparse matrices.

---

### Final Notes

**Learning Points:**
- The importance of considering the properties of the input data (in this case, sparsity) to optimize algorithms.
- How to adapt standard algorithms (like matrix multiplication) to take advantage of specific characteristics of the input.
- The trade-off between time and space complexity in algorithm design.

**Mistakes to Avoid:**
- Not checking the dimensions of the input matrices before attempting multiplication.
- Not handling edge cases, such as empty input matrices.
- Failing to consider the sparsity of the matrices, leading to inefficient algorithms.
- Not validating the input matrices for correct formatting and data types.