## Stone Game III
**Problem Link:** https://leetcode.com/problems/stone-game-iii/description

**Problem Statement:**
- Input format: An array of integers `stoneValue` representing the value of each pile of stones.
- Constraints: $1 \leq stoneValue.length \leq 10^5$, $1 \leq stoneValue[i] \leq 10^4$.
- Expected output format: The maximum score Alice can achieve.
- Key requirements: Alice and Bob take turns removing 1 to 3 stones from the end of the array. The player who removes the stones earns the points for those stones. The game ends when all stones have been removed.
- Example test cases:
  - `stoneValue = [1,2,3,7]`, Output: `13`
  - `stoneValue = [1,2,3,-9]`, Output: `5`
  - `stoneValue = [1,2,3,6]`, Output: `6`

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to use recursion to simulate all possible moves for Alice and Bob.
- We calculate the score for each possible move and choose the one that maximizes Alice's score.

```cpp
class Solution {
public:
    int stoneGameIII(vector<int>& stoneValue) {
        int n = stoneValue.size();
        vector<int> suffixSum(n + 1, 0);
        for (int i = n - 1; i >= 0; i--) {
            suffixSum[i] = suffixSum[i + 1] + stoneValue[i];
        }
        
        vector<int> dp(n + 1, INT_MIN);
        dp[n] = 0;
        
        for (int i = n - 1; i >= 0; i--) {
            for (int x = 1; x <= 3; x++) {
                if (i + x > n) break;
                dp[i] = max(dp[i], suffixSum[i] - dp[i + x]);
            }
        }
        
        return dp[0];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of stones.
> - **Space Complexity:** $O(n)$, for the `suffixSum` and `dp` arrays.
> - **Why these complexities occur:** The time complexity is linear because we iterate over the `stoneValue` array once to calculate the suffix sum, and then iterate over the `dp` array to fill it. The space complexity is also linear because we need to store the suffix sum and the dynamic programming table.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use dynamic programming to store the maximum score Alice can achieve for each suffix of the `stoneValue` array.
- We calculate the suffix sum of the `stoneValue` array to efficiently calculate the score for each possible move.

```cpp
class Solution {
public:
    int stoneGameIII(vector<int>& stoneValue) {
        int n = stoneValue.size();
        vector<int> suffixSum(n + 1, 0);
        for (int i = n - 1; i >= 0; i--) {
            suffixSum[i] = suffixSum[i + 1] + stoneValue[i];
        }
        
        vector<int> dp(n + 1, INT_MIN);
        dp[n] = 0;
        
        for (int i = n - 1; i >= 0; i--) {
            for (int x = 1; x <= 3; x++) {
                if (i + x > n) break;
                dp[i] = max(dp[i], suffixSum[i] - dp[i + x]);
            }
        }
        
        return dp[0];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of stones.
> - **Space Complexity:** $O(n)$, for the `suffixSum` and `dp` arrays.
> - **Optimality proof:** This is the optimal solution because we are using dynamic programming to store the maximum score Alice can achieve for each suffix of the `stoneValue` array, and we are considering all possible moves for Alice.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, suffix sum.
- Problem-solving patterns identified: using dynamic programming to store the maximum score for each suffix of the array.
- Optimization techniques learned: using suffix sum to efficiently calculate the score for each possible move.

**Mistakes to Avoid:**
- Common implementation errors: not initializing the `dp` array correctly, not considering all possible moves for Alice.
- Edge cases to watch for: when the input array is empty, when the input array has only one element.
- Performance pitfalls: not using dynamic programming to store the maximum score for each suffix of the array, not using suffix sum to efficiently calculate the score for each possible move.
- Testing considerations: testing the solution with different input arrays, testing the solution with edge cases.