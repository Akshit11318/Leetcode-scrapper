## Longest Substring of One Repeating Character

**Problem Link:** https://leetcode.com/problems/longest-substring-of-one-repeating-character/description

**Problem Statement:**
- Input format: A string `s`.
- Constraints: `1 <= s.length <= 10^5`.
- Expected output format: The length of the longest substring that consists of only one repeating character.
- Key requirements: Find the longest substring with a single repeating character.
- Edge cases: Empty string, single-character string, string with all unique characters.
- Example test cases:
  - Input: `s = "aabbbcc"`; Output: `3` (The longest substring is `"bbb"`)
  - Input: `s = "abc"`; Output: `1` (The longest substring is any single character)

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible substring of `s` to see if it consists of a single repeating character.
- Step-by-step breakdown of the solution:
  1. Generate all possible substrings of `s`.
  2. For each substring, check if all characters are the same.
  3. Keep track of the longest substring found that meets the condition.
- Why this approach comes to mind first: It's straightforward and ensures we don't miss any potential substrings.

```cpp
int longestSubstring(const string& s) {
    int maxLength = 0;
    for (int i = 0; i < s.size(); ++i) {
        for (int j = i + 1; j <= s.size(); ++j) {
            string substr = s.substr(i, j - i);
            bool isSingleChar = true;
            for (int k = 1; k < substr.size(); ++k) {
                if (substr[k] != substr[0]) {
                    isSingleChar = false;
                    break;
                }
            }
            if (isSingleChar) {
                maxLength = max(maxLength, (int)substr.size());
            }
        }
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the string. This is because we generate all substrings ($O(n^2)$) and then for each substring, we potentially check all its characters again ($O(n)$).
> - **Space Complexity:** $O(n)$, for storing the substrings.
> - **Why these complexities occur:** The brute force approach involves nested loops for generating substrings and checking each substring, leading to high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all substrings, we can use a sliding window approach to track the longest substring with a single repeating character as we iterate through the string.
- Detailed breakdown of the approach:
  1. Initialize variables to keep track of the current character and the length of the current substring.
  2. Iterate through the string. If the current character matches the previous one, increment the length of the current substring.
  3. If the characters do not match, update the maximum length if necessary and reset the current substring length.
- Proof of optimality: This approach ensures we visit each character once, resulting in linear time complexity, which is optimal for this problem.

```cpp
int longestSubstring(const string& s) {
    if (s.empty()) return 0;
    
    int maxLength = 1;
    int currentLength = 1;
    char currentChar = s[0];
    
    for (int i = 1; i < s.size(); ++i) {
        if (s[i] == currentChar) {
            currentLength++;
        } else {
            maxLength = max(maxLength, currentLength);
            currentLength = 1;
            currentChar = s[i];
        }
    }
    
    return max(maxLength, currentLength);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string, because we make a single pass through the string.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space to store our variables.
> - **Optimality proof:** The optimal approach has linear time complexity because it only requires a single pass through the input string, making it impossible to achieve a better time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window technique, iteration through a string.
- Problem-solving patterns identified: Reducing the problem space by avoiding unnecessary operations (like generating all substrings).
- Optimization techniques learned: Using a single pass through the data to achieve linear time complexity.
- Similar problems to practice: Other string manipulation problems, especially those involving substrings or patterns.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases (like an empty string), not updating maximum lengths correctly.
- Edge cases to watch for: Empty string, single-character string, string with all unique characters.
- Performance pitfalls: Using brute force approaches for large inputs, not optimizing loops.
- Testing considerations: Ensure to test with a variety of inputs, including edge cases and large strings.