## Check If Move Is Legal
**Problem Link:** https://leetcode.com/problems/check-if-move-is-legal/description

**Problem Statement:**
- Input format and constraints: The problem involves a game board represented as an 8x8 grid, where each cell can be empty or occupied by a piece. The input includes the current state of the board and the proposed move (source and destination coordinates).
- Expected output format: The function should return a boolean indicating whether the proposed move is legal according to the game's rules.
- Key requirements and edge cases to consider:
  - The source and destination cells must be within the board boundaries.
  - The source cell must contain a piece.
  - The destination cell must be empty or contain a piece of the opposite color.
  - The move must follow the game's rules for piece movement.
- Example test cases with explanations:
  - Moving a piece to an adjacent cell.
  - Moving a piece to a cell occupied by a piece of the same color.
  - Moving a piece to a cell that is not reachable according to the game's rules.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to manually check each possible move from the source cell to determine if it is legal. This involves checking all possible destinations within the board boundaries and verifying that the destination cell is empty or contains a piece of the opposite color.
- Step-by-step breakdown of the solution:
  1. Define the possible moves for each piece type (e.g., knight, bishop, rook, queen, king, pawn).
  2. Iterate through all possible moves from the source cell.
  3. For each possible move, check if the destination cell is within the board boundaries and if it is empty or contains a piece of the opposite color.
  4. If a legal move is found, return true. If no legal moves are found, return false.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, as it involves manually checking all possible moves.

```cpp
bool isLegalMove(vector<vector<int>>& board, int sourceX, int sourceY, int destX, int destY) {
    // Check if source and destination cells are within board boundaries
    if (sourceX < 0 || sourceX >= board.size() || sourceY < 0 || sourceY >= board[0].size() ||
        destX < 0 || destX >= board.size() || destY < 0 || destY >= board[0].size()) {
        return false;
    }

    // Check if source cell contains a piece
    if (board[sourceX][sourceY] == 0) {
        return false;
    }

    // Check if destination cell is empty or contains a piece of the opposite color
    if (board[destX][destY] != 0 && board[sourceX][sourceY] == board[destX][destY]) {
        return false;
    }

    // Define possible moves for each piece type
    vector<vector<int>> possibleMoves = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};

    // Iterate through all possible moves from source cell
    for (auto move : possibleMoves) {
        int newX = sourceX + move[0];
        int newY = sourceY + move[1];

        // Check if destination cell is within board boundaries and is empty or contains a piece of the opposite color
        if (newX >= 0 && newX < board.size() && newY >= 0 && newY < board[0].size() &&
            (board[newX][newY] == 0 || board[newX][newY] != board[sourceX][sourceY])) {
            // Check if the move follows the game's rules for piece movement
            if (isMoveValid(board, sourceX, sourceY, newX, newY)) {
                return true;
            }
        }
    }

    return false;
}

// Function to check if a move is valid according to the game's rules for piece movement
bool isMoveValid(vector<vector<int>>& board, int sourceX, int sourceY, int destX, int destY) {
    // Implement game-specific rules for piece movement
    // For example, a knight moves in an L-shape, a bishop moves diagonally, etc.
    // This function is not implemented here as it depends on the specific game rules
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of rows in the board and $m$ is the number of columns. This is because we are iterating through all possible moves from the source cell.
> - **Space Complexity:** $O(1)$, as we are not using any additional data structures that scale with the input size.
> - **Why these complexities occur:** The time complexity occurs because we are manually checking all possible moves from the source cell, which can be time-consuming for large boards. The space complexity is low because we are not using any additional data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of manually checking all possible moves from the source cell, we can use a more efficient algorithm that takes into account the specific game rules for piece movement.
- Detailed breakdown of the approach:
  1. Define a function to check if a move is valid according to the game's rules for piece movement.
  2. Use a more efficient algorithm to check if the proposed move is legal, such as using a `set` to store the possible moves from the source cell.
  3. Iterate through the possible moves and check if the destination cell is within the board boundaries and if it is empty or contains a piece of the opposite color.
- Proof of optimality: This approach is optimal because it uses a more efficient algorithm to check if the proposed move is legal, reducing the time complexity to $O(1)$.
- Why further optimization is impossible: This approach is already optimal because it uses a more efficient algorithm to check if the proposed move is legal, and it is not possible to reduce the time complexity further.

```cpp
bool isLegalMove(vector<vector<int>>& board, int sourceX, int sourceY, int destX, int destY) {
    // Check if source and destination cells are within board boundaries
    if (sourceX < 0 || sourceX >= board.size() || sourceY < 0 || sourceY >= board[0].size() ||
        destX < 0 || destX >= board.size() || destY < 0 || destY >= board[0].size()) {
        return false;
    }

    // Check if source cell contains a piece
    if (board[sourceX][sourceY] == 0) {
        return false;
    }

    // Check if destination cell is empty or contains a piece of the opposite color
    if (board[destX][destY] != 0 && board[sourceX][sourceY] == board[destX][destY]) {
        return false;
    }

    // Define possible moves for each piece type
    vector<vector<int>> possibleMoves = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};

    // Use a set to store the possible moves from the source cell
    set<pair<int, int>> possibleMovesSet;
    for (auto move : possibleMoves) {
        int newX = sourceX + move[0];
        int newY = sourceY + move[1];

        // Check if destination cell is within board boundaries and is empty or contains a piece of the opposite color
        if (newX >= 0 && newX < board.size() && newY >= 0 && newY < board[0].size() &&
            (board[newX][newY] == 0 || board[newX][newY] != board[sourceX][sourceY])) {
            possibleMovesSet.insert({newX, newY});
        }
    }

    // Check if the proposed move is in the set of possible moves
    return possibleMovesSet.find({destX, destY}) != possibleMovesSet.end();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, as we are using a `set` to store the possible moves from the source cell, which allows for constant-time lookup.
> - **Space Complexity:** $O(1)$, as we are not using any additional data structures that scale with the input size.
> - **Optimality proof:** This approach is optimal because it uses a more efficient algorithm to check if the proposed move is legal, reducing the time complexity to $O(1)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a `set` to store possible moves from the source cell, and using a more efficient algorithm to check if the proposed move is legal.
- Problem-solving patterns identified: Using a more efficient algorithm to solve the problem, and using data structures such as `set` to improve the solution.
- Optimization techniques learned: Using a `set` to store possible moves from the source cell, and using a more efficient algorithm to check if the proposed move is legal.
- Similar problems to practice: Other problems that involve checking if a move is legal according to specific game rules.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the source and destination cells are within the board boundaries, not checking if the source cell contains a piece, and not checking if the destination cell is empty or contains a piece of the opposite color.
- Edge cases to watch for: The source and destination cells being outside the board boundaries, the source cell not containing a piece, and the destination cell not being empty or containing a piece of the opposite color.
- Performance pitfalls: Using a brute-force approach to check if the proposed move is legal, which can result in high time complexity.
- Testing considerations: Testing the function with different input scenarios, including different board sizes, piece positions, and proposed moves.