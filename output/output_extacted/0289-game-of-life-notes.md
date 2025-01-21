## Game of Life
**Problem Link:** https://leetcode.com/problems/game-of-life/description

**Problem Statement:**
- Input format and constraints: The input is a 2D `board` of size `m x n`, where each cell has one of two possible values:
  - `0`: Dead cell
  - `1`: Live cell
- Expected output format: Modify the input `board` in-place to represent the next state of the game.
- Key requirements and edge cases to consider:
  - Any live cell with fewer than two live neighbours dies, as if by underpopulation.
  - Any live cell with two or three live neighbours lives on to the next generation.
  - Any live cell with more than three live neighbours dies, as if by overpopulation.
  - Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
- Example test cases with explanations:
  - Given a board with live cells, the next state should reflect the rules of the game.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Create a copy of the original board to store the next state, then iterate over each cell to apply the rules of the game.
- Step-by-step breakdown of the solution:
  1. Create a copy of the original board.
  2. Iterate over each cell in the original board.
  3. For each cell, count the number of live neighbours.
  4. Apply the rules of the game to determine the next state of the cell.
  5. Update the corresponding cell in the copy of the board with the next state.
- Why this approach comes to mind first: It's a straightforward way to solve the problem, but it requires extra space to store the copy of the board.

```cpp
void gameOfLife(vector<vector<int>>& board) {
    int m = board.size();
    int n = board[0].size();
    vector<vector<int>> copyBoard(m, vector<int>(n));
    
    // Copy the original board
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            copyBoard[i][j] = board[i][j];
        }
    }
    
    // Apply the rules of the game
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            int liveNeighbours = 0;
            
            // Count the number of live neighbours
            for (int x = -1; x <= 1; x++) {
                for (int y = -1; y <= 1; y++) {
                    int ni = i + x;
                    int nj = j + y;
                    
                    if (x == 0 && y == 0) continue;
                    if (ni < 0 || ni >= m || nj < 0 || nj >= n) continue;
                    
                    if (copyBoard[ni][nj] == 1) liveNeighbours++;
                }
            }
            
            // Apply the rules of the game
            if (copyBoard[i][j] == 1 && (liveNeighbours < 2 || liveNeighbours > 3)) {
                board[i][j] = 0;
            } else if (copyBoard[i][j] == 0 && liveNeighbours == 3) {
                board[i][j] = 1;
            }
        }
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the board. This is because we need to iterate over each cell in the board.
> - **Space Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the board. This is because we need to store a copy of the original board.
> - **Why these complexities occur:** The time complexity occurs because we need to iterate over each cell in the board, and the space complexity occurs because we need to store a copy of the original board.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of creating a copy of the original board, we can use the values of the cells to represent both the current state and the next state.
- Detailed breakdown of the approach:
  1. Iterate over each cell in the board.
  2. For each cell, count the number of live neighbours.
  3. Apply the rules of the game to determine the next state of the cell.
  4. Update the cell with a special value that represents both the current state and the next state.
- Why further optimization is impossible: This approach has the same time complexity as the brute force approach, but it uses less space because it doesn't require a copy of the board.

```cpp
void gameOfLife(vector<vector<int>>& board) {
    int m = board.size();
    int n = board[0].size();
    
    // Apply the rules of the game
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            int liveNeighbours = 0;
            
            // Count the number of live neighbours
            for (int x = -1; x <= 1; x++) {
                for (int y = -1; y <= 1; y++) {
                    int ni = i + x;
                    int nj = j + y;
                    
                    if (x == 0 && y == 0) continue;
                    if (ni < 0 || ni >= m || nj < 0 || nj >= n) continue;
                    
                    if (board[ni][nj] == 1 || board[ni][nj] == -1) liveNeighbours++;
                }
            }
            
            // Apply the rules of the game
            if (board[i][j] == 1 && (liveNeighbours < 2 || liveNeighbours > 3)) {
                board[i][j] = -1;
            } else if (board[i][j] == 0 && liveNeighbours == 3) {
                board[i][j] = 2;
            }
        }
    }
    
    // Update the board with the next state
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (board[i][j] == -1) board[i][j] = 0;
            if (board[i][j] == 2) board[i][j] = 1;
        }
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the board. This is because we need to iterate over each cell in the board.
> - **Space Complexity:** $O(1)$, where the space complexity is constant because we don't need to store a copy of the original board.
> - **Optimality proof:** This approach is optimal because it has the same time complexity as the brute force approach, but it uses less space because it doesn't require a copy of the board.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The game of life is a classic example of a cellular automaton, where the next state of a cell is determined by its current state and the states of its neighbours.
- Problem-solving patterns identified: The problem requires iterating over each cell in the board and applying the rules of the game to determine the next state.
- Optimization techniques learned: The optimal approach uses less space than the brute force approach by using the values of the cells to represent both the current state and the next state.
- Similar problems to practice: Other problems that involve iterating over a grid or matrix and applying rules to determine the next state, such as the `Surrounded Regions` problem.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the board correctly, or not counting the number of live neighbours correctly.
- Edge cases to watch for: The board may have a size of 0 or 1, or the cells may have invalid values.
- Performance pitfalls: Using too much space or time, or not optimizing the solution correctly.
- Testing considerations: Test the solution with different board sizes and cell values to ensure that it works correctly.