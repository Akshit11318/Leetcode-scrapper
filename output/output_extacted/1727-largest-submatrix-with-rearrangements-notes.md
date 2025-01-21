## Largest Submatrix with Rearrangements
**Problem Link:** https://leetcode.com/problems/largest-submatrix-with-rearrangements/description

**Problem Statement:**
- Input: A 2D integer array `matrix` where each row has the same number of elements.
- Constraints: The input matrix is non-empty, and each row has the same number of elements.
- Expected Output: The area of the largest submatrix that can be obtained by rearranging the elements of the input matrix such that the elements in each row are in non-decreasing order.
- Key Requirements: 
  - The submatrix can be any size, from 1x1 to the size of the input matrix.
  - Rearrangement can only occur within each row, not between rows.
  - The goal is to maximize the area of the submatrix, which is the product of the number of rows and the number of columns.
- Example Test Cases:
  - For the input `matrix = [[0,3,1,1],[2,0,3,4],[3,3,3,2],[0,0,0,2]]`, the output is `4`, which corresponds to the submatrix `[[0,0,0,0],[2,2,2,2],[3,3,3,3],[3,3,3,3]]`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves checking every possible submatrix and determining if its rows can be rearranged into non-decreasing order.
- For each possible submatrix, sort each row and then check if the columns are in non-decreasing order.
- If they are, calculate the area of the submatrix and update the maximum area found so far.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int largestSubmatrix(std::vector<std::vector<int>>& matrix) {
    int rows = matrix.size();
    int cols = matrix[0].size();
    int maxArea = 0;

    // Iterate over all possible submatrices
    for (int rowStart = 0; rowStart < rows; rowStart++) {
        for (int rowEnd = rowStart; rowEnd < rows; rowEnd++) {
            for (int colStart = 0; colStart < cols; colStart++) {
                for (int colEnd = colStart; colEnd < cols; colEnd++) {
                    // Extract the current submatrix
                    std::vector<std::vector<int>> submatrix(rowEnd - rowStart + 1, std::vector<int>(colEnd - colStart + 1));
                    for (int i = rowStart; i <= rowEnd; i++) {
                        for (int j = colStart; j <= colEnd; j++) {
                            submatrix[i - rowStart][j - colStart] = matrix[i][j];
                        }
                    }

                    // Check if the rows of the submatrix can be rearranged into non-decreasing order
                    bool valid = true;
                    for (auto& row : submatrix) {
                        std::sort(row.begin(), row.end());
                    }
                    for (int j = 0; j < submatrix[0].size(); j++) {
                        for (int i = 1; i < submatrix.size(); i++) {
                            if (submatrix[i - 1][j] > submatrix[i][j]) {
                                valid = false;
                                break;
                            }
                        }
                        if (!valid) break;
                    }

                    // If valid, update the maximum area
                    if (valid) {
                        maxArea = std::max(maxArea, (rowEnd - rowStart + 1) * (colEnd - colStart + 1));
                    }
                }
            }
        }
    }

    return maxArea;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{n \cdot m} \cdot n \cdot m \cdot log(n \cdot m))$, where $n$ is the number of rows and $m$ is the number of columns in the input matrix. This is because we are iterating over all possible submatrices, sorting each row, and then checking each column.
> - **Space Complexity:** $O(n \cdot m)$, which is used to store the current submatrix.
> - **Why these complexities occur:** The brute force approach involves checking every possible submatrix, which leads to an exponential number of iterations. Additionally, sorting each row and checking each column adds to the time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to sort each row of the input matrix and then use a greedy approach to find the maximum area submatrix.
- After sorting each row, iterate over each column from top to bottom and keep track of the number of rows that can be included in the submatrix without violating the non-decreasing order constraint.
- The maximum area submatrix can be found by keeping track of the maximum product of the number of rows and the number of columns.

```cpp
int largestSubmatrix(std::vector<std::vector<int>>& matrix) {
    int rows = matrix.size();
    int cols = matrix[0].size();
    int maxArea = 0;

    // Sort each row of the input matrix
    for (auto& row : matrix) {
        std::sort(row.begin(), row.end());
    }

    // Iterate over each column from top to bottom
    for (int col = 0; col < cols; col++) {
        std::vector<int> heights(rows);
        for (int row = 0; row < rows; row++) {
            heights[row] = 1;
            for (int prevCol = col - 1; prevCol >= 0; prevCol--) {
                if (matrix[row][prevCol] <= matrix[row][col]) {
                    heights[row]++;
                } else {
                    break;
                }
            }
        }

        // Sort the heights in non-decreasing order
        std::sort(heights.begin(), heights.end());

        // Find the maximum area submatrix
        for (int i = 0; i < rows; i++) {
            maxArea = std::max(maxArea, (rows - i) * heights[i]);
        }
    }

    return maxArea;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot log(n))$, where $n$ is the number of rows and $m$ is the number of columns in the input matrix. This is because we are sorting each row and then iterating over each column.
> - **Space Complexity:** $O(n)$, which is used to store the heights of the submatrix.
> - **Optimality proof:** This approach is optimal because it takes advantage of the fact that the rows are sorted, allowing us to use a greedy approach to find the maximum area submatrix. The time complexity is also optimal because we need to iterate over each column and sort the heights.

---

### Final Notes

**Learning Points:**
- The importance of sorting each row of the input matrix to take advantage of the non-decreasing order constraint.
- The use of a greedy approach to find the maximum area submatrix.
- The need to iterate over each column from top to bottom to find the maximum area submatrix.

**Mistakes to Avoid:**
- Not sorting each row of the input matrix, which can lead to incorrect results.
- Not using a greedy approach to find the maximum area submatrix, which can lead to inefficient solutions.
- Not iterating over each column from top to bottom, which can lead to missing the maximum area submatrix.