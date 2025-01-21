## Design a Leaderboard

**Problem Link:** https://leetcode.com/problems/design-a-leaderboard/description

**Problem Statement:**
- Input format and constraints: The problem involves designing a leaderboard that supports `addScore`, `top`, and `reset` operations. The `addScore` operation adds a score for a given player, the `top` operation returns the top K scores, and the `reset` operation resets the score of a player to 0.
- Expected output format: The `top` operation should return the sum of the top K scores.
- Key requirements and edge cases to consider: The leaderboard should handle multiple players, and the `top` operation should return the correct sum of the top K scores.
- Example test cases with explanations:
  - Example 1: 
    - Input: `["Leaderboard","addScore","addScore","top","reset","top"]`
    - Output: `[null,null,null,8,null,5]`
    - Explanation: 
      - `addScore(1, 73)`: Player 1 has a score of 73.
      - `addScore(2, 68)`: Player 2 has a score of 68.
      - `top(1)`: The top 1 score is 73, so the sum of the top 1 score is 73.
      - `reset(1)`: Player 1's score is reset to 0.
      - `top(2)`: The top 2 scores are 68 and 0, so the sum of the top 2 scores is 68.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves using a `map` to store the scores of each player and a `vector` to store all the scores. When the `addScore` operation is called, the score is added to the player's current score in the `map`. When the `top` operation is called, all the scores are sorted in descending order, and the sum of the top K scores is calculated. When the `reset` operation is called, the player's score is reset to 0 in the `map`.
- Step-by-step breakdown of the solution:
  1. Create a `map` to store the scores of each player.
  2. Create a `vector` to store all the scores.
  3. Implement the `addScore` operation by adding the score to the player's current score in the `map` and updating the `vector` of scores.
  4. Implement the `top` operation by sorting the `vector` of scores in descending order and calculating the sum of the top K scores.
  5. Implement the `reset` operation by resetting the player's score to 0 in the `map` and updating the `vector` of scores.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it has a high time complexity due to the sorting operation.

```cpp
class Leaderboard {
public:
    map<int, int> scores;
    vector<int> allScores;

    Leaderboard() {}

    void addScore(int playerId, int score) {
        if (scores.find(playerId) != scores.end()) {
            allScores.push_back(-scores[playerId]); // remove old score
            scores[playerId] += score;
        } else {
            scores[playerId] = score;
        }
        allScores.push_back(scores[playerId]);
    }

    int top(int K) {
        sort(allScores.rbegin(), allScores.rend());
        int sum = 0;
        for (int i = 0; i < K; i++) {
            sum += allScores[i];
        }
        return sum;
    }

    void reset(int playerId) {
        allScores.push_back(-scores[playerId]); // remove old score
        scores[playerId] = 0;
        allScores.push_back(scores[playerId]);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \log N)$, where $N$ is the number of scores. The `top` operation has a time complexity of $O(N \log N)$ due to the sorting operation.
> - **Space Complexity:** $O(N)$, where $N$ is the number of scores. The `vector` of scores has a space complexity of $O(N)$.
> - **Why these complexities occur:** The brute force approach has a high time complexity due to the sorting operation, which is necessary to calculate the sum of the top K scores.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal approach involves using a `map` to store the scores of each player and a `multiset` to store all the scores. The `multiset` is a data structure that automatically sorts the scores in descending order, allowing for efficient calculation of the sum of the top K scores.
- Detailed breakdown of the approach:
  1. Create a `map` to store the scores of each player.
  2. Create a `multiset` to store all the scores.
  3. Implement the `addScore` operation by adding the score to the player's current score in the `map` and updating the `multiset` of scores.
  4. Implement the `top` operation by calculating the sum of the top K scores using the `multiset`.
  5. Implement the `reset` operation by resetting the player's score to 0 in the `map` and updating the `multiset` of scores.
- Why further optimization is impossible: The optimal approach has a time complexity of $O(\log N)$ for the `addScore` and `reset` operations, and a time complexity of $O(K)$ for the `top` operation. This is the best possible time complexity for this problem.

```cpp
class Leaderboard {
public:
    map<int, int> scores;
    multiset<int> allScores;

    Leaderboard() {}

    void addScore(int playerId, int score) {
        if (scores.find(playerId) != scores.end()) {
            allScores.erase(allScores.find(scores[playerId])); // remove old score
        }
        scores[playerId] += score;
        allScores.insert(scores[playerId]);
    }

    int top(int K) {
        int sum = 0;
        for (auto it = allScores.rbegin(); it != allScores.rend() && K > 0; it++, K--) {
            sum += *it;
        }
        return sum;
    }

    void reset(int playerId) {
        allScores.erase(allScores.find(scores[playerId])); // remove old score
        scores[playerId] = 0;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** 
>   - `addScore`: $O(\log N)$, where $N$ is the number of scores.
>   - `top`: $O(K)$, where $K$ is the number of top scores to return.
>   - `reset`: $O(\log N)$, where $N$ is the number of scores.
> - **Space Complexity:** $O(N)$, where $N$ is the number of scores.
> - **Optimality proof:** The optimal approach has the best possible time complexity for this problem, as it uses a `multiset` to store the scores, which allows for efficient calculation of the sum of the top K scores.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The use of a `multiset` to store scores and calculate the sum of the top K scores.
- Problem-solving patterns identified: The use of a `map` to store the scores of each player and a `multiset` to store all the scores.
- Optimization techniques learned: The use of a `multiset` to reduce the time complexity of the `top` operation.
- Similar problems to practice: Problems that involve calculating the sum of the top K scores, such as the "Top K Frequent Elements" problem.

**Mistakes to Avoid:**
- Common implementation errors: Failing to update the `multiset` of scores when adding or resetting a score.
- Edge cases to watch for: Handling the case where a player has a score of 0.
- Performance pitfalls: Using a sorting algorithm with a high time complexity, such as the brute force approach.
- Testing considerations: Testing the `addScore`, `top`, and `reset` operations with different inputs and edge cases.