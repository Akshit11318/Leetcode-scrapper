## Number of Dice Rolls With Target Sum

**Problem Link:** https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/description

**Problem Statement:**
- Input: `n` (number of dice), `k` (number of faces on each die), `target` (the target sum)
- Output: The number of possible ways to roll the dice to reach the target sum
- Key requirements: Each die has `k` faces numbered from 1 to `k`, and we want to find the number of ways to roll `n` dice to reach a sum of `target`
- Example test cases:
  - `n = 1`, `k = 6`, `target = 3` -> `1` (there's only one way to roll a single die to get a sum of 3)
  - `n = 2`, `k = 6`, `target = 7` -> `6` (there are 6 ways to roll two dice to get a sum of 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1))

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible combinations of dice rolls and count the ones that sum up to the target
- We can use a recursive function to generate all possible combinations of dice rolls
- However, this approach is inefficient because it generates many duplicate combinations and has a high time complexity

```cpp
class Solution {
public:
    int numRollsToTarget(int n, int k, int target) {
        int count = 0;
        vector<int> rolls(n);
        function<void(int)> rollDice = [&](int index) {
            if (index == n) {
                int sum = 0;
                for (int roll : rolls) sum += roll;
                if (sum == target) count++;
            } else {
                for (int i = 1; i <= k; i++) {
                    rolls[index] = i;
                    rollDice(index + 1);
                }
            }
        };
        rollDice(0);
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(k^n)$ (we generate $k^n$ possible combinations of dice rolls)
> - **Space Complexity:** $O(n)$ (we use a recursive function with a depth of $n$)
> - **Why these complexities occur:** The time complexity is high because we generate all possible combinations of dice rolls, and the space complexity is moderate because we use a recursive function with a depth of $n$

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use dynamic programming to store the number of ways to reach each sum with each number of dice
- We can use a 2D array `dp` where `dp[i][j]` is the number of ways to reach a sum of `j` with `i` dice
- We can fill up the `dp` array in a bottom-up manner by iterating over each die and each possible sum

```cpp
class Solution {
public:
    int numRollsToTarget(int n, int k, int target) {
        const int MOD = 1e9 + 7;
        vector<vector<int>> dp(n + 1, vector<int>(target + 1));
        dp[0][0] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= target; j++) {
                for (int face = 1; face <= k; face++) {
                    if (j - face >= 0) {
                        dp[i][j] = (dp[i][j] + dp[i - 1][j - face]) % MOD;
                    }
                }
            }
        }
        return dp[n][target];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k \cdot target)$ (we fill up the `dp` array in a bottom-up manner)
> - **Space Complexity:** $O(n \cdot target)$ (we use a 2D array `dp` with a size of $n \cdot target$)
> - **Optimality proof:** This approach is optimal because we use dynamic programming to store the number of ways to reach each sum with each number of dice, which avoids duplicate calculations and reduces the time complexity significantly.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is dynamic programming, which is used to store the number of ways to reach each sum with each number of dice
- The problem-solving pattern identified is the use of a 2D array to store the dynamic programming state
- The optimization technique learned is the use of dynamic programming to avoid duplicate calculations and reduce the time complexity
- Similar problems to practice include other dynamic programming problems, such as the Fibonacci sequence and the knapsack problem

**Mistakes to Avoid:**
- A common implementation error is to forget to initialize the `dp` array correctly, which can lead to incorrect results
- An edge case to watch for is when `n` or `k` is 0, which can lead to division by zero or other errors
- A performance pitfall is to use a recursive function without memoization, which can lead to high time complexity and stack overflow errors
- A testing consideration is to test the function with different inputs and edge cases to ensure it works correctly.