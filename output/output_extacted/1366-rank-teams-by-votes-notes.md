## Rank Teams by Votes
**Problem Link:** https://leetcode.com/problems/rank-teams-by-votes/description

**Problem Statement:**
- Input format and constraints: Given a list of strings representing votes where each string is a team and each character in the string represents a team's ranking in a particular vote.
- Expected output format: Return a list of strings representing the ranked teams based on the input votes.
- Key requirements and edge cases to consider: If a team is not present in a vote, it should be ranked last. If two teams have the same ranking, the team with the higher name (lexicographically) should be ranked higher.
- Example test cases with explanations: 
    - Input: ["ABC","ACB","ABC","ACB","ACB"]
    - Output: ["ACB","ABC"]

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Create a `map` to store the frequency of each ranking for each team, then sort the teams based on these rankings.
- Step-by-step breakdown of the solution: 
    1. Initialize a `map` to store the rankings of each team.
    2. Iterate over each vote and update the rankings in the `map`.
    3. Sort the teams based on their rankings.
- Why this approach comes to mind first: It is the most straightforward way to solve the problem, as it directly counts the votes for each team and ranking.

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

vector<string> rankTeams(vector<string>& votes) {
    int n = votes.size();
    int k = votes[0].size();
    map<string, vector<int>> rankings;
    
    for (const auto& vote : votes) {
        for (int i = 0; i < k; i++) {
            string team(1, vote[i]);
            if (rankings.find(team) == rankings.end()) {
                rankings[team] = vector<int>(k, 0);
            }
            rankings[team][i]++;
        }
    }
    
    vector<string> teams;
    for (const auto& pair : rankings) {
        teams.push_back(pair.first);
    }
    
    sort(teams.begin(), teams.end(), [&rankings, k](const string& a, const string& b) {
        for (int i = 0; i < k; i++) {
            if (rankings[a][i] > rankings[b][i]) return true;
            if (rankings[a][i] < rankings[b][i]) return false;
        }
        return a < b;
    });
    
    return teams;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k \cdot k \cdot log(k))$, where $n$ is the number of votes and $k$ is the number of teams. This is because we are iterating over each vote and each team, and then sorting the teams based on their rankings.
> - **Space Complexity:** $O(k \cdot k)$, where $k$ is the number of teams. This is because we are storing the rankings of each team in a `map`.
> - **Why these complexities occur:** The time complexity occurs because we are iterating over each vote and each team, and then sorting the teams based on their rankings. The space complexity occurs because we are storing the rankings of each team in a `map`.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a `vector` of `pair` to store the rankings of each team, and then sort the teams based on these rankings.
- Detailed breakdown of the approach: 
    1. Initialize a `vector` of `pair` to store the rankings of each team.
    2. Iterate over each vote and update the rankings in the `vector`.
    3. Sort the teams based on their rankings.
- Proof of optimality: This solution is optimal because it has the same time complexity as the brute force approach, but it uses less space because it does not use a `map`.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<string> rankTeams(vector<string>& votes) {
    int n = votes.size();
    int k = votes[0].size();
    vector<pair<string, vector<int>>> rankings(k);
    
    for (int i = 0; i < k; i++) {
        rankings[i].first = string(1, votes[0][i]);
        rankings[i].second = vector<int>(k, 0);
    }
    
    for (const auto& vote : votes) {
        for (int i = 0; i < k; i++) {
            for (auto& pair : rankings) {
                if (pair.first == string(1, vote[i])) {
                    pair.second[i]++;
                    break;
                }
            }
        }
    }
    
    sort(rankings.begin(), rankings.end(), [k](const auto& a, const auto& b) {
        for (int i = 0; i < k; i++) {
            if (a.second[i] > b.second[i]) return true;
            if (a.second[i] < b.second[i]) return false;
        }
        return a.first < b.first;
    });
    
    vector<string> result;
    for (const auto& pair : rankings) {
        result.push_back(pair.first);
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k^2)$, where $n$ is the number of votes and $k$ is the number of teams. This is because we are iterating over each vote and each team, and then sorting the teams based on their rankings.
> - **Space Complexity:** $O(k^2)$, where $k$ is the number of teams. This is because we are storing the rankings of each team in a `vector`.
> - **Optimality proof:** This solution is optimal because it has the same time complexity as the brute force approach, but it uses less space because it does not use a `map`.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sorting, ranking, and voting systems.
- Problem-solving patterns identified: using a `vector` of `pair` to store rankings and sorting teams based on these rankings.
- Optimization techniques learned: using a `vector` instead of a `map` to store rankings.
- Similar problems to practice: other problems involving ranking and voting systems.

**Mistakes to Avoid:**
- Common implementation errors: not initializing variables, not checking for edge cases, and not using the correct data structures.
- Edge cases to watch for: teams with the same ranking, teams not present in a vote, and votes with different lengths.
- Performance pitfalls: using inefficient algorithms, not optimizing space complexity, and not considering edge cases.
- Testing considerations: testing with different inputs, testing with edge cases, and testing with large inputs.