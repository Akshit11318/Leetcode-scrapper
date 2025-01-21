## Rotate Image
**Problem Link:** [https://leetcode.com/problems/rotate-image/description](https://leetcode.com/problems/rotate-image/description)

**Problem Statement:**
- Input format: A 2D `matrix` representing an image, where each element is an integer.
- Constraints: The input `matrix` is a square matrix (i.e., it has the same number of rows and columns), and the number of rows and columns is in the range `[1, 10^3]`.
- Expected output format: The rotated image.
- Key requirements and edge cases to consider:
  - The input `matrix` is guaranteed to be a square matrix.
  - The rotation should be performed in-place (i.e., without using any additional space that scales with input size, beyond what is required for the output).
- Example test cases with explanations:
  - For a `matrix` `[[1,2,3],[4,5,6],[7,8,9]]`, the rotated image should be `[[7,4,1],[8,5,2],[9,6,3]]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to rotate an image is to create a new `matrix` and copy elements from the original `matrix` to the new `matrix` in the rotated positions.
- Step-by-step breakdown of the solution:
  1. Create a new `matrix` with the same dimensions as the original `matrix`.
  2. Iterate through each element in the original `matrix`.
  3. For each element, calculate its new position in the rotated `matrix` and copy it to the new `matrix`.
- Why this approach comes to mind first: This approach is simple and easy to understand, but it requires additional space to store the new `matrix`.

```cpp
void rotate(vector<vector<int>>& matrix) {
    int n = matrix.size();
    vector<vector<int>> newMatrix(n, vector<int>(n));
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            newMatrix[j][n - i - 1] = matrix[i][j];
        }
    }
    
    matrix = newMatrix;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of rows (or columns) in the `matrix`, because we are iterating through each element in the `matrix` once.
> - **Space Complexity:** $O(n^2)$, because we are creating a new `matrix` with the same dimensions as the original `matrix`.
> - **Why these complexities occur:** The time complexity is $O(n^2)$ because we are iterating through each element in the `matrix`, and the space complexity is $O(n^2)$ because we are creating a new `matrix` with the same dimensions as the original `matrix`.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of creating a new `matrix`, we can rotate the original `matrix` in-place by using a two-step process: first, transpose the `matrix`, and then reverse each row.
- Detailed breakdown of the approach:
  1. Transpose the `matrix` by swapping the elements across the main diagonal.
  2. Reverse each row in the transposed `matrix`.
- Proof of optimality: This approach is optimal because it only requires a constant amount of additional space (for the temporary swap variable), and it only iterates through each element in the `matrix` a constant number of times.

```cpp
void rotate(vector<vector<int>>& matrix) {
    int n = matrix.size();
    
    // Transpose the matrix
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            swap(matrix[i][j], matrix[j][i]);
        }
    }
    
    // Reverse each row
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n / 2; j++) {
            swap(matrix[i][j], matrix[i][n - j - 1]);
        }
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, because we are iterating through each element in the `matrix` a constant number of times.
> - **Space Complexity:** $O(1)$, because we are only using a constant amount of additional space (for the temporary swap variable).
> - **Optimality proof:** This approach is optimal because it only requires a constant amount of additional space, and it only iterates through each element in the `matrix` a constant number of times.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Transpose, reverse, and in-place rotation.
- Problem-solving patterns identified: Divide-and-conquer approach, using a two-step process to solve the problem.
- Optimization techniques learned: Reducing space complexity by using in-place rotation, and reducing time complexity by minimizing the number of iterations.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, such as an empty `matrix`.
- Edge cases to watch for: An empty `matrix`, a `matrix` with a single row or column.
- Performance pitfalls: Using a brute force approach that requires additional space, or iterating through each element in the `matrix` multiple times.
- Testing considerations: Testing the function with different input sizes, including edge cases.