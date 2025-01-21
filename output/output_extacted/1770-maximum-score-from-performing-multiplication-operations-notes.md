## Maximum Score from Performing Multiplication Operations

**Problem Link:** https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/description

**Problem Statement:**
- Input: An array of integers `nums` and an integer `k`.
- Constraints: `1 <= k <= 10`, `1 <= nums.length <= 1000`.
- Expected output: The maximum score that can be obtained from performing `k` multiplication operations.
- Key requirements: Find the optimal way to choose numbers from `nums` to maximize the score after `k` multiplications.

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible combinations of numbers from `nums` for each multiplication operation.
- For each combination, calculate the score and keep track of the maximum score found.
- This approach comes to mind first because it exhaustively explores all possibilities, ensuring the optimal solution is found.

```cpp
class Solution {
public:
    int maximumScore(vector<int>& nums, int k) {
        int maxScore = 0;
        int n = nums.size();
        vector<bool> visited(n, false);
        function<void(int, int, int)> dfs = [&](int step, int score, int pos) {
            if (step == k) {
                maxScore = max(maxScore, score);
                return;
            }
            for (int i = 0; i < n; ++i) {
                if (!visited[i]) {
                    visited[i] = true;
                    dfs(step + 1, score * nums[i], i);
                    visited[i] = false;
                }
            }
        };
        dfs(0, 1, 0);
        return maxScore;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^k)$, where $n$ is the size of `nums`. This is because for each of the $k$ steps, we potentially try all $n$ numbers.
> - **Space Complexity:** $O(k)$, due to the recursion stack.
> - **Why these complexities occur:** The brute force approach tries all combinations of numbers for each step, leading to exponential time complexity. The space complexity is linear with respect to the recursion depth, which is $k$.

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use dynamic programming to store and reuse the results of subproblems.
- We use a 2D DP table `dp` where `dp[i][j]` represents the maximum score that can be obtained after performing `i` multiplications and considering the first `j` numbers in `nums`.
- We fill up the DP table in a bottom-up manner and finally return `dp[k][n]`.

```cpp
class Solution {
public:
    int maximumScore(vector<int>& nums, int k) {
        int n = nums.size();
        vector<vector<int>> dp(k + 1, vector<int>(n + 1, 0));
        for (int i = 1; i <= k; ++i) {
            for (int j = i; j <= n; ++j) {
                int maxScore = 0;
                for (int l = i - 1; l < j; ++l) {
                    maxScore = max(maxScore, dp[i - 1][l] * nums[l]);
                }
                dp[i][j] = max(dp[i][j - 1], maxScore);
            }
        }
        return dp[k][n];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(nk^2)$, where $n$ is the size of `nums`. This is because we have three nested loops, with the outer two loops running in $O(nk)$ and the innermost loop running in $O(k)$.
> - **Space Complexity:** $O(nk)$, for the DP table.
> - **Optimality proof:** This approach is optimal because it avoids redundant calculations by storing and reusing the results of subproblems. The time complexity is significantly improved compared to the brute force approach.

---

### Final Notes

**Learning Points:**
- The importance of dynamic programming in solving problems with overlapping subproblems.
- How to apply dynamic programming to avoid redundant calculations and improve time complexity.
- The trade-off between time and space complexity in using a DP table.

**Mistakes to Avoid:**
- Failing to consider the base cases and boundary conditions in the DP approach.
- Not properly initializing the DP table, leading to incorrect results.
- Overlooking the possibility of using dynamic programming to solve the problem.