## Word Search
**Problem Link:** https://leetcode.com/problems/word-search/description

**Problem Statement:**
- Input format: A 2D board of characters and a word.
- Constraints: The board consists of m x n characters, and the word has a length of at least 1 and at most 10.
- Expected output format: Return `true` if the word exists in the grid, `false` otherwise.
- Key requirements and edge cases to consider:
  - The word can be constructed from letters of sequentially adjacent cell, where adjacent cells are horizontally or vertically neighboring.
  - The same letter cell may not be used more than once.
- Example test cases with explanations:
  - Example 1: Given a 2D board and word = "ABCCED", the function returns `true`.
  - Example 2: Given a 2D board and word = "SEE", the function returns `true`.
  - Example 3: Given a 2D board and word = "ABCB", the function returns `false`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible path in the grid to see if the word can be formed.
- Step-by-step breakdown of the solution:
  1. Iterate over each cell in the grid.
  2. For each cell, try to form the word by exploring all possible directions (up, down, left, right).
  3. Use backtracking to explore all possible paths.
- Why this approach comes to mind first: It's the most straightforward way to solve the problem, but it's not efficient.

```cpp
class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int m = board.size();
        int n = board[0].size();
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == word[0]) {
                    if (dfs(board, word, i, j, 0)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
    
    bool dfs(vector<vector<char>>& board, string& word, int i, int j, int k) {
        if (k == word.size()) {
            return true;
        }
        
        if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || board[i][j] != word[k]) {
            return false;
        }
        
        char temp = board[i][j];
        board[i][j] = '#';
        
        bool found = dfs(board, word, i + 1, j, k + 1) ||
                      dfs(board, word, i - 1, j, k + 1) ||
                      dfs(board, word, i, j + 1, k + 1) ||
                      dfs(board, word, i, j - 1, k + 1);
        
        board[i][j] = temp;
        
        return found;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot M \cdot 4^L)$, where $N$ is the number of rows, $M$ is the number of columns, and $L$ is the length of the word. This is because we're exploring all possible paths of length $L$ from each cell.
> - **Space Complexity:** $O(L)$, where $L$ is the length of the word. This is because of the recursive call stack.
> - **Why these complexities occur:** The time complexity is high because we're exploring all possible paths, and the space complexity is due to the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a depth-first search (DFS) with backtracking to explore all possible paths, but only start the search from cells that match the first character of the word.
- Detailed breakdown of the approach:
  1. Iterate over each cell in the grid.
  2. For each cell that matches the first character of the word, start a DFS search.
  3. Use backtracking to explore all possible paths.
- Proof of optimality: This approach is optimal because it only explores possible paths that can lead to the word, reducing the number of unnecessary searches.

```cpp
class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int m = board.size();
        int n = board[0].size();
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == word[0]) {
                    if (dfs(board, word, i, j, 0)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
    
    bool dfs(vector<vector<char>>& board, string& word, int i, int j, int k) {
        if (k == word.size()) {
            return true;
        }
        
        if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || board[i][j] != word[k]) {
            return false;
        }
        
        char temp = board[i][j];
        board[i][j] = '#';
        
        bool found = dfs(board, word, i + 1, j, k + 1) ||
                      dfs(board, word, i - 1, j, k + 1) ||
                      dfs(board, word, i, j + 1, k + 1) ||
                      dfs(board, word, i, j - 1, k + 1);
        
        board[i][j] = temp;
        
        return found;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot M \cdot 4^L)$, where $N$ is the number of rows, $M$ is the number of columns, and $L$ is the length of the word. This is because we're exploring all possible paths of length $L$ from each cell that matches the first character of the word.
> - **Space Complexity:** $O(L)$, where $L$ is the length of the word. This is because of the recursive call stack.
> - **Optimality proof:** This approach is optimal because it only explores possible paths that can lead to the word, reducing the number of unnecessary searches.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-first search (DFS) with backtracking.
- Problem-solving patterns identified: Exploring all possible paths and using backtracking to reduce unnecessary searches.
- Optimization techniques learned: Only starting the search from cells that match the first character of the word.
- Similar problems to practice: Other problems that involve searching for a path in a grid or matrix.

**Mistakes to Avoid:**
- Common implementation errors: Not checking the boundaries of the grid, not using backtracking correctly.
- Edge cases to watch for: Empty grid, word longer than the grid, word not found in the grid.
- Performance pitfalls: Exploring all possible paths without using backtracking, not optimizing the search.
- Testing considerations: Test the function with different grids and words, including edge cases.