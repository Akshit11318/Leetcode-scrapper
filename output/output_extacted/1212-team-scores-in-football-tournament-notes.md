## Team Scores in Football Tournament
**Problem Link:** https://leetcode.com/problems/team-scores-in-football-tournament/description

**Problem Statement:**
- Input format: A 2D array `matches` where each match is represented as an array of four integers `[team1, team2, score1, score2]`.
- Constraints: Each team will play exactly one match against another team.
- Expected output format: Return an array of integers representing the scores of all teams in no particular order.
- Key requirements and edge cases to consider: Teams are represented by integers, scores are non-negative integers, and there are no ties in the scores.
- Example test cases with explanations:
    - Example 1: `matches = [[1,3,0,2],[2,1,3,1],[3,6,1,3],[6,1,2,3],[5,4,2,1],[3,5,3,3],[1,2,0,3]]`, the output will be `[5,6,3,3,3,0]`.

### Brute Force Approach
**Explanation:**
- Initial thought process: Create a dictionary to store the scores of each team and then update the scores based on the matches.
- Step-by-step breakdown of the solution:
    1. Initialize a dictionary to store the scores of each team.
    2. Iterate over each match in the `matches` array.
    3. For each match, update the scores of the two teams in the dictionary.
    4. Finally, return the scores of all teams as an array.
- Why this approach comes to mind first: It's a straightforward way to solve the problem by iterating over each match and updating the scores accordingly.

```cpp
vector<int> findScoreOfTeam(int team, vector<vector<int>>& matches) {
    vector<int> scores(1, 0);
    for (auto& match : matches) {
        if (match[0] == team) {
            if (match[2] > match[3]) {
                scores[0] += 3;
            } else if (match[2] == match[3]) {
                scores[0] += 1;
            }
        } else if (match[1] == team) {
            if (match[2] < match[3]) {
                scores[0] += 3;
            } else if (match[2] == match[3]) {
                scores[0] += 1;
            }
        }
    }
    return scores;
}

vector<int> teamScores(vector<vector<int>>& matches) {
    set<int> teams;
    for (auto& match : matches) {
        teams.insert(match[0]);
        teams.insert(match[1]);
    }
    vector<int> result;
    for (auto& team : teams) {
        result.push_back(findScoreOfTeam(team, matches)[0]);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of teams and $m$ is the number of matches.
> - **Space Complexity:** $O(n + m)$ for storing the teams and matches.
> - **Why these complexities occur:** The time complexity is due to iterating over each match for each team, and the space complexity is for storing the teams and matches.

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of iterating over each match for each team, we can iterate over each match only once and update the scores of both teams in that match.
- Detailed breakdown of the approach:
    1. Initialize a dictionary to store the scores of each team.
    2. Iterate over each match in the `matches` array.
    3. For each match, update the scores of the two teams in the dictionary.
    4. Finally, return the scores of all teams as an array.
- Proof of optimality: This approach has a time complexity of $O(n + m)$, which is the best possible time complexity for this problem because we need to at least read the input.

```cpp
vector<int> teamScores(vector<vector<int>>& matches) {
    unordered_map<int, int> scores;
    for (auto& match : matches) {
        int team1 = match[0];
        int team2 = match[1];
        int score1 = match[2];
        int score2 = match[3];
        scores[team1] += score1 > score2 ? 3 : score1 == score2 ? 1 : 0;
        scores[team2] += score1 < score2 ? 3 : score1 == score2 ? 1 : 0;
    }
    vector<int> result;
    for (auto& pair : scores) {
        result.push_back(pair.second);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ where $n$ is the number of teams and $m$ is the number of matches.
> - **Space Complexity:** $O(n)$ for storing the teams and their scores.
> - **Optimality proof:** This approach has the best possible time complexity because we only need to iterate over each match once and update the scores of both teams in that match.

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Hashing, iteration, and conditional statements.
- Problem-solving patterns identified: Using a dictionary to store the scores of each team and updating the scores based on the matches.
- Optimization techniques learned: Reducing the time complexity by iterating over each match only once.
- Similar problems to practice: Other problems that involve iterating over a list of matches or games and updating scores or states.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the dictionary or not updating the scores correctly.
- Edge cases to watch for: Teams with no matches or matches with no scores.
- Performance pitfalls: Iterating over each match for each team, which can lead to a high time complexity.
- Testing considerations: Test the function with different inputs, including empty lists of matches and lists with multiple matches for the same team.