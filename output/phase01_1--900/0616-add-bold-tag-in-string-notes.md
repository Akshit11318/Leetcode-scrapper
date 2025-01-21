## Add Bold Tag in String
**Problem Link:** https://leetcode.com/problems/add-bold-tag-in-string/description

**Problem Statement:**
- Input format and constraints: Given a string `s` and a list of strings `words`, add `<b>` tags around each occurrence of the `words` in `s`.
- Expected output format: A string with `<b>` tags around each occurrence of the `words`.
- Key requirements and edge cases to consider: 
    * Non-overlapping occurrences of words.
    * Multiple occurrences of the same word.
    * Empty input string or words list.
- Example test cases with explanations:
    * Input: `s = "abcxyz123"`, `words = ["abc","123"]`. Output: `"abc<b>abc</b>xyz<b>123</b>"`.
    * Input: `s = "aaabbcc"`, `words = ["aaa","aab","bc"]`. Output: `"aaabbcc"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each word in the list and check if it exists in the string. If it does, add `<b>` tags around it.
- Step-by-step breakdown of the solution:
    1. Iterate over each word in the list.
    2. For each word, iterate over the string to find all occurrences of the word.
    3. For each occurrence, add `<b>` tags around it.
- Why this approach comes to mind first: It is the most straightforward way to solve the problem.

```cpp
string addBoldTag(string s, vector<string>& words) {
    string result = s;
    for (const auto& word : words) {
        size_t pos = result.find(word);
        while (pos != string::npos) {
            result.replace(pos, word.size(), "<b>" + word + "</b>");
            pos = result.find(word, pos + word.size() + 7); // 7 is the length of "<b></b>"
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m \times k)$ where $n$ is the length of the string, $m$ is the number of words, and $k$ is the maximum length of a word.
> - **Space Complexity:** $O(n)$ where $n$ is the length of the string.
> - **Why these complexities occur:** The brute force approach involves iterating over each word in the list, and for each word, iterating over the string to find all occurrences of the word.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a single pass over the string to find all occurrences of the words.
- Detailed breakdown of the approach:
    1. Initialize an array to keep track of the positions where a word starts.
    2. Iterate over each word in the list.
    3. For each word, iterate over the string to find all occurrences of the word and mark the start positions in the array.
    4. Iterate over the string again and add `<b>` tags around the words based on the marked positions.
- Proof of optimality: This approach only requires two passes over the string, making it more efficient than the brute force approach.

```cpp
string addBoldTag(string s, vector<string>& words) {
    vector<bool> bold(s.size(), false);
    for (const auto& word : words) {
        size_t pos = s.find(word);
        while (pos != string::npos) {
            for (size_t i = pos; i < pos + word.size(); i++) {
                bold[i] = true;
            }
            pos = s.find(word, pos + 1);
        }
    }
    string result;
    for (size_t i = 0; i < s.size(); i++) {
        if (bold[i] && (i == 0 || !bold[i - 1])) {
            result += "<b>";
        }
        result += s[i];
        if (bold[i] && (i == s.size() - 1 || !bold[i + 1])) {
            result += "</b>";
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m + n)$ where $n$ is the length of the string and $m$ is the number of words.
> - **Space Complexity:** $O(n)$ where $n$ is the length of the string.
> - **Optimality proof:** The optimal approach reduces the number of passes over the string, making it more efficient than the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: 
    * Using a single pass over the string to find all occurrences of the words.
    * Using a boolean array to keep track of the positions where a word starts.
- Problem-solving patterns identified: 
    * Using a two-pass approach to solve the problem.
    * Using a boolean array to mark the positions where a word starts.
- Optimization techniques learned: 
    * Reducing the number of passes over the string.
    * Using a boolean array to keep track of the positions where a word starts.

**Mistakes to Avoid:**
- Common implementation errors: 
    * Not initializing the boolean array correctly.
    * Not marking the positions where a word starts correctly.
- Edge cases to watch for: 
    * Empty input string or words list.
    * Non-overlapping occurrences of words.
- Performance pitfalls: 
    * Using a brute force approach that involves multiple passes over the string.
- Testing considerations: 
    * Testing with different input strings and words lists.
    * Testing with edge cases such as empty input string or words list.