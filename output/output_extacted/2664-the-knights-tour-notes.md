## The Knight's Tour
**Problem Link:** https://leetcode.com/problems/the-knights-tour/description

**Problem Statement:**
- Input format and constraints: The problem involves finding a knight's tour on an `n x n` chessboard. The knight can move in an `L` shape (two squares in one direction, then one square to the side). The input is an integer `n`, representing the size of the chessboard. The output should be a 2D array representing the order of moves.
- Expected output format: A 2D array where each cell contains the move number (starting from 1) that the knight visits that cell.
- Key requirements and edge cases to consider: The knight must visit each cell exactly once, and the tour must be possible. If a tour is not possible, return an empty array.
- Example test cases with explanations: For example, on a `3 x 3` board, the knight can visit each cell in the following order: `[[1, 6, 3], [8, 5, 2], [7, 4, 9]]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves trying all possible moves from each cell and backtracking when a dead end is reached.
- Step-by-step breakdown of the solution:
  1. Initialize an empty board with all cells set to 0.
  2. Start at a random cell (e.g., the top-left cell).
  3. Try all possible moves from the current cell.
  4. For each possible move, check if the destination cell is empty (i.e., its value is 0).
  5. If the destination cell is empty, mark it with the next move number and recursively try all possible moves from that cell.
  6. If a dead end is reached (i.e., no more possible moves), backtrack to the previous cell and try the next possible move.
- Why this approach comes to mind first: This approach is intuitive because it involves trying all possible moves and backtracking when necessary.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> tourOfKnight(int n) {
        vector<vector<int>> board(n, vector<int>(n, 0));
        vector<pair<int, int>> moves = {{-2, -1}, {-1, -2}, {1, -2}, {2, -1}, {2, 1}, {1, 2}, {-1, 2}, {-2, 1}};
        if (!dfs(board, 0, 0, 1, moves)) {
            return {};
        }
        return board;
    }

    bool dfs(vector<vector<int>>& board, int x, int y, int step, vector<pair<int, int>>& moves) {
        if (step > board.size() * board.size()) {
            return true;
        }
        board[x][y] = step;
        for (auto& move : moves) {
            int newX = x + move.first;
            int newY = y + move.second;
            if (newX >= 0 && newX < board.size() && newY >= 0 && newY < board.size() && board[newX][newY] == 0) {
                if (dfs(board, newX, newY, step + 1, moves)) {
                    return true;
                }
            }
        }
        board[x][y] = 0;
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(8^n)$, where $n$ is the size of the board. This is because in the worst case, we try all possible moves from each cell.
> - **Space Complexity:** $O(n^2)$, where $n$ is the size of the board. This is because we need to store the board and the recursive call stack.
> - **Why these complexities occur:** The time complexity is high because we try all possible moves from each cell, and the space complexity is moderate because we need to store the board and the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The knight's tour problem can be solved using Warnsdorff's rule, which involves choosing the next move that leads to the cell with the fewest possible moves.
- Detailed breakdown of the approach:
  1. Initialize an empty board with all cells set to 0.
  2. Start at a random cell (e.g., the top-left cell).
  3. Try all possible moves from the current cell.
  4. For each possible move, count the number of possible moves from the destination cell.
  5. Choose the move that leads to the cell with the fewest possible moves.
  6. Mark the chosen cell with the next move number and recursively try all possible moves from that cell.
- Proof of optimality: Warnsdorff's rule is a heuristic that leads to a solution in most cases, but it is not guaranteed to find a solution in all cases. However, it is the most efficient known algorithm for solving the knight's tour problem.

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> tourOfKnight(int n) {
        vector<vector<int>> board(n, vector<int>(n, 0));
        vector<pair<int, int>> moves = {{-2, -1}, {-1, -2}, {1, -2}, {2, -1}, {2, 1}, {1, 2}, {-1, 2}, {-2, 1}};
        if (!warnsdorff(board, 0, 0, 1, moves)) {
            return {};
        }
        return board;
    }

    bool warnsdorff(vector<vector<int>>& board, int x, int y, int step, vector<pair<int, int>>& moves) {
        if (step > board.size() * board.size()) {
            return true;
        }
        board[x][y] = step;
        vector<pair<int, int>> nextMoves;
        for (auto& move : moves) {
            int newX = x + move.first;
            int newY = y + move.second;
            if (newX >= 0 && newX < board.size() && newY >= 0 && newY < board.size() && board[newX][newY] == 0) {
                nextMoves.push_back({newX, newY});
            }
        }
        if (nextMoves.empty()) {
            return false;
        }
        sort(nextMoves.begin(), nextMoves.end(), [&](pair<int, int> a, pair<int, int> b) {
            return degree(board, a.first, a.second, moves) < degree(board, b.first, b.second, moves);
        });
        for (auto& nextMove : nextMoves) {
            if (warnsdorff(board, nextMove.first, nextMove.second, step + 1, moves)) {
                return true;
            }
        }
        board[x][y] = 0;
        return false;
    }

    int degree(vector<vector<int>>& board, int x, int y, vector<pair<int, int>>& moves) {
        int degree = 0;
        for (auto& move : moves) {
            int newX = x + move.first;
            int newY = y + move.second;
            if (newX >= 0 && newX < board.size() && newY >= 0 && newY < board.size() && board[newX][newY] == 0) {
                degree++;
            }
        }
        return degree;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(8n)$, where $n$ is the size of the board. This is because we try all possible moves from each cell, but we use Warnsdorff's rule to choose the next move.
> - **Space Complexity:** $O(n^2)$, where $n$ is the size of the board. This is because we need to store the board and the recursive call stack.
> - **Optimality proof:** Warnsdorff's rule is a heuristic that leads to a solution in most cases, but it is not guaranteed to find a solution in all cases. However, it is the most efficient known algorithm for solving the knight's tour problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Backtracking, recursion, and heuristics.
- Problem-solving patterns identified: The knight's tour problem is a classic example of a backtracking problem, where we try all possible moves and backtrack when necessary.
- Optimization techniques learned: Warnsdorff's rule is a heuristic that can be used to optimize the solution to the knight's tour problem.
- Similar problems to practice: Other backtracking problems, such as the N-Queens problem and the Sudoku problem.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for out-of-bounds moves, not marking visited cells, and not backtracking correctly.
- Edge cases to watch for: The knight's tour problem has several edge cases, including the case where the board size is odd or even, and the case where the starting cell is in a corner or not.
- Performance pitfalls: The knight's tour problem can be slow if not implemented correctly, especially for large board sizes. Using Warnsdorff's rule can help optimize the solution.