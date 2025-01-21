## Minimize String Length
**Problem Link:** https://leetcode.com/problems/minimize-string-length/description

**Problem Statement:**
- Input format and constraints: Given a string `s` containing lowercase letters, return the length of the longest substring that can be removed to make `s` a **palindrome**.
- Expected output format: The length of the longest substring that can be removed.
- Key requirements and edge cases to consider:
  - The input string only contains lowercase letters.
  - The string can be empty.
  - The string can already be a palindrome.
- Example test cases with explanations:
  - If `s = "ca"` (not a palindrome), the longest substring that can be removed is `"c"` or `"a"`, so the function should return `1`.
  - If `s = "caba"` (not a palindrome), the longest substring that can be removed is `"ba"`, so the function should return `2`.
  - If `s = "acba"` (already a palindrome), no characters need to be removed, so the function should return `0`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible substring of `s` to see if removing it would result in a palindrome.
- Step-by-step breakdown of the solution:
  1. Generate all possible substrings of `s`.
  2. For each substring, create a new string by removing the substring from `s`.
  3. Check if the new string is a palindrome.
  4. If it is, update the maximum length of the substring that can be removed.
- Why this approach comes to mind first: It's a straightforward, exhaustive search approach that guarantees finding the solution if one exists.

```cpp
#include <string>
using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0, right = s.size() - 1;
        while (left < right) {
            if (s[left] != s[right]) return false;
            left++; right--;
        }
        return true;
    }

    int minimumDeleteSum(string s) {
        int n = s.size();
        int maxLen = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                string newStr = s.substr(0, i) + s.substr(j + 1);
                if (isPalindrome(newStr)) {
                    maxLen = max(maxLen, j - i + 1);
                }
            }
        }
        return maxLen;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the string. The outer two loops generate all substrings ($O(n^2)$), and the `isPalindrome` check inside is $O(n)$.
> - **Space Complexity:** $O(n)$, as we are creating new strings of up to length $n$.
> - **Why these complexities occur:** The brute force approach involves exhaustive search and string manipulation, leading to high time and space complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking every possible substring, we can use dynamic programming to build up a table that stores whether each substring is a palindrome.
- Detailed breakdown of the approach:
  1. Create a 2D table `dp` where `dp[i][j]` is true if the substring from `i` to `j` is a palindrome.
  2. Fill the table in a bottom-up manner, starting with substrings of length 1 (which are always palindromes) and then considering substrings of length 2 and above.
  3. For substrings of length 2 and above, a substring is a palindrome if its first and last characters are the same and the substring in between is a palindrome.
- Proof of optimality: This approach ensures we consider all possible substrings exactly once, minimizing the time complexity.
- Why further optimization is impossible: This approach has a time complexity that is linear in the size of the input string squared, which is the minimum required to check all substrings.

```cpp
class Solution {
public:
    int minimumDeleteSum(string s) {
        int n = s.size();
        vector<vector<bool>> dp(n, vector<bool>(n, false));
        for (int i = 0; i < n; i++) dp[i][i] = true;
        for (int len = 2; len <= n; len++) {
            for (int i = 0; i <= n - len; i++) {
                int j = i + len - 1;
                if (len == 2) {
                    dp[i][j] = (s[i] == s[j]);
                } else {
                    dp[i][j] = (s[i] == s[j] && dp[i + 1][j - 1]);
                }
            }
        }
        // Now, dp contains whether each substring is a palindrome.
        // We can use this to find the longest substring that can be removed.
        int maxLen = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                if (dp[i][j]) {
                    maxLen = max(maxLen, j - i + 1);
                }
            }
        }
        return maxLen;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the string. We fill a 2D table of size $n \times n$.
> - **Space Complexity:** $O(n^2)$, for the 2D table.
> - **Optimality proof:** This approach is optimal because it considers all substrings exactly once, ensuring we find the longest substring that can be removed to make the string a palindrome.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming for building up solutions to larger problems from smaller ones.
- Problem-solving patterns identified: Using a table to store intermediate results to avoid redundant computation.
- Optimization techniques learned: Filling a table in a bottom-up manner to ensure all smaller subproblems are solved before larger ones.
- Similar problems to practice: Other string manipulation problems, especially those involving palindromes or substrings.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly initializing the dynamic programming table or not considering the base cases correctly.
- Edge cases to watch for: Handling empty strings or strings with a single character.
- Performance pitfalls: Using a naive approach that checks all substrings without using dynamic programming, leading to high time complexity.
- Testing considerations: Thoroughly testing the function with various inputs, including edge cases and large strings.