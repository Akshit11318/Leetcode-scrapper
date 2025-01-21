## Regular Expression Matching
**Problem Link:** https://leetcode.com/problems/regular-expression-matching/description

**Problem Statement:**
- Input format and constraints: Given an input string `s` and a pattern `p`, implement regular expression matching with support for `.` and `*` where `.` matches any single character and `*` matches zero or more of the preceding element.
- Expected output format: Return `true` if the entire string `s` matches the entire pattern `p`, otherwise return `false`.
- Key requirements and edge cases to consider:
  - Handling of `*` when the preceding character does not match any character in `s`.
  - Matching `.` with any single character.
  - Empty string and pattern handling.
- Example test cases with explanations:
  - `isMatch("aa", "a")` returns `false` because the pattern does not fully match the string.
  - `isMatch("aa", "a*")` returns `true` because `a*` matches zero or more `a`s, which covers the case of two `a`s.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves generating all possible matches of the pattern against the string and checking each one. This can be achieved through recursion, exploring all possible branches of matches.
- Step-by-step breakdown of the solution:
  1. Start with the first character of the string and the first character of the pattern.
  2. If the pattern character is `.` or matches the string character, move on to the next characters in both the string and the pattern.
  3. If the pattern character is followed by `*`, consider two possibilities: using the `*` to match zero occurrences of the preceding character (thus moving on to the next character in the pattern) or using the `*` to match one or more occurrences (thus staying on the same character in the pattern but moving on in the string).
  4. Continue this process until either the entire string and pattern are matched or it's determined that no match is possible.
- Why this approach comes to mind first: It's a straightforward, exhaustive search that checks all possible combinations, ensuring no potential matches are overlooked.

```cpp
bool isMatch(string s, string p) {
    if (p.empty()) return s.empty();
    bool first_match = (!s.empty() && 
                        (p[0] == s[0] || p[0] == '.'));
    if (p.length() >= 2 && p[1] == '*') {
        return (isMatch(s, p.substr(2)) || 
                first_match && isMatch(s.substr(1), p));
    } else {
        return first_match && isMatch(s.substr(1), p.substr(1));
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{n+m})$ in the worst case, where $n$ and $m$ are the lengths of the string and pattern, respectively. This is because each character in the pattern can potentially branch into two separate paths (one where the character matches and one where it doesn't), leading to exponential time complexity.
> - **Space Complexity:** $O(n+m)$ due to the recursion stack, which in the worst case can go as deep as the sum of the lengths of the string and the pattern.
> - **Why these complexities occur:** The exponential time complexity occurs because of the branching factor in the recursion, where each character in the pattern can lead to multiple recursive calls. The space complexity is linear due to the maximum depth of the recursion stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Using dynamic programming to store and reuse the results of subproblems, reducing the time complexity significantly. The idea is to build a 2D table where each cell `[i][j]` represents whether the first `i` characters of the string match the first `j` characters of the pattern.
- Detailed breakdown of the approach:
  1. Initialize a 2D boolean array `dp` of size `(s.length() + 1) x (p.length() + 1)`.
  2. `dp[i][j]` is `true` if the first `i` characters in `s` match the first `j` characters in `p`.
  3. Fill in the table by iterating through `s` and `p`, using the rules for `.` and `*`.
  4. The final result is stored in `dp[s.length()][p.length()]`.
- Proof of optimality: This approach ensures that each subproblem is solved only once and the results are stored for future reference, avoiding the exponential time complexity of the brute force approach.

```cpp
bool isMatch(string s, string p) {
    int n = s.length(), m = p.length();
    vector<vector<bool>> dp(n + 1, vector<bool>(m + 1, false));
    dp[n][m] = true;
    for (int i = n; i >= 0; --i) {
        for (int j = m - 1; j >= 0; --j) {
            bool first_match = (i < n && (p[j] == s[i] || p[j] == '.'));
            if (j + 1 < m && p[j + 1] == '*') {
                dp[i][j] = dp[i][j + 2] || first_match && dp[i + 1][j];
            } else {
                dp[i][j] = first_match && dp[i + 1][j + 1];
            }
        }
    }
    return dp[0][0];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ and $m$ are the lengths of the string and pattern, respectively. This is because we fill in a 2D table of size $n \times m$.
> - **Space Complexity:** $O(n \cdot m)$ for the 2D table.
> - **Optimality proof:** This is optimal because we solve each subproblem exactly once and store its result, avoiding redundant computation and achieving a linear time complexity in terms of the input sizes.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming for solving problems with overlapping subproblems.
- Problem-solving patterns identified: Breaking down complex string matching into smaller subproblems and solving them efficiently.
- Optimization techniques learned: Using a 2D table to store results of subproblems and avoid redundant computation.
- Similar problems to practice: Other string matching problems, such as those involving different types of wildcards or regular expression patterns.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect handling of edge cases, such as empty strings or patterns, and not properly initializing the dynamic programming table.
- Edge cases to watch for: Patterns starting with `*`, empty patterns, and patterns that are longer than the string.
- Performance pitfalls: Not using dynamic programming, leading to exponential time complexity.
- Testing considerations: Thoroughly testing with various inputs, including edge cases, to ensure correctness.