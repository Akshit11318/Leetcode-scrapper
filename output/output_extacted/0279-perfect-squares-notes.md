## Perfect Squares

**Problem Link:** https://leetcode.com/problems/perfect-squares/description

**Problem Statement:**
- Input: An integer `n`
- Constraints: `1 <= n <= 10^4`
- Expected output: The least number of perfect square numbers (for example, `1`, `4`, `9`, `16`, ...) which sum to `n`.
- Key requirements and edge cases to consider:
  - Handling large inputs efficiently.
  - Finding the minimum number of perfect squares.
- Example test cases:
  - Input: `n = 12`
    - Output: `3` (Explanation: `4 + 4 + 4`)
  - Input: `n = 13`
    - Output: `2` (Explanation: `9 + 4`)

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all combinations of perfect squares that sum up to `n`.
- Step-by-step breakdown:
  1. Generate all perfect squares up to `n`.
  2. For each perfect square, recursively try to find a combination that sums up to the remaining value.
  3. Keep track of the minimum number of perfect squares found so far.

```cpp
class Solution {
public:
    int numSquares(int n) {
        vector<int> squares;
        for (int i = 1; i * i <= n; i++) {
            squares.push_back(i * i);
        }
        
        int minCount = INT_MAX;
        function<void(int, int, int)> dfs = [&](int index, int target, int count) {
            if (target < 0) return;
            if (target == 0) {
                minCount = min(minCount, count);
                return;
            }
            for (int i = index; i < squares.size(); i++) {
                dfs(i, target - squares[i], count + 1);
            }
        };
        
        dfs(0, n, 0);
        return minCount;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(4^n)$, due to the recursive nature and trying all combinations of perfect squares.
> - **Space Complexity:** $O(n)$, for the recursive call stack.
> - **Why these complexities occur:** The brute force approach tries all possible combinations, leading to exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use dynamic programming to store the minimum number of perfect squares for each number up to `n`.
- Detailed breakdown:
  1. Initialize a DP array `dp` of size `n + 1`, where `dp[i]` represents the minimum number of perfect squares that sum up to `i`.
  2. Initialize `dp[0] = 0`, as the minimum number of perfect squares for `0` is `0`.
  3. For each number `i` from `1` to `n`, try all perfect squares `j` such that `j * j <= i`.
  4. Update `dp[i]` with the minimum of its current value and `dp[i - j * j] + 1`.
  5. Return `dp[n]` as the minimum number of perfect squares for `n`.

```cpp
class Solution {
public:
    int numSquares(int n) {
        vector<int> dp(n + 1, INT_MAX);
        dp[0] = 0;
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j * j <= i; j++) {
                dp[i] = min(dp[i], dp[i - j * j] + 1);
            }
        }
        
        return dp[n];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \sqrt{n})$, as we iterate over all numbers up to `n` and for each number, we try all perfect squares up to its square root.
> - **Space Complexity:** $O(n)$, for the DP array.
> - **Optimality proof:** This approach is optimal as it uses dynamic programming to store and reuse the results of subproblems, avoiding redundant calculations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, memoization.
- Problem-solving patterns identified: breaking down the problem into smaller subproblems, using a bottom-up approach.
- Optimization techniques learned: avoiding redundant calculations using dynamic programming.

**Mistakes to Avoid:**
- Not considering the optimal approach using dynamic programming.
- Not handling edge cases, such as `n = 0` or `n = 1`.
- Not optimizing the brute force approach, leading to exponential time complexity.

---