## Shortest Uncommon Substring in an Array
**Problem Link:** https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/description

**Problem Statement:**
- Input: An array of strings `words` and a string `s`.
- Constraints: `1 <= words.length <= 100`, `1 <= words[i].length <= 10`, `1 <= s.length <= 10`.
- Expected Output: The length of the shortest uncommon substring in `s`.
- Key Requirements: A substring is uncommon if it appears in exactly one string in `words`.
- Edge Cases: If no such substring exists, return `-1`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves generating all possible substrings of `s` and checking their occurrence in each string in `words`.
- For each substring, iterate through `words` to count its occurrences.
- If a substring occurs exactly once, it's a candidate for the shortest uncommon substring.

```cpp
int findLUSlength(vector<string>& words, string s) {
    int min_length = INT_MAX;
    for (int i = 0; i < s.size(); i++) {
        for (int j = i + 1; j <= s.size(); j++) {
            string substr = s.substr(i, j - i);
            int count = 0;
            for (const string& word : words) {
                if (word.find(substr) != string::npos) {
                    count++;
                }
            }
            if (count == 1 && substr.size() < min_length) {
                min_length = substr.size();
            }
        }
    }
    return min_length == INT_MAX ? -1 : min_length;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m^3)$, where $n$ is the number of strings in `words` and $m$ is the maximum length of a string. This is because for each character in `s`, we generate all possible substrings and check each one against all strings in `words`.
> - **Space Complexity:** $O(m)$, as we only need to store the current substring being processed.
> - **Why these complexities occur:** The nested loops for generating substrings and checking their occurrences lead to the cubic time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to iterate through `words` and check if `s` contains any substring of each word. If `s` contains a substring of a word, that word cannot be the source of an uncommon substring.
- We can use a `set` to store the lengths of substrings found in `s` for each word.
- If `s` is a substring of any word, return `-1` because there's no uncommon substring.
- Otherwise, iterate through `s` to find the shortest substring not in the set of lengths.

```cpp
int findLUSlength(vector<string>& words, string s) {
    unordered_set<int> lengths;
    for (const string& word : words) {
        for (int i = 0; i < word.size(); i++) {
            for (int j = i + 1; j <= word.size(); j++) {
                string substr = word.substr(i, j - i);
                if (s.find(substr) != string::npos) {
                    lengths.insert(substr.size());
                }
            }
        }
    }
    int length = s.size();
    while (length > 0) {
        if (lengths.find(length) == lengths.end()) {
            return length;
        }
        length--;
    }
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m^3)$, where $n$ is the number of strings in `words` and $m$ is the maximum length of a string. This is because for each word, we generate all possible substrings and check if `s` contains them.
> - **Space Complexity:** $O(m)$, as we store the lengths of substrings found in `s`.
> - **Optimality proof:** This approach is optimal because it checks all possible substrings of `s` and all words in `words`, ensuring that no uncommon substring is missed.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: substring generation, occurrence counting, and set operations.
- Problem-solving patterns identified: iterating through strings and sets to find uncommon elements.
- Optimization techniques learned: using sets to store unique lengths and iterating through `s` to find the shortest uncommon substring.

**Mistakes to Avoid:**
- Common implementation errors: incorrect substring generation, incorrect counting of occurrences.
- Edge cases to watch for: empty strings, strings with no uncommon substrings.
- Performance pitfalls: using inefficient data structures, not optimizing the iteration through `s`.
- Testing considerations: testing with different inputs, including edge cases and large inputs.