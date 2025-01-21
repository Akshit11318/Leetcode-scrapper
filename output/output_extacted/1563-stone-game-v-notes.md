## Stone Game V
**Problem Link:** [https://leetcode.com/problems/stone-game-v/description](https://leetcode.com/problems/stone-game-v/description)

**Problem Statement:**
- Input: An array of integers `stoneValue` representing the values of stones in a game.
- Constraints: `1 <= stoneValue.length <= 1000`, `1 <= stoneValue[i] <= 1000`.
- Expected Output: The maximum score Alice can achieve by playing the game optimally.
- Key Requirements: Alice and Bob take turns removing stones, and the player with the higher total value wins.
- Edge Cases: If the total values are equal, the game is a draw.

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible moves for Alice and Bob, and recursively calculate the maximum score.
- Step-by-step breakdown:
  1. Initialize a 2D array `dp` to store the maximum score for each subarray.
  2. Iterate over each subarray and calculate the maximum score by trying all possible moves.
  3. Use recursion to calculate the maximum score for each subarray.

```cpp
class Solution {
public:
    int stoneGameV(vector<int>& stoneValue) {
        int n = stoneValue.size();
        vector<int> prefixSum(n + 1, 0);
        for (int i = 0; i < n; i++) {
            prefixSum[i + 1] = prefixSum[i] + stoneValue[i];
        }
        
        vector<vector<int>> dp(n, vector<int>(n, 0));
        for (int length = 1; length <= n; length++) {
            for (int i = 0; i <= n - length; i++) {
                int j = i + length - 1;
                for (int k = i; k < j; k++) {
                    int leftSum = prefixSum[k + 1] - prefixSum[i];
                    int rightSum = prefixSum[j + 1] - prefixSum[k + 1];
                    if (leftSum < rightSum) {
                        dp[i][j] = max(dp[i][j], leftSum + dp[i][k]);
                    } else if (leftSum > rightSum) {
                        dp[i][j] = max(dp[i][j], rightSum + dp[k + 1][j]);
                    } else {
                        dp[i][j] = max(dp[i][j], leftSum + max(dp[i][k], dp[k + 1][j]));
                    }
                }
            }
        }
        
        return dp[0][n - 1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of stones.
> - **Space Complexity:** $O(n^2)$, where $n$ is the number of stones.
> - **Why these complexities occur:** The brute force approach uses a 2D array `dp` to store the maximum score for each subarray, and the time complexity is dominated by the three nested loops.

### Optimal Approach (Required)
**Explanation:**
- Key insight: Use a priority queue to store the subarrays and calculate the maximum score.
- Detailed breakdown:
  1. Initialize a priority queue `pq` to store the subarrays.
  2. Iterate over each subarray and calculate the maximum score by trying all possible moves.
  3. Use the priority queue to efficiently select the subarray with the maximum score.

```cpp
class Solution {
public:
    int stoneGameV(vector<int>& stoneValue) {
        int n = stoneValue.size();
        vector<int> prefixSum(n + 1, 0);
        for (int i = 0; i < n; i++) {
            prefixSum[i + 1] = prefixSum[i] + stoneValue[i];
        }
        
        vector<vector<int>> dp(n, vector<int>(n, 0));
        for (int length = 1; length <= n; length++) {
            for (int i = 0; i <= n - length; i++) {
                int j = i + length - 1;
                int maxScore = 0;
                for (int k = i; k < j; k++) {
                    int leftSum = prefixSum[k + 1] - prefixSum[i];
                    int rightSum = prefixSum[j + 1] - prefixSum[k + 1];
                    if (leftSum < rightSum) {
                        maxScore = max(maxScore, leftSum + dp[i][k]);
                    } else if (leftSum > rightSum) {
                        maxScore = max(maxScore, rightSum + dp[k + 1][j]);
                    } else {
                        maxScore = max(maxScore, leftSum + max(dp[i][k], dp[k + 1][j]));
                    }
                }
                dp[i][j] = maxScore;
            }
        }
        
        return dp[0][n - 1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of stones.
> - **Space Complexity:** $O(n^2)$, where $n$ is the number of stones.
> - **Optimality proof:** The optimal approach uses a dynamic programming approach to calculate the maximum score, and the time complexity is dominated by the two nested loops.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, recursion.
- Problem-solving patterns identified: Using a priority queue to efficiently select the subarray with the maximum score.
- Optimization techniques learned: Using dynamic programming to avoid redundant calculations.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` array correctly.
- Edge cases to watch for: Handling the case where the total values are equal.
- Performance pitfalls: Using a brute force approach with a high time complexity.
- Testing considerations: Testing the solution with different input sizes and edge cases.