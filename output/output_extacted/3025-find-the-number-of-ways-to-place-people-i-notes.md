## Find the Number of Ways to Place People I
**Problem Link:** https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/description

**Problem Statement:**
- Input: `n` (number of pairs) and `m` (number of rows)
- Constraints: $1 \leq n \leq 1000$ and $1 \leq m \leq 1000$
- Expected output: The number of ways to place `n` pairs in `m` rows such that no two people from the same pair are in the same row.
- Key requirements and edge cases:
  - Handle cases where `n` is greater than `m`.
  - Consider cases where `m` is 1.

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible combinations of placing `n` pairs in `m` rows.
- For each pair, choose a row for the first person and then choose a different row for the second person.
- Count all valid combinations.

```cpp
int countWays(int n, int m) {
    if (n > m) return 0; // Not enough rows for all pairs
    int ways = 1;
    for (int i = 0; i < n; i++) {
        ways *= (m - i); // Choose a row for the first person of the pair
        ways *= (m - i - 1); // Choose a different row for the second person
    }
    return ways;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of pairs, because we perform a constant amount of work for each pair.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the result.
> - **Why these complexities occur:** The time complexity is linear because we iterate over each pair once, and the space complexity is constant because we only use a fixed amount of space regardless of the input size.

### Optimal Approach (Required)

**Explanation:**
- The optimal approach recognizes that for each pair, we have $(m - i)$ choices for the first person and $(m - i - 1)$ choices for the second person, where $i$ is the current pair index.
- This is equivalent to calculating the number of permutations of `m` items taken `n` at a time, which can be expressed as $P(m, n) = \frac{m!}{(m-n)!}$.
- However, because we're dealing with pairs and the order within a pair doesn't matter (i.e., placing person A in row 1 and person B in row 2 is the same as placing person B in row 1 and person A in row 2), we need to account for this by dividing by $2^n$, where $n$ is the number of pairs.

```cpp
int countWays(int n, int m) {
    if (n > m) return 0; // Not enough rows for all pairs
    long long ways = 1;
    for (int i = 0; i < n; i++) {
        ways *= (m - i); // Choose a row for the first person of the pair
        ways *= (m - i - 1); // Choose a different row for the second person
        ways /= 2; // Account for the fact that order within a pair doesn't matter
    }
    return ways;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of pairs, because we perform a constant amount of work for each pair.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the result.
> - **Optimality proof:** This is the optimal solution because it directly calculates the number of valid placements without unnecessary iterations or memory usage.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: permutations, combinatorics, and optimization.
- Problem-solving patterns identified: recognizing the need to account for indistinguishable outcomes within pairs.
- Optimization techniques learned: reducing unnecessary calculations by dividing by the number of indistinguishable arrangements within each pair.

**Mistakes to Avoid:**
- Common implementation errors: not checking for the case where `n` is greater than `m`, and not accounting for indistinguishable arrangements within pairs.
- Edge cases to watch for: when `m` is 1, and when `n` equals `m`.
- Performance pitfalls: using excessive memory or iterations, such as attempting to generate all permutations explicitly.
- Testing considerations: ensure that the function correctly handles edge cases and large inputs efficiently.