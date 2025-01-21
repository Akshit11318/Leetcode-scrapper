## Length of Last Word
**Problem Link:** https://leetcode.com/problems/length-of-last-word/description

**Problem Statement:**
- Input: A string `s` containing one or more words separated by spaces.
- Constraints: `1 <= s.length <= 10^4`, `s` consists of only English letters and spaces.
- Expected Output: The length of the last word in the input string.
- Key Requirements: The solution should handle strings with leading, trailing, or multiple consecutive spaces correctly.
- Edge Cases: Empty strings, strings with a single word, strings with multiple words, and strings with leading/trailing spaces.
- Example Test Cases:
  - Input: `"Hello World"`, Output: `5`
  - Input: `"   fly me   to   the moon  "`, Output: `4`
  - Input: `"a"`, Output: `1`

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves iterating through the string from the end to find the last word and then calculating its length.
- This approach comes to mind first because it directly addresses the requirement to find the length of the last word.

```cpp
int lengthOfLastWord(string s) {
    // Remove trailing spaces
    while (!s.empty() && s.back() == ' ') {
        s.pop_back();
    }

    int length = 0;
    // Iterate through the string from the end
    for (int i = s.size() - 1; i >= 0; --i) {
        if (s[i] == ' ') {
            break;
        }
        length++;
    }
    return length;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string, because we potentially iterate through the entire string once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the length variable and the loop counter.
> - **Why these complexities occur:** The time complexity is linear because we might need to remove trailing spaces and then iterate through the string to find the last word. The space complexity is constant because we do not use any data structures that scale with the input size.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to start from the end of the string and iterate backwards to find the first space after a word, which indicates the end of the last word.
- This approach is optimal because it minimizes the number of iterations by directly targeting the last word.

```cpp
int lengthOfLastWord(string s) {
    int length = 0;
    bool wordStarted = false;
    // Iterate through the string from the end
    for (int i = s.size() - 1; i >= 0; --i) {
        if (s[i] != ' ') {
            wordStarted = true;
            length++;
        } else if (wordStarted) {
            break;
        }
    }
    return length;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string, because we potentially iterate through the entire string once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the length variable, the loop counter, and a boolean flag.
> - **Optimality proof:** This approach is optimal because it achieves the best possible time complexity for this problem, which is linear, by directly finding the last word without unnecessary iterations or additional space usage.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional checks, and optimization by minimizing unnecessary operations.
- Problem-solving patterns identified: Starting from the end of the string to find the last occurrence of a pattern (in this case, a word).
- Optimization techniques learned: Removing unnecessary iterations and using boolean flags to track state.
- Similar problems to practice: Other string manipulation problems, such as finding the first occurrence of a pattern or counting specific characters.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases like empty strings or strings with only spaces.
- Edge cases to watch for: Leading, trailing, or multiple consecutive spaces.
- Performance pitfalls: Using inefficient algorithms that have higher time or space complexity than necessary.
- Testing considerations: Thoroughly testing with a variety of inputs, including edge cases, to ensure the solution works correctly in all scenarios.