## Find Number of Ways to Reach the K-th Stair

**Problem Link:** https://leetcode.com/problems/find-number-of-ways-to-reach-the-k-th-stair/description

**Problem Statement:**
- Input: An integer `k`, representing the number of stairs.
- Constraints: `1 <= k <= 45`
- Expected Output: The number of ways to reach the `k`-th stair, where you can either climb 1 or 2 steps at a time.
- Key Requirements and Edge Cases: 
    - For `k = 1`, there is only 1 way to reach the first stair (1 step).
    - For `k = 2`, there are 2 ways to reach the second stair (1+1 or 2 steps).
    - For larger `k`, the number of ways to reach the `k`-th stair is the sum of the number of ways to reach the `(k-1)`-th and `(k-2)`-th stairs.

### Brute Force Approach

**Explanation:**
- The initial thought process is to use recursion to calculate the number of ways to reach each stair. This approach comes to mind first because it directly follows the problem's recursive nature.
- However, this approach is inefficient because it performs many redundant calculations.

```cpp
int climbStairs(int k) {
    if (k == 1) return 1;
    if (k == 2) return 2;
    return climbStairs(k - 1) + climbStairs(k - 2);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^k)$, because each call branches into two more calls.
> - **Space Complexity:** $O(k)$, due to the recursion stack.
> - **Why these complexities occur:** The exponential time complexity is due to the overlapping subproblems, while the space complexity is due to the maximum depth of the recursion tree.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is recognizing that this problem can be solved using dynamic programming, specifically by storing the solutions to subproblems to avoid redundant calculations.
- We can use an array `dp` of size `k+1` to store the number of ways to reach each stair, where `dp[i]` represents the number of ways to reach the `i`-th stair.
- We initialize `dp[1] = 1` and `dp[2] = 2`, and then for each stair `i` from 3 to `k`, we calculate `dp[i] = dp[i-1] + dp[i-2]`.

```cpp
int climbStairs(int k) {
    if (k == 1) return 1;
    if (k == 2) return 2;
    vector<int> dp(k + 1);
    dp[1] = 1;
    dp[2] = 2;
    for (int i = 3; i <= k; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    return dp[k];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k)$, because we only need to iterate up to `k` once.
> - **Space Complexity:** $O(k)$, because we need to store the `dp` array of size `k+1`.
> - **Optimality proof:** This solution is optimal because it avoids all redundant calculations by storing the solutions to subproblems, resulting in a linear time complexity.

---

### Alternative Approach

**Explanation:**
- An alternative approach is to use a constant amount of space by only keeping track of the last two values in the sequence, since each new value only depends on the previous two.
- This approach reduces the space complexity to $O(1)$, making it more memory-efficient for large inputs.

```cpp
int climbStairs(int k) {
    if (k == 1) return 1;
    if (k == 2) return 2;
    int a = 1, b = 2;
    for (int i = 3; i <= k; i++) {
        int temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k)$, because we still need to iterate up to `k` once.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the last two values.
> - **Trade-off analysis:** This approach is preferred when memory usage is a concern, as it achieves the same time complexity as the optimal approach but with reduced space complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, memoization, and optimization of recursive problems.
- Problem-solving patterns identified: recognizing overlapping subproblems and applying dynamic programming to avoid redundant calculations.
- Optimization techniques learned: using dynamic programming to store solutions to subproblems and reducing space complexity by only keeping track of necessary values.
- Similar problems to practice: Fibonacci sequence, Longest Common Subsequence, and other dynamic programming problems.

**Mistakes to Avoid:**
- Common implementation errors: not handling base cases correctly, not initializing arrays or variables properly, and not considering edge cases.
- Edge cases to watch for: inputs of 1 and 2, and ensuring the solution works for all `k` within the given constraints.
- Performance pitfalls: not optimizing recursive problems, resulting in exponential time complexities, and not considering memory usage for large inputs.
- Testing considerations: thoroughly testing the solution with various inputs, including edge cases, to ensure correctness and efficiency.