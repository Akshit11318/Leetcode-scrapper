## Maximum Matrix Sum
**Problem Link:** https://leetcode.com/problems/maximum-matrix-sum/description

**Problem Statement:**
- Input format: A 2D integer array `matrix` of size `n x n`.
- Constraints: `1 <= n <= 50`.
- Expected output format: The maximum sum of a matrix after rotating the rows and columns.
- Key requirements and edge cases to consider:
  - The matrix is square (i.e., `n x n`).
  - The values in the matrix are integers.
  - We can rotate the rows and columns by 90 degrees clockwise any number of times.
- Example test cases with explanations:
  - A simple 2x2 matrix with positive values.
  - A 3x3 matrix with a mix of positive and negative values.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible rotations of rows and columns and calculate the sum for each configuration.
- Step-by-step breakdown of the solution:
  1. Generate all possible rotations of rows (2^n possibilities).
  2. For each row rotation, generate all possible rotations of columns (2^n possibilities).
  3. Calculate the sum of the matrix for each configuration.
  4. Keep track of the maximum sum found.
- Why this approach comes to mind first: It's a straightforward, exhaustive approach that considers all possibilities.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int maxMatrixSum(vector<vector<int>>& matrix) {
    int n = matrix.size();
    int maxSum = INT_MIN;

    // Generate all possible rotations of rows
    for (int rowMask = 0; rowMask < (1 << n); rowMask++) {
        // Generate all possible rotations of columns
        for (int colMask = 0; colMask < (1 << n); colMask++) {
            vector<vector<int>> rotatedMatrix = matrix;

            // Rotate rows
            for (int i = 0; i < n; i++) {
                if ((rowMask & (1 << i)) != 0) {
                    // Rotate row i by 90 degrees clockwise
                    vector<int> newRow(n);
                    for (int j = 0; j < n; j++) {
                        newRow[j] = rotatedMatrix[i][n - 1 - j];
                    }
                    rotatedMatrix[i] = newRow;
                }
            }

            // Rotate columns
            for (int j = 0; j < n; j++) {
                if ((colMask & (1 << j)) != 0) {
                    // Rotate column j by 90 degrees clockwise
                    vector<int> newCol(n);
                    for (int i = 0; i < n; i++) {
                        newCol[i] = rotatedMatrix[n - 1 - i][j];
                    }
                    for (int i = 0; i < n; i++) {
                        rotatedMatrix[i][j] = newCol[i];
                    }
                }
            }

            // Calculate the sum of the rotated matrix
            int sum = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    sum += rotatedMatrix[i][j];
                }
            }

            // Update the maximum sum
            maxSum = max(maxSum, sum);
        }
    }

    return maxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{2n} \cdot n^2)$, where $n$ is the size of the matrix. This is because we have $2^n$ possible rotations for rows and $2^n$ possible rotations for columns, and for each configuration, we calculate the sum of the matrix, which takes $O(n^2)$ time.
> - **Space Complexity:** $O(n^2)$, where $n$ is the size of the matrix. This is because we need to store the rotated matrix.
> - **Why these complexities occur:** The high time complexity occurs because we are trying all possible rotations of rows and columns, which leads to an exponential number of configurations. The space complexity occurs because we need to store the rotated matrix.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: We can calculate the sum of the matrix without actually rotating the rows and columns. We can simply calculate the sum of the absolute values of the elements and then add the minimum value multiplied by the number of negative values.
- Detailed breakdown of the approach:
  1. Calculate the sum of the absolute values of the elements.
  2. Count the number of negative values.
  3. Calculate the minimum value.
  4. Calculate the maximum sum by adding the sum of the absolute values and the minimum value multiplied by the number of negative values.
- Proof of optimality: This approach is optimal because it avoids the need to try all possible rotations of rows and columns, which reduces the time complexity significantly.

```cpp
int maxMatrixSum(vector<vector<int>>& matrix) {
    int n = matrix.size();
    int sum = 0;
    int minVal = INT_MAX;
    int negCount = 0;

    // Calculate the sum of the absolute values of the elements
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            sum += abs(matrix[i][j]);
            minVal = min(minVal, abs(matrix[i][j]));
            if (matrix[i][j] < 0) {
                negCount++;
            }
        }
    }

    // Calculate the maximum sum
    if (negCount % 2 == 1) {
        return sum - 2 * minVal;
    } else {
        return sum;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the matrix. This is because we need to iterate over all elements in the matrix.
> - **Space Complexity:** $O(1)$, where $n$ is the size of the matrix. This is because we only need a constant amount of space to store the sum, minimum value, and count of negative values.
> - **Optimality proof:** This approach is optimal because it avoids the need to try all possible rotations of rows and columns, which reduces the time complexity significantly.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The importance of finding a key insight to simplify the problem.
- Problem-solving patterns identified: The use of mathematical properties to avoid brute force approaches.
- Optimization techniques learned: The use of absolute values and counting to simplify the calculation.
- Similar problems to practice: Problems that involve finding the maximum or minimum value of a function.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where the number of negative values is odd.
- Edge cases to watch for: The case where the matrix contains all zeros.
- Performance pitfalls: Using a brute force approach that tries all possible rotations of rows and columns.
- Testing considerations: Testing the function with different input matrices, including edge cases.