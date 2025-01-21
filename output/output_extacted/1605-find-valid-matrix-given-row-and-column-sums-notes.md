## Find Valid Matrix Given Row and Column Sums

**Problem Link:** [https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/description](https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/description)

**Problem Statement:**
- Input format and constraints: Given two arrays `rowSum` and `colSum` of length `m` and `n` respectively, find a `m x n` matrix `mat` where `mat[i][j]` equals to `rowSum[i]` and `colSum[j]`. 
- Expected output format: Return the matrix `mat`.
- Key requirements and edge cases to consider: The sum of each row in the matrix should be equal to the corresponding element in `rowSum`, and the sum of each column in the matrix should be equal to the corresponding element in `colSum`.
- Example test cases with explanations: For example, if `rowSum = [3,8]` and `colSum = [4,7,6,8]`, the output should be `[[3,0,0,0],[0,1,2,5]]`.

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to try all possible combinations of numbers in the matrix and check if the sum of each row and column matches the given arrays.
- Step-by-step breakdown of the solution: 
    1. Initialize an empty matrix with the given dimensions.
    2. Try all possible combinations of numbers in the matrix.
    3. For each combination, check if the sum of each row and column matches the given arrays.
    4. If a match is found, return the matrix.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it is not efficient because it has a high time complexity.

```cpp
using namespace std;

vector<vector<int>> restoreMatrix(vector<int>& rowSum, vector<int>& colSum) {
    int m = rowSum.size();
    int n = colSum.size();
    vector<vector<int>> mat(m, vector<int>(n, 0));
    
    function<bool(int, int)> dfs = [&](int i, int j) {
        if (i == m) return true;
        if (j == n) return dfs(i + 1, 0);
        
        for (int k = 0; k <= min(rowSum[i], colSum[j]); k++) {
            mat[i][j] = k;
            if (rowSum[i] - k >= 0 && colSum[j] - k >= 0) {
                rowSum[i] -= k;
                colSum[j] -= k;
                if (dfs(i, j + 1)) return true;
                rowSum[i] += k;
                colSum[j] += k;
            }
        }
        return false;
    };
    
    if (!dfs(0, 0)) return {};
    return mat;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{m \cdot n})$ because in the worst case, we have to try all possible combinations of numbers in the matrix.
> - **Space Complexity:** $O(m \cdot n)$ for the space needed to store the matrix.
> - **Why these complexities occur:** These complexities occur because we are trying all possible combinations of numbers in the matrix, which results in a high time complexity.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a greedy approach to fill the matrix. For each cell, we can fill it with the minimum of the remaining sum of the row and the remaining sum of the column.
- Detailed breakdown of the approach: 
    1. Initialize an empty matrix with the given dimensions.
    2. For each cell in the matrix, fill it with the minimum of the remaining sum of the row and the remaining sum of the column.
    3. Update the remaining sum of the row and the column after filling each cell.
- Proof of optimality: This approach is optimal because it ensures that the sum of each row and column is equal to the given arrays, and it does so in a way that minimizes the number of operations.

```cpp
using namespace std;

vector<vector<int>> restoreMatrix(vector<int>& rowSum, vector<int>& colSum) {
    int m = rowSum.size();
    int n = colSum.size();
    vector<vector<int>> mat(m, vector<int>(n, 0));
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            mat[i][j] = min(rowSum[i], colSum[j]);
            rowSum[i] -= mat[i][j];
            colSum[j] -= mat[i][j];
        }
    }
    
    return mat;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$ because we are filling each cell in the matrix once.
> - **Space Complexity:** $O(m \cdot n)$ for the space needed to store the matrix.
> - **Optimality proof:** This approach is optimal because it ensures that the sum of each row and column is equal to the given arrays, and it does so in a way that minimizes the number of operations.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy approach, matrix operations.
- Problem-solving patterns identified: Filling a matrix with given row and column sums.
- Optimization techniques learned: Using a greedy approach to minimize the number of operations.
- Similar problems to practice: Other problems that involve filling a matrix with given constraints.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the remaining sum of the row and column after filling each cell.
- Edge cases to watch for: Handling cases where the given row and column sums are not valid.
- Performance pitfalls: Using a brute force approach instead of a greedy approach.
- Testing considerations: Testing the solution with different inputs to ensure it works correctly.