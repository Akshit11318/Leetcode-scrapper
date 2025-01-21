## Match Alphanumerical Pattern in Matrix I

**Problem Link:** https://leetcode.com/problems/match-alphanumerical-pattern-in-matrix-i/description

**Problem Statement:**
- Input format and constraints: Given an `m x n` matrix `matrix` and a string `s`, return `true` if `s` can be found in the matrix by moving in `right` or `down` direction, and `false` otherwise.
- Expected output format: A boolean value indicating whether the pattern `s` can be matched in the matrix.
- Key requirements and edge cases to consider: The input matrix is a 2D array of characters, and the string `s` can be of varying lengths. The matrix can be empty, and the string can also be empty. We need to handle these edge cases properly.
- Example test cases with explanations:
  - Example 1: Input: `matrix = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]`, `s = "ABCCED"`. Output: `true`.
  - Example 2: Input: `matrix = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]`, `s = "SEE"`. Output: `true`.
  - Example 3: Input: `matrix = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]`, `s = "ABCB"`. Output: `false`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can start by checking every cell in the matrix as a potential starting point for the pattern `s`.
- Step-by-step breakdown of the solution:
  1. Iterate over each cell in the matrix.
  2. For each cell, try to match the pattern `s` by moving right or down.
  3. If the pattern `s` can be matched starting from the current cell, return `true`.
  4. If the pattern `s` cannot be matched starting from any cell, return `false`.
- Why this approach comes to mind first: This approach is straightforward and simple to implement. It checks all possible starting points and directions, ensuring that we don't miss any potential matches.

```cpp
class Solution {
public:
    bool exist(vector<vector<char>>& matrix, string s) {
        int m = matrix.size();
        int n = matrix[0].size();
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (dfs(matrix, i, j, s, 0)) {
                    return true;
                }
            }
        }
        return false;
    }
    
    bool dfs(vector<vector<char>>& matrix, int i, int j, string s, int index) {
        int m = matrix.size();
        int n = matrix[0].size();
        
        if (index == s.size()) {
            return true;
        }
        
        if (i < 0 || i >= m || j < 0 || j >= n || matrix[i][j] != s[index]) {
            return false;
        }
        
        char temp = matrix[i][j];
        matrix[i][j] = '#';
        
        bool found = dfs(matrix, i + 1, j, s, index + 1) || dfs(matrix, i, j + 1, s, index + 1);
        
        matrix[i][j] = temp;
        
        return found;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot 2^L)$, where $m$ is the number of rows, $n$ is the number of columns, and $L$ is the length of the string `s`. This is because in the worst case, we need to explore all possible directions (right and down) for each cell in the matrix.
> - **Space Complexity:** $O(L)$, which is the maximum depth of the recursion call stack. This is because we need to store the recursive call stack, which can go up to the length of the string `s`.
> - **Why these complexities occur:** The time complexity occurs because we are exploring all possible directions for each cell in the matrix, and the space complexity occurs because we need to store the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is similar to the brute force approach, but we can optimize it by using a more efficient data structure, such as a `set`, to store the visited cells. However, in this case, the optimal solution is the same as the brute force approach, as we need to explore all possible directions for each cell in the matrix.
- Detailed breakdown of the approach:
  1. Iterate over each cell in the matrix.
  2. For each cell, try to match the pattern `s` by moving right or down.
  3. If the pattern `s` can be matched starting from the current cell, return `true`.
  4. If the pattern `s` cannot be matched starting from any cell, return `false`.
- Proof of optimality: This approach is optimal because we need to explore all possible directions for each cell in the matrix to ensure that we don't miss any potential matches.

```cpp
class Solution {
public:
    bool exist(vector<vector<char>>& matrix, string s) {
        int m = matrix.size();
        int n = matrix[0].size();
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (dfs(matrix, i, j, s, 0)) {
                    return true;
                }
            }
        }
        return false;
    }
    
    bool dfs(vector<vector<char>>& matrix, int i, int j, string s, int index) {
        int m = matrix.size();
        int n = matrix[0].size();
        
        if (index == s.size()) {
            return true;
        }
        
        if (i < 0 || i >= m || j < 0 || j >= n || matrix[i][j] != s[index]) {
            return false;
        }
        
        char temp = matrix[i][j];
        matrix[i][j] = '#';
        
        bool found = dfs(matrix, i + 1, j, s, index + 1) || dfs(matrix, i, j + 1, s, index + 1);
        
        matrix[i][j] = temp;
        
        return found;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot 2^L)$, where $m$ is the number of rows, $n$ is the number of columns, and $L$ is the length of the string `s`.
> - **Space Complexity:** $O(L)$, which is the maximum depth of the recursion call stack.
> - **Optimality proof:** This approach is optimal because we need to explore all possible directions for each cell in the matrix to ensure that we don't miss any potential matches.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-First Search (DFS), recursion, and backtracking.
- Problem-solving patterns identified: Exploring all possible directions for each cell in the matrix.
- Optimization techniques learned: Using a more efficient data structure, such as a `set`, to store the visited cells.
- Similar problems to practice: Other problems that involve exploring all possible directions for each cell in a matrix, such as finding a path in a maze.

**Mistakes to Avoid:**
- Common implementation errors: Not checking the boundaries of the matrix, not handling the case where the pattern `s` is empty, and not using a more efficient data structure to store the visited cells.
- Edge cases to watch for: The matrix can be empty, and the string `s` can also be empty.
- Performance pitfalls: Not using a more efficient data structure to store the visited cells, which can lead to a higher time complexity.
- Testing considerations: Testing the function with different inputs, including edge cases, to ensure that it works correctly.