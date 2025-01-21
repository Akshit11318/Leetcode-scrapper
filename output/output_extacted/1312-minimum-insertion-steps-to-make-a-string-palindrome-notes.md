## Minimum Insertion Steps to Make a String Palindrome

**Problem Link:** https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/description

**Problem Statement:**
- Input format and constraints: Given a string `s`, find the minimum number of characters that need to be inserted to make `s` a palindrome.
- Expected output format: The minimum number of characters to insert.
- Key requirements and edge cases to consider: The input string `s` can be empty, and the solution should handle this case. The string can also be a single character, which is already a palindrome.
- Example test cases with explanations:
  - Input: `s = "zzazz"`
    Output: `0`
    Explanation: `s` is already a palindrome.
  - Input: `s = "mbadm"`
    Output: `2`
    Explanation: Insert "b" and "a" to make `s` a palindrome.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible insertions of characters to make the string a palindrome and count the minimum number of insertions required.
- Step-by-step breakdown of the solution:
  1. Start with an empty string and the input string `s`.
  2. For each character in `s`, try inserting all possible characters before it.
  3. Check if the resulting string is a palindrome.
  4. If it is, update the minimum number of insertions required.
- Why this approach comes to mind first: It's a straightforward approach that tries all possibilities.

```cpp
int minInsertions(string s) {
    int n = s.length();
    int ans = INT_MAX;
    // Generate all possible strings by inserting characters
    for (int mask = 0; mask < (1 << (n * 26)); mask++) {
        string t = s;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 26; j++) {
                if ((mask & (1 << (i * 26 + j))) != 0) {
                    t.insert(i, 1, 'a' + j);
                }
            }
        }
        // Check if the resulting string is a palindrome
        if (isPalindrome(t)) {
            ans = min(ans, t.length() - n);
        }
    }
    return ans;
}

bool isPalindrome(string s) {
    int i = 0, j = s.length() - 1;
    while (i < j) {
        if (s[i] != s[j]) return false;
        i++, j--;
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{26n} \cdot n)$, where $n$ is the length of the string. This is because we generate all possible strings by inserting characters, and for each string, we check if it's a palindrome.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string. This is because we need to store the resulting string after inserting characters.
> - **Why these complexities occur:** The time complexity is high because we try all possible insertions of characters, and the space complexity is moderate because we need to store the resulting string.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use dynamic programming to find the longest common subsequence between the input string and its reverse. The minimum number of insertions required is the difference between the length of the input string and the length of the longest common subsequence.
- Detailed breakdown of the approach:
  1. Reverse the input string `s` to get `t`.
  2. Use dynamic programming to find the longest common subsequence between `s` and `t`.
  3. The minimum number of insertions required is the difference between the length of `s` and the length of the longest common subsequence.
- Proof of optimality: This approach is optimal because it uses dynamic programming to find the longest common subsequence, which is the most efficient way to solve this problem.
- Why further optimization is impossible: This approach has a time complexity of $O(n^2)$, which is the best possible time complexity for this problem.

```cpp
int minInsertions(string s) {
    int n = s.length();
    string t = s;
    reverse(t.begin(), t.end());
    vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0));
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (s[i - 1] == t[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    return n - dp[n][n];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the string. This is because we use dynamic programming to find the longest common subsequence.
> - **Space Complexity:** $O(n^2)$, where $n$ is the length of the string. This is because we need to store the dynamic programming table.
> - **Optimality proof:** This approach is optimal because it uses dynamic programming to find the longest common subsequence, which is the most efficient way to solve this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, longest common subsequence.
- Problem-solving patterns identified: Using dynamic programming to solve problems that have overlapping subproblems.
- Optimization techniques learned: Using dynamic programming to reduce the time complexity of a problem.
- Similar problems to practice: Longest common subsequence, edit distance.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the dynamic programming table correctly, not handling edge cases correctly.
- Edge cases to watch for: Empty input string, single-character input string.
- Performance pitfalls: Using a brute force approach that has a high time complexity.
- Testing considerations: Test the solution with different input strings, including edge cases.