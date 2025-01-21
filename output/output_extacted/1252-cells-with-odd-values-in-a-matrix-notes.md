## Cells with Odd Values in a Matrix

**Problem Link:** https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/description

**Problem Statement:**
- Input format and constraints: Given a matrix `n x m` and `k` operations, each operation is represented as a `row` and a `col` where we flip all cells in the row and column.
- Expected output format: The number of cells with odd values after performing all operations.
- Key requirements and edge cases to consider: The initial matrix contains all zeros, and a cell is flipped if it is in the same row or column as the given operation.
- Example test cases with explanations:
  - `n = 2, m = 3, indices = [[0,1],[1,1]]`: The initial matrix is `[[0,0,0],[0,0,0]]`. After flipping the cells at `(0,1)` and `(1,1)`, the resulting matrix is `[[0,1,0],[0,1,0]]`. The number of cells with odd values is `2`.
  - `n = 2, m = 2, indices = [[0,0],[1,1]]`: The initial matrix is `[[0,0],[0,0]]`. After flipping the cells at `(0,0)` and `(1,1)`, the resulting matrix is `[[1,0],[0,1]]`. The number of cells with odd values is `2`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Create a matrix of size `n x m` and initialize it with zeros. Iterate over each operation and flip the corresponding row and column.
- Step-by-step breakdown of the solution:
  1. Create a matrix of size `n x m` and initialize it with zeros.
  2. Iterate over each operation.
  3. For each operation, flip the corresponding row and column.
  4. After all operations, count the number of cells with odd values.
- Why this approach comes to mind first: It is a straightforward approach that directly simulates the problem statement.

```cpp
#include <vector>

int oddCells(int n, int m, std::vector<std::vector<int>>& indices) {
    std::vector<std::vector<int>> matrix(n, std::vector<int>(m, 0));
    for (const auto& index : indices) {
        int row = index[0];
        int col = index[1];
        // Flip the row
        for (int i = 0; i < m; i++) {
            matrix[row][i] ^= 1;
        }
        // Flip the column
        for (int i = 0; i < n; i++) {
            matrix[i][col] ^= 1;
        }
    }
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (matrix[i][j] % 2 != 0) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k \cdot (n + m) + n \cdot m)$, where $k$ is the number of operations, $n$ is the number of rows, and $m$ is the number of columns. This is because we iterate over each operation and flip the corresponding row and column, and then count the number of cells with odd values.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of rows and $m$ is the number of columns. This is because we create a matrix of size `n x m`.
> - **Why these complexities occur:** The time complexity occurs because we iterate over each operation and flip the corresponding row and column, and then count the number of cells with odd values. The space complexity occurs because we create a matrix of size `n x m`.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of simulating the flipping of rows and columns, we can count the number of times each row and column is flipped. If a row or column is flipped an odd number of times, all cells in that row or column will have an odd value.
- Detailed breakdown of the approach:
  1. Initialize two arrays, `rows` and `cols`, of size `n` and `m`, respectively, to keep track of the number of times each row and column is flipped.
  2. Iterate over each operation and increment the corresponding row and column in `rows` and `cols`.
  3. Count the number of cells with odd values by iterating over `rows` and `cols`.
- Proof of optimality: This approach is optimal because it avoids simulating the flipping of rows and columns, which reduces the time complexity from $O(k \cdot (n + m) + n \cdot m)$ to $O(k + n + m)$.

```cpp
int oddCells(int n, int m, std::vector<std::vector<int>>& indices) {
    std::vector<int> rows(n, 0);
    std::vector<int> cols(m, 0);
    for (const auto& index : indices) {
        rows[index[0]]++;
        cols[index[1]]++;
    }
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if ((rows[i] + cols[j]) % 2 != 0) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k + n \cdot m)$, where $k$ is the number of operations, $n$ is the number of rows, and $m$ is the number of columns. This is because we iterate over each operation and increment the corresponding row and column, and then count the number of cells with odd values.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of rows and $m$ is the number of columns. This is because we create two arrays, `rows` and `cols`, of size `n` and `m`, respectively.
> - **Optimality proof:** This approach is optimal because it avoids simulating the flipping of rows and columns, which reduces the time complexity from $O(k \cdot (n + m) + n \cdot m)$ to $O(k + n \cdot m)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Counting, iteration, and modular arithmetic.
- Problem-solving patterns identified: Instead of simulating the problem, count the number of times each row and column is flipped.
- Optimization techniques learned: Avoid simulating the problem and use counting instead.
- Similar problems to practice: Problems that involve counting and iteration, such as `Count of Smaller Numbers After Self` and `K-Diff Pairs in an Array`.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize arrays or variables, and not checking for edge cases.
- Edge cases to watch for: When the number of rows or columns is zero, and when the number of operations is zero.
- Performance pitfalls: Simulating the problem instead of using counting, and using unnecessary data structures.
- Testing considerations: Test the function with different inputs, including edge cases, to ensure it works correctly.