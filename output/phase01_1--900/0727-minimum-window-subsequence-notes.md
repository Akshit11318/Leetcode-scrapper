## Minimum Window Subsequence

**Problem Link:** https://leetcode.com/problems/minimum-window-subsequence/description

**Problem Statement:**
- Given two sequences `s1` and `s2`, find the length of the shortest subsequence in `s1` that contains `s2` as a subsequence.
- Input: Two strings `s1` and `s2`.
- Expected Output: The length of the minimum window subsequence.
- Key requirements and edge cases to consider:
  - Empty strings.
  - `s2` is longer than `s1`.
  - `s1` and `s2` have no common characters.
- Example test cases:
  - `s1 = "abcde", s2 = "ace"`: The minimum window is `"ace"`.
  - `s1 = "abc", s2 = "bca"`: The minimum window is `"abc"`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking all possible subsequences of `s1` to see if they contain `s2`.
- Step-by-step breakdown:
  1. Generate all possible subsequences of `s1`.
  2. For each subsequence, check if it contains `s2` as a subsequence.
  3. Keep track of the shortest subsequence that contains `s2`.
- Why this approach comes to mind first: It's a straightforward, exhaustive approach to ensure we don't miss any possible subsequences.

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int minWindowSubsequence(string s1, string s2) {
    int len1 = s1.length(), len2 = s2.length();
    vector<vector<int>> dp(len1 + 1, vector<int>(len2 + 1, -1));
    
    // Base case: If s2 is empty, return 0
    for (int i = 0; i <= len1; i++) {
        dp[i][0] = 0;
    }
    
    for (int i = 1; i <= len1; i++) {
        for (int j = 1; j <= len2; j++) {
            if (s1[i - 1] == s2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }
    
    int minLen = INT_MAX;
    for (int i = 1; i <= len1; i++) {
        if (dp[i][len2] != -1) {
            minLen = min(minLen, i - dp[i][len2] + 1);
        }
    }
    
    return minLen == INT_MAX ? -1 : minLen;
}

int main() {
    string s1 = "abcde", s2 = "ace";
    cout << "Minimum window subsequence length: " << minWindowSubsequence(s1, s2) << endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ and $m$ are the lengths of `s1` and `s2`, respectively, because we're using a dynamic programming approach to fill up a 2D table of size $n \times m$.
> - **Space Complexity:** $O(n \cdot m)$, for the same reason as the time complexity.
> - **Why these complexities occur:** The dynamic programming approach requires us to fill up a table of size $n \times m$, resulting in $O(n \cdot m)$ time and space complexities.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is using dynamic programming to find the minimum window subsequence.
- Detailed breakdown of the approach:
  1. Create a 2D table `dp` where `dp[i][j]` represents the length of the minimum window subsequence ending at index `i` in `s1` that contains the first `j` characters of `s2`.
  2. Fill up the `dp` table by iterating through `s1` and `s2`.
  3. Keep track of the minimum length of the window subsequence.
- Proof of optimality: This approach is optimal because it ensures that we consider all possible subsequences of `s1` that contain `s2` and returns the shortest one.

```cpp
int minWindowSubsequence(string s1, string s2) {
    int len1 = s1.length(), len2 = s2.length();
    vector<vector<int>> dp(len1 + 1, vector<int>(len2 + 1, INT_MAX));
    
    dp[0][0] = 0;
    for (int i = 1; i <= len1; i++) {
        dp[i][0] = 0;
    }
    
    for (int i = 1; i <= len1; i++) {
        for (int j = 1; j <= len2; j++) {
            if (s1[i - 1] == s2[j - 1]) {
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1);
            }
            dp[i][j] = min(dp[i][j], dp[i - 1][j]);
        }
    }
    
    return dp[len1][len2] == INT_MAX ? -1 : dp[len1][len2];
}

int main() {
    string s1 = "abcde", s2 = "ace";
    cout << "Minimum window subsequence length: " << minWindowSubsequence(s1, s2) << endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ and $m$ are the lengths of `s1` and `s2`, respectively.
> - **Space Complexity:** $O(n \cdot m)$, for the same reason as the time complexity.
> - **Optimality proof:** This approach is optimal because it ensures that we consider all possible subsequences of `s1` that contain `s2` and returns the shortest one.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, minimum window subsequence.
- Problem-solving patterns identified: Using a 2D table to keep track of the minimum window subsequence.
- Optimization techniques learned: Using dynamic programming to reduce the time complexity.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` table correctly, not handling edge cases.
- Edge cases to watch for: Empty strings, `s2` is longer than `s1`.
- Performance pitfalls: Not using dynamic programming, resulting in a high time complexity.
- Testing considerations: Test the function with different inputs, including edge cases.