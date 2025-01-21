## N-Queens Problem

**Problem Link:** https://leetcode.com/problems/n-queens/description

**Problem Statement:**
- Input: An integer `n` representing the size of the chessboard.
- Constraints: `1 <= n <= 9`.
- Expected Output: A list of all possible configurations of the board, where each configuration is represented as a list of strings. Each string represents a row of the board, and a `Q` denotes the position of a queen, while a `.` represents an empty space.
- Key Requirements:
  - Each queen must be placed in a unique row.
  - Each queen must be placed in a unique column.
  - No two queens can attack each other.
- Edge Cases:
  - `n = 1`: There is only one possible configuration, with the queen in the center of the board.
  - `n = 2` or `n = 3`: There are no possible configurations, as it is impossible to place the queens without any of them attacking each other.
- Example Test Cases:
  - `n = 4`: There are two possible configurations, with the queens placed in the following positions:
    - `[".Q..", "...Q", "Q...", "..Q."]`
    - `["..Q.", "Q...", "...Q", ".Q.."]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible configurations of the board and check if each configuration is valid.
- Step-by-step breakdown:
  1. Initialize an empty board with `n` rows and `n` columns.
  2. Iterate over each row of the board.
  3. For each row, iterate over each column.
  4. Place a queen in the current column of the current row.
  5. Check if the current configuration is valid by verifying that no two queens attack each other.
  6. If the configuration is valid, recursively place the remaining queens in the next rows.
  7. If a valid configuration is found, add it to the result list.
- Why this approach comes to mind first: It is a straightforward and intuitive approach, as it involves trying all possible configurations and checking their validity.

```cpp
#include <vector>
#include <string>

class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> result;
        vector<string> board(n, string(n, '.'));
        solveNQueensHelper(board, 0, result);
        return result;
    }

    void solveNQueensHelper(vector<string>& board, int row, vector<vector<string>>& result) {
        if (row == board.size()) {
            result.push_back(board);
            return;
        }
        for (int col = 0; col < board.size(); col++) {
            if (isValid(board, row, col)) {
                board[row][col] = 'Q';
                solveNQueensHelper(board, row + 1, result);
                board[row][col] = '.';
            }
        }
    }

    bool isValid(vector<string>& board, int row, int col) {
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < board.size(); j++) {
                if (board[i][j] == 'Q' && (j == col || abs(j - col) == abs(i - row))) {
                    return false;
                }
            }
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$, where $n$ is the size of the board. This is because in the worst case, we need to try all possible configurations of the board.
> - **Space Complexity:** $O(n^2)$, where $n$ is the size of the board. This is because we need to store the board and the result list.
> - **Why these complexities occur:** The time complexity occurs because we are trying all possible configurations of the board, and the space complexity occurs because we need to store the board and the result list.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use backtracking to efficiently explore all possible configurations of the board.
- Detailed breakdown:
  1. Initialize an empty board with `n` rows and `n` columns.
  2. Use a recursive function to place the queens in the board, one row at a time.
  3. For each row, iterate over each column and check if it is safe to place a queen in that column.
  4. If it is safe, place a queen in that column and recursively place the remaining queens in the next rows.
  5. If a valid configuration is found, add it to the result list.
- Proof of optimality: This approach is optimal because it uses backtracking to efficiently explore all possible configurations of the board, avoiding the need to try all possible configurations.

```cpp
#include <vector>
#include <string>

class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> result;
        vector<string> board(n, string(n, '.'));
        vector<bool> cols(n, false);
        vector<bool> diagonals(2 * n - 1, false);
        vector<bool> antiDiagonals(2 * n - 1, false);
        solveNQueensHelper(board, 0, cols, diagonals, antiDiagonals, result);
        return result;
    }

    void solveNQueensHelper(vector<string>& board, int row, vector<bool>& cols, vector<bool>& diagonals, vector<bool>& antiDiagonals, vector<vector<string>>& result) {
        if (row == board.size()) {
            result.push_back(board);
            return;
        }
        for (int col = 0; col < board.size(); col++) {
            if (!cols[col] && !diagonals[row + col] && !antiDiagonals[row - col + board.size() - 1]) {
                board[row][col] = 'Q';
                cols[col] = true;
                diagonals[row + col] = true;
                antiDiagonals[row - col + board.size() - 1] = true;
                solveNQueensHelper(board, row + 1, cols, diagonals, antiDiagonals, result);
                board[row][col] = '.';
                cols[col] = false;
                diagonals[row + col] = false;
                antiDiagonals[row - col + board.size() - 1] = false;
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$, where $n$ is the size of the board. This is because in the worst case, we need to try all possible configurations of the board.
> - **Space Complexity:** $O(n^2)$, where $n$ is the size of the board. This is because we need to store the board and the result list.
> - **Optimality proof:** This approach is optimal because it uses backtracking to efficiently explore all possible configurations of the board, avoiding the need to try all possible configurations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: backtracking, recursion.
- Problem-solving patterns identified: using boolean arrays to keep track of safe positions.
- Optimization techniques learned: using backtracking to efficiently explore all possible configurations.
- Similar problems to practice: knight's tour, Sudoku.

**Mistakes to Avoid:**
- Common implementation errors: not checking for safe positions before placing a queen.
- Edge cases to watch for: handling the base case of the recursion correctly.
- Performance pitfalls: using a naive approach that tries all possible configurations.
- Testing considerations: testing the solution with different inputs and edge cases.