## Min Cost Climbing Stairs

**Problem Link:** https://leetcode.com/problems/min-cost-climbing-stairs/description

**Problem Statement:**
- Input format and constraints: You are given an integer array `cost` where `cost[i]` is the cost of the `i`-th step on a staircase. You are allowed to climb either one or two steps at a time.
- Expected output format: The function should return the minimum cost to reach the top of the staircase.
- Key requirements and edge cases to consider: The length of the `cost` array will be in the range `[2, 1000]`. Every `cost[i]` will be an integer in the range `[1, 999]`.
- Example test cases with explanations:
  - For the input `cost = [10, 15, 20]`, the output should be `15`. This is because you can climb from the first step to the second step, and then directly to the top.
  - For the input `cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]`, the output should be `6`. This is because you can climb from the first step to the second step, then to the third step, and so on, avoiding the expensive steps.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to solve this problem is to try all possible combinations of steps and calculate the total cost for each combination.
- Step-by-step breakdown of the solution:
  1. Start from the first step.
  2. For each step, try climbing one step or two steps.
  3. Recursively calculate the minimum cost to reach the top from the current step.
  4. Return the minimum cost among all possible combinations.

```cpp
int minCostClimbingStairs(vector<int>& cost) {
    int n = cost.size();
    return minCostClimbingStairsHelper(cost, n - 1);
}

int minCostClimbingStairsHelper(vector<int>& cost, int i) {
    if (i < 0) {
        return 0;
    }
    if (i == 0 || i == 1) {
        return cost[i];
    }
    return cost[i] + min(minCostClimbingStairsHelper(cost, i - 1), minCostClimbingStairsHelper(cost, i - 2));
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the number of steps. This is because we are trying all possible combinations of steps, resulting in exponential time complexity.
> - **Space Complexity:** $O(n)$, where $n$ is the number of steps. This is because we need to store the recursive call stack.
> - **Why these complexities occur:** The brute force approach tries all possible combinations of steps, resulting in exponential time complexity. The recursive call stack requires linear space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to store the minimum cost to reach each step, avoiding redundant calculations.
- Detailed breakdown of the approach:
  1. Create a dynamic programming array `dp` of size `n + 1`, where `dp[i]` represents the minimum cost to reach the `i`-th step.
  2. Initialize `dp[0] = dp[1] = 0`, since we can start from either the first or second step.
  3. For each step `i` from `2` to `n`, calculate `dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]`.
  4. Return `min(dp[n - 1], dp[n - 2])`, since we can reach the top from either the second last or last step.

```cpp
int minCostClimbingStairs(vector<int>& cost) {
    int n = cost.size();
    vector<int> dp(n + 1, 0);
    dp[0] = dp[1] = 0;
    for (int i = 2; i <= n; i++) {
        dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i - 1];
    }
    return min(dp[n], dp[n - 1]);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of steps. This is because we are calculating the minimum cost to reach each step in linear time.
> - **Space Complexity:** $O(n)$, where $n$ is the number of steps. This is because we need to store the dynamic programming array.
> - **Optimality proof:** The dynamic programming approach ensures that we are calculating the minimum cost to reach each step, avoiding redundant calculations. This results in linear time complexity, making it the optimal solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, memoization.
- Problem-solving patterns identified: Avoiding redundant calculations using dynamic programming.
- Optimization techniques learned: Using dynamic programming to reduce time complexity.
- Similar problems to practice: Other dynamic programming problems, such as Fibonacci sequence, Longest Common Subsequence.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the dynamic programming array correctly, not handling edge cases properly.
- Edge cases to watch for: Handling the base cases correctly, such as when `n` is `1` or `2`.
- Performance pitfalls: Not using dynamic programming, resulting in exponential time complexity.
- Testing considerations: Testing the solution with different inputs, including edge cases and large inputs.