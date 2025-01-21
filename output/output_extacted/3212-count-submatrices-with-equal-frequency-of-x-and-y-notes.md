## Count Submatrices with Equal Frequency of X and Y
**Problem Link:** https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/description

**Problem Statement:**
- Given a 2D array `matrix` of size `m x n` and two distinct integers `x` and `y`, return the number of submatrices where `x` and `y` appear with the same frequency.
- Input format and constraints: The input matrix will contain integers in the range `[0, 100]`, and the integers `x` and `y` will be distinct and within the same range.
- Expected output format: The count of submatrices where `x` and `y` have the same frequency.
- Key requirements and edge cases to consider: The problem involves counting submatrices based on the frequency of two distinct integers, so we need to consider cases where the submatrices may have different sizes and positions within the main matrix.
- Example test cases with explanations: For instance, given a matrix `[[1,2,3],[2,2,3],[3,2,1]]` and `x = 2` and `y = 3`, we should count submatrices where `2` and `3` appear the same number of times.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: To solve this problem, we can start by considering all possible submatrices within the given matrix.
- Step-by-step breakdown of the solution: 
  1. Generate all possible submatrices.
  2. For each submatrix, count the occurrences of `x` and `y`.
  3. If `x` and `y` have the same count in a submatrix, increment the result.
- Why this approach comes to mind first: It's a straightforward method that ensures we consider every possible submatrix.

```cpp
int numSubmatrixSum(vector<vector<int>>& matrix, int x, int y) {
    int m = matrix.size();
    int n = matrix[0].size();
    int count = 0;
    
    for (int rowStart = 0; rowStart < m; rowStart++) {
        for (int rowEnd = rowStart; rowEnd < m; rowEnd++) {
            for (int colStart = 0; colStart < n; colStart++) {
                for (int colEnd = colStart; colEnd < n; colEnd++) {
                    int xCount = 0;
                    int yCount = 0;
                    
                    for (int i = rowStart; i <= rowEnd; i++) {
                        for (int j = colStart; j <= colEnd; j++) {
                            if (matrix[i][j] == x) xCount++;
                            if (matrix[i][j] == y) yCount++;
                        }
                    }
                    
                    if (xCount == yCount) count++;
                }
            }
        }
    }
    
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m^3n^3)$, where $m$ and $n$ are the dimensions of the matrix. This is because we are generating all possible submatrices and for each, we are counting the occurrences of `x` and `y`.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input matrix, as we only use a constant amount of space to store our variables.
> - **Why these complexities occur:** The time complexity is high because we are considering every possible submatrix, and for each, we perform a nested loop to count `x` and `y`. The space complexity is low because we only use a fixed amount of space to store our counters and loop variables.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of counting `x` and `y` for each submatrix from scratch, we can use a prefix sum approach to efficiently calculate the counts of `x` and `y` for any given submatrix.
- Detailed breakdown of the approach: 
  1. Create a prefix sum matrix for `x` and `y` separately.
  2. Use the prefix sum matrices to calculate the counts of `x` and `y` for any submatrix in constant time.
  3. Iterate through all possible submatrices and use the prefix sums to check if `x` and `y` have the same count.
- Proof of optimality: This approach is optimal because it reduces the time complexity of counting `x` and `y` for each submatrix from $O(mn)$ to $O(1)$, leveraging the prefix sum property.

```cpp
int numSubmatrixSum(vector<vector<int>>& matrix, int x, int y) {
    int m = matrix.size();
    int n = matrix[0].size();
    int count = 0;
    vector<vector<int>> prefixX(m + 1, vector<int>(n + 1, 0));
    vector<vector<int>> prefixY(m + 1, vector<int>(n + 1, 0));
    
    // Calculate prefix sums for x and y
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            prefixX[i][j] = prefixX[i-1][j] + prefixX[i][j-1] - prefixX[i-1][j-1] + (matrix[i-1][j-1] == x ? 1 : 0);
            prefixY[i][j] = prefixY[i-1][j] + prefixY[i][j-1] - prefixY[i-1][j-1] + (matrix[i-1][j-1] == y ? 1 : 0);
        }
    }
    
    // Use prefix sums to count submatrices where x and y have the same frequency
    for (int rowStart = 0; rowStart < m; rowStart++) {
        for (int rowEnd = rowStart; rowEnd < m; rowEnd++) {
            for (int colStart = 0; colStart < n; colStart++) {
                for (int colEnd = colStart; colEnd < n; colEnd++) {
                    int xCount = prefixX[rowEnd+1][colEnd+1] - prefixX[rowStart][colEnd+1] - prefixX[rowEnd+1][colStart] + prefixX[rowStart][colStart];
                    int yCount = prefixY[rowEnd+1][colEnd+1] - prefixY[rowStart][colEnd+1] - prefixY[rowEnd+1][colStart] + prefixY[rowStart][colStart];
                    
                    if (xCount == yCount) count++;
                }
            }
        }
    }
    
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m^3n^3)$, because although we use prefix sums to efficiently calculate counts, we still need to consider all possible submatrices.
> - **Space Complexity:** $O(mn)$, for the prefix sum matrices.
> - **Optimality proof:** While the time complexity remains the same as the brute force due to the necessity of considering all submatrices, the use of prefix sums optimizes the calculation of `x` and `y` counts for each submatrix, making the approach more efficient in practice.

---

### Final Notes

**Learning Points:**
- The importance of prefix sums in optimizing the calculation of submatrix properties.
- The trade-off between time and space complexity in algorithm design.
- The necessity of considering all possible submatrices in this problem, which dictates the time complexity.

**Mistakes to Avoid:**
- Failing to initialize prefix sum matrices correctly.
- Incorrectly calculating the counts of `x` and `y` using prefix sums.
- Not considering edge cases, such as when `x` or `y` is not present in the matrix.