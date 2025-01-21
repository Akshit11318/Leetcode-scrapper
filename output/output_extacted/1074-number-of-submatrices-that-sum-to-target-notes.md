## Number of Submatrices That Sum to Target

**Problem Link:** https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/description

**Problem Statement:**
- Input: A 2D array `matrix` and an integer `target`.
- Output: The number of submatrices that sum to `target`.
- Constraints: `1 <= matrix.length <= 100`, `1 <= matrix[0].length <= 100`, `-1000 <= matrix[i][j] <= 1000`, `target` is an integer.
- Expected output format: The number of submatrices that sum to `target`.
- Key requirements and edge cases to consider: Handling empty matrices, matrices with a single row or column, and cases where `target` is not present in any submatrix.

**Example Test Cases:**
- `matrix = [[1,-1,-1],[1,2,1],[2,1,-1]], target = 0` returns `8`.
- `matrix = [[0,1,0],[1,1,0],[0,1,0]], target = 0` returns `4`.
- `matrix = [[1,2,3],[4,5,6],[7,8,9]], target = 15` returns `0`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to check every possible submatrix in the given matrix.
- Step-by-step breakdown:
  1. Iterate over each cell in the matrix.
  2. For each cell, consider all possible submatrices that start at this cell.
  3. Calculate the sum of each submatrix.
  4. Check if the sum equals the target.

```cpp
int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target) {
    int count = 0;
    int rows = matrix.size();
    int cols = matrix[0].size();
    
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            for (int k = i; k < rows; k++) {
                for (int l = j; l < cols; l++) {
                    int sum = 0;
                    for (int x = i; x <= k; x++) {
                        for (int y = j; y <= l; y++) {
                            sum += matrix[x][y];
                        }
                    }
                    if (sum == target) {
                        count++;
                    }
                }
            }
        }
    }
    
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^4)$, where $n$ is the maximum of the number of rows and columns in the matrix. This is because for each cell, we potentially iterate over all cells in the matrix to form submatrices.
> - **Space Complexity:** $O(1)$, since we only use a constant amount of space to store the count and sum variables.
> - **Why these complexities occur:** The brute force approach checks all possible submatrices, leading to an exponential number of operations with respect to the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a prefix sum array to efficiently calculate the sum of any submatrix in $O(1)$ time.
- Detailed breakdown:
  1. Calculate the prefix sum for the entire matrix.
  2. Iterate over all possible submatrices using two pairs of pointers (top-left and bottom-right corners).
  3. For each submatrix, calculate its sum using the prefix sum array.
  4. Check if the sum equals the target.

```cpp
int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target) {
    int rows = matrix.size();
    int cols = matrix[0].size();
    vector<vector<int>> prefixSum(rows + 1, vector<int>(cols + 1, 0));
    
    // Calculate prefix sum
    for (int i = 1; i <= rows; i++) {
        for (int j = 1; j <= cols; j++) {
            prefixSum[i][j] = prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1] + matrix[i-1][j-1];
        }
    }
    
    int count = 0;
    for (int i = 1; i <= rows; i++) {
        for (int j = 1; j <= cols; j++) {
            for (int k = i; k <= rows; k++) {
                for (int l = j; l <= cols; l++) {
                    int sum = prefixSum[k][l] - prefixSum[k][j-1] - prefixSum[i-1][l] + prefixSum[i-1][j-1];
                    if (sum == target) {
                        count++;
                    }
                }
            }
        }
    }
    
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^4)$, where $n$ is the maximum of the number of rows and columns in the matrix. Although the prefix sum calculation reduces the time to calculate the sum of a submatrix, we still iterate over all possible submatrices.
> - **Space Complexity:** $O(n^2)$, for storing the prefix sum array.
> - **Optimality proof:** This approach is optimal because we must consider all possible submatrices to find those that sum to the target.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Prefix sum arrays for efficient calculation of subarray sums.
- Problem-solving patterns identified: Using prefix sums to reduce the time complexity of calculating subarray sums.
- Optimization techniques learned: Applying prefix sums to avoid redundant calculations.
- Similar problems to practice: Other problems involving subarray or submatrix sums.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating prefix sums or using them to calculate submatrix sums.
- Edge cases to watch for: Empty matrices, matrices with a single row or column, and cases where the target is not present in any submatrix.
- Performance pitfalls: Failing to use prefix sums, leading to inefficient calculation of submatrix sums.
- Testing considerations: Thoroughly testing the solution with various input matrices and targets.