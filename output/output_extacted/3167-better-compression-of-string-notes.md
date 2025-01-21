## Better Compression of String

**Problem Link:** https://leetcode.com/problems/better-compression-of-string/description

**Problem Statement:**
- Input format: A string `s` containing only lowercase letters.
- Constraints: `1 <= s.length <= 400`.
- Expected output format: The compressed string or the original string if compression does not reduce the length.
- Key requirements and edge cases to consider: Handle strings with repeated characters, strings with no repeated characters, and strings with alternating characters.
- Example test cases with explanations:
  - Input: `"aabcccccaaa"`; Output: `"a2c5a3"`.
  - Input: `"abcdef"`; Output: `"abcdef"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through the string and count consecutive occurrences of each character.
- Step-by-step breakdown of the solution:
  1. Initialize an empty string `result` to store the compressed string.
  2. Initialize a counter `count` to count consecutive occurrences of a character.
  3. Iterate through the string `s`.
  4. If the current character is the same as the previous one, increment the counter.
  5. If the current character is different from the previous one, append the previous character and its count to `result`, and reset the counter.
  6. After the loop, append the last character and its count to `result`.
- Why this approach comes to mind first: It directly addresses the problem by iterating through the string and counting consecutive occurrences of each character.

```cpp
string compress(string s) {
    if (s.length() <= 2) return s;
    string result = "";
    int count = 1;
    for (int i = 1; i <= s.length(); i++) {
        if (i == s.length() || s[i] != s[i - 1]) {
            result += s[i - 1];
            result += to_string(count);
            count = 1;
        } else {
            count++;
        }
    }
    return result.length() < s.length() ? result : s;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string, because we make one pass through the string.
> - **Space Complexity:** $O(n)$, because in the worst case, the compressed string could be as long as the original string.
> - **Why these complexities occur:** The iteration through the string and the construction of the compressed string lead to these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same as the brute force approach, as it already has a linear time complexity.
- Detailed breakdown of the approach: The brute force approach is already optimal in terms of time complexity.
- Proof of optimality: Since we must examine each character at least once to determine if it should be included in the compressed string, the time complexity cannot be less than $O(n)$.
- Why further optimization is impossible: The brute force approach already achieves the best possible time complexity for this problem.

```cpp
string compress(string s) {
    if (s.length() <= 2) return s;
    string result = "";
    int count = 1;
    for (int i = 1; i <= s.length(); i++) {
        if (i == s.length() || s[i] != s[i - 1]) {
            result += s[i - 1];
            result += to_string(count);
            count = 1;
        } else {
            count++;
        }
    }
    return result.length() < s.length() ? result : s;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string.
> - **Space Complexity:** $O(n)$, because in the worst case, the compressed string could be as long as the original string.
> - **Optimality proof:** The optimal approach has the same time complexity as the brute force approach, proving that it is indeed optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: String manipulation, character counting, and basic compression techniques.
- Problem-solving patterns identified: Iterating through a string to collect data and then constructing a new string based on that data.
- Optimization techniques learned: Recognizing when a brute force approach is already optimal due to the inherent complexity of the problem.
- Similar problems to practice: Other string compression problems, such as Run-Length Encoding (RLE).

**Mistakes to Avoid:**
- Common implementation errors: Off-by-one errors when iterating through the string, incorrect counting of consecutive characters.
- Edge cases to watch for: Empty strings, strings with a single character, strings with no repeated characters.
- Performance pitfalls: Using inefficient string concatenation methods, not checking for the case where the compressed string is longer than the original string.
- Testing considerations: Thoroughly testing the function with a variety of input strings, including edge cases.