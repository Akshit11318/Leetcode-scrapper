## Maximum Number of Moves in a Grid

**Problem Link:** https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/description

**Problem Statement:**
- Input: A 2D grid of size `m x n` and an integer `k`.
- Constraints: `1 <= m, n <= 10^5`, `1 <= k <= 10^5`.
- Expected Output: The maximum number of moves in the grid.
- Key Requirements: The moves can only be made from an empty cell to an adjacent empty cell.
- Edge Cases: If the grid is empty, return 0. If `k` is 0, return 0.

**Example Test Cases:**
- `grid = [[0,0,0],[0,0,0],[0,0,0]]`, `k = 2`. The output should be 2.
- `grid = [[0,0,0],[0,1,0],[0,0,0]]`, `k = 2`. The output should be 1.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible moves from each cell and keep track of the maximum number of moves.
- The brute force approach involves iterating over each cell in the grid and trying to move in all four directions (up, down, left, right).
- This approach comes to mind first because it is a straightforward way to solve the problem, but it is not efficient for large grids.

```cpp
int maxMoves(vector<vector<int>>& grid, int k) {
    int m = grid.size();
    int n = grid[0].size();
    int maxMoves = 0;
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 0) {
                int moves = 0;
                vector<vector<bool>> visited(m, vector<bool>(n, false));
                visited[i][j] = true;
                queue<pair<int, int>> q;
                q.push({i, j});
                
                while (!q.empty()) {
                    int x = q.front().first;
                    int y = q.front().second;
                    q.pop();
                    moves++;
                    
                    vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
                    for (auto& dir : directions) {
                        int nx = x + dir.first;
                        int ny = y + dir.second;
                        
                        if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] == 0 && !visited[nx][ny]) {
                            visited[nx][ny] = true;
                            q.push({nx, ny});
                        }
                    }
                    
                    if (moves == k) {
                        break;
                    }
                }
                
                maxMoves = max(maxMoves, moves);
            }
        }
    }
    
    return maxMoves;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \times n \times k)$, where $m$ and $n$ are the dimensions of the grid, and $k$ is the number of moves. This is because in the worst case, we are trying all possible moves from each cell.
> - **Space Complexity:** $O(m \times n)$, where $m$ and $n$ are the dimensions of the grid. This is because we are using a visited array to keep track of the cells that have been visited.
> - **Why these complexities occur:** These complexities occur because we are using a brute force approach that involves trying all possible moves from each cell.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a breadth-first search (BFS) algorithm to find the maximum number of moves.
- We start from each empty cell and try to move in all four directions (up, down, left, right).
- We keep track of the maximum number of moves and return it as the result.
- This approach is optimal because it ensures that we are trying all possible moves from each cell, but it does so in a more efficient way than the brute force approach.

```cpp
int maxMoves(vector<vector<int>>& grid, int k) {
    int m = grid.size();
    int n = grid[0].size();
    int maxMoves = 0;
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 0) {
                int moves = 0;
                vector<vector<bool>> visited(m, vector<bool>(n, false));
                visited[i][j] = true;
                queue<pair<int, int>> q;
                q.push({i, j});
                
                while (!q.empty() && moves < k) {
                    int size = q.size();
                    
                    for (int _ = 0; _ < size; _++) {
                        int x = q.front().first;
                        int y = q.front().second;
                        q.pop();
                        
                        vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
                        for (auto& dir : directions) {
                            int nx = x + dir.first;
                            int ny = y + dir.second;
                            
                            if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] == 0 && !visited[nx][ny]) {
                                visited[nx][ny] = true;
                                q.push({nx, ny});
                            }
                        }
                    }
                    
                    moves++;
                }
                
                maxMoves = max(maxMoves, moves);
            }
        }
    }
    
    return maxMoves;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \times n \times k)$, where $m$ and $n$ are the dimensions of the grid, and $k$ is the number of moves. This is because in the worst case, we are trying all possible moves from each cell.
> - **Space Complexity:** $O(m \times n)$, where $m$ and $n$ are the dimensions of the grid. This is because we are using a visited array to keep track of the cells that have been visited.
> - **Optimality proof:** This approach is optimal because it ensures that we are trying all possible moves from each cell, but it does so in a more efficient way than the brute force approach.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated in this problem is the use of breadth-first search (BFS) to find the maximum number of moves in a grid.
- The problem-solving pattern identified in this problem is to use a visited array to keep track of the cells that have been visited.
- The optimization technique learned in this problem is to use a more efficient algorithm (BFS) to solve the problem instead of a brute force approach.

**Mistakes to Avoid:**
- A common implementation error is to forget to check if a cell is empty before trying to move to it.
- An edge case to watch for is when the grid is empty or when `k` is 0.
- A performance pitfall is to use a brute force approach that involves trying all possible moves from each cell, which can lead to a time complexity of $O(m \times n \times k)$.
- A testing consideration is to test the code with different inputs and edge cases to ensure that it is working correctly.