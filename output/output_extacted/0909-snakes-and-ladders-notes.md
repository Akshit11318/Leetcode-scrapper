## Snakes and Ladders
**Problem Link:** https://leetcode.com/problems/snakes-and-ladders/description

**Problem Statement:**
- Input format: A 2D grid `board` representing the snakes and ladders game board.
- Constraints: The board is a square grid with dimensions `n x n`, where `n` is an integer between 1 and 20.
- Expected output format: The minimum number of moves required to reach the square `n*n` from the square 1, or `-1` if it's impossible to reach the target square.
- Key requirements and edge cases to consider:
  - The game starts from square 1.
  - The player can move the dice in a clockwise direction.
  - If the player lands on a square with a snake or ladder, they must move to the square indicated by the snake or ladder.
  - If the player lands on a square that is out of the board's bounds, the move is invalid.
- Example test cases with explanations:
  - For example, given a board `[[1,-1,-1],[-1,2,-1],[-1,-1,-1]]`, the output should be `2` because the player can move from square 1 to square 2, then from square 2 to square 3.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can use a recursive approach to try all possible moves from each square and keep track of the minimum number of moves required to reach the target square.
- Step-by-step breakdown of the solution:
  1. Start from square 1 and try all possible moves (1-6) using a dice roll.
  2. For each move, check if the new square is within the board's bounds and if it's a valid move (i.e., not landing on a square with a snake or ladder that would move us backward).
  3. If the new square is valid, recursively call the function to try all possible moves from the new square.
  4. Keep track of the minimum number of moves required to reach the target square.
- Why this approach comes to mind first: It's a straightforward and intuitive approach that tries all possible moves, but it's inefficient due to the high number of recursive calls.

```cpp
class Solution {
public:
    int snakesAndLadders(vector<vector<int>>& board) {
        int n = board.size();
        vector<int> cells;
        for (int i = n - 1; i >= 0; --i) {
            for (int j = (i % 2 == 0) ? 0 : n - 1; j < n && (j >= 0); j += (i % 2 == 0) ? 1 : -1) {
                cells.push_back(board[i][j]);
            }
        }
        return bfs(cells);
    }

    int bfs(vector<int>& cells) {
        queue<pair<int, int>> q; // {cell index, number of moves}
        vector<bool> visited(cells.size(), false);
        q.push({0, 0});
        visited[0] = true;
        while (!q.empty()) {
            auto [cell, moves] = q.front();
            q.pop();
            if (cell == cells.size() - 1) {
                return moves;
            }
            for (int i = 1; i <= 6; ++i) {
                int nextCell = cell + i;
                if (nextCell >= cells.size()) {
                    continue;
                }
                if (cells[nextCell] != -1) {
                    nextCell = cells[nextCell] - 1;
                }
                if (!visited[nextCell]) {
                    q.push({nextCell, moves + 1});
                    visited[nextCell] = true;
                }
            }
        }
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot 6^d)$, where $d$ is the minimum number of moves required to reach the target square. The reason is that in the worst case, we need to try all possible moves from each square, and there are $6$ possible moves for each square.
> - **Space Complexity:** $O(n^2)$, where $n$ is the size of the board. The reason is that we need to store the visited squares to avoid revisiting them.
> - **Why these complexities occur:** The brute force approach tries all possible moves from each square, which leads to an exponential time complexity. The space complexity is due to the need to store the visited squares.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a breadth-first search (BFS) algorithm to try all possible moves from each square in a level order, which reduces the time complexity significantly.
- Detailed breakdown of the approach:
  1. Create a queue to store the squares to be visited, along with the number of moves required to reach each square.
  2. Start from square 1 and add it to the queue.
  3. While the queue is not empty, dequeue a square and try all possible moves (1-6) using a dice roll.
  4. For each move, check if the new square is within the board's bounds and if it's a valid move (i.e., not landing on a square with a snake or ladder that would move us backward).
  5. If the new square is valid, add it to the queue if it has not been visited before.
  6. Keep track of the minimum number of moves required to reach the target square.
- Why further optimization is impossible: The BFS algorithm tries all possible moves in a level order, which is the most efficient way to find the minimum number of moves required to reach the target square.

```cpp
class Solution {
public:
    int snakesAndLadders(vector<vector<int>>& board) {
        int n = board.size();
        vector<int> cells;
        for (int i = n - 1; i >= 0; --i) {
            for (int j = (i % 2 == 0) ? 0 : n - 1; j < n && (j >= 0); j += (i % 2 == 0) ? 1 : -1) {
                cells.push_back(board[i][j]);
            }
        }
        return bfs(cells);
    }

    int bfs(vector<int>& cells) {
        queue<pair<int, int>> q; // {cell index, number of moves}
        vector<bool> visited(cells.size(), false);
        q.push({0, 0});
        visited[0] = true;
        while (!q.empty()) {
            auto [cell, moves] = q.front();
            q.pop();
            if (cell == cells.size() - 1) {
                return moves;
            }
            for (int i = 1; i <= 6; ++i) {
                int nextCell = cell + i;
                if (nextCell >= cells.size()) {
                    continue;
                }
                if (cells[nextCell] != -1) {
                    nextCell = cells[nextCell] - 1;
                }
                if (!visited[nextCell]) {
                    q.push({nextCell, moves + 1});
                    visited[nextCell] = true;
                }
            }
        }
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the board. The reason is that we need to visit each square at most once.
> - **Space Complexity:** $O(n^2)$, where $n$ is the size of the board. The reason is that we need to store the visited squares to avoid revisiting them.
> - **Optimality proof:** The BFS algorithm tries all possible moves in a level order, which is the most efficient way to find the minimum number of moves required to reach the target square.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS algorithm, queue data structure, and visited array to avoid revisiting squares.
- Problem-solving patterns identified: Using a queue to store squares to be visited and trying all possible moves in a level order.
- Optimization techniques learned: Using a BFS algorithm to reduce the time complexity from exponential to linear.
- Similar problems to practice: Other problems that involve finding the minimum number of moves required to reach a target state, such as the "Minimum Moves to Equal Array Elements" problem.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if a square is within the board's bounds before trying a move, or not handling the case where a square has a snake or ladder that moves us backward.
- Edge cases to watch for: The case where the target square is not reachable, or the case where the board has a size of 1x1.
- Performance pitfalls: Using a recursive approach instead of an iterative approach, or not using a visited array to avoid revisiting squares.
- Testing considerations: Testing the function with different board sizes and configurations, and checking the output for correctness.