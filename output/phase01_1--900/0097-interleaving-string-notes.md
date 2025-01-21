## Interleaving String

**Problem Link:** https://leetcode.com/problems/interleaving-string/description

**Problem Statement:**
- Given three strings `s1`, `s2`, and `s3`, find if `s3` can be formed by interleaving `s1` and `s2`.
- The length of `s1` and `s2` must be less than or equal to the length of `s3`.
- The interleaving of two strings `s1` and `s2` is defined as containing all the characters of both `s1` and `s2` and these characters are in the same order in `s3` as they are in `s1` and `s2`.
- Expected output is `true` if `s3` can be formed by interleaving `s1` and `s2`, `false` otherwise.

**Example Test Cases:**
- `s1 = "aabcc"`, `s2 = "dbbca"`, `s3 = "aadbbcbcac"` -> `true`
- `s1 = "aabcc"`, `s2 = "dbbca"`, `s3 = "aadbbbaccc"` -> `false`
- `s1 = ""`, `s2 = ""`, `s3 = ""` -> `true`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves generating all possible combinations of `s1` and `s2` and checking if any of these combinations match `s3`.
- This can be achieved by using recursion to interleave the strings and then checking the resulting string.

```cpp
class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        if (s1.size() + s2.size() != s3.size()) return false;
        return helper(s1, s2, s3, 0, 0, 0);
    }
    
    bool helper(string s1, string s2, string s3, int i, int j, int k) {
        if (k == s3.size()) return true;
        
        bool match = false;
        if (i < s1.size() && s1[i] == s3[k]) {
            match = match || helper(s1, s2, s3, i + 1, j, k + 1);
        }
        if (j < s2.size() && s2[j] == s3[k]) {
            match = match || helper(s1, s2, s3, i, j + 1, k + 1);
        }
        
        return match;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{n + m})$, where $n$ and $m$ are the lengths of `s1` and `s2`, respectively. This is because in the worst case, the recursive function could branch out in two directions for each character in `s1` and `s2`.
> - **Space Complexity:** $O(n + m)$, which is the maximum depth of the recursion call stack.
> - **Why these complexities occur:** The recursive approach leads to exponential time complexity due to overlapping subproblems. The space complexity is linear due to the recursion stack.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use dynamic programming to store the results of subproblems and avoid redundant computation.
- A 2D DP table can be used to store whether the first `i` characters of `s1` and the first `j` characters of `s2` can interleave to form the first `i + j` characters of `s3`.

```cpp
class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        if (s1.size() + s2.size() != s3.size()) return false;
        int n = s1.size(), m = s2.size();
        vector<vector<bool>> dp(n + 1, vector<bool>(m + 1, false));
        
        dp[0][0] = true;
        for (int i = 1; i <= n; i++) {
            dp[i][0] = dp[i - 1][0] && s1[i - 1] == s3[i - 1];
        }
        for (int j = 1; j <= m; j++) {
            dp[0][j] = dp[0][j - 1] && s2[j - 1] == s3[j - 1];
        }
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                dp[i][j] = (dp[i - 1][j] && s1[i - 1] == s3[i + j - 1]) || (dp[i][j - 1] && s2[j - 1] == s3[i + j - 1]);
            }
        }
        
        return dp[n][m];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ and $m$ are the lengths of `s1` and `s2`, respectively.
> - **Space Complexity:** $O(n \cdot m)$, which is the size of the DP table.
> - **Optimality proof:** This is the optimal solution because it avoids redundant computation by storing the results of subproblems in a DP table. The time complexity is linear with respect to the input size, and the space complexity is also linear.

---

### Final Notes

**Learning Points:**
- The problem demonstrates the use of dynamic programming to solve problems with overlapping subproblems.
- The importance of choosing the correct data structure (in this case, a 2D DP table) to store the results of subproblems.
- The need to initialize the DP table correctly and fill it in a bottom-up manner.

**Mistakes to Avoid:**
- Not checking the base cases (e.g., `s1.size() + s2.size() != s3.size()`) before proceeding with the solution.
- Not initializing the DP table correctly (e.g., setting `dp[0][0] = true`).
- Not filling the DP table in a bottom-up manner, which can lead to incorrect results.