## Sum of Matrix After Queries
**Problem Link:** https://leetcode.com/problems/sum-of-matrix-after-queries/description

**Problem Statement:**
- Input format and constraints: Given a `m x n` matrix `mat` and an array of queries `queries`, where each query is an array `[row, col, val]`. For each query, add `val` to all cells in the row `row` and column `col` (including `mat[row][col]`). Then, return the sum of all elements in the matrix.
- Expected output format: The sum of all elements in the matrix after applying all queries.
- Key requirements and edge cases to consider: 
    - The input matrix `mat` will have a size between `1` and `1000`.
    - The input array `queries` will have a length between `1` and `1000`.
    - The values in `mat` and `queries` will be between `0` and `100`.
- Example test cases with explanations:
    - For `mat = [[1,1,1],[1,1,1],[1,1,1]]` and `queries = [[0,0,2],[1,1,3]]`, the output should be `28`. The first query adds `2` to all cells in row `0` and column `0`, resulting in `mat = [[3,3,1],[1,1,1],[1,1,1]]`. The second query adds `3` to all cells in row `1` and column `1`, resulting in `mat = [[3,3,1],[1,4,1],[1,1,1]]`. The sum of all elements in the matrix is then `3 + 3 + 1 + 1 + 4 + 1 + 1 + 1 + 1 = 16 + 12 = 28`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward approach is to apply each query to the matrix and then calculate the sum of all elements in the matrix.
- Step-by-step breakdown of the solution:
    1. Initialize a copy of the input matrix `mat` to store the result of each query.
    2. For each query in the `queries` array, iterate over each row and column in the matrix and add the value `val` to the corresponding cells.
    3. After applying all queries, calculate the sum of all elements in the matrix.
- Why this approach comes to mind first: This approach directly implements the problem description and is easy to understand.

```cpp
class Solution {
public:
    int matrixSum(vector<vector<int>>& mat, vector<vector<int>>& queries) {
        int m = mat.size();
        int n = mat[0].size();
        
        // Apply each query to the matrix
        for (auto& query : queries) {
            int row = query[0];
            int col = query[1];
            int val = query[2];
            
            // Add val to all cells in the row and column
            for (int i = 0; i < m; i++) {
                mat[i][col] += val;
            }
            for (int j = 0; j < n; j++) {
                mat[row][j] += val;
            }
            // Subtract val from mat[row][col] since it was added twice
            mat[row][col] -= val;
        }
        
        // Calculate the sum of all elements in the matrix
        int sum = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                sum += mat[i][j];
            }
        }
        
        return sum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(q \cdot (m + n))$, where $q$ is the number of queries, $m$ is the number of rows in the matrix, and $n$ is the number of columns in the matrix. This is because for each query, we iterate over all rows and columns in the matrix.
> - **Space Complexity:** $O(1)$, since we modify the input matrix in-place.
> - **Why these complexities occur:** The time complexity occurs because we apply each query to the matrix, which involves iterating over all rows and columns in the matrix. The space complexity occurs because we modify the input matrix in-place, without using any additional data structures.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can calculate the sum of all elements in the matrix without actually applying each query to the matrix. Instead, we can maintain a running sum of the values added to each row and column.
- Detailed breakdown of the approach:
    1. Initialize the sum of all elements in the matrix to `0`.
    2. For each query in the `queries` array, add the value `val` to the sum of all elements in the row and column.
    3. After applying all queries, calculate the final sum of all elements in the matrix.
- Proof of optimality: This approach is optimal because it avoids the overhead of actually applying each query to the matrix, which reduces the time complexity.

```cpp
class Solution {
public:
    int matrixSum(vector<vector<int>>& mat, vector<vector<int>>& queries) {
        int m = mat.size();
        int n = mat[0].size();
        
        // Initialize the sum of all elements in the matrix
        int sum = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                sum += mat[i][j];
            }
        }
        
        // Apply each query to the sum
        for (auto& query : queries) {
            int row = query[0];
            int col = query[1];
            int val = query[2];
            
            // Add val to the sum of all elements in the row and column
            sum += val * (m + n - 1);
        }
        
        return sum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n + q)$, where $m$ is the number of rows in the matrix, $n$ is the number of columns in the matrix, and $q$ is the number of queries. This is because we initialize the sum of all elements in the matrix and then apply each query to the sum.
> - **Space Complexity:** $O(1)$, since we only use a constant amount of space to store the sum.
> - **Optimality proof:** This approach is optimal because it avoids the overhead of actually applying each query to the matrix, which reduces the time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: 
    - **_Dynamic Programming_**: We maintain a running sum of the values added to each row and column, which avoids the overhead of actually applying each query to the matrix.
    - **_Optimization_**: We reduce the time complexity by avoiding unnecessary work.
- Problem-solving patterns identified: 
    - **_Query-based problems_**: We often need to apply a series of queries to a data structure and then calculate some property of the resulting data structure.
- Optimization techniques learned: 
    - **_Avoiding unnecessary work_**: We avoid applying each query to the matrix, which reduces the time complexity.
- Similar problems to practice: 
    - **_Range Sum Query 2D_**: Given a 2D array and a series of range sum queries, calculate the sum of all elements in the specified ranges.

**Mistakes to Avoid:**
- Common implementation errors: 
    - **_Incorrect indexing_**: Make sure to use the correct indices when accessing the matrix.
    - **_Off-by-one errors_**: Make sure to handle the edges of the matrix correctly.
- Edge cases to watch for: 
    - **_Empty matrix_**: Make sure to handle the case where the matrix is empty.
    - **_No queries_**: Make sure to handle the case where there are no queries.
- Performance pitfalls: 
    - **_Using unnecessary data structures_**: Make sure to use the minimum amount of data structures necessary to solve the problem.
    - **_Applying queries unnecessarily_**: Make sure to avoid applying queries unnecessarily, which can reduce the time complexity.