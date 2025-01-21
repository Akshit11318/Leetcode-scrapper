## Replace All Digits with Characters
**Problem Link:** https://leetcode.com/problems/replace-all-digits-with-characters/description

**Problem Statement:**
- Input format and constraints: The input is a string `s` containing only lowercase letters and digits. The string is at most 100 characters long.
- Expected output format: The output is a modified string where all digits are replaced by characters based on the following rule: For every digit `i` found, replace it with the character that is `i` positions ahead of the character that immediately precedes `i` in the string. If `i` is the first character, use 'a' as the reference character.
- Key requirements and edge cases to consider:
  - Handling digits at the beginning of the string.
  - Ensuring the character replacement does not go out of the alphabet range (a-z).
- Example test cases with explanations:
  - "a1c1e1" should return "abcdef" because:
    - '1' after 'a' becomes 'b' ('a' + 1),
    - '1' after 'c' becomes 'd' ('c' + 1),
    - '1' after 'e' becomes 'f' ('e' + 1).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through each character in the string, and whenever a digit is encountered, calculate the character to replace it based on the preceding character.
- Step-by-step breakdown of the solution:
  1. Initialize an empty result string.
  2. Iterate through the input string. For each character:
     - If the character is a letter, append it to the result string.
     - If the character is a digit, find the preceding character in the result string (or use 'a' if it's the first character), calculate the character to replace the digit, and append this new character to the result string.
  3. Return the result string.
- Why this approach comes to mind first: It's a straightforward, intuitive way to solve the problem by directly following the given rules for replacing digits with characters.

```cpp
string replaceDigits(string s) {
    string result;
    for (int i = 0; i < s.length(); i++) {
        if (isalpha(s[i])) {
            result += s[i];
        } else {
            char baseChar = (i > 0) ? result.back() : 'a';
            result += baseChar + (s[i] - '0');
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the string, because we are iterating through the string once.
> - **Space Complexity:** $O(n)$ for storing the result string.
> - **Why these complexities occur:** The iteration through the string and the storage of the result string are linear operations with respect to the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved in a single pass through the string without any additional data structures other than the output string. This is because each replacement depends only on the immediately preceding character, which we can keep track of during the iteration.
- Detailed breakdown of the approach:
  1. Initialize an empty result string.
  2. Iterate through the input string. For each character:
     - If the character is a letter, append it to the result string.
     - If the character is a digit, calculate the character to replace the digit based on the last character in the result string (or 'a' if the result string is empty), and append this new character to the result string.
  3. Return the result string.
- Proof of optimality: This solution is optimal because it only requires a single pass through the input string, and it uses a minimal amount of extra memory to store the output string.

```cpp
string replaceDigits(string s) {
    string result;
    for (char c : s) {
        if (isalpha(c)) {
            result += c;
        } else {
            char baseChar = result.empty() ? 'a' : result.back();
            result += baseChar + (c - '0');
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the string, because we are iterating through the string once.
> - **Space Complexity:** $O(n)$ for storing the result string.
> - **Optimality proof:** This is the best possible time complexity because we must at least read the input string once. The space complexity is also optimal because we need to store the output string.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Single-pass iteration, in-place calculation, and minimal extra memory usage.
- Problem-solving patterns identified: Handling each character in a string based on its type (digit or letter) and its position.
- Optimization techniques learned: Avoiding unnecessary data structures and minimizing the number of passes through the input data.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect handling of edge cases (e.g., digits at the beginning of the string) or miscalculating the replacement character.
- Edge cases to watch for: Digits at the start of the string, and ensuring the replacement does not go out of the alphabet range.
- Performance pitfalls: Using inefficient data structures or algorithms that lead to higher time or space complexities than necessary.
- Testing considerations: Thoroughly testing with various inputs, including edge cases, to ensure the solution works correctly in all scenarios.