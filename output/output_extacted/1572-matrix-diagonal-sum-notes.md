## Matrix Diagonal Sum

**Problem Link:** https://leetcode.com/problems/matrix-diagonal-sum/description

**Problem Statement:**
- Input: A `matrix` which is a 2D array of integers.
- Constraints: `1 <= matrix.length <= 100`, `1 <= matrix[i].length <= 100`, `matrix[i].length == matrix[1].length`, `1 <= matrix[i][j] <= 10^4`.
- Expected Output: The sum of all the elements on the diagonals of the matrix.
- Key Requirements: Identify and sum all the elements that are on the primary and secondary diagonals of the matrix.
- Edge Cases: Consider cases where the matrix is a square (has the same number of rows and columns), and where it is not.

---

### Brute Force Approach

**Explanation:**
- Initial thought process is to iterate over each element in the matrix.
- Step-by-step breakdown involves checking each element to see if it lies on either of the diagonals.
- This approach comes to mind first because it involves a straightforward iteration over the matrix without needing to consider any complex properties of the diagonals.

```cpp
int diagonalSum(vector<vector<int>>& matrix) {
    int sum = 0;
    int n = matrix.size();
    // Iterate over each element in the matrix
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            // Check if the element is on the primary diagonal (i == j)
            // or the secondary diagonal (i + j == n - 1)
            if (i == j || i + j == n - 1) {
                sum += matrix[i][j];
            }
        }
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of rows (or columns) in the matrix. This is because we are potentially checking every element in the matrix once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store our variables, regardless of the input size.
> - **Why these complexities occur:** The time complexity is quadratic because of the nested loop structure, and the space complexity is constant because we do not allocate any additional data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to the optimal solution is recognizing that we only need to iterate over the rows (or columns) of the matrix once, checking for elements on both diagonals in a single pass.
- Detailed breakdown involves iterating over the rows and for each row, adding the elements at the current row index and at the mirrored index from the end.
- This approach is optimal because it minimizes the number of iterations and directly targets the elements of interest without unnecessary checks.

```cpp
int diagonalSum(vector<vector<int>>& matrix) {
    int sum = 0;
    int n = matrix.size();
    // Iterate over the rows of the matrix
    for (int i = 0; i < n; i++) {
        // Add the element on the primary diagonal
        sum += matrix[i][i];
        // Add the element on the secondary diagonal, avoiding double-counting the middle element in square matrices
        if (i != n - i - 1) {
            sum += matrix[i][n - i - 1];
        }
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows (or columns) in the matrix. This is because we make a single pass through the rows.
> - **Space Complexity:** $O(1)$, as we still only use a constant amount of space.
> - **Optimality proof:** This is the best possible time complexity because we must at least look at each diagonal element once to sum them, and we do so in a single pass.

---

### Final Notes

**Learning Points:**
- Key algorithmic concept demonstrated is the importance of recognizing patterns in the problem that allow for efficient iteration and reduction of unnecessary checks.
- Problem-solving pattern identified is the use of a single pass through the data to collect all necessary information, minimizing complexity.
- Optimization technique learned is to directly target the elements of interest and avoid iterating over the entire dataset when possible.
- Similar problems to practice include other matrix or array traversal problems where efficient iteration is key.

**Mistakes to Avoid:**
- Common implementation error is not correctly handling the case where the matrix is a square and the middle element is counted twice.
- Edge case to watch for is ensuring the solution works for both square and non-square matrices.
- Performance pitfall is using nested loops when a single pass is sufficient, leading to unnecessary complexity.
- Testing consideration is to thoroughly test the solution with matrices of varying sizes and shapes.