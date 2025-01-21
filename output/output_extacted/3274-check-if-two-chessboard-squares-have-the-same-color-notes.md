## Check If Two Chessboard Squares Have The Same Color

**Problem Link:** https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/description

**Problem Statement:**
- Input format: Two integers `n` and `m`, representing the coordinates of the two squares on the chessboard.
- Constraints: `1 <= n <= 8` and `1 <= m <= 8`.
- Expected output format: `true` if the two squares have the same color, `false` otherwise.
- Key requirements and edge cases to consider: The chessboard has alternating black and white squares, and the input coordinates are 1-indexed.

### Brute Force Approach

**Explanation:**
- Initial thought process: To determine the color of each square, we can manually calculate the color of each square based on its coordinates.
- Step-by-step breakdown of the solution:
  1. Create a 2D array representing the chessboard, with `true` for white squares and `false` for black squares.
  2. Iterate over each square on the board, and for each square, calculate its color based on its coordinates.
  3. Compare the colors of the two input squares.
- Why this approach comes to mind first: It is a straightforward, intuitive approach that directly addresses the problem.

```cpp
bool squareIsWhite(int n, int m) {
    bool board[8][8];
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            board[i][j] = (i + j) % 2 == 0;
        }
    }
    return board[n - 1][m - 1];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, since we are only accessing a fixed-size array.
> - **Space Complexity:** $O(1)$, since we are using a fixed-size array.
> - **Why these complexities occur:** The board is always 8x8, so the time and space complexities are constant.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can directly calculate the color of a square based on its coordinates, without needing to create a 2D array.
- Detailed breakdown of the approach:
  1. Calculate the sum of the coordinates of each square.
  2. If the sum is even, the square is white; otherwise, it is black.
- Proof of optimality: This approach has the same time complexity as the brute force approach, but uses less space.

```cpp
bool squareIsWhite(int n, int m) {
    return (n + m) % 2 == 1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, since we are only performing a constant number of operations.
> - **Space Complexity:** $O(1)$, since we are not using any additional space that scales with input size.
> - **Optimality proof:** This approach is optimal because it directly calculates the result without using any unnecessary space or operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Direct calculation, modulo arithmetic.
- Problem-solving patterns identified: Simplifying complex problems by finding patterns or relationships between variables.
- Optimization techniques learned: Reducing space complexity by avoiding unnecessary data structures.
- Similar problems to practice: Other problems involving grid or matrix calculations.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to adjust for 1-indexed coordinates.
- Edge cases to watch for: None in this problem, since the input range is fixed and well-defined.
- Performance pitfalls: Using unnecessary data structures or operations.
- Testing considerations: Test the function with different input values to ensure it works correctly for all possible cases.