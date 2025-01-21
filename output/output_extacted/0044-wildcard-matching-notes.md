## Wildcard Matching
**Problem Link:** https://leetcode.com/problems/wildcard-matching/description

**Problem Statement:**
- Input format and constraints: The function takes two strings `s` and `p` as input, where `s` is the source string and `p` is the pattern string containing wildcards `?` and `*`.
- Expected output format: The function returns a boolean indicating whether the source string matches the pattern string.
- Key requirements and edge cases to consider: 
  - `?` matches any single character.
  - `*` matches any sequence of characters (including an empty sequence).
  - The function should handle edge cases such as empty strings and patterns.
- Example test cases with explanations:
  - `isMatch("aa", "a")` returns `false`
  - `isMatch("aa", "*")` returns `true`
  - `isMatch("cb", "?a")` returns `false`
  - `isMatch("adceb", "*a*b")` returns `true`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Use recursion to explore all possible matches between the source string and the pattern string.
- Step-by-step breakdown of the solution:
  1. If the pattern string is empty, return whether the source string is also empty.
  2. If the source string is empty, return whether the pattern string only contains `*`.
  3. If the current characters in the source and pattern strings match or the pattern character is `?`, recursively check the remaining strings.
  4. If the pattern character is `*`, recursively check the remaining pattern string with the current source string or the remaining source string with the current pattern string.
- Why this approach comes to mind first: It directly implements the pattern matching rules.

```cpp
bool isMatch(string s, string p) {
    if (p.empty()) return s.empty();
    if (s.empty()) return p == "*" || (p.size() > 1 && p[1] == '*');

    if (p[0] == '?' || p[0] == s[0]) {
        return isMatch(s.substr(1), p.substr(1));
    }
    if (p[0] == '*') {
        return isMatch(s, p.substr(1)) || !s.empty() && isMatch(s.substr(1), p);
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{m+n})$, where $m$ and $n$ are the lengths of the source and pattern strings, respectively. This is because each recursive call branches into two possibilities.
> - **Space Complexity:** $O(m+n)$ due to the recursive call stack.
> - **Why these complexities occur:** The brute force approach explores all possible matches, leading to exponential time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Use dynamic programming to store the results of subproblems and avoid redundant computations.
- Detailed breakdown of the approach:
  1. Create a 2D table `dp` where `dp[i][j]` represents whether the first `i` characters of the source string match the first `j` characters of the pattern string.
  2. Initialize the base cases: `dp[0][0] = true`, `dp[0][j] = dp[0][j-1] && p[j-1] == '*'`, and `dp[i][0] = false` for `i > 0`.
  3. Fill in the table using the following rules:
    - If `p[j-1] == '?'` or `p[j-1] == s[i-1]`, `dp[i][j] = dp[i-1][j-1]`.
    - If `p[j-1] == '*'`, `dp[i][j] = dp[i][j-1] || dp[i-1][j]`.
- Proof of optimality: This approach has a time complexity of $O(mn)$, which is optimal because we must examine each character in the source and pattern strings at least once.

```cpp
bool isMatch(string s, string p) {
    int m = s.size(), n = p.size();
    vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
    dp[0][0] = true;
    for (int j = 1; j <= n; j++) {
        if (p[j-1] == '*') dp[0][j] = dp[0][j-1];
    }
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (p[j-1] == '?' || p[j-1] == s[i-1]) {
                dp[i][j] = dp[i-1][j-1];
            } else if (p[j-1] == '*') {
                dp[i][j] = dp[i][j-1] || dp[i-1][j];
            }
        }
    }
    return dp[m][n];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(mn)$, where $m$ and $n$ are the lengths of the source and pattern strings, respectively.
> - **Space Complexity:** $O(mn)$ for the 2D table.
> - **Optimality proof:** This approach has the optimal time complexity because it only examines each character in the source and pattern strings once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming and memoization.
- Problem-solving patterns identified: Using a 2D table to store the results of subproblems.
- Optimization techniques learned: Avoiding redundant computations by storing the results of subproblems.
- Similar problems to practice: Regular expression matching, substring matching.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the base cases correctly, not handling edge cases properly.
- Edge cases to watch for: Empty strings, patterns with only `*`, and patterns with `?` at the beginning or end.
- Performance pitfalls: Not using dynamic programming or memoization, leading to exponential time complexity.
- Testing considerations: Test the function with different input cases, including edge cases and boundary cases.