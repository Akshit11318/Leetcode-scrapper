## Count Square Submatrices with All Ones

**Problem Link:** https://leetcode.com/problems/count-square-submatrices-with-all-ones/description

**Problem Statement:**
- Input: A 2D binary matrix `matrix` containing 0s and 1s.
- Output: The number of square submatrices with all ones in the matrix.
- Key requirements: The submatrices must be square (i.e., have the same number of rows and columns) and contain only 1s.
- Edge cases: Empty matrix, matrix with only one row or column, matrix with no 1s.

**Example Test Cases:**
- `matrix = [[0,1,1,1],[1,1,1,1],[0,1,1,1]]` should return `15` because there are 15 square submatrices with all ones.
- `matrix = [[1,0,1],[1,1,0],[1,1,0]]` should return `7` because there are 7 square submatrices with all ones.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to check every possible square submatrix in the given matrix.
- For each possible square submatrix, we check if all its elements are 1s.
- If a submatrix has all 1s, we increment the count of square submatrices with all ones.

```cpp
class Solution {
public:
    int countSquares(vector<vector<int>>& matrix) {
        int count = 0;
        int rows = matrix.size();
        if (rows == 0) return 0;
        int cols = matrix[0].size();
        
        for (int size = 1; size <= min(rows, cols); size++) {
            for (int i = 0; i <= rows - size; i++) {
                for (int j = 0; j <= cols - size; j++) {
                    bool allOnes = true;
                    for (int x = i; x < i + size; x++) {
                        for (int y = j; y < j + size; y++) {
                            if (matrix[x][y] == 0) {
                                allOnes = false;
                                break;
                            }
                        }
                        if (!allOnes) break;
                    }
                    if (allOnes) count++;
                }
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^4)$, where $n$ is the minimum of the number of rows and columns in the matrix. This is because we are iterating over all possible square submatrices and checking each element in the submatrix.
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with the input size.
> - **Why these complexities occur:** The brute force approach checks every possible submatrix, which results in a high time complexity. However, it does not require any additional space that scales with the input size, so the space complexity is constant.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use dynamic programming to store the number of square submatrices with all ones ending at each cell.
- We can calculate the number of square submatrices with all ones ending at each cell by considering the minimum number of square submatrices with all ones ending at the top, left, and top-left cells.
- This approach allows us to avoid redundant calculations and improve the time complexity.

```cpp
class Solution {
public:
    int countSquares(vector<vector<int>>& matrix) {
        int rows = matrix.size();
        if (rows == 0) return 0;
        int cols = matrix[0].size();
        vector<vector<int>> dp(rows, vector<int>(cols, 0));
        int count = 0;
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (matrix[i][j] == 1) {
                    if (i == 0 || j == 0) {
                        dp[i][j] = 1;
                    } else {
                        dp[i][j] = min(dp[i-1][j], min(dp[i][j-1], dp[i-1][j-1])) + 1;
                    }
                    count += dp[i][j];
                }
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of cells in the matrix. This is because we are iterating over all cells in the matrix once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of cells in the matrix. This is because we are using a 2D array to store the dynamic programming table.
> - **Optimality proof:** This approach is optimal because it has a time complexity of $O(n^2)$, which is the minimum possible time complexity for this problem. The space complexity of $O(n)$ is also optimal because we need to store the dynamic programming table to avoid redundant calculations.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is dynamic programming, which allows us to store and reuse the results of subproblems to improve the time complexity.
- The problem-solving pattern identified is the use of a 2D array to store the dynamic programming table.
- The optimization technique learned is the use of dynamic programming to avoid redundant calculations.

**Mistakes to Avoid:**
- A common implementation error is to forget to initialize the dynamic programming table correctly.
- An edge case to watch for is when the input matrix is empty or has only one row or column.
- A performance pitfall is to use a brute force approach with a high time complexity, which can result in slow performance for large inputs.
- A testing consideration is to test the implementation with different input sizes and edge cases to ensure correctness and performance.