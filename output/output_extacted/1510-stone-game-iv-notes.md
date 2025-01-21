## Stone Game IV

**Problem Link:** https://leetcode.com/problems/stone-game-iv/description

**Problem Statement:**
- Input format and constraints: Given a positive integer `n`, return `true` if and only if `n` can be represented as the sum of two squares.
- Expected output format: A boolean value indicating whether `n` can be represented as the sum of two squares.
- Key requirements and edge cases to consider: The input `n` will be in the range `[1, 10^8]`.
- Example test cases with explanations:
  - Input: `n = 5`, Output: `true` (5 can be represented as 2^2 + 1^2)
  - Input: `n = 3`, Output: `false` (3 cannot be represented as the sum of two squares)

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of two squares to see if their sum equals `n`.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `i` to 0.
  2. Loop through all possible values of `i` from 0 to `sqrt(n)`.
  3. For each `i`, calculate `j = sqrt(n - i * i)`.
  4. If `j` is an integer, return `true`.
  5. If no such `i` is found, return `false`.
- Why this approach comes to mind first: It's a straightforward way to check all possible combinations of two squares.

```cpp
bool winnerSquareGame(int n) {
    vector<bool> dp(n + 1, false);
    dp[0] = true;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j * j <= i; j++) {
            if (!dp[i - j * j]) {
                dp[i] = true;
                break;
            }
        }
    }
    return dp[n];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^{1.5})$ because we loop through all possible values of `i` and for each `i`, we loop through all possible values of `j`.
> - **Space Complexity:** $O(n)$ because we use a boolean array of size `n + 1`.
> - **Why these complexities occur:** The brute force approach has a high time complexity because it checks all possible combinations of two squares.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to solve this problem. The idea is to build a boolean array `dp` where `dp[i]` is `true` if and only if the current player can win the game with `i` stones.
- Detailed breakdown of the approach:
  1. Initialize a boolean array `dp` of size `n + 1`.
  2. Set `dp[0] = true` because the current player can win the game with 0 stones.
  3. Loop through all possible values of `i` from 1 to `n`.
  4. For each `i`, loop through all possible values of `j` such that `j * j <= i`.
  5. If `dp[i - j * j]` is `false`, set `dp[i] = true` because the current player can win the game by taking `j * j` stones.
- Proof of optimality: This approach is optimal because it uses dynamic programming to avoid redundant calculations.

```cpp
bool winnerSquareGame(int n) {
    vector<bool> dp(n + 1, false);
    dp[0] = true;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j * j <= i; j++) {
            if (!dp[i - j * j]) {
                dp[i] = true;
                break;
            }
        }
    }
    return dp[n];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^{1.5})$ because we loop through all possible values of `i` and for each `i`, we loop through all possible values of `j`.
> - **Space Complexity:** $O(n)$ because we use a boolean array of size `n + 1`.
> - **Optimality proof:** This approach is optimal because it uses dynamic programming to avoid redundant calculations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, bit manipulation.
- Problem-solving patterns identified: Using dynamic programming to avoid redundant calculations.
- Optimization techniques learned: Using bit manipulation to improve the efficiency of the solution.
- Similar problems to practice: Other dynamic programming problems, such as the Fibonacci sequence or the knapsack problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the boolean array correctly, not handling edge cases correctly.
- Edge cases to watch for: The input `n` will be in the range `[1, 10^8]`.
- Performance pitfalls: Using a brute force approach instead of dynamic programming.
- Testing considerations: Test the solution with different inputs, including edge cases and large inputs.