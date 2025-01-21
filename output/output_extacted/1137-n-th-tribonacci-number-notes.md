## N-th Tribonacci Number

**Problem Link:** https://leetcode.com/problems/n-th-tribonacci-number/description

**Problem Statement:**
- Input format and constraints: The problem takes an integer `n` as input and returns the `n`-th Tribonacci number. The Tribonacci sequence is defined such that each number is the sum of the three preceding ones, starting from 0, 0, 1.
- Expected output format: The output should be the `n`-th Tribonacci number.
- Key requirements and edge cases to consider: The input `n` will be in the range `[0, 37]`.
- Example test cases with explanations:
  - `tribonacci(0) = 0` because the first Tribonacci number is 0.
  - `tribonacci(1) = 0` because the second Tribonacci number is 0.
  - `tribonacci(2) = 1` because the third Tribonacci number is 1.
  - `tribonacci(3) = 1` because the fourth Tribonacci number is the sum of the first three (0 + 0 + 1 = 1).
  - `tribonacci(4) = 2` because the fifth Tribonacci number is the sum of the second, third, and fourth (0 + 1 + 1 = 2).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One of the simplest ways to solve this problem is by using recursion. The idea is to calculate each Tribonacci number by summing the three preceding ones.
- Step-by-step breakdown of the solution:
  1. Define a recursive function that takes `n` as input.
  2. Base cases: If `n` is 0 or 1, return 0. If `n` is 2, return 1.
  3. Recursive case: For `n > 2`, return the sum of the `n-1`, `n-2`, and `n-3` Tribonacci numbers.
- Why this approach comes to mind first: It directly follows from the definition of the Tribonacci sequence.

```cpp
class Solution {
public:
    int tribonacci(int n) {
        if (n == 0 || n == 1) return 0;
        if (n == 2) return 1;
        return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(3^n)$ because each call branches into three more recursive calls.
> - **Space Complexity:** $O(n)$ due to the recursion stack.
> - **Why these complexities occur:** The exponential time complexity is due to the repeated computation of the same subproblems, and the space complexity is due to the maximum depth of the recursion tree.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is inefficient due to the repeated computation of the same subproblems. We can improve this by using dynamic programming to store and reuse the results of subproblems.
- Detailed breakdown of the approach:
  1. Initialize an array `dp` of size `n+1` with the base cases `dp[0] = dp[1] = 0` and `dp[2] = 1`.
  2. For `i` from 3 to `n`, calculate `dp[i] = dp[i-1] + dp[i-2] + dp[i-3]`.
  3. Return `dp[n]`.
- Proof of optimality: This approach ensures that each subproblem is solved only once and its result is stored for future use, reducing the time complexity to linear.
- Why further optimization is impossible: This approach has a linear time complexity, which is the best possible for this problem since we must at least read the input and write the output.

```cpp
class Solution {
public:
    int tribonacci(int n) {
        if (n == 0 || n == 1) return 0;
        if (n == 2) return 1;
        vector<int> dp(n+1);
        dp[0] = 0;
        dp[1] = 0;
        dp[2] = 1;
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3];
        }
        return dp[n];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because we only iterate up to `n` once.
> - **Space Complexity:** $O(n)$ for the `dp` array.
> - **Optimality proof:** The linear time complexity is optimal because we must at least compute each Tribonacci number once to solve the problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming and recursion.
- Problem-solving patterns identified: Breaking down problems into smaller subproblems and solving them efficiently.
- Optimization techniques learned: Memoization and dynamic programming to avoid redundant computation.
- Similar problems to practice: Fibonacci sequence, Longest Common Subsequence, etc.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting base cases or not handling edge cases properly.
- Edge cases to watch for: Small inputs like `n = 0, 1, 2`.
- Performance pitfalls: Using naive recursion without memoization or dynamic programming for problems with overlapping subproblems.
- Testing considerations: Always test with small inputs and edge cases to ensure correctness before optimizing for performance.