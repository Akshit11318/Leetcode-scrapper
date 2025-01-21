## Determine the Winner of a Bowling Game

**Problem Link:** https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/description

**Problem Statement:**
- Input: Two integer arrays `player1` and `player2`, where `player1[i]` and `player2[i]` represent the number of pins knocked down by the first and second player in the `i-th` frame, respectively.
- Constraints: Each player can knock down at most 10 pins per frame.
- Expected output: Return `1` if the first player will win, `2` if the second player will win, and `0` if the game will end in a draw.
- Key requirements and edge cases to consider:
  - A player can score a strike (10 points) by knocking down all 10 pins in a single roll.
  - A player can score a spare (10 points plus the number of pins knocked down in the next roll) by knocking down all 10 pins in two rolls.
  - If a player scores a strike or a spare in the last frame, they get to roll again to score extra points.
- Example test cases with explanations:
  - If `player1 = [4,6,2,5,0]` and `player2 = [3,5,3,2,4]`, the output should be `0` because both players have the same total score.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to calculate the total score for each player by iterating through each frame and adding up the points.
- The brute force approach involves calculating the score for each frame separately and then comparing the total scores of both players.
- This approach comes to mind first because it directly implements the rules of bowling without any optimization.

```cpp
int calculateScore(int* player, int playerSize) {
    int score = 0;
    for (int i = 0; i < playerSize; i++) {
        // Add points for the current frame
        score += player[i];
    }
    return score;
}

int determineWinner(int* player1, int player1Size, int* player2, int player2Size) {
    int score1 = calculateScore(player1, player1Size);
    int score2 = calculateScore(player2, player2Size);
    if (score1 > score2) return 1;
    else if (score1 < score2) return 2;
    else return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of frames played by each player. This is because we iterate through each frame once for each player.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the scores and other variables.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each frame, and the space complexity is constant because we do not use any data structures that grow with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves calculating the score for each player in a single pass through the frames, taking into account the rules of bowling for strikes and spares.
- We can keep track of the current score and the number of rolls remaining for each player.
- This approach is optimal because it only requires a single pass through the input and uses a constant amount of space.

```cpp
int determineWinner(int* player1, int player1Size, int* player2, int player2Size) {
    int score1 = 0, score2 = 0;
    int roll1 = 0, roll2 = 0;
    for (int i = 0; i < 10; i++) {
        // Calculate the score for the current frame
        if (player1[roll1] == 10) {
            // Strike
            score1 += 10 + player1[roll1 + 1] + player1[roll1 + 2];
            roll1++;
        } else if (player1[roll1] + player1[roll1 + 1] == 10) {
            // Spare
            score1 += 10 + player1[roll1 + 2];
            roll1 += 2;
        } else {
            // Normal frame
            score1 += player1[roll1] + player1[roll1 + 1];
            roll1 += 2;
        }
        
        if (player2[roll2] == 10) {
            // Strike
            score2 += 10 + player2[roll2 + 1] + player2[roll2 + 2];
            roll2++;
        } else if (player2[roll2] + player2[roll2 + 1] == 10) {
            // Spare
            score2 += 10 + player2[roll2 + 2];
            roll2 += 2;
        } else {
            // Normal frame
            score2 += player2[roll2] + player2[roll2 + 1];
            roll2 += 2;
        }
    }
    if (score1 > score2) return 1;
    else if (score1 < score2) return 2;
    else return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of frames played by each player. This is because we iterate through each frame once for each player.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the scores and other variables.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the input and uses a constant amount of space, which is the minimum possible time and space complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: iteration, conditional statements, and calculation of scores based on rules.
- Problem-solving patterns identified: breaking down the problem into smaller sub-problems (calculating the score for each frame) and combining the solutions.
- Optimization techniques learned: reducing the number of passes through the input and using a constant amount of space.
- Similar problems to practice: other sports-related problems, such as calculating the winner of a tennis match or a game of pool.

**Mistakes to Avoid:**
- Common implementation errors: off-by-one errors when indexing the input arrays, and not handling the case where a player scores a strike or spare in the last frame.
- Edge cases to watch for: the input arrays may not be the same length, and the scores may be equal.
- Performance pitfalls: using too much space or making too many passes through the input.
- Testing considerations: test the function with different input arrays, including edge cases, to ensure it produces the correct output.