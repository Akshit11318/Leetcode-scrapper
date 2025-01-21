## Reverse Prefix of Word
**Problem Link:** https://leetcode.com/problems/reverse-prefix-of-word/description

**Problem Statement:**
- Input: A string `word` and a character `ch`.
- Constraints: `1 <= word.length <= 250`, `word` consists of lowercase English letters, and `ch` is a lowercase English letter.
- Expected output: The word after reversing the prefix that ends with the character `ch`.
- Key requirements and edge cases:
  - If `ch` is not found in `word`, return the original `word`.
  - If `ch` is found multiple times, reverse the prefix up to the first occurrence of `ch`.
- Example test cases:
  - Input: `word = "abcdefd", ch = "d"`, Output: `"dcbaefd"`
  - Input: `word = "xyxz", ch = "z"`, Output: `"zxyx"`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves finding the first occurrence of `ch` in `word` and then reversing the prefix up to that point.
- Step-by-step breakdown:
  1. Find the index of the first occurrence of `ch` in `word`.
  2. If `ch` is not found, return the original `word`.
  3. Otherwise, reverse the substring from the beginning of `word` to the index of `ch`.
  4. Concatenate the reversed prefix with the rest of `word`.

```cpp
string reversePrefix(string word, char ch) {
    int index = word.find(ch);
    if (index == string::npos) {
        return word;
    }
    string prefix = word.substr(0, index + 1);
    reverse(prefix.begin(), prefix.end());
    return prefix + word.substr(index + 1);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `word`, because we are potentially scanning the entire string to find `ch` and then reversing a part of it.
> - **Space Complexity:** $O(n)$, as we are creating new strings for the prefix and the rest of `word`.
> - **Why these complexities occur:** The time complexity is linear due to the string operations, and the space complexity is also linear because of the new strings created.

---

### Optimal Approach

**Explanation:**
- The key insight is to use the same approach as the brute force but optimize it by avoiding unnecessary string creations and operations.
- Detailed breakdown:
  1. Find the index of `ch` in `word`.
  2. If `ch` is not found, return `word` as is.
  3. Reverse the prefix in-place or by creating a new string only for the reversed part.
  4. Concatenate the reversed prefix with the rest of `word`.

```cpp
string reversePrefix(string word, char ch) {
    int index = word.find(ch);
    if (index == string::npos) {
        return word;
    }
    string reversedPrefix = word.substr(0, index + 1);
    reverse(reversedPrefix.begin(), reversedPrefix.end());
    return reversedPrefix + word.substr(index + 1);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `word`, due to finding `ch` and reversing the prefix.
> - **Space Complexity:** $O(n)$, as we create a new string for the reversed prefix.
> - **Optimality proof:** This approach is optimal because we must at least scan `word` once to find `ch`, and then we must reverse the prefix, both of which are linear operations. Creating a new string for the reversed prefix is unavoidable if we want to modify the original string's prefix without altering the rest of it.

---

### Final Notes

**Learning Points:**
- The problem demonstrates the importance of understanding string manipulation functions in C++.
- It highlights the need to consider the trade-offs between time and space complexity in algorithm design.
- The solution illustrates how to approach problems that involve modifying parts of a string.

**Mistakes to Avoid:**
- Not checking for the case where `ch` is not found in `word`.
- Creating unnecessary intermediate strings, which can increase space complexity.
- Not considering the impact of string operations on time complexity.

By following this approach, you can efficiently solve the "Reverse Prefix of Word" problem while understanding the complexities involved and how to optimize your solution.