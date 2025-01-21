## Subsequence with the Minimum Score

**Problem Link:** https://leetcode.com/problems/subsequence-with-the-minimum-score/description

**Problem Statement:**
- Given two strings `s` and `t`, find the longest common subsequence of `s` and `t`, and then return the minimum possible score that can be achieved by removing characters from `s` and `t` to make them identical.
- The score of a string is defined as the sum of the ASCII values of its characters.
- The input strings `s` and `t` are non-empty and consist of lowercase English letters.
- The length of `s` is less than or equal to 1000, and the length of `t` is less than or equal to 1000.
- The expected output is the minimum possible score.

**Example Test Cases:**
- If `s = "sea"` and `t = "eat"`, the longest common subsequence is `"ea"`, and the minimum possible score is `9`.
- If `s = "delete"` and `t = "leet"`, the longest common subsequence is `"leet"`, and the minimum possible score is `100`.

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible subsequences of `s` and `t`, and then find the longest common subsequence among them.
- However, this approach is inefficient because it has a high time complexity.

```cpp
int minimumScore(string s, string t) {
    int m = s.size();
    int n = t.size();
    int res = INT_MAX;
    for (int mask = 0; mask < (1 << m); mask++) {
        string subseq;
        for (int i = 0; i < m; i++) {
            if ((mask & (1 << i)) != 0) {
                subseq += s[i];
            }
        }
        for (int mask2 = 0; mask2 < (1 << n); mask2++) {
            string subseq2;
            for (int i = 0; i < n; i++) {
                if ((mask2 & (1 << i)) != 0) {
                    subseq2 += t[i];
                }
            }
            if (subseq == subseq2) {
                int score = 0;
                for (int i = 0; i < m; i++) {
                    if ((mask & (1 << i)) == 0) {
                        score += s[i];
                    }
                }
                for (int i = 0; i < n; i++) {
                    if ((mask2 & (1 << i)) == 0) {
                        score += t[i];
                    }
                }
                res = min(res, score);
            }
        }
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^m \cdot 2^n \cdot (m + n))$, where $m$ and $n$ are the lengths of `s` and `t`, respectively.
> - **Space Complexity:** $O(m + n)$, where $m$ and $n$ are the lengths of `s` and `t`, respectively.
> - **Why these complexities occur:** The brute force approach generates all possible subsequences of `s` and `t`, which results in a high time complexity.

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use dynamic programming to find the longest common subsequence of `s` and `t`.
- We can use a 2D array `dp` to store the lengths of the longest common subsequences of the prefixes of `s` and `t`.
- We can then use another 2D array `score` to store the minimum possible scores for each prefix of `s` and `t`.

```cpp
int minimumScore(string s, string t) {
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
    int i = m;
    int j = n;
    int score = 0;
    while (i > 0 && j > 0) {
        if (s[i - 1] == t[j - 1]) {
            i--;
            j--;
        } else if (dp[i - 1][j] > dp[i][j - 1]) {
            score += s[i - 1];
            i--;
        } else {
            score += t[j - 1];
            j--;
        }
    }
    while (i > 0) {
        score += s[i - 1];
        i--;
    }
    while (j > 0) {
        score += t[j - 1];
        j--;
    }
    return score;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the lengths of `s` and `t`, respectively.
> - **Space Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the lengths of `s` and `t`, respectively.
> - **Optimality proof:** The optimal approach uses dynamic programming to find the longest common subsequence of `s` and `t`, which results in a much lower time complexity than the brute force approach.

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is dynamic programming.
- The problem-solving pattern identified is finding the longest common subsequence of two strings.
- The optimization technique learned is using dynamic programming to reduce the time complexity of the solution.
- Similar problems to practice include finding the longest common subsequence of two strings, finding the shortest common supersequence of two strings, and finding the edit distance between two strings.

**Mistakes to Avoid:**
- A common implementation error is not initializing the `dp` array correctly.
- An edge case to watch for is when `s` or `t` is empty.
- A performance pitfall is using a brute force approach instead of dynamic programming.
- A testing consideration is to test the solution with different inputs, including edge cases.