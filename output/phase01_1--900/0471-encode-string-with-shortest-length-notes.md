## Encode String with Shortest Length
**Problem Link:** https://leetcode.com/problems/encode-string-with-shortest-length/description

**Problem Statement:**
- Input: A string `s` containing only lowercase letters.
- Constraints: `1 <= s.length <= 1000`.
- Expected Output: The shortest encoded string of `s` using the Run-Length Encoding (RLE) technique.
- Key Requirements: If the length of the encoded string is not shorter than the original string, return the original string.
- Edge Cases: Handle strings with repeating characters and those without any repetition.

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate through the string and count the consecutive occurrences of each character.
- Then, construct the encoded string by appending the character and its count.
- If the length of the encoded string is not shorter than the original, return the original string.

```cpp
class Solution {
public:
    string encodeString(string s) {
        string encoded = "";
        int count = 1;
        
        for (int i = 1; i <= s.length(); i++) {
            if (i == s.length() || s[i] != s[i - 1]) {
                encoded += s[i - 1] + to_string(count);
                count = 1;
            } else {
                count++;
            }
        }
        
        return encoded.length() < s.length() ? encoded : s;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string, because we make a single pass through the string.
> - **Space Complexity:** $O(n)$, as in the worst case, the encoded string could be of the same length as the original string if no characters repeat.
> - **Why these complexities occur:** The iteration through the string causes the linear time complexity, and the construction of the encoded string leads to the space complexity.

### Optimal Approach (Required)

**Explanation:**
- The optimal solution involves the same logic as the brute force approach but with a focus on minimizing unnecessary operations.
- We directly compare the lengths of the original and encoded strings during construction to decide whether to return the original string early.
- This approach ensures we do not spend extra time constructing an encoded string that will not be used.

```cpp
class Solution {
public:
    string encodeString(string s) {
        string encoded = "";
        int count = 1;
        for (int i = 1; i <= s.length(); i++) {
            if (i == s.length() || s[i] != s[i - 1]) {
                encoded += s[i - 1] + to_string(count);
                if (encoded.length() >= s.length()) return s; // Early return if encoded string is not shorter
                count = 1;
            } else {
                count++;
            }
        }
        return encoded;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, as we still make a single pass through the string.
> - **Space Complexity:** $O(n)$, because the space required does not change.
> - **Optimality proof:** This is optimal because we must examine each character at least once to determine if it can be encoded more compactly, and we do this in a single pass.

### Final Notes

**Learning Points:**
- The problem demonstrates the use of Run-Length Encoding (RLE) for string compression.
- It highlights the importance of considering the trade-offs between the lengths of the original and encoded strings.
- The solution showcases a simple, efficient algorithm for solving the problem.

**Mistakes to Avoid:**
- Not checking for the length of the encoded string against the original string during construction.
- Failing to handle edge cases, such as strings with no repeating characters.
- Not optimizing the solution to return the original string as soon as it's clear the encoded string won't be shorter.