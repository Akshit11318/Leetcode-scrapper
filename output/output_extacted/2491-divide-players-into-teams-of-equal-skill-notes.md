## Divide Players into Teams of Equal Skill

**Problem Link:** https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/description

**Problem Statement:**
- Input format and constraints: The input is a 2D vector `scores` where each element is a vector of two integers representing the scores of two players. The constraint is that the number of players is even.
- Expected output format: The output is the total score of all teams, which is the sum of the products of the scores of the players in each team.
- Key requirements and edge cases to consider: The teams must have equal skill, meaning that the sum of the scores of the players in each team must be the same.
- Example test cases with explanations: For example, if the input is `[[4,5],[4,6],[6,5]]`, the output is `60` because the teams are `(4, 6)` and `(5, 5)`, and the total score is `(4 * 6) + (5 * 5) = 24 + 36 = 60`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to generate all possible pairs of players and calculate the sum of the scores of each pair. Then, we can check if the sums of the scores of all pairs are equal.
- Step-by-step breakdown of the solution:
  1. Generate all possible pairs of players.
  2. Calculate the sum of the scores of each pair.
  3. Check if the sums of the scores of all pairs are equal.
  4. If the sums are equal, calculate the total score of all teams.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient because it has a high time complexity.

```cpp
#include <vector>
#include <algorithm>

int dividePlayers(std::vector<std::vector<int>>& scores) {
    int n = scores.size();
    int totalScore = 0;
    std::vector<int> sums(n);
    
    // Calculate the sum of the scores of each pair
    for (int i = 0; i < n; i++) {
        sums[i] = scores[i][0] + scores[i][1];
    }
    
    // Check if the sums of the scores of all pairs are equal
    std::sort(sums.begin(), sums.end());
    for (int i = 1; i < n; i++) {
        if (sums[i] != sums[i - 1]) {
            return -1;
        }
    }
    
    // Calculate the total score of all teams
    for (int i = 0; i < n; i++) {
        totalScore += scores[i][0] * scores[i][1];
    }
    
    return totalScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of pairs of players. This is because we are generating all possible pairs of players and calculating the sum of the scores of each pair.
> - **Space Complexity:** $O(n)$, where $n$ is the number of pairs of players. This is because we are storing the sums of the scores of all pairs in a vector.
> - **Why these complexities occur:** These complexities occur because we are using a brute force approach that generates all possible pairs of players and calculates the sum of the scores of each pair.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is that the sum of the scores of all players must be even, because the number of players is even. Therefore, we can calculate the target sum of the scores of each team by dividing the total sum of the scores of all players by the number of teams.
- Detailed breakdown of the approach:
  1. Calculate the total sum of the scores of all players.
  2. Calculate the target sum of the scores of each team by dividing the total sum by the number of teams.
  3. Use a hashmap to store the frequency of each score.
  4. Iterate over the hashmap and for each score, check if its complement (i.e., the target sum minus the score) is in the hashmap. If it is, calculate the product of the score and its complement and add it to the total score.
- Proof of optimality: This approach is optimal because it has a time complexity of $O(n)$, which is the best possible time complexity for this problem.

```cpp
#include <vector>
#include <unordered_map>

int dividePlayers(std::vector<std::vector<int>>& scores) {
    int n = scores.size();
    int totalScore = 0;
    std::unordered_map<int, int> freq;
    
    // Calculate the total sum of the scores of all players
    int totalSum = 0;
    for (int i = 0; i < n; i++) {
        totalSum += scores[i][0] + scores[i][1];
    }
    
    // Calculate the target sum of the scores of each team
    int targetSum = totalSum / (n / 2);
    
    // Use a hashmap to store the frequency of each score
    for (int i = 0; i < n; i++) {
        freq[scores[i][0]]++;
        freq[scores[i][1]]++;
    }
    
    // Iterate over the hashmap and calculate the total score
    for (auto& pair : freq) {
        int score = pair.first;
        int complement = targetSum - score;
        if (freq.find(complement) != freq.end()) {
            int count = std::min(pair.second, freq[complement]);
            totalScore += count * score * complement;
            pair.second -= count;
            freq[complement] -= count;
        }
    }
    
    return totalScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of pairs of players. This is because we are iterating over the hashmap and calculating the total score.
> - **Space Complexity:** $O(n)$, where $n$ is the number of pairs of players. This is because we are storing the frequency of each score in a hashmap.
> - **Optimality proof:** This approach is optimal because it has a time complexity of $O(n)$, which is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of hashmaps and the concept of complementary scores.
- Problem-solving patterns identified: The problem requires the use of a hashmap to store the frequency of each score and the calculation of the total score by iterating over the hashmap.
- Optimization techniques learned: The problem requires the use of a target sum to calculate the total score and the use of a hashmap to store the frequency of each score.
- Similar problems to practice: Similar problems to practice include problems that require the use of hashmaps and the calculation of total scores.

**Mistakes to Avoid:**
- Common implementation errors: Common implementation errors include not checking if the sum of the scores of all players is even and not using a hashmap to store the frequency of each score.
- Edge cases to watch for: Edge cases to watch for include cases where the number of players is odd and cases where the sum of the scores of all players is not even.
- Performance pitfalls: Performance pitfalls include using a brute force approach that generates all possible pairs of players and calculates the sum of the scores of each pair.
- Testing considerations: Testing considerations include testing the function with different inputs and edge cases to ensure that it works correctly.