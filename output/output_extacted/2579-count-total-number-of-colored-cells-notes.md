## Count Total Number of Colored Cells

**Problem Link:** https://leetcode.com/problems/count-total-number-of-colored-cells/description

**Problem Statement:**
- Input format and constraints: The problem takes an integer `n` as input, representing the number of rows and columns in the grid.
- Expected output format: The function should return the total number of colored cells in the grid.
- Key requirements and edge cases to consider: The grid is colored in a specific pattern where the cell at position `(i, j)` is colored if `i + j` is even.
- Example test cases with explanations:
  - For `n = 3`, the grid will be:
    ```
    1 0 1
    0 1 0
    1 0 1
    ```
    The total number of colored cells is 5.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward approach is to create a grid of size `n x n` and then iterate over each cell. For each cell, we check if the sum of its row and column indices is even. If it is, we increment the count of colored cells.
- Step-by-step breakdown of the solution:
  1. Create a grid of size `n x n`.
  2. Initialize a variable `count` to store the number of colored cells.
  3. Iterate over each cell in the grid.
  4. For each cell, check if the sum of its row and column indices is even.
  5. If the sum is even, increment the `count`.
  6. Return the total count of colored cells.

```cpp
int coloredCells(int n) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if ((i + j) % 2 == 0) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of rows and columns in the grid. This is because we are iterating over each cell in the grid.
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with the input size.
> - **Why these complexities occur:** The time complexity is quadratic because we are iterating over each cell in the grid. The space complexity is constant because we are only using a fixed amount of space to store the count of colored cells.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can observe that the pattern of colored cells is symmetrical and periodic. Specifically, the pattern repeats every two rows and two columns. This means that we can calculate the number of colored cells in a smaller sub-grid and then scale it up to the full grid size.
- Detailed breakdown of the approach:
  1. Calculate the number of colored cells in a single row.
  2. Since the pattern repeats every two rows, we can multiply the number of colored cells in a single row by `n / 2` to get the total number of colored cells in the grid.
  3. However, if `n` is odd, we need to add the number of colored cells in the middle row.
- Proof of optimality: This approach is optimal because it takes advantage of the periodic nature of the pattern, allowing us to calculate the number of colored cells in a much smaller sub-grid and then scale it up.

```cpp
int coloredCells(int n) {
    if (n % 2 == 0) {
        return n * n / 2;
    } else {
        return n * n / 2 + (n + 1) / 2;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, as we are only performing a constant number of operations.
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with the input size.
> - **Optimality proof:** This approach is optimal because it takes advantage of the periodic nature of the pattern, allowing us to calculate the number of colored cells in a much smaller sub-grid and then scale it up. This reduces the time complexity from $O(n^2)$ to $O(1)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the importance of observing patterns and symmetries in the input data. By taking advantage of these patterns, we can often reduce the time complexity of the solution.
- Problem-solving patterns identified: The problem illustrates the use of mathematical insights to simplify the solution. By recognizing the periodic nature of the pattern, we can calculate the number of colored cells in a much smaller sub-grid and then scale it up.
- Optimization techniques learned: The problem demonstrates the use of mathematical insights to optimize the solution. By recognizing the periodic nature of the pattern, we can reduce the time complexity from $O(n^2)$ to $O(1)$.

**Mistakes to Avoid:**
- Common implementation errors: One common mistake is to use a brute force approach without considering the periodic nature of the pattern. This can lead to a solution with a high time complexity.
- Edge cases to watch for: The problem requires handling edge cases where `n` is odd or even. Failing to consider these edge cases can lead to incorrect results.
- Performance pitfalls: The problem requires avoiding performance pitfalls such as using a brute force approach with a high time complexity. This can lead to slow performance for large input sizes.
- Testing considerations: The problem requires testing the solution with different input sizes and edge cases to ensure that it produces the correct results.