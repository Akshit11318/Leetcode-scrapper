## Maximum Score from Removing Substrings

**Problem Link:** https://leetcode.com/problems/maximum-score-from-removing-substrings/description

**Problem Statement:**
- Input: string `s`, strings `s1` and `s2`, and integers `x` and `y`
- Output: The maximum score that can be achieved by removing substrings `s1` and `s2` from `s`
- Key requirements: 
  - Removing `s1` yields a score of `x`
  - Removing `s2` yields a score of `y`
  - The goal is to maximize the total score
- Edge cases: 
  - Overlapping occurrences of `s1` and `s2`
  - Non-overlapping occurrences of `s1` and `s2`
  - No occurrences of `s1` and `s2`

### Brute Force Approach

**Explanation:**
- The initial thought process is to check all possible substrings of `s` to see if they match `s1` or `s2`.
- We will then remove the matching substrings one by one and keep track of the maximum score.
- This approach comes to mind first because it is straightforward and easy to understand.

```cpp
int maximumScore(string s, string s1, string s2, int x, int y) {
    int n = s.size();
    int res = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j <= n; j++) {
            string substr = s.substr(i, j - i);
            if (substr == s1) {
                res = max(res, x + maximumScore(s.substr(0, i) + s.substr(j), s1, s2, x, y));
            } else if (substr == s2) {
                res = max(res, y + maximumScore(s.substr(0, i) + s.substr(j), s1, s2, x, y));
            }
        }
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n^2)$, where $n$ is the length of the string `s`. This is because we are generating all possible substrings of `s` and recursively calling the function for each substring.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we are using a recursive call stack to store the function calls.
> - **Why these complexities occur:** The brute force approach is inefficient because it generates all possible substrings of `s` and recursively calls the function for each substring, resulting in an exponential time complexity.

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a dynamic programming approach to store the maximum score for each prefix of `s`.
- We will iterate over `s` and check if the current substring matches `s1` or `s2`.
- If it matches, we will update the maximum score for the current prefix.
- This approach is optimal because it avoids the overhead of recursive function calls and uses a bottom-up dynamic programming approach to store the maximum score for each prefix.

```cpp
int maximumScore(string s, string s1, string s2, int x, int y) {
    int n = s.size();
    vector<int> dp(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        dp[i] = dp[i - 1];
        for (int j = 0; j < i; j++) {
            string substr = s.substr(j, i - j);
            if (substr == s1) {
                dp[i] = max(dp[i], dp[j] + x);
            } else if (substr == s2) {
                dp[i] = max(dp[i], dp[j] + y);
            }
        }
    }
    return dp[n];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the string `s`. This is because we are iterating over `s` and checking all possible substrings.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we are using a dynamic programming array to store the maximum score for each prefix.
> - **Optimality proof:** This approach is optimal because it uses a bottom-up dynamic programming approach to store the maximum score for each prefix, avoiding the overhead of recursive function calls.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, string matching
- Problem-solving patterns identified: using a bottom-up approach to store the maximum score for each prefix
- Optimization techniques learned: avoiding recursive function calls, using dynamic programming to store intermediate results
- Similar problems to practice: string matching, dynamic programming problems

**Mistakes to Avoid:**
- Common implementation errors: incorrect indexing, incorrect substring matching
- Edge cases to watch for: overlapping occurrences of `s1` and `s2`, non-overlapping occurrences of `s1` and `s2`
- Performance pitfalls: using recursive function calls, not using dynamic programming to store intermediate results
- Testing considerations: testing with different inputs, testing with edge cases