## Solving Questions with Brainpower
**Problem Link:** https://leetcode.com/problems/solving-questions-with-brainpower/description

**Problem Statement:**
- Input format and constraints: Given a 2D array `questions` where `questions[i] = [points_i, brainpower_i]`.
- Expected output format: The maximum points that can be obtained.
- Key requirements and edge cases to consider: 
  - Each question must be answered in the order they appear in the array.
  - Each question can be answered either by using the brainpower to solve it or by not answering it.
  - If the question is answered, the points for the question are awarded.
  - If the question is not answered, no points are awarded.
- Example test cases with explanations:
  - `questions = [[3,2],[4,3],[4,4],[6,5]]`: The maximum points that can be obtained is 5.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of answering or not answering each question.
- Step-by-step breakdown of the solution:
  1. Initialize a variable to store the maximum points.
  2. Iterate over all possible combinations of answering or not answering each question.
  3. For each combination, calculate the total points.
  4. Update the maximum points if the total points for the current combination are higher.
- Why this approach comes to mind first: It's a straightforward way to solve the problem by trying all possible solutions.

```cpp
class Solution {
public:
    int mostPoints(vector<vector<int>>& questions) {
        int n = questions.size();
        int maxPoints = 0;
        for (int mask = 0; mask < (1 << n); mask++) {
            int points = 0;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    points += questions[i][0];
                }
            }
            maxPoints = max(maxPoints, points);
        }
        return maxPoints;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the number of questions. This is because we're trying all possible combinations of answering or not answering each question.
> - **Space Complexity:** $O(1)$, because we're only using a constant amount of space to store the maximum points.
> - **Why these complexities occur:** The brute force approach tries all possible combinations, resulting in exponential time complexity. The space complexity is constant because we're only using a fixed amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: This problem can be solved using dynamic programming.
- Detailed breakdown of the approach:
  1. Initialize a dynamic programming table `dp` where `dp[i]` represents the maximum points that can be obtained up to the `i-th` question.
  2. Iterate over each question.
  3. For each question, calculate the maximum points that can be obtained by either answering or not answering the question.
  4. Update the dynamic programming table with the maximum points.
- Proof of optimality: The dynamic programming approach ensures that we're considering all possible combinations of answering or not answering each question, and it does so in a way that avoids redundant calculations.

```cpp
class Solution {
public:
    int mostPoints(vector<vector<int>>& questions) {
        int n = questions.size();
        vector<int> dp(n + 1, 0);
        for (int i = 1; i <= n; i++) {
            dp[i] = max(dp[i - 1], dp[max(0, i - questions[i - 1][1] - 1)] + questions[i - 1][0]);
        }
        return dp[n];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of questions. This is because we're iterating over each question once.
> - **Space Complexity:** $O(n)$, because we're using a dynamic programming table of size $n + 1$.
> - **Optimality proof:** The dynamic programming approach ensures that we're considering all possible combinations of answering or not answering each question in a way that avoids redundant calculations, resulting in linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming.
- Problem-solving patterns identified: The problem can be broken down into smaller sub-problems, and the solutions to these sub-problems can be combined to solve the larger problem.
- Optimization techniques learned: Dynamic programming can be used to avoid redundant calculations and improve the efficiency of the solution.
- Similar problems to practice: Other dynamic programming problems, such as the `0/1 Knapsack Problem` or `Longest Common Subsequence`.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the dynamic programming table correctly, or not updating the table correctly.
- Edge cases to watch for: The case where the input array is empty, or the case where the input array contains only one question.
- Performance pitfalls: Using a brute force approach, which can result in exponential time complexity.
- Testing considerations: Testing the solution with different input arrays, including edge cases, to ensure that it's working correctly.