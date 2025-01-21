## Increment Submatrices by One
**Problem Link:** https://leetcode.com/problems/increment-submatrices-by-one/description

**Problem Statement:**
- Input: A 2D integer array `matrix` of size `m x n`, and an integer `k`.
- Constraints: `1 <= m, n <= 10^5`, `1 <= k <= m * n`, `-10^5 <= matrix[i][j] <= 10^5`.
- Expected Output: Increment all elements in `k` submatrices by `1`. 
- Key Requirements: For each submatrix, you can only increment all its elements by `1` once. 
- Example Test Cases: 
    - `matrix = [[1,2,3],[4,5,6],[7,8,9]]`, `k = 1`. 
    - `matrix = [[1,2],[2,1]]`, `k = 2`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: For each submatrix, iterate through all its elements and increment them by `1`.
- Step-by-step breakdown:
    1. Iterate through all possible submatrices in the `matrix`.
    2. For each submatrix, increment all its elements by `1`.
    3. Repeat step 2 for `k` submatrices.
- Why this approach comes to mind first: It's the most straightforward way to solve the problem, but it's inefficient.

```cpp
void incrementSubmatrices(vector<vector<int>>& matrix, int k) {
    int m = matrix.size();
    int n = matrix[0].size();
    for (int i = 0; i < k; i++) {
        // Generate a random submatrix
        int r1 = rand() % m;
        int r2 = rand() % m;
        int c1 = rand() % n;
        int c2 = rand() % n;
        // Ensure r1 <= r2 and c1 <= c2
        if (r1 > r2) swap(r1, r2);
        if (c1 > c2) swap(c1, c2);
        // Increment all elements in the submatrix
        for (int j = r1; j <= r2; j++) {
            for (int l = c1; l <= c2; l++) {
                matrix[j][l]++;
            }
        }
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k \cdot m \cdot n)$, where `m` and `n` are the dimensions of the `matrix`, and `k` is the number of submatrices to increment. 
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the loop variables.
> - **Why these complexities occur:** The time complexity is high because we're iterating through all elements in each submatrix, and we're doing this `k` times. The space complexity is low because we're not using any additional data structures that scale with the input size.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Instead of actually incrementing all elements in each submatrix, we can just keep track of the number of times each element should be incremented.
- Detailed breakdown:
    1. Create a `result` matrix with the same dimensions as the input `matrix`, filled with zeros.
    2. For each submatrix, increment the corresponding elements in the `result` matrix.
    3. Finally, add the `result` matrix to the original `matrix`.
- Proof of optimality: This approach is optimal because it only requires a single pass through the `matrix` to calculate the final result.

```cpp
void incrementSubmatrices(vector<vector<int>>& matrix, int k) {
    int m = matrix.size();
    int n = matrix[0].size();
    vector<vector<int>> result(m, vector<int>(n, 0));
    for (int i = 0; i < k; i++) {
        // Generate a random submatrix
        int r1 = rand() % m;
        int r2 = rand() % m;
        int c1 = rand() % n;
        int c2 = rand() % n;
        // Ensure r1 <= r2 and c1 <= c2
        if (r1 > r2) swap(r1, r2);
        if (c1 > c2) swap(c1, c2);
        // Increment all elements in the submatrix
        for (int j = r1; j <= r2; j++) {
            for (int l = c1; l <= c2; l++) {
                result[j][l]++;
            }
        }
    }
    // Add the result matrix to the original matrix
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            matrix[i][j] += result[i][j];
        }
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k \cdot m \cdot n + m \cdot n)$, which simplifies to $O(k \cdot m \cdot n)$ because $k \cdot m \cdot n$ dominates $m \cdot n$.
> - **Space Complexity:** $O(m \cdot n)$, because we need to store the `result` matrix.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the `matrix` to calculate the final result, and it avoids the overhead of incrementing all elements in each submatrix.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: 
    - **_Incremental Approach_**: Instead of actually incrementing all elements in each submatrix, we can just keep track of the number of times each element should be incremented.
    - **_Result Matrix_**: We can use a separate matrix to store the result of incrementing all submatrices.
- Problem-solving patterns identified: 
    - **_Optimization_**: We can optimize the solution by avoiding unnecessary work, such as incrementing all elements in each submatrix.
- Optimization techniques learned: 
    - **_Single Pass_**: We can calculate the final result in a single pass through the `matrix`.
- Similar problems to practice: 
    - **_Range Sum Query_**: Given a 2D array and a range, calculate the sum of all elements in the range.

**Mistakes to Avoid:**
- Common implementation errors: 
    - **_Off-by-One Error_**: Make sure to handle the boundaries of the `matrix` correctly.
- Edge cases to watch for: 
    - **_Empty Matrix_**: Handle the case where the `matrix` is empty.
- Performance pitfalls: 
    - **_Unnecessary Work_**: Avoid doing unnecessary work, such as incrementing all elements in each submatrix.
- Testing considerations: 
    - **_Random Test Cases_**: Test the solution with random test cases to ensure it works correctly.