## Delete Characters to Make Fancy String
**Problem Link:** https://leetcode.com/problems/delete-characters-to-make-fancy-string/description

**Problem Statement:**
- Input format and constraints: Given two strings `s` and `t`, find the length of the longest subsequence of `s` that is a subsequence of `t`.
- Expected output format: The length of the longest subsequence.
- Key requirements and edge cases to consider: `s` and `t` are non-empty and consist of lowercase English letters.
- Example test cases with explanations:
  - Example 1: Input: `s = "aaa", t = "aa"` Output: `2` Explanation: The longest subsequence of `s` that is a subsequence of `t` is `"aa"`.
  - Example 2: Input: `s = "abc", t = "abc"` Output: `3` Explanation: The longest subsequence of `s` that is a subsequence of `t` is `"abc"`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible subsequences of `s` and check if they are a subsequence of `t`.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsequences of `s`.
  2. For each subsequence, check if it is a subsequence of `t`.
  3. Keep track of the longest subsequence that is a subsequence of `t`.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible solutions.

```cpp
class Solution {
public:
    int longestCommonSubsequence(string s, string t) {
        int m = s.size();
        int n = t.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s[i - 1] == t[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        
        return dp[m][n];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$ where $m$ and $n$ are the lengths of `s` and `t`, respectively.
> - **Space Complexity:** $O(m \cdot n)$ for the `dp` array.
> - **Why these complexities occur:** The time complexity is due to the nested loops that fill up the `dp` array, and the space complexity is due to the size of the `dp` array.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Use dynamic programming to store the lengths of the longest common subsequences of substrings of `s` and `t`.
- Detailed breakdown of the approach:
  1. Create a 2D array `dp` where `dp[i][j]` stores the length of the longest common subsequence of the first `i` characters of `s` and the first `j` characters of `t`.
  2. Fill up the `dp` array using the recurrence relation: if `s[i - 1]` equals `t[j - 1]`, then `dp[i][j] = dp[i - 1][j - 1] + 1`; otherwise, `dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])`.
- Proof of optimality: This approach has a time complexity of $O(m \cdot n)$, which is optimal because we need to consider all pairs of characters in `s` and `t`.

```cpp
class Solution {
public:
    int longestCommonSubsequence(string s, string t) {
        int m = s.size();
        int n = t.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s[i - 1] == t[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        
        return dp[m][n];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$ where $m$ and $n$ are the lengths of `s` and `t`, respectively.
> - **Space Complexity:** $O(m \cdot n)$ for the `dp` array.
> - **Optimality proof:** This approach has a time complexity of $O(m \cdot n)$, which is optimal because we need to consider all pairs of characters in `s` and `t`.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, longest common subsequence.
- Problem-solving patterns identified: Breaking down a problem into smaller subproblems, using a 2D array to store the results of subproblems.
- Optimization techniques learned: Using dynamic programming to avoid redundant computation.
- Similar problems to practice: Longest increasing subsequence, shortest path in a graph.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect initialization of the `dp` array, incorrect recurrence relation.
- Edge cases to watch for: Empty strings, strings with different lengths.
- Performance pitfalls: Using a naive approach that has a high time complexity.
- Testing considerations: Test the function with different input strings, including edge cases.