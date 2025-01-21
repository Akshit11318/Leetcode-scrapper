## Word Pattern
**Problem Link:** https://leetcode.com/problems/word-pattern/description

**Problem Statement:**
- Input format: The function takes two parameters: `pattern` (a string) and `s` (a string). The string `s` is split into words based on spaces.
- Constraints: `1 <= pattern.length <= 11`, `1 <= s.length <= 100`, `pattern` contains only lowercase letters, `s` contains only lowercase letters and spaces.
- Expected output format: A boolean indicating whether the given pattern matches the word pattern in the string `s`.
- Key requirements and edge cases to consider:
  - Each letter in the pattern maps to a unique word in `s`.
  - Each word in `s` maps to a unique letter in the pattern.
- Example test cases with explanations:
  - `pattern = "abba"`, `s = "dog cat cat dog"`: Returns `true`.
  - `pattern = "abba"`, `s = "dog cat cat fish"`: Returns `false`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The most straightforward approach involves checking every possible mapping of pattern letters to words in the string `s`.
- Step-by-step breakdown of the solution:
  1. Split the string `s` into words.
  2. Create a mapping from pattern letters to words and vice versa.
  3. Iterate through the pattern and the words simultaneously, checking if each pattern letter maps to the correct word and each word maps back to the correct pattern letter.
- Why this approach comes to mind first: It directly addresses the problem statement by creating mappings and checking them against the given pattern and string.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

bool wordPattern(string pattern, string s) {
    // Split the string s into words
    vector<string> words;
    string word;
    for (char c : s) {
        if (c == ' ') {
            words.push_back(word);
            word.clear();
        } else {
            word += c;
        }
    }
    words.push_back(word);

    // Check if the number of words matches the length of the pattern
    if (words.size() != pattern.size()) {
        return false;
    }

    // Create mappings from pattern letters to words and vice versa
    unordered_map<char, string> patternToWord;
    unordered_map<string, char> wordToPattern;

    for (int i = 0; i < pattern.size(); ++i) {
        char patternLetter = pattern[i];
        string word = words[i];

        // Check if the pattern letter is already mapped to a word
        if (patternToWord.find(patternLetter) != patternToWord.end()) {
            // If it is, check if the mapped word matches the current word
            if (patternToWord[patternLetter] != word) {
                return false;
            }
        } else {
            // If not, check if the word is already mapped to a pattern letter
            if (wordToPattern.find(word) != wordToPattern.end()) {
                return false;
            }
            // If not, create the mapping
            patternToWord[patternLetter] = word;
            wordToPattern[word] = patternLetter;
        }
    }

    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the length of the pattern and $m$ is the total length of all words in the string `s`. This is because we iterate through the pattern and the string once.
> - **Space Complexity:** $O(n + m)$, for storing the mappings from pattern letters to words and vice versa.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each character in the pattern and each character in the string `s`. The space complexity is also linear because in the worst case, we might need to store every character in the pattern and every character in the string `s` in our mappings.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The same insight as the brute force approach, but recognizing that the initial implementation is already optimal because it uses unordered maps for efficient lookups and only requires a single pass through the pattern and the string.
- Detailed breakdown of the approach: The approach remains the same as the brute force approach because it is already optimal.
- Proof of optimality: The solution is optimal because it achieves the minimum time complexity required to solve the problem, which involves checking each character in the pattern and each word in the string at least once.

```cpp
// The code remains the same as the brute force approach because it is already optimal.
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the length of the pattern and $m$ is the total length of all words in the string `s`.
> - **Space Complexity:** $O(n + m)$, for storing the mappings from pattern letters to words and vice versa.
> - **Optimality proof:** The solution is optimal because it checks each pattern letter and each word exactly once, which is the minimum required to determine if the pattern matches the word pattern in the string.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Efficient use of unordered maps for fast lookups, iterating through multiple data structures simultaneously.
- Problem-solving patterns identified: Checking for unique mappings between two sets of data.
- Optimization techniques learned: Recognizing when an initial solution is already optimal.
- Similar problems to practice: Other string and pattern matching problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases, such as an empty pattern or string, or not checking for unique mappings in both directions.
- Edge cases to watch for: Patterns or strings with repeating elements, patterns or strings of different lengths.
- Performance pitfalls: Using data structures with slower lookup times, such as vectors or lists, instead of unordered maps.
- Testing considerations: Thoroughly testing the function with a variety of inputs, including edge cases and large datasets.