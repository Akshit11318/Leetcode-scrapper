## Minesweeper
**Problem Link:** https://leetcode.com/problems/minesweeper/description

**Problem Statement:**
- Input format: A 2D integer array `board` representing the game board, where `board[i][j]` can have the following values:
  - `-1` representing a mine
  - `0` representing an empty cell
  - A positive number representing the number of mines adjacent to the cell
- Input constraints:
  - The board will have a size of `m x n`, where `m` and `n` are between `1` and `200`.
  - The board will only contain integers in the range `[-1, 0, 1, 2, ..., 8]`.
- Expected output format: The modified board after the first click at position `(x, y)`.
- Key requirements and edge cases to consider:
  - If the clicked cell is a mine, mark all mines with `X` and reveal all non-mine cells.
  - If the clicked cell is not a mine, reveal the cell and all its adjacent cells that are not mines, using the standard rules of Minesweeper.
- Example test cases with explanations:
  - Example 1:
    - Input: `board = [[-1,1,0,0],[1,1,0,0],[0,0,1,-1],[1,0,0,0]]`, `x = 3`, `y = 4`
    - Output: `[[-1,1,0,0],[1,1,0,0],[0,0,1,-1],[1,2,2,1]]`
  - Example 2:
    - Input: `board = [[1,2,0],[0,1,-1],[0,0,0]]`, `x = 0`, `y = 2`
    - Output: `[[1,2,0],[0,1,-1],[0,0,0]]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The simplest approach would be to implement the game logic of Minesweeper from scratch, including revealing cells, counting adjacent mines, and handling the game over condition.
- Step-by-step breakdown of the solution:
  1. Create a copy of the board to store the current state of the game.
  2. When a cell is clicked, check if it is a mine. If it is, mark all mines with `X` and reveal all non-mine cells.
  3. If the clicked cell is not a mine, reveal the cell and all its adjacent cells that are not mines, using the standard rules of Minesweeper.
- Why this approach comes to mind first: It directly implements the game logic, making it easy to understand and visualize the solution.

```cpp
class Solution {
public:
    vector<vector<char>> updateBoard(vector<vector<char>>& board, vector<int>& click) {
        int m = board.size();
        int n = board[0].size();
        int x = click[0];
        int y = click[1];
        
        if (board[x][y] == 'M') {
            board[x][y] = 'X';
            return board;
        }
        
        dfs(board, x, y);
        
        return board;
    }
    
    void dfs(vector<vector<char>>& board, int x, int y) {
        int m = board.size();
        int n = board[0].size();
        
        if (x < 0 || x >= m || y < 0 || y >= n || board[x][y] != 'E') {
            return;
        }
        
        int count = countMines(board, x, y);
        
        if (count > 0) {
            board[x][y] = '0' + count;
            return;
        }
        
        board[x][y] = 'B';
        
        dfs(board, x - 1, y);
        dfs(board, x + 1, y);
        dfs(board, x, y - 1);
        dfs(board, x, y + 1);
        dfs(board, x - 1, y - 1);
        dfs(board, x - 1, y + 1);
        dfs(board, x + 1, y - 1);
        dfs(board, x + 1, y + 1);
    }
    
    int countMines(vector<vector<char>>& board, int x, int y) {
        int m = board.size();
        int n = board[0].size();
        int count = 0;
        
        for (int i = -1; i <= 1; i++) {
            for (int j = -1; j <= 1; j++) {
                int nx = x + i;
                int ny = y + j;
                
                if (nx < 0 || nx >= m || ny < 0 || ny >= n) {
                    continue;
                }
                
                if (board[nx][ny] == 'M') {
                    count++;
                }
            }
        }
        
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the board. This is because in the worst case, we need to reveal all cells on the board.
> - **Space Complexity:** $O(m \cdot n)$, due to the recursive call stack in the worst case.
> - **Why these complexities occur:** The time complexity is due to the need to potentially reveal all cells on the board, while the space complexity is due to the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is to use a depth-first search (DFS) to reveal the cells, similar to the brute force approach. However, we can optimize the solution by only exploring the cells that are adjacent to the clicked cell and have not been revealed yet.
- Detailed breakdown of the approach:
  1. When a cell is clicked, check if it is a mine. If it is, mark all mines with `X` and reveal all non-mine cells.
  2. If the clicked cell is not a mine, use DFS to reveal the cell and all its adjacent cells that are not mines.
- Proof of optimality: The optimal solution has a time complexity of $O(m \cdot n)$, which is the best possible time complexity for this problem because we need to potentially reveal all cells on the board.

```cpp
class Solution {
public:
    vector<vector<char>> updateBoard(vector<vector<char>>& board, vector<int>& click) {
        int m = board.size();
        int n = board[0].size();
        int x = click[0];
        int y = click[1];
        
        if (board[x][y] == 'M') {
            board[x][y] = 'X';
            return board;
        }
        
        dfs(board, x, y);
        
        return board;
    }
    
    void dfs(vector<vector<char>>& board, int x, int y) {
        int m = board.size();
        int n = board[0].size();
        
        if (x < 0 || x >= m || y < 0 || y >= n || board[x][y] != 'E') {
            return;
        }
        
        int count = countMines(board, x, y);
        
        if (count > 0) {
            board[x][y] = '0' + count;
            return;
        }
        
        board[x][y] = 'B';
        
        dfs(board, x - 1, y);
        dfs(board, x + 1, y);
        dfs(board, x, y - 1);
        dfs(board, x, y + 1);
        dfs(board, x - 1, y - 1);
        dfs(board, x - 1, y + 1);
        dfs(board, x + 1, y - 1);
        dfs(board, x + 1, y + 1);
    }
    
    int countMines(vector<vector<char>>& board, int x, int y) {
        int m = board.size();
        int n = board[0].size();
        int count = 0;
        
        for (int i = -1; i <= 1; i++) {
            for (int j = -1; j <= 1; j++) {
                int nx = x + i;
                int ny = y + j;
                
                if (nx < 0 || nx >= m || ny < 0 || ny >= n) {
                    continue;
                }
                
                if (board[nx][ny] == 'M') {
                    count++;
                }
            }
        }
        
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the board. This is because in the worst case, we need to reveal all cells on the board.
> - **Space Complexity:** $O(m \cdot n)$, due to the recursive call stack in the worst case.
> - **Optimality proof:** The optimal solution has a time complexity of $O(m \cdot n)$, which is the best possible time complexity for this problem because we need to potentially reveal all cells on the board.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-first search (DFS) and recursive functions.
- Problem-solving patterns identified: Using DFS to reveal cells in a grid-based game.
- Optimization techniques learned: Avoiding unnecessary exploration of cells that have already been revealed.
- Similar problems to practice: Other grid-based games or problems that involve revealing cells, such as Sudoku or Battleship.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for out-of-bounds cells or not handling the game over condition correctly.
- Edge cases to watch for: Cells that are adjacent to the clicked cell but have already been revealed, or cells that are mines.
- Performance pitfalls: Using an inefficient data structure or algorithm, such as a brute force approach that explores all cells on the board.
- Testing considerations: Testing the solution with different input boards and click positions to ensure that it works correctly in all cases.