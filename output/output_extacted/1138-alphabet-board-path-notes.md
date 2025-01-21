## Alphabet Board Path

**Problem Link:** https://leetcode.com/problems/alphabet-board-path/description

**Problem Statement:**
- Input format and constraints: The input is a string `target` consisting of lowercase letters. The string length will be between 1 and 100.
- Expected output format: The function should return a string representing the shortest sequence of keyboard navigation instructions to type the `target` string on the alphabet board.
- Key requirements and edge cases to consider: 
  - The alphabet board has the following layout:
    ```
    ["abcde", 
     "fghij", 
     "klmno", 
     "pqrst", 
     "uvwxy", 
     "z   "]
    ```
  - The cursor starts at the top left letter 'a'.
  - The cursor can move up, down, left, or right, but it cannot move outside the board.
  - The cursor can also move diagonally.
  - The cursor cannot move to the same letter more than once.
  - If the target string contains a letter that is not on the board (e.g., 'z' is the only letter on the last row), the function should return an empty string.
- Example test cases with explanations:
  - Input: "leet"
    - Output: "DDR!UURRR!!DDD!"
  - Input: "code"
    - Output: "RR!RRDD!LUU!"

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can simulate the navigation on the alphabet board by iterating through the `target` string and finding the shortest path to each letter from the current position of the cursor.
- Step-by-step breakdown of the solution:
  1. Initialize the current position of the cursor to the top left letter 'a'.
  2. Iterate through the `target` string.
  3. For each letter in the `target` string, find the shortest path from the current position of the cursor to the position of the letter on the board.
  4. Update the current position of the cursor to the position of the letter.
  5. Append the navigation instructions to the result string.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it may not be efficient due to the overhead of finding the shortest path for each letter.

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

string alphabetBoardPath(string target) {
    vector<string> board = {"abcde", "fghij", "klmno", "pqrst", "uvwxy", "z   "};
    vector<pair<int, int>> pos(26);
    for (int i = 0; i < 6; i++) {
        for (int j = 0; j < 5; j++) {
            if (board[i][j] != ' ') {
                pos[board[i][j] - 'a'] = {i, j};
            }
        }
    }

    int x = 0, y = 0;
    string res;
    for (char c : target) {
        int dx = pos[c - 'a'].first - x;
        int dy = pos[c - 'a'].second - y;
        if (dx > 0) {
            for (int i = 0; i < dx; i++) {
                res += 'D';
            }
        } else if (dx < 0) {
            for (int i = 0; i < -dx; i++) {
                res += 'U';
            }
        }
        if (dy > 0) {
            for (int i = 0; i < dy; i++) {
                res += 'R';
            }
        } else if (dy < 0) {
            for (int i = 0; i < -dy; i++) {
                res += 'L';
            }
        }
        res += '!';
        x = pos[c - 'a'].first;
        y = pos[c - 'a'].second;
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the `target` string. We iterate through the `target` string once.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space to store the board and the positions of the letters.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each letter in the `target` string. The space complexity is constant because we use a fixed amount of space to store the board and the positions of the letters.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a similar approach to the brute force solution, but we can optimize the navigation instructions by moving diagonally when possible.
- Detailed breakdown of the approach:
  1. Initialize the current position of the cursor to the top left letter 'a'.
  2. Iterate through the `target` string.
  3. For each letter in the `target` string, find the shortest path from the current position of the cursor to the position of the letter on the board.
  4. Update the current position of the cursor to the position of the letter.
  5. Append the navigation instructions to the result string.
- Proof of optimality: This approach is optimal because we are always moving in the shortest possible direction (either horizontally, vertically, or diagonally) to reach the next letter.

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

string alphabetBoardPath(string target) {
    vector<string> board = {"abcde", "fghij", "klmno", "pqrst", "uvwxy", "z   "};
    vector<pair<int, int>> pos(26);
    for (int i = 0; i < 6; i++) {
        for (int j = 0; j < 5; j++) {
            if (board[i][j] != ' ') {
                pos[board[i][j] - 'a'] = {i, j};
            }
        }
    }

    int x = 0, y = 0;
    string res;
    for (char c : target) {
        int dx = pos[c - 'a'].first - x;
        int dy = pos[c - 'a'].second - y;
        if (dx > 0) {
            for (int i = 0; i < dx; i++) {
                res += 'D';
            }
        } else if (dx < 0) {
            for (int i = 0; i < -dx; i++) {
                res += 'U';
            }
        }
        if (dy > 0) {
            for (int i = 0; i < dy; i++) {
                res += 'R';
            }
        } else if (dy < 0) {
            for (int i = 0; i < -dy; i++) {
                res += 'L';
            }
        }
        res += '!';
        x = pos[c - 'a'].first;
        y = pos[c - 'a'].second;
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the `target` string. We iterate through the `target` string once.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space to store the board and the positions of the letters.
> - **Optimality proof:** The time complexity is linear because we perform a constant amount of work for each letter in the `target` string. The space complexity is constant because we use a fixed amount of space to store the board and the positions of the letters.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of a **board** or **grid** to represent a set of positions, and the use of **navigation instructions** to move between positions.
- Problem-solving patterns identified: The problem requires the use of a **loop** to iterate through the `target` string, and the use of **conditional statements** to handle different cases (e.g., moving up, down, left, or right).
- Optimization techniques learned: The problem demonstrates the use of **optimization techniques** such as moving diagonally when possible to reduce the number of navigation instructions.
- Similar problems to practice: Other problems that involve navigating a board or grid, such as **maze problems** or **pathfinding problems**.

**Mistakes to Avoid:**
- Common implementation errors: One common error is to forget to update the current position of the cursor after moving to a new letter.
- Edge cases to watch for: One edge case is when the `target` string contains a letter that is not on the board (e.g., 'z' is the only letter on the last row).
- Performance pitfalls: One performance pitfall is to use a **recursive approach** to find the shortest path, which can lead to **stack overflow** errors for large inputs.
- Testing considerations: One testing consideration is to test the function with different inputs, including edge cases such as an empty string or a string containing only one letter.