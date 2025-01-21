## Stone Game II
**Problem Link:** https://leetcode.com/problems/stone-game-ii/description

**Problem Statement:**
- Input format: An array of integers `piles` representing the number of stones in each pile.
- Constraints: `2 <= piles.length <= 100`, `0 <= piles[i] <= 10^4`.
- Expected output format: The maximum number of stones Alice can get.
- Key requirements: Alice and Bob play a game where they take turns removing stones from piles. Alice goes first, and she can remove `x` stones from the first `i + x` piles. Bob goes second, and he can remove any number of stones from the remaining piles.
- Example test cases:
  - Input: `piles = [2,7,9,4,4]`
  - Output: `10`
  - Explanation: Alice can remove 2 stones from the first pile, and then Bob can remove the remaining stones.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Use recursion to try all possible moves for Alice and Bob, and calculate the maximum number of stones Alice can get.
- Step-by-step breakdown of the solution:
  1. Define a recursive function `dfs` that takes the current index `i` and the number of stones `M` as arguments.
  2. In the `dfs` function, iterate over all possible moves `x` for Alice.
  3. For each move `x`, calculate the number of stones Alice can get, and recursively call the `dfs` function for Bob's turn.
  4. Update the maximum number of stones Alice can get.

```cpp
class Solution {
public:
    int stoneGameII(vector<int>& piles) {
        int n = piles.size();
        vector<int> suffix_sum(n + 1, 0);
        for (int i = n - 1; i >= 0; i--) {
            suffix_sum[i] = suffix_sum[i + 1] + piles[i];
        }
        
        unordered_map<string, int> memo;
        return dfs(0, 1, suffix_sum, memo);
    }
    
    int dfs(int i, int M, vector<int>& suffix_sum, unordered_map<string, int>& memo) {
        string key = to_string(i) + "," + to_string(M);
        if (memo.count(key)) {
            return memo[key];
        }
        
        if (i + 2 * M >= suffix_sum.size()) {
            return suffix_sum[i];
        }
        
        int max_stones = 0;
        for (int x = 1; x <= 2 * M; x++) {
            max_stones = max(max_stones, suffix_sum[i] - dfs(i + x, max(M, x), suffix_sum, memo));
        }
        
        memo[key] = max_stones;
        return max_stones;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot M)$, where $n$ is the number of piles and $M$ is the maximum number of stones that can be removed.
> - **Space Complexity:** $O(n \cdot M)$, where $n$ is the number of piles and $M$ is the maximum number of stones that can be removed.
> - **Why these complexities occur:** The brute force approach uses recursion to try all possible moves, resulting in exponential time complexity. The space complexity is due to the recursive call stack and the memoization table.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use dynamic programming to store the maximum number of stones Alice can get for each subproblem.
- Detailed breakdown of the approach:
  1. Define a 2D array `dp` to store the maximum number of stones Alice can get for each subproblem.
  2. Iterate over the piles in reverse order, and for each pile, iterate over all possible moves `x`.
  3. For each move `x`, calculate the number of stones Alice can get, and update the `dp` array.
  4. The final answer is stored in `dp[0][1]`.

```cpp
class Solution {
public:
    int stoneGameII(vector<int>& piles) {
        int n = piles.size();
        vector<int> suffix_sum(n + 1, 0);
        for (int i = n - 1; i >= 0; i--) {
            suffix_sum[i] = suffix_sum[i + 1] + piles[i];
        }
        
        vector<vector<int>> dp(n, vector<int>(n + 1, 0));
        for (int i = n - 1; i >= 0; i--) {
            for (int M = 1; i + 2 * M <= n; M++) {
                int max_stones = 0;
                for (int x = 1; x <= 2 * M; x++) {
                    max_stones = max(max_stones, suffix_sum[i] - dp[i + x][max(M, x)]);
                }
                dp[i][M] = max_stones;
            }
        }
        
        return dp[0][1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot M)$, where $n$ is the number of piles and $M$ is the maximum number of stones that can be removed.
> - **Space Complexity:** $O(n \cdot M)$, where $n$ is the number of piles and $M$ is the maximum number of stones that can be removed.
> - **Optimality proof:** The dynamic programming approach stores the maximum number of stones Alice can get for each subproblem, avoiding redundant calculations and resulting in optimal time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, recursion, memoization.
- Problem-solving patterns identified: Breaking down complex problems into smaller subproblems, using memoization to avoid redundant calculations.
- Optimization techniques learned: Using dynamic programming to store intermediate results, avoiding exponential time complexity.
- Similar problems to practice: Stone Game, Stone Game III.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, not initializing variables correctly.
- Edge cases to watch for: Empty input, invalid input.
- Performance pitfalls: Using exponential time complexity algorithms, not using memoization.
- Testing considerations: Test with different input sizes, test with different input values.