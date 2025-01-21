## Premier League Table Ranking III
**Problem Link:** https://leetcode.com/problems/premier-league-table-ranking-iii/description

**Problem Statement:**
- Input format: An array of strings `results`, where each string is in the format "Team1,Score1,Team2,Score2".
- Constraints: Each team plays every other team exactly once.
- Expected output format: A list of integers representing the ranking of the teams.
- Key requirements and edge cases to consider:
  - A team gets 3 points for a win, 1 point for a draw, and 0 points for a loss.
  - Teams are ranked based on their total points, then goal difference, and finally goals scored.
- Example test cases with explanations:
  - Example 1:
    - Input: results = ["HTML,10,JS,0","JS,2,Python,1","Python,10,HTML,0"]
    - Output: [1,2,3]
  - Example 2:
    - Input: results = ["HTML,6,JS,1","JS,1,Python,10","Python,2,HTML,1"]
    - Output: [1,2,3]

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Create a map to store the points, goal difference, and goals scored for each team. Then, iterate over the results to update the team statistics. Finally, sort the teams based on their points, goal difference, and goals scored.
- Step-by-step breakdown of the solution:
  1. Initialize a map to store the team statistics.
  2. Iterate over the results to update the team statistics.
  3. Sort the teams based on their points, goal difference, and goals scored.
- Why this approach comes to mind first: It is a straightforward and intuitive approach to solve the problem.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

struct Team {
    int points;
    int goalDiff;
    int goalsScored;
};

bool compareTeams(Team a, Team b) {
    if (a.points != b.points) return a.points > b.points;
    if (a.goalDiff != b.goalDiff) return a.goalDiff > b.goalDiff;
    return a.goalsScored > b.goalsScored;
}

vector<int> premierLeague(vector<string>& results) {
    map<string, Team> teamStats;
    for (const auto& result : results) {
        string team1, team2, score1, score2;
        size_t pos = result.find(',');
        team1 = result.substr(0, pos);
        size_t pos1 = result.find(',', pos + 1);
        score1 = result.substr(pos + 1, pos1 - pos - 1);
        size_t pos2 = result.find(',', pos1 + 1);
        team2 = result.substr(pos1 + 1, pos2 - pos1 - 1);
        score2 = result.substr(pos2 + 1);

        int score1Int = stoi(score1);
        int score2Int = stoi(score2);

        if (teamStats.find(team1) == teamStats.end()) {
            teamStats[team1] = {0, 0, 0};
        }
        if (teamStats.find(team2) == teamStats.end()) {
            teamStats[team2] = {0, 0, 0};
        }

        if (score1Int > score2Int) {
            teamStats[team1].points += 3;
        } else if (score1Int < score2Int) {
            teamStats[team2].points += 3;
        } else {
            teamStats[team1].points += 1;
            teamStats[team2].points += 1;
        }

        teamStats[team1].goalDiff += score1Int - score2Int;
        teamStats[team2].goalDiff += score2Int - score1Int;
        teamStats[team1].goalsScored += score1Int;
        teamStats[team2].goalsScored += score2Int;
    }

    vector<Team> teams;
    for (const auto& pair : teamStats) {
        teams.push_back(pair.second);
    }

    sort(teams.begin(), teams.end(), compareTeams);

    vector<int> ranking;
    for (size_t i = 0; i < teams.size(); i++) {
        ranking.push_back(i + 1);
    }

    return ranking;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of teams. The time complexity is dominated by the sorting operation.
> - **Space Complexity:** $O(n)$, where $n$ is the number of teams. The space complexity is dominated by the map used to store the team statistics.
> - **Why these complexities occur:** The time complexity occurs because we need to sort the teams based on their points, goal difference, and goals scored. The space complexity occurs because we need to store the team statistics in a map.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a struct to store the team statistics and a vector to store the teams. We can then use the `sort` function to sort the teams based on their points, goal difference, and goals scored.
- Detailed breakdown of the approach:
  1. Initialize a map to store the team statistics.
  2. Iterate over the results to update the team statistics.
  3. Create a vector of teams and sort it based on the team statistics.
- Proof of optimality: This approach is optimal because it has a time complexity of $O(n \log n)$, which is the best possible time complexity for sorting $n$ elements.
- Why further optimization is impossible: Further optimization is impossible because the time complexity is already optimal.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

struct Team {
    string name;
    int points;
    int goalDiff;
    int goalsScored;
};

bool compareTeams(Team a, Team b) {
    if (a.points != b.points) return a.points > b.points;
    if (a.goalDiff != b.goalDiff) return a.goalDiff > b.goalDiff;
    return a.goalsScored > b.goalsScored;
}

vector<int> premierLeague(vector<string>& results) {
    map<string, Team> teamStats;
    for (const auto& result : results) {
        string team1, team2, score1, score2;
        size_t pos = result.find(',');
        team1 = result.substr(0, pos);
        size_t pos1 = result.find(',', pos + 1);
        score1 = result.substr(pos + 1, pos1 - pos - 1);
        size_t pos2 = result.find(',', pos1 + 1);
        team2 = result.substr(pos1 + 1, pos2 - pos1 - 1);
        score2 = result.substr(pos2 + 1);

        int score1Int = stoi(score1);
        int score2Int = stoi(score2);

        if (teamStats.find(team1) == teamStats.end()) {
            teamStats[team1] = {team1, 0, 0, 0};
        }
        if (teamStats.find(team2) == teamStats.end()) {
            teamStats[team2] = {team2, 0, 0, 0};
        }

        if (score1Int > score2Int) {
            teamStats[team1].points += 3;
        } else if (score1Int < score2Int) {
            teamStats[team2].points += 3;
        } else {
            teamStats[team1].points += 1;
            teamStats[team2].points += 1;
        }

        teamStats[team1].goalDiff += score1Int - score2Int;
        teamStats[team2].goalDiff += score2Int - score1Int;
        teamStats[team1].goalsScored += score1Int;
        teamStats[team2].goalsScored += score2Int;
    }

    vector<Team> teams;
    for (const auto& pair : teamStats) {
        teams.push_back(pair.second);
    }

    sort(teams.begin(), teams.end(), compareTeams);

    vector<int> ranking;
    for (size_t i = 0; i < teams.size(); i++) {
        ranking.push_back(i + 1);
    }

    return ranking;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of teams. The time complexity is dominated by the sorting operation.
> - **Space Complexity:** $O(n)$, where $n$ is the number of teams. The space complexity is dominated by the map used to store the team statistics.
> - **Optimality proof:** This approach is optimal because it has a time complexity of $O(n \log n)$, which is the best possible time complexity for sorting $n$ elements.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sorting, map usage, and struct usage.
- Problem-solving patterns identified: using a map to store team statistics and sorting teams based on their points, goal difference, and goals scored.
- Optimization techniques learned: using a struct to store team statistics and using the `sort` function to sort teams.
- Similar problems to practice: other problems that involve sorting and using maps or structs.

**Mistakes to Avoid:**
- Common implementation errors: not checking if a team exists in the map before updating its statistics.
- Edge cases to watch for: teams with the same points, goal difference, and goals scored.
- Performance pitfalls: using a slow sorting algorithm or not using a map to store team statistics.
- Testing considerations: testing the function with different inputs and edge cases to ensure it works correctly.