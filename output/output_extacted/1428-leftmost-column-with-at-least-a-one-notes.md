## Leftmost Column with at Least a One

**Problem Link:** https://leetcode.com/problems/leftmost-column-with-at-least-a-one/description

**Problem Statement:**
- Input format: A binary matrix `mat` where each row is sorted in ascending order.
- Constraints: The number of rows and columns in the matrix are in the range [1, 100].
- Expected output format: The leftmost column index with at least one 1 in it. If no such column exists, return -1.
- Key requirements and edge cases to consider:
  - Handling an empty matrix or a matrix with no 1s.
  - Ensuring the solution works for matrices of varying sizes.
- Example test cases with explanations:
  - `mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]`, the output should be 2 because the leftmost column with at least a one is the third column.
  - `mat = [[0,0,0,0],[0,0,0,0]]`, the output should be -1 because there is no column with at least a one.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through each column from left to right and check if there's at least one 1 in the column.
- Step-by-step breakdown of the solution:
  1. Iterate through each column index from left to right.
  2. For each column, iterate through each row.
  3. Check if the current cell contains a 1. If it does, return the current column index because we've found the leftmost column with at least a one.
- Why this approach comes to mind first: It's straightforward and ensures we find the leftmost column by checking columns in order from left to right.

```cpp
class Solution {
public:
    int leftMostColumnWithOne(BinaryMatrix &binaryMatrix) {
        int rows = binaryMatrix.numberOfRows();
        int cols = binaryMatrix.numberOfColumns();
        
        for (int col = 0; col < cols; col++) {
            for (int row = 0; row < rows; row++) {
                if (binaryMatrix.get(row, col) == 1) {
                    return col;
                }
            }
        }
        
        return -1; // No column with at least a one found
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$ where $m$ is the number of rows and $n$ is the number of columns. This is because in the worst case, we have to check every cell in the matrix.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input matrix, because we only use a constant amount of space to store the row and column indices.
> - **Why these complexities occur:** The brute force approach checks every cell in the matrix once, leading to a linear time complexity in terms of the total number of cells.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Since each row is sorted, we can use a binary search approach for each row to find the leftmost 1 in that row, but this would still be inefficient for finding the leftmost column across all rows. However, we can take advantage of the fact that we're looking for the leftmost column that has at least one 1 across all rows. We can start from the top-left corner and move right, and if we find a 1, we return the current column. If we don't find a 1 in the current column, we move down to the next row and continue the process in the same column.
- Detailed breakdown of the approach:
  1. Start at the top-right corner of the matrix.
  2. Move left if the current cell is 1, because we want to find the leftmost column with a 1.
  3. Move down if the current cell is 0, because we need to check the next row for a 1 in the current column.
- Proof of optimality: This approach ensures we find the leftmost column with at least a one by always moving towards the left when a 1 is found and only moving down when necessary (i.e., when a 0 is encountered). This minimizes the number of cells we need to check.

```cpp
class Solution {
public:
    int leftMostColumnWithOne(BinaryMatrix &binaryMatrix) {
        int rows = binaryMatrix.numberOfRows();
        int cols = binaryMatrix.numberOfColumns();
        int res = cols; // Initialize result to be out of bounds
        
        for (int row = 0; row < rows; row++) {
            int left = 0, right = cols - 1;
            while (left <= right) {
                int mid = left + (right - left) / 2;
                if (binaryMatrix.get(row, mid) == 1) {
                    res = min(res, mid);
                    right = mid - 1; // Continue searching on the left half
                } else {
                    left = mid + 1; // Continue searching on the right half
                }
            }
        }
        
        return res == cols ? -1 : res; // Return -1 if no column with at least a one is found
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot \log n)$ where $m$ is the number of rows and $n$ is the number of columns. This is because we perform a binary search for each row.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input matrix, because we only use a constant amount of space.
> - **Optimality proof:** This approach is optimal because it minimizes the number of cells that need to be checked by using binary search for each row and keeping track of the leftmost column found so far.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search, optimization by reducing the search space.
- Problem-solving patterns identified: Taking advantage of sorted data to improve efficiency.
- Optimization techniques learned: Using binary search to find the target in a sorted array, minimizing the number of operations by only considering necessary data.
- Similar problems to practice: Other problems involving binary search, sorted matrices, or finding minimum/maximum values in a constrained environment.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly implementing binary search, not handling edge cases properly.
- Edge cases to watch for: Empty matrix, matrix with no 1s, single-row or single-column matrix.
- Performance pitfalls: Using inefficient algorithms for large inputs, not optimizing the search process.
- Testing considerations: Thoroughly testing with different matrix sizes, contents, and edge cases to ensure the solution is robust.