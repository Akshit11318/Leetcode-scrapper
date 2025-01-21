## Output Contest Matches

**Problem Link:** https://leetcode.com/problems/output-contest-matches/description

**Problem Statement:**
- Input format and constraints: The function `findWinner` takes two parameters: `n` (the number of teams) and `matches` (a vector of vectors where each inner vector contains two integers representing the teams competing against each other in a match).
- Expected output format: The function should return a vector of integers representing the matches that should be played in the contest.
- Key requirements and edge cases to consider: The number of teams `n` is a power of 2, and the input matches are valid (i.e., each match is played between two different teams, and each team plays at most one match).
- Example test cases with explanations:
  - Example 1: `findWinner(2, [[1, 2]])` returns `[1, 2]`.
  - Example 2: `findWinner(4, [[1, 2], [3, 4]])` returns `[1, 3]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the winner of the contest, we can simulate the entire tournament. We start by creating a list of all teams, and then for each match, we remove the loser from the list and add the winner to the next round.
- Step-by-step breakdown of the solution:
  1. Create a list of all teams.
  2. For each match, remove the loser from the list and add the winner to the next round.
  3. Repeat step 2 until only one team remains.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, as it simulates the actual process of a tournament.

```cpp
vector<int> findWinner(int n, vector<vector<int>>& matches) {
    vector<int> teams(n);
    for (int i = 0; i < n; i++) {
        teams[i] = i + 1;
    }
    for (auto& match : matches) {
        int winner = match[0];
        int loser = match[1];
        // Remove the loser from the list of teams
        teams.erase(remove(teams.begin(), teams.end(), loser), teams.end());
    }
    // The last team remaining is the winner
    return teams;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of teams. The reason is that in the worst case, we might have to remove a team from the list in each iteration, which takes $O(n)$ time.
> - **Space Complexity:** $O(n)$, where $n$ is the number of teams. We need to store the list of teams.
> - **Why these complexities occur:** The brute force approach is not efficient because it involves removing elements from a list, which can be expensive. Additionally, it does not take advantage of the fact that the number of teams is a power of 2.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is that the winner of the contest is the team that wins all its matches. Since the number of teams is a power of 2, we can use a recursive approach to find the winner.
- Detailed breakdown of the approach:
  1. Create a recursive function that takes a list of teams and a list of matches as input.
  2. In each recursive call, simulate the matches and remove the losers from the list of teams.
  3. Repeat step 2 until only one team remains.
- Proof of optimality: The optimal approach is efficient because it uses a recursive approach, which reduces the time complexity to $O(n \log n)$.

```cpp
vector<int> findWinner(int n, vector<vector<int>>& matches) {
    vector<int> teams(n);
    for (int i = 0; i < n; i++) {
        teams[i] = i + 1;
    }
    function<vector<int>(vector<int>, vector<vector<int>>)> recursiveFindWinner =
        [&](vector<int> teams, vector<vector<int>> matches) -> vector<int> {
            if (teams.size() == 1) {
                return teams;
            }
            vector<vector<int>> nextRoundMatches;
            vector<int> nextRoundTeams;
            for (auto& match : matches) {
                int winner = match[0];
                int loser = match[1];
                nextRoundTeams.push_back(winner);
                // Remove the loser from the list of teams
                teams.erase(remove(teams.begin(), teams.end(), loser), teams.end());
            }
            // Create the matches for the next round
            for (int i = 0; i < nextRoundTeams.size(); i += 2) {
                nextRoundMatches.push_back({nextRoundTeams[i], nextRoundTeams[i + 1]});
            }
            return recursiveFindWinner(nextRoundTeams, nextRoundMatches);
        };
    return recursiveFindWinner(teams, matches);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of teams. The reason is that we use a recursive approach, which reduces the number of teams by half in each recursive call.
> - **Space Complexity:** $O(n)$, where $n$ is the number of teams. We need to store the list of teams and the recursive call stack.
> - **Optimality proof:** The optimal approach is efficient because it uses a recursive approach, which reduces the time complexity to $O(n \log n)$. This is the best possible time complexity for this problem, as we need to simulate the matches and remove the losers from the list of teams.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive approach, simulation of matches, and removal of losers from the list of teams.
- Problem-solving patterns identified: Using a recursive approach to solve a problem that can be divided into smaller sub-problems.
- Optimization techniques learned: Reducing the time complexity by using a recursive approach.
- Similar problems to practice: Other problems that involve simulating a process and removing elements from a list.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the base case of the recursion correctly, not removing the losers from the list of teams correctly.
- Edge cases to watch for: The number of teams is a power of 2, and the input matches are valid.
- Performance pitfalls: Using an inefficient approach that has a high time complexity.
- Testing considerations: Testing the function with different inputs and edge cases to ensure that it works correctly.