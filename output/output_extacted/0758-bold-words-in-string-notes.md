## Bold Words in String
**Problem Link:** https://leetcode.com/problems/bold-words-in-string/description

**Problem Statement:**
- Input format: Given a string `s` and an array of strings `words`, each word in `words` should be bolded in `s`.
- Constraints: $1 \leq s.length \leq 500$, $1 \leq words.length \leq 500$, $1 \leq words[i].length \leq 30$, `s` and `words[i]` consist of lowercase letters, and `words` does not contain duplicates.
- Expected output format: A string with all occurrences of `words` in `s` bolded.
- Key requirements and edge cases to consider:
  - The input string `s` and the array of words `words` can contain any lowercase letters.
  - The array `words` does not contain duplicates, but a word can appear multiple times in `s`.
  - The output string should have all occurrences of `words` in `s` wrapped in `<b>` and `</b>` tags.

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate through each word in `words` and check if it exists in `s`.
- For each occurrence of a word in `s`, we will replace it with the bolded version.
- This approach is straightforward but may not be efficient for large inputs due to repeated string operations.

```cpp
string boldWords(vector<string>& words, string s) {
    for (const auto& word : words) {
        size_t pos = s.find(word);
        while (pos != string::npos) {
            s.replace(pos, word.length(), "<b>" + word + "</b>");
            pos = s.find(word, pos + word.length() + 6); // 6 is the length of "<b>" and "</b>"
        }
    }
    return s;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$, where $n$ is the length of `s`, $m$ is the number of words, and $k$ is the average length of a word. The reason is that for each word, we potentially scan the entire string `s`.
> - **Space Complexity:** $O(n + m \cdot k)$, as we need to store the modified string and potentially all words.
> - **Why these complexities occur:** The brute force approach involves repeated string searching and replacement, which are expensive operations, especially for large inputs.

### Optimal Approach (Required)

**Explanation:**
- Instead of replacing words in `s` directly, we can iterate through `s` and check if the current position is the start of any word in `words`.
- We use a boolean array `bold` of the same length as `s` to mark the positions that should be bolded.
- Then, we construct the result string by checking the `bold` array and adding `<b>` and `</b>` tags accordingly.

```cpp
string boldWords(vector<string>& words, string s) {
    vector<bool> bold(s.length(), false);
    for (const auto& word : words) {
        size_t pos = s.find(word);
        while (pos != string::npos) {
            for (size_t i = pos; i < pos + word.length(); ++i) {
                bold[i] = true;
            }
            pos = s.find(word, pos + 1);
        }
    }
    string result;
    bool inBold = false;
    for (size_t i = 0; i < s.length(); ++i) {
        if (bold[i] && !inBold) {
            result += "<b>";
            inBold = true;
        } else if (!bold[i] && inBold) {
            result += "</b>";
            inBold = false;
        }
        result += s[i];
    }
    if (inBold) {
        result += "</b>";
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k + n)$, where the first part comes from finding all occurrences of words in `s`, and the second part comes from constructing the result string.
> - **Space Complexity:** $O(n + m \cdot k)$, for storing the `bold` array and the result string.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through `s` to mark the bold positions and another pass to construct the result string, minimizing the number of operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: string manipulation, iteration, and marking positions for later processing.
- Problem-solving patterns identified: using a separate data structure (`bold` array) to mark positions that need special handling.
- Optimization techniques learned: reducing the number of string operations by using a boolean array to mark bold positions instead of directly modifying the string.

**Mistakes to Avoid:**
- Common implementation errors: forgetting to handle edge cases, such as when a word is not found in `s` or when `s` is empty.
- Performance pitfalls: using inefficient string operations, such as repeated `replace` calls in the brute force approach.
- Testing considerations: ensuring that the solution handles all possible input cases, including empty strings, single-word inputs, and inputs with multiple occurrences of the same word.