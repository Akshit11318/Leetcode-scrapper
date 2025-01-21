## Count Palindromic Subsequences

**Problem Link:** https://leetcode.com/problems/count-palindromic-subsequences/description

**Problem Statement:**
- Input format and constraints: Given a string `s`, return the number of different non-empty **palindromic subsequences** in `s`. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. A sequence is palindromic if it reads the same backward as forward.
- Expected output format: The number of different non-empty palindromic subsequences.
- Key requirements and edge cases to consider: Handle strings with repeating characters, empty strings, and single-character strings.
- Example test cases with explanations: 
    - For `s = "abc"`, the answer is `6` because all possible subsequences are "a", "b", "c", "aa", "bb", "cc".
    - For `s = "aaa"`, the answer is `6` because all possible subsequences are "a", "aa", "aaa".

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subsequences and check if each one is palindromic.
- Step-by-step breakdown of the solution:
    1. Generate all possible subsequences of the input string.
    2. Check each subsequence to see if it is palindromic.
    3. Count the number of unique palindromic subsequences.
- Why this approach comes to mind first: It's a straightforward, brute-force approach that checks every possible subsequence.

```cpp
class Solution {
public:
    int countPalindromicSubsequence(string s) {
        unordered_set<string> palindromes;
        int n = s.length();
        
        for (int mask = 1; mask < (1 << n); mask++) {
            string sub;
            for (int i = 0; i < n; i++) {
                if (mask & (1 << i)) {
                    sub += s[i];
                }
            }
            if (isPalindrome(sub)) {
                palindromes.insert(sub);
            }
        }
        return palindromes.size();
    }
    
    bool isPalindrome(string s) {
        int left = 0, right = s.length() - 1;
        while (left < right) {
            if (s[left] != s[right]) return false;
            left++; right--;
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n * n)$ where $n$ is the length of the string. This is because we generate all possible subsequences ($2^n$) and for each, we check if it's palindromic, which takes $O(n)$ time.
> - **Space Complexity:** $O(2^n * n)$ for storing all unique palindromic subsequences in the set.
> - **Why these complexities occur:** The exponential time complexity comes from generating all possible subsequences, and the space complexity comes from storing unique subsequences.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use dynamic programming to count the number of palindromic subsequences. This approach is more efficient because it avoids the overhead of generating all subsequences and checking if they are palindromic.
- Detailed breakdown of the approach:
    1. Create a 2D array `dp` where `dp[i][j]` represents the number of palindromic subsequences in the substring `s[i..j]`.
    2. Initialize `dp[i][i] = 1` for all `i`, since a single character is always a palindrome.
    3. For substrings of length 2, `dp[i][i+1] = 1` if `s[i] == s[i+1]`, otherwise `dp[i][i+1] = 2`.
    4. For longer substrings, `dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1] + (s[i] == s[j] ? 1 : 0)`.
- Proof of optimality: This dynamic programming approach has a polynomial time complexity, which is optimal for this problem.
- Why further optimization is impossible: The problem inherently requires considering all characters in the string, making a polynomial time complexity the best achievable.

```cpp
class Solution {
public:
    int countPalindromicSubsequence(string s) {
        int n = s.length();
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        // Initialize dp[i][i] = 1
        for (int i = 0; i < n; i++) {
            dp[i][i] = 1;
        }
        
        // For substrings of length 2
        for (int i = 0; i < n - 1; i++) {
            if (s[i] == s[i+1]) {
                dp[i][i+1] = 3;
            } else {
                dp[i][i+1] = 2;
            }
        }
        
        // For longer substrings
        for (int length = 3; length <= n; length++) {
            for (int i = 0; i <= n - length; i++) {
                int j = i + length - 1;
                dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1];
                if (s[i] == s[j]) {
                    dp[i][j] += 1;
                }
            }
        }
        
        return dp[0][n-1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the length of the string.
> - **Space Complexity:** $O(n^2)$ for the 2D `dp` array.
> - **Optimality proof:** The dynamic programming approach ensures that we consider all possible palindromic subsequences exactly once, making it optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, palindrome checking.
- Problem-solving patterns identified: Breaking down problems into smaller subproblems and using dynamic programming to solve them efficiently.
- Optimization techniques learned: Using dynamic programming to avoid redundant computation and reduce time complexity.
- Similar problems to practice: Other dynamic programming problems, such as the Longest Common Subsequence problem.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect initialization of the `dp` array, incorrect update of `dp` values.
- Edge cases to watch for: Handling empty strings, single-character strings, and strings with repeating characters.
- Performance pitfalls: Using a brute-force approach that generates all possible subsequences, which can lead to exponential time complexity.
- Testing considerations: Thoroughly testing the solution with different input strings, including edge cases.