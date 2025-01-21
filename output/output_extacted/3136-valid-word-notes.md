## Valid Word
**Problem Link:** https://leetcode.com/problems/valid-word/description

**Problem Statement:**
- Input format: A string `word` representing the word to validate, and a 2D vector `square` representing a 2x2 sub-grid of a Boggle board.
- Constraints: The word must be between 1 and 10 characters long, and the Boggle board is a 2x2 grid.
- Expected output format: A boolean value indicating whether the word can be formed on the Boggle board.
- Key requirements and edge cases to consider: The word must be formed by connecting adjacent letters (horizontally, vertically, or diagonally) on the Boggle board.
- Example test cases with explanations: 
  - `word = "abnb", square = [["a","b"],["b","c"]]` returns `False` because the word "abnb" cannot be formed on the given Boggle board.
  - `word = "abnb", square = [["a","b"],["b","a"]]` returns `True` because the word "abnb" can be formed on the given Boggle board.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To check if the word can be formed on the Boggle board, we need to check all possible paths on the board.
- Step-by-step breakdown of the solution: 
  1. Define a function to check if a word can be formed at a given position on the board.
  2. Iterate over all positions on the board.
  3. For each position, check if the word can be formed starting from that position.
  4. If the word can be formed, return `True`.
  5. If the word cannot be formed at any position, return `False`.
- Why this approach comes to mind first: This approach is straightforward and involves checking all possible paths on the board.

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
    
    bool dfs(vector<vector<char>>& board, string word, int i, int j, int k) {
        int m = board.size();
        int n = board[0].size();
        
        if (k == word.size()) {
            return true;
        }
        
        if (i < 0 || i >= m || j < 0 || j >= n || board[i][j] != word[k]) {
            return false;
        }
        
        char temp = board[i][j];
        board[i][j] = '#';
        
        bool found = dfs(board, word, i + 1, j, k + 1) ||
                      dfs(board, word, i - 1, j, k + 1) ||
                      dfs(board, word, i, j + 1, k + 1) ||
                      dfs(board, word, i, j - 1, k + 1) ||
                      dfs(board, word, i + 1, j + 1, k + 1) ||
                      dfs(board, word, i - 1, j - 1, k + 1) ||
                      dfs(board, word, i + 1, j - 1, k + 1) ||
                      dfs(board, word, i - 1, j + 1, k + 1);
        
        board[i][j] = temp;
        
        return found;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(M \times N \times 8^L)$ where $M$ and $N$ are the dimensions of the board, and $L$ is the length of the word. This is because in the worst case, we need to check all possible paths of length $L$ starting from each position on the board.
> - **Space Complexity:** $O(L)$ due to the recursion stack.
> - **Why these complexities occur:** The time complexity occurs because we are checking all possible paths on the board, and the space complexity occurs because of the recursion stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is the same as the brute force approach, as we need to check all possible paths on the board to determine if the word can be formed.
- Detailed breakdown of the approach: 
  1. Define a function to check if a word can be formed at a given position on the board.
  2. Iterate over all positions on the board.
  3. For each position, check if the word can be formed starting from that position.
  4. If the word can be formed, return `True`.
  5. If the word cannot be formed at any position, return `False`.
- Proof of optimality: This solution is optimal because we need to check all possible paths on the board to determine if the word can be formed.

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
    
    bool dfs(vector<vector<char>>& board, string word, int i, int j, int k) {
        int m = board.size();
        int n = board[0].size();
        
        if (k == word.size()) {
            return true;
        }
        
        if (i < 0 || i >= m || j < 0 || j >= n || board[i][j] != word[k]) {
            return false;
        }
        
        char temp = board[i][j];
        board[i][j] = '#';
        
        bool found = dfs(board, word, i + 1, j, k + 1) ||
                      dfs(board, word, i - 1, j, k + 1) ||
                      dfs(board, word, i, j + 1, k + 1) ||
                      dfs(board, word, i, j - 1, k + 1) ||
                      dfs(board, word, i + 1, j + 1, k + 1) ||
                      dfs(board, word, i - 1, j - 1, k + 1) ||
                      dfs(board, word, i + 1, j - 1, k + 1) ||
                      dfs(board, word, i - 1, j + 1, k + 1);
        
        board[i][j] = temp;
        
        return found;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(M \times N \times 8^L)$ where $M$ and $N$ are the dimensions of the board, and $L$ is the length of the word.
> - **Space Complexity:** $O(L)$ due to the recursion stack.
> - **Optimality proof:** This solution is optimal because we need to check all possible paths on the board to determine if the word can be formed.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-first search (DFS) and backtracking.
- Problem-solving patterns identified: Checking all possible paths on the board to determine if a word can be formed.
- Optimization techniques learned: None, as this problem requires checking all possible paths.
- Similar problems to practice: Word Search II, Word Break, and Word Break II.

**Mistakes to Avoid:**
- Common implementation errors: Not checking the boundaries of the board, not marking visited cells, and not backtracking correctly.
- Edge cases to watch for: Empty board, empty word, and word longer than the board.
- Performance pitfalls: Not optimizing the DFS function to avoid redundant checks.
- Testing considerations: Test the function with different board sizes, word lengths, and edge cases.