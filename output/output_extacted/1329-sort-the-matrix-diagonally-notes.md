## Sort the Matrix Diagonally
**Problem Link:** https://leetcode.com/problems/sort-the-matrix-diagonally/description

**Problem Statement:**
- Input: A 2D array `mat` of integers, where `mat[i][j]` represents an element in the matrix.
- Constraints: The input matrix `mat` is a non-empty 2D array with dimensions `m x n`, where `1 <= m, n <= 100` and `1 <= mat[i][j] <= 100`.
- Expected output: The input matrix `mat` modified in-place, where all elements in each diagonal from top-left to bottom-right are sorted in ascending order.
- Key requirements and edge cases to consider:
  - The input matrix may contain duplicate elements.
  - The input matrix may have different numbers of rows and columns.
- Example test cases with explanations:
  - `mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]`, the output should be `[[1,1,1,1],[1,2,2,2],[1,2,3,3]]`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to extract each diagonal, sort it, and then replace the elements in the original matrix with the sorted ones.
- Step-by-step breakdown of the solution:
  1. Identify all diagonals in the matrix by iterating over each element and calculating its diagonal index as `i - j`, where `i` is the row index and `j` is the column index.
  2. For each diagonal, extract its elements into a vector.
  3. Sort the vector of elements for each diagonal.
  4. Replace the original elements in the matrix with the sorted elements from the vector, maintaining their diagonal positions.
- Why this approach comes to mind first: It directly addresses the requirement of sorting each diagonal without considering the complexity of the operations involved.

```cpp
void diagonalSort(vector<vector<int>>& mat) {
    int m = mat.size();
    int n = mat[0].size();
    map<int, vector<int>> diagonals;

    // Extract elements into diagonals
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            int diagonalIndex = i - j;
            diagonals[diagonalIndex].push_back(mat[i][j]);
        }
    }

    // Sort each diagonal
    for (auto& pair : diagonals) {
        sort(pair.second.begin(), pair.second.end());
    }

    // Replace original elements with sorted ones
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            int diagonalIndex = i - j;
            mat[i][j] = diagonals[diagonalIndex].back();
            diagonals[diagonalIndex].pop_back();
        }
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot \log(m + n))$, where $m$ is the number of rows and $n$ is the number of columns. This is because we iterate over each element in the matrix to extract diagonals ($O(m \cdot n)$), and then sort each diagonal ($O(\log(m + n))$) considering the maximum size of a diagonal can be $m + n - 1$.
> - **Space Complexity:** $O(m \cdot n)$, as we store all elements of the matrix in the `diagonals` map.
> - **Why these complexities occur:** The time complexity is dominated by the sorting operation for each diagonal, and the space complexity is due to storing all elements in the `diagonals` map.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a similar approach as the brute force but optimize the sorting and replacement process by directly using the indices of the matrix to store and retrieve elements for each diagonal.
- Detailed breakdown of the approach:
  1. Initialize a map to store the diagonals, where each key represents a diagonal index and the value is a vector of elements in that diagonal.
  2. Iterate through the matrix, and for each element, calculate its diagonal index and store it in the corresponding vector in the map.
  3. Sort each vector in the map.
  4. Iterate through the matrix again, and for each element, replace it with the next element from its corresponding sorted diagonal vector.
- Proof of optimality: This approach is optimal because it minimizes the number of operations needed to sort each diagonal without unnecessary data movements or complex data structures beyond the map and vectors.

```cpp
void diagonalSort(vector<vector<int>>& mat) {
    int m = mat.size();
    int n = mat[0].size();
    map<int, vector<int>> diagonals;

    // Extract and sort diagonals
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            int diagonalIndex = i - j;
            diagonals[diagonalIndex].push_back(mat[i][j]);
        }
    }

    for (auto& pair : diagonals) {
        sort(pair.second.begin(), pair.second.end());
    }

    // Replace original elements with sorted ones
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            int diagonalIndex = i - j;
            mat[i][j] = diagonals[diagonalIndex].back();
            diagonals[diagonalIndex].pop_back();
        }
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot \log(m + n))$, where $m$ is the number of rows and $n$ is the number of columns. This is because we iterate over each element in the matrix to extract diagonals ($O(m \cdot n)$), and then sort each diagonal ($O(\log(m + n))$).
> - **Space Complexity:** $O(m \cdot n)$, as we store all elements of the matrix in the `diagonals` map.
> - **Optimality proof:** This is the optimal approach because it directly addresses the problem statement with the minimum number of operations required to sort each diagonal, leveraging the inherent structure of the matrix and the properties of maps and vectors in C++.

---

### Final Notes
**Learning Points:**
- The importance of understanding the problem structure and identifying key insights (in this case, the diagonal indexing).
- The use of maps and vectors for efficient data storage and manipulation.
- The application of sorting algorithms to solve problems involving ordered data.
- The analysis of time and space complexity to evaluate the efficiency of algorithms.

**Mistakes to Avoid:**
- Not considering the diagonal indexing, leading to incorrect or inefficient solutions.
- Failing to optimize the sorting and replacement process, resulting in higher time complexity.
- Not validating the input matrix for empty or invalid cases.
- Insufficient testing for edge cases, such as matrices with duplicate elements or varying dimensions.