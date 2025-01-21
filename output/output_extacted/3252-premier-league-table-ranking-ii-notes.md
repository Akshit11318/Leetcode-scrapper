## Premier League Table Ranking II
**Problem Link:** https://leetcode.com/problems/premier-league-table-ranking-ii/description

**Problem Statement:**
- Input format and constraints: The problem involves ranking teams in a premier league table based on their match results. We are given a list of match results where each match result is represented as a string in the format "Team1#Team2#Score1#Score2" where Team1 and Team2 are the names of the two teams, and Score1 and Score2 are the scores of the two teams in the match. The constraints include that each team plays each other team exactly once.
- Expected output format: The output should be a list of team names in descending order of their rankings based on the match results.
- Key requirements and edge cases to consider: The ranking should be based on the total points earned by each team, with points being awarded as 3 points for a win, 1 point for a draw, and 0 points for a loss. If two or more teams have the same number of points, the team with the higher goal difference should be ranked higher. If the goal difference is also the same, the team with the higher total number of goals scored should be ranked higher.
- Example test cases with explanations: For example, if the input is ["HTML#C#0#2","C#HTML#5#1","C#HTML#0#2"], the output should be ["C","HTML"] because team C has 3 points and team HTML has 0 points.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to iterate through each match result, update the points, goal difference, and total goals for each team, and then sort the teams based on these criteria.
- Step-by-step breakdown of the solution:
  1. Create a data structure to store the points, goal difference, and total goals for each team.
  2. Iterate through each match result, update the points, goal difference, and total goals for each team.
  3. Sort the teams based on the points, goal difference, and total goals.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it may not be the most efficient solution.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

struct Team {
    std::string name;
    int points;
    int goalDifference;
    int totalGoals;
};

bool compareTeams(const Team& a, const Team& b) {
    if (a.points != b.points) return a.points > b.points;
    if (a.goalDifference != b.goalDifference) return a.goalDifference > b.goalDifference;
    return a.totalGoals > b.totalGoals;
}

std::vector<std::string> rankTeams(std::vector<std::string>& results) {
    std::map<std::string, Team> teams;
    for (const auto& result : results) {
        size_t pos1 = result.find('#');
        size_t pos2 = result.find('#', pos1 + 1);
        size_t pos3 = result.find('#', pos2 + 1);
        std::string team1 = result.substr(0, pos1);
        std::string team2 = result.substr(pos1 + 1, pos2 - pos1 - 1);
        int score1 = std::stoi(result.substr(pos2 + 1, pos3 - pos2 - 1));
        int score2 = std::stoi(result.substr(pos3 + 1));
        
        if (teams.find(team1) == teams.end()) {
            teams[team1] = {team1, 0, 0, 0};
        }
        if (teams.find(team2) == teams.end()) {
            teams[team2] = {team2, 0, 0, 0};
        }
        
        teams[team1].totalGoals += score1;
        teams[team2].totalGoals += score2;
        
        if (score1 > score2) {
            teams[team1].points += 3;
        } else if (score1 < score2) {
            teams[team2].points += 3;
        } else {
            teams[team1].points += 1;
            teams[team2].points += 1;
        }
        
        teams[team1].goalDifference += score1 - score2;
        teams[team2].goalDifference += score2 - score1;
    }
    
    std::vector<Team> teamList;
    for (const auto& team : teams) {
        teamList.push_back(team.second);
    }
    
    std::sort(teamList.begin(), teamList.end(), compareTeams);
    
    std::vector<std::string> rankedTeams;
    for (const auto& team : teamList) {
        rankedTeams.push_back(team.name);
    }
    
    return rankedTeams;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ where $n$ is the number of teams, because we need to sort the teams.
> - **Space Complexity:** $O(n)$, because we need to store the points, goal difference, and total goals for each team.
> - **Why these complexities occur:** The time complexity occurs because we need to sort the teams, and the space complexity occurs because we need to store the information for each team.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use a custom sorting function that compares teams based on their points, goal difference, and total goals.
- Detailed breakdown of the approach:
  1. Create a data structure to store the points, goal difference, and total goals for each team.
  2. Iterate through each match result, update the points, goal difference, and total goals for each team.
  3. Use a custom sorting function to sort the teams based on the points, goal difference, and total goals.
- Proof of optimality: This approach is optimal because it has a time complexity of $O(n \log n)$, which is the best possible time complexity for sorting $n$ teams.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

struct Team {
    std::string name;
    int points;
    int goalDifference;
    int totalGoals;
};

bool compareTeams(const Team& a, const Team& b) {
    if (a.points != b.points) return a.points > b.points;
    if (a.goalDifference != b.goalDifference) return a.goalDifference > b.goalDifference;
    return a.totalGoals > b.totalGoals;
}

std::vector<std::string> rankTeams(std::vector<std::string>& results) {
    std::map<std::string, Team> teams;
    for (const auto& result : results) {
        size_t pos1 = result.find('#');
        size_t pos2 = result.find('#', pos1 + 1);
        size_t pos3 = result.find('#', pos2 + 1);
        std::string team1 = result.substr(0, pos1);
        std::string team2 = result.substr(pos1 + 1, pos2 - pos1 - 1);
        int score1 = std::stoi(result.substr(pos2 + 1, pos3 - pos2 - 1));
        int score2 = std::stoi(result.substr(pos3 + 1));
        
        if (teams.find(team1) == teams.end()) {
            teams[team1] = {team1, 0, 0, 0};
        }
        if (teams.find(team2) == teams.end()) {
            teams[team2] = {team2, 0, 0, 0};
        }
        
        teams[team1].totalGoals += score1;
        teams[team2].totalGoals += score2;
        
        if (score1 > score2) {
            teams[team1].points += 3;
        } else if (score1 < score2) {
            teams[team2].points += 3;
        } else {
            teams[team1].points += 1;
            teams[team2].points += 1;
        }
        
        teams[team1].goalDifference += score1 - score2;
        teams[team2].goalDifference += score2 - score1;
    }
    
    std::vector<Team> teamList;
    for (const auto& team : teams) {
        teamList.push_back(team.second);
    }
    
    std::sort(teamList.begin(), teamList.end(), compareTeams);
    
    std::vector<std::string> rankedTeams;
    for (const auto& team : teamList) {
        rankedTeams.push_back(team.name);
    }
    
    return rankedTeams;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ where $n$ is the number of teams, because we need to sort the teams.
> - **Space Complexity:** $O(n)$, because we need to store the points, goal difference, and total goals for each team.
> - **Optimality proof:** This approach is optimal because it has a time complexity of $O(n \log n)$, which is the best possible time complexity for sorting $n$ teams.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sorting, custom comparison function.
- Problem-solving patterns identified: using a data structure to store information, iterating through each match result, using a custom sorting function.
- Optimization techniques learned: using a custom comparison function to sort teams based on multiple criteria.
- Similar problems to practice: other problems that involve sorting and custom comparison functions.

**Mistakes to Avoid:**
- Common implementation errors: forgetting to initialize variables, not handling edge cases.
- Edge cases to watch for: teams with the same number of points, goal difference, and total goals.
- Performance pitfalls: using an inefficient sorting algorithm, not using a custom comparison function.
- Testing considerations: testing the function with different inputs, including edge cases.