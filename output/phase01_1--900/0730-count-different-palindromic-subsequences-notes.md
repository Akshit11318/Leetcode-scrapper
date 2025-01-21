## Count Different Palindromic Subsequences

**Problem Link:** https://leetcode.com/problems/count-different-palindromic-subsequences/description

**Problem Statement:**
- Input: A string `s` consisting of lowercase letters.
- Output: The number of different palindromic subsequences in `s`.
- Key requirements: A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.
- Edge cases: Empty string, single character string, strings with repeated characters.

**Example Test Cases:**
- Input: `"abc"`
  - Output: `8`
  - Explanation: The different palindromic subsequences are: `a`, `b`, `c`, `aa`, `bb`, `cc`, `aaa`, `abc` is not a palindrome.
- Input: `"aaa"`
  - Output: `3`
  - Explanation: The different palindromic subsequences are: `a`, `aa`, `aaa`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible subsequences of the input string and check if each one is a palindrome.
- We can use a recursive approach to generate all subsequences.

```cpp
int countPalindromicSubsequences(string s) {
    unordered_set<string> set;
    function<void(string, int)> dfs = [&](string sub, int start) {
        if (start == s.size()) {
            if (isPalindrome(sub)) {
                set.insert(sub);
            }
            return;
        }
        dfs(sub, start + 1); // skip current character
        dfs(sub + s[start], start + 1); // include current character
    };
    dfs("", 0);
    return set.size();
}

bool isPalindrome(string s) {
    int left = 0, right = s.size() - 1;
    while (left < right) {
        if (s[left] != s[right]) return false;
        left++, right--;
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input string. This is because we generate all possible subsequences and check if each one is a palindrome.
> - **Space Complexity:** $O(2^n)$, where $n$ is the length of the input string. This is because we store all unique palindromic subsequences in a set.
> - **Why these complexities occur:** The recursive approach generates all possible subsequences, resulting in exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- We can use dynamic programming to solve this problem. The idea is to build up a table where each cell `[i][j]` represents the number of different palindromic subsequences in the substring `s[i..j]`.
- We can fill up the table by considering two cases: when `s[i] == s[j]` and when `s[i] != s[j]`.
- When `s[i] == s[j]`, we can either include `s[i]` and `s[j]` in the subsequence or exclude them. If we include them, we need to consider all possible subsequences in the substring `s[i+1..j-1]`. If we exclude them, we can consider all possible subsequences in the substrings `s[i+1..j]` and `s[i..j-1]`.
- When `s[i] != s[j]`, we can only exclude `s[i]` or `s[j]` from the subsequence.

```cpp
int countPalindromicSubsequences(string s) {
    int n = s.size();
    vector<vector<int>> dp(n, vector<int>(n, 0));
    for (int i = 0; i < n; i++) {
        dp[i][i] = 1;
    }
    for (int length = 2; length <= n; length++) {
        for (int i = 0; i <= n - length; i++) {
            int j = i + length - 1;
            dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1];
            if (s[i] == s[j]) {
                dp[i][j] += dp[i + 1][j - 1] + 1;
            }
        }
    }
    return dp[0][n - 1];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input string. This is because we fill up a table of size $n \times n$.
> - **Space Complexity:** $O(n^2)$, where $n$ is the length of the input string. This is because we use a table of size $n \times n$ to store the number of different palindromic subsequences.
> - **Optimality proof:** The dynamic programming approach ensures that we consider all possible subsequences and count each one exactly once, resulting in the optimal solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, recursive approach.
- Problem-solving patterns identified: breaking down the problem into smaller subproblems, using a table to store intermediate results.
- Optimization techniques learned: using dynamic programming to avoid redundant computations.
- Similar problems to practice: count the number of different subsequences, count the number of different palindromic substrings.

**Mistakes to Avoid:**
- Common implementation errors: incorrect indexing, incorrect base cases.
- Edge cases to watch for: empty string, single character string, strings with repeated characters.
- Performance pitfalls: using a recursive approach without memoization, using a brute force approach.
- Testing considerations: test the function with different input strings, test the function with edge cases.