## Last Stone Weight II
**Problem Link:** https://leetcode.com/problems/last-stone-weight-ii/description

**Problem Statement:**
- Input: An array of integers representing stone weights.
- Constraints: The length of the input array is between 1 and 30.
- Expected Output: The minimum possible weight after all stones are smashed.
- Key Requirements: Minimize the weight difference between two piles of stones.
- Edge Cases: Empty input, single stone, equal weights.

Example:
- Input: `[2,7,4,1,8,1]`
- Output: `1`
- Explanation: We can divide the stones into two piles `[2,4,1,1]` and `[7,8]`, with a total weight of `8` and `15` respectively. After smashing, we get `|8-15|=7`. We can further divide the stones into `[1,1,4,2,7]` and `[8]`, resulting in a minimum weight difference of `1`.

---

### Brute Force Approach

**Explanation:**
- The initial thought is to generate all possible subsets of stones and calculate the weight difference between each subset and the remaining stones.
- We will use a recursive approach to generate all subsets.

```cpp
class Solution {
public:
    int lastStoneWeightII(vector<int>& stones) {
        int sum = 0;
        for (int stone : stones) {
            sum += stone;
        }
        int n = stones.size();
        vector<vector<bool>> dp(n, vector<bool>(sum / 2 + 1, false));
        dp[0][stones[0]] = true;
        for (int i = 1; i < n; i++) {
            for (int j = 0; j <= sum / 2; j++) {
                if (j >= stones[i]) {
                    dp[i][j] = dp[i - 1][j] || dp[i - 1][j - stones[i]];
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }
        int maxWeight = 0;
        for (int j = sum / 2; j >= 0; j--) {
            if (dp[n - 1][j]) {
                maxWeight = j;
                break;
            }
        }
        return sum - 2 * maxWeight;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot sum)$, where $n$ is the number of stones and $sum$ is the total weight of all stones.
> - **Space Complexity:** $O(n \cdot sum)$, for the dynamic programming table.
> - **Why these complexities occur:** The brute force approach generates all possible subsets, resulting in an exponential time complexity. However, we use dynamic programming to store intermediate results and avoid redundant calculations, reducing the time complexity to $O(n \cdot sum)$.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach is to use dynamic programming to find the maximum weight that can be achieved with a subset of stones, without exceeding half of the total weight.
- We will use a bottom-up dynamic programming approach to fill a table `dp` of size `n x (sum / 2 + 1)`, where `dp[i][j]` is `true` if it is possible to achieve a weight of `j` with the first `i` stones.

```cpp
class Solution {
public:
    int lastStoneWeightII(vector<int>& stones) {
        int sum = 0;
        for (int stone : stones) {
            sum += stone;
        }
        int n = stones.size();
        vector<vector<int>> dp(n + 1, vector<int>(sum / 2 + 1, 0));
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= sum / 2; j++) {
                if (j < stones[i - 1]) {
                    dp[i][j] = dp[i - 1][j];
                } else {
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - stones[i - 1]] + stones[i - 1]);
                }
            }
        }
        return sum - 2 * dp[n][sum / 2];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot sum)$, where $n$ is the number of stones and $sum$ is the total weight of all stones.
> - **Space Complexity:** $O(n \cdot sum)$, for the dynamic programming table.
> - **Optimality proof:** This approach is optimal because it uses dynamic programming to store intermediate results and avoid redundant calculations, resulting in the minimum possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, subset sum problem.
- Problem-solving patterns identified: using dynamic programming to avoid redundant calculations.
- Optimization techniques learned: using a bottom-up dynamic programming approach to fill a table.
- Similar problems to practice: subset sum problem, knapsack problem.

**Mistakes to Avoid:**
- Common implementation errors: incorrect indexing, incorrect initialization of the dynamic programming table.
- Edge cases to watch for: empty input, single stone, equal weights.
- Performance pitfalls: using a recursive approach without memoization, resulting in exponential time complexity.
- Testing considerations: test the solution with different inputs, including edge cases and large inputs.