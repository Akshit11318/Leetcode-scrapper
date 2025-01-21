# Snake in Matrix
**Problem Link:** https://leetcode.com/problems/snake-in-matrix/description

**Problem Statement:**
- Input format and constraints: Given an integer `n`, generate a `n x n` matrix where each cell contains a unique number from 1 to `n * n`, and the numbers are filled in a snake-like pattern starting from the top left corner.
- Expected output format: A 2D array representing the `n x n` matrix.
- Key requirements and edge cases to consider: The input `n` will be a positive integer, and the output matrix should have the correct snake-like pattern.
- Example test cases with explanations: For example, given `n = 3`, the output should be `[[1, 2, 3], [6, 7, 4], [5, 8, 9]]`, which represents a 3x3 matrix with a snake-like pattern.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we can start by initializing an empty `n x n` matrix. Then, we can fill in the numbers from 1 to `n * n` in a snake-like pattern by iterating over the rows and columns of the matrix.
- Step-by-step breakdown of the solution: We can use a variable `dir` to keep track of the current direction (right, down, left, or up) and update it accordingly as we fill in the numbers.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, as it directly implements the snake-like pattern.

```cpp
vector<vector<int>> generateMatrix(int n) {
    vector<vector<int>> matrix(n, vector<int>(n, 0));
    int num = 1;
    int row = 0, col = 0;
    vector<int> dx = {0, 1, 0, -1};
    vector<int> dy = {1, 0, -1, 0};
    int dir = 0;
    
    while (num <= n * n) {
        matrix[row][col] = num++;
        
        int nextRow = row + dx[dir];
        int nextCol = col + dy[dir];
        
        if (nextRow < 0 || nextRow >= n || nextCol < 0 || nextCol >= n || matrix[nextRow][nextCol] != 0) {
            dir = (dir + 1) % 4;
        }
        
        row += dx[dir];
        col += dy[dir];
    }
    
    return matrix;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the matrix. This is because we need to fill in all $n^2$ cells in the matrix.
> - **Space Complexity:** $O(n^2)$, where $n$ is the size of the matrix. This is because we need to store the entire matrix.
> - **Why these complexities occur:** The time complexity is $O(n^2)$ because we need to iterate over all cells in the matrix, and the space complexity is $O(n^2)$ because we need to store the entire matrix.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is to use the same approach as the brute force solution, but with some minor optimizations. We can use a more efficient way to update the direction `dir` and to check if the next cell is valid.
- Detailed breakdown of the approach: We can use the same variables `row`, `col`, `dx`, `dy`, and `dir` as in the brute force solution. We can also use the same loop to fill in the numbers from 1 to `n * n`.
- Proof of optimality: This solution is optimal because it has the same time and space complexity as the brute force solution, but with some minor optimizations.

```cpp
vector<vector<int>> generateMatrix(int n) {
    vector<vector<int>> matrix(n, vector<int>(n, 0));
    int num = 1;
    int row = 0, col = 0;
    vector<int> dx = {0, 1, 0, -1};
    vector<int> dy = {1, 0, -1, 0};
    int dir = 0;
    
    while (num <= n * n) {
        matrix[row][col] = num++;
        
        int nextRow = row + dx[dir];
        int nextCol = col + dy[dir];
        
        if (nextRow < 0 || nextRow >= n || nextCol < 0 || nextCol >= n || matrix[nextRow][nextCol] != 0) {
            dir = (dir + 1) % 4;
            nextRow = row + dx[dir];
            nextCol = col + dy[dir];
        }
        
        row = nextRow;
        col = nextCol;
    }
    
    return matrix;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the matrix. This is because we need to fill in all $n^2$ cells in the matrix.
> - **Space Complexity:** $O(n^2)$, where $n$ is the size of the matrix. This is because we need to store the entire matrix.
> - **Optimality proof:** This solution is optimal because it has the same time and space complexity as the brute force solution, but with some minor optimizations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of a snake-like pattern to fill in a matrix.
- Problem-solving patterns identified: The problem requires the use of a loop to fill in the numbers from 1 to `n * n`.
- Optimization techniques learned: The problem requires the use of minor optimizations to improve the efficiency of the solution.
- Similar problems to practice: Other problems that involve filling in a matrix with a specific pattern, such as a spiral pattern.

**Mistakes to Avoid:**
- Common implementation errors: One common error is to forget to update the direction `dir` when the next cell is not valid.
- Edge cases to watch for: One edge case is when the input `n` is 1, in which case the output should be a 1x1 matrix with the number 1.
- Performance pitfalls: One performance pitfall is to use a solution with a time complexity greater than $O(n^2)$.
- Testing considerations: The solution should be tested with different inputs, including edge cases, to ensure that it works correctly.