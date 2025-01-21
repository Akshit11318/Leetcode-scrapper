## Transform to Chessboard
**Problem Link:** https://leetcode.com/problems/transform-to-chessboard/description

**Problem Statement:**
- Input: An `n x n` board, represented as a vector of vectors, where each cell can be either 0 or 1.
- Constraints: `1 <= n <= 8`
- Expected Output: The minimum number of moves required to transform the board into a chessboard pattern, where each row and column has an equal number of 0s and 1s.
- Key Requirements: 
  - A move consists of flipping a row or a column.
  - The goal is to minimize the number of moves.
- Example Test Cases:
  - Input: `[[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]`
    - Output: `2`
  - Input: `[[0,1,1,0],[0,1,0,1],[1,0,1,0],[1,0,1,0]]`
    - Output: `4`
  - Input: `[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]`
    - Output: `2`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible combinations of row and column flips to see which results in a chessboard pattern with the minimum number of moves.
- This approach involves generating all permutations of flips for rows and columns and then checking each permutation to see if it results in a valid chessboard pattern.

```cpp
#include <vector>
#include <algorithm>

int movesToChessboard(vector<vector<int>>& board) {
    int n = board.size();
    int minMoves = INT_MAX;

    // Generate all permutations of rows
    for (int mask = 0; mask < (1 << n); ++mask) {
        vector<vector<int>> tempBoard = board;

        // Apply row flips based on the current permutation
        for (int i = 0; i < n; ++i) {
            if ((mask & (1 << i))) {
                for (int j = 0; j < n; ++j) {
                    tempBoard[i][j] = 1 - tempBoard[i][j];
                }
            }
        }

        // Generate all permutations of columns
        for (int colMask = 0; colMask < (1 << n); ++colMask) {
            vector<vector<int>> finalBoard = tempBoard;

            // Apply column flips based on the current permutation
            for (int j = 0; j < n; ++j) {
                if ((colMask & (1 << j))) {
                    for (int i = 0; i < n; ++i) {
                        finalBoard[i][j] = 1 - finalBoard[i][j];
                    }
                }
            }

            // Check if the resulting board is a chessboard pattern
            if (isChessboard(finalBoard)) {
                // Calculate the number of moves required for this permutation
                int moves = __builtin_popcount(mask) + __builtin_popcount(colMask);
                minMoves = min(minMoves, moves);
            }
        }
    }

    return minMoves;
}

bool isChessboard(vector<vector<int>>& board) {
    int n = board.size();
    for (int i = 0; i < n; ++i) {
        int count = 0;
        for (int j = 0; j < n; ++j) {
            if (board[i][j] == 1) count++;
        }
        if (count != n / 2) return false;
    }

    for (int j = 0; j < n; ++j) {
        int count = 0;
        for (int i = 0; i < n; ++i) {
            if (board[i][j] == 1) count++;
        }
        if (count != n / 2) return false;
    }

    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{2n} \cdot n^2)$, where $n$ is the size of the board. This is because we generate all permutations of row and column flips, and for each permutation, we check if the resulting board is a chessboard pattern.
> - **Space Complexity:** $O(n^2)$, for storing the temporary boards.
> - **Why these complexities occur:** The brute force approach is inherently expensive due to the exponential number of permutations it needs to consider.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to observe that for a board to be transformable into a chessboard pattern, each row and column must have an equal number of 0s and 1s. This significantly reduces the search space.
- We can calculate the minimum number of moves required to achieve this balance for rows and columns separately.
- For rows, we can calculate the minimum number of row flips needed to make all rows have the same number of 1s.
- Similarly, for columns, we can calculate the minimum number of column flips needed.

```cpp
int movesToChessboard(vector<vector<int>>& board) {
    int n = board.size();
    int rowMask = 0, colMask = 0;
    int rowMoves = 0, colMoves = 0;

    // Calculate the target number of 1s per row and column
    int targetOnes = n / 2;

    // Calculate row moves
    for (int i = 0; i < n; ++i) {
        int ones = 0;
        for (int j = 0; j < n; ++j) {
            if (board[i][j] == 1) ones++;
        }
        if (ones > targetOnes) return -1; // Cannot achieve target
        rowMask |= (ones << i);
        rowMoves += abs(targetOnes - ones);
    }

    // Calculate column moves
    for (int j = 0; j < n; ++j) {
        int ones = 0;
        for (int i = 0; i < n; ++i) {
            if (board[i][j] == 1) ones++;
        }
        if (ones > targetOnes) return -1; // Cannot achieve target
        colMask |= (ones << j);
        colMoves += abs(targetOnes - ones);
    }

    // Calculate the minimum number of moves required
    int minMoves = rowMoves / 2 + colMoves / 2;

    return minMoves;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the board. This is because we iterate through the board once to calculate the minimum number of moves.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the row and column masks and moves.
> - **Optimality proof:** This approach is optimal because it directly calculates the minimum number of moves required to achieve the target number of 1s per row and column, which is the necessary condition for a chessboard pattern.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: 
  - **Pattern recognition**: Identifying the necessary conditions for a chessboard pattern.
  - **Bit manipulation**: Using bit masks to represent row and column flips.
- Problem-solving patterns identified: 
  - **Divide and Conquer**: Breaking down the problem into smaller sub-problems (rows and columns).
- Optimization techniques learned: 
  - **Pruning**: Eliminating impossible cases early on.
- Similar problems to practice: 
  - **Sliding Window**: Problems that involve finding a subset of a larger set that satisfies certain conditions.

**Mistakes to Avoid:**
- Common implementation errors: 
  - **Off-by-one errors**: Incorrectly calculating the target number of 1s per row and column.
- Edge cases to watch for: 
  - **Empty board**: Handling the case where the board is empty.
- Performance pitfalls: 
  - **Exponential time complexity**: Avoiding brute force approaches that have exponential time complexity.
- Testing considerations: 
  - **Corner cases**: Testing the solution with corner cases, such as a board with all 0s or all 1s.