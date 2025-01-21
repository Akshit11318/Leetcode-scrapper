## Longest Substring of All Vowels in Order

**Problem Link:** https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/description

**Problem Statement:**
- Input: a string `word` containing only lowercase letters.
- Constraints: $1 \leq \text{length of } word \leq 10^5$.
- Expected output: the length of the longest substring that contains all vowels in order.
- Key requirements: the substring must contain all vowels (`a`, `e`, `i`, `o`, `u`) in order, but can contain other characters as well.
- Edge cases: an empty string, a string with no vowels, or a string with vowels but not in order.

### Brute Force Approach

**Explanation:**
- The initial thought process is to check every possible substring of the input string.
- We then check each substring to see if it contains all vowels in order.
- This approach comes to mind first because it's a straightforward way to ensure we don't miss any potential substrings.

```cpp
class Solution {
public:
    int longestSubstring(string word) {
        int n = word.size();
        int maxLen = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j <= n; j++) {
                string substr = word.substr(i, j - i);
                if (checkVowelsInOrder(substr)) {
                    maxLen = max(maxLen, (int)substr.size());
                }
            }
        }
        return maxLen;
    }
    
    bool checkVowelsInOrder(string substr) {
        int vowelIndex = 0;
        string vowels = "aeiou";
        for (char c : substr) {
            if (c == vowels[vowelIndex]) {
                vowelIndex++;
                if (vowelIndex == 5) return true;
            }
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ where $n$ is the length of the input string. This is because for each substring (which is $O(n^2)$), we check if it contains all vowels in order, which can take up to $O(n)$ time.
> - **Space Complexity:** $O(n)$ for storing the substring.
> - **Why these complexities occur:** The brute force approach has high time complexity due to the nested loops that generate all possible substrings and then check each one for the condition.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a sliding window approach to efficiently check substrings without generating all possible ones.
- We maintain a window of characters and slide it through the string, expanding it when we find a vowel in the correct order and shrinking it when we encounter a character that doesn't fit the order.
- This approach is optimal because it avoids unnecessary checks and only considers substrings that could potentially contain all vowels in order.

```cpp
class Solution {
public:
    int longestSubstring(string word) {
        int n = word.size();
        int maxLen = 0;
        int vowelIndex = 0;
        string vowels = "aeiou";
        int left = 0;
        for (int right = 0; right < n; right++) {
            if (word[right] == vowels[vowelIndex]) {
                vowelIndex++;
                if (vowelIndex == 5) {
                    maxLen = max(maxLen, right - left + 1);
                    vowelIndex--;
                    left++;
                }
            } else if (word[right] != vowels[vowelIndex] && word[right] != 'a') {
                vowelIndex = 0;
                left = right + 1;
            }
        }
        return maxLen;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the input string. This is because we make a single pass through the string.
> - **Space Complexity:** $O(1)$ as we use a constant amount of space to store the vowel index, left pointer, and max length.
> - **Optimality proof:** This is the optimal solution because we only make one pass through the string and avoid unnecessary checks by using a sliding window approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sliding window technique, efficient substring checking.
- Problem-solving patterns identified: using a sliding window to reduce time complexity.
- Optimization techniques learned: avoiding unnecessary checks, using pointers to track window boundaries.
- Similar problems to practice: other substring problems, pattern matching problems.

**Mistakes to Avoid:**
- Common implementation errors: incorrect handling of edge cases (e.g., empty string, string with no vowels).
- Edge cases to watch for: strings with repeated vowels, strings with vowels not in order.
- Performance pitfalls: using brute force approaches for large inputs.
- Testing considerations: thoroughly test with different types of inputs to ensure correctness.