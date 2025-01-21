## Longest Line of Consecutive One in Matrix

**Problem Link:** https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/description

**Problem Statement:**
- Input format and constraints: The input is a 2D matrix `mat` of size `m x n` where `m` and `n` are integers, and each cell contains either `0` or `1`. The goal is to find the length of the longest line of consecutive ones in the matrix. The line can be horizontal, vertical, or diagonal.
- Expected output format: The function should return an integer representing the length of the longest line of consecutive ones.
- Key requirements and edge cases to consider: The input matrix may be empty, or it may contain only zeros. The function should handle these edge cases correctly.
- Example test cases with explanations:
  - For the input `[[0,1,1],[1,1,0],[0,1,1]]`, the output should be `3`.
  - For the input `[[1,1,0],[1,1,0],[0,0,1]]`, the output should be `2`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves checking every possible line in the matrix (horizontal, vertical, and diagonal) and counting the consecutive ones in each line.
- Step-by-step breakdown of the solution:
  1. Iterate over each cell in the matrix.
  2. For each cell, check the horizontal, vertical, and diagonal lines starting from that cell.
  3. For each line, count the consecutive ones.
  4. Keep track of the maximum length of consecutive ones found so far.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it has a high time complexity due to the nested loops.

```cpp
int longestLine(vector<vector<int>>& mat) {
    int m = mat.size();
    if (m == 0) return 0;
    int n = mat[0].size();
    int maxLen = 0;

    // Check horizontal lines
    for (int i = 0; i < m; i++) {
        int len = 0;
        for (int j = 0; j < n; j++) {
            if (mat[i][j] == 1) len++;
            else len = 0;
            maxLen = max(maxLen, len);
        }
    }

    // Check vertical lines
    for (int j = 0; j < n; j++) {
        int len = 0;
        for (int i = 0; i < m; i++) {
            if (mat[i][j] == 1) len++;
            else len = 0;
            maxLen = max(maxLen, len);
        }
    }

    // Check diagonal lines (from top-left to bottom-right)
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            int x = i, y = j, len = 0;
            while (x < m && y < n) {
                if (mat[x][y] == 1) len++;
                else len = 0;
                maxLen = max(maxLen, len);
                x++; y++;
            }
        }
    }

    // Check diagonal lines (from top-right to bottom-left)
    for (int i = 0; i < m; i++) {
        for (int j = n - 1; j >= 0; j--) {
            int x = i, y = j, len = 0;
            while (x < m && y >= 0) {
                if (mat[x][y] == 1) len++;
                else len = 0;
                maxLen = max(maxLen, len);
                x++; y--;
            }
        }
    }

    return maxLen;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot (m + n))$ because we are checking every possible line in the matrix.
> - **Space Complexity:** $O(1)$ because we are not using any extra space that scales with the input size.
> - **Why these complexities occur:** The time complexity is high due to the nested loops, and the space complexity is low because we are only using a constant amount of space to store the maximum length.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking every possible line, we can iterate over each cell in the matrix and check the four directions (up, down, left, right, and two diagonals) starting from that cell.
- Detailed breakdown of the approach:
  1. Iterate over each cell in the matrix.
  2. For each cell, check the four directions (up, down, left, right, and two diagonals) starting from that cell.
  3. For each direction, count the consecutive ones.
  4. Keep track of the maximum length of consecutive ones found so far.
- Proof of optimality: This approach is optimal because it only checks the necessary cells in the matrix, reducing the time complexity.

```cpp
int longestLine(vector<vector<int>>& mat) {
    int m = mat.size();
    if (m == 0) return 0;
    int n = mat[0].size();
    int maxLen = 0;

    vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {1, 1}, {1, -1}};

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (mat[i][j] == 1) {
                for (auto& dir : directions) {
                    int x = i, y = j, len = 1;
                    while (x + dir.first < m && y + dir.second < n && x + dir.first >= 0 && y + dir.second >= 0) {
                        x += dir.first; y += dir.second;
                        if (mat[x][y] == 1) len++;
                        else break;
                    }
                    maxLen = max(maxLen, len);
                }
            }
        }
    }

    return maxLen;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$ because we are iterating over each cell in the matrix and checking the four directions.
> - **Space Complexity:** $O(1)$ because we are not using any extra space that scales with the input size.
> - **Optimality proof:** This approach is optimal because it only checks the necessary cells in the matrix, reducing the time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional statements, and optimization.
- Problem-solving patterns identified: Checking all possible lines and optimizing the approach by reducing the number of checks.
- Optimization techniques learned: Reducing the number of checks by only iterating over each cell in the matrix and checking the four directions.
- Similar problems to practice: Finding the longest increasing subsequence, longest common subsequence, and longest palindromic subsequence.

**Mistakes to Avoid:**
- Common implementation errors: Not checking the edge cases, not handling the case where the input matrix is empty.
- Edge cases to watch for: Empty matrix, matrix with only zeros, and matrix with only ones.
- Performance pitfalls: Checking every possible line in the matrix, which has a high time complexity.
- Testing considerations: Test the function with different input matrices, including edge cases and large matrices.