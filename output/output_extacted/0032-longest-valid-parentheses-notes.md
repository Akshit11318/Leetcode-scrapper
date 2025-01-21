## Longest Valid Parentheses

**Problem Link:** [https://leetcode.com/problems/longest-valid-parentheses/description](https://leetcode.com/problems/longest-valid-parentheses/description)

**Problem Statement:**
- Input: a string `s` containing only parentheses `(` and `)`.
- Constraints: `1 <= s.length <= 1000`.
- Expected output: the length of the longest valid (i.e., properly nested) parentheses substring.
- Key requirements and edge cases:
  - A valid parentheses substring is one where every open parenthesis can be matched with a corresponding close parenthesis.
  - Consider edge cases like empty strings, strings with only one type of parenthesis, and strings with balanced but not nested parentheses.
- Example test cases:
  - Input: `"(()"` - Output: `2` (Explanation: the longest valid parentheses substring is `"()"`).
  - Input: `")()())"` - Output: `4` (Explanation: the longest valid parentheses substring is `"()()"`).

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to check every possible substring of `s` to see if it's a valid parentheses sequence.
- This involves iterating over all substrings, then for each substring, checking if it's valid by ensuring every open parenthesis has a corresponding close parenthesis.
- Why this approach comes to mind first: it's straightforward and ensures we consider all possibilities.

```cpp
int longestValidParentheses(string s) {
    int maxLength = 0;
    for (int i = 0; i < s.length(); i++) {
        for (int j = i + 1; j <= s.length(); j++) {
            string substr = s.substr(i, j - i);
            if (isValid(substr)) {
                maxLength = max(maxLength, (int)substr.length());
            }
        }
    }
    return maxLength;
}

bool isValid(string s) {
    stack<char> st;
    for (char c : s) {
        if (c == '(') st.push(c);
        else if (c == ')' && !st.empty()) st.pop();
        else return false;
    }
    return st.empty();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of `s`. This is because for each of the $O(n^2)$ substrings, we perform a validation check that takes $O(n)$ time.
> - **Space Complexity:** $O(n)$, due to the use of a stack in the `isValid` function.
> - **Why these complexities occur:** The nested loops over the string generate all possible substrings, and for each, we perform a linear scan to check validity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a dynamic programming (DP) approach to keep track of the length of the longest valid parentheses ending at each position.
- We maintain an array `dp` where `dp[i]` is the length of the longest valid parentheses substring ending at index `i`.
- We iterate through the string once, updating `dp[i]` based on whether the current character is an open or close parenthesis and the state of the previous characters.
- Proof of optimality: this approach ensures we consider all possible valid substrings exactly once, leading to linear time complexity.

```cpp
int longestValidParentheses(string s) {
    int n = s.length();
    vector<int> dp(n, 0);
    int maxLength = 0;
    for (int i = 1; i < n; i++) {
        if (s[i] == ')') {
            if (s[i - 1] == '(') {
                dp[i] = (i >= 2 ? dp[i - 2] : 0) + 2;
            } else if (i - dp[i - 1] > 0 && s[i - dp[i - 1] - 1] == '(') {
                dp[i] = dp[i - 1] + ((i - dp[i - 1]) >= 2 ? dp[i - dp[i - 1] - 2] : 0) + 2;
            }
            maxLength = max(maxLength, dp[i]);
        }
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `s`, because we make a single pass through the string.
> - **Space Complexity:** $O(n)$, for the `dp` array.
> - **Optimality proof:** This approach is optimal because it processes the input string in linear time, avoiding the redundant computations of the brute force approach.

---

### Final Notes

**Learning Points:**
- The importance of dynamic programming in solving string problems involving subsequences or substrings.
- How to recognize and optimize away brute force solutions by identifying patterns and applying algorithmic techniques.
- The value of considering edge cases and constraints in problem-solving.

**Mistakes to Avoid:**
- Overlooking the possibility of using dynamic programming for string problems.
- Failing to consider edge cases, such as empty strings or strings with only one type of parenthesis.
- Not optimizing the solution for time complexity, leading to inefficient algorithms.