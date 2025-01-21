## Find the Winning Player in Coin Game
**Problem Link:** https://leetcode.com/problems/find-the-winning-player-in-coin-game/description

**Problem Statement:**
- Input format and constraints: Given a string `s` of length `n`, where `s[i]` is either `'H'` or `'T'`.
- Expected output format: Return the winner of the game, either `"Alice"` or `"Bob"`.
- Key requirements and edge cases to consider: The game starts with `Alice`, and players take turns flipping coins. The game ends when a player flips two heads in a row.
- Example test cases with explanations:
  - If `s = "HT"` then Alice wins because she flipped a head on her first turn.
  - If `s = "TH"` then Bob wins because he flipped a head on his first turn.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Simulate the game step by step, keeping track of whose turn it is and the last coin flipped.
- Step-by-step breakdown of the solution:
  1. Initialize variables to keep track of the current player and the last coin flipped.
  2. Iterate through the string `s`.
  3. For each character in `s`, check if it's a head or a tail.
  4. If it's a head and the last coin flipped was also a head, return the current player as the winner.
  5. Update the current player and the last coin flipped.
- Why this approach comes to mind first: It directly simulates the game as described in the problem statement.

```cpp
string findTheWinner(string s) {
    int n = s.size();
    string currentPlayer = "Alice";
    char lastCoin = ' ';
    for (int i = 0; i < n; i++) {
        if (s[i] == 'H' && lastCoin == 'H') {
            return currentPlayer;
        }
        lastCoin = s[i];
        currentPlayer = (currentPlayer == "Alice") ? "Bob" : "Alice";
    }
    return "";
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`, because we iterate through `s` once.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store the current player and the last coin flipped.
> - **Why these complexities occur:** The iteration through `s` causes the linear time complexity, and the use of a fixed number of variables causes the constant space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The game ends as soon as a player flips two heads in a row. Thus, we can still simulate the game but focus on identifying sequences of two heads.
- Detailed breakdown of the approach:
  1. Initialize variables to keep track of the current player.
  2. Iterate through the string `s`, checking for sequences of two heads.
  3. If a sequence of two heads is found, return the current player as the winner.
  4. Update the current player after each move.
- Proof of optimality: This approach is optimal because it still checks each character in `s` exactly once, which is necessary to find the winner.

```cpp
string findTheWinner(string s) {
    int n = s.size();
    string currentPlayer = "Alice";
    for (int i = 0; i < n - 1; i++) {
        if (s[i] == 'H' && s[i + 1] == 'H') {
            return currentPlayer;
        }
        currentPlayer = (currentPlayer == "Alice") ? "Bob" : "Alice";
    }
    return "";
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`, because we iterate through `s` once.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store the current player.
> - **Optimality proof:** The time complexity is optimal because we must at least read the input string once to determine the winner. The space complexity is also optimal because we only need a constant amount of space to keep track of the current player.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Simulation, iteration, and conditional checking.
- Problem-solving patterns identified: Breaking down the problem into manageable steps and focusing on key events (in this case, flipping two heads in a row).
- Optimization techniques learned: Reducing unnecessary operations by focusing on critical sequences (two heads in a row).
- Similar problems to practice: Other simulation-based problems, such as games or processes that can be modeled step by step.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the current player correctly, or not checking for the end condition (two heads in a row) properly.
- Edge cases to watch for: An empty string or a string with only one character.
- Performance pitfalls: Using more complex data structures or algorithms than necessary, leading to increased time or space complexity.
- Testing considerations: Ensure that the function works correctly for different lengths of strings, including edge cases, and that it correctly identifies the winner based on the sequence of heads and tails.