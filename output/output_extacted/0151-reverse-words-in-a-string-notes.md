## Reverse Words in a String

**Problem Link:** https://leetcode.com/problems/reverse-words-in-a-string/description

**Problem Statement:**
- Input format: A string `s` containing one or more words separated by spaces.
- Constraints: `1 <= s.length <= 10^4`, `s` consists of English letters and spaces, and there is at least one word.
- Expected output format: A string with the words in reversed order.
- Key requirements: Reverse the order of the words in the input string.
- Edge cases: Empty strings, strings with leading or trailing spaces, strings with multiple consecutive spaces.

Example test cases:
- Input: "hello world"
  Output: "world hello"
- Input: "a good   example"
  Output: "example good a"

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Split the string into words and then reverse the order of the words.
- Step-by-step breakdown:
  1. Split the input string into words using space as the delimiter.
  2. Store the words in a data structure like a vector.
  3. Reverse the order of the words in the vector.
  4. Join the words back into a string with spaces in between.

```cpp
#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>

string reverseWords(string s) {
    // Remove leading and trailing spaces
    while (s.size() > 0 && s[0] == ' ') s.erase(0, 1);
    while (s.size() > 0 && s[s.size() - 1] == ' ') s.pop_back();

    // Split the string into words
    vector<string> words;
    stringstream ss(s);
    string word;
    while (ss >> word) {
        words.push_back(word);
    }

    // Reverse the order of the words
    reverse(words.begin(), words.end());

    // Join the words back into a string
    string result;
    for (int i = 0; i < words.size(); i++) {
        result += words[i];
        if (i < words.size() - 1) result += " ";
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we are scanning the string twice: once to split it into words and once to reverse the order of the words.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we are storing the words in a vector.
> - **Why these complexities occur:** The time complexity is linear because we are performing a constant amount of work for each character in the input string. The space complexity is also linear because we are storing all the words in a vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use two pointers to track the start and end of each word in the string.
- Detailed breakdown:
  1. Remove leading and trailing spaces from the input string.
  2. Initialize two pointers, `start` and `end`, to the beginning of the string.
  3. Iterate through the string to find the end of each word.
  4. When a space is encountered, reverse the word from `start` to `end - 1`.
  5. Update `start` to the character after the space.
  6. After the loop, reverse the last word.
  7. Reverse the entire string to get the words in reversed order.

```cpp
string reverseWords(string s) {
    // Remove leading and trailing spaces
    int start = 0;
    while (start < s.size() && s[start] == ' ') start++;
    int end = s.size() - 1;
    while (end >= 0 && s[end] == ' ') end--;

    // Reverse the entire string
    reverse(s.begin() + start, s.begin() + end + 1);

    // Initialize pointers
    int wordStart = start;
    for (int i = start; i <= end; i++) {
        if (s[i] == ' ') {
            // Reverse the word
            reverse(s.begin() + wordStart, s.begin() + i);
            wordStart = i + 1;
        }
    }

    // Reverse the last word
    reverse(s.begin() + wordStart, s.begin() + end + 1);

    return s.substr(start, end - start + 1);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we are scanning the string twice: once to reverse the entire string and once to reverse each word.
> - **Space Complexity:** $O(1)$, excluding the space required for the output string. This is because we are only using a constant amount of space to store the pointers.
> - **Optimality proof:** This is the optimal solution because we are only scanning the string twice and using a constant amount of space. We cannot do better than this because we must at least scan the string once to reverse the words.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two pointers, string reversal, and word splitting.
- Problem-solving patterns identified: Removing leading and trailing spaces, reversing the entire string, and then reversing each word.
- Optimization techniques learned: Using two pointers to track the start and end of each word, and reversing the entire string before reversing each word.
- Similar problems to practice: Reversing a linked list, reversing a substring in a string.

**Mistakes to Avoid:**
- Common implementation errors: Not removing leading and trailing spaces, not handling the case where the input string is empty.
- Edge cases to watch for: Strings with multiple consecutive spaces, strings with leading or trailing spaces.
- Performance pitfalls: Using a brute force approach that has a high time or space complexity.
- Testing considerations: Testing the function with different input strings, including edge cases and boundary cases.