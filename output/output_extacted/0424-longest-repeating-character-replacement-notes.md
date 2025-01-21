## Longest Repeating Character Replacement

**Problem Link:** https://leetcode.com/problems/longest-repeating-character-replacement/description

**Problem Statement:**
- Input: A string `s` and an integer `k`.
- Constraints: `1 <= s.length <= 10^5`, `0 <= k <= 10^5`.
- Expected Output: The length of the longest substring after replacing at most `k` characters such that the substring contains only repeating characters.
- Key Requirements: Find the maximum length of the substring with repeating characters after at most `k` replacements.
- Example Test Cases:
  - Input: `s = "ABAB", k = 2`, Output: `4`
  - Input: `s = "AABABBA", k = 1`, Output: `4`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible substrings and for each substring, calculate how many replacements are needed to make all characters the same.
- We then check if the number of replacements needed is less than or equal to `k` and update our answer accordingly.

```cpp
class Solution {
public:
    int characterReplacement(string s, int k) {
        int n = s.length();
        int maxLen = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j <= n; j++) {
                string substr = s.substr(i, j - i);
                int replacements = 0;
                char mostFrequentChar = findMostFrequentChar(substr, &replacements);
                if (replacements <= k) {
                    maxLen = max(maxLen, substr.length());
                }
            }
        }
        return maxLen;
    }
    
    char findMostFrequentChar(string& substr, int* replacements) {
        int maxCount = 0;
        char mostFrequentChar = substr[0];
        unordered_map<char, int> charCount;
        for (char c : substr) {
            charCount[c]++;
            if (charCount[c] > maxCount) {
                maxCount = charCount[c];
                mostFrequentChar = c;
            }
        }
        *replacements = substr.length() - maxCount;
        return mostFrequentChar;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the string. The reason is we are generating all substrings ($O(n^2)$) and for each substring, we are finding the most frequent character ($O(n)$).
> - **Space Complexity:** $O(n)$, for storing the frequency of characters in the substring.
> - **Why these complexities occur:** The brute force approach is not efficient due to the nested loops that generate all substrings and the additional loop to find the most frequent character in each substring.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a sliding window approach to track the maximum length of the substring with repeating characters after at most `k` replacements.
- We maintain a frequency map of characters within the current window and the maximum frequency of any character in the window.
- We expand the window to the right and update the frequency map and the maximum frequency.
- If the number of characters that need to be replaced to make all characters the same exceeds `k`, we shrink the window from the left.

```cpp
class Solution {
public:
    int characterReplacement(string s, int k) {
        int n = s.length();
        int maxLen = 0;
        int maxCount = 0;
        unordered_map<char, int> charCount;
        int left = 0;
        for (int right = 0; right < n; right++) {
            charCount[s[right]]++;
            maxCount = max(maxCount, charCount[s[right]]);
            if (right - left + 1 - maxCount > k) {
                charCount[s[left]]--;
                left++;
            }
            maxLen = max(maxLen, right - left + 1);
        }
        return maxLen;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string. We are scanning the string once with the right pointer of the window.
> - **Space Complexity:** $O(1)$, as the number of unique characters in the string is constant (at most 26 for lowercase English letters).
> - **Optimality proof:** This is the optimal solution because we are scanning the string only once and maintaining the necessary information (frequency map and maximum frequency) within the window. We are also making the most efficient decisions about when to expand or shrink the window.

---

### Final Notes

**Learning Points:**
- The sliding window technique is useful for problems that involve finding a maximum or minimum length of a substring with certain properties.
- Maintaining a frequency map and the maximum frequency within the window can help in making decisions about when to expand or shrink the window.
- The key to solving this problem efficiently is to avoid generating all substrings and instead use a sliding window approach to track the maximum length of the substring with repeating characters after at most `k` replacements.

**Mistakes to Avoid:**
- Generating all substrings and checking each one, as this leads to an inefficient solution with high time complexity.
- Not maintaining the necessary information within the window, such as the frequency map and the maximum frequency.
- Not making the most efficient decisions about when to expand or shrink the window based on the number of characters that need to be replaced.