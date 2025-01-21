## Dice Roll Simulation
**Problem Link:** https://leetcode.com/problems/dice-roll-simulation/description

**Problem Statement:**
- Input format and constraints: Given an integer `n` and a `rollMax` array representing the maximum number of times each number can be rolled, and an array `target` representing the target number of rolls for each number, find the number of ways to roll the dice to reach the target.
- Expected output format: The number of ways to roll the dice to reach the target, modulo $10^9 + 7$.
- Key requirements and edge cases to consider: The target array may contain numbers that are not possible to roll given the `rollMax` constraints, and the number of ways to roll the dice may exceed the modulo value.
- Example test cases with explanations: 
    - `n = 2, rollMax = [1,1,2,2,2,3], target = [1,1,1,1,1,1]`: The output should be `1`, because there is only one way to roll the dice to reach the target.
    - `n = 2, rollMax = [1,1,1,1,1,1], target = [1,1,1,1,1,1]`: The output should be `0`, because it is not possible to roll the dice to reach the target.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves generating all possible combinations of rolls and counting the number of ways to reach the target.
- Step-by-step breakdown of the solution: 
    1. Initialize a counter to store the number of ways to roll the dice to reach the target.
    2. Generate all possible combinations of rolls using recursion or iteration.
    3. For each combination, check if the target is reached by comparing the number of rolls for each number with the corresponding target value.
    4. If the target is reached, increment the counter.
- Why this approach comes to mind first: The brute force approach is often the most straightforward solution, as it involves generating all possible combinations and checking each one.

```cpp
class Solution {
public:
    int dieSimulator(int n, vector<int>& rollMax, vector<int>& target) {
        long long mod = 1e9 + 7;
        long long count = 0;
        vector<int> rolls(6, 0);
        
        function<void(int)> dfs = [&](int i) {
            if (i == n) {
                bool match = true;
                for (int j = 0; j < 6; j++) {
                    if (rolls[j] != target[j]) {
                        match = false;
                        break;
                    }
                }
                if (match) count++;
                return;
            }
            for (int j = 0; j < 6; j++) {
                if (rolls[j] < rollMax[j]) {
                    rolls[j]++;
                    dfs(i + 1);
                    rolls[j]--;
                }
            }
        };
        dfs(0);
        return count % mod;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(6^n)$, where $n$ is the number of rolls. This is because there are $6$ possible outcomes for each roll, and we are generating all possible combinations of rolls.
> - **Space Complexity:** $O(n)$, where $n$ is the number of rolls. This is because we are using a recursive function call stack to generate all possible combinations of rolls.
> - **Why these complexities occur:** The brute force approach involves generating all possible combinations of rolls, which results in an exponential time complexity. The space complexity is linear because we are using a recursive function call stack to generate all possible combinations of rolls.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using dynamic programming to store the number of ways to roll the dice to reach each target value.
- Detailed breakdown of the approach: 
    1. Initialize a 3D array `dp` to store the number of ways to roll the dice to reach each target value.
    2. Iterate over each roll and update the `dp` array accordingly.
    3. Use the `dp` array to calculate the number of ways to roll the dice to reach the target.
- Proof of optimality: The optimal solution has a time complexity of $O(n \cdot 16 \cdot 6)$, which is much faster than the brute force approach.

```cpp
class Solution {
public:
    int dieSimulator(int n, vector<int>& rollMax, vector<int>& target) {
        long long mod = 1e9 + 7;
        vector<vector<vector<long long>>> dp(n + 1, vector<vector<long long>>(6, vector<long long>(16, -1)));
        
        function<long long(int, int, int)> dfs = [&](int i, int j, int k) {
            if (i == n) {
                return k == target[j];
            }
            if (dp[i][j][k] != -1) return dp[i][j][k];
            long long res = 0;
            for (int x = 0; x < 6; x++) {
                if (x == j) {
                    if (k < rollMax[j]) {
                        res = (res + dfs(i + 1, x, k + 1)) % mod;
                    }
                } else {
                    if (target[x] > 0) {
                        res = (res + dfs(i + 1, x, 1)) % mod;
                    }
                }
            }
            return dp[i][j][k] = res;
        };
        long long res = 0;
        for (int i = 0; i < 6; i++) {
            if (target[i] > 0) {
                res = (res + dfs(1, i, 1)) % mod;
            }
        }
        return res;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot 16 \cdot 6)$, where $n$ is the number of rolls. This is because we are using a recursive function call stack to generate all possible combinations of rolls, and we are storing the number of ways to roll the dice to reach each target value in a 3D array.
> - **Space Complexity:** $O(n \cdot 16 \cdot 6)$, where $n$ is the number of rolls. This is because we are using a 3D array to store the number of ways to roll the dice to reach each target value.
> - **Optimality proof:** The optimal solution has a time complexity of $O(n \cdot 16 \cdot 6)$, which is much faster than the brute force approach. This is because we are using dynamic programming to store the number of ways to roll the dice to reach each target value, which reduces the number of recursive function calls.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, recursive function calls, and memoization.
- Problem-solving patterns identified: Using dynamic programming to store the number of ways to roll the dice to reach each target value.
- Optimization techniques learned: Using memoization to reduce the number of recursive function calls.
- Similar problems to practice: Other problems that involve dynamic programming and recursive function calls.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` array correctly, not using memoization to reduce the number of recursive function calls.
- Edge cases to watch for: The target array may contain numbers that are not possible to roll given the `rollMax` constraints.
- Performance pitfalls: Not using dynamic programming to store the number of ways to roll the dice to reach each target value, which can result in an exponential time complexity.
- Testing considerations: Testing the solution with different input values to ensure that it works correctly.