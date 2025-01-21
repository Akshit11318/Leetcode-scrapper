## Range Sum Query 2D - Immutable
**Problem Link:** https://leetcode.com/problems/range-sum-query-2d-immutable/description

**Problem Statement:**
- Input format: A 2D array `matrix` and a query array `nums` where `nums[0]` is the row, `nums[1]` is the column, `nums[2]` is the row end, and `nums[3]` is the column end.
- Constraints: The input matrix will be a non-empty 2D array of size `m x n` where `1 <= m, n <= 100`. The query will be a 2D array of size `1 x 4` where `0 <= row1 <= row2 < m` and `0 <= col1 <= col2 < n`.
- Expected output format: The sum of all elements in the sub-matrix defined by the query.
- Key requirements and edge cases to consider: The input matrix is immutable, meaning it cannot be modified after initialization. The query may overlap with previous queries or not.
- Example test cases with explanations:
  - `matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]` and `nums = [2,1,4,3]` returns `8`.
  - `matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]` and `nums = [1,1,2,2]` returns `11`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each query, iterate through the sub-matrix defined by the query and sum up all the elements.
- Step-by-step breakdown of the solution:
  1. Define a function to calculate the sum of a sub-matrix given the top-left and bottom-right coordinates.
  2. In the function, iterate through each element in the sub-matrix and add it to the sum.
- Why this approach comes to mind first: It directly addresses the problem by summing the elements in the specified range.

```cpp
class NumMatrix {
public:
    vector<vector<int>> matrix;
    NumMatrix(vector<vector<int>>& matrix) {
        this->matrix = matrix;
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        int sum = 0;
        for (int i = row1; i <= row2; i++) {
            for (int j = col1; j <= col2; j++) {
                sum += matrix[i][j];
            }
        }
        return sum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$ where $m$ and $n$ are the number of rows and columns in the sub-matrix, respectively. This occurs because we iterate through each element in the sub-matrix.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space to store the sum and loop variables.
> - **Why these complexities occur:** The time complexity is high because we re-calculate the sum for each query, and the space complexity is low because we don't use any additional data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Pre-calculate the prefix sum of the entire matrix, which allows us to calculate the sum of any sub-matrix in constant time.
- Detailed breakdown of the approach:
  1. Initialize a prefix sum matrix `prefixSum` of the same size as the input matrix.
  2. Calculate the prefix sum for each element in the matrix, where `prefixSum[i][j]` is the sum of all elements in the sub-matrix from the top-left corner to `(i, j)`.
  3. Define a function to calculate the sum of a sub-matrix given the top-left and bottom-right coordinates using the prefix sum matrix.
- Proof of optimality: This approach is optimal because it reduces the time complexity of calculating the sum of a sub-matrix from $O(m \cdot n)$ to $O(1)$.

```cpp
class NumMatrix {
public:
    vector<vector<int>> prefixSum;
    NumMatrix(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        prefixSum.resize(m + 1, vector<int>(n + 1, 0));
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                prefixSum[i][j] = prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1] + matrix[i-1][j-1];
            }
        }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        return prefixSum[row2+1][col2+1] - prefixSum[row1][col2+1] - prefixSum[row2+1][col1] + prefixSum[row1][col1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for calculating the sum of a sub-matrix, and $O(m \cdot n)$ for initializing the prefix sum matrix.
> - **Space Complexity:** $O(m \cdot n)$ for storing the prefix sum matrix.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity of calculating the sum of a sub-matrix to constant time, and the space complexity is necessary to store the prefix sum matrix.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Prefix sum, dynamic programming.
- Problem-solving patterns identified: Using a prefix sum matrix to reduce the time complexity of calculating the sum of a sub-matrix.
- Optimization techniques learned: Pre-calculating the prefix sum matrix to reduce the time complexity of subsequent queries.
- Similar problems to practice: Range Sum Query, Range Sum Query - Mutable.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize the prefix sum matrix, incorrectly calculating the prefix sum.
- Edge cases to watch for: Handling queries with overlapping or non-overlapping sub-matrices.
- Performance pitfalls: Using a brute force approach that re-calculates the sum for each query.
- Testing considerations: Testing with different input sizes and query ranges to ensure the solution is correct and efficient.