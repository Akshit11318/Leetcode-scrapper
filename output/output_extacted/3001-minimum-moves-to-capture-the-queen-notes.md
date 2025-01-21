## Minimum Moves to Capture the Queen
**Problem Link:** https://leetcode.com/problems/minimum-moves-to-capture-the-queen/description

**Problem Statement:**
- Input: `queen` and `king` positions on a chessboard, both represented as strings in standard algebraic notation (e.g., "e4").
- Constraints: Both positions are on the same `8x8` chessboard, and the queen and king are not in the same position.
- Expected output: The minimum number of moves required for the king to capture the queen, assuming the king moves according to standard chess rules (one square in any direction: horizontally, vertically, or diagonally).
- Key requirements: Calculate the minimum moves based on the king's movement capabilities, considering the queen's position as a target to be captured.
- Example test cases:
  - Input: `queen = "e4", king = "e6"`
    - Explanation: The king can move from "e6" to "e4" in 2 moves (e.g., "e6" -> "e5" -> "e4").
  - Input: `queen = "a1", king = "h8"`
    - Explanation: The minimum moves would involve moving diagonally or in a combination of horizontal and vertical moves to reach the queen.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Enumerate all possible moves from the king's position and recursively explore each move until the queen's position is reached.
- Step-by-step breakdown:
  1. Convert the input positions to coordinates (e.g., "e4" becomes `(4, 3)` if we consider "a" as 0 and "1" as 0).
  2. Define all possible moves for the king (up, down, left, right, and four diagonals).
  3. Use a breadth-first search (BFS) or depth-first search (DFS) to explore all possible paths from the king to the queen.
- Why this approach comes to mind first: It's a straightforward method to ensure all possible moves are considered, but it's inefficient due to the large number of potential paths.

```cpp
#include <queue>
#include <string>

using namespace std;

int minMovesToCaptureQueen(string queen, string king) {
    // Convert positions to coordinates
    int queenX = queen[0] - 'a';
    int queenY = queen[1] - '1';
    int kingX = king[0] - 'a';
    int kingY = king[1] - '1';

    // Define all possible moves for the king
    int dx[] = {-1, 1, 0, 0, -1, 1, -1, 1};
    int dy[] = {0, 0, -1, 1, -1, 1, 1, -1};

    // BFS to find the shortest path
    queue<pair<int, int>> q;
    q.push({kingX, kingY});
    int moves = 0;
    bool visited[8][8] = {{false}};

    while (!q.empty()) {
        int size = q.size();
        for (int i = 0; i < size; i++) {
            auto [x, y] = q.front();
            q.pop();

            if (x == queenX && y == queenY) return moves;

            for (int j = 0; j < 8; j++) {
                int newX = x + dx[j];
                int newY = y + dy[j];

                if (newX >= 0 && newX < 8 && newY >= 0 && newY < 8 && !visited[newX][newY]) {
                    q.push({newX, newY});
                    visited[newX][newY] = true;
                }
            }
        }
        moves++;
    }

    return -1; // If there's no path
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(8^d)$ where $d$ is the distance between the king and the queen, due to exploring all possible moves in each step.
> - **Space Complexity:** $O(8^d)$ for storing visited positions and the queue.
> - **Why these complexities occur:** The brute force approach explores all possible paths without considering the optimal direction towards the queen.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The king moves in a straight line (horizontally, vertically, or diagonally) towards the queen in the minimum number of moves.
- Detailed breakdown:
  1. Calculate the absolute differences in x and y coordinates between the king and the queen.
  2. If the differences are equal, the king can move diagonally; otherwise, it moves horizontally and then vertically or vice versa.
- Proof of optimality: This approach directly calculates the minimum moves required based on the king's movement capabilities and the positions of the king and the queen.

```cpp
int minMovesToCaptureQueenOptimal(string queen, string king) {
    // Convert positions to coordinates
    int queenX = queen[0] - 'a';
    int queenY = queen[1] - '1';
    int kingX = king[0] - 'a';
    int kingY = king[1] - '1';

    // Calculate the absolute differences
    int dx = abs(queenX - kingX);
    int dy = abs(queenY - kingY);

    // If differences are equal, move diagonally; otherwise, move horizontally and vertically
    if (dx == dy) {
        return dx;
    } else {
        return dx + dy;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ since we only perform constant-time operations.
> - **Space Complexity:** $O(1)$ as we use a constant amount of space.
> - **Optimality proof:** This approach directly calculates the minimum moves by considering the king's movement capabilities and the positions of the king and the queen, making it the most efficient solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS for exploring all possible paths, and direct calculation for optimal solution.
- Problem-solving patterns identified: Using movement patterns and coordinates to solve problems involving positions on a grid.
- Optimization techniques learned: Reducing the search space by considering the optimal direction towards the target.
- Similar problems to practice: Other chess-related problems, such as finding the minimum moves for a knight or bishop to reach a target.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases (e.g., positions outside the chessboard).
- Edge cases to watch for: Positions where the king and queen are in the same row, column, or diagonal.
- Performance pitfalls: Using brute force approaches for large inputs.
- Testing considerations: Thoroughly testing the function with various inputs, including edge cases.