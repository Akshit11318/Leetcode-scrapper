## Longest Winning Streak

**Problem Link:** https://leetcode.com/problems/longest-winning-streak/description

**Problem Statement:**
- Input: A 2D array `matches` where each element is an array of two integers, representing the winner and loser of a match.
- Constraints: The input array will not be empty, and each match will have a winner and a loser.
- Expected Output: The length of the longest winning streak.
- Key Requirements: Determine the longest sequence of wins for any player.
- Edge Cases: Consider scenarios with multiple players, ties, or players with no wins.

**Example Test Cases:**
- `matches = [[1,3],[2,3],[3,6],[1,2],[2,3],[3,6],[1,2],[4,5],[4,6]]`: The longest winning streak is 4, achieved by player 3.
- `matches = [[1,3],[2,3]]`: The longest winning streak is 2, achieved by player 3.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to simulate each match and keep track of the wins for each player.
- For each match, update the win count for the winner and the loss count for the loser.
- After all matches are processed, find the player with the longest winning streak by comparing the win counts.

```cpp
#include <vector>
#include <unordered_map>

int longestWinningStreak(std::vector<std::vector<int>>& matches) {
    // Initialize a map to store the win counts for each player
    std::unordered_map<int, int> winCounts;
    std::unordered_map<int, int> currentStreaks;

    // Process each match
    for (const auto& match : matches) {
        int winner = match[0];
        int loser = match[1];

        // Update the win count for the winner
        winCounts[winner]++;
        currentStreaks[winner]++;

        // Reset the current streak for the loser
        currentStreaks[loser] = 0;
    }

    // Find the player with the longest winning streak
    int longestStreak = 0;
    for (const auto& streak : currentStreaks) {
        longestStreak = std::max(longestStreak, streak.second);
    }

    return longestStreak;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of matches. We process each match once and perform constant-time operations for each match.
> - **Space Complexity:** $O(n)$, where $n$ is the number of matches. In the worst case, we might need to store the win counts for each player, which could be equal to the number of matches.
> - **Why these complexities occur:** The time complexity is linear because we iterate through the matches once, and the space complexity is also linear because we store the win counts for each player.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach is similar to the brute force approach but with some optimizations.
- We can use a single map to store the current winning streak for each player.
- For each match, we update the current winning streak for the winner and reset it for the loser.
- We keep track of the maximum winning streak seen so far.

```cpp
#include <vector>
#include <unordered_map>

int longestWinningStreak(std::vector<std::vector<int>>& matches) {
    // Initialize a map to store the current winning streak for each player
    std::unordered_map<int, int> currentStreaks;
    int maxStreak = 0;

    // Process each match
    for (const auto& match : matches) {
        int winner = match[0];
        int loser = match[1];

        // Update the current winning streak for the winner
        currentStreaks[winner]++;
        maxStreak = std::max(maxStreak, currentStreaks[winner]);

        // Reset the current winning streak for the loser
        currentStreaks[loser] = 0;
    }

    return maxStreak;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of matches. We process each match once and perform constant-time operations for each match.
> - **Space Complexity:** $O(n)$, where $n$ is the number of matches. In the worst case, we might need to store the current winning streak for each player, which could be equal to the number of matches.
> - **Optimality proof:** This approach is optimal because we only process each match once and keep track of the necessary information to determine the longest winning streak.

---

### Final Notes

**Learning Points:**
- The importance of using maps to store and update player information efficiently.
- The need to consider edge cases, such as players with no wins or ties.
- The optimization technique of using a single map to store the current winning streak for each player.

**Mistakes to Avoid:**
- Not initializing the map correctly or not updating the current winning streak for each player.
- Not considering edge cases, such as players with no wins or ties.
- Not using the most efficient data structures and algorithms to solve the problem.