## Smallest Substring with Identical Characters I
**Problem Link:** https://leetcode.com/problems/smallest-substring-with-identical-characters-i/description

**Problem Statement:**
- Input: a string `s` containing only lowercase English letters.
- Constraints: $1 \leq s.length \leq 10^5$.
- Expected output: the length of the smallest substring with identical characters. If there is no such substring, return -1.
- Key requirements: finding the smallest substring that consists entirely of the same character.
- Example test cases:
  - Input: "aa"
    - Output: 1
    - Explanation: The smallest substring with identical characters is "a".
  - Input: "ab"
    - Output: -1
    - Explanation: There is no substring with identical characters.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: to find the smallest substring with identical characters, we can iterate over all possible substrings of the input string `s`.
- Step-by-step breakdown of the solution:
  1. Iterate over the string `s` to generate all possible substrings.
  2. For each substring, check if all characters are identical.
  3. Keep track of the minimum length of such substrings.
- Why this approach comes to mind first: it is straightforward and ensures we consider all possibilities.

```cpp
int smallestSubstringWithIdenticalCharacters(string s) {
    int minLen = INT_MAX;
    for (int i = 0; i < s.length(); ++i) {
        for (int j = i + 1; j <= s.length(); ++j) {
            string substr = s.substr(i, j - i);
            if (isIdentical(substr)) {
                minLen = min(minLen, (int)substr.length());
            }
        }
    }
    return minLen == INT_MAX ? -1 : minLen;
}

bool isIdentical(string s) {
    char c = s[0];
    for (char ch : s) {
        if (ch != c) return false;
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the string `s`. This is because we generate all substrings ($O(n^2)$) and for each, we check if all characters are identical ($O(n)$).
> - **Space Complexity:** $O(n)$, as we need to store the substrings.
> - **Why these complexities occur:** The nested loops for generating substrings and the additional loop for checking identical characters contribute to the time complexity. The space complexity is due to the storage of substrings.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: instead of generating all substrings and checking for identical characters, we can directly find the smallest substring with identical characters by iterating over the string and expanding the window of identical characters.
- Detailed breakdown of the approach:
  1. Initialize the minimum length to infinity.
  2. Iterate over the string, and for each character, expand a window of identical characters.
  3. Update the minimum length as we find smaller substrings with identical characters.
- Proof of optimality: this approach ensures we consider all substrings with identical characters without generating all possible substrings, thus reducing the time complexity significantly.

```cpp
int smallestSubstringWithIdenticalCharacters(string s) {
    int minLen = INT_MAX;
    for (int i = 0; i < s.length(); ++i) {
        char c = s[i];
        int len = 1;
        while (i + 1 < s.length() && s[i + 1] == c) {
            i++;
            len++;
        }
        minLen = min(minLen, len);
    }
    return minLen == INT_MAX ? -1 : minLen;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we make a single pass through the string.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space.
> - **Optimality proof:** This approach is optimal because it has a linear time complexity and uses minimal space, making it the most efficient solution for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: window expansion, substring generation, and optimization techniques.
- Problem-solving patterns identified: reducing complexity by avoiding unnecessary computations and using efficient data structures.
- Optimization techniques learned: avoiding unnecessary loops and using direct window expansion.
- Similar problems to practice: finding the longest substring with identical characters, smallest substring containing a specific character, etc.

**Mistakes to Avoid:**
- Common implementation errors: incorrect loop bounds, missing edge cases (e.g., empty string), and inefficient algorithms.
- Edge cases to watch for: empty strings, strings with a single character, and strings with no substrings of identical characters.
- Performance pitfalls: using $O(n^3)$ algorithms when $O(n)$ solutions are possible.
- Testing considerations: ensure to test with various inputs, including edge cases and large inputs to verify performance.