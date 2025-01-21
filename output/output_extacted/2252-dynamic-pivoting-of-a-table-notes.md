## Dynamic Pivoting of a Table

**Problem Link:** https://leetcode.com/problems/dynamic-pivoting-of-a-table/description

**Problem Statement:**
- Input format and constraints: The input is a 2D vector `table` representing the table, and two integers `row` and `col` representing the row and column indices to pivot.
- Expected output format: The output is the pivoted table.
- Key requirements and edge cases to consider: The pivot operation should be performed in-place, and the table should be modified accordingly.
- Example test cases with explanations:
  - Test case 1: `table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`, `row = 1`, `col = 1`. Expected output: `[[4, 2, 6], [1, 5, 3], [7, 8, 9]]`.
  - Test case 2: `table = [[1, 2], [3, 4]]`, `row = 0`, `col = 0`. Expected output: `[[3, 2], [1, 4]]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves creating a new table and manually swapping the elements according to the pivot operation.
- Step-by-step breakdown of the solution:
  1. Create a new table with the same dimensions as the input table.
  2. Iterate over the input table and swap the elements according to the pivot operation.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it has high time and space complexity.

```cpp
void pivotTable(vector<vector<int>>& table, int row, int col) {
    int n = table.size();
    int m = table[0].size();
    vector<vector<int>> newTable(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (i == row && j == col) {
                newTable[i][j] = table[row][col];
            } else if (i == row) {
                newTable[i][j] = table[row][m - 1 - j];
            } else if (j == col) {
                newTable[i][j] = table[n - 1 - i][col];
            } else {
                newTable[i][j] = table[n - 1 - i][m - 1 - j];
            }
        }
    }
    table = newTable;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ and $m$ are the dimensions of the table.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ and $m$ are the dimensions of the table.
> - **Why these complexities occur:** The brute force approach involves creating a new table and manually swapping the elements, which requires $O(n \cdot m)$ time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The pivot operation can be performed in-place by swapping the elements in a specific order.
- Detailed breakdown of the approach:
  1. Swap the elements in the pivot row with the corresponding elements in the last row.
  2. Swap the elements in the pivot column with the corresponding elements in the last column.
- Proof of optimality: This approach has a time complexity of $O(n + m)$, which is optimal because we need to access each element at least once to perform the pivot operation.
- Why further optimization is impossible: This approach has the minimum possible time complexity because it only requires accessing each element once.

```cpp
void pivotTable(vector<vector<int>>& table, int row, int col) {
    int n = table.size();
    int m = table[0].size();
    // Swap the elements in the pivot row with the corresponding elements in the last row
    for (int j = 0; j < m; j++) {
        swap(table[row][j], table[n - 1 - row][j]);
    }
    // Swap the elements in the pivot column with the corresponding elements in the last column
    for (int i = 0; i < n; i++) {
        if (i != row) {
            swap(table[i][col], table[i][m - 1 - col]);
        }
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ and $m$ are the dimensions of the table.
> - **Space Complexity:** $O(1)$, because the pivot operation is performed in-place.
> - **Optimality proof:** This approach has the minimum possible time complexity because it only requires accessing each element once to perform the pivot operation.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: In-place pivot operation, swapping elements in a specific order.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems, using symmetry to reduce the number of operations.
- Optimization techniques learned: Reducing the number of operations by using in-place swapping, minimizing the number of accesses to each element.
- Similar problems to practice: Other pivot operations, such as rotating a matrix by 90 degrees.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, such as when the pivot row or column is the first or last row/column.
- Edge cases to watch for: When the pivot row or column is the first or last row/column, when the table has only one row or column.
- Performance pitfalls: Using a brute force approach with high time and space complexity.
- Testing considerations: Testing the function with different input sizes, testing the function with different pivot rows and columns.