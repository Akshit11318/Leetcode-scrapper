## Longest Team Pass Streak
**Problem Link:** https://leetcode.com/problems/longest-team-pass-streak/description

**Problem Statement:**
- Input format and constraints: Given a list of integers `matches` where `matches[i] = [team_i, score_i, opponent_i, opponent_score_i]`, determine the longest streak of wins for each team.
- Expected output format: Return a list of integers representing the longest streak of wins for each team in the order of team IDs.
- Key requirements and edge cases to consider: 
  - A team is considered to have won if their score is greater than their opponent's score.
  - If a team has not played any games, their longest streak is 0.
  - If a team has played games but has not won any, their longest streak is 0.
- Example test cases with explanations:
  - For `matches = [[1,3,0,0],[2,3,0,0],[3,6,1,3],[4,5,1,1],[5,4,0,0]]`, the output should be `[3,3,2,2,2]`, as the longest winning streaks for teams 1, 2, 3, 4, and 5 are 3, 3, 2, 2, and 2 respectively.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward approach is to iterate through each match for each team, keeping track of the current streak and updating the maximum streak as necessary.
- Step-by-step breakdown of the solution:
  1. Initialize a dictionary to store the longest streak for each team.
  2. Iterate through each match.
  3. For each match, determine the winner (if any) and update the current streak for the winning team.
  4. Update the maximum streak for the winning team if the current streak is greater.
  5. Repeat steps 2-4 until all matches have been processed.
- Why this approach comes to mind first: It directly addresses the problem by simulating the process of teams playing matches and updating their streaks accordingly.

```cpp
#include <vector>
#include <unordered_map>

std::vector<int> longestStreak(std::vector<std::vector<int>>& matches) {
    std::unordered_map<int, int> teamStreaks; // team_id, current_streak
    std::unordered_map<int, int> maxStreaks; // team_id, max_streak

    for (const auto& match : matches) {
        int team = match[0];
        int opponent = match[2];
        int teamScore = match[1];
        int opponentScore = match[3];

        if (teamScore > opponentScore) {
            // Team wins, update current streak
            if (teamStreaks.find(team) == teamStreaks.end()) {
                teamStreaks[team] = 1;
            } else {
                teamStreaks[team]++;
            }

            // Update max streak if necessary
            if (maxStreaks.find(team) == maxStreaks.end() || teamStreaks[team] > maxStreaks[team]) {
                maxStreaks[team] = teamStreaks[team];
            }
        } else {
            // Team loses, reset current streak
            teamStreaks[team] = 0;
        }

        if (opponentScore > teamScore) {
            // Opponent wins, update current streak
            if (teamStreaks.find(opponent) == teamStreaks.end()) {
                teamStreaks[opponent] = 1;
            } else {
                teamStreaks[opponent]++;
            }

            // Update max streak if necessary
            if (maxStreaks.find(opponent) == maxStreaks.end() || teamStreaks[opponent] > maxStreaks[opponent]) {
                maxStreaks[opponent] = teamStreaks[opponent];
            }
        } else {
            // Opponent loses, reset current streak
            teamStreaks[opponent] = 0;
        }
    }

    std::vector<int> result;
    for (int team = 0; team <= matches.size(); team++) {
        if (maxStreaks.find(team) != maxStreaks.end()) {
            result.push_back(maxStreaks[team]);
        } else {
            result.push_back(0);
        }
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of matches and $m$ is the average number of teams involved in a match, because we are potentially updating streaks for both teams in each match.
> - **Space Complexity:** $O(n)$ for storing the streaks of all teams.
> - **Why these complexities occur:** The time complexity is due to the iteration over all matches and the potential update of streaks for each team in a match. The space complexity is due to the storage of streaks for all teams.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of processing each match individually and updating streaks, we can first build a dictionary of teams and their matches, then process the matches for each team to calculate the longest streak.
- Detailed breakdown of the approach:
  1. Initialize dictionaries to store matches for each team and the longest streak for each team.
  2. Iterate through each match to populate the dictionary of matches for each team.
  3. For each team, iterate through their matches to calculate the current streak and update the maximum streak as necessary.
  4. After processing all matches for a team, store the maximum streak found.
- Why further optimization is impossible: This approach minimizes the number of iterations over the matches and directly calculates the longest streak for each team, making it optimal in terms of time complexity.

```cpp
#include <vector>
#include <unordered_map>

std::vector<int> longestStreak(std::vector<std::vector<int>>& matches) {
    std::unordered_map<int, std::vector<std::pair<int, int>>> teamMatches; // team_id, [(opponent, result)]
    std::unordered_map<int, int> maxStreaks; // team_id, max_streak

    for (const auto& match : matches) {
        int team = match[0];
        int opponent = match[2];
        int teamScore = match[1];
        int opponentScore = match[3];
        bool teamWon = teamScore > opponentScore;

        teamMatches[team].push_back({opponent, teamWon});
        teamMatches[opponent].push_back({team, !teamWon});
    }

    for (const auto& [team, matches] : teamMatches) {
        int currentStreak = 0;
        int maxStreak = 0;

        for (const auto& [opponent, won] : matches) {
            if (won) {
                currentStreak++;
                maxStreak = std::max(maxStreak, currentStreak);
            } else {
                currentStreak = 0;
            }
        }

        maxStreaks[team] = maxStreak;
    }

    std::vector<int> result;
    for (int team = 0; team <= matches.size(); team++) {
        if (maxStreaks.find(team) != maxStreaks.end()) {
            result.push_back(maxStreaks[team]);
        } else {
            result.push_back(0);
        }
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the total number of matches, because we process each match twice (once for each team involved).
> - **Space Complexity:** $O(n)$ for storing the matches and streaks of all teams.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to calculate the longest streak for each team, processing each match exactly twice.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, dictionary usage for efficient lookup and storage.
- Problem-solving patterns identified: Breaking down complex problems into simpler, manageable parts (processing matches for each team separately).
- Optimization techniques learned: Minimizing the number of iterations over data, using dictionaries for efficient storage and lookup.
- Similar problems to practice: Other problems involving processing and analyzing sequences of events or matches.

**Mistakes to Avoid:**
- Common implementation errors: Not resetting the current streak when a team loses, not updating the maximum streak correctly.
- Edge cases to watch for: Teams with no matches, teams with only losses.
- Performance pitfalls: Processing each match multiple times unnecessarily, using inefficient data structures for storage and lookup.
- Testing considerations: Ensure to test with various inputs, including edge cases like teams with no matches or only losses.