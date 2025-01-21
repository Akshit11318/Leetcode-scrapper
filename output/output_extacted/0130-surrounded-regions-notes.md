## Surrounded Regions

**Problem Link:** https://leetcode.com/problems/surrounded-regions/description

**Problem Statement:**
- Input format: A 2D `board` containing 'X' and 'O' where 'X' represents a blocked cell and 'O' represents an open cell.
- Constraints: The input `board` is a non-empty 2D array of size `m x n`, where `1 <= m, n <= 200`.
- Expected output format: Modify the input `board` in-place such that all 'O' regions not connected to the boundary are marked as 'X'.
- Key requirements and edge cases to consider: 
  - Regions are considered connected if they share an edge (not a corner).
  - The boundary of the board is the set of all cells in the first and last row, and the first and last column.
- Example test cases with explanations:
  - Input: 
    ```cpp
    [
      ['X', 'X', 'X', 'X'],
      ['X', 'O', 'O', 'X'],
      ['X', 'X', 'O', 'X'],
      ['X', 'O', 'X', 'X']
    ]
    ```
    Output:
    ```cpp
    [
      ['X', 'X', 'X', 'X'],
      ['X', 'X', 'X', 'X'],
      ['X', 'X', 'X', 'X'],
      ['X', 'O', 'X', 'X']
    ]
    ```
    Explanation: The 'O' region in the middle is not connected to the boundary, so it is marked as 'X'.

### Brute Force Approach

**Explanation:**
- Initial thought process: Identify all 'O' regions connected to the boundary and mark them as 'N' (for "not surrounded"), then mark all remaining 'O' regions as 'X', and finally mark all 'N' regions back to 'O'.
- Step-by-step breakdown of the solution:
  1. Perform a depth-first search (DFS) from each 'O' cell on the boundary to mark all connected 'O' cells as 'N'.
  2. Iterate over the board and mark all 'O' cells as 'X' (since they are not connected to the boundary).
  3. Iterate over the board again and mark all 'N' cells back to 'O' (since they are connected to the boundary).
- Why this approach comes to mind first: It's a straightforward approach that directly addresses the problem statement.

```cpp
void solve(vector<vector<char>>& board) {
    if (board.empty() || board[0].empty()) return;

    int m = board.size(), n = board[0].size();
    // Mark all 'O' regions connected to the boundary
    for (int i = 0; i < m; i++) {
        dfs(board, i, 0);
        dfs(board, i, n - 1);
    }
    for (int j = 0; j < n; j++) {
        dfs(board, 0, j);
        dfs(board, m - 1, j);
    }

    // Mark all 'O' regions not connected to the boundary as 'X'
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (board[i][j] == 'O') board[i][j] = 'X';
            if (board[i][j] == 'N') board[i][j] = 'O';
        }
    }
}

void dfs(vector<vector<char>>& board, int i, int j) {
    if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || board[i][j] != 'O') return;
    board[i][j] = 'N';
    dfs(board, i - 1, j);
    dfs(board, i + 1, j);
    dfs(board, i, j - 1);
    dfs(board, i, j + 1);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the input board. This is because in the worst case, we visit each cell once during the DFS from the boundary and once during the iteration to mark 'O' regions as 'X' and 'N' regions back to 'O'.
> - **Space Complexity:** $O(m \cdot n)$, due to the recursive call stack in the worst case when the board is filled with 'O' and we start DFS from one corner.
> - **Why these complexities occur:** The time complexity is linear because we visit each cell a constant number of times. The space complexity is due to the recursive call stack used by the DFS.

### Optimal Approach (Required)

The provided brute force approach is already optimal for this problem. It correctly identifies and marks all 'O' regions not connected to the boundary as 'X' with a time complexity of $O(m \cdot n)$ and a space complexity of $O(m \cdot n)$ due to the recursive call stack.

However, we can slightly optimize the code by reducing the number of iterations and DFS calls, but the overall time complexity remains the same.

```cpp
void solve(vector<vector<char>>& board) {
    if (board.empty() || board[0].empty()) return;

    int m = board.size(), n = board[0].size();
    for (int i = 0; i < m; i++) {
        dfs(board, i, 0);
        dfs(board, i, n - 1);
    }
    for (int j = 0; j < n; j++) {
        dfs(board, 0, j);
        dfs(board, m - 1, j);
    }

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (board[i][j] == 'O') board[i][j] = 'X';
            else if (board[i][j] == 'N') board[i][j] = 'O';
        }
    }
}

void dfs(vector<vector<char>>& board, int i, int j) {
    if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || board[i][j] != 'O') return;
    board[i][j] = 'N';
    dfs(board, i - 1, j);
    dfs(board, i + 1, j);
    dfs(board, i, j - 1);
    dfs(board, i, j + 1);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the input board.
> - **Space Complexity:** $O(m \cdot n)$, due to the recursive call stack in the worst case.
> - **Optimality proof:** This approach is optimal because it must visit each cell at least once to determine if it's part of a surrounded region or not, resulting in a linear time complexity.

### Final Notes

**Learning Points:**
- The importance of identifying connected components in a graph or grid.
- Using DFS to traverse and mark connected regions.
- Optimizing the solution by reducing unnecessary iterations and function calls.

**Mistakes to Avoid:**
- Not checking for boundary conditions in the DFS function.
- Not marking visited cells to avoid revisiting them.
- Not handling the case where the input board is empty or contains no 'O' regions.