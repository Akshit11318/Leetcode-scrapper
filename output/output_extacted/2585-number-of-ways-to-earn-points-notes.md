## Number of Ways to Earn Points

**Problem Link:** https://leetcode.com/problems/number-of-ways-to-earn-points/description

**Problem Statement:**
- Input: `tasks` - a 2D array where each task is represented as an array of two integers `[points, duration]`.
- Constraints: `1 <= tasks.length <= 10^5`, `1 <= points[i] <= 10^5`, `1 <= duration[i] <= 10^5`.
- Expected output: The number of ways to earn `k` points, where `k` is given as input.
- Key requirements: Count the number of ways to select tasks such that the total points earned equals `k`.
- Example test cases:
  - `tasks = [[1,1],[2,2],[3,3]]`, `k = 4`, output: `4` (Selecting tasks [1,1], [2,2], [1,1] and [2,2] gives 4 points).
  - `tasks = [[1,1],[2,2],[3,3]]`, `k = 6`, output: `7` (There are 7 ways to earn 6 points).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subsets of tasks and calculate the total points for each subset.
- Step-by-step breakdown:
  1. Initialize a variable to store the count of ways to earn `k` points.
  2. Generate all possible subsets of tasks using recursion or bit manipulation.
  3. For each subset, calculate the total points earned.
  4. If the total points equal `k`, increment the count.
- Why this approach comes to mind first: It is a straightforward approach to generate all possible combinations and check if they meet the condition.

```cpp
int countWays(vector<vector<int>>& tasks, int k) {
    int n = tasks.size();
    int count = 0;
    for (int mask = 0; mask < (1 << n); mask++) {
        int points = 0;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                points += tasks[i][0];
            }
        }
        if (points == k) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of tasks. This is because we generate all possible subsets (2^n) and for each subset, we iterate over all tasks to calculate the total points.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the count and the current subset.
> - **Why these complexities occur:** The time complexity is high because we generate all possible subsets, which has an exponential time complexity. The space complexity is low because we only use a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use dynamic programming to store the number of ways to earn `i` points using the first `j` tasks.
- Detailed breakdown:
  1. Initialize a 2D array `dp` of size `(k+1) x (n+1)`, where `dp[i][j]` represents the number of ways to earn `i` points using the first `j` tasks.
  2. Initialize the base case: `dp[0][0] = 1`, as there is one way to earn 0 points (by not selecting any tasks).
  3. Iterate over each task and update the `dp` array accordingly.
- Proof of optimality: This approach has a polynomial time complexity, which is much better than the exponential time complexity of the brute force approach.

```cpp
int countWays(vector<vector<int>>& tasks, int k) {
    int n = tasks.size();
    vector<vector<int>> dp(k+1, vector<int>(n+1, 0));
    dp[0][0] = 1;
    for (int j = 1; j <= n; j++) {
        for (int i = 0; i <= k; i++) {
            dp[i][j] = dp[i][j-1];
            if (i >= tasks[j-1][0]) {
                dp[i][j] += dp[i-tasks[j-1][0]][j-1];
            }
        }
    }
    return dp[k][n];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k \cdot n)$, where $k$ is the target points and $n$ is the number of tasks.
> - **Space Complexity:** $O(k \cdot n)$, as we use a 2D array to store the `dp` values.
> - **Optimality proof:** This approach has a polynomial time complexity, which is much better than the exponential time complexity of the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Dynamic programming, bit manipulation.
- Problem-solving patterns: Using dynamic programming to store intermediate results and avoid redundant calculations.
- Optimization techniques: Using a 2D array to store the `dp` values and iterating over each task to update the `dp` array.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the base case correctly, not updating the `dp` array correctly.
- Edge cases to watch for: Handling cases where `k` is 0 or `n` is 0.
- Performance pitfalls: Using an exponential time complexity approach, not using dynamic programming to store intermediate results.