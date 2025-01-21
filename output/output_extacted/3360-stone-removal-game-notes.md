## Stone Game
**Problem Link:** https://leetcode.com/problems/stone-removal-game/description

**Problem Statement:**
- Input format: An array of integers `piles` representing the number of stones in each pile.
- Constraints: `1 <= piles.length <= 1000`, `1 <= piles[i] <= 1000`.
- Expected output format: The maximum number of stones that can be removed.
- Key requirements and edge cases to consider: The game is played by two players who take turns removing stones from the piles. A player can remove any number of stones from a single pile. The game ends when all stones have been removed. The goal is to find the maximum number of stones that can be removed.

**Example Test Cases:**
- Input: `[2, 3, 1, 4]`
- Output: `6`
- Explanation: Player 1 removes all stones from the first and third piles, and then player 2 removes all stones from the second and fourth piles.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of removing stones from the piles.
- Step-by-step breakdown of the solution:
  1. Initialize a variable to store the maximum number of stones that can be removed.
  2. Generate all possible combinations of removing stones from the piles.
  3. For each combination, calculate the number of stones that can be removed.
  4. Update the maximum number of stones that can be removed if the current combination results in a higher number.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible combinations, but it is not efficient for large inputs.

```cpp
#include <vector>
#include <algorithm>

int stoneGame(int piles[], int n) {
    int maxStones = 0;
    // Generate all possible combinations of removing stones from the piles
    for (int mask = 0; mask < (1 << n); mask++) {
        int stones = 0;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                stones += piles[i];
            }
        }
        maxStones = std::max(maxStones, stones);
    }
    return maxStones;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of piles. This is because we generate all possible combinations of removing stones from the piles, which takes $O(2^n)$ time, and then calculate the number of stones that can be removed for each combination, which takes $O(n)$ time.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum number of stones that can be removed.
> - **Why these complexities occur:** The time complexity occurs because we try all possible combinations of removing stones from the piles, and the space complexity occurs because we only use a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The game can be solved using dynamic programming. We can build a table where each cell represents the maximum number of stones that can be removed for a given range of piles.
- Detailed breakdown of the approach:
  1. Initialize a table to store the maximum number of stones that can be removed for each range of piles.
  2. Fill the table in a bottom-up manner, starting from the smallest range of piles.
  3. For each range of piles, calculate the maximum number of stones that can be removed by considering all possible ways to split the range into two sub-ranges.
- Proof of optimality: The dynamic programming approach ensures that we consider all possible ways to remove stones from the piles, and the table is filled in a way that ensures we always choose the optimal solution.

```cpp
#include <vector>
#include <algorithm>

int stoneGame(int piles[], int n) {
    std::vector<std::vector<int>> dp(n, std::vector<int>(n, 0));
    for (int i = 0; i < n; i++) {
        dp[i][i] = piles[i];
    }
    for (int length = 2; length <= n; length++) {
        for (int i = 0; i <= n - length; i++) {
            int j = i + length - 1;
            dp[i][j] = std::max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1]);
        }
    }
    return dp[0][n - 1];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of piles. This is because we fill the table in a bottom-up manner, and each cell requires $O(1)$ time to calculate.
> - **Space Complexity:** $O(n^2)$, as we need to store the table of maximum number of stones that can be removed for each range of piles.
> - **Optimality proof:** The dynamic programming approach ensures that we consider all possible ways to remove stones from the piles, and the table is filled in a way that ensures we always choose the optimal solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, bottom-up approach.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems, solving each sub-problem only once, and storing the solutions to sub-problems to avoid redundant computation.
- Optimization techniques learned: Using dynamic programming to solve problems that have overlapping sub-problems.
- Similar problems to practice: Other dynamic programming problems, such as the Fibonacci sequence, the longest common subsequence problem, and the knapsack problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the table correctly, not filling the table in a bottom-up manner, not considering all possible ways to split the range into two sub-ranges.
- Edge cases to watch for: The case where the input array is empty, the case where the input array has only one element.
- Performance pitfalls: Not using dynamic programming to solve problems that have overlapping sub-problems, not storing the solutions to sub-problems to avoid redundant computation.
- Testing considerations: Testing the function with different input arrays, testing the function with edge cases, testing the function with large input arrays to ensure it has good performance.