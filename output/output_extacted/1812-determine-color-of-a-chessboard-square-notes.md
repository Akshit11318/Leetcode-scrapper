## Determine Color of a Chessboard Square
**Problem Link:** https://leetcode.com/problems/determine-color-of-a-chessboard-square/description

**Problem Statement:**
- Input format: The input is a string `coordinates` representing a square on a chessboard.
- Constraints: The input string is in the format of a standard algebraic notation for a chess square, i.e., it consists of a letter from 'a' to 'h' followed by a number from '1' to '8'.
- Expected output format: The function should return a string indicating the color of the square, either "white" or "black".
- Key requirements and edge cases to consider: The input is guaranteed to be valid, and the function should handle all possible chessboard squares.

**Example Test Cases:**
- Input: "a1" - Output: "black"
- Input: "h3" - Output: "white"
- Input: "c5" - Output: "black"

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves creating a mapping of all possible chessboard squares to their respective colors.
- Step-by-step breakdown:
  1. Create a 2D array or a map to represent the chessboard.
  2. Iterate through each square and assign its color based on the standard chessboard pattern (alternating colors for adjacent squares).
  3. Use the input coordinates to look up the color of the corresponding square in the map.
- Why this approach comes to mind first: It's straightforward and directly addresses the problem by considering each square individually.

```cpp
string squareColor(string coordinates) {
    // Create a map to store the color of each square
    unordered_map<string, string> squareColors;
    
    // Iterate over all possible squares
    for (char col = 'a'; col <= 'h'; ++col) {
        for (int row = 1; row <= 8; ++row) {
            // Generate the square's coordinates
            string coord = string(1, col) + to_string(row);
            
            // Determine the square's color based on its position
            if ((col - 'a' + row) % 2 == 0) {
                squareColors[coord] = "white";
            } else {
                squareColors[coord] = "black";
            }
        }
    }
    
    // Look up the color of the given square
    return squareColors[coordinates];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for lookup after initialization, but $O(64)$ for the initial setup, where $64$ is the total number of squares on a chessboard.
> - **Space Complexity:** $O(64)$ to store the colors of all squares.
> - **Why these complexities occur:** The brute force approach involves creating a map for all squares, which requires constant time for lookup but linear space and time for initialization.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The color of a square can be determined directly from its coordinates without needing to create a map of all squares.
- Detailed breakdown:
  1. Convert the column letter to a number (a=0, b=1, ..., h=7).
  2. Calculate the sum of the column number and the row number.
  3. If the sum is even, the square is white; otherwise, it's black.
- Proof of optimality: This approach directly computes the color based on the input without any unnecessary data structures or iterations.

```cpp
string squareColor(string coordinates) {
    // Convert the column letter to a number
    int colNum = coordinates[0] - 'a';
    
    // Extract the row number
    int rowNum = coordinates[1] - '0';
    
    // Determine the square's color based on its position
    if ((colNum + rowNum) % 2 == 0) {
        return "white";
    } else {
        return "black";
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, as the computation is constant time.
> - **Space Complexity:** $O(1)$, as no additional space is used that scales with input size.
> - **Optimality proof:** This approach is optimal because it directly calculates the result without any unnecessary operations or data structures, achieving the best possible time and space complexity.

---

### Final Notes

**Learning Points:**
- The importance of directly calculating results when possible.
- How to convert between different representations (e.g., letters to numbers).
- The value of analyzing the problem structure to find an optimal solution.

**Mistakes to Avoid:**
- Overcomplicating the solution with unnecessary data structures.
- Not considering the direct calculation of results.
- Failing to analyze the problem's structure for optimization opportunities.

---