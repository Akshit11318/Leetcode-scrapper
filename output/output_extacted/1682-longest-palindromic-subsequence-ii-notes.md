## Longest Palindromic Subsequence II
**Problem Link:** https://leetcode.com/problems/longest-palindromic-subsequence-ii/description

**Problem Statement:**
- Input format: A string `s` of length `n`.
- Constraints: `1 <= n <= 1000`.
- Expected output format: The length of the longest palindromic subsequence of `s`.
- Key requirements and edge cases to consider: The input string may contain duplicate characters, and the longest palindromic subsequence may not be unique.
- Example test cases with explanations:
  - Input: `s = "bbbab"` Output: `4`
  - Input: `s = "cbbd"` Output: `2`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subsequences of the input string and check if each one is a palindrome.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsequences of the input string using a recursive approach or bit manipulation.
  2. For each subsequence, check if it is a palindrome by comparing characters from the start and end.
  3. Keep track of the longest palindromic subsequence found so far.
- Why this approach comes to mind first: It is a straightforward and intuitive solution that checks all possible subsequences.

```cpp
class Solution {
public:
    int longestPalindromicSubsequence(string s) {
        int n = s.length();
        int maxLen = 0;
        for (int mask = 0; mask < (1 << n); mask++) {
            string sub = "";
            for (int i = 0; i < n; i++) {
                if (mask & (1 << i)) {
                    sub += s[i];
                }
            }
            if (isPalindrome(sub)) {
                maxLen = max(maxLen, (int)sub.length());
            }
        }
        return maxLen;
    }

    bool isPalindrome(string s) {
        int left = 0, right = s.length() - 1;
        while (left < right) {
            if (s[left] != s[right]) {
                return false;
            }
            left++, right--;
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input string. This is because we generate all possible subsequences of the input string, and for each subsequence, we check if it is a palindrome in $O(n)$ time.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we need to store the current subsequence being processed.
> - **Why these complexities occur:** The brute force approach has an exponential time complexity because it generates all possible subsequences of the input string. The space complexity is linear because we only need to store the current subsequence being processed.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to store the lengths of the longest palindromic subsequences of subproblems.
- Detailed breakdown of the approach:
  1. Create a 2D table `dp` of size `n x n`, where `dp[i][j]` represents the length of the longest palindromic subsequence of the subproblem `s[i..j]`.
  2. Initialize the table by setting `dp[i][i] = 1` for all `i`, since a single character is always a palindrome of length 1.
  3. Fill in the table in a bottom-up manner by considering all possible subsequences of the input string.
  4. For each subproblem `s[i..j]`, if `s[i] == s[j]`, then `dp[i][j] = dp[i+1][j-1] + 2`, since we can extend the palindrome by adding the characters `s[i]` and `s[j]`. Otherwise, `dp[i][j] = max(dp[i+1][j], dp[i][j-1])`, since we can either ignore the character `s[i]` or `s[j]`.
- Proof of optimality: The dynamic programming approach ensures that we only consider each subproblem once, and we store the result of each subproblem in the table to avoid redundant computation.

```cpp
class Solution {
public:
    int longestPalindromicSubsequence(string s) {
        int n = s.length();
        vector<vector<int>> dp(n, vector<int>(n, 0));
        for (int i = 0; i < n; i++) {
            dp[i][i] = 1;
        }
        for (int len = 2; len <= n; len++) {
            for (int i = 0; i < n - len + 1; i++) {
                int j = i + len - 1;
                if (s[i] == s[j]) {
                    dp[i][j] = (len == 2) ? 2 : dp[i+1][j-1] + 2;
                } else {
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1]);
                }
            }
        }
        return dp[0][n-1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input string. This is because we fill in the 2D table `dp` in a bottom-up manner.
> - **Space Complexity:** $O(n^2)$, where $n$ is the length of the input string. This is because we need to store the 2D table `dp`.
> - **Optimality proof:** The dynamic programming approach ensures that we only consider each subproblem once, and we store the result of each subproblem in the table to avoid redundant computation. This results in a time complexity of $O(n^2)$, which is optimal for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, memoization.
- Problem-solving patterns identified: Breaking down a problem into smaller subproblems, storing the results of subproblems to avoid redundant computation.
- Optimization techniques learned: Using a 2D table to store the lengths of the longest palindromic subsequences of subproblems.
- Similar problems to practice: Longest common subsequence, shortest common supersequence.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize the table, incorrect indexing.
- Edge cases to watch for: Empty input string, input string with a single character.
- Performance pitfalls: Using a brute force approach, not storing the results of subproblems.
- Testing considerations: Testing with different input sizes, testing with different types of input strings (e.g., strings with duplicate characters, strings with no duplicate characters).