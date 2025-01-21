## Longest Common Subsequence

**Problem Link:** https://leetcode.com/problems/longest-common-subsequence/description

**Problem Statement:**
- Input format and constraints: Two strings `text1` and `text2` are given, and the goal is to find the length of their `longest common subsequence`.
- Expected output format: The length of the longest common subsequence.
- Key requirements and edge cases to consider: The input strings can be empty, and the longest common subsequence can be empty as well.
- Example test cases with explanations:
  - If `text1 = "abc"` and `text2 = "abc"`, the longest common subsequence is `"abc"` with a length of `3`.
  - If `text1 = "abc"` and `text2 = "def"`, the longest common subsequence is an empty string with a length of `0`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subsequences of both strings and compare them to find the longest common one.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsequences of `text1`.
  2. Generate all possible subsequences of `text2`.
  3. Compare each subsequence of `text1` with each subsequence of `text2`.
  4. Keep track of the longest common subsequence found.
- Why this approach comes to mind first: It is a straightforward approach that checks all possibilities.

```cpp
int longestCommonSubsequenceBrute(string text1, string text2) {
    int maxLen = 0;
    for (int mask1 = 0; mask1 < (1 << text1.size()); mask1++) {
        string sub1;
        for (int i = 0; i < text1.size(); i++) {
            if ((mask1 & (1 << i)) != 0) {
                sub1 += text1[i];
            }
        }
        for (int mask2 = 0; mask2 < (1 << text2.size()); mask2++) {
            string sub2;
            for (int i = 0; i < text2.size(); i++) {
                if ((mask2 & (1 << i)) != 0) {
                    sub2 += text2[i];
                }
            }
            if (sub1 == sub2) {
                maxLen = max(maxLen, (int)sub1.size());
            }
        }
    }
    return maxLen;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{n + m} \cdot min(n, m))$ where $n$ and $m$ are the lengths of `text1` and `text2` respectively. This is because we generate all possible subsequences of both strings and compare them.
> - **Space Complexity:** $O(n + m)$ for storing the subsequences.
> - **Why these complexities occur:** The brute force approach checks all possible subsequences, leading to exponential time complexity. The space complexity is linear due to the storage of subsequences.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use dynamic programming to store the lengths of common subsequences.
- Detailed breakdown of the approach:
  1. Create a 2D array `dp` where `dp[i][j]` represents the length of the longest common subsequence of the first `i` characters of `text1` and the first `j` characters of `text2`.
  2. Initialize the first row and column of `dp` to `0`.
  3. Fill in the rest of `dp` based on whether the current characters in `text1` and `text2` match or not.
- Proof of optimality: This approach has a time complexity of $O(n \cdot m)$, which is optimal because we must at least read the input strings.

```cpp
int longestCommonSubsequenceOptimal(string text1, string text2) {
    int n = text1.size();
    int m = text2.size();
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (text1[i - 1] == text2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    return dp[n][m];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ and $m$ are the lengths of `text1` and `text2` respectively.
> - **Space Complexity:** $O(n \cdot m)$ for the `dp` array.
> - **Optimality proof:** This approach is optimal because it uses dynamic programming to store and reuse the lengths of common subsequences, avoiding redundant computations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, string comparison.
- Problem-solving patterns identified: Breaking down the problem into smaller subproblems and using memoization to store intermediate results.
- Optimization techniques learned: Avoiding redundant computations by storing and reusing intermediate results.
- Similar problems to practice: Longest increasing subsequence, shortest common supersequence.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect initialization of the `dp` array, incorrect updating of the `dp` array.
- Edge cases to watch for: Empty input strings, strings with different lengths.
- Performance pitfalls: Using a brute force approach with exponential time complexity.
- Testing considerations: Test the function with different input strings, including edge cases.