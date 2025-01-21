## Check if Word Can Be Placed in Crossword
**Problem Link:** https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/description

**Problem Statement:**
- Input format and constraints: The input consists of a 2D grid representing the crossword puzzle and a word that needs to be placed in the crossword. The grid cells can either be empty (`' '`) or contain a block (`'#'`).
- Expected output format: The function should return `true` if the word can be placed in the crossword, either horizontally or vertically, and `false` otherwise.
- Key requirements and edge cases to consider: The word can only be placed in an empty row or column that is long enough to accommodate the word. No part of the word can overlap with a block (`'#'`) in the grid.
- Example test cases with explanations:
  - For a crossword grid `[['#', '#'], ['#', '#']]` and a word `"abc"`, the function should return `false` because there is no empty row or column to place the word.
  - For a crossword grid `[[" ", " ", " "], [" ", " ", " "], ["#", "#", "#"]]` and a word `"abc"`, the function should return `true` because the word can be placed horizontally in the first or second row, or vertically in the first, second, or third column.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To determine if a word can be placed in a crossword, we need to check every possible position in the grid where the word could potentially fit, either horizontally or vertically.
- Step-by-step breakdown of the solution:
  1. Iterate through each cell in the grid.
  2. For each cell, check if the word can be placed horizontally starting from that cell by checking if the next cells to the right are empty.
  3. If the word can be placed horizontally, check if it can be placed without overlapping any blocks.
  4. Repeat the process for vertical placement by checking cells below the current cell.
- Why this approach comes to mind first: It is straightforward to think about checking every possible placement of the word in the grid.

```cpp
#include <vector>
#include <string>

bool placeWordInCrossword(std::vector<std::vector<char>>& board, std::string word) {
    int m = board.size();
    int n = board[0].size();
    
    // Check horizontal placement
    for (int i = 0; i < m; i++) {
        for (int j = 0; j <= n - word.size(); j++) {
            bool canPlace = true;
            for (int k = 0; k < word.size(); k++) {
                if (board[i][j + k] == '#') {
                    canPlace = false;
                    break;
                }
            }
            if (canPlace) {
                if (j == 0 || board[i][j - 1] == '#') {
                    if (j + word.size() == n || board[i][j + word.size()] == '#') {
                        return true;
                    }
                }
            }
        }
    }
    
    // Check vertical placement
    for (int i = 0; i <= m - word.size(); i++) {
        for (int j = 0; j < n; j++) {
            bool canPlace = true;
            for (int k = 0; k < word.size(); k++) {
                if (board[i + k][j] == '#') {
                    canPlace = false;
                    break;
                }
            }
            if (canPlace) {
                if (i == 0 || board[i - 1][j] == '#') {
                    if (i + word.size() == m || board[i + word.size()][j] == '#') {
                        return true;
                    }
                }
            }
        }
    }
    
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot |word|)$, where $m$ and $n$ are the dimensions of the grid and $|word|$ is the length of the word. This is because for each cell in the grid, we potentially check a path of length $|word|$.
> - **Space Complexity:** $O(1)$, since we are not using any additional space that scales with the input size.
> - **Why these complexities occur:** The brute force approach involves checking every possible placement of the word in the grid, which leads to the time complexity. The space complexity is constant because we are only using a fixed amount of space to store variables.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves checking only the rows and columns that are long enough to accommodate the word, and ensuring that these rows or columns do not contain any blocks (`'#'`) where the word would be placed.
- Detailed breakdown of the approach:
  1. Iterate through each row and check if it is long enough to accommodate the word and if it contains any blocks where the word would be placed.
  2. If a suitable row is found, check if the word can be placed at the beginning of the row or after a block, and if the row ends with a block or is the last row.
  3. Repeat the process for columns.
- Proof of optimality: This solution is optimal because it only checks rows and columns that are potential candidates for placing the word, reducing unnecessary checks.

```cpp
#include <vector>
#include <string>

bool placeWordInCrossword(std::vector<std::vector<char>>& board, std::string word) {
    int m = board.size();
    int n = board[0].size();
    
    // Check horizontal placement
    for (int i = 0; i < m; i++) {
        int consecutiveEmpty = 0;
        for (int j = 0; j < n; j++) {
            if (board[i][j] == ' ') {
                consecutiveEmpty++;
                if (consecutiveEmpty == word.size()) {
                    if (j == n - 1 || board[i][j + 1] == '#') {
                        if (j - word.size() + 1 == 0 || board[i][j - word.size()] == '#') {
                            return true;
                        }
                    }
                }
            } else {
                consecutiveEmpty = 0;
            }
        }
    }
    
    // Check vertical placement
    for (int j = 0; j < n; j++) {
        int consecutiveEmpty = 0;
        for (int i = 0; i < m; i++) {
            if (board[i][j] == ' ') {
                consecutiveEmpty++;
                if (consecutiveEmpty == word.size()) {
                    if (i == m - 1 || board[i + 1][j] == '#') {
                        if (i - word.size() + 1 == 0 || board[i - word.size()][j] == '#') {
                            return true;
                        }
                    }
                }
            } else {
                consecutiveEmpty = 0;
            }
        }
    }
    
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the grid. This is because we are potentially scanning each cell in the grid once.
> - **Space Complexity:** $O(1)$, since we are not using any additional space that scales with the input size.
> - **Optimality proof:** This solution is optimal because it only checks rows and columns that are potential candidates for placing the word, reducing unnecessary checks.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem involves scanning a grid and checking for certain conditions, which is a fundamental concept in algorithm design.
- Problem-solving patterns identified: The solution involves breaking down the problem into smaller sub-problems (checking rows and columns) and solving them independently.
- Optimization techniques learned: The optimal solution involves reducing unnecessary checks by only considering rows and columns that are long enough to accommodate the word.
- Similar problems to practice: Other problems involving grid scanning and pattern matching, such as finding a path in a maze or detecting a certain pattern in a grid.

**Mistakes to Avoid:**
- Common implementation errors: Failing to check for edge cases, such as an empty grid or a word that is longer than the grid.
- Edge cases to watch for: The solution should handle cases where the word is placed at the beginning or end of a row or column, and where the row or column ends with a block.
- Performance pitfalls: The brute force approach can be slow for large grids, so optimizing the solution to reduce unnecessary checks is important.
- Testing considerations: The solution should be tested with different grid sizes, word lengths, and placement scenarios to ensure it works correctly in all cases.