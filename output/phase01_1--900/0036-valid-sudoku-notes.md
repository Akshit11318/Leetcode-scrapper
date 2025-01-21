## Valid Sudoku

**Problem Link:** https://leetcode.com/problems/valid-sudoku/description

**Problem Statement:**
- Input: A 2D array `board` of size 9x9, where `board[i][j]` is either a digit from '1' to '9' or '.'.
- Expected output: A boolean indicating whether the Sudoku puzzle is valid according to Sudoku rules.
- Key requirements and edge cases to consider: 
  - Each row must contain the digits '1-9' without repetition.
  - Each column must contain the digits '1-9' without repetition.
  - Each of the nine 3x3 sub-boxes of the grid must contain the digits '1-9' without repetition.
- Example test cases with explanations:
  - A valid Sudoku puzzle with all numbers filled correctly.
  - An invalid Sudoku puzzle with repeated numbers in a row, column, or sub-box.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check each row, column, and sub-box individually for repeated numbers.
- Step-by-step breakdown of the solution:
  1. Iterate through each row and check for repeated numbers.
  2. Iterate through each column and check for repeated numbers.
  3. Iterate through each sub-box and check for repeated numbers.
- Why this approach comes to mind first: It directly addresses the requirements of the problem by checking each condition separately.

```cpp
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // Check rows
        for (int i = 0; i < 9; i++) {
            vector<bool> seen(9, false);
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') {
                    int num = board[i][j] - '1';
                    if (seen[num]) return false;
                    seen[num] = true;
                }
            }
        }
        
        // Check columns
        for (int i = 0; i < 9; i++) {
            vector<bool> seen(9, false);
            for (int j = 0; j < 9; j++) {
                if (board[j][i] != '.') {
                    int num = board[j][i] - '1';
                    if (seen[num]) return false;
                    seen[num] = true;
                }
            }
        }
        
        // Check sub-boxes
        for (int i = 0; i < 9; i += 3) {
            for (int j = 0; j < 9; j += 3) {
                vector<bool> seen(9, false);
                for (int x = 0; x < 3; x++) {
                    for (int y = 0; y < 3; y++) {
                        if (board[i+x][j+y] != '.') {
                            int num = board[i+x][j+y] - '1';
                            if (seen[num]) return false;
                            seen[num] = true;
                        }
                    }
                }
            }
        }
        
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(9 \times 9 + 9 \times 9 + 9 \times 9) = O(1)$, since we're dealing with a fixed-size Sudoku board.
> - **Space Complexity:** $O(1)$, for the `seen` vectors used in each iteration, which have a fixed size of 9.
> - **Why these complexities occur:** The time complexity is constant because we're performing a fixed number of operations, and the space complexity is constant because we're using a fixed amount of space to store the `seen` vectors.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of using separate iterations for rows, columns, and sub-boxes, we can use a single pass through the board and keep track of all three conditions simultaneously.
- Detailed breakdown of the approach:
  1. Initialize three types of sets: one for rows, one for columns, and one for sub-boxes.
  2. Iterate through the board once. For each cell, check if the number is already in the corresponding row, column, or sub-box set. If it is, return false. Otherwise, add the number to the sets.
- Proof of optimality: This approach is optimal because it only requires a single pass through the board, reducing the constant factor in the time complexity.

```cpp
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<unordered_set<char>> rows(9);
        vector<unordered_set<char>> cols(9);
        vector<unordered_set<char>> boxes(9);
        
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char val = board[i][j];
                if (val == '.') continue;
                
                // Calculate box index
                int boxIndex = (i / 3) * 3 + j / 3;
                
                if (rows[i].count(val) || cols[j].count(val) || boxes[boxIndex].count(val)) {
                    return false;
                }
                
                rows[i].insert(val);
                cols[j].insert(val);
                boxes[boxIndex].insert(val);
            }
        }
        
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because we're still dealing with a fixed-size Sudoku board.
> - **Space Complexity:** $O(1)$, for the sets used to keep track of rows, columns, and sub-boxes.
> - **Optimality proof:** This is the optimal solution because it minimizes the number of operations required to solve the problem, achieving a constant time complexity with a single pass through the board.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, set operations, and the importance of minimizing the number of passes through the data.
- Problem-solving patterns identified: Breaking down the problem into smaller, more manageable parts, and using data structures to keep track of information.
- Optimization techniques learned: Reducing the number of iterations and using efficient data structures to minimize time and space complexity.
- Similar problems to practice: Other validation problems, such as validating a binary search tree or checking if a graph is connected.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle edge cases, such as an empty board or a board with invalid characters.
- Edge cases to watch for: Boards with repeated numbers in rows, columns, or sub-boxes, and boards with invalid characters.
- Performance pitfalls: Using inefficient data structures or algorithms, such as using a linear search instead of a set to check for repeated numbers.
- Testing considerations: Testing the function with a variety of inputs, including valid and invalid Sudoku puzzles, to ensure it works correctly in all cases.