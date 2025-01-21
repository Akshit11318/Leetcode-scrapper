## Candy Crush
**Problem Link:** https://leetcode.com/problems/candy-crush/description

**Problem Statement:**
- Input format and constraints: Given a 2D array `board` representing a Candy Crush game, where `board[i][j]` is the type of candy at position `(i, j)` on the board. The goal is to crush candies of the same type that are adjacent to each other (horizontally or vertically) and then drop the remaining candies to fill the gaps.
- Expected output format: Return the resulting board after crushing and dropping candies.
- Key requirements and edge cases to consider:
  - Crushing candies of the same type that are adjacent to each other.
  - Dropping the remaining candies to fill the gaps.
  - Handling cases where there are no candies to crush.
- Example test cases with explanations:
  - `board = [[110, 5, 112, 113, 114], [210, 211, 5, 213, 214], [310, 311, 3, 313, 314], [410, 411, 412, 5, 414], [5, 1, 5, 3, 5]]`
  - `board = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: We can iterate through the board to find adjacent candies of the same type (horizontally and vertically) and mark them for crushing.
- Step-by-step breakdown of the solution:
  1. Create a copy of the board to mark candies for crushing.
  2. Iterate through the board to find adjacent candies of the same type and mark them for crushing.
  3. Iterate through the board to drop the remaining candies to fill the gaps.
- Why this approach comes to mind first: It's a straightforward approach that directly implements the problem's requirements.

```cpp
class Solution {
public:
    vector<vector<int>> candyCrush(vector<vector<int>>& board) {
        int m = board.size();
        int n = board[0].size();
        bool crushed = false;
        
        // Iterate through the board to find adjacent candies of the same type and mark them for crushing
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] != 0) {
                    // Check for horizontal crush
                    if (j < n - 2 && board[i][j] == board[i][j + 1] && board[i][j] == board[i][j + 2]) {
                        board[i][j] = board[i][j + 1] = board[i][j + 2] = 0;
                        crushed = true;
                    }
                    
                    // Check for vertical crush
                    if (i < m - 2 && board[i][j] == board[i + 1][j] && board[i][j] == board[i + 2][j]) {
                        board[i][j] = board[i + 1][j] = board[i + 2][j] = 0;
                        crushed = true;
                    }
                }
            }
        }
        
        // Drop the remaining candies to fill the gaps
        for (int j = 0; j < n; j++) {
            int bottom = m - 1;
            for (int i = m - 1; i >= 0; i--) {
                if (board[i][j] != 0) {
                    board[bottom--][j] = board[i][j];
                }
            }
            for (int i = bottom; i >= 0; i--) {
                board[i][j] = 0;
            }
        }
        
        // If no candies were crushed, return the original board
        if (!crushed) {
            return board;
        }
        
        // Recursively call the function to crush and drop candies until no more candies can be crushed
        return candyCrush(board);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns in the board. The time complexity is linear with respect to the size of the board because we iterate through the board a constant number of times.
> - **Space Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns in the board. The space complexity is linear with respect to the size of the board because we create a copy of the board to mark candies for crushing.
> - **Why these complexities occur:** The time complexity occurs because we iterate through the board to find adjacent candies of the same type and mark them for crushing, and then we iterate through the board to drop the remaining candies to fill the gaps. The space complexity occurs because we create a copy of the board to mark candies for crushing.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a more efficient data structure, such as a `vector` of `vectors`, to represent the board and mark candies for crushing. We can also use a more efficient algorithm, such as a single pass through the board, to find adjacent candies of the same type and mark them for crushing.
- Detailed breakdown of the approach:
  1. Create a `vector` of `vectors` to represent the board.
  2. Iterate through the board to find adjacent candies of the same type and mark them for crushing.
  3. Iterate through the board to drop the remaining candies to fill the gaps.
- Proof of optimality: The time complexity of the optimal solution is $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns in the board. This is because we iterate through the board a constant number of times to find adjacent candies of the same type and mark them for crushing, and then we iterate through the board to drop the remaining candies to fill the gaps.

```cpp
class Solution {
public:
    vector<vector<int>> candyCrush(vector<vector<int>>& board) {
        int m = board.size();
        int n = board[0].size();
        bool crushed = false;
        
        // Iterate through the board to find adjacent candies of the same type and mark them for crushing
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] != 0) {
                    // Check for horizontal crush
                    if (j < n - 2 && board[i][j] == board[i][j + 1] && board[i][j] == board[i][j + 2]) {
                        board[i][j] = board[i][j + 1] = board[i][j + 2] = 0;
                        crushed = true;
                    }
                    
                    // Check for vertical crush
                    if (i < m - 2 && board[i][j] == board[i + 1][j] && board[i][j] == board[i + 2][j]) {
                        board[i][j] = board[i + 1][j] = board[i + 2][j] = 0;
                        crushed = true;
                    }
                }
            }
        }
        
        // Drop the remaining candies to fill the gaps
        for (int j = 0; j < n; j++) {
            int bottom = m - 1;
            for (int i = m - 1; i >= 0; i--) {
                if (board[i][j] != 0) {
                    board[bottom--][j] = board[i][j];
                }
            }
            for (int i = bottom; i >= 0; i--) {
                board[i][j] = 0;
            }
        }
        
        // If no candies were crushed, return the original board
        if (!crushed) {
            return board;
        }
        
        // Recursively call the function to crush and drop candies until no more candies can be crushed
        return candyCrush(board);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns in the board. The time complexity is linear with respect to the size of the board because we iterate through the board a constant number of times.
> - **Space Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns in the board. The space complexity is linear with respect to the size of the board because we create a copy of the board to mark candies for crushing.
> - **Optimality proof:** The time complexity of the optimal solution is $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns in the board. This is because we iterate through the board a constant number of times to find adjacent candies of the same type and mark them for crushing, and then we iterate through the board to drop the remaining candies to fill the gaps.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, recursion, and dynamic programming.
- Problem-solving patterns identified: Finding adjacent candies of the same type and marking them for crushing, and then dropping the remaining candies to fill the gaps.
- Optimization techniques learned: Using a more efficient data structure and algorithm to reduce the time complexity.
- Similar problems to practice: Candy Crush II, Candy Crush III.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty board or a board with no candies to crush.
- Edge cases to watch for: An empty board, a board with no candies to crush, and a board with only one type of candy.
- Performance pitfalls: Using a recursive function with a large number of recursive calls, which can lead to a stack overflow.
- Testing considerations: Testing the function with different input cases, such as an empty board, a board with no candies to crush, and a board with only one type of candy.