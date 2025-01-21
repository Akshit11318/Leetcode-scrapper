## Number of Ways to Build House of Cards

**Problem Link:** https://leetcode.com/problems/number-of-ways-to-build-house-of-cards/description

**Problem Statement:**
- Input: An integer `n`, representing the number of `n` cards to build a house of cards.
- Expected Output: The number of ways to build a house of cards using `n` cards.
- Key Requirements:
  - Each card can be either a single card or a pair of cards.
  - A house of cards is valid if it is built from either a single card or a pair of cards, and the top card can be either a single card or a pair of cards.
- Edge Cases:
  - If `n` is less than 1, the function should return 0.
- Example Test Cases:
  - `n = 1`, output: 1 (a single card)
  - `n = 2`, output: 2 (either a single card and a single card, or a pair of cards)
  - `n = 3`, output: 4 (either a single card and a pair of cards, or a pair of cards and a single card, or a single card and a single card and a single card)

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can build a house of cards by recursively adding a single card or a pair of cards to the top of the house.
- Step-by-step breakdown of the solution:
  1. Define a recursive function that takes the number of cards as input.
  2. If the number of cards is less than 1, return 0 (base case).
  3. If the number of cards is 1, return 1 (a single card).
  4. Otherwise, recursively call the function with `n-1` cards (adding a single card) and `n-2` cards (adding a pair of cards).
  5. Return the sum of the two recursive calls.
- Why this approach comes to mind first: It is a straightforward and intuitive way to solve the problem, but it is not efficient due to the repeated computations.

```cpp
int buildHouseOfCardsBruteForce(int n) {
    if (n < 1) {
        return 0;
    }
    if (n == 1) {
        return 1;
    }
    return buildHouseOfCardsBruteForce(n-1) + buildHouseOfCardsBruteForce(n-2);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the number of cards. This is because each recursive call branches into two new calls, resulting in an exponential number of computations.
> - **Space Complexity:** $O(n)$, where $n$ is the number of cards. This is because the maximum depth of the recursion tree is $n$.
> - **Why these complexities occur:** The brute force approach is inefficient due to the repeated computations, which lead to an exponential time complexity. The space complexity is linear due to the recursion stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use dynamic programming to store the results of subproblems and avoid repeated computations.
- Detailed breakdown of the approach:
  1. Define a dynamic programming array `dp` of size `n+1`, where `dp[i]` represents the number of ways to build a house of cards using `i` cards.
  2. Initialize `dp[0] = 0` and `dp[1] = 1`.
  3. For each `i` from 2 to `n`, compute `dp[i] = dp[i-1] + dp[i-2]`.
  4. Return `dp[n]`.
- Why further optimization is impossible: The dynamic programming approach has a time complexity of $O(n)$ and a space complexity of $O(n)$, which is the best possible complexity for this problem.

```cpp
int buildHouseOfCardsOptimal(int n) {
    if (n < 1) {
        return 0;
    }
    vector<int> dp(n+1, 0);
    dp[1] = 1;
    for (int i = 2; i <= n; i++) {
        dp[i] = dp[i-1] + dp[i-2];
    }
    return dp[n];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of cards. This is because we only need to iterate from 2 to `n` to compute the dynamic programming array.
> - **Space Complexity:** $O(n)$, where $n` is the number of cards. This is because we need to store the dynamic programming array of size `n+1`.
> - **Optimality proof:** The dynamic programming approach is optimal because it avoids repeated computations and has a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, recursive functions.
- Problem-solving patterns identified: Avoiding repeated computations using dynamic programming.
- Optimization techniques learned: Using dynamic programming to improve time complexity.
- Similar problems to practice: Fibonacci sequence, Longest Common Subsequence.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the dynamic programming array correctly.
- Edge cases to watch for: Handling the case where `n` is less than 1.
- Performance pitfalls: Using a brute force approach that leads to exponential time complexity.
- Testing considerations: Testing the function with different values of `n` to ensure correctness.