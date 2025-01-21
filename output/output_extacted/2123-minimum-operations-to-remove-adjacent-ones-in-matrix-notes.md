## Minimum Operations to Remove Adjacent Ones in Matrix

**Problem Link:** https://leetcode.com/problems/minimum-operations-to-remove-adjacent-ones-in-matrix/description

**Problem Statement:**
- Input: A binary matrix `mat` of size `m x n`.
- Constraints: `1 <= m, n <= 10^5`, `mat[i][j]` is either `0` or `1`.
- Expected Output: The minimum number of operations to remove all adjacent ones in the matrix.
- Key Requirements: 
  - An operation consists of choosing any cell in the matrix and changing its value to `0`.
  - Two cells are considered adjacent if they share an edge (not diagonally).
- Edge Cases: 
  - If the matrix is empty, return `0`.
  - If the matrix contains no adjacent ones, return `0`.

**Example Test Cases:**
- Input: `mat = [[1,0,0],[0,1,0],[0,0,1]]`, Output: `0` because there are no adjacent ones.
- Input: `mat = [[1,1,0],[0,1,0],[0,0,1]]`, Output: `1` because we can remove one of the adjacent ones.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every cell in the matrix for adjacent ones.
- For each cell, we check its neighbors (up, down, left, right) to see if any of them are also `1`.
- If we find adjacent ones, we increment our operation count and mark one of the adjacent cells as `0` to remove the adjacency.

```cpp
int minOperations(vector<vector<int>>& mat) {
    int m = mat.size();
    int n = mat[0].size();
    int operations = 0;

    // Iterate over each cell in the matrix
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            // Check neighbors for adjacent ones
            if (mat[i][j] == 1) {
                // Check up
                if (i > 0 && mat[i-1][j] == 1) operations++;
                // Check down
                if (i < m - 1 && mat[i+1][j] == 1) operations++;
                // Check left
                if (j > 0 && mat[i][j-1] == 1) operations++;
                // Check right
                if (j < n - 1 && mat[i][j+1] == 1) operations++;
            }
        }
    }
    return operations;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns in the matrix. This is because we are potentially checking every cell in the matrix once.
> - **Space Complexity:** $O(1)$, not counting the space needed for the input matrix, because we are only using a constant amount of space to store our operation count.
> - **Why these complexities occur:** The time complexity is linear with respect to the size of the input matrix because we are iterating over each cell once. The space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach

**Explanation:**
- The key insight to the optimal solution is to recognize that we only need to count each pair of adjacent ones once.
- We can achieve this by only checking the neighbors of each cell in one direction (e.g., only check up and left for each cell).
- This approach ensures that each pair of adjacent ones is counted exactly once, minimizing the number of operations needed.

```cpp
int minOperations(vector<vector<int>>& mat) {
    int m = mat.size();
    int n = mat[0].size();
    int operations = 0;

    // Iterate over each cell in the matrix
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            // Check up and left for adjacent ones
            if (mat[i][j] == 1) {
                // Check up
                if (i > 0 && mat[i-1][j] == 1) operations++;
                // Check left
                if (j > 0 && mat[i][j-1] == 1) operations++;
            }
        }
    }
    return operations;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns in the matrix. This is because we are potentially checking every cell in the matrix once.
> - **Space Complexity:** $O(1)$, not counting the space needed for the input matrix, because we are only using a constant amount of space to store our operation count.
> - **Optimality proof:** This approach is optimal because it counts each pair of adjacent ones exactly once, which is the minimum number of operations needed to remove all adjacent ones.

---

### Final Notes

**Learning Points:**
- The importance of counting each pair of adjacent ones exactly once to minimize operations.
- How to optimize the brute force approach by reducing the number of checks for each cell.
- The concept of optimizing the iteration to only consider relevant neighbors.

**Mistakes to Avoid:**
- Counting each pair of adjacent ones more than once, which would overestimate the number of operations needed.
- Not considering the boundary conditions correctly, which could lead to incorrect results for cells at the edges of the matrix.
- Failing to optimize the iteration, which could result in unnecessary checks and increased time complexity.