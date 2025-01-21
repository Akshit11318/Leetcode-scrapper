## Replace All S to Avoid Consecutive Repeating Characters

**Problem Link:** https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/description

**Problem Statement:**
- Input: A string `s` containing only lowercase letters.
- Constraints: The length of `s` is between `1` and `1000` inclusive.
- Expected Output: The modified string `s` after replacing all occurrences of 's' with a character that ensures no two consecutive characters are the same.
- Key Requirements: The modified string should not contain any consecutive repeating characters.
- Edge Cases: The input string might contain no 's', or it might be a single character.

**Example Test Cases:**
- Input: `"abcd"` - Output: `"abcd"` (no modifications needed)
- Input: `"ssss"` - Output: `"sdse"` (replace 's' to avoid consecutive repeats)
- Input: `"aabbcc"` - Output: `"aabbcc"` (no modifications needed)

---

### Brute Force Approach

**Explanation:**
- Start by iterating through the string `s`.
- For each character that is 's', consider replacing it with all possible lowercase letters (excluding 's') and check if the resulting string has any consecutive repeating characters.
- If a replacement does not introduce consecutive repeats, use it; otherwise, try the next possible replacement.

```cpp
string modifyString(string s) {
    for (int i = 0; i < s.length(); ++i) {
        if (s[i] == 's') {
            for (char c = 'a'; c <= 'z'; ++c) {
                if (c != 's') {
                    bool valid = true;
                    if (i > 0 && s[i - 1] == c) valid = false;
                    if (i < s.length() - 1 && s[i + 1] == c) valid = false;
                    if (valid) {
                        s[i] = c;
                        break;
                    }
                }
            }
        }
    }
    return s;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot 26)$, where $n$ is the length of string `s`. This is because for each 's' in the string, we potentially try 25 other characters.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the loop variables and do not allocate any additional space that scales with input size.
> - **Why these complexities occur:** The brute force approach involves trying all possible replacements for each 's', leading to a time complexity that is linear in the input size but multiplied by the number of possible replacements (25, in this case).

---

### Optimal Approach (Required)

**Explanation:**
- Instead of trying all possible replacements for each 's', we can observe that we only need to ensure the character before and after the current 's' are not the same as the replacement.
- We can maintain a set of forbidden characters (the characters before and after the current position) and choose the first character from 'a' to 'z' that is not in this set.
- This approach ensures we always find a valid replacement in a single pass through the string.

```cpp
string modifyString(string s) {
    for (int i = 0; i < s.length(); ++i) {
        if (s[i] == 's') {
            set<char> forbidden;
            if (i > 0) forbidden.insert(s[i - 1]);
            if (i < s.length() - 1) forbidden.insert(s[i + 1]);
            for (char c = 'a'; c <= 'z'; ++c) {
                if (c != 's' && forbidden.find(c) == forbidden.end()) {
                    s[i] = c;
                    break;
                }
            }
        }
    }
    return s;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of string `s`. We make a single pass through the string.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space to store the loop variables and the set of forbidden characters, which in the worst case can contain up to 2 characters (the ones before and after the current 's').
> - **Optimality proof:** This approach is optimal because it ensures we find a valid replacement for each 's' in a single pass through the string, without needing to try all possible replacements.

---

### Final Notes

**Learning Points:**
- The importance of considering all possible edge cases, such as when the input string contains no 's' or is a single character.
- The value of optimizing the brute force approach by reducing the number of possible replacements to consider.
- The use of a set to efficiently keep track of forbidden characters.

**Mistakes to Avoid:**
- Failing to check for edge cases, such as an empty string or a string with a single character.
- Not optimizing the brute force approach, leading to inefficient code.
- Not considering the use of data structures like sets to improve efficiency.