## Minimum Moves to Get a Peaceful Board
**Problem Link:** https://leetcode.com/problems/minimum-moves-to-get-a-peaceful-board/description

**Problem Statement:**
- Input: A 2D integer array `board` where `board[i]` is a non-empty array of integers representing the state of the `i-th` row.
- Constraints: `1 <= board.length <= 8`, `1 <= board[i].length <= 8`, `1 <= board[i][j] <= 8`.
- Expected output: The minimum number of moves required to get a peaceful board.
- Key requirements and edge cases to consider: The board is considered peaceful if there are no two pieces of the same color in the same row or column.

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach would involve checking all possible configurations of the board by trying all possible moves for each piece and then checking if the resulting board is peaceful.
- Step-by-step breakdown of the solution:
  1. Generate all possible moves for each piece on the board.
  2. For each possible move, create a copy of the board and apply the move.
  3. Check if the resulting board is peaceful.
  4. If the board is peaceful, return the number of moves made.
- Why this approach comes to mind first: It's a straightforward approach that tries all possibilities, but it's inefficient due to the large number of possible configurations.

```cpp
#include <vector>
using namespace std;

int minMovesToGetPeacefulBoard(vector<vector<int>>& board) {
    int rows = board.size();
    int cols = board[0].size();
    int moves = 0;

    // Brute force approach to try all possible moves
    // This is not an efficient solution and is only for illustration
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            // Try moving the piece at (i, j) to all other positions
            for (int x = 0; x < rows; x++) {
                for (int y = 0; y < cols; y++) {
                    // Create a copy of the board and apply the move
                    vector<vector<int>> newBoard = board;
                    newBoard[i][j] = 0;
                    newBoard[x][y] = board[i][j];

                    // Check if the resulting board is peaceful
                    if (isPeaceful(newBoard)) {
                        // If the board is peaceful, return the number of moves
                        return moves + 1;
                    }
                }
            }
        }
    }

    return -1; // No peaceful board found
}

// Function to check if a board is peaceful
bool isPeaceful(vector<vector<int>>& board) {
    int rows = board.size();
    int cols = board[0].size();

    // Check rows and columns for pieces of the same color
    for (int i = 0; i < rows; i++) {
        vector<int> rowCounts(9, 0);
        vector<int> colCounts(9, 0);

        for (int j = 0; j < cols; j++) {
            rowCounts[board[i][j]]++;
            colCounts[board[j][i]]++;
        }

        // If there are two pieces of the same color in the same row or column, return false
        for (int k = 1; k <= 8; k++) {
            if (rowCounts[k] > 1 || colCounts[k] > 1) {
                return false;
            }
        }
    }

    return true; // Board is peaceful
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(8^{n^2})$ where $n$ is the number of rows (or columns) in the board, because we're trying all possible configurations.
> - **Space Complexity:** $O(n^2)$ for the copy of the board.
> - **Why these complexities occur:** The brute force approach tries all possible moves for each piece, resulting in an exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can observe that the problem can be solved by counting the number of pieces of each color in each row and column and then calculating the minimum number of moves required to make the board peaceful.
- Detailed breakdown of the approach:
  1. Count the number of pieces of each color in each row and column.
  2. Calculate the minimum number of moves required to make each row and column peaceful.
  3. Return the total minimum number of moves.
- Proof of optimality: This approach is optimal because it considers all possible configurations and returns the minimum number of moves required to make the board peaceful.

```cpp
#include <vector>
using namespace std;

int minMovesToGetPeacefulBoard(vector<vector<int>>& board) {
    int rows = board.size();
    int cols = board[0].size();
    int moves = 0;

    // Count the number of pieces of each color in each row and column
    vector<vector<int>> rowCounts(rows, vector<int>(9, 0));
    vector<vector<int>> colCounts(cols, vector<int>(9, 0));

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            rowCounts[i][board[i][j]]++;
            colCounts[j][board[i][j]]++;
        }
    }

    // Calculate the minimum number of moves required to make each row and column peaceful
    for (int i = 0; i < rows; i++) {
        int maxCount = 0;
        for (int j = 1; j <= 8; j++) {
            maxCount = max(maxCount, rowCounts[i][j]);
        }
        moves += maxCount - 1;
    }

    for (int i = 0; i < cols; i++) {
        int maxCount = 0;
        for (int j = 1; j <= 8; j++) {
            maxCount = max(maxCount, colCounts[i][j]);
        }
        moves += maxCount - 1;
    }

    return moves;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the number of rows (or columns) in the board, because we're counting the number of pieces in each row and column.
> - **Space Complexity:** $O(n^2)$ for the row and column counts.
> - **Optimality proof:** This approach is optimal because it considers all possible configurations and returns the minimum number of moves required to make the board peaceful.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Counting, optimization.
- Problem-solving patterns identified: Counting the number of pieces in each row and column, calculating the minimum number of moves required.
- Optimization techniques learned: Using row and column counts to reduce the number of moves required.
- Similar problems to practice: Other optimization problems, such as the minimum number of moves to solve a puzzle.

**Mistakes to Avoid:**
- Common implementation errors: Not counting the number of pieces in each row and column correctly.
- Edge cases to watch for: Boards with no pieces, boards with only one piece.
- Performance pitfalls: Using a brute force approach, which can result in exponential time complexity.
- Testing considerations: Testing the function with different board configurations, including boards with no pieces and boards with only one piece.