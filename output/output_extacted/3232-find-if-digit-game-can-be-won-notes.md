## Find if Digit Game Can Be Won
**Problem Link:** https://leetcode.com/problems/find-if-digit-game-can-be-won/description

**Problem Statement:**
- Given an integer `n`, determine if the digit game can be won.
- The game starts with the number `n`, and at each step, the player can choose a digit from `n` and remove it, resulting in a new number.
- The goal is to determine if there exists a winning strategy for the first player.
- Input format: `n`, an integer.
- Constraints: `1 <= n <= 10^9`.
- Expected output format: `true` if the digit game can be won, `false` otherwise.
- Key requirements and edge cases to consider:
  - The number `n` can be very large, so the solution should be efficient.
  - The game is won if the first player can force a win, regardless of the moves made by the second player.
- Example test cases with explanations:
  - `n = 1`, the first player can win by removing the only digit.
  - `n = 2`, the first player can win by removing the only digit.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible moves and use recursion to explore the game tree.
- Step-by-step breakdown of the solution:
  1. Start with the number `n` and try removing each digit.
  2. Recursively call the function with the new number after removing each digit.
  3. If the second player has no moves left, the first player wins.
- Why this approach comes to mind first: It's a straightforward way to explore all possible moves and outcomes.

```cpp
#include <iostream>
#include <string>

bool canWin(int n) {
    // Convert the number to a string to easily remove digits
    std::string str = std::to_string(n);
    // Base case: If the number is empty, the first player loses
    if (str.empty()) return false;
    // Try removing each digit
    for (int i = 0; i < str.size(); i++) {
        // Create a new string with the digit removed
        std::string newStr = str.substr(0, i) + str.substr(i + 1);
        // Recursively call the function with the new string
        if (!canWin(std::stoi(newStr))) return true;
    }
    // If no winning move is found, the first player loses
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(10^n)$, where $n$ is the number of digits in the input number. This is because we try removing each digit in each recursive call.
> - **Space Complexity:** $O(n)$, where $n$ is the number of digits in the input number. This is because we need to store the recursive call stack.
> - **Why these complexities occur:** The brute force approach has exponential time complexity because it tries all possible moves, resulting in a large number of recursive calls. The space complexity is linear because we only need to store the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The game can be won if and only if the number of 1's in the binary representation of `n` is odd.
- Detailed breakdown of the approach:
  1. Convert the number `n` to binary.
  2. Count the number of 1's in the binary representation.
  3. If the count is odd, the first player can win.
- Proof of optimality: This approach is optimal because it directly determines the winning condition without trying all possible moves.

```cpp
bool canWin(int n) {
    int count = 0;
    while (n > 0) {
        count += n & 1;
        n >>= 1;
    }
    return count % 2 == 1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(log n)$, where $n$ is the input number. This is because we need to iterate over the bits of the binary representation.
> - **Space Complexity:** $O(1)$, because we only need a constant amount of space to store the count.
> - **Optimality proof:** This approach is optimal because it directly determines the winning condition without trying all possible moves, resulting in a significant reduction in time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bit manipulation and recursive functions.
- Problem-solving patterns identified: Using binary representation to solve problems.
- Optimization techniques learned: Reducing time complexity by directly determining the winning condition.
- Similar problems to practice: Other problems that involve bit manipulation and recursive functions.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, such as an empty input string.
- Edge cases to watch for: An input number with a large number of digits.
- Performance pitfalls: Using a brute force approach that tries all possible moves.
- Testing considerations: Testing the function with different input values to ensure it works correctly.