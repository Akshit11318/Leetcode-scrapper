## First Completely Painted Row or Column

**Problem Link:** https://leetcode.com/problems/first-completely-painted-row-or-column/description

**Problem Statement:**
- Input: A `m x n` matrix and a list of `length` operations to paint a row or a column.
- Expected Output: The first row or column that is completely painted.
- Key Requirements:
  - Identify the first completely painted row or column.
  - If no row or column is completely painted, return `-1`.
- Edge Cases:
  - An empty matrix or an empty list of operations.
  - Operations that paint outside the matrix bounds.

Example Test Cases:
- Given a `3x4` matrix and operations to paint rows and columns, find the first completely painted row or column.
- If no row or column is completely painted after all operations, return `-1`.

---

### Brute Force Approach

**Explanation:**
- Initialize a `m x n` matrix with all elements set to `0`, representing unpainted cells.
- Iterate through each operation:
  - If the operation paints a row, mark all cells in that row as painted (`1`).
  - If the operation paints a column, mark all cells in that column as painted (`1`).
- After each operation, check all rows and columns to see if any are completely painted.
- Return the index of the first completely painted row or column, or `-1` if none are found.

```cpp
class Solution {
public:
    int firstCompleteRowOrColumn(vector<vector<int>>& matrix, vector<vector<int>>& operations) {
        int m = matrix.size();
        int n = matrix[0].size();
        vector<vector<int>> painted(m, vector<int>(n, 0));
        
        for (auto& op : operations) {
            if (op[0] == 1) { // Paint row
                for (int j = 0; j < n; j++) {
                    painted[op[1]][j] = 1;
                }
            } else { // Paint column
                for (int i = 0; i < m; i++) {
                    painted[i][op[1]] = 1;
                }
            }
            
            // Check rows and columns
            for (int i = 0; i < m; i++) {
                bool rowPainted = true;
                for (int j = 0; j < n; j++) {
                    if (painted[i][j] == 0) {
                        rowPainted = false;
                        break;
                    }
                }
                if (rowPainted) {
                    return i + 1; // Row index is 1-based
                }
            }
            for (int j = 0; j < n; j++) {
                bool colPainted = true;
                for (int i = 0; i < m; i++) {
                    if (painted[i][j] == 0) {
                        colPainted = false;
                        break;
                    }
                }
                if (colPainted) {
                    return -(j + 1); // Column index is negative and 1-based
                }
            }
        }
        
        return -1; // No row or column is completely painted
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot k)$, where $m$ and $n$ are the dimensions of the matrix, and $k$ is the number of operations. Each operation potentially checks all cells in a row or column.
> - **Space Complexity:** $O(m \cdot n)$, for the `painted` matrix.
> - **Why these complexities occur:** The brute force approach checks all cells for each operation, leading to high time complexity. The space complexity is due to the additional matrix to track painted cells.

---

### Optimal Approach (Required)

**Explanation:**
- Instead of checking all rows and columns after each operation, maintain separate counts for each row and column.
- For each operation:
  - If painting a row, increment the count for that row by the number of cells in the row.
  - If painting a column, increment the count for that column by the number of cells in the column.
- After each operation, check the counts to see if any row or column has been completely painted (i.e., its count equals the number of cells in that row or column).
- Return the index of the first completely painted row or column, or `-1` if none are found.

```cpp
class Solution {
public:
    int firstCompleteRowOrColumn(vector<vector<int>>& matrix, vector<vector<int>>& operations) {
        int m = matrix.size();
        int n = matrix[0].size();
        vector<int> rowCounts(m, 0);
        vector<int> colCounts(n, 0);
        
        for (auto& op : operations) {
            if (op[0] == 1) { // Paint row
                rowCounts[op[1]] += n;
            } else { // Paint column
                colCounts[op[1]] += m;
            }
            
            // Check rows and columns
            for (int i = 0; i < m; i++) {
                if (rowCounts[i] == n) {
                    return i + 1; // Row index is 1-based
                }
            }
            for (int j = 0; j < n; j++) {
                if (colCounts[j] == m) {
                    return -(j + 1); // Column index is negative and 1-based
                }
            }
        }
        
        return -1; // No row or column is completely painted
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot k + n \cdot k)$, where $m$ and $n$ are the dimensions of the matrix, and $k$ is the number of operations. Each operation updates a row or column count.
> - **Space Complexity:** $O(m + n)$, for the row and column counts.
> - **Optimality proof:** This approach is optimal because it only checks the counts after each operation, avoiding the need to check all cells. The space complexity is minimal, using only arrays to track row and column counts.

---

### Final Notes

**Learning Points:**
- Maintaining separate counts for rows and columns can significantly reduce the time complexity of the algorithm.
- Checking counts after each operation is more efficient than checking all cells.
- This problem demonstrates the importance of optimizing the algorithm by reducing unnecessary checks.

**Mistakes to Avoid:**
- Failing to consider the dimensions of the matrix when updating row and column counts.
- Not checking for completely painted rows and columns after each operation.
- Using a brute force approach without considering optimizations.