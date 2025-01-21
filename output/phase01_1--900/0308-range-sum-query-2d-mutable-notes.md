## Range Sum Query 2D - Mutable

**Problem Link:** [https://leetcode.com/problems/range-sum-query-2d-mutable/description](https://leetcode.com/problems/range-sum-query-2d-mutable/description)

**Problem Statement:**
- Input: A 2D matrix `matrix` and a list of operations where each operation can be either a `sumRegion` query or an `update` operation.
- Constraints: The number of rows and columns in the matrix are fixed and known beforehand.
- Expected Output: For `sumRegion` queries, return the sum of all elements in the specified region. For `update` operations, update the value at the specified cell.
- Key Requirements and Edge Cases:
  - Handle both `sumRegion` and `update` operations efficiently.
  - The `sumRegion` query should be able to handle any rectangular region within the matrix.
  - The `update` operation should be able to update any cell in the matrix.
- Example Test Cases:
  - Initialize a matrix with values and perform `sumRegion` queries and `update` operations to verify the correctness of the solution.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to simply iterate through the specified region for `sumRegion` queries and sum up all the elements.
- For `update` operations, directly update the value at the specified cell.
- This approach comes to mind first because it directly addresses the problem statement without considering optimization.

```cpp
class NumMatrix {
public:
    vector<vector<int>> matrix;
    NumMatrix(vector<vector<int>>& matrix) {
        this->matrix = matrix;
    }
    
    void update(int row, int col, int val) {
        matrix[row][col] = val;
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
> - **Time Complexity:** $O(m \cdot n)$ for the `sumRegion` query where $m$ and $n$ are the number of rows and columns in the query region, respectively. $O(1)$ for the `update` operation.
> - **Space Complexity:** $O(m \cdot n)$ for storing the matrix, where $m$ and $n$ are the dimensions of the input matrix.
> - **Why these complexities occur:** The brute force approach requires iterating over the entire query region for `sumRegion` queries, leading to a time complexity proportional to the size of the region. The `update` operation only accesses a single cell, hence its constant time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a prefix sum array (also known as a cumulative sum array) to store the sum of all elements in the region from the top-left corner to each cell.
- This allows for efficient calculation of the sum of any rectangular region by subtracting the sums of the regions outside the desired area.
- For `update` operations, update the prefix sum array accordingly to maintain its correctness.

```cpp
class NumMatrix {
private:
    vector<vector<int>> prefixSum;
public:
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
    
    void update(int row, int col, int val) {
        int diff = val - getCell(row, col);
        updatePrefixSum(row + 1, col + 1, diff);
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        return getRegionSum(row1 + 1, col1 + 1, row2 + 1, col2 + 1);
    }
    
    int getCell(int row, int col) {
        return getRegionSum(row + 1, col + 1, row + 1, col + 1);
    }
    
    void updatePrefixSum(int row, int col, int diff) {
        int m = prefixSum.size();
        int n = prefixSum[0].size();
        
        for (int i = row; i < m; i++) {
            for (int j = col; j < n; j++) {
                prefixSum[i][j] += diff;
            }
        }
    }
    
    int getRegionSum(int row1, int col1, int row2, int col2) {
        return prefixSum[row2][col2] - prefixSum[row2][col1 - 1] - prefixSum[row1 - 1][col2] + prefixSum[row1 - 1][col1 - 1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for `update` operations and $O(1)$ for `sumRegion` queries because we can calculate the sum of any region in constant time using the prefix sum array.
> - **Space Complexity:** $O(m \cdot n)$ for the prefix sum array, where $m$ and $n$ are the dimensions of the input matrix.
> - **Optimality proof:** This approach is optimal because it achieves the best possible time complexity for both `update` and `sumRegion` operations using the prefix sum array, which allows for constant time queries and updates.

---

### Final Notes

**Learning Points:**
- The use of prefix sum arrays for efficient range sum queries.
- How to update a prefix sum array when the underlying data changes.
- The importance of choosing the right data structure for the problem at hand.

**Mistakes to Avoid:**
- Not considering the update operation's impact on the prefix sum array.
- Failing to handle edge cases, such as queries or updates outside the bounds of the matrix.
- Not optimizing the solution for the specific requirements of the problem, leading to inefficient solutions.