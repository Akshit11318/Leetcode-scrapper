## Minimum ASCII Delete Sum for Two Strings
**Problem Link:** https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description

**Problem Statement:**
- Given two strings `s1` and `s2`, find the minimum ASCII delete sum for these two strings.
- The ASCII delete sum is the sum of the ASCII values of the characters that need to be deleted to make the two strings equal.
- The strings only contain lowercase letters.
- The input strings can be empty.
- The expected output is the minimum ASCII delete sum.

**Example Test Cases:**
- `s1 = "sea", s2 = "eat"`: The minimum ASCII delete sum is `231` (`'s' + 'a' + 't'`).
- `s1 = "delete", s2 = "leet"`: The minimum ASCII delete sum is `403` (`'d' + 'e' + 'e' + 'l' + 'e' + 't'`).

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible subsequences of both strings and compare them.
- We then calculate the ASCII delete sum for each pair of subsequences and find the minimum sum.
- This approach comes to mind first because it involves checking all possible combinations, which guarantees finding the minimum sum.

```cpp
int minimumDeleteSum(string s1, string s2) {
    int result = INT_MAX;
    int m = s1.size();
    int n = s2.size();
    for (int mask1 = 0; mask1 < (1 << m); mask1++) {
        for (int mask2 = 0; mask2 < (1 << n); mask2++) {
            string sub1 = "";
            string sub2 = "";
            for (int i = 0; i < m; i++) {
                if ((mask1 & (1 << i)) != 0) {
                    sub1 += s1[i];
                }
            }
            for (int i = 0; i < n; i++) {
                if ((mask2 & (1 << i)) != 0) {
                    sub2 += s2[i];
                }
            }
            if (sub1 == sub2) {
                int sum = 0;
                for (int i = 0; i < m; i++) {
                    if ((mask1 & (1 << i)) == 0) {
                        sum += s1[i];
                    }
                }
                for (int i = 0; i < n; i++) {
                    if ((mask2 & (1 << i)) == 0) {
                        sum += s2[i];
                    }
                }
                result = min(result, sum);
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^m \cdot 2^n \cdot (m + n))$ where $m$ and $n$ are the lengths of `s1` and `s2`, respectively. This is because we generate all possible subsequences of both strings and compare them.
> - **Space Complexity:** $O(m + n)$ for storing the subsequences.
> - **Why these complexities occur:** The brute force approach involves generating all possible combinations of subsequences, which leads to exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use dynamic programming to find the longest common subsequence (LCS) between `s1` and `s2`.
- We then calculate the ASCII delete sum by summing the ASCII values of the characters that are not part of the LCS.
- This approach is optimal because it avoids the exponential time complexity of the brute force approach.

```cpp
int minimumDeleteSum(string s1, string s2) {
    int m = s1.size();
    int n = s2.size();
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (s1[i - 1] == s2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + s1[i - 1];
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    int sum = 0;
    for (int i = 0; i < m; i++) {
        sum += s1[i];
    }
    for (int i = 0; i < n; i++) {
        sum += s2[i];
    }
    return sum - 2 * dp[m][n];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$ where $m$ and $n$ are the lengths of `s1` and `s2`, respectively. This is because we use a dynamic programming table to store the intermediate results.
> - **Space Complexity:** $O(m \cdot n)$ for the dynamic programming table.
> - **Optimality proof:** This approach is optimal because it uses dynamic programming to find the LCS, which has a polynomial time complexity. The ASCII delete sum is then calculated in linear time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, longest common subsequence.
- Problem-solving patterns identified: finding the minimum ASCII delete sum by using dynamic programming to find the LCS.
- Optimization techniques learned: avoiding exponential time complexity by using dynamic programming.

**Mistakes to Avoid:**
- Common implementation errors: not initializing the dynamic programming table correctly, not handling the base cases correctly.
- Edge cases to watch for: empty strings, strings with different lengths.
- Performance pitfalls: using the brute force approach for large inputs.
- Testing considerations: testing the function with different inputs, including edge cases.