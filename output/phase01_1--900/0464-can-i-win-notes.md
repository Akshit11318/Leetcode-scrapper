## Can I Win

**Problem Link:** https://leetcode.com/problems/can-i-win/description

**Problem Statement:**
- Input format: `int maxChoosableInteger` and `int desiredTotal`
- Constraints: `1 <= maxChoosableInteger <= 20` and `0 <= desiredTotal <= 300`
- Expected output format: `bool`
- Key requirements and edge cases to consider: The function should determine if the first player can win the game where two players take turns picking a number from `1` to `maxChoosableInteger` without repeating any number, and the game ends when a player's total exceeds `desiredTotal`.
- Example test cases with explanations:
  - Example 1: `canIWin(10, 0)` returns `true` because the first player can choose any number, and since the total is 0, they can win by not playing.
  - Example 2: `canIWin(10, 40)` returns `false` because the sum of numbers from 1 to 10 is 55, which is greater than 40, but the first player cannot guarantee a win because the second player can also try to reach the total.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of numbers that the first player can choose and see if they can reach the desired total before the second player does.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of numbers from 1 to `maxChoosableInteger`.
  2. For each combination, calculate the total sum of the numbers.
  3. Check if the total sum is equal to or greater than `desiredTotal`.
  4. If it is, return `true` because the first player can win.
  5. If no combination leads to a win, return `false`.
- Why this approach comes to mind first: It's a straightforward way to solve the problem by trying all possible scenarios.

```cpp
class Solution {
public:
    bool canIWin(int maxChoosableInteger, int desiredTotal) {
        if (maxChoosableInteger * (maxChoosableInteger + 1) / 2 < desiredTotal) {
            return false;
        }
        
        vector<bool> used(maxChoosableInteger + 1, false);
        return dfs(used, 0, desiredTotal);
    }
    
    bool dfs(vector<bool>& used, int sum, int desiredTotal) {
        for (int i = 1; i <= used.size() - 1; i++) {
            if (!used[i]) {
                used[i] = true;
                if (sum + i >= desiredTotal || !dfs(used, sum + i, desiredTotal)) {
                    used[i] = false;
                    return true;
                }
                used[i] = false;
            }
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is `maxChoosableInteger`, because in the worst case, we have to try all possible combinations of numbers.
> - **Space Complexity:** $O(n)$, where $n$ is `maxChoosableInteger`, because we need to store the used numbers.
> - **Why these complexities occur:** The brute force approach tries all possible combinations, leading to exponential time complexity, and we need to store the used numbers, leading to linear space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use memoization to store the results of subproblems to avoid redundant calculations.
- Detailed breakdown of the approach:
  1. Create a memoization table to store the results of subproblems.
  2. Use a bitmask to represent the used numbers.
  3. For each possible bitmask, calculate the total sum of the used numbers.
  4. Check if the total sum is equal to or greater than `desiredTotal`.
  5. If it is, return `true` because the first player can win.
  6. If no combination leads to a win, return `false`.
- Proof of optimality: This approach has a time complexity of $O(2^n)$, which is optimal because we have to try all possible combinations of numbers.

```cpp
class Solution {
public:
    bool canIWin(int maxChoosableInteger, int desiredTotal) {
        if (maxChoosableInteger * (maxChoosableInteger + 1) / 2 < desiredTotal) {
            return false;
        }
        
        unordered_map<int, bool> memo;
        return dfs(maxChoosableInteger, desiredTotal, 0, memo);
    }
    
    bool dfs(int maxChoosableInteger, int desiredTotal, int state, unordered_map<int, bool>& memo) {
        if (memo.count(state)) {
            return memo[state];
        }
        
        for (int i = 1; i <= maxChoosableInteger; i++) {
            if ((state >> (i - 1)) & 1) {
                continue;
            }
            if (i >= desiredTotal || !dfs(maxChoosableInteger, desiredTotal - i, state | (1 << (i - 1)), memo)) {
                memo[state] = true;
                return true;
            }
        }
        memo[state] = false;
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is `maxChoosableInteger`, because in the worst case, we have to try all possible combinations of numbers.
> - **Space Complexity:** $O(2^n)$, where $n$ is `maxChoosableInteger`, because we need to store the results of subproblems in the memoization table.
> - **Optimality proof:** This approach has a time complexity of $O(2^n)$, which is optimal because we have to try all possible combinations of numbers.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Memoization, bitmask, and recursive search.
- Problem-solving patterns identified: Using memoization to store the results of subproblems to avoid redundant calculations.
- Optimization techniques learned: Using a bitmask to represent the used numbers and memoization to store the results of subproblems.
- Similar problems to practice: Other problems that involve recursive search and memoization, such as the N-Queens problem.

**Mistakes to Avoid:**
- Common implementation errors: Not using memoization to store the results of subproblems, leading to redundant calculations and exponential time complexity.
- Edge cases to watch for: The case where `maxChoosableInteger` is 0 or `desiredTotal` is 0.
- Performance pitfalls: Not using a bitmask to represent the used numbers, leading to inefficient use of memory.
- Testing considerations: Test the function with different inputs, including edge cases, to ensure that it works correctly.