## Climbing Stairs
**Problem Link:** https://leetcode.com/problems/climbing-stairs/description

**Problem Statement:**
- Input: `n`, the number of stairs.
- Constraints: `1 <= n <= 45`.
- Expected output: The number of distinct ways to climb `n` stairs.
- Key requirements: Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top of a staircase with `n` steps?
- Edge cases: `n = 1`, `n = 2`.
- Example test cases:
  - Input: `n = 2`
  Output: `2`
  Explanation: There are two ways to climb to the top.
  1. 1 step + 1 step
  2. 2 steps
  - Input: `n = 3`
  Output: `3`
  Explanation: There are three ways to climb to the top.
  1. 1 step + 1 step + 1 step
  2. 1 step + 2 steps
  3. 2 steps + 1 step

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to try all possible combinations of climbing 1 or 2 steps and count the number of distinct ways to reach the top.
- This involves recursive exploration of all possible step combinations.
- This approach comes to mind first because it directly addresses the problem by trying all possibilities.

```cpp
class Solution {
public:
    int climbStairs(int n) {
        return climbStairsRecursive(n);
    }
    
    int climbStairsRecursive(int n) {
        // Base cases
        if (n == 1) return 1; // Only one way to climb 1 step
        if (n == 2) return 2; // Two ways to climb 2 steps
        
        // Recursive case: Try climbing 1 or 2 steps and sum the results
        return climbStairsRecursive(n-1) + climbStairsRecursive(n-2);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$ because each step can lead to two recursive calls, leading to an exponential number of operations.
> - **Space Complexity:** $O(n)$ due to the recursion stack, as the maximum depth of the recursion tree is $n$.
> - **Why these complexities occur:** The exponential time complexity is due to the overlapping subproblems that are solved multiple times. The space complexity is due to the recursive call stack.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is recognizing that this problem has overlapping subproblems, which can be solved using dynamic programming.
- The dynamic programming approach involves storing the results of subproblems in a table to avoid redundant computation.
- This approach is optimal because it solves each subproblem exactly once, reducing the time complexity significantly.

```cpp
class Solution {
public:
    int climbStairs(int n) {
        if (n == 1) return 1;
        if (n == 2) return 2;
        
        vector<int> dp(n+1, 0);
        dp[1] = 1;
        dp[2] = 2;
        
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i-1] + dp[i-2];
        }
        
        return dp[n];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because we solve each subproblem exactly once and store the results.
> - **Space Complexity:** $O(n)$ for the dynamic programming table.
> - **Optimality proof:** This is optimal because we minimize the number of operations by solving each subproblem once and storing the result, avoiding the exponential growth of the brute force approach.

---

### Final Notes

**Learning Points:**
- Dynamic programming is a powerful technique for solving problems with overlapping subproblems.
- Recognizing the structure of a problem is key to applying dynamic programming.
- The `climbStairs` problem demonstrates how to transform a recursive solution into a dynamic programming solution.

**Mistakes to Avoid:**
- Not recognizing overlapping subproblems, leading to inefficient recursive solutions.
- Failing to initialize the base cases correctly in dynamic programming.
- Not considering the trade-offs between time and space complexity in different approaches.

---