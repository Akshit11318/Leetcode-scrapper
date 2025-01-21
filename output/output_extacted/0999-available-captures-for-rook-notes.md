## Available Captures for Rook

**Problem Link:** https://leetcode.com/problems/available-captures-for-rook/description

**Problem Statement:**
- Input format and constraints: The problem provides an 8x8 chessboard represented as a 2D array, with 'R' representing the rook, 'B' representing bishops, 'p' and 'P' representing pawns, and '.' representing empty cells.
- Expected output format: The number of available captures for the rook.
- Key requirements and edge cases to consider: 
  - The rook can capture any piece (except for the king) in the same row or column.
  - The rook can only move horizontally or vertically.
  - The rook can only capture a piece if there are no other pieces in between.
- Example test cases with explanations:
  - `[[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]` should return 2.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every cell on the board to see if it's a piece that can be captured by the rook.
- Step-by-step breakdown of the solution:
  1. Find the position of the rook on the board.
  2. Check all cells in the same row and column as the rook.
  3. If a cell contains a piece that can be captured (any piece except for the king), check if there are any other pieces in between the rook and the piece.
  4. If there are no other pieces in between, increment the count of available captures.
- Why this approach comes to mind first: It's a straightforward solution that checks every possible capture.

```cpp
int numRookCaptures(vector<vector<char>>& board) {
    int count = 0;
    int rookRow, rookCol;
    // Find the position of the rook
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            if (board[i][j] == 'R') {
                rookRow = i;
                rookCol = j;
                break;
            }
        }
    }
    // Check all cells in the same row as the rook
    for (int i = rookCol - 1; i >= 0; i--) {
        if (board[rookRow][i] == 'p') {
            count++;
            break;
        } else if (board[rookRow][i] == 'B' || board[rookRow][i] == 'P') {
            break;
        }
    }
    for (int i = rookCol + 1; i < 8; i++) {
        if (board[rookRow][i] == 'p') {
            count++;
            break;
        } else if (board[rookRow][i] == 'B' || board[rookRow][i] == 'P') {
            break;
        }
    }
    // Check all cells in the same column as the rook
    for (int i = rookRow - 1; i >= 0; i--) {
        if (board[i][rookCol] == 'p') {
            count++;
            break;
        } else if (board[i][rookCol] == 'B' || board[i][rookCol] == 'P') {
            break;
        }
    }
    for (int i = rookRow + 1; i < 8; i++) {
        if (board[i][rookCol] == 'p') {
            count++;
            break;
        } else if (board[i][rookCol] == 'B' || board[i][rookCol] == 'P') {
            break;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because the board size is constant (8x8).
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the position of the rook and the count of available captures.
> - **Why these complexities occur:** The time complexity is constant because we only need to check a fixed number of cells on the board. The space complexity is constant because we only use a fixed amount of space to store the position of the rook and the count of available captures.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The rook can only capture pieces in the same row or column, and we can stop checking as soon as we find a piece that can be captured or a piece that blocks the rook's path.
- Detailed breakdown of the approach:
  1. Find the position of the rook on the board.
  2. Check all cells in the same row and column as the rook, stopping as soon as we find a piece that can be captured or a piece that blocks the rook's path.
- Proof of optimality: This solution is optimal because it only checks the cells that are necessary to find all available captures.
- Why further optimization is impossible: We must check every cell in the same row and column as the rook to find all available captures.

```cpp
int numRookCaptures(vector<vector<char>>& board) {
    int count = 0;
    int rookRow, rookCol;
    // Find the position of the rook
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            if (board[i][j] == 'R') {
                rookRow = i;
                rookCol = j;
                break;
            }
        }
    }
    // Check all cells in the same row as the rook
    for (int i = rookCol - 1; i >= 0; i--) {
        if (board[rookRow][i] == 'p') {
            count++;
            break;
        } else if (board[rookRow][i] == 'B' || board[rookRow][i] == 'P') {
            break;
        }
    }
    for (int i = rookCol + 1; i < 8; i++) {
        if (board[rookRow][i] == 'p') {
            count++;
            break;
        } else if (board[rookRow][i] == 'B' || board[rookRow][i] == 'P') {
            break;
        }
    }
    // Check all cells in the same column as the rook
    for (int i = rookRow - 1; i >= 0; i--) {
        if (board[i][rookCol] == 'p') {
            count++;
            break;
        } else if (board[i][rookCol] == 'B' || board[i][rookCol] == 'P') {
            break;
        }
    }
    for (int i = rookRow + 1; i < 8; i++) {
        if (board[i][rookCol] == 'p') {
            count++;
            break;
        } else if (board[i][rookCol] == 'B' || board[i][rookCol] == 'P') {
            break;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because the board size is constant (8x8).
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the position of the rook and the count of available captures.
> - **Optimality proof:** This solution is optimal because it only checks the cells that are necessary to find all available captures.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Checking all cells in the same row and column as the rook to find available captures.
- Problem-solving patterns identified: Stopping as soon as we find a piece that can be captured or a piece that blocks the rook's path.
- Optimization techniques learned: Only checking the cells that are necessary to find all available captures.
- Similar problems to practice: Other chess-related problems, such as finding the number of available moves for a knight or a bishop.

**Mistakes to Avoid:**
- Common implementation errors: Not stopping as soon as we find a piece that can be captured or a piece that blocks the rook's path.
- Edge cases to watch for: The rook being at the edge of the board, or there being no pieces that can be captured.
- Performance pitfalls: Checking every cell on the board, rather than only checking the cells that are necessary.
- Testing considerations: Testing the function with different board configurations, including edge cases.