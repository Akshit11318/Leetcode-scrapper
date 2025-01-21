## Number of Corner Rectangles

**Problem Link:** https://leetcode.com/problems/number-of-corner-rectangles/description

**Problem Statement:**
- Input format: A 2D binary matrix `mat` where `mat[i][j] = 1` indicates that there is a nail at the grid point `(i, j)`, and `mat[i][j] = 0` indicates that there is no nail.
- Constraints: `1 <= mat.length <= 500`, `1 <= mat[i].length <= 500`, and `0 <= mat[i][j] <= 1`.
- Expected output format: The number of rectangles that have four corners on the nails, possibly rotated or reflected.
- Key requirements and edge cases to consider: 
  - Rectangles can be rotated or reflected.
  - The input matrix is not necessarily square.
- Example test cases with explanations:
  - For example, given the input `[[1,0,0],[0,1,0],[0,0,1]]`, the output should be `4`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check all possible rectangles by iterating over all pairs of points in the matrix.
- Step-by-step breakdown of the solution:
  1. Iterate over all pairs of points in the matrix.
  2. For each pair, check if the other two points of the rectangle are also nails.
  3. Count the number of rectangles found.
- Why this approach comes to mind first: It is a straightforward approach that checks all possibilities.

```cpp
int countCornerRectangles(vector<vector<int>>& mat) {
    int count = 0;
    int m = mat.size();
    int n = mat[0].size();
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            for (int k = i + 1; k < m; k++) {
                for (int l = j + 1; l < n; l++) {
                    if (mat[i][j] && mat[i][l] && mat[k][j] && mat[k][l]) {
                        count++;
                    }
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m^2n^2)$, where $m$ is the number of rows and $n$ is the number of columns in the matrix. This is because we are iterating over all pairs of points in the matrix.
> - **Space Complexity:** $O(1)$, because we are not using any additional space that scales with the input size.
> - **Why these complexities occur:** The time complexity occurs because we are checking all pairs of points in the matrix, and the space complexity occurs because we are not using any additional space that scales with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking all pairs of points, we can iterate over all pairs of rows and count the number of pairs of nails that appear in both rows.
- Detailed breakdown of the approach:
  1. Iterate over all pairs of rows in the matrix.
  2. For each pair of rows, iterate over all pairs of columns and count the number of pairs of nails that appear in both rows.
  3. Return the total count of rectangles found.
- Proof of optimality: This approach is optimal because it only checks the pairs of rows and columns that are necessary to count the number of rectangles.
- Why further optimization is impossible: This approach has a time complexity of $O(m^2n^2)$, which is the minimum time complexity required to count all pairs of nails that appear in both rows.

```cpp
int countCornerRectangles(vector<vector<int>>& mat) {
    int m = mat.size();
    int n = mat[0].size();
    int count = 0;
    for (int i = 0; i < m; i++) {
        for (int j = i + 1; j < m; j++) {
            unordered_map<int, int> map;
            for (int k = 0; k < n; k++) {
                if (mat[i][k] && mat[j][k]) {
                    map[k]++;
                }
            }
            for (auto& pair : map) {
                if (pair.second == 1) {
                    count += pair.second;
                } else {
                    count += pair.second * (pair.second - 1) / 2;
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m^2n)$, where $m$ is the number of rows and $n$ is the number of columns in the matrix. This is because we are iterating over all pairs of rows and columns.
> - **Space Complexity:** $O(n)$, because we are using a map to count the number of pairs of nails that appear in both rows.
> - **Optimality proof:** This approach is optimal because it only checks the pairs of rows and columns that are necessary to count the number of rectangles.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration over all pairs of rows and columns, use of a map to count the number of pairs of nails that appear in both rows.
- Problem-solving patterns identified: Checking all pairs of points in the matrix, counting the number of pairs of nails that appear in both rows.
- Optimization techniques learned: Using a map to count the number of pairs of nails that appear in both rows, only checking the pairs of rows and columns that are necessary to count the number of rectangles.
- Similar problems to practice: Other problems that involve counting the number of rectangles in a matrix, such as counting the number of rectangles with a certain property.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to check all pairs of rows and columns, not using a map to count the number of pairs of nails that appear in both rows.
- Edge cases to watch for: The input matrix may be empty, or it may contain no nails.
- Performance pitfalls: The brute force approach has a high time complexity, so it should be avoided for large inputs.
- Testing considerations: The input matrix should be tested for all possible cases, including the empty matrix and the matrix with no nails.