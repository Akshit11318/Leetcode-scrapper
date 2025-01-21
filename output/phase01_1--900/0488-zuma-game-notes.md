## Zuma Game
**Problem Link:** https://leetcode.com/problems/zuma-game/description

**Problem Statement:**
- Input format and constraints: The game is represented as a string `board` containing lowercase letters, each representing a different colored ball. The goal is to find the minimum number of moves to clear the board.
- Expected output format: The minimum number of moves required to clear the board. If it's impossible to clear the board, return -1.
- Key requirements and edge cases to consider: The game can be cleared by removing sequences of three or more balls of the same color. The removal of balls can create new sequences of the same color, allowing for further removals.
- Example test cases with explanations:
  - Input: `board = "aaabbb"`, Output: `2`
  - Input: `board = "abababa"`, Output: `0`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible moves and use a recursive approach to explore all possible game states.
- Step-by-step breakdown of the solution:
  1. Generate all possible moves from the current game state.
  2. For each move, apply the move to the game state and remove any sequences of three or more balls of the same color.
  3. Recursively explore all possible moves from the new game state.
  4. Keep track of the minimum number of moves required to clear the board.
- Why this approach comes to mind first: It's a straightforward way to explore all possible game states and find the minimum number of moves required to clear the board.

```cpp
class Solution {
public:
    int findMinStep(string board) {
        unordered_map<string, int> memo;
        return dfs(board, memo);
    }

    int dfs(string board, unordered_map<string, int>& memo) {
        if (memo.count(board)) return memo[board];
        if (board.empty()) return 0;

        int res = INT_MAX;
        for (int i = 0; i < board.size() - 1; i++) {
            if (board[i] == board[i + 1]) {
                string newBoard = removeBalls(board, i, i + 1);
                res = min(res, 1 + dfs(newBoard, memo));
            }
        }
        memo[board] = res;
        return res;
    }

    string removeBalls(string board, int start, int end) {
        int count = 0;
        for (int i = start; i <= end; i++) {
            if (board[i] == board[start]) count++;
        }
        if (count < 3) return board;
        string newBoard = "";
        for (int i = 0; i < board.size(); i++) {
            if (i < start || i > end || board[i] != board[start]) {
                newBoard += board[i];
            }
        }
        return newBoard;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where n is the length of the board. This is because in the worst case, we might need to explore all possible moves.
> - **Space Complexity:** $O(n)$, where n is the length of the board. This is because we need to store the recursive call stack and the memoization table.
> - **Why these complexities occur:** The recursive approach and the use of memoization lead to these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a greedy approach and always try to remove the longest sequence of balls of the same color.
- Detailed breakdown of the approach:
  1. Initialize an empty stack to store the balls.
  2. Iterate through the board and push each ball onto the stack.
  3. If the top two balls on the stack are the same color, pop them from the stack and increment the move count.
  4. If the top three balls on the stack are the same color, pop them from the stack and increment the move count.
  5. Repeat steps 2-4 until the stack is empty or no more moves can be made.
- Proof of optimality: This approach is optimal because it always tries to remove the longest sequence of balls of the same color, which minimizes the number of moves required to clear the board.

```cpp
class Solution {
public:
    int findMinStep(string board) {
        int res = 0;
        while (true) {
            int pos = -1;
            int maxLen = 0;
            for (int i = 0; i < board.size() - 2; i++) {
                if (board[i] == board[i + 1] && board[i] == board[i + 2]) {
                    if (i + 2 < board.size() && board[i] == board[i + 2]) {
                        int j = i + 2;
                        while (j < board.size() && board[i] == board[j]) j++;
                        if (j - i > maxLen) {
                            maxLen = j - i;
                            pos = i;
                        }
                    }
                }
            }
            if (pos == -1) break;
            res++;
            board = board.substr(0, pos) + board.substr(pos + maxLen);
        }
        return board.empty() ? res : -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where n is the length of the board. This is because in the worst case, we might need to iterate through the board multiple times.
> - **Space Complexity:** $O(n)$, where n is the length of the board. This is because we need to store the board and the stack.
> - **Optimality proof:** This approach is optimal because it always tries to remove the longest sequence of balls of the same color, which minimizes the number of moves required to clear the board.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy approach, memoization, recursive approach.
- Problem-solving patterns identified: Always try to remove the longest sequence of balls of the same color.
- Optimization techniques learned: Use a greedy approach and memoization to minimize the number of moves required to clear the board.
- Similar problems to practice: Other problems that involve removing sequences of elements, such as removing duplicates from a string or array.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty board or a board with only one ball.
- Edge cases to watch for: A board with only one ball, a board with only two balls of the same color.
- Performance pitfalls: Using a recursive approach without memoization, which can lead to exponential time complexity.
- Testing considerations: Test the solution with different inputs, including edge cases and large inputs.