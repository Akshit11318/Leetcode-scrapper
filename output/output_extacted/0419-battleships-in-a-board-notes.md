## Battleships in a Board
**Problem Link:** https://leetcode.com/problems/battleships-in-a-board/description

**Problem Statement:**
- Input format: A 2D array `board` of size `m x n`, containing only characters `'.'`, `'X'`, and `'.'` represents empty spaces, and `'X'` represents parts of battleships.
- Constraints: 
  - `m == board.length`
  - `n == board[i].length`
  - `1 <= m, n <= 200`
  - `board[i][j]` is either `'.'` or `'X'`.
- Expected output: The number of battleships on the board.
- Key requirements: 
  - Each battleship occupies one or more adjacent cells in the same row, and all cells in a battleship are connected.
  - The input contains at least one `'X'`.
- Example test cases: 
  - `board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]` should return `2` because there are two battleships.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate through each cell in the board. If a cell contains an `'X'`, we then check all its adjacent cells (up, down, left, right) to see if they also contain `'X'` to determine if they belong to the same battleship.
- This approach comes to mind first because it involves checking each cell and its neighbors, which seems like a straightforward way to identify connected `'X'` cells.

```cpp
int countBattleships(vector<vector<char>>& board) {
    int count = 0;
    for (int i = 0; i < board.size(); i++) {
        for (int j = 0; j < board[0].size(); j++) {
            if (board[i][j] == 'X') {
                // Mark all connected 'X' cells as visited
                dfs(board, i, j);
                count++;
            }
        }
    }
    return count;
}

void dfs(vector<vector<char>>& board, int i, int j) {
    if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || board[i][j] != 'X') {
        return;
    }
    board[i][j] = '.'; // Mark as visited
    dfs(board, i - 1, j); // Up
    dfs(board, i + 1, j); // Down
    dfs(board, i, j - 1); // Left
    dfs(board, i, j + 1); // Right
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$ where $m$ is the number of rows and $n$ is the number of columns in the board, because in the worst case, we might visit every cell.
> - **Space Complexity:** $O(m \cdot n)$ due to the recursion stack in the worst case (when the board is filled with `'X'` and they are all connected).
> - **Why these complexities occur:** The brute force approach involves potentially visiting every cell in the board and marking its neighbors as visited, which leads to these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to only count a battleship when we encounter its top-left cell (i.e., an `'X'` that does not have an `'X'` to its left or above it). This way, we avoid counting the same battleship multiple times.
- This approach is optimal because it only requires a single pass through the board, and it directly identifies each battleship without needing to explore all its cells.

```cpp
int countBattleships(vector<vector<char>>& board) {
    int count = 0;
    for (int i = 0; i < board.size(); i++) {
        for (int j = 0; j < board[0].size(); j++) {
            if (board[i][j] == 'X' && (i == 0 || board[i-1][j] == '.') && (j == 0 || board[i][j-1] == '.')) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$ where $m$ and $n$ are the dimensions of the board, as we make a single pass through the board.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the count of battleships.
> - **Optimality proof:** This is the best possible time complexity because we must at least look at each cell once to determine if it's part of a battleship. The space complexity is optimal as we only use a constant amount of space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, condition checking, and optimization by only counting top-left cells of battleships.
- Problem-solving patterns identified: Identifying the key characteristic of the problem (in this case, the top-left cell of a battleship) to optimize the solution.
- Optimization techniques learned: Reducing the number of operations by only counting each battleship once.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for the boundaries of the board when accessing cells.
- Edge cases to watch for: Boards with no battleships, boards with only one cell, and boards filled with battleships.
- Performance pitfalls: Using unnecessary data structures or algorithms that increase time or space complexity.
- Testing considerations: Ensure to test with various board sizes, battleship configurations, and edge cases.