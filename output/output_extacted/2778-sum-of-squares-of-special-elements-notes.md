## Sum of Squares of Special Elements
**Problem Link:** https://leetcode.com/problems/sum-of-squares-of-special-elements/description

**Problem Statement:**
- Input: A 2D array `mat` of integers, where each element represents a value in a matrix.
- Constraints: The input matrix is non-empty and has dimensions `m x n`.
- Expected Output: The sum of the squares of the special elements in the matrix. A special element is an element that is the minimum element in its row or the maximum element in its column.
- Key Requirements and Edge Cases:
  - The matrix can have any number of rows and columns.
  - The matrix can contain duplicate values.
  - The matrix can contain negative numbers.
- Example Test Cases:
  - Input: `mat = [[1,2,3],[4,5,6]]`
    - Output: `25`
    - Explanation: The special elements are `1` (minimum in row 1), `3` (maximum in column 3), `4` (minimum in row 2), and `6` (maximum in column 3). The sum of their squares is `1^2 + 3^2 + 4^2 + 6^2 = 1 + 9 + 16 + 36 = 62`.
  - Input: `mat = [[7,7,7]]`
    - Output: `49`
    - Explanation: The special element is `7` (minimum and maximum in row 1 and column 1). The sum of its square is `7^2 = 49`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate over each element in the matrix, check if it's the minimum in its row or the maximum in its column, and if so, add its square to the sum.
- This approach comes to mind first because it directly checks each element against the conditions for being a special element.

```cpp
int specialElementsSum(vector<vector<int>>& mat) {
    int sum = 0;
    int m = mat.size();
    int n = mat[0].size();
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            bool isMinInRow = true;
            bool isMaxInCol = true;
            
            // Check if current element is the minimum in its row
            for (int k = 0; k < n; k++) {
                if (mat[i][k] < mat[i][j]) {
                    isMinInRow = false;
                    break;
                }
            }
            
            // Check if current element is the maximum in its column
            for (int k = 0; k < m; k++) {
                if (mat[k][j] > mat[i][j]) {
                    isMaxInCol = false;
                    break;
                }
            }
            
            // If the current element is the minimum in its row or the maximum in its column, add its square to the sum
            if (isMinInRow || isMaxInCol) {
                sum += mat[i][j] * mat[i][j];
            }
        }
    }
    
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot (m + n))$ because for each element, we potentially check every other element in its row and column.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space to store the sum and indices.
> - **Why these complexities occur:** The time complexity is high because we have nested loops that check each element against every other element in its row and column. The space complexity is low because we don't use any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to first find the minimum of each row and the maximum of each column, then iterate over the matrix to find elements that match these minima or maxima.
- This approach is optimal because it reduces the number of comparisons needed to identify special elements.

```cpp
int specialElementsSum(vector<vector<int>>& mat) {
    int sum = 0;
    int m = mat.size();
    int n = mat[0].size();
    vector<int> rowMins(m, INT_MAX);
    vector<int> colMaxs(n, INT_MIN);
    
    // Find the minimum of each row and the maximum of each column
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            rowMins[i] = min(rowMins[i], mat[i][j]);
            colMaxs[j] = max(colMaxs[j], mat[i][j]);
        }
    }
    
    // Iterate over the matrix to find elements that are the minimum in their row or the maximum in their column
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (mat[i][j] == rowMins[i] || mat[i][j] == colMaxs[j]) {
                sum += mat[i][j] * mat[i][j];
            }
        }
    }
    
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$ because we make two passes over the matrix: one to find row minima and column maxima, and another to identify special elements.
> - **Space Complexity:** $O(m + n)$ for storing the row minima and column maxima.
> - **Optimality proof:** This approach is optimal because it only requires two passes over the matrix, and each pass is necessary to identify special elements efficiently. Further optimization is impossible without reducing the number of passes over the matrix.

---

### Final Notes

**Learning Points:**
- The importance of identifying special elements in a matrix based on row and column properties.
- How to optimize a brute force approach by reducing the number of comparisons needed.
- The use of auxiliary arrays to store row minima and column maxima for efficient lookup.

**Mistakes to Avoid:**
- Not considering the possibility of duplicate values in the matrix.
- Failing to handle edge cases such as a matrix with a single row or column.
- Not optimizing the brute force approach, leading to inefficient solutions.