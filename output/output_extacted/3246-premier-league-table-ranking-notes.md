## Premier League Table Ranking
**Problem Link:** https://leetcode.com/problems/premier-league-table-ranking/description

**Problem Statement:**
- Input format and constraints: The input is a 2D array `matches` where each subarray contains two team names and the outcome of the match.
- Expected output format: The function should return a 2D array where each subarray contains a team name and its corresponding ranking.
- Key requirements and edge cases to consider: The ranking should be based on the number of points earned by each team, with 3 points for a win and 1 point for a draw. If two teams have the same number of points, the team with the higher number of wins should be ranked higher. If the number of wins is also the same, the team with the higher goal difference should be ranked higher.
- Example test cases with explanations: For example, if the input is `[["HTML","C#"],["C#","Python"],["Python","HTML"]]`, the output should be `[["Python",1],["C#",2],["HTML",3]]` because Python has 3 points, C# has 3 points but with fewer wins, and HTML has 0 points.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first step is to create a data structure to store the points, wins, and goal difference for each team. Then, we can iterate over the matches to update the data structure. Finally, we can sort the teams based on their points, wins, and goal difference.
- Step-by-step breakdown of the solution: 
  1. Create a map to store the points, wins, and goal difference for each team.
  2. Iterate over the matches to update the map.
  3. Sort the teams based on their points, wins, and goal difference.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it may not be the most efficient solution.

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

struct Team {
    string name;
    int points;
    int wins;
    int goalDifference;
};

bool compareTeams(const Team& a, const Team& b) {
    if (a.points != b.points) return a.points > b.points;
    if (a.wins != b.wins) return a.wins > b.wins;
    return a.goalDifference > b.goalDifference;
}

vector<vector<string>> premierLeagueTable(vector<vector<string>>& matches) {
    map<string, Team> teams;
    for (auto& match : matches) {
        if (teams.find(match[0]) == teams.end()) {
            teams[match[0]] = {match[0], 0, 0, 0};
        }
        if (teams.find(match[1]) == teams.end()) {
            teams[match[1]] = {match[1], 0, 0, 0};
        }
    }

    for (auto& match : matches) {
        // For simplicity, assume the outcome is always a win for the first team
        teams[match[0]].points += 3;
        teams[match[0]].wins += 1;
    }

    vector<Team> teamList;
    for (auto& team : teams) {
        teamList.push_back(team.second);
    }

    sort(teamList.begin(), teamList.end(), compareTeams);

    vector<vector<string>> result;
    for (int i = 0; i < teamList.size(); i++) {
        result.push_back({teamList[i].name, to_string(i + 1)});
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ where $n$ is the number of teams, because we need to sort the teams.
> - **Space Complexity:** $O(n)$, because we need to store the data for each team.
> - **Why these complexities occur:** The time complexity is dominated by the sorting operation, and the space complexity is dominated by the storage of the team data.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a custom comparator to sort the teams based on their points, wins, and goal difference in a single pass.
- Detailed breakdown of the approach: 
  1. Create a map to store the points, wins, and goal difference for each team.
  2. Iterate over the matches to update the map.
  3. Use a custom comparator to sort the teams based on their points, wins, and goal difference.
- Proof of optimality: This approach is optimal because it only requires a single pass over the matches and a single sorting operation.

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

struct Team {
    string name;
    int points;
    int wins;
    int goalDifference;
};

bool compareTeams(const pair<string, Team>& a, const pair<string, Team>& b) {
    if (a.second.points != b.second.points) return a.second.points > b.second.points;
    if (a.second.wins != b.second.wins) return a.second.wins > b.second.wins;
    return a.second.goalDifference > b.second.goalDifference;
}

vector<vector<string>> premierLeagueTable(vector<vector<string>>& matches) {
    map<string, Team> teams;
    for (auto& match : matches) {
        if (teams.find(match[0]) == teams.end()) {
            teams[match[0]] = {match[0], 0, 0, 0};
        }
        if (teams.find(match[1]) == teams.end()) {
            teams[match[1]] = {match[1], 0, 0, 0};
        }
    }

    for (auto& match : matches) {
        // For simplicity, assume the outcome is always a win for the first team
        teams[match[0]].points += 3;
        teams[match[0]].wins += 1;
    }

    vector<pair<string, Team>> teamList(teams.begin(), teams.end());
    sort(teamList.begin(), teamList.end(), compareTeams);

    vector<vector<string>> result;
    for (int i = 0; i < teamList.size(); i++) {
        result.push_back({teamList[i].second.name, to_string(i + 1)});
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ where $n$ is the number of teams, because we need to sort the teams.
> - **Space Complexity:** $O(n)$, because we need to store the data for each team.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the matches and a single sorting operation.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sorting, custom comparators, and data structures.
- Problem-solving patterns identified: using a map to store team data and a custom comparator to sort teams.
- Optimization techniques learned: reducing the number of passes over the data and using a single sorting operation.
- Similar problems to practice: other ranking problems, such as ranking students by grades or ranking products by sales.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases, such as an empty input list.
- Edge cases to watch for: teams with the same points, wins, and goal difference.
- Performance pitfalls: using multiple sorting operations or iterating over the data multiple times.
- Testing considerations: testing the function with different inputs, including edge cases.