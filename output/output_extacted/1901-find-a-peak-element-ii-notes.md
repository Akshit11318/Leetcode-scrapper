## Find a Peak Element II
**Problem Link:** https://leetcode.com/problems/find-a-peak-element-ii/description

**Problem Statement:**
- Input: A 2D integer array `mat` where each row is sorted in ascending order.
- Constraints: `1 <= mat.length <= 100`, `1 <= mat[i].length <= 100`, `1 <= mat[i][j] <= 10^5`.
- Expected output: An array `ans` of length 2 where `ans[0]` is the row index and `ans[1]` is the column index of a peak element in the 2D array.
- Key requirements: A peak element is an element that is not smaller than its neighbors.
- Example test cases: 
    - Input: `mat = [[1,2,3,1],[3,8,6,4],[2,5,9,3]]`, Output: `[2,2]`
    - Input: `mat = [[1,2],[3,4]]`, Output: `[1,1]`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Iterate over each element in the 2D array and check if it's a peak element by comparing it with its neighbors.
- Step-by-step breakdown:
    1. Iterate over each element in the 2D array.
    2. For each element, check if it's a peak element by comparing it with its neighbors (up, down, left, right).
    3. If an element is a peak element, return its row and column indices.
- Why this approach comes to mind first: It's a straightforward approach that checks each element individually.

```cpp
vector<int> findPeakGrid(vector<vector<int>>& mat) {
    int rows = mat.size();
    int cols = mat[0].size();
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            bool isPeak = true;
            // Check up
            if (i > 0 && mat[i - 1][j] > mat[i][j]) {
                isPeak = false;
            }
            // Check down
            if (i < rows - 1 && mat[i + 1][j] > mat[i][j]) {
                isPeak = false;
            }
            // Check left
            if (j > 0 && mat[i][j - 1] > mat[i][j]) {
                isPeak = false;
            }
            // Check right
            if (j < cols - 1 && mat[i][j + 1] > mat[i][j]) {
                isPeak = false;
            }
            if (isPeak) {
                return {i, j};
            }
        }
    }
    return {-1, -1}; // Return -1 if no peak element is found
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the number of rows and columns in the 2D array, respectively.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the row and column indices of the peak element.
> - **Why these complexities occur:** The time complexity occurs because we iterate over each element in the 2D array once. The space complexity occurs because we only use a constant amount of space to store the row and column indices of the peak element.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Since each row is sorted in ascending order, we can find the maximum element in each row and then find the maximum element among these row maximums.
- Detailed breakdown:
    1. Find the maximum element in each row.
    2. Find the maximum element among the row maximums.
    3. Return the row and column indices of the maximum element.
- Proof of optimality: This approach is optimal because we only need to iterate over each row once to find the maximum element, resulting in a time complexity of $O(m \cdot n)$.

```cpp
vector<int> findPeakGrid(vector<vector<int>>& mat) {
    int rows = mat.size();
    int cols = mat[0].size();
    int maxRow = 0;
    int maxVal = INT_MIN;
    for (int i = 0; i < rows; i++) {
        int rowMax = *max_element(mat[i].begin(), mat[i].end());
        if (rowMax > maxVal) {
            maxVal = rowMax;
            maxRow = i;
        }
    }
    int maxCol = max_element(mat[maxRow].begin(), mat[maxRow].end()) - mat[maxRow].begin();
    return {maxRow, maxCol};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the number of rows and columns in the 2D array, respectively.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the row and column indices of the peak element.
> - **Optimality proof:** This approach is optimal because we only need to iterate over each row once to find the maximum element, resulting in a time complexity of $O(m \cdot n)$.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, comparison, and optimization.
- Problem-solving patterns identified: Finding the maximum element in a 2D array.
- Optimization techniques learned: Reducing the number of iterations by finding the maximum element in each row.
- Similar problems to practice: Finding the minimum element in a 2D array, finding the maximum element in a 3D array.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty 2D array.
- Edge cases to watch for: An empty 2D array, a 2D array with a single row or column.
- Performance pitfalls: Using a brute force approach that iterates over each element in the 2D array multiple times.
- Testing considerations: Testing the function with different inputs, including edge cases.