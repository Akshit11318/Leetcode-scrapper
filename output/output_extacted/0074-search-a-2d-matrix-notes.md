## Search a 2D Matrix

**Problem Link:** https://leetcode.com/problems/search-a-2d-matrix/description

**Problem Statement:**
- Input: A `rows x cols` matrix `matrix`, and a target integer `target`.
- Constraints: `1 <= rows, cols <= 200`; `-10^9 <= matrix[i][j] <= 10^9`; `-10^9 <= target <= 10^9`.
- Expected output: Return `true` if `target` is found in the matrix, otherwise return `false`.
- Key requirements: The matrix is sorted in a specific way: the integers in each row are sorted from left to right, and the first integer of each row is greater than the last integer of the previous row.
- Example test cases:
  - `matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]`, `target = 3` returns `true`.
  - `matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]`, `target = 13` returns `false`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate over each element in the matrix and check if it matches the target.
- This approach comes to mind first because it's straightforward and doesn't require any complex algorithms or data structures.
- However, it's not efficient for large matrices because it checks every element.

```cpp
bool searchMatrix(vector<vector<int>>& matrix, int target) {
    int rows = matrix.size();
    int cols = matrix[0].size();
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (matrix[i][j] == target) return true;
        }
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(rows \times cols)$, because in the worst case, we need to check every element in the matrix.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the row and column indices.
> - **Why these complexities occur:** The brute force approach has a high time complexity because it checks every element in the matrix, resulting in a linear search. The space complexity is low because we don't use any additional data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to treat the 2D matrix as a 1D array and use a binary search algorithm to find the target.
- We can do this because the matrix is sorted in a specific way: the integers in each row are sorted from left to right, and the first integer of each row is greater than the last integer of the previous row.
- This approach is optimal because it reduces the time complexity from linear to logarithmic.

```cpp
bool searchMatrix(vector<vector<int>>& matrix, int target) {
    int rows = matrix.size();
    int cols = matrix[0].size();
    int left = 0;
    int right = rows * cols - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        int num = matrix[mid / cols][mid % cols];
        if (num == target) return true;
        else if (num < target) left = mid + 1;
        else right = mid - 1;
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log(rows \times cols))$, because we use a binary search algorithm to find the target.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the indices and the target.
> - **Optimality proof:** This approach is optimal because it takes advantage of the sorted property of the matrix to reduce the time complexity from linear to logarithmic. Further optimization is impossible because we need to check at least $\log(n)$ elements in the worst case to find the target in a sorted array of size $n$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: binary search, treating a 2D matrix as a 1D array.
- Problem-solving patterns identified: using the sorted property of the input to reduce the time complexity.
- Optimization techniques learned: treating a 2D matrix as a 1D array, using binary search to find the target.
- Similar problems to practice: searching in a rotated sorted array, searching in a sorted matrix with unknown dimensions.

**Mistakes to Avoid:**
- Common implementation errors: not checking the bounds of the matrix, not handling the case where the target is not found.
- Edge cases to watch for: an empty matrix, a matrix with a single element, a target that is not in the matrix.
- Performance pitfalls: using a linear search algorithm instead of a binary search algorithm.
- Testing considerations: testing the function with different inputs, including edge cases and large matrices.