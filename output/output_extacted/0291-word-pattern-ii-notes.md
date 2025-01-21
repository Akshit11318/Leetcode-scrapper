## Word Pattern II
**Problem Link:** https://leetcode.com/problems/word-pattern-ii/description

**Problem Statement:**
- Input format and constraints: The problem involves two strings, `pattern` and `s`, where `pattern` consists of lowercase English letters and `s` is a string consisting of lowercase English letters. The goal is to determine if `s` matches `pattern`.
- Expected output format: A boolean indicating whether `s` matches `pattern`.
- Key requirements and edge cases to consider: Each character in `pattern` must map to a non-empty substring in `s`, and each substring in `s` must map to exactly one character in `pattern`.
- Example test cases with explanations:
  - Input: `pattern = "abab"`, `s = "redblueredblue"` Output: `true`
  - Input: `pattern = "aaaa"`, `s = "asdasdasd"` Output: `true`
  - Input: `pattern = "aabb"`, `s = "abcabc"` Output: `false`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The brute force approach involves checking every possible substring of `s` to see if it matches the given `pattern`.
- Step-by-step breakdown of the solution:
  1. Generate all possible substrings of `s`.
  2. For each possible mapping of `pattern` to substrings of `s`, check if the mapping is valid.
  3. If a valid mapping is found, return `true`. If no valid mapping is found after checking all possibilities, return `false`.
- Why this approach comes to mind first: It's a straightforward way to solve the problem, but it's inefficient due to the large number of possible substrings and mappings.

```cpp
bool wordPatternMatch(string pattern, string s) {
    unordered_map<char, string> charToSubstr;
    unordered_map<string, char> substrToChar;
    return dfs(pattern, s, 0, 0, charToSubstr, substrToChar);
}

bool dfs(string& pattern, string& s, int patternIndex, int sIndex, 
         unordered_map<char, string>& charToSubstr, unordered_map<string, char>& substrToChar) {
    if (patternIndex == pattern.size() && sIndex == s.size()) return true;
    if (patternIndex == pattern.size() || sIndex == s.size()) return false;

    char currentChar = pattern[patternIndex];
    if (charToSubstr.count(currentChar)) {
        string mappedSubstr = charToSubstr[currentChar];
        if (sIndex + mappedSubstr.size() > s.size() || s.substr(sIndex, mappedSubstr.size()) != mappedSubstr) {
            return false;
        }
        return dfs(pattern, s, patternIndex + 1, sIndex + mappedSubstr.size(), charToSubstr, substrToChar);
    }

    for (int i = sIndex + 1; i <= s.size(); ++i) {
        string substr = s.substr(sIndex, i - sIndex);
        if (substrToChar.count(substr)) continue;
        charToSubstr[currentChar] = substr;
        substrToChar[substr] = currentChar;
        if (dfs(pattern, s, patternIndex + 1, i, charToSubstr, substrToChar)) return true;
        charToSubstr.erase(currentChar);
        substrToChar.erase(substr);
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{|s|})$ where $|s|$ is the length of string `s`, because in the worst case, we might need to try all possible substrings of `s`.
> - **Space Complexity:** $O(|s| + |pattern|)$ for the recursion stack and the maps.
> - **Why these complexities occur:** The high time complexity comes from the brute force nature of trying all possible substrings and mappings.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using depth-first search (DFS) with backtracking, similar to the brute force approach. However, we can optimize it by using two maps to keep track of the mapping between characters in the pattern and substrings in `s`.
- Detailed breakdown of the approach:
  1. Initialize two maps, `charToSubstr` and `substrToChar`, to keep track of the mapping between characters and substrings.
  2. Perform DFS with backtracking to try all possible mappings.
  3. If a character in the pattern is already mapped to a substring, check if the current substring matches the mapped substring. If not, return false.
  4. If a substring is already mapped to a character, skip it to avoid duplicate mappings.
- Proof of optimality: This approach is optimal because it tries all possible mappings in a systematic way, avoiding duplicate work by using the two maps to keep track of the current mapping.

```cpp
bool wordPatternMatch(string pattern, string s) {
    unordered_map<char, string> charToSubstr;
    unordered_map<string, char> substrToChar;
    return dfs(pattern, s, 0, 0, charToSubstr, substrToChar);
}

bool dfs(string& pattern, string& s, int patternIndex, int sIndex, 
         unordered_map<char, string>& charToSubstr, unordered_map<string, char>& substrToChar) {
    if (patternIndex == pattern.size() && sIndex == s.size()) return true;
    if (patternIndex == pattern.size() || sIndex == s.size()) return false;

    char currentChar = pattern[patternIndex];
    if (charToSubstr.count(currentChar)) {
        string mappedSubstr = charToSubstr[currentChar];
        if (sIndex + mappedSubstr.size() > s.size() || s.substr(sIndex, mappedSubstr.size()) != mappedSubstr) {
            return false;
        }
        return dfs(pattern, s, patternIndex + 1, sIndex + mappedSubstr.size(), charToSubstr, substrToChar);
    }

    for (int i = sIndex + 1; i <= s.size(); ++i) {
        string substr = s.substr(sIndex, i - sIndex);
        if (substrToChar.count(substr)) continue;
        charToSubstr[currentChar] = substr;
        substrToChar[substr] = currentChar;
        if (dfs(pattern, s, patternIndex + 1, i, charToSubstr, substrToChar)) return true;
        charToSubstr.erase(currentChar);
        substrToChar.erase(substr);
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{|s|})$ where $|s|$ is the length of string `s`, because in the worst case, we might need to try all possible substrings of `s`.
> - **Space Complexity:** $O(|s| + |pattern|)$ for the recursion stack and the maps.
> - **Optimality proof:** This approach is optimal because it tries all possible mappings in a systematic way, avoiding duplicate work by using the two maps to keep track of the current mapping.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-first search (DFS) with backtracking, using maps to keep track of mappings.
- Problem-solving patterns identified: Using systematic search to try all possible solutions, avoiding duplicate work by keeping track of the current state.
- Optimization techniques learned: Using maps to keep track of mappings, avoiding duplicate work by skipping already mapped substrings.
- Similar problems to practice: Other problems involving string matching, pattern recognition, and backtracking.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, not handling duplicate mappings correctly.
- Edge cases to watch for: Empty strings, strings with only one character, patterns with duplicate characters.
- Performance pitfalls: Not using maps to keep track of mappings, not avoiding duplicate work.
- Testing considerations: Test with different input sizes, test with different patterns and strings.