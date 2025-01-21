## League Statistics
**Problem Link:** https://leetcode.com/problems/league-statistics/description

**Problem Statement:**
- Input format and constraints: The input will be a list of integers representing the `results` of games played, where each integer is in the format `x:y`, with `x` being the score of the first team and `y` being the score of the second team. The number of teams is given as `n`.
- Expected output format: The function should return a list of integers representing the `statistics` of each team, with each integer being the number of games won by the team.
- Key requirements and edge cases to consider: The function should handle cases where a team wins, loses, or ties a game. It should also handle cases where a team does not play any games.
- Example test cases with explanations: For example, if the input is `["1:0", "2:1", "3:1"]` and `n = 3`, the output should be `[1, 1, 1]` because each team won one game.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to iterate over each game result and update the win count for each team.
- Step-by-step breakdown of the solution:
  1. Create a map to store the win count for each team.
  2. Iterate over each game result.
  3. For each game result, split the string into two parts: the score of the first team and the score of the second team.
  4. Compare the scores to determine the winner of the game.
  5. Update the win count for the winning team in the map.
  6. Finally, create a list of integers representing the win count for each team.

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <string>

using namespace std;

vector<int> leagueStatistics(vector<string>& results, int n) {
    map<int, int> winCount;
    for (int i = 1; i <= n; i++) {
        winCount[i] = 0;
    }
    
    for (string result : results) {
        int colonIndex = result.find(":");
        int score1 = stoi(result.substr(0, colonIndex));
        int score2 = stoi(result.substr(colonIndex + 1));
        
        if (score1 > score2) {
            winCount[1]++;
        } else if (score2 > score1) {
            winCount[2]++;
        }
    }
    
    vector<int> statistics;
    for (int i = 1; i <= n; i++) {
        statistics.push_back(winCount[i]);
    }
    
    return statistics;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot k)$, where $m$ is the number of game results and $k$ is the average length of a game result string. This is because we iterate over each game result and split the string into two parts.
> - **Space Complexity:** $O(n)$, where $n$ is the number of teams. This is because we use a map to store the win count for each team.
> - **Why these complexities occur:** The time complexity occurs because we iterate over each game result and perform string operations. The space complexity occurs because we use a map to store the win count for each team.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of using a map to store the win count for each team, we can use a vector of size `n` to store the win count for each team. This is because the team IDs are consecutive integers from 1 to `n`.
- Detailed breakdown of the approach:
  1. Create a vector of size `n` to store the win count for each team.
  2. Iterate over each game result.
  3. For each game result, split the string into two parts: the score of the first team and the score of the second team.
  4. Compare the scores to determine the winner of the game.
  5. Update the win count for the winning team in the vector.
  6. Finally, return the vector of win counts.

```cpp
vector<int> leagueStatistics(vector<string>& results, int n) {
    vector<int> winCount(n, 0);
    
    for (string result : results) {
        int colonIndex = result.find(":");
        int score1 = stoi(result.substr(0, colonIndex));
        int score2 = stoi(result.substr(colonIndex + 1));
        
        if (score1 > score2) {
            winCount[0]++;
        } else if (score2 > score1) {
            winCount[1]++;
        }
    }
    
    return winCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot k)$, where $m$ is the number of game results and $k$ is the average length of a game result string. This is because we iterate over each game result and split the string into two parts.
> - **Space Complexity:** $O(n)$, where $n$ is the number of teams. This is because we use a vector to store the win count for each team.
> - **Optimality proof:** This is the optimal solution because we use a vector to store the win count for each team, which has a constant time complexity for accessing and updating elements.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, string manipulation, and data storage using vectors.
- Problem-solving patterns identified: Using vectors to store data when the indices are consecutive integers.
- Optimization techniques learned: Using vectors instead of maps to store data when the indices are consecutive integers.
- Similar problems to practice: Problems that involve iterating over data and updating counts or statistics.

**Mistakes to Avoid:**
- Common implementation errors: Using maps instead of vectors to store data when the indices are consecutive integers.
- Edge cases to watch for: Handling cases where a team wins, loses, or ties a game.
- Performance pitfalls: Using inefficient data structures or algorithms that have high time complexities.
- Testing considerations: Testing the function with different inputs and edge cases to ensure it works correctly.