## Count Substrings with Only One Distinct Letter
**Problem Link:** https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/description

**Problem Statement:**
- Input: A string `s`.
- Expected output: The number of substrings in `s` that have only one distinct letter.
- Key requirements and edge cases to consider: Handling strings of varying lengths, including empty strings, and ensuring the solution works for all possible characters.
- Example test cases with explanations:
  - For `s = "abc"`, the output should be `3`, because there are three substrings with only one distinct letter: `"a"`, `"b"`, and `"c"`.
  - For `s = "aaa"`, the output should be `6`, because all substrings (`"a"`, `"aa"`, `"aaa"`) have only one distinct letter.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this, we need to generate all possible substrings of the input string and check each one to see if it contains only one distinct letter.
- Step-by-step breakdown of the solution:
  1. Generate all possible substrings of the input string.
  2. For each substring, check if all characters are the same.
  3. Count the substrings that meet the condition.
- Why this approach comes to mind first: It's straightforward and directly addresses the problem statement by considering every possible case.

```cpp
class Solution {
public:
    int countSubstrings(string s) {
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            for (int j = i + 1; j <= s.length(); j++) {
                string substr = s.substr(i, j - i);
                bool isDistinct = true;
                for (int k = 1; k < substr.length(); k++) {
                    if (substr[k] != substr[0]) {
                        isDistinct = false;
                        break;
                    }
                }
                if (isDistinct) {
                    count++;
                }
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the string. This is because for each character in the string (first loop), we consider all possible substrings starting from that character (second loop), and for each substring, we potentially check every character (third loop).
> - **Space Complexity:** $O(n)$, for storing the substrings.
> - **Why these complexities occur:** The nested loops and the substring generation lead to these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all substrings and checking them, we can iterate through the string and for each character, consider the substrings starting from that character that could have only one distinct letter.
- Detailed breakdown of the approach:
  1. Iterate through the string.
  2. For each character, expand outwards to form substrings with only that character.
  3. Count these substrings.
- Proof of optimality: This approach directly counts the substrings without unnecessary generation or checks, making it more efficient than the brute force method.

```cpp
class Solution {
public:
    int countSubstrings(string s) {
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            // Count odd length substrings
            count += countSubstrings(s, i, i);
            // Count even length substrings
            count += countSubstrings(s, i, i + 1);
        }
        return count;
    }
    
    int countSubstrings(string s, int left, int right) {
        int count = 0;
        while (left >= 0 && right < s.length() && s[left] == s[right]) {
            count++;
            left--;
            right++;
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the string. This is because for each character, we potentially expand outwards to consider all possible substrings.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input string.
> - **Optimality proof:** This solution directly counts the substrings without generating them, making it more efficient than the brute force approach. It's optimal because it only considers substrings that could potentially have only one distinct letter, avoiding unnecessary checks.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Expanding from the center to count substrings, a common technique for string problems involving substrings.
- Problem-solving patterns identified: Directly counting substrings instead of generating them, which can reduce complexity.
- Optimization techniques learned: Avoiding unnecessary generation of substrings and using two pointers to expand from the center.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases like empty strings or strings with only one character.
- Edge cases to watch for: Handling the start and end of the string correctly when expanding substrings.
- Performance pitfalls: Using brute force approaches for large inputs, which can lead to timeouts or errors.
- Testing considerations: Thoroughly testing with various inputs, including edge cases and large strings, to ensure correctness and performance.