## Maximum Side Length of a Square with Sum Less Than or Equal to Threshold

**Problem Link:** https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/description

**Problem Statement:**
- Input format: A 2D array `mat` of integers and an integer `threshold`.
- Constraints: `1 <= mat.length <= 1000`, `1 <= mat[0].length <= 1000`, `0 <= mat[i][j] <= 10^4`, and `0 <= threshold <= 10^8`.
- Expected output format: The maximum side length of a square with a sum less than or equal to the threshold.
- Key requirements and edge cases to consider: The square must be fully contained within the matrix, and the sum of all elements in the square must not exceed the threshold.

**Example Test Cases:**
- `mat = [[1,1,3,2,4,3,3,2,1,1],[1,1,3,2,4,3,3,2,1,1],[1,1,3,2,4,3,3,2,1,1],[1,1,3,2,4,3,3,2,1,1],[1,1,3,2,4,3,3,2,1,1],[1,1,3,2,4,3,3,2,1,1],[1,1,3,2,4,3,3,2,1,1],[1,1,3,2,4,3,3,2,1,1],[1,1,3,2,4,3,3,2,1,1],[1,1,3,2,4,3,3,2,1,1]]`, `threshold = 15`.
- The maximum side length of a square with a sum less than or equal to the threshold is `2`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to check all possible squares in the matrix and calculate their sums.
- Step-by-step breakdown of the solution:
  1. Iterate over all possible top-left corners of squares in the matrix.
  2. For each top-left corner, iterate over all possible side lengths of squares.
  3. For each square, calculate the sum of its elements.
  4. If the sum is less than or equal to the threshold, update the maximum side length.
- Why this approach comes to mind first: It is a straightforward and intuitive solution that checks all possible squares.

```cpp
int maxSideLength(vector<vector<int>>& mat, int threshold) {
    int maxSide = 0;
    for (int i = 0; i < mat.size(); i++) {
        for (int j = 0; j < mat[0].size(); j++) {
            for (int side = 1; side <= min(mat.size() - i, mat[0].size() - j); side++) {
                int sum = 0;
                for (int x = i; x < i + side; x++) {
                    for (int y = j; y < j + side; y++) {
                        sum += mat[x][y];
                    }
                }
                if (sum <= threshold) {
                    maxSide = max(maxSide, side);
                }
            }
        }
    }
    return maxSide;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^4)$, where $n$ is the size of the matrix. This is because we have four nested loops: two for iterating over the top-left corner of the square, one for iterating over the side length of the square, and one for calculating the sum of the square's elements.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum side length and the sum of the square's elements.
> - **Why these complexities occur:** The brute force approach has a high time complexity because it checks all possible squares in the matrix, resulting in a large number of iterations.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a prefix sum array to efficiently calculate the sum of any square in the matrix.
- Detailed breakdown of the approach:
  1. Create a prefix sum array `prefixSum` of the same size as the input matrix `mat`.
  2. Initialize the first element of `prefixSum` to the first element of `mat`.
  3. For each element in `mat` (starting from the second row and second column), calculate the prefix sum by adding the current element of `mat` to the sum of the elements above and to the left, minus the element diagonally up and to the left (to avoid double-counting).
  4. Iterate over all possible top-left corners of squares in the matrix.
  5. For each top-left corner, iterate over all possible side lengths of squares.
  6. For each square, calculate the sum of its elements using the prefix sum array.
  7. If the sum is less than or equal to the threshold, update the maximum side length.
- Why further optimization is impossible: This approach has a time complexity of $O(n^3)$, which is the best possible time complexity for this problem because we must check all possible squares in the matrix.

```cpp
int maxSideLength(vector<vector<int>>& mat, int threshold) {
    int n = mat.size();
    int m = mat[0].size();
    vector<vector<int>> prefixSum(n + 1, vector<int>(m + 1, 0));
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            prefixSum[i][j] = prefixSum[i - 1][j] + prefixSum[i][j - 1] - prefixSum[i - 1][j - 1] + mat[i - 1][j - 1];
        }
    }
    int maxSide = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            for (int side = 1; side <= min(n - i, m - j); side++) {
                int sum = prefixSum[i + side][j + side] - prefixSum[i + side][j] - prefixSum[i][j + side] + prefixSum[i][j];
                if (sum <= threshold) {
                    maxSide = max(maxSide, side);
                }
            }
        }
    }
    return maxSide;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the size of the matrix. This is because we have three nested loops: two for iterating over the top-left corner of the square and one for iterating over the side length of the square.
> - **Space Complexity:** $O(n^2)$, as we use a prefix sum array of the same size as the input matrix.
> - **Optimality proof:** This approach is optimal because it uses a prefix sum array to efficiently calculate the sum of any square in the matrix, reducing the time complexity from $O(n^4)$ to $O(n^3)$.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the use of prefix sum arrays to efficiently calculate the sum of any square in the matrix.
- The problem-solving pattern identified is the use of prefix sum arrays to reduce the time complexity of the solution.
- The optimization technique learned is the use of prefix sum arrays to avoid redundant calculations.
- Similar problems to practice include finding the maximum sum of a subarray within a given range.

**Mistakes to Avoid:**
- A common implementation error is not properly initializing the prefix sum array.
- An edge case to watch for is when the input matrix is empty or has a size of 1x1.
- A performance pitfall is not using a prefix sum array, resulting in a high time complexity.
- A testing consideration is to test the solution with large input matrices to ensure it can handle them efficiently.