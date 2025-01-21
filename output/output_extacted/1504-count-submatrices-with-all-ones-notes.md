## Count Submatrices With All Ones
**Problem Link:** https://leetcode.com/problems/count-submatrices-with-all-ones/description

**Problem Statement:**
- Input format: A 2D array `mat` of size `m x n` containing only `0`s and `1`s.
- Constraints: `1 <= m, n <= 10^5`.
- Expected output format: The number of submatrices that contain all `1`s.
- Key requirements: Count all possible submatrices that contain only `1`s.
- Example test cases:
  - `mat = [[1,0,1],[1,1,0],[1,1,0]]` returns `13`.
  - `mat = [[0,1,1,0],[0,1,1,1],[1,0,1,0]]` returns `24`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to check every possible submatrix within the given matrix.
- We will iterate over all possible start and end row and column indices to define each submatrix.
- For each submatrix, we will check if all elements are `1`s.

```cpp
int numSubmat(vector<vector<int>>& mat) {
    int m = mat.size();
    int n = mat[0].size();
    int count = 0;
    
    // Iterate over all possible submatrices
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            for (int k = i; k < m; k++) {
                for (int l = j; l < n; l++) {
                    bool isAllOnes = true;
                    // Check if the current submatrix contains all 1s
                    for (int x = i; x <= k; x++) {
                        for (int y = j; y <= l; y++) {
                            if (mat[x][y] == 0) {
                                isAllOnes = false;
                                break;
                            }
                        }
                        if (!isAllOnes) break;
                    }
                    if (isAllOnes) count++;
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m^3 * n^3)$ because for each cell, we are potentially checking all other cells in the worst case.
> - **Space Complexity:** $O(1)$ because we are only using a constant amount of space to store our variables.
> - **Why these complexities occur:** The brute force approach checks every possible submatrix, leading to a high time complexity. The space complexity remains low because we only use a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a prefix sum array (or a similar cumulative sum technique) to efficiently calculate the sum of any submatrix.
- However, directly applying prefix sum might not be straightforward due to the need to count submatrices with all `1`s, not their sum.
- Instead, we can use a histogram approach. For each row, we calculate the height of the histogram (where `1`s are considered as increasing the height by `1`, and `0`s reset the height to `0`).
- We then calculate the number of rectangles that can be formed with this histogram and repeat the process for each row, adding up the counts.

```cpp
int numSubmat(vector<vector<int>>& mat) {
    int m = mat.size();
    int n = mat[0].size();
    int count = 0;
    
    // Iterate over each row
    for (int i = 0; i < m; i++) {
        vector<int> height(n, 0);
        for (int j = i; j < m; j++) {
            // Update the height of the histogram for the current row
            for (int k = 0; k < n; k++) {
                height[k] = mat[j][k] == 1 ? height[k] + 1 : 0;
            }
            
            // Calculate the number of rectangles in the current histogram
            for (int k = 0; k < n; k++) {
                int minH = height[k];
                for (int l = k; l < n; l++) {
                    minH = min(minH, height[l]);
                    count += minH;
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m^2 * n^2)$ because we are iterating over the rows and for each row, we are potentially checking all other rows and columns.
> - **Space Complexity:** $O(n)$ because we use a vector of size `n` to store the height of the histogram.
> - **Optimality proof:** This approach is more efficient than the brute force because it reduces the number of operations by using a cumulative sum approach (in the form of a histogram) to calculate the number of submatrices with all `1`s. Further optimization might be challenging due to the inherent complexity of the problem.

---

### Final Notes
**Learning Points:**
- The importance of using cumulative sum techniques (like prefix sum or histogram) to efficiently calculate properties of submatrices.
- How to approach problems that require counting specific patterns within a matrix.
- The value of breaking down complex problems into simpler, more manageable parts.

**Mistakes to Avoid:**
- Not considering the use of cumulative sum techniques for problems involving submatrices.
- Failing to optimize the solution by reducing unnecessary iterations.
- Not validating the input and handling edge cases properly.