## Longest Substring Without Repeating Characters

**Problem Link:** https://leetcode.com/problems/longest-substring-without-repeating-characters/description

**Problem Statement:**
- Input format: a string `s` containing letters, digits, or symbols.
- Constraints: `0 <= s.length <= 5 * 10^4`.
- Expected output format: the length of the longest substring without repeating characters.
- Key requirements and edge cases to consider: handling empty strings, strings with all unique characters, and strings with repeating characters.
- Example test cases:
  - Input: `s = "abcabcbb"`, Output: `3` (Explanation: "abc" is the longest substring without repeating characters).
  - Input: `s = "bbbbb"`, Output: `1` (Explanation: "b" is the longest substring without repeating characters).
  - Input: `s = "pwwkew"`, Output: `3` (Explanation: "wke" is the longest substring without repeating characters).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: check every possible substring of the input string to see if it contains any repeating characters.
- Step-by-step breakdown of the solution:
  1. Generate all possible substrings of the input string.
  2. For each substring, check if it contains any repeating characters by iterating through each character and comparing it with the rest.
  3. Keep track of the longest substring without repeating characters.
- Why this approach comes to mind first: it's a straightforward, intuitive solution that checks all possibilities.

```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int maxLength = 0;
        for (int i = 0; i < s.length(); i++) {
            for (int j = i + 1; j <= s.length(); j++) {
                string substr = s.substr(i, j - i);
                if (isUnique(substr)) {
                    maxLength = max(maxLength, (int)substr.length());
                }
            }
        }
        return maxLength;
    }

    bool isUnique(string s) {
        for (int i = 0; i < s.length(); i++) {
            for (int j = i + 1; j < s.length(); j++) {
                if (s[i] == s[j]) return false;
            }
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input string. This is because we generate all possible substrings ($O(n^2)$) and then check each substring for uniqueness ($O(n)$).
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we need to store each substring.
> - **Why these complexities occur:** the brute force approach checks all possibilities, resulting in high time and space complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: use a sliding window approach with a set to keep track of unique characters in the current window.
- Detailed breakdown of the approach:
  1. Initialize a set to store unique characters in the current window.
  2. Initialize two pointers, `left` and `right`, to represent the start and end of the window.
  3. Move the `right` pointer to the right, adding characters to the set.
  4. If a repeating character is found, move the `left` pointer to the right, removing characters from the set, until the repeating character is removed.
  5. Keep track of the maximum length of the window.
- Proof of optimality: this approach has a linear time complexity because each character is visited at most twice (once by the `right` pointer and once by the `left` pointer).

```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> charSet;
        int left = 0;
        int maxLength = 0;
        for (int right = 0; right < s.length(); right++) {
            while (charSet.find(s[right]) != charSet.end()) {
                charSet.erase(s[left]);
                left++;
            }
            charSet.insert(s[right]);
            maxLength = max(maxLength, right - left + 1);
        }
        return maxLength;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string. This is because each character is visited at most twice.
> - **Space Complexity:** $O(min(n, m))$, where $n$ is the length of the input string and $m$ is the size of the character set. This is because we need to store unique characters in the set.
> - **Optimality proof:** this approach has a linear time complexity, making it optimal for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sliding window approach, set data structure.
- Problem-solving patterns identified: using a set to keep track of unique elements, moving pointers to represent a window.
- Optimization techniques learned: reducing time complexity by avoiding redundant operations.
- Similar problems to practice: Longest Substring with At Most K Distinct Characters, Longest Substring with At Least K Repeating Characters.

**Mistakes to Avoid:**
- Common implementation errors: not checking for edge cases, not handling repeating characters correctly.
- Edge cases to watch for: empty strings, strings with all unique characters, strings with repeating characters.
- Performance pitfalls: using a brute force approach, not optimizing the solution for large inputs.
- Testing considerations: testing with different input sizes, testing with different character sets.