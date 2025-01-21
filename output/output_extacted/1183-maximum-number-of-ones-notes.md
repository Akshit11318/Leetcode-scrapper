## Maximum Number of Ones

**Problem Link:** https://leetcode.com/problems/maximum-number-of-ones/description

**Problem Statement:**
- Input format: A 2D array `mat` of size `m x n` and an integer `k`.
- Constraints: `1 <= m <= 1000`, `1 <= n <= 1000`, `1 <= k <= min(m, n)`.
- Expected output format: The maximum number of ones in a submatrix of size `k x k`.
- Key requirements and edge cases to consider:
  - The submatrix can be any position in the original matrix.
  - The submatrix must be a square of size `k x k`.
- Example test cases with explanations:
  - `mat = [[1,0,1],[0,1,0],[1,0,1]], k = 2` should return `4`.
  - `mat = [[0,0,0],[0,0,0],[0,0,0]], k = 1` should return `0`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through all possible submatrices of size `k x k` and count the number of ones in each submatrix.
- Step-by-step breakdown of the solution:
  1. Iterate through all possible top-left positions of a submatrix of size `k x k`.
  2. For each position, count the number of ones in the corresponding submatrix.
  3. Keep track of the maximum count of ones found.
- Why this approach comes to mind first: It is the most straightforward way to solve the problem, but it is not efficient for large inputs.

```cpp
int maxOnes(vector<vector<int>>& mat, int k) {
    int m = mat.size();
    int n = mat[0].size();
    int maxCount = 0;
    for (int i = 0; i <= m - k; i++) {
        for (int j = 0; j <= n - k; j++) {
            int count = 0;
            for (int x = i; x < i + k; x++) {
                for (int y = j; y < j + k; y++) {
                    if (mat[x][y] == 1) {
                        count++;
                    }
                }
            }
            maxCount = max(maxCount, count);
        }
    }
    return maxCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m^2 \cdot n^2 \cdot k^2)$, where $m$ and $n$ are the dimensions of the input matrix and $k$ is the size of the submatrix.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum count and the current count.
> - **Why these complexities occur:** The brute force approach has a high time complexity because it iterates through all possible submatrices and counts the number of ones in each submatrix. The space complexity is low because we only use a constant amount of space to store the maximum count and the current count.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a prefix sum array to efficiently count the number of ones in a submatrix.
- Detailed breakdown of the approach:
  1. Create a prefix sum array `prefix` of size `(m + 1) x (n + 1)`, where `prefix[i][j]` represents the sum of all elements in the submatrix from `(0, 0)` to `(i - 1, j - 1)`.
  2. Iterate through all possible top-left positions of a submatrix of size `k x k`.
  3. For each position, use the prefix sum array to efficiently count the number of ones in the corresponding submatrix.
  4. Keep track of the maximum count of ones found.
- Proof of optimality: The optimal approach has a time complexity of $O(m^2 \cdot n^2)$, which is the best possible time complexity for this problem.

```cpp
int maxOnes(vector<vector<int>>& mat, int k) {
    int m = mat.size();
    int n = mat[0].size();
    vector<vector<int>> prefix(m + 1, vector<int>(n + 1, 0));
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + mat[i - 1][j - 1];
        }
    }
    int maxCount = 0;
    for (int i = k; i <= m; i++) {
        for (int j = k; j <= n; j++) {
            int count = prefix[i][j] - prefix[i - k][j] - prefix[i][j - k] + prefix[i - k][j - k];
            maxCount = max(maxCount, count);
        }
    }
    return maxCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n + m^2 \cdot n^2)$, where $m$ and $n$ are the dimensions of the input matrix.
> - **Space Complexity:** $O(m \cdot n)$, as we use a prefix sum array of size `(m + 1) x (n + 1)`.
> - **Optimality proof:** The optimal approach has a time complexity of $O(m^2 \cdot n^2)$, which is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Prefix sum arrays, efficient counting of ones in a submatrix.
- Problem-solving patterns identified: Using prefix sum arrays to efficiently count the number of ones in a submatrix.
- Optimization techniques learned: Using prefix sum arrays to reduce the time complexity of the algorithm.
- Similar problems to practice: Problems that involve counting the number of ones in a submatrix, such as the "Maximum Number of Ones" problem on LeetCode.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the prefix sum array correctly, not using the prefix sum array correctly to count the number of ones in a submatrix.
- Edge cases to watch for: The input matrix may be empty, the size of the submatrix may be larger than the input matrix.
- Performance pitfalls: Using a brute force approach that has a high time complexity, not using a prefix sum array to efficiently count the number of ones in a submatrix.
- Testing considerations: Test the algorithm with different input matrices, test the algorithm with different sizes of submatrices.