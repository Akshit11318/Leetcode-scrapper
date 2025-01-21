## Search a 2D Matrix II

**Problem Link:** https://leetcode.com/problems/search-a-2d-matrix-ii/description

**Problem Statement:**
- Input format and constraints: Given an `m x n` matrix of integers `matrix` and an integer `target`, return `true` if `target` is in the matrix and `false` otherwise.
- Expected output format: A boolean indicating whether the target is found.
- Key requirements and edge cases to consider: The matrix is sorted in a way that all elements in each row are in ascending order and all elements in each column are in ascending order.
- Example test cases with explanations:
  - Example 1: Given `matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]`, `target = 5`, return `true`.
  - Example 2: Given `matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]`, `target = 20`, return `false`.

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every element in the matrix to see if it matches the target.
- Step-by-step breakdown of the solution:
  1. Iterate through each row in the matrix.
  2. For each row, iterate through each column.
  3. Check if the current element is equal to the target.
- Why this approach comes to mind first: It's the simplest way to ensure every element is checked.

```cpp
bool searchMatrix(vector<vector<int>>& matrix, int target) {
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[0].size(); j++) {
            if (matrix[i][j] == target) {
                return true;
            }
        }
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns, because in the worst case, we have to check every element in the matrix.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the indices and the target.
> - **Why these complexities occur:** The brute force approach requires checking every element, leading to linear time complexity with respect to the total number of elements. The space complexity is constant because we don't use any additional data structures that scale with the input size.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Since the matrix is sorted in ascending order both row-wise and column-wise, we can start from the top-right corner and move either left or down based on whether the current element is greater than or less than the target. This allows us to eliminate rows or columns with each comparison.
- Detailed breakdown of the approach:
  1. Start at the top-right corner of the matrix.
  2. Compare the current element with the target.
  3. If the current element is equal to the target, return `true`.
  4. If the current element is greater than the target, move left (since all elements to the right are also greater).
  5. If the current element is less than the target, move down (since all elements above are also less).
- Proof of optimality: This approach minimizes the number of comparisons needed by eliminating entire rows or columns with each comparison, making it more efficient than checking every element.

```cpp
bool searchMatrix(vector<vector<int>>& matrix, int target) {
    if (matrix.empty() || matrix[0].empty()) return false;
    
    int row = 0, col = matrix[0].size() - 1;
    while (row < matrix.size() && col >= 0) {
        if (matrix[row][col] == target) return true;
        else if (matrix[row][col] < target) row++;
        else col--;
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m + n)$, where $m$ is the number of rows and $n$ is the number of columns, because in the worst case, we might have to traverse the entire length of the matrix either horizontally or vertically.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the indices and the target.
> - **Optimality proof:** This approach is optimal because it takes advantage of the sorted structure of the matrix to minimize the number of comparisons needed to find the target or determine it's not present.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Taking advantage of the structure of the input data to optimize the algorithm.
- Problem-solving patterns identified: Using a combination of row-wise and column-wise sorting to reduce the search space.
- Optimization techniques learned: Eliminating rows or columns based on comparisons to reduce the number of elements that need to be checked.
- Similar problems to practice: Other problems involving searching in sorted matrices or arrays.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases such as an empty matrix or a matrix with a single row or column.
- Edge cases to watch for: The target being at the boundary of the matrix (first or last row, first or last column).
- Performance pitfalls: Failing to take advantage of the sorted structure, leading to a brute-force approach.
- Testing considerations: Ensure to test with various matrix sizes, target locations, and edge cases.