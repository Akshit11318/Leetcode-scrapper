## Matrix Block Sum
**Problem Link:** https://leetcode.com/problems/matrix-block-sum/description

**Problem Statement:**
- Input format: A 2D array `mat` of integers, and an integer `k`.
- Constraints: `1 <= mat.length <= 100`, `1 <= mat[0].length <= 100`, `1 <= k <= 100`, and `-1000 <= mat[i][j] <= 1000`.
- Expected output format: A 2D array where each element at position `(i, j)` is the sum of all elements in the `k x k` sub-matrix that has its top left corner at `(i - k + 1, j - k + 1)`.
- Key requirements and edge cases to consider: Handling out-of-bounds indices, ensuring the sub-matrix is fully contained within the original matrix.
- Example test cases with explanations: For example, given `mat = [[1,2,3],[4,5,6],[7,8,9]]` and `k = 1`, the output should be `[[12,21,16],[27,45,33],[24,39,28]]`, which are the sums of the `1x1`, `2x2`, and `3x3` sub-matrices respectively.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, one might initially think to iterate over each cell in the matrix and for each cell, calculate the sum of the `k x k` sub-matrix centered at that cell.
- Step-by-step breakdown of the solution:
  1. Iterate over each cell `(i, j)` in the matrix.
  2. For each cell, calculate the sum of the `k x k` sub-matrix by iterating over the range `(i - k + 1, i + k)` and `(j - k + 1, j + k)`.
  3. If the sub-matrix goes out of bounds, adjust the range to stay within the matrix bounds.
  4. Store the sum in the result matrix at position `(i, j)`.

```cpp
vector<vector<int>> matrixBlockSum(vector<vector<int>>& mat, int k) {
    int m = mat.size();
    int n = mat[0].size();
    vector<vector<int>> result(m, vector<int>(n, 0));
    
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            int sum = 0;
            int rowStart = max(0, i - k + 1);
            int rowEnd = min(m - 1, i + k - 1);
            int colStart = max(0, j - k + 1);
            int colEnd = min(n - 1, j + k - 1);
            
            for (int x = rowStart; x <= rowEnd; ++x) {
                for (int y = colStart; y <= colEnd; ++y) {
                    sum += mat[x][y];
                }
            }
            result[i][j] = sum;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot k^2)$, where $m$ is the number of rows, $n$ is the number of columns, and $k$ is the size of the sub-matrix. This is because for each cell, we potentially iterate over a `k x k` sub-matrix.
> - **Space Complexity:** $O(m \cdot n)$, as we need to store the result in a matrix of the same size as the input.
> - **Why these complexities occur:** The brute force approach has high time complexity because it involves nested loops for each cell, leading to quadratic complexity in terms of `k`. The space complexity is linear with respect to the input size because we only need to store the result matrix.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of recalculating the sum for each cell, we can use a prefix sum array (also known as a cumulative sum array) to store the sum of all elements in the sub-matrix in constant time.
- Detailed breakdown of the approach:
  1. Calculate the prefix sum array for the entire matrix.
  2. For each cell, use the prefix sum array to calculate the sum of the `k x k` sub-matrix in constant time.
  3. Store the sum in the result matrix at position `(i, j)`.

```cpp
vector<vector<int>> matrixBlockSum(vector<vector<int>>& mat, int k) {
    int m = mat.size();
    int n = mat[0].size();
    vector<vector<int>> prefixSum(m + 1, vector<int>(n + 1, 0));
    vector<vector<int>> result(m, vector<int>(n, 0));
    
    // Calculate prefix sum
    for (int i = 1; i <= m; ++i) {
        for (int j = 1; j <= n; ++j) {
            prefixSum[i][j] = prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1] + mat[i-1][j-1];
        }
    }
    
    // Calculate sum for each cell using prefix sum
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            int rowStart = max(0, i - k + 1);
            int rowEnd = min(m - 1, i + k - 1);
            int colStart = max(0, j - k + 1);
            int colEnd = min(n - 1, j + k - 1);
            
            int sum = prefixSum[rowEnd+1][colEnd+1] - prefixSum[rowEnd+1][colStart] - prefixSum[rowStart][colEnd+1] + prefixSum[rowStart][colStart];
            result[i][j] = sum;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m` is the number of rows and `n` is the number of columns. This is because we calculate the prefix sum array once and then use it to calculate the sum for each cell in constant time.
> - **Space Complexity:** $O(m \cdot n)$, as we need to store the prefix sum array and the result matrix.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity from $O(m \cdot n \cdot k^2)$ to $O(m \cdot n)$, which is the minimum required to iterate over each cell in the matrix.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Prefix sum array, cumulative sum.
- Problem-solving patterns identified: Using prefix sum to reduce time complexity.
- Optimization techniques learned: Avoiding redundant calculations by using precomputed values.
- Similar problems to practice: Other problems involving prefix sum arrays, such as range sum queries.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating the prefix sum array, failing to handle edge cases.
- Edge cases to watch for: Out-of-bounds indices, zero-sized sub-matrices.
- Performance pitfalls: Recalculating sums for each cell instead of using a prefix sum array.
- Testing considerations: Thoroughly testing the solution with different input sizes and edge cases.