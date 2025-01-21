## Burst Balloons
**Problem Link:** https://leetcode.com/problems/burst-balloons/description

**Problem Statement:**
- Input format and constraints: Given `n` balloons, each with a number of coins associated with it, we need to find the maximum number of coins that can be collected by bursting the balloons in a specific order.
- Expected output format: The maximum number of coins that can be collected.
- Key requirements and edge cases to consider: The balloons are initially tied to the left and right ends with dummy balloons of value 1.
- Example test cases with explanations:
  - Example 1: Input: `nums = [3,1,5,8]`, Output: `167`, Explanation: `nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []`, Coins collected: `3*1*5 + 3*5*8 + 1*3*8 + 1*8*1 = 167`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can generate all possible permutations of the balloons and calculate the maximum coins that can be collected for each permutation.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of the balloons.
  2. For each permutation, calculate the maximum coins that can be collected by bursting the balloons in that order.
  3. Keep track of the maximum coins collected across all permutations.

```cpp
class Solution {
public:
    int maxCoins(vector<int>& nums) {
        int n = nums.size();
        vector<int> balloons = {1};
        for (int num : nums) balloons.push_back(num);
        balloons.push_back(1);
        int max_coins = 0;
        vector<int> permutation(balloons.size());
        for (int i = 0; i < balloons.size(); i++) permutation[i] = i;
        do {
            int coins = 0;
            vector<int> remaining(balloons.size());
            for (int i = 0; i < balloons.size(); i++) remaining[i] = i;
            for (int i = 0; i < balloons.size() - 1; i++) {
                int index = permutation[i];
                coins += balloons[remaining[index - 1]] * balloons[index] * balloons[remaining[index + 1]];
                remaining.erase(remaining.begin() + index);
            }
            max_coins = max(max_coins, coins);
        } while (next_permutation(permutation.begin(), permutation.end()));
        return max_coins;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$, where `n` is the number of balloons. This is because we are generating all permutations of the balloons.
> - **Space Complexity:** $O(n)$, where `n` is the number of balloons. This is because we need to store the permutations and the remaining balloons.
> - **Why these complexities occur:** The time complexity is exponential because we are generating all permutations, and the space complexity is linear because we need to store the permutations and the remaining balloons.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to store the maximum coins that can be collected for each subproblem.
- Detailed breakdown of the approach:
  1. Initialize a 2D array `dp` of size `(n + 2) x (n + 2)`, where `dp[i][j]` represents the maximum coins that can be collected by bursting the balloons from index `i` to `j`.
  2. Fill the `dp` array in a bottom-up manner.
  3. For each subproblem, try bursting each balloon and calculate the maximum coins that can be collected.

```cpp
class Solution {
public:
    int maxCoins(vector<int>& nums) {
        int n = nums.size();
        vector<int> balloons = {1};
        for (int num : nums) balloons.push_back(num);
        balloons.push_back(1);
        int m = balloons.size();
        vector<vector<int>> dp(m, vector<int>(m, 0));
        for (int length = 1; length <= m - 1; length++) {
            for (int left = 0; left <= m - length - 1; left++) {
                int right = left + length;
                for (int i = left + 1; i < right; i++) {
                    dp[left][right] = max(dp[left][right], dp[left][i] + dp[i][right] + balloons[left] * balloons[i] * balloons[right]);
                }
            }
        }
        return dp[0][m - 1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where `n` is the number of balloons. This is because we are filling the `dp` array in a bottom-up manner.
> - **Space Complexity:** $O(n^2)$, where `n` is the number of balloons. This is because we need to store the `dp` array.
> - **Optimality proof:** This solution is optimal because it uses dynamic programming to store the maximum coins that can be collected for each subproblem, avoiding redundant calculations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, bottom-up approach.
- Problem-solving patterns identified: Using dynamic programming to store the maximum coins that can be collected for each subproblem.
- Optimization techniques learned: Avoiding redundant calculations by using dynamic programming.
- Similar problems to practice: Other dynamic programming problems, such as the knapsack problem or the longest common subsequence problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` array correctly, not filling the `dp` array in a bottom-up manner.
- Edge cases to watch for: The case where there is only one balloon, the case where there are no balloons.
- Performance pitfalls: Using a brute force approach, not using dynamic programming to store the maximum coins that can be collected for each subproblem.
- Testing considerations: Testing the solution with different inputs, including edge cases.