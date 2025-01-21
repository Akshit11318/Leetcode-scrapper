## Check Knight Tour Configuration

**Problem Link:** https://leetcode.com/problems/check-knight-tour-configuration/description

**Problem Statement:**
- Input: An 8x8 `board` representing a chessboard, where 0 indicates an empty space and 1 indicates a space visited by a knight.
- Constraints: The board will contain at most 64 cells with a value of 1.
- Expected Output: `true` if the given configuration is a valid knight tour, `false` otherwise.
- Key Requirements: 
  - A knight can move in an L-shape (two squares in one direction, then one square to the side).
  - A valid knight tour visits each square exactly once.
- Edge Cases:
  - An empty board (all zeros).
  - A board with a single 1.
  - A board with multiple disjoint knight tours.
- Example Test Cases:
  - A board with a valid knight tour (all squares visited exactly once).
  - A board with an invalid knight tour (some squares visited more than once, or not all squares visited).

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking all possible knight moves from each square to see if we can visit all squares exactly once.
- We can use a recursive function to explore all possible moves and check if the current configuration is a valid knight tour.
- This approach comes to mind first because it directly addresses the problem statement, but it's inefficient due to the large number of possible moves.

```cpp
bool checkKnightTour(vector<vector<int>>& board) {
    int n = board.size();
    vector<pair<int, int>> moves = {{-2, -1}, {-2, 1}, {-1, -2}, {-1, 2}, {1, -2}, {1, 2}, {2, -1}, {2, 1}};
    vector<vector<bool>> visited(n, vector<bool>(n, false));
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (board[i][j] == 1) {
                visited[i][j] = true;
            }
        }
    }
    
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (visited[i][j]) {
                count++;
            }
        }
    }
    
    if (count == n * n) {
        return true;
    }
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (visited[i][j]) {
                for (auto& move : moves) {
                    int x = i + move.first;
                    int y = j + move.second;
                    
                    if (x >= 0 && x < n && y >= 0 && y < n && !visited[x][y]) {
                        visited[x][y] = true;
                        if (checkKnightTour(board)) {
                            return true;
                        }
                        visited[x][y] = false;
                    }
                }
            }
        }
    }
    
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(8^n)$, where $n$ is the number of squares on the board, because we're exploring all possible moves from each square.
> - **Space Complexity:** $O(n)$, where $n$ is the number of squares on the board, because we're using a recursive function and a visited array.
> - **Why these complexities occur:** The time complexity is high because we're using a recursive function to explore all possible moves, and the space complexity is relatively low because we're only using a visited array to keep track of visited squares.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is that we can use a **backtracking algorithm** to check if the given configuration is a valid knight tour.
- We start from the first square that is visited by the knight and try to visit all the remaining squares exactly once.
- We use a `visited` array to keep track of visited squares and a `moves` array to store all possible moves from a square.
- If we can visit all squares exactly once, we return `true`; otherwise, we return `false`.

```cpp
bool checkKnightTour(vector<vector<int>>& board) {
    int n = board.size();
    vector<pair<int, int>> moves = {{-2, -1}, {-2, 1}, {-1, -2}, {-1, 2}, {1, -2}, {1, 2}, {2, -1}, {2, 1}};
    vector<vector<bool>> visited(n, vector<bool>(n, false));
    
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (board[i][j] == 1) {
                visited[i][j] = true;
                count++;
            }
        }
    }
    
    if (count == n * n) {
        return true;
    }
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (visited[i][j]) {
                for (auto& move : moves) {
                    int x = i + move.first;
                    int y = j + move.second;
                    
                    if (x >= 0 && x < n && y >= 0 && y < n && !visited[x][y]) {
                        visited[x][y] = true;
                        if (checkKnightTour(board)) {
                            return true;
                        }
                        visited[x][y] = false;
                    }
                }
            }
        }
    }
    
    return false;
}
```

However, the optimal solution would actually involve checking the given configuration directly without trying to generate all possible knight tours. We can do this by checking if the number of visited squares is equal to the number of moves made by the knight, which should be one less than the number of visited squares.

```cpp
bool checkKnightTour(vector<vector<int>>& board) {
    int n = board.size();
    vector<pair<int, int>> moves = {{-2, -1}, {-2, 1}, {-1, -2}, {-1, 2}, {1, -2}, {1, 2}, {2, -1}, {2, 1}};
    vector<vector<bool>> visited(n, vector<bool>(n, false));
    
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (board[i][j] == 1) {
                visited[i][j] = true;
                count++;
            }
        }
    }
    
    if (count == n * n) {
        return true;
    }
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (visited[i][j]) {
                int validMoves = 0;
                for (auto& move : moves) {
                    int x = i + move.first;
                    int y = j + move.second;
                    
                    if (x >= 0 && x < n && y >= 0 && y < n) {
                        if (!visited[x][y]) {
                            validMoves++;
                        }
                    }
                }
                
                if (validMoves > 2) {
                    return false;
                }
            }
        }
    }
    
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of squares on the board, because we're checking each square exactly once.
> - **Space Complexity:** $O(n^2)$, where $n$ is the number of squares on the board, because we're using a visited array to keep track of visited squares.
> - **Optimality proof:** This solution is optimal because it directly checks the given configuration without trying to generate all possible knight tours.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated in this problem is the use of a **backtracking algorithm** to check if the given configuration is a valid knight tour.
- The problem-solving pattern identified in this problem is the use of a **visited array** to keep track of visited squares.
- The optimization technique learned in this problem is the use of a **direct check** to verify if the given configuration is a valid knight tour, rather than trying to generate all possible knight tours.

**Mistakes to Avoid:**
- A common implementation error is to use a recursive function without a proper base case, which can lead to a **stack overflow**.
- An edge case to watch for is when the input board is empty or contains only a single 1, which requires special handling.
- A performance pitfall is to use a **brute force approach** to generate all possible knight tours, which can be very inefficient.
- A testing consideration is to test the solution with different input boards, including valid and invalid knight tours, to ensure that the solution works correctly in all cases.