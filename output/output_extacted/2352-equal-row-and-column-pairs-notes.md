## Equal Row and Column Pairs
**Problem Link:** https://leetcode.com/problems/equal-row-and-column-pairs/description

**Problem Statement:**
- Input format and constraints: Given a 0-indexed `n x n` matrix `grid`, return the number of pairs of rows and columns that are equal.
- Expected output format: The number of pairs of equal rows and columns.
- Key requirements and edge cases to consider: The input matrix is guaranteed to be a square matrix, but there may be duplicate rows or columns.
- Example test cases with explanations:
  - For a 3x3 matrix with all elements being the same, there would be 9 pairs (each row with each column).
  - For a matrix with distinct rows and columns, there would be `n` pairs (each row with its corresponding column).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Compare each row with each column to check for equality.
- Step-by-step breakdown of the solution:
  1. Iterate through each row in the matrix.
  2. For each row, iterate through each column in the matrix.
  3. Compare the elements of the current row with the elements of the current column.
  4. If all elements match, increment the count of equal pairs.
- Why this approach comes to mind first: It's the most straightforward way to compare rows and columns.

```cpp
int equalPairs(vector<vector<int>>& grid) {
    int n = grid.size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            bool match = true;
            for (int k = 0; k < n; k++) {
                if (grid[i][k] != grid[k][j]) {
                    match = false;
                    break;
                }
            }
            if (match) count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of rows (or columns) in the grid. This is because for each row, we iterate through each column, and for each pair, we compare $n$ elements.
> - **Space Complexity:** $O(1)$, excluding the input grid, since we only use a constant amount of space to store the count and indices.
> - **Why these complexities occur:** The cubic time complexity comes from the nested loops that compare each element of each row with each element of each column.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of comparing rows and columns element by element, we can create a set of rows and a set of columns. Then, we compare the sets directly to find matches.
- Detailed breakdown of the approach:
  1. Create a set of strings representing the rows.
  2. Create a set of strings representing the columns.
  3. Initialize a count variable to 0.
  4. Iterate through each row in the set of rows.
  5. For each row, construct a string representing the column that would match this row.
  6. Check if this column string exists in the set of columns. If it does, increment the count.
- Proof of optimality: This approach is optimal because it reduces the comparison to a set lookup, which is $O(1)$ on average, leading to an overall time complexity of $O(n^2)$.

```cpp
int equalPairs(vector<vector<int>>& grid) {
    int n = grid.size();
    unordered_set<string> rows, cols;
    for (int i = 0; i < n; i++) {
        string row, col;
        for (int j = 0; j < n; j++) {
            row += to_string(grid[i][j]) + ",";
            col += to_string(grid[j][i]) + ",";
        }
        rows.insert(row);
        cols.insert(col);
    }
    int count = 0;
    for (auto row : rows) {
        if (cols.find(row) != cols.end()) {
            count += rows.count(row) * cols.count(row);
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of rows (or columns) in the grid. This is because we construct the sets of rows and columns in $O(n^2)$ time and then perform set lookups.
> - **Space Complexity:** $O(n^2)$, for storing the sets of rows and columns.
> - **Optimality proof:** The quadratic time complexity is optimal because we must at least read the input once, and the set operations allow us to count the matches efficiently.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Set operations, string manipulation for efficient comparison.
- Problem-solving patterns identified: Reducing complex comparisons to set lookups.
- Optimization techniques learned: Using data structures to reduce comparison complexity.
- Similar problems to practice: Other problems involving set operations and string manipulation for efficient comparisons.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling the construction of the row and column strings, or miscounting the matches.
- Edge cases to watch for: Duplicate rows or columns, and ensuring that the comparison is done correctly.
- Performance pitfalls: Using inefficient data structures or algorithms that lead to higher time complexities.
- Testing considerations: Thoroughly testing with different input sizes and edge cases to ensure correctness and performance.