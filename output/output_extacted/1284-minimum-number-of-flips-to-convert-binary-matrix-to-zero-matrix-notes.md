## Minimum Number of Flips to Convert Binary Matrix to Zero Matrix

**Problem Link:** https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/description

**Problem Statement:**
- Input format: A binary matrix `mat` of size `m x n`, where each cell can have a value of 0 or 1.
- Constraints: `1 <= m, n <= 100`, `mat[i][j]` is `0` or `1`.
- Expected output format: The minimum number of flips required to convert the binary matrix to a zero matrix.
- Key requirements and edge cases to consider:
  - Flipping a cell in the matrix flips all cells in the same row and column.
  - The goal is to find the minimum number of flips to make all cells in the matrix 0.
- Example test cases with explanations:
  - `mat = [[0,0],[0,1]]`: The minimum number of flips is 3 (flip the cell at position (1,1), then flip the row and column).
  - `mat = [[1,1,0],[1,0,1],[0,0,0]]`: The minimum number of flips is 6 (flip the cell at position (0,0), then flip the row and column, and repeat for the cell at position (1,1)).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of flips to find the minimum number of flips required.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of flips.
  2. For each combination, apply the flips to the matrix.
  3. Check if the resulting matrix is a zero matrix.
  4. If it is, update the minimum number of flips.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible solutions.

```cpp
#include <vector>
#include <algorithm>

using namespace std;

int minFlips(vector<vector<int>>& mat) {
    int m = mat.size();
    int n = mat[0].size();
    int minFlips = m * n;

    // Generate all possible combinations of flips
    for (int mask = 0; mask < (1 << (m + n)); mask++) {
        vector<vector<int>> flippedMat = mat;
        int flips = 0;

        // Apply the flips to the matrix
        for (int i = 0; i < m + n; i++) {
            if ((mask & (1 << i)) != 0) {
                flips++;
                if (i < m) {
                    // Flip the row
                    for (int j = 0; j < n; j++) {
                        flippedMat[i][j] ^= 1;
                    }
                } else {
                    // Flip the column
                    for (int j = 0; j < m; j++) {
                        flippedMat[j][i - m] ^= 1;
                    }
                }
            }
        }

        // Check if the resulting matrix is a zero matrix
        bool isZeroMatrix = true;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (flippedMat[i][j] != 0) {
                    isZeroMatrix = false;
                    break;
                }
            }
            if (!isZeroMatrix) {
                break;
            }
        }

        // Update the minimum number of flips
        if (isZeroMatrix) {
            minFlips = min(minFlips, flips);
        }
    }

    return minFlips;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{m+n} \cdot (m+n) \cdot m \cdot n)$, where $m$ and $n$ are the dimensions of the matrix. This is because we generate all possible combinations of flips, and for each combination, we apply the flips to the matrix and check if the resulting matrix is a zero matrix.
> - **Space Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the matrix. This is because we need to store the flipped matrix.
> - **Why these complexities occur:** The brute force approach tries all possible combinations of flips, which results in an exponential time complexity. The space complexity is linear because we only need to store the flipped matrix.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a greedy approach to find the minimum number of flips. We start by flipping the rows, and then flip the columns.
- Detailed breakdown of the approach:
  1. Flip the rows: For each row, if the number of 1s is greater than the number of 0s, flip the row.
  2. Flip the columns: For each column, if the number of 1s is greater than the number of 0s, flip the column.
- Proof of optimality: This approach is optimal because it minimizes the number of flips required to make all cells in the matrix 0.

```cpp
int minFlips(vector<vector<int>>& mat) {
    int m = mat.size();
    int n = mat[0].size();
    int flips = 0;

    // Flip the rows
    for (int i = 0; i < m; i++) {
        int ones = 0;
        for (int j = 0; j < n; j++) {
            if (mat[i][j] == 1) {
                ones++;
            }
        }
        if (ones > n - ones) {
            flips++;
            for (int j = 0; j < n; j++) {
                mat[i][j] ^= 1;
            }
        }
    }

    // Flip the columns
    for (int j = 0; j < n; j++) {
        int ones = 0;
        for (int i = 0; i < m; i++) {
            if (mat[i][j] == 1) {
                ones++;
            }
        }
        if (ones > m - ones) {
            flips++;
            for (int i = 0; i < m; i++) {
                mat[i][j] ^= 1;
            }
        }
    }

    return flips;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the matrix. This is because we iterate over the matrix twice, once for flipping the rows and once for flipping the columns.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the number of flips.
> - **Optimality proof:** This approach is optimal because it minimizes the number of flips required to make all cells in the matrix 0. The greedy approach ensures that we always flip the row or column that has the most 1s, which minimizes the number of flips required.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy approach, bit manipulation.
- Problem-solving patterns identified: Minimizing the number of operations required to achieve a goal.
- Optimization techniques learned: Using a greedy approach to minimize the number of flips required.
- Similar problems to practice: Other problems that involve minimizing the number of operations required to achieve a goal, such as the `minSwaps` problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing variables correctly, not checking for edge cases.
- Edge cases to watch for: Matrices with all 0s or all 1s, matrices with a single row or column.
- Performance pitfalls: Using a brute force approach, not optimizing the solution.
- Testing considerations: Test the solution with different inputs, including edge cases and large inputs.