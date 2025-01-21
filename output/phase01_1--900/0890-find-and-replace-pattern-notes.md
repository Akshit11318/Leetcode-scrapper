## Find and Replace Pattern
**Problem Link:** https://leetcode.com/problems/find-and-replace-pattern/description

**Problem Statement:**
- Input format: You are given a list of strings `words` and a string `pattern`.
- Constraints: Each word in `words` and `pattern` consists only of lowercase English letters.
- Expected output format: Return a list of strings from `words` that match the given `pattern`.
- Key requirements and edge cases to consider: 
  - A word matches the `pattern` if replacing all occurrences of each character in the word with a unique character in the `pattern` results in the `pattern`. 
  - A character in the word can be replaced by only one character in the `pattern`, and a character in the `pattern` can be replaced by only one character in the word.
- Example test cases with explanations:
  - Input: `words = ["abc","deq","mee","aqq","dkd","ccc"]`, `pattern = "abb"`
  - Output: `["mee","aqq"]`
  - Explanation: 
    - "abc" does not match "abb" because 'c' can't be 'b'.
    - "deq" does not match "abb" because 'e' can't be 'b' and 'q' can't be 'b'.
    - "mee" matches "abb" by replacing 'm' with 'a' and 'e' with 'b'.
    - "aqq" matches "abb" by replacing 'a' with 'a' and 'q' with 'b'.
    - "dkd" does not match "abb" because 'd' can't be 'a' and 'k' can't be 'b'.
    - "ccc" does not match "abb" because 'c' can't be 'a' and 'c' can't be 'b'.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each word in the list and compare it with the pattern.
- Step-by-step breakdown of the solution:
  1. Create a mapping from the word to the pattern.
  2. Check if the mapping is valid (i.e., each character in the word maps to a unique character in the pattern, and vice versa).
  3. If the mapping is valid, add the word to the result list.
- Why this approach comes to mind first: It's a straightforward approach that checks each word individually.

```cpp
vector<string> findAndReplacePattern(vector<string>& words, string pattern) {
    vector<string> result;
    for (const auto& word : words) {
        unordered_map<char, char> wordToPattern;
        unordered_map<char, char> patternToWord;
        bool isValid = true;
        for (int i = 0; i < word.size(); ++i) {
            char wordChar = word[i];
            char patternChar = pattern[i];
            if ((wordToPattern.count(wordChar) && wordToPattern[wordChar] != patternChar) ||
                (patternToWord.count(patternChar) && patternToWord[patternChar] != wordChar)) {
                isValid = false;
                break;
            }
            wordToPattern[wordChar] = patternChar;
            patternToWord[patternChar] = wordChar;
        }
        if (isValid) {
            result.push_back(word);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where $n$ is the number of words and $m$ is the length of each word (or the pattern).
> - **Space Complexity:** $O(n \times m)$, where $n$ is the number of words and $m$ is the length of each word (or the pattern).
> - **Why these complexities occur:** The time complexity is due to the iteration over each word and each character in the word. The space complexity is due to the storage of the mapping from the word to the pattern and from the pattern to the word.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same as the brute force approach, but with a more efficient implementation.
- Detailed breakdown of the approach:
  1. Create a mapping from the word to the pattern.
  2. Check if the mapping is valid (i.e., each character in the word maps to a unique character in the pattern, and vice versa).
  3. If the mapping is valid, add the word to the result list.
- Proof of optimality: This approach is optimal because it checks each word individually and uses a mapping to efficiently check the validity of the mapping.

```cpp
vector<string> findAndReplacePattern(vector<string>& words, string pattern) {
    vector<string> result;
    for (const auto& word : words) {
        if (word.size() != pattern.size()) continue;
        unordered_map<char, char> wordToPattern;
        unordered_map<char, char> patternToWord;
        for (int i = 0; i < word.size(); ++i) {
            char wordChar = word[i];
            char patternChar = pattern[i];
            if ((wordToPattern.count(wordChar) && wordToPattern[wordChar] != patternChar) ||
                (patternToWord.count(patternChar) && patternToWord[patternChar] != wordChar)) {
                break;
            }
            wordToPattern[wordChar] = patternChar;
            patternToWord[patternChar] = wordChar;
            if (i == word.size() - 1) {
                result.push_back(word);
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where $n$ is the number of words and $m$ is the length of each word (or the pattern).
> - **Space Complexity:** $O(n \times m)$, where $n$ is the number of words and $m$ is the length of each word (or the pattern).
> - **Optimality proof:** This approach is optimal because it checks each word individually and uses a mapping to efficiently check the validity of the mapping.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: 
  - **_Hashing_**: Using `unordered_map` to efficiently store and retrieve mappings between characters.
  - **_Pattern Matching_**: Checking if a word matches a given pattern by replacing characters.
- Problem-solving patterns identified: 
  - **_Iterative Approach_**: Iterating over each word and checking if it matches the pattern.
- Optimization techniques learned: 
  - **_Early Pruning_**: Continuing to the next word if the current word does not match the pattern in length.
- Similar problems to practice: 
  - **_Regular Expression Matching_**: Checking if a string matches a given regular expression.

**Mistakes to Avoid:**
- Common implementation errors: 
  - Not checking if the word matches the pattern in length before attempting to match the pattern.
  - Not using a mapping to efficiently check the validity of the mapping.
- Edge cases to watch for: 
  - Empty words or patterns.
  - Words or patterns with different lengths.
- Performance pitfalls: 
  - Not using `unordered_map` for efficient lookup and insertion.
- Testing considerations: 
  - Test cases with different word lengths and patterns.
  - Test cases with empty words or patterns.