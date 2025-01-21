## To Lower Case

**Problem Link:** https://leetcode.com/problems/to-lower-case/description

**Problem Statement:**
- Input: a string `s`.
- Output: the string `s` converted to lowercase.
- Key requirements and edge cases to consider: The input string may contain uppercase letters, lowercase letters, and non-alphabetic characters. The solution should handle these cases correctly.
- Example test cases:
  - Input: `"Hello"`
    - Expected output: `"hello"`
  - Input: `"here"`
    - Expected output: `"here"`
  - Input: `"LOVELY"`
    - Expected output: `"lovely"`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each character in the string and check if it is an uppercase letter. If it is, convert it to lowercase.
- Step-by-step breakdown of the solution:
  1. Initialize an empty string to store the result.
  2. Iterate over each character in the input string.
  3. Check if the character is an uppercase letter.
  4. If it is, convert it to lowercase and append it to the result string. Otherwise, append it as is.
- Why this approach comes to mind first: It is a straightforward and intuitive solution that directly addresses the problem statement.

```cpp
string toLowerCase(string s) {
    string result = "";
    for (char c : s) {
        if (c >= 'A' && c <= 'Z') {
            result += c - 'A' + 'a';
        } else {
            result += c;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string, because we are iterating over each character once.
> - **Space Complexity:** $O(n)$, because we are creating a new string that can potentially be as large as the input string.
> - **Why these complexities occur:** The iteration over the input string and the creation of a new string of similar size lead to these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can modify the input string in-place, avoiding the need to create a new string.
- Detailed breakdown of the approach:
  1. Iterate over each character in the input string.
  2. Check if the character is an uppercase letter.
  3. If it is, convert it to lowercase in-place.
- Proof of optimality: This approach has the same time complexity as the brute force approach but improves the space complexity by avoiding the creation of a new string.

```cpp
string toLowerCase(string s) {
    for (char& c : s) {
        if (c >= 'A' && c <= 'Z') {
            c = c - 'A' + 'a';
        }
    }
    return s;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string.
> - **Space Complexity:** $O(1)$, because we are modifying the input string in-place, using no additional space that scales with input size.
> - **Optimality proof:** This solution is optimal because it achieves the best possible time complexity for this problem (since we must at least read the input once) and the best possible space complexity (since we are using no additional space that scales with input size).

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: iteration, character manipulation, and in-place modification.
- Problem-solving patterns identified: checking for specific conditions (uppercase letters) and applying transformations based on those conditions.
- Optimization techniques learned: reducing space complexity by modifying input in-place when possible.

**Mistakes to Avoid:**
- Common implementation errors: forgetting to check the bounds of characters (e.g., assuming all characters are within the ASCII range without checking).
- Edge cases to watch for: non-English characters, special characters, and numbers.
- Performance pitfalls: creating unnecessary temporary strings or data structures.
- Testing considerations: ensure to test with a variety of inputs, including empty strings, strings with only uppercase or lowercase letters, and strings containing non-alphabetic characters.