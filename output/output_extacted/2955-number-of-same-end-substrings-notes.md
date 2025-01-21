## Number of Same End Substrings
**Problem Link:** https://leetcode.com/problems/number-of-same-end-substrings/description

**Problem Statement:**
- Input: A string `s`.
- Constraints: `1 <= s.length <= 10^5`, `s` consists only of lowercase English letters.
- Expected Output: The number of substrings where the first character is the same as the last character.
- Key Requirements and Edge Cases:
  - Consider substrings of all possible lengths.
  - Count each substring that meets the condition exactly once.
- Example Test Cases:
  - Input: `s = "abc"`, Output: `3` because `"a"`, `"b"`, `"c"` all have the first character the same as the last.
  - Input: `s = "aaa"`, Output: `6` because all substrings ("a", "aa", "aaa") have the first character the same as the last.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible substrings of the given string and check each one to see if the first character is the same as the last character.
- Step-by-Step Breakdown:
  1. Generate all substrings of the given string.
  2. For each substring, compare the first character with the last character.
  3. If they are the same, increment a counter.
- Why this approach comes to mind first: It's straightforward and directly addresses the problem statement by checking every possible substring.

```cpp
int numberOfSubstrings(string s) {
    int count = 0;
    int n = s.length();
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            string substr = s.substr(i, j - i + 1);
            if (substr[0] == substr[substr.length() - 1]) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ where $n$ is the length of the string. This is because we are generating all substrings ($O(n^2)$) and then checking each one, which in the worst case (when all substrings have the same first and last character) could take $O(n)$ time due to string operations.
> - **Space Complexity:** $O(n)$ because we are storing substrings, which in the worst case could be as long as the original string.
> - **Why these complexities occur:** The generation of all substrings and the subsequent checking of each substring's first and last characters lead to these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key Insight: Instead of generating all substrings and then checking them, we can iterate through the string and directly count the substrings that end at the current position and start at any previous position, provided the characters at these positions are the same.
- Detailed Breakdown:
  1. Initialize a counter for the number of substrings.
  2. Iterate through the string. For each character, compare it with all previous characters.
  3. If a match is found, increment the counter because all substrings ending at the current position and starting at the matched position will have the same first and last character.
- Proof of Optimality: This approach is optimal because it avoids unnecessary string operations and directly counts the substrings that meet the condition in a single pass through the string.

```cpp
int numberOfSubstrings(string s) {
    int count = 0;
    int n = s.length();
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            if (s[j] == s[i]) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the length of the string. This is because we are iterating through the string and for each character, we are potentially checking all previous characters.
> - **Space Complexity:** $O(1)$ because we are only using a constant amount of space to store our counter and loop variables.
> - **Optimality Proof:** This is the best possible time complexity for this problem because we must at least read the input string once, which takes $O(n)$ time. The additional $O(n)$ factor comes from the nested loop structure, which is necessary to compare each character with all previous ones.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, comparison, and direct counting.
- Problem-solving patterns identified: Avoiding unnecessary operations (like generating all substrings) and instead directly counting the desired outcomes.
- Optimization techniques learned: Reducing the number of operations by directly counting substrings that meet the condition.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect indexing, not checking for edge cases.
- Edge cases to watch for: Empty strings, strings with a single character.
- Performance pitfalls: Generating all substrings and then checking them, which leads to inefficient time complexity.
- Testing considerations: Ensure to test with strings of varying lengths and characters to cover all edge cases.