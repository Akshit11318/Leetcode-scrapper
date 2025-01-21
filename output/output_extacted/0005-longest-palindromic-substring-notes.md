## Longest Palindromic Substring

**Problem Link:** https://leetcode.com/problems/longest-palindromic-substring/description

**Problem Statement:**
- Input format and constraints: The input is a string `s` containing only lowercase English letters. The length of `s` is in the range `[1, 1000]`.
- Expected output format: The output should be the longest palindromic substring of `s`.
- Key requirements and edge cases to consider: A palindromic substring is a substring that reads the same backward as forward. If there are multiple palindromic substrings with the same maximum length, return any one of them.
- Example test cases with explanations:
  - Example 1: Input: `s = "babad"`, Output: `"bab"` or `"aba"`, Explanation: Both `"bab"` and `"aba"` are palindromic substrings.
  - Example 2: Input: `s = "cbbd"`, Output: `"bb"`, Explanation: `"bb"` is the longest palindromic substring.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible substrings of the input string and check if each one is a palindrome.
- Step-by-step breakdown of the solution:
  1. Generate all possible substrings of the input string.
  2. For each substring, check if it is a palindrome by comparing it with its reverse.
  3. Keep track of the longest palindromic substring found so far.
- Why this approach comes to mind first: It is a straightforward and intuitive approach to solve the problem by checking all possible substrings.

```cpp
class Solution {
public:
    string longestPalindrome(string s) {
        string longest = "";
        for (int i = 0; i < s.length(); i++) {
            for (int j = i + 1; j <= s.length(); j++) {
                string substr = s.substr(i, j - i);
                if (isPalindrome(substr) && substr.length() > longest.length()) {
                    longest = substr;
                }
            }
        }
        return longest;
    }
    
    bool isPalindrome(string s) {
        int left = 0, right = s.length() - 1;
        while (left < right) {
            if (s[left] != s[right]) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input string. This is because we generate all possible substrings ($O(n^2)$) and check if each one is a palindrome ($O(n)$).
> - **Space Complexity:** $O(1)$, excluding the space needed for the output. We only use a constant amount of space to store the longest palindromic substring and the current substring being checked.
> - **Why these complexities occur:** The time complexity is high because we are generating all possible substrings and checking if each one is a palindrome. The space complexity is low because we only use a constant amount of space to store the necessary information.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible substrings, we can expand around the center of the palindrome to find the longest palindromic substring.
- Detailed breakdown of the approach:
  1. Initialize the longest palindromic substring to an empty string.
  2. Iterate over the input string, considering each character as the center of a potential palindrome.
  3. For each character, expand around the center to find the longest palindromic substring.
  4. Update the longest palindromic substring if a longer one is found.
- Proof of optimality: This approach is optimal because it only considers the necessary substrings to find the longest palindromic substring, reducing the time complexity to $O(n^2)$.

```cpp
class Solution {
public:
    string longestPalindrome(string s) {
        string longest = "";
        for (int i = 0; i < s.length(); i++) {
            // Odd length palindrome
            string odd = expandAroundCenter(s, i, i);
            if (odd.length() > longest.length()) {
                longest = odd;
            }
            // Even length palindrome
            string even = expandAroundCenter(s, i, i + 1);
            if (even.length() > longest.length()) {
                longest = even;
            }
        }
        return longest;
    }
    
    string expandAroundCenter(string s, int left, int right) {
        while (left >= 0 && right < s.length() && s[left] == s[right]) {
            left--;
            right++;
        }
        return s.substr(left + 1, right - left - 1);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input string. This is because we iterate over the input string and expand around the center of the palindrome.
> - **Space Complexity:** $O(1)$, excluding the space needed for the output. We only use a constant amount of space to store the longest palindromic substring and the current substring being checked.
> - **Optimality proof:** This approach is optimal because it only considers the necessary substrings to find the longest palindromic substring, reducing the time complexity to $O(n^2)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Expanding around the center of a palindrome to find the longest palindromic substring.
- Problem-solving patterns identified: Using a brute force approach as a starting point and then optimizing it to find a more efficient solution.
- Optimization techniques learned: Reducing the time complexity by only considering the necessary substrings to find the longest palindromic substring.
- Similar problems to practice: Finding the shortest palindromic substring, finding all palindromic substrings, etc.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, such as an empty input string or a string with only one character.
- Edge cases to watch for: Handling strings with only one character, handling empty strings, etc.
- Performance pitfalls: Using a brute force approach that has a high time complexity, such as $O(n^3)$.
- Testing considerations: Testing the solution with different input strings, including edge cases, to ensure that it works correctly.