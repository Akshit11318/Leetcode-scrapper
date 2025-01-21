## Find Players With Zero or One Losses

**Problem Link:** https://leetcode.com/problems/find-players-with-zero-or-one-losses/description

**Problem Statement:**
- Input format and constraints: You are given a 2D integer array `matches` where `matches[i] = [winner_i, loser_i]` indicates that `winner_i` beat `loser_i` in a match. Return a list of integers representing the players with zero or one losses.
- Expected output format: The output should be a list of integers representing the players with zero or one losses.
- Key requirements and edge cases to consider: A player with zero losses is a player who has not lost any matches, and a player with one loss is a player who has lost exactly one match.
- Example test cases with explanations:
  - Example 1: Input: `matches = [[1,3],[2,3],[3,6],[1,2],[2,4],[5,2],[7,4]]`, Output: `[1,2,5,6]`.
  - Example 2: Input: `matches = [[2,3]]`, Output: `[1]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can create a dictionary to store the number of wins and losses for each player. Then, we can iterate through the matches and update the wins and losses for each player. Finally, we can return a list of players with zero or one losses.
- Step-by-step breakdown of the solution:
  1. Create a dictionary to store the number of wins and losses for each player.
  2. Iterate through the matches and update the wins and losses for each player.
  3. Return a list of players with zero or one losses.
- Why this approach comes to mind first: This approach is straightforward and easy to implement.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

std::vector<int> findWinners(std::vector<std::vector<int>>& matches) {
    std::unordered_map<int, std::pair<int, int>> players;
    for (const auto& match : matches) {
        int winner = match[0];
        int loser = match[1];
        
        // Update wins and losses for the winner
        if (players.find(winner) == players.end()) {
            players[winner] = {1, 0};
        } else {
            players[winner].first++;
        }
        
        // Update wins and losses for the loser
        if (players.find(loser) == players.end()) {
            players[loser] = {0, 1};
        } else {
            players[loser].second++;
        }
    }
    
    std::vector<int> result;
    for (const auto& player : players) {
        if (player.second.second <= 1) {
            result.push_back(player.first);
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of matches and $m$ is the number of players. This is because we iterate through the matches and players once.
> - **Space Complexity:** $O(m)$, where $m$ is the number of players. This is because we store the wins and losses for each player in a dictionary.
> - **Why these complexities occur:** The time complexity occurs because we iterate through the matches and players once, and the space complexity occurs because we store the wins and losses for each player in a dictionary.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a dictionary to store the number of losses for each player. Then, we can iterate through the matches and update the losses for each player. Finally, we can return a list of players with zero or one losses.
- Detailed breakdown of the approach:
  1. Create a dictionary to store the number of losses for each player.
  2. Iterate through the matches and update the losses for each player.
  3. Return a list of players with zero or one losses.
- Proof of optimality: This approach is optimal because we only iterate through the matches once and store the losses for each player in a dictionary.
- Why further optimization is impossible: Further optimization is impossible because we need to iterate through the matches at least once to update the losses for each player.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

std::vector<int> findWinners(std::vector<std::vector<int>>& matches) {
    std::unordered_map<int, int> losses;
    std::unordered_set<int> players;
    
    for (const auto& match : matches) {
        int winner = match[0];
        int loser = match[1];
        
        players.insert(winner);
        players.insert(loser);
        
        losses[loser]++;
    }
    
    std::vector<int> result;
    for (const auto& player : players) {
        if (losses[player] <= 1) {
            result.push_back(player);
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of matches and $m$ is the number of players. This is because we iterate through the matches and players once.
> - **Space Complexity:** $O(m)$, where $m$ is the number of players. This is because we store the losses for each player in a dictionary.
> - **Optimality proof:** This approach is optimal because we only iterate through the matches once and store the losses for each player in a dictionary.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a dictionary to store the number of losses for each player and iterating through the matches to update the losses.
- Problem-solving patterns identified: Iterating through the matches and players to update the losses and returning a list of players with zero or one losses.
- Optimization techniques learned: Using a dictionary to store the losses for each player and iterating through the matches only once.
- Similar problems to practice: Other problems that involve iterating through matches or games and updating the wins and losses for each player.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the dictionary to store the losses for each player or not updating the losses correctly.
- Edge cases to watch for: Players with zero losses or players with one loss.
- Performance pitfalls: Iterating through the matches multiple times or using a data structure that is not efficient for storing the losses for each player.
- Testing considerations: Testing the function with different inputs and edge cases to ensure that it returns the correct result.