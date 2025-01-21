## Design Tic Tac Toe

**Problem Link:** [https://leetcode.com/problems/design-tic-tac-toe/description](https://leetcode.com/problems/design-tic-tac-toe/description)

**Problem Statement:**
- Input format and constraints: The game is played between two players, X and O, on a 3x3 grid. The input will be the player's move, represented as a pair of integers (row, column).
- Expected output format: The output will be 0 if there is no winner, 1 if player 1 (X) wins, and 2 if player 2 (O) wins.
- Key requirements and edge cases to consider: The game will end when a player has three of their marks in a row, column, or diagonal, or when all squares are filled (a draw).
- Example test cases with explanations:
  - Test case 1: `board = ["XOX", "OXO", "XOX"]`, the function should return 1 because player 1 (X) wins.
  - Test case 2: `board = ["OOO", "XXX", "OOX"]`, the function should return 0 because there is no winner.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to solve this problem is to check all possible winning combinations after each move.
- Step-by-step breakdown of the solution:
  1. Initialize an empty board.
  2. For each move, update the board and check all possible winning combinations.
  3. If a winning combination is found, return the winner.
- Why this approach comes to mind first: It is the most straightforward way to solve the problem, but it is not the most efficient.

```cpp
class TicTacToe {
public:
    vector<vector<int>> board;
    int n;
    TicTacToe(int n) {
        this->n = n;
        board = vector<vector<int>>(n, vector<int>(n, 0));
    }
    
    int move(int row, int col, int player) {
        board[row][col] = player;
        // Check rows
        for (int i = 0; i < n; i++) {
            bool allSame = true;
            for (int j = 1; j < n; j++) {
                if (board[i][j] != board[i][0] || board[i][j] == 0) {
                    allSame = false;
                    break;
                }
            }
            if (allSame && board[i][0] != 0) {
                return board[i][0];
            }
        }
        // Check columns
        for (int i = 0; i < n; i++) {
            bool allSame = true;
            for (int j = 1; j < n; j++) {
                if (board[j][i] != board[0][i] || board[j][i] == 0) {
                    allSame = false;
                    break;
                }
            }
            if (allSame && board[0][i] != 0) {
                return board[0][i];
            }
        }
        // Check diagonals
        bool allSame1 = true;
        bool allSame2 = true;
        for (int i = 1; i < n; i++) {
            if (board[i][i] != board[0][0] || board[i][i] == 0) {
                allSame1 = false;
            }
            if (board[i][n - i - 1] != board[0][n - 1] || board[i][n - i - 1] == 0) {
                allSame2 = false;
            }
        }
        if (allSame1 && board[0][0] != 0) {
            return board[0][0];
        }
        if (allSame2 && board[0][n - 1] != 0) {
            return board[0][n - 1];
        }
        // If no winner, check if the board is full
        bool full = true;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 0) {
                    full = false;
                    break;
                }
            }
        }
        if (full) {
            return 0;
        }
        return 0;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the board. This is because we need to check all cells in the worst case.
> - **Space Complexity:** $O(n^2)$, where $n$ is the size of the board. This is because we need to store the board.
> - **Why these complexities occur:** The time complexity occurs because we need to check all possible winning combinations after each move, which requires iterating over the entire board. The space complexity occurs because we need to store the board.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking all possible winning combinations after each move, we can only check the row, column, and diagonal that the current move belongs to.
- Detailed breakdown of the approach:
  1. Initialize an empty board.
  2. For each move, update the board and check the row, column, and diagonal that the current move belongs to.
  3. If a winning combination is found, return the winner.
- Proof of optimality: This approach is optimal because it only checks the necessary cells after each move, reducing the time complexity to $O(1)$.
- Why further optimization is impossible: This approach is already optimal because it only checks the necessary cells after each move.

```cpp
class TicTacToe {
public:
    int n;
    vector<int> rows;
    vector<int> cols;
    int diagonal1;
    int diagonal2;
    TicTacToe(int n) {
        this->n = n;
        rows = vector<int>(n, 0);
        cols = vector<int>(n, 0);
        diagonal1 = 0;
        diagonal2 = 0;
    }
    
    int move(int row, int col, int player) {
        int val = (player == 1) ? 1 : -1;
        rows[row] += val;
        cols[col] += val;
        if (row == col) {
            diagonal1 += val;
        }
        if (row + col == n - 1) {
            diagonal2 += val;
        }
        if (rows[row] == n || cols[col] == n || diagonal1 == n || diagonal2 == n) {
            return 1;
        }
        if (rows[row] == -n || cols[col] == -n || diagonal1 == -n || diagonal2 == -n) {
            return 2;
        }
        return 0;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, where $n$ is the size of the board. This is because we only need to check the row, column, and diagonal that the current move belongs to.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the board. This is because we need to store the rows, columns, and diagonals.
> - **Optimality proof:** This approach is optimal because it only checks the necessary cells after each move, reducing the time complexity to $O(1)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The importance of checking only the necessary cells after each move.
- Problem-solving patterns identified: The use of rows, columns, and diagonals to keep track of the game state.
- Optimization techniques learned: Reducing the time complexity by only checking the necessary cells.
- Similar problems to practice: Other games like Connect Four or Gomoku.

**Mistakes to Avoid:**
- Common implementation errors: Not checking all possible winning combinations.
- Edge cases to watch for: The case where the board is full and there is no winner.
- Performance pitfalls: Checking all possible winning combinations after each move.
- Testing considerations: Testing the game with different inputs and edge cases.