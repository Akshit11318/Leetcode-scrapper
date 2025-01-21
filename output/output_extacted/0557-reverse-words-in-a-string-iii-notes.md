## Reverse Words in a String III
**Problem Link:** https://leetcode.com/problems/reverse-words-in-a-string-iii/description

**Problem Statement:**
- Input format: a string `s` containing one or more words separated by spaces.
- Constraints: `1 <= s.length <= 10^5`.
- Expected output format: a string with each word reversed.
- Key requirements: reverse each word in the string while maintaining the original word order.
- Example test cases:
  - Input: `s = "Let's take LeetCode contest"`
    Output: `"s'teL ekat edoCteeL tsetnoc"`
  - Input: `s = "God ding"`
    Output: `"doG gniD"`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: iterate through the string to find spaces and reverse each word individually.
- Step-by-step breakdown:
  1. Split the input string into words using space as the delimiter.
  2. For each word, reverse the characters.
  3. Join the reversed words back into a single string with spaces in between.
- Why this approach comes to mind first: it directly addresses the requirement of reversing each word without considering the overall string structure.

```cpp
class Solution {
public:
    string reverseWords(string s) {
        vector<string> words;
        string word = "";
        
        // Split the string into words
        for (char c : s) {
            if (c == ' ') {
                words.push_back(word);
                word = "";
            } else {
                word += c;
            }
        }
        words.push_back(word); // Add the last word
        
        // Reverse each word and join them back
        for (int i = 0; i < words.size(); i++) {
            int left = 0, right = words[i].size() - 1;
            while (left < right) {
                swap(words[i][left], words[i][right]);
                left++, right--;
            }
        }
        
        string result = "";
        for (string w : words) {
            result += w + " ";
        }
        result.pop_back(); // Remove the trailing space
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string, because we are scanning the string twice: once to split it into words and once to reverse each word.
> - **Space Complexity:** $O(n)$, as in the worst case, we might end up storing all characters in the `words` vector.
> - **Why these complexities occur:** The brute force approach involves iterating over the string multiple times (to split and to reverse), leading to linear time complexity. The space complexity is also linear due to the storage of the reversed words.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: instead of splitting the string into words and then reversing each word, we can use two pointers to find the start and end of each word in the original string and reverse the characters in place.
- Detailed breakdown:
  1. Initialize two pointers, `start` and `end`, to the beginning of the string.
  2. Move `end` until a space is found, marking the end of a word.
  3. Reverse the word from `start` to `end - 1`.
  4. Move `start` to the character after the space (the beginning of the next word).
  5. Repeat steps 2-4 until the end of the string is reached.
- Proof of optimality: this approach scans the string only once, making it more efficient than the brute force approach.

```cpp
class Solution {
public:
    string reverseWords(string s) {
        int start = 0;
        for (int end = 0; end < s.size(); end++) {
            if (s[end] == ' ') {
                reverse(s.begin() + start, s.begin() + end);
                start = end + 1;
            }
        }
        // Reverse the last word
        reverse(s.begin() + start, s.end());
        
        return s;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string. Although this is the same as the brute force approach, the constant factors are smaller because we're doing less work overall.
> - **Space Complexity:** $O(1)$, excluding the space needed for the output, because we're modifying the input string in place and using a constant amount of space to store our pointers.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the string, minimizing both time and space complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: string manipulation, in-place reversal, and the use of pointers or indices to track positions within a string.
- Problem-solving patterns: looking for ways to reduce the number of passes through the data and minimizing extra space usage.
- Optimization techniques: recognizing that splitting the string into words and then reversing each word is less efficient than reversing words in place.

**Mistakes to Avoid:**
- Common implementation errors: forgetting to handle the last word in the string, incorrectly calculating the end index of a word.
- Edge cases to watch for: strings with leading, trailing, or multiple consecutive spaces.
- Performance pitfalls: using unnecessary extra space or making multiple passes through the data when a single pass can suffice.
- Testing considerations: ensure that the solution works correctly for strings of varying lengths, including empty strings and strings with a single word.