## Longest Palindromic Subsequence

**Problem Link:** https://leetcode.com/problems/longest-palindromic-subsequence/description

**Problem Statement:**
- Input format and constraints: The input is a string `s` containing only lowercase English letters. The length of `s` is in the range `[1, 1000]`.
- Expected output format: The output should be the length of the `longest palindromic subsequence` in `s`.
- Key requirements and edge cases to consider: The subsequence must be a palindrome, and it should be the longest among all possible subsequences.
- Example test cases with explanations:
  - Input: `s = "banana"`
    - Output: `3`
    - Explanation: The longest palindromic subsequence is `"ana"`.
  - Input: `s = "bbbab"`
    - Output: `4`
    - Explanation: The longest palindromic subsequence is `"bbbb"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the longest palindromic subsequence, we can generate all possible subsequences and check if each one is a palindrome.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsequences of the input string `s`.
  2. For each subsequence, check if it is a palindrome by comparing characters from the start and end, moving towards the center.
  3. Keep track of the longest palindromic subsequence found so far.
- Why this approach comes to mind first: It is a straightforward approach that checks all possibilities.

```cpp
#include <string>
using namespace std;

int longestPalindromicSubsequence(string s) {
    int n = s.length();
    int maxLength = 1; // Initialize with the minimum possible length

    // Generate all possible subsequences
    for (int mask = 1; mask < (1 << n); mask++) {
        string subsequence = "";
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                subsequence += s[i];
            }
        }

        // Check if the subsequence is a palindrome
        bool isPalindrome = true;
        int left = 0, right = subsequence.length() - 1;
        while (left < right) {
            if (subsequence[left] != subsequence[right]) {
                isPalindrome = false;
                break;
            }
            left++;
            right--;
        }

        if (isPalindrome) {
            maxLength = max(maxLength, (int)subsequence.length());
        }
    }

    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input string `s`. This is because we generate $2^n$ subsequences and for each subsequence, we check if it is a palindrome in $O(n)$ time.
> - **Space Complexity:** $O(n)$, as we need to store the subsequence and other variables.
> - **Why these complexities occur:** The exponential time complexity is due to generating all possible subsequences, and the linear space complexity is for storing the subsequence and other variables.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to solve this problem. The idea is to build a table where each cell `[i][j]` represents the length of the longest palindromic subsequence in the substring `s[i..j]`.
- Detailed breakdown of the approach:
  1. Create a table `dp` of size `n x n`, where `n` is the length of the input string `s`.
  2. Initialize the table by setting `dp[i][i] = 1` for all `i`, since a single character is always a palindrome of length 1.
  3. Fill the table in a bottom-up manner. For each substring `s[i..j]`, if `s[i] == s[j]`, then `dp[i][j] = dp[i+1][j-1] + 2`. Otherwise, `dp[i][j] = max(dp[i+1][j], dp[i][j-1])`.
  4. The value of `dp[0][n-1]` will be the length of the longest palindromic subsequence in the entire string `s`.
- Proof of optimality: This approach has a polynomial time complexity, which is much better than the exponential time complexity of the brute force approach. It also correctly computes the length of the longest palindromic subsequence.

```cpp
int longestPalindromicSubsequence(string s) {
    int n = s.length();
    vector<vector<int>> dp(n, vector<int>(n, 0));

    // Initialize the table
    for (int i = 0; i < n; i++) {
        dp[i][i] = 1;
    }

    // Fill the table in a bottom-up manner
    for (int length = 2; length <= n; length++) {
        for (int i = 0; i < n - length + 1; i++) {
            int j = i + length - 1;
            if (s[i] == s[j]) {
                dp[i][j] = dp[i+1][j-1] + 2;
            } else {
                dp[i][j] = max(dp[i+1][j], dp[i][j-1]);
            }
        }
    }

    return dp[0][n-1];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input string `s`. This is because we fill a table of size `n x n`.
> - **Space Complexity:** $O(n^2)$, as we need to store the table `dp`.
> - **Optimality proof:** This approach has a polynomial time complexity, which is much better than the exponential time complexity of the brute force approach. It also correctly computes the length of the longest palindromic subsequence.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, bottom-up approach, and table filling.
- Problem-solving patterns identified: Breaking down the problem into smaller subproblems, solving each subproblem only once, and storing the solutions to subproblems to avoid redundant computation.
- Optimization techniques learned: Using dynamic programming to reduce the time complexity from exponential to polynomial.
- Similar problems to practice: `Longest Common Subsequence`, `Shortest Common Supersequence`, and `Edit Distance`.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect initialization of the table, incorrect filling of the table, and incorrect computation of the final result.
- Edge cases to watch for: Empty string, string with a single character, and string with only two characters.
- Performance pitfalls: Using an exponential time complexity approach for large inputs.
- Testing considerations: Test the function with different inputs, including edge cases, to ensure it produces the correct output.