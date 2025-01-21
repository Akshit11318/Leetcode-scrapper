## Stone Game VIII
**Problem Link:** https://leetcode.com/problems/stone-game-viii/description

**Problem Statement:**
- Input format: An array of integers `stones` representing the stones and their values.
- Constraints: `1 <= stones.length <= 10^5`, `1 <= stones[i] <= 10^4`.
- Expected output format: The maximum score that can be obtained.
- Key requirements and edge cases to consider: The game ends when all stones are removed or the current player cannot remove stones. The score is calculated as the sum of the values of the removed stones.
- Example test cases with explanations: 
  - `stones = [1, 2, 3, 4, 5]`, the maximum score that can be obtained is `18`.
  - `stones = [1, 2, 3, 4, 100]`, the maximum score that can be obtained is `107`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of removing stones and calculate the score for each combination.
- Step-by-step breakdown of the solution:
  1. Initialize a variable to store the maximum score.
  2. Iterate over all possible combinations of removing stones.
  3. For each combination, calculate the score by summing the values of the removed stones.
  4. Update the maximum score if the current score is higher.
- Why this approach comes to mind first: It is a straightforward and intuitive approach to try all possible combinations and calculate the score for each combination.

```cpp
int stoneGameVIII(vector<int>& stones) {
    int n = stones.size();
    int maxScore = INT_MIN;
    for (int i = 0; i < (1 << n); i++) {
        int score = 0;
        for (int j = 0; j < n; j++) {
            if ((i & (1 << j)) != 0) {
                score += stones[j];
            }
        }
        maxScore = max(maxScore, score);
    }
    return maxScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of stones. This is because we are trying all possible combinations of removing stones, which is $2^n$, and for each combination, we are calculating the score, which takes $O(n)$ time.
> - **Space Complexity:** $O(1)$, as we are only using a constant amount of space to store the maximum score.
> - **Why these complexities occur:** The time complexity occurs because we are trying all possible combinations of removing stones, and for each combination, we are calculating the score. The space complexity occurs because we are only using a constant amount of space to store the maximum score.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using dynamic programming. We can calculate the maximum score that can be obtained by considering the stones one by one from left to right.
- Detailed breakdown of the approach:
  1. Initialize a variable to store the maximum score.
  2. Initialize an array to store the cumulative sum of the stone values.
  3. Iterate over the stones from left to right.
  4. For each stone, calculate the maximum score that can be obtained by considering the current stone and the previous stones.
  5. Update the maximum score if the current score is higher.
- Proof of optimality: The dynamic programming approach ensures that we consider all possible combinations of removing stones and calculate the score for each combination. This approach is optimal because it avoids the redundant calculations of the brute force approach.

```cpp
int stoneGameVIII(vector<int>& stones) {
    int n = stones.size();
    vector<int> suffixSum(n + 1, 0);
    for (int i = n - 1; i >= 0; i--) {
        suffixSum[i] = suffixSum[i + 1] + stones[i];
    }
    vector<int> dp(n + 1, INT_MIN);
    dp[0] = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = i - 1; j >= 0; j--) {
            dp[i] = max(dp[i], dp[j] + suffixSum[j]);
        }
    }
    return dp[n];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of stones. This is because we are iterating over the stones and calculating the maximum score for each stone.
> - **Space Complexity:** $O(n)$, as we are using an array to store the cumulative sum of the stone values and an array to store the dynamic programming state.
> - **Optimality proof:** The dynamic programming approach ensures that we consider all possible combinations of removing stones and calculate the score for each combination. This approach is optimal because it avoids the redundant calculations of the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, cumulative sum.
- Problem-solving patterns identified: The problem can be solved by considering the stones one by one from left to right and calculating the maximum score for each stone.
- Optimization techniques learned: Dynamic programming can be used to avoid redundant calculations and improve the time complexity.
- Similar problems to practice: Stone Game, Stone Game II, Stone Game III.

**Mistakes to Avoid:**
- Common implementation errors: Not considering all possible combinations of removing stones, not calculating the score correctly.
- Edge cases to watch for: The game ends when all stones are removed or the current player cannot remove stones.
- Performance pitfalls: The brute force approach has a high time complexity and should be avoided.
- Testing considerations: Test the solution with different inputs and edge cases to ensure correctness.