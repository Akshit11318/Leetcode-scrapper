## Construct String with Minimum Cost
**Problem Link:** https://leetcode.com/problems/construct-string-with-minimum-cost-easy/description

**Problem Statement:**
- Input: Two strings `s` and `cost`.
- Constraints: The length of `s` and `cost` are the same, and the length is in the range `[1, 5 * 10^3]`.
- Expected Output: The minimum cost to construct the string.
- Key Requirements:
  - The cost of deleting a character is `0`.
  - The cost of inserting a character is `1`.
  - The cost of replacing a character is the cost of the character in the `cost` string.
- Edge Cases:
  - When `s` and `cost` are the same, the minimum cost should be `0`.
  - When `s` and `cost` are completely different, the minimum cost should be the length of `s`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible operations (insert, delete, replace) for each character in the string and calculate the minimum cost.
- This approach comes to mind first because it is a straightforward way to solve the problem by trying all possible solutions.

```cpp
int minCost(string s, string cost) {
    int n = s.length();
    int minCost = 0;
    for (int i = 0; i < n; i++) {
        // Try all possible operations
        int replaceCost = cost[i] - '0';
        int insertCost = 1;
        int deleteCost = 0;
        minCost += min(replaceCost, min(insertCost, deleteCost));
    }
    return minCost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we are iterating over each character in the string once.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the minimum cost.
> - **Why these complexities occur:** The time complexity is linear because we are iterating over the string once, and the space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is that we can use dynamic programming to store the minimum cost of constructing the string up to each position.
- We can then use these stored values to calculate the minimum cost of constructing the rest of the string.
- This approach is optimal because it avoids redundant calculations and has a time complexity of $O(n)$.

```cpp
int minCost(string s, string cost) {
    int n = s.length();
    int minCost = 0;
    for (int i = 0; i < n; i++) {
        // Calculate the minimum cost of constructing the string up to this position
        minCost += cost[i] - '0';
    }
    return minCost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we are iterating over each character in the string once.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the minimum cost.
> - **Optimality proof:** This approach is optimal because it has a time complexity of $O(n)$ and uses a constant amount of space. We cannot do better than this because we must at least read the input string once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, greedy algorithms.
- Problem-solving patterns identified: using stored values to avoid redundant calculations.
- Optimization techniques learned: avoiding redundant calculations, using dynamic programming.
- Similar problems to practice: other dynamic programming problems, such as the Fibonacci sequence or the longest common subsequence.

**Mistakes to Avoid:**
- Common implementation errors: not initializing variables, not checking for edge cases.
- Edge cases to watch for: when the input strings are empty, when the input strings are the same.
- Performance pitfalls: using excessive memory, having a high time complexity.
- Testing considerations: testing with different input sizes, testing with different input values.