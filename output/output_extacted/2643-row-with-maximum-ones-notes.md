## Row with Maximum Ones

**Problem Link:** https://leetcode.com/problems/row-with-maximum-ones/description

**Problem Statement:**
- Input format: A 2D binary matrix `mat` of size `m x n`.
- Constraints: `1 <= m <= 10^5`, `1 <= n <= 10^5`.
- Expected output format: The index of the row with the maximum number of ones.
- Key requirements and edge cases to consider: 
  - If there are multiple rows with the same maximum number of ones, return the row with the smallest index.
  - If the input matrix is empty, return -1.
- Example test cases with explanations:
  - Example 1: `mat = [[0,1,1,1],[0,0,1,0],[0,0,1,1],[0,0,0,1]]`, Output: `3`.
  - Example 2: `mat = [[0,0,0],[0,1,0]]`, Output: `1`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Count the number of ones in each row and compare them to find the row with the maximum number of ones.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `max_count` to store the maximum number of ones found so far and `max_row` to store the index of the row with the maximum number of ones.
  2. Iterate through each row in the matrix.
  3. For each row, count the number of ones using a nested loop.
  4. If the count of ones in the current row is greater than `max_count`, update `max_count` and `max_row`.
- Why this approach comes to mind first: It is a straightforward approach that directly addresses the problem statement.

```cpp
int maxRow(vector<vector<int>>& mat) {
    int m = mat.size();
    int n = mat[0].size();
    int max_count = 0;
    int max_row = -1;
    
    for (int i = 0; i < m; i++) {
        int count = 0;
        for (int j = 0; j < n; j++) {
            if (mat[i][j] == 1) {
                count++;
            }
        }
        if (count > max_count) {
            max_count = count;
            max_row = i;
        }
    }
    return max_row;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns in the matrix. This is because we are iterating through each element in the matrix once.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the variables `max_count` and `max_row`.
> - **Why these complexities occur:** The time complexity is high because we are using nested loops to count the number of ones in each row. The space complexity is low because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of counting the number of ones in each row from scratch, we can use a single pass through the matrix to find the row with the maximum number of ones.
- Detailed breakdown of the approach:
  1. Initialize a variable `max_count` to store the maximum number of ones found so far and `max_row` to store the index of the row with the maximum number of ones.
  2. Iterate through each row in the matrix.
  3. For each row, count the number of ones by summing the elements in the row (since the elements are either 0 or 1).
  4. If the count of ones in the current row is greater than `max_count`, update `max_count` and `max_row`.
- Proof of optimality: This approach has the same time complexity as the brute force approach but with a simpler implementation. It is optimal because we must at least look at each element in the matrix once to find the row with the maximum number of ones.

```cpp
int maxRow(vector<vector<int>>& mat) {
    int m = mat.size();
    int n = mat[0].size();
    int max_count = 0;
    int max_row = -1;
    
    for (int i = 0; i < m; i++) {
        int count = 0;
        for (int j = 0; j < n; j++) {
            count += mat[i][j];
        }
        if (count > max_count) {
            max_count = count;
            max_row = i;
        }
    }
    return max_row;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns in the matrix. This is because we are iterating through each element in the matrix once.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the variables `max_count` and `max_row`.
> - **Optimality proof:** This approach is optimal because we must at least look at each element in the matrix once to find the row with the maximum number of ones.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Counting, iteration, and comparison.
- Problem-solving patterns identified: Using a single pass through the data to find the maximum or minimum value.
- Optimization techniques learned: Simplifying the implementation by using the properties of the data (in this case, the fact that the elements are either 0 or 1).
- Similar problems to practice: Finding the column with the maximum number of ones, finding the row with the minimum number of ones, etc.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing variables before using them, not checking for edge cases (e.g., an empty matrix).
- Edge cases to watch for: An empty matrix, a matrix with only one row or column, etc.
- Performance pitfalls: Using nested loops when a single loop would suffice, using unnecessary data structures, etc.
- Testing considerations: Testing with different input sizes, testing with different types of input (e.g., a matrix with all zeros, a matrix with all ones), etc.