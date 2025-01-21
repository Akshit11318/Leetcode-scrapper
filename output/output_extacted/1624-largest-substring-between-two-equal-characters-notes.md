## Largest Substring Between Two Equal Characters
**Problem Link:** https://leetcode.com/problems/largest-substring-between-two-equal-characters/description

**Problem Statement:**
- Input: A string `s` containing only lowercase English letters.
- Constraints: `1 <= s.length <= 10^5`.
- Expected Output: The length of the largest substring between two equal characters.
- Key Requirements: Find the maximum length of a substring that starts and ends with the same character.
- Edge Cases: Consider strings with repeated characters, single-character strings, and empty strings.
- Example Test Cases:
  - Input: `s = "aa"`
    - Output: `2`
    - Explanation: The substring `"aa"` is between two equal characters.
  - Input: `s = "abca"`
    - Output: `2`
    - Explanation: The substring `"bca"` is between two equal characters.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Iterate over all substrings of `s` and check if the first and last characters are equal.
- Step-by-step breakdown:
  1. Generate all possible substrings of `s`.
  2. For each substring, check if the first and last characters are equal.
  3. Keep track of the maximum length of such substrings.
- Why this approach comes to mind first: It's a straightforward, exhaustive search.

```cpp
int maxLengthBetweenEqualCharacters(string s) {
    int max_length = 0;
    for (int i = 0; i < s.length(); i++) {
        for (int j = i + 1; j < s.length(); j++) {
            if (s[i] == s[j]) {
                max_length = max(max_length, j - i - 1);
            }
        }
    }
    return max_length;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of `s`. This is because we're generating all possible substrings (quadratic number of them) and checking each one.
> - **Space Complexity:** $O(1)$, as we're only using a constant amount of space to store the maximum length.
> - **Why these complexities occur:** The nested loops over the string cause the quadratic time complexity, while the constant space usage is due to only keeping track of a single variable.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Instead of checking all substrings, we can iterate over the string and for each character, find the first and last occurrence of that character.
- Detailed breakdown:
  1. Iterate over each unique character in `s`.
  2. For each character, find its first and last occurrence in `s`.
  3. Calculate the length of the substring between these two occurrences.
  4. Update the maximum length if necessary.
- Proof of optimality: This approach is optimal because it avoids the unnecessary quadratic complexity of generating all substrings, instead focusing on the relevant substrings defined by the first and last occurrences of each character.

```cpp
int maxLengthBetweenEqualCharacters(string s) {
    int max_length = 0;
    for (char c = 'a'; c <= 'z'; c++) {
        int first_occurrence = s.find(c);
        if (first_occurrence != string::npos) {
            int last_occurrence = s.rfind(c);
            max_length = max(max_length, last_occurrence - first_occurrence - 1);
        }
    }
    return max_length;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the length of `s` and $m$ is the number of unique characters (at most 26 for lowercase English letters). This is because we're iterating over each unique character and then finding its first and last occurrence in `s`.
> - **Space Complexity:** $O(1)$, as we're only using a constant amount of space to store the maximum length and the current character.
> - **Optimality proof:** This is the best possible complexity because we must at least read the input string once, and our approach does this while minimizing unnecessary work.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration over substrings, optimization by focusing on relevant substrings.
- Problem-solving patterns identified: Avoiding brute force by exploiting problem-specific structures.
- Optimization techniques learned: Reducing complexity by focusing on necessary computations.
- Similar problems to practice: Other substring problems, such as finding the longest palindromic substring.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating substring lengths or missing edge cases.
- Edge cases to watch for: Empty strings, single-character strings, and strings with no repeated characters.
- Performance pitfalls: Using brute force approaches for large inputs.
- Testing considerations: Ensure to test with a variety of inputs, including edge cases and large strings.