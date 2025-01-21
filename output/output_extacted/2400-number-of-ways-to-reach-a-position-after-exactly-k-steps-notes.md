## Number of Ways to Reach a Position After Exactly K Steps

**Problem Link:** https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/description

**Problem Statement:**
- Input format: `int target, int k`
- Constraints: `1 <= target <= 10^9`, `1 <= k <= 10^9`
- Expected output format: The number of ways to reach the target position after exactly `k` steps.
- Key requirements: Calculate the number of ways to reach the target position after exactly `k` steps, where at each step, you can either move to the right or to the left.
- Example test cases:
  - `target = 2, k = 3`, the output should be `1`.
  - `target = 5, k = 10`, the output should be `0`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of moving to the right or to the left.
- Step-by-step breakdown:
  1. Initialize a counter for the number of ways to reach the target position.
  2. Use a recursive function to try all possible combinations of moving to the right or to the left.
  3. If the current position is equal to the target position and the number of steps is equal to `k`, increment the counter.
- Why this approach comes to mind first: It is a straightforward and intuitive solution.

```cpp
class Solution {
public:
    int numberOfWays(int target, int k) {
        int count = 0;
        dfs(0, 0, target, k, count);
        return count;
    }
    
    void dfs(int pos, int steps, int target, int k, int& count) {
        if (pos == target && steps == k) {
            count++;
            return;
        }
        if (steps >= k) {
            return;
        }
        dfs(pos + 1, steps + 1, target, k, count);
        if (pos > 0) {
            dfs(pos - 1, steps + 1, target, k, count);
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^k)$, where `k` is the number of steps. This is because we try all possible combinations of moving to the right or to the left.
> - **Space Complexity:** $O(k)$, where `k` is the number of steps. This is because of the recursive call stack.
> - **Why these complexities occur:** The recursive function tries all possible combinations of moving to the right or to the left, resulting in an exponential time complexity. The recursive call stack also results in a linear space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The problem can be solved using dynamic programming. We can use a 2D array `dp` where `dp[i][j]` represents the number of ways to reach position `j` after `i` steps.
- Detailed breakdown:
  1. Initialize a 2D array `dp` with dimensions `(k + 1) x (target + 1)`.
  2. Set `dp[0][0] = 1`, because there is one way to reach position 0 after 0 steps (i.e., do nothing).
  3. For each step `i` from 1 to `k`, for each position `j` from 1 to `target`, calculate `dp[i][j]` as the sum of `dp[i - 1][j - 1]` and `dp[i - 1][j + 1]`.
  4. Return `dp[k][target]`.
- Proof of optimality: The dynamic programming approach ensures that we only calculate each state once, resulting in a polynomial time complexity.

```cpp
class Solution {
public:
    int numberOfWays(int target, int k) {
        vector<vector<int>> dp(k + 1, vector<int>(target + 1));
        dp[0][0] = 1;
        for (int i = 1; i <= k; i++) {
            for (int j = 0; j <= target; j++) {
                if (j > 0) {
                    dp[i][j] += dp[i - 1][j - 1];
                }
                if (j < target) {
                    dp[i][j] += dp[i - 1][j + 1];
                }
            }
        }
        return dp[k][target];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(k \cdot target)$, where `k` is the number of steps and `target` is the target position. This is because we fill up a 2D array of dimensions `(k + 1) x (target + 1)`.
> - **Space Complexity:** $O(k \cdot target)$, where `k` is the number of steps and `target` is the target position. This is because we use a 2D array of dimensions `(k + 1) x (target + 1)`.
> - **Optimality proof:** The dynamic programming approach ensures that we only calculate each state once, resulting in a polynomial time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Dynamic programming, recursive functions.
- Problem-solving patterns: Breaking down a problem into smaller sub-problems, using memoization to avoid redundant calculations.
- Optimization techniques: Using dynamic programming to reduce the time complexity from exponential to polynomial.
- Similar problems to practice: Other dynamic programming problems, such as the Fibonacci sequence or the longest common subsequence.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect indexing, incorrect boundary conditions.
- Edge cases to watch for: `target` is 0, `k` is 0.
- Performance pitfalls: Using a recursive function without memoization, resulting in an exponential time complexity.
- Testing considerations: Test the function with different inputs, including edge cases.