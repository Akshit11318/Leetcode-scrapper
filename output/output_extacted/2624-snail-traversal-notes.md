## Snail Traversal

**Problem Link:** https://leetcode.com/problems/snail-traversal/description

**Problem Statement:**
- Input: A 2D `matrix` of integers.
- Constraints: `matrix` is a non-empty 2D array with dimensions `m x n`, where `m` and `n` are between 1 and 10,000 (inclusive), and `m * n` is less than or equal to 10,000.
- Expected output: Return the elements of the `matrix` in a snail traversal order (starting from the top left, moving right, then down, then left, then up, repeating the pattern until all elements are visited).
- Key requirements and edge cases to consider:
  - Handling matrices of varying sizes.
  - Correctly traversing the matrix in the specified order.
- Example test cases with explanations:
  - For a 3x3 matrix, the output should follow the snail pattern, starting from the top left and moving right, then down, then left, then up.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One might start by thinking of manually iterating through each cell in the specified order, keeping track of the current position and direction.
- Step-by-step breakdown of the solution:
  1. Initialize the current position at the top left corner of the matrix.
  2. Set the initial direction to move right.
  3. Iterate through the matrix, moving in the current direction until a boundary is reached or a cell that has already been visited is encountered.
  4. When a boundary or a visited cell is encountered, change the direction (e.g., from right to down, from down to left, from left to up, and from up to right).
  5. Repeat steps 3 and 4 until all cells have been visited.

```cpp
#include <vector>

std::vector<int> snailTraversal(std::vector<std::vector<int>>& matrix) {
    if (matrix.empty() || matrix[0].empty()) return {};
    
    int rows = matrix.size();
    int cols = matrix[0].size();
    std::vector<int> result;
    std::vector<std::vector<bool>> visited(rows, std::vector<bool>(cols, false));
    
    int row = 0, col = 0;
    std::vector<std::pair<int, int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}}; // right, down, left, up
    int dirIndex = 0;
    
    for (int i = 0; i < rows * cols; ++i) {
        result.push_back(matrix[row][col]);
        visited[row][col] = true;
        
        int nextRow = row + directions[dirIndex].first;
        int nextCol = col + directions[dirIndex].second;
        
        if (nextRow < 0 || nextRow >= rows || nextCol < 0 || nextCol >= cols || visited[nextRow][nextCol]) {
            dirIndex = (dirIndex + 1) % 4;
            nextRow = row + directions[dirIndex].first;
            nextCol = col + directions[dirIndex].second;
        }
        
        row = nextRow;
        col = nextCol;
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the matrix. This is because we visit each cell exactly once.
> - **Space Complexity:** $O(m \cdot n)$, for storing the result and the visited status of each cell.
> - **Why these complexities occur:** The time complexity is linear with respect to the total number of cells in the matrix because we perform a constant amount of work for each cell. The space complexity is also linear due to the need to store the result and keep track of visited cells.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of manually keeping track of the current position and direction, we can simplify the problem by using four pointers (or indices) to represent the current boundaries of the matrix we are interested in. This allows us to efficiently traverse the matrix in a snail pattern without needing to explicitly check for boundaries and change directions.
- Detailed breakdown of the approach:
  1. Initialize four pointers: `top`, `bottom`, `left`, and `right`, representing the current boundaries of the matrix.
  2. Initialize an empty result vector to store the elements in the snail traversal order.
  3. While the current boundaries are valid (i.e., `top` is less than or equal to `bottom` and `left` is less than or equal to `right`), perform the following steps:
    - Traverse from `left` to `right` at the `top` row, adding each element to the result.
    - Move `top` down by one.
    - Traverse from `top` to `bottom` at the `right` column, adding each element to the result.
    - Move `right` left by one.
    - If the current boundaries are still valid, traverse from `right` to `left` at the `bottom` row, adding each element to the result, and then move `bottom` up by one.
    - Finally, if the boundaries are still valid after the previous steps, traverse from `bottom` to `top` at the `left` column, adding each element to the result, and then move `left` right by one.
  4. Return the result vector containing the elements in the snail traversal order.

```cpp
std::vector<int> snailTraversalOptimal(std::vector<std::vector<int>>& matrix) {
    if (matrix.empty() || matrix[0].empty()) return {};
    
    int rows = matrix.size();
    int cols = matrix[0].size();
    std::vector<int> result;
    int top = 0, bottom = rows - 1, left = 0, right = cols - 1;
    
    while (top <= bottom && left <= right) {
        // Traverse from left to right
        for (int i = left; i <= right; ++i) {
            result.push_back(matrix[top][i]);
        }
        top++;
        
        // Traverse from top to bottom
        for (int i = top; i <= bottom; ++i) {
            result.push_back(matrix[i][right]);
        }
        right--;
        
        if (top <= bottom) {
            // Traverse from right to left
            for (int i = right; i >= left; --i) {
                result.push_back(matrix[bottom][i]);
            }
            bottom--;
        }
        
        if (left <= right) {
            // Traverse from bottom to top
            for (int i = bottom; i >= top; --i) {
                result.push_back(matrix[i][left]);
            }
            left++;
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the matrix. This is because we visit each cell exactly once.
> - **Space Complexity:** $O(m \cdot n)$, for storing the result.
> - **Optimality proof:** This solution is optimal because it achieves the minimum possible time complexity for traversing all elements in the matrix. The space complexity is also minimal as we only store the result, which is necessary for the problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Matrix traversal, boundary conditions, and optimization through simplification of the problem space.
- Problem-solving patterns identified: Breaking down complex traversal patterns into simpler, more manageable parts.
- Optimization techniques learned: Using pointers or indices to efficiently represent and update boundaries.
- Similar problems to practice: Other matrix or grid traversal problems, such as spiral matrix, diagonal traversal, or finding paths in a maze.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly updating boundaries or indices, failing to check for edge cases (e.g., empty matrix, single row/column).
- Edge cases to watch for: Matrices with dimensions 1x1, 1xn, or mx1, and matrices with all elements being the same.
- Performance pitfalls: Using inefficient data structures or algorithms that lead to higher than necessary time or space complexity.
- Testing considerations: Thoroughly testing with various matrix sizes and patterns to ensure correctness and efficiency.