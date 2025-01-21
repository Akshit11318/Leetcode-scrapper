## Delete Operation for Two Strings

**Problem Link:** https://leetcode.com/problems/delete-operation-for-two-strings/description

**Problem Statement:**
- Given two strings `word1` and `word2`, return the minimum number of steps to make `word1` and `word2` the same.
- In one step, you can delete exactly one character in either string.
- Input format: Two strings `word1` and `word2`.
- Constraints: `1 <= word1.length, word2.length <= 500`.
- Expected output format: The minimum number of steps required to make `word1` and `word2` the same.
- Key requirements: The goal is to find the longest common subsequence (LCS) between `word1` and `word2` and then calculate the minimum number of deletions required to make both strings equal to this LCS.
- Example test cases:
  - `word1 = "sea", word2 = "eat"`: The LCS is `"ea"`. To make `word1` equal to `"ea"`, delete `"s"`. To make `word2` equal to `"ea"`, delete `"t"`. Thus, the minimum number of steps is `2`.
  - `word1 = "leetcode", word2 = "etco"`: The LCS is `"etc"`. To make `word1` equal to `"etc"`, delete `"l"`, `"o"`, `"d"`, and `"e"`. To make `word2` equal to `"etc"`, delete `"o"`. Thus, the minimum number of steps is `8`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves generating all possible subsequences of `word1` and `word2` and checking which one is the longest common subsequence.
- However, this approach is inefficient because it involves generating an exponential number of subsequences.

```cpp
class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.size(), n = word2.size();
        int count = 0;
        // Generate all possible subsequences of word1 and word2
        for (int mask = 1; mask < (1 << m); ++mask) {
            string sub1;
            for (int i = 0; i < m; ++i) {
                if ((mask & (1 << i))) {
                    sub1 += word1[i];
                }
            }
            for (int mask2 = 1; mask2 < (1 << n); ++mask2) {
                string sub2;
                for (int j = 0; j < n; ++j) {
                    if ((mask2 & (1 << j))) {
                        sub2 += word2[j];
                    }
                }
                // Check if sub1 is equal to sub2
                if (sub1 == sub2) {
                    count = max(count, (int)sub1.size());
                }
            }
        }
        return m + n - 2 * count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^m \times 2^n \times max(m, n))$ where $m$ and $n$ are the lengths of `word1` and `word2`, respectively. This is because we generate all possible subsequences of both strings and compare them.
> - **Space Complexity:** $O(max(m, n))$ for storing the subsequences.
> - **Why these complexities occur:** The brute force approach involves generating an exponential number of subsequences, leading to high time complexity. The space complexity is relatively low because we only need to store the current subsequences being compared.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use dynamic programming to find the longest common subsequence (LCS) between `word1` and `word2`.
- We create a 2D array `dp` where `dp[i][j]` represents the length of the LCS of the first `i` characters of `word1` and the first `j` characters of `word2`.
- We fill up the `dp` array in a bottom-up manner by comparing characters from `word1` and `word2`.
- Finally, we calculate the minimum number of steps required to make both strings equal to the LCS.

```cpp
class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.size(), n = word2.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (word1[i - 1] == word2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        return m + n - 2 * dp[m][n];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \times n)$ where $m$ and $n$ are the lengths of `word1` and `word2`, respectively. This is because we fill up the `dp` array in a bottom-up manner.
> - **Space Complexity:** $O(m \times n)$ for storing the `dp` array.
> - **Optimality proof:** This approach is optimal because it uses dynamic programming to find the LCS in a single pass, avoiding the exponential time complexity of the brute force approach.

---

### Final Notes

**Learning Points:**
- The importance of dynamic programming in solving string problems.
- How to find the longest common subsequence (LCS) between two strings using dynamic programming.
- The relationship between the LCS and the minimum number of steps required to make two strings equal.

**Mistakes to Avoid:**
- Using the brute force approach for large inputs, which can lead to exponential time complexity.
- Not considering the dynamic programming approach, which can significantly improve the time complexity.
- Not handling edge cases, such as empty strings or strings with different lengths.