## Card Flipping Game

**Problem Link:** https://leetcode.com/problems/card-flipping-game/description

**Problem Statement:**
- Input format: You are given an array of integers `fronts` and `backs` representing the front and back of each card in the game.
- Constraints: The length of `fronts` and `backs` will be the same, and each integer will be between 1 and 2000 (inclusive).
- Expected output format: Return the maximum score that can be achieved in the game.
- Key requirements and edge cases to consider: The score is calculated based on the difference between the number of cards with the same number on both sides and the number of cards with different numbers on both sides.
- Example test cases with explanations:
  - Input: `fronts = [1,2,4,4,7], backs = [1,3,4,1,3]`
  - Output: `4`
  - Explanation: The cards with the same number on both sides are `[1, 4]`, and the cards with different numbers on both sides are `[2, 7]`. The score is `2 - 2 = 0`, but since the game allows us to flip one card, we can flip the card with number `7` to get a score of `3 - 1 = 2`. However, we can also flip the card with number `4` to get a score of `4 - 0 = 4`, which is the maximum score.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves checking all possible combinations of flipping cards to find the maximum score.
- Step-by-step breakdown of the solution:
  1. Initialize the maximum score to 0.
  2. Generate all possible combinations of flipping cards.
  3. For each combination, calculate the score based on the difference between the number of cards with the same number on both sides and the number of cards with different numbers on both sides.
  4. Update the maximum score if the current score is higher.
- Why this approach comes to mind first: The brute force approach is often the first solution that comes to mind because it involves checking all possible scenarios, which guarantees finding the optimal solution.

```cpp
#include <vector>
#include <algorithm>

int flipgame(std::vector<int>& fronts, std::vector<int>& backs) {
    int maxScore = 0;
    for (int i = 0; i < fronts.size(); i++) {
        std::vector<int> same, different;
        for (int j = 0; j < fronts.size(); j++) {
            if (fronts[j] == backs[j]) {
                same.push_back(fronts[j]);
            } else {
                different.push_back(fronts[j]);
                different.push_back(backs[j]);
            }
        }
        int score = 0;
        if (std::find(same.begin(), same.end(), fronts[i]) != same.end() || std::find(same.begin(), same.end(), backs[i]) != same.end()) {
            score = 0;
        } else {
            score = 2000;
            for (int j = 0; j < different.size(); j++) {
                if (different[j] == fronts[i] || different[j] == backs[i]) {
                    score = std::min(score, different[j]);
                }
            }
        }
        maxScore = std::max(maxScore, score);
    }
    return maxScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of cards. This is because we are generating all possible combinations of flipping cards, which takes $O(n)$ time, and then calculating the score for each combination, which takes $O(n)$ time.
> - **Space Complexity:** $O(n)$, where $n$ is the number of cards. This is because we are storing the same and different numbers in separate vectors, which takes $O(n)$ space.
> - **Why these complexities occur:** The time complexity occurs because we are using nested loops to generate all possible combinations of flipping cards and calculate the score. The space complexity occurs because we are storing the same and different numbers in separate vectors.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves finding the maximum score that can be achieved by flipping one card.
- Detailed breakdown of the approach:
  1. Initialize the maximum score to 0.
  2. Iterate over each card and check if flipping it would result in a higher score.
  3. If flipping the card would result in a higher score, update the maximum score.
- Proof of optimality: The optimal solution is optimal because it involves checking all possible scenarios of flipping one card, which guarantees finding the maximum score.
- Why further optimization is impossible: Further optimization is impossible because we are already checking all possible scenarios of flipping one card, which is the minimum number of flips required to achieve the maximum score.

```cpp
#include <vector>
#include <algorithm>

int flipgame(std::vector<int>& fronts, std::vector<int>& backs) {
    std::vector<int> same;
    for (int i = 0; i < fronts.size(); i++) {
        if (fronts[i] == backs[i]) {
            same.push_back(fronts[i]);
        }
    }
    int maxScore = 0;
    for (int i = 0; i < fronts.size(); i++) {
        if (std::find(same.begin(), same.end(), fronts[i]) != same.end() || std::find(same.begin(), same.end(), backs[i]) != same.end()) {
            continue;
        }
        maxScore = std::max(maxScore, std::min(fronts[i], backs[i]));
    }
    return maxScore == 0 ? 0 : maxScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of cards. This is because we are iterating over each card once to find the same numbers and once to find the maximum score.
> - **Space Complexity:** $O(n)$, where $n$ is the number of cards. This is because we are storing the same numbers in a separate vector.
> - **Optimality proof:** The optimal solution is optimal because it involves checking all possible scenarios of flipping one card, which guarantees finding the maximum score.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the concept of finding the maximum score that can be achieved by flipping one card.
- Problem-solving patterns identified: The problem-solving pattern involves finding the maximum score by iterating over each card and checking if flipping it would result in a higher score.
- Optimization techniques learned: The optimization technique involves checking all possible scenarios of flipping one card to find the maximum score.
- Similar problems to practice: Similar problems to practice include finding the maximum score that can be achieved by flipping multiple cards.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is not checking if flipping a card would result in a higher score.
- Edge cases to watch for: An edge case to watch for is when there are no cards that can be flipped to achieve a higher score.
- Performance pitfalls: A performance pitfall is not using an efficient algorithm to find the maximum score.
- Testing considerations: A testing consideration is to test the algorithm with different inputs to ensure it works correctly.