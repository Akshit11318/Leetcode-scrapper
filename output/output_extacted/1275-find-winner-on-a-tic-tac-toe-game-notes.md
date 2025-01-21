## Find Winner on a Tic Tac Toe Game
**Problem Link:** https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/description

**Problem Statement:**
- Input format: a 2D vector `moves` of size `n x 2` where `moves[i] = [row_i, col_i]` represents the `i-th` move. `n` is guaranteed to be even and between 2 and 9 (inclusive).
- Constraints: The game board is 3x3, and players take turns marking a square on the board with their respective symbols (either 'X' or 'O').
- Expected output format: Return `'X'` if 'X' wins, `'O'` if 'O' wins, and `'Draw'` if there is no winner.
- Key requirements and edge cases to consider: Handle cases where there are no moves, the game is not finished yet, or it's a draw.
- Example test cases with explanations:
  - Example 1:
    - Input: `moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]`
    - Output: `"X"`
  - Example 2:
    - Input: `moves = [[0,0],[1,1],[0,2],[1,0],[1,2],[2,0]]`
    - Output: `"O"`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To determine the winner, we need to simulate the game based on the given moves and check after each move if there is a winner.
- Step-by-step breakdown of the solution:
  1. Initialize a 3x3 board.
  2. Iterate through each move and update the board accordingly.
  3. After each move, check rows, columns, and diagonals for a winner.
- Why this approach comes to mind first: It directly simulates the game process, making it intuitive but potentially inefficient due to repeated checks.

```cpp
class Solution {
public:
    string tictactoe(vector<vector<int>>& moves) {
        vector<vector<char>> board(3, vector<char>(3, ' '));
        for (int i = 0; i < moves.size(); i++) {
            if (i % 2 == 0) {
                board[moves[i][0]][moves[i][1]] = 'X';
            } else {
                board[moves[i][0]][moves[i][1]] = 'O';
            }
            if (checkWinner(board, 'X')) return "X";
            if (checkWinner(board, 'O')) return "O";
        }
        if (moves.size() < 9) return "Pending";
        return "Draw";
    }
    
    bool checkWinner(vector<vector<char>>& board, char player) {
        // Check rows and columns
        for (int i = 0; i < 3; i++) {
            if (board[i][0] == player && board[i][1] == player && board[i][2] == player) return true;
            if (board[0][i] == player && board[1][i] == player && board[2][i] == player) return true;
        }
        // Check diagonals
        if ((board[0][0] == player && board[1][1] == player && board[2][2] == player) ||
            (board[0][2] == player && board[1][1] == player && board[2][0] == player)) return true;
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of moves. In each move, we perform a constant amount of work to update the board and check for a winner.
> - **Space Complexity:** $O(1)$, as we use a fixed-size board and a constant amount of space to store variables.
> - **Why these complexities occur:** The time complexity is linear because we potentially check for a winner after each move, and the space complexity is constant because the size of the board and the number of variables do not grow with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking for a winner after each move, we can directly determine the winner based on the given moves without simulating the game step by step.
- Detailed breakdown of the approach:
  1. Count the number of moves made by 'X' and 'O'.
  2. Determine the possible winning lines (rows, columns, diagonals) and check if any player has three of their symbols in a line.
  3. If a player has won, return that player. Otherwise, if all squares are filled and no player has won, return 'Draw'. If not all squares are filled, return 'Pending'.
- Proof of optimality: This approach is optimal because it directly calculates the outcome without unnecessary steps, achieving the same result in less computational work.

```cpp
class Solution {
public:
    string tictactoe(vector<vector<int>>& moves) {
        vector<vector<int>> rows(3, 0), cols(3, 0), diag(2, 0);
        int player = 1;
        for (auto& move : moves) {
            rows[move[0]] += player;
            cols[move[1]] += player;
            if (move[0] == move[1]) diag[0] += player;
            if (move[0] + move[1] == 2) diag[1] += player;
            if (abs(rows[move[0]]) == 3 || abs(cols[move[1]]) == 3 || abs(diag[0]) == 3 || abs(diag[1]) == 3) {
                return player == 1 ? "X" : "O";
            }
            player *= -1;
        }
        return moves.size() == 9 ? "Draw" : "Pending";
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of moves. We iterate through each move once.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space to store the row, column, and diagonal sums.
> - **Optimality proof:** This approach is optimal because it processes each move exactly once and uses a minimal amount of extra space to track the game state.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Direct calculation, iteration, and conditional checks.
- Problem-solving patterns identified: Checking for a winner in a game by examining possible winning combinations.
- Optimization techniques learned: Reducing the number of checks and directly calculating the outcome.
- Similar problems to practice: Other game-related problems, such as determining the winner in a different type of game or solving puzzles.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly updating the game state or not checking all possible winning combinations.
- Edge cases to watch for: Handling cases where the game is not finished, it's a draw, or there are no moves.
- Performance pitfalls: Unnecessary checks or iterations that increase the time complexity.
- Testing considerations: Ensuring that the solution works correctly for all possible inputs and edge cases.