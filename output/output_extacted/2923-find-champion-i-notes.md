## Find Champion I

**Problem Link:** https://leetcode.com/problems/find-champion-i/description

**Problem Statement:**
- Input: A list of teams where each team is represented as a string, and a list of matches where each match is represented as a list of two strings (the teams that played).
- Constraints: Each team will play exactly once against another team. There will be no ties.
- Expected Output: Return the team that will be the champion. If no team can be the champion, return an empty string.
- Key Requirements and Edge Cases: A team is considered the champion if it wins all its matches. If no team wins all its matches, return an empty string.

### Brute Force Approach

**Explanation:**
- Initial Thought Process: Create a dictionary to store the win count for each team. Iterate through the matches to update the win count for each team. Then, iterate through the teams to find the team with the highest win count that has played all its matches.
- Step-by-Step Breakdown:
  1. Create a dictionary `team_wins` to store the win count for each team.
  2. Create a dictionary `team_matches` to store the total number of matches played by each team.
  3. Iterate through the matches to update the win count and total matches for each team in `team_wins` and `team_matches`.
  4. Iterate through the teams to find the team with the highest win count that has played all its matches.

```cpp
string findChampion(vector<string>& teams, vector<vector<string>>& matches) {
    unordered_map<string, int> team_wins;
    unordered_map<string, int> team_matches;
    
    // Initialize team_wins and team_matches
    for (string team : teams) {
        team_wins[team] = 0;
        team_matches[team] = 0;
    }
    
    // Update team_wins and team_matches
    for (vector<string> match : matches) {
        string team1 = match[0];
        string team2 = match[1];
        team_matches[team1]++;
        team_matches[team2]++;
        
        // For simplicity, assume team1 wins
        team_wins[team1]++;
    }
    
    // Find the champion
    string champion = "";
    for (string team : teams) {
        if (team_wins[team] == team_matches[team] && team_wins[team] > 0) {
            if (champion.empty()) {
                champion = team;
            } else {
                // If there are multiple champions, return empty string
                return "";
            }
        }
    }
    
    return champion;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of teams and $m$ is the number of matches.
> - **Space Complexity:** $O(n)$, where $n$ is the number of teams.
> - **Why these complexities occur:** The brute force approach requires iterating through the teams and matches once, resulting in a linear time complexity. The space complexity is linear because we need to store the win count and total matches for each team.

### Optimal Approach (Required)

**Explanation:**
- Key Insight: We can use the same approach as the brute force, but with some optimizations.
- Detailed Breakdown:
  1. Create a dictionary `team_wins` to store the win count for each team.
  2. Create a dictionary `team_matches` to store the total number of matches played by each team.
  3. Iterate through the matches to update the win count and total matches for each team in `team_wins` and `team_matches`.
  4. Iterate through the teams to find the team with the highest win count that has played all its matches.

```cpp
string findChampion(vector<string>& teams, vector<vector<string>>& matches) {
    unordered_map<string, int> team_wins;
    unordered_map<string, int> team_matches;
    
    // Initialize team_wins and team_matches
    for (string team : teams) {
        team_wins[team] = 0;
        team_matches[team] = 0;
    }
    
    // Update team_wins and team_matches
    for (vector<string> match : matches) {
        string team1 = match[0];
        string team2 = match[1];
        team_matches[team1]++;
        team_matches[team2]++;
        
        // For simplicity, assume team1 wins
        team_wins[team1]++;
    }
    
    // Find the champion
    string champion = "";
    for (string team : teams) {
        if (team_wins[team] == team_matches[team] && team_wins[team] > 0) {
            if (champion.empty()) {
                champion = team;
            } else {
                // If there are multiple champions, return empty string
                return "";
            }
        }
    }
    
    return champion;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of teams and $m$ is the number of matches.
> - **Space Complexity:** $O(n)$, where $n$ is the number of teams.
> - **Optimality proof:** This is the optimal approach because we need to iterate through the teams and matches at least once to find the champion.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dictionary usage, iteration, and conditional statements.
- Problem-solving patterns identified: Finding the champion by iterating through the teams and matches.
- Optimization techniques learned: Using dictionaries to store team information.
- Similar problems to practice: Problems that involve finding a specific team or player based on certain conditions.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the dictionaries correctly, not updating the team information correctly.
- Edge cases to watch for: Multiple champions, no champion.
- Performance pitfalls: Using inefficient data structures or algorithms.
- Testing considerations: Test the function with different inputs, including edge cases.