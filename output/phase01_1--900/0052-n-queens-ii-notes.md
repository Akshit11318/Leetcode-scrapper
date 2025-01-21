## N-Queens II
**Problem Link:** https://leetcode.com/problems/n-queens-ii/description

**Problem Statement:**
- Input format and constraints: The problem takes an integer `n` as input, representing the size of the chessboard.
- Expected output format: The output is the number of distinct solutions to place `n` queens on an `n x n` chessboard such that no two queens attack each other.
- Key requirements and edge cases to consider: The solution should ensure that no two queens share the same row, column, or diagonal.
- Example test cases with explanations: For `n = 4`, there are two distinct solutions.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to generate all possible configurations of the board and check each one to see if it satisfies the conditions.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of `n` columns.
  2. For each permutation, check if any pair of queens attacks each other.
  3. If no queens attack each other, increment the count of valid configurations.
- Why this approach comes to mind first: It is straightforward and easy to implement, but it is inefficient due to the large number of possible configurations.

```cpp
class Solution {
public:
    int totalNQueens(int n) {
        vector<int> board(n, -1);
        int count = 0;
        solve(board, 0, count);
        return count;
    }
    
    void solve(vector<int>& board, int row, int& count) {
        if (row == board.size()) {
            count++;
            return;
        }
        for (int col = 0; col < board.size(); col++) {
            if (isValid(board, row, col)) {
                board[row] = col;
                solve(board, row + 1, count);
                board[row] = -1;
            }
        }
    }
    
    bool isValid(vector<int>& board, int row, int col) {
        for (int i = 0; i < row; i++) {
            if (board[i] == col || 
                board[i] - i == col - row || 
                board[i] + i == col + row) {
                return false;
            }
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N!)$, where $N$ is the number of queens. This is because we are generating all permutations of the columns.
> - **Space Complexity:** $O(N)$, where $N$ is the number of queens. This is because we are storing the current configuration of the board.
> - **Why these complexities occur:** The time complexity is high because we are generating all possible configurations, and the space complexity is relatively low because we only need to store the current configuration.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use backtracking to efficiently explore all possible configurations.
- Detailed breakdown of the approach:
  1. Start with an empty board.
  2. Try to place a queen in each column of the current row.
  3. For each placement, check if it is valid (i.e., no queens attack each other).
  4. If it is valid, recursively try to place queens in the next row.
  5. If it is not valid, backtrack and try the next placement.
- Proof of optimality: This approach is optimal because it explores all possible configurations without generating unnecessary ones.
- Why further optimization is impossible: This approach has a time complexity of $O(N!)$, which is the best possible time complexity for this problem because we must generate all possible configurations.

```cpp
class Solution {
public:
    int totalNQueens(int n) {
        vector<int> board(n, -1);
        int count = 0;
        solve(board, 0, count);
        return count;
    }
    
    void solve(vector<int>& board, int row, int& count) {
        if (row == board.size()) {
            count++;
            return;
        }
        for (int col = 0; col < board.size(); col++) {
            if (isValid(board, row, col)) {
                board[row] = col;
                solve(board, row + 1, count);
                board[row] = -1;
            }
        }
    }
    
    bool isValid(vector<int>& board, int row, int col) {
        for (int i = 0; i < row; i++) {
            if (board[i] == col || 
                board[i] - i == col - row || 
                board[i] + i == col + row) {
                return false;
            }
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N!)$, where $N$ is the number of queens. This is because we are generating all permutations of the columns.
> - **Space Complexity:** $O(N)$, where $N$ is the number of queens. This is because we are storing the current configuration of the board.
> - **Optimality proof:** This approach is optimal because it explores all possible configurations without generating unnecessary ones.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Backtracking, recursion.
- Problem-solving patterns identified: Exploring all possible configurations, using backtracking to efficiently explore the search space.
- Optimization techniques learned: Using backtracking to avoid generating unnecessary configurations.
- Similar problems to practice: N-Queens, Sudoku, Knight's Tour.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for validity before placing a queen, not backtracking correctly.
- Edge cases to watch for: Empty board, board with one queen.
- Performance pitfalls: Generating all possible configurations without using backtracking.
- Testing considerations: Test with different board sizes, test with different initial configurations.