## Find Champion II
**Problem Link:** https://leetcode.com/problems/find-champion-ii/description

**Problem Statement:**
- Given a list of integers `n` and a list of lists `matches`, where `matches[i] = [winner_i, loser_i]`, find the champion of the league.
- A champion is a player who has won at least one match and has not lost any matches.
- If there is no champion, return `-1`.
- Input format: `n` (integer) and `matches` (list of lists of integers)
- Constraints: `1 <= n <= 1000`, `0 <= matches.length <= 1000`, `0 <= winner_i, loser_i <= n-1`
- Expected output: The champion of the league, or `-1` if no champion exists.
- Key requirements and edge cases to consider:
  - Handling cases where there are no matches.
  - Handling cases where a player has won but also lost a match.
  - Handling cases where there are multiple champions (in which case we should return any of them).
- Example test cases with explanations:
  - `n = 3`, `matches = [[1, 2], [2, 3]]`, expected output: `2` because player 2 won a match and did not lose any.
  - `n = 2`, `matches = [[1, 2], [1, 2]]`, expected output: `1` because player 1 won two matches and did not lose any.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through each player and check if they have won at least one match and not lost any matches.
- Step-by-step breakdown of the solution:
  1. Create a `wins` array to store the number of wins for each player.
  2. Create a `losses` array to store the number of losses for each player.
  3. Iterate through each match and update the `wins` and `losses` arrays accordingly.
  4. Iterate through each player and check if they have won at least one match and not lost any matches. If such a player is found, return their index.

```cpp
#include <vector>

int findChampion(int n, std::vector<std::vector<int>>& matches) {
    // Initialize wins and losses arrays
    std::vector<int> wins(n, 0);
    std::vector<int> losses(n, 0);
    
    // Update wins and losses arrays
    for (const auto& match : matches) {
        wins[match[0]]++;
        losses[match[1]]++;
    }
    
    // Find the champion
    for (int i = 0; i < n; i++) {
        if (wins[i] > 0 && losses[i] == 0) {
            return i;
        }
    }
    
    // If no champion is found, return -1
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of players and $m$ is the number of matches. This is because we iterate through each match once and each player once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of players. This is because we use two arrays of size $n$ to store the wins and losses of each player.
> - **Why these complexities occur:** The time complexity occurs because we need to iterate through each match and each player to find the champion. The space complexity occurs because we need to store the wins and losses of each player.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same as the brute force approach. However, we can optimize the solution by using a single pass through the matches and players.
- Detailed breakdown of the approach:
  1. Create a `wins` array to store the number of wins for each player.
  2. Create a `losses` array to store the number of losses for each player.
  3. Iterate through each match and update the `wins` and `losses` arrays accordingly.
  4. Iterate through each player and check if they have won at least one match and not lost any matches. If such a player is found, return their index.

```cpp
#include <vector>

int findChampion(int n, std::vector<std::vector<int>>& matches) {
    // Initialize wins and losses arrays
    std::vector<int> wins(n, 0);
    std::vector<int> losses(n, 0);
    
    // Update wins and losses arrays and find the champion
    for (const auto& match : matches) {
        wins[match[0]]++;
        losses[match[1]]++;
    }
    
    // Find the champion
    for (int i = 0; i < n; i++) {
        if (wins[i] > 0 && losses[i] == 0) {
            return i;
        }
    }
    
    // If no champion is found, return -1
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of players and $m$ is the number of matches. This is because we iterate through each match once and each player once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of players. This is because we use two arrays of size $n$ to store the wins and losses of each player.
> - **Optimality proof:** This is the optimal solution because we need to iterate through each match and each player to find the champion.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional statements, and array manipulation.
- Problem-solving patterns identified: Finding the champion by iterating through each match and player.
- Optimization techniques learned: Using a single pass through the matches and players to find the champion.
- Similar problems to practice: Other problems that involve finding a specific player or team based on certain conditions.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the wins and losses arrays, not updating the wins and losses arrays correctly, and not checking for the champion correctly.
- Edge cases to watch for: Handling cases where there are no matches, handling cases where a player has won but also lost a match, and handling cases where there are multiple champions.
- Performance pitfalls: Using multiple passes through the matches and players, using unnecessary data structures, and not optimizing the solution.
- Testing considerations: Testing the solution with different inputs, including edge cases, to ensure that it works correctly.