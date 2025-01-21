## Maximum Deletions on a String
**Problem Link:** https://leetcode.com/problems/maximum-deletions-on-a-string/description

**Problem Statement:**
- Input format: a string `s`
- Constraints: `1 <= s.length <= 10^5`
- Expected output format: the maximum number of deletions that can be performed on the string `s` to make it a palindrome
- Key requirements and edge cases to consider: the string `s` can contain any ASCII characters, and we need to find the maximum number of deletions that can be performed to make it a palindrome
- Example test cases with explanations:
  - Input: `s = "abcba"`
    - Output: `0`
    - Explanation: The string is already a palindrome, so no deletions are needed.
  - Input: `s = "abc"`
    - Output: `2`
    - Explanation: We can delete the characters `'a'` and `'c'` to make the string a palindrome (`"b"`).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: try all possible deletions of characters from the string and check if the resulting string is a palindrome
- Step-by-step breakdown of the solution:
  1. Generate all possible subsets of the string `s`
  2. For each subset, check if it is a palindrome
  3. Keep track of the maximum number of deletions that can be performed to make the string a palindrome
- Why this approach comes to mind first: it is a straightforward and intuitive approach, but it has an exponential time complexity due to the generation of all possible subsets

```cpp
#include <iostream>
#include <string>
#include <vector>

int maxDeletions(const std::string& s) {
    int n = s.length();
    int maxDeletions = 0;

    for (int mask = 0; mask < (1 << n); ++mask) {
        std::string subset;
        for (int i = 0; i < n; ++i) {
            if ((mask & (1 << i)) != 0) {
                subset += s[i];
            }
        }

        if (isPalindrome(subset)) {
            maxDeletions = std::max(maxDeletions, n - subset.length());
        }
    }

    return maxDeletions;
}

bool isPalindrome(const std::string& s) {
    int left = 0;
    int right = s.length() - 1;

    while (left < right) {
        if (s[left] != s[right]) {
            return false;
        }
        ++left;
        --right;
    }

    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the string `s`, because we generate all possible subsets of the string and check if each subset is a palindrome
> - **Space Complexity:** $O(n)$, because we need to store the current subset being checked
> - **Why these complexities occur:** the exponential time complexity occurs because we generate all possible subsets of the string, and the linear space complexity occurs because we need to store the current subset being checked

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: use dynamic programming to find the longest palindromic subsequence in the string `s`, and then calculate the maximum number of deletions as the difference between the length of the string and the length of the longest palindromic subsequence
- Detailed breakdown of the approach:
  1. Create a 2D array `dp` to store the lengths of the longest palindromic subsequences for all substrings of `s`
  2. Fill the `dp` array in a bottom-up manner, using the following recurrence relation:
    - If the current substring has a length of 1, the length of the longest palindromic subsequence is 1
    - If the current substring has a length of 2, the length of the longest palindromic subsequence is 2 if the characters are the same, and 1 otherwise
    - If the current substring has a length greater than 2, the length of the longest palindromic subsequence is the maximum of the lengths of the longest palindromic subsequences for the substrings without the first and last characters, and the length of the longest palindromic subsequence for the substring without the first character plus the length of the longest palindromic subsequence for the substring without the last character, if the first and last characters are the same
  3. Calculate the maximum number of deletions as the difference between the length of the string and the length of the longest palindromic subsequence
- Proof of optimality: this approach is optimal because it uses dynamic programming to find the longest palindromic subsequence in the string, which is the key to finding the maximum number of deletions

```cpp
int maxDeletions(const std::string& s) {
    int n = s.length();
    std::vector<std::vector<int>> dp(n, std::vector<int>(n, 0));

    for (int i = 0; i < n; ++i) {
        dp[i][i] = 1;
    }

    for (int length = 2; length <= n; ++length) {
        for (int i = 0; i <= n - length; ++i) {
            int j = i + length - 1;

            if (length == 2) {
                dp[i][j] = (s[i] == s[j]) ? 2 : 1;
            } else {
                dp[i][j] = std::max(dp[i + 1][j], dp[i][j - 1]);
                if (s[i] == s[j]) {
                    dp[i][j] = std::max(dp[i][j], dp[i + 1][j - 1] + 2);
                }
            }
        }
    }

    return n - dp[0][n - 1];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the string `s`, because we fill the `dp` array in a bottom-up manner
> - **Space Complexity:** $O(n^2)$, because we need to store the `dp` array
> - **Optimality proof:** this approach is optimal because it uses dynamic programming to find the longest palindromic subsequence in the string, which is the key to finding the maximum number of deletions

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, longest palindromic subsequence
- Problem-solving patterns identified: using dynamic programming to solve problems that have overlapping subproblems
- Optimization techniques learned: using dynamic programming to avoid redundant computations
- Similar problems to practice: finding the longest common subsequence, finding the shortest path in a graph

**Mistakes to Avoid:**
- Common implementation errors: not initializing the `dp` array correctly, not using the correct recurrence relation
- Edge cases to watch for: handling strings with a length of 1 or 2, handling strings with duplicate characters
- Performance pitfalls: not using dynamic programming to avoid redundant computations, not using the correct data structure to store the `dp` array
- Testing considerations: testing the function with different input strings, testing the function with edge cases