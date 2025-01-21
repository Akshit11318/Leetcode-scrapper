## Equalize Strings by Adding or Removing Characters at Ends

**Problem Link:** https://leetcode.com/problems/equalize-strings-by-adding-or-removing-characters-at-ends/description

**Problem Statement:**
- Input: Two strings `s` and `t`.
- Constraints: `1 <= s.length, t.length <= 10^5`.
- Expected Output: The length of the longest common prefix that can be obtained by adding or removing characters at the ends of `s` and `t`.
- Key Requirements: Find the length of the longest common prefix that can be achieved by modifying the ends of the strings.
- Edge Cases: Empty strings, strings of different lengths, strings with no common prefix.

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible combination of adding or removing characters at the ends of `s` and `t` to find the longest common prefix.
- Step-by-step breakdown:
  1. Generate all possible prefixes of `s` by removing characters from the start or end.
  2. For each prefix of `s`, check if it is a prefix of `t` by removing characters from the start or end of `t`.
  3. Keep track of the longest common prefix found.
- Why this approach comes to mind first: It is a straightforward method to ensure all possibilities are considered.

```cpp
int equalizeStrings(string s, string t) {
    int maxLen = 0;
    for (int i = 0; i < s.length(); i++) {
        for (int j = i + 1; j <= s.length(); j++) {
            string prefix = s.substr(i, j - i);
            for (int k = 0; k <= t.length(); k++) {
                for (int end = k + 1; end <= t.length(); end++) {
                    string substr = t.substr(k, end - k);
                    if (prefix == substr && prefix.length() > maxLen) {
                        maxLen = prefix.length();
                    }
                }
            }
        }
    }
    return maxLen;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 * m^2)$ where $n$ and $m$ are the lengths of `s` and `t`, respectively. This is because we have four nested loops, each potentially iterating over the length of the strings.
> - **Space Complexity:** $O(1)$, not counting the space needed for the input strings, as we only use a constant amount of space to store the maximum length and loop variables.
> - **Why these complexities occur:** The brute force approach is inherently inefficient due to the exhaustive search over all possible substrings and prefixes.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of checking every possible prefix, we can use a two-pointer technique to find the longest common prefix between `s` and `t` directly, without modifying them.
- Detailed breakdown:
  1. Initialize two pointers, one at the start of `s` and one at the start of `t`.
  2. Compare characters at the current positions of the pointers. If they match, move both pointers forward and increment the length of the common prefix.
  3. If the characters do not match, we have found the longest common prefix.
- Proof of optimality: This approach ensures we find the longest common prefix in a single pass through the strings, making it more efficient than the brute force method.

```cpp
int equalizeStrings(string s, string t) {
    int maxLen = 0;
    for (int i = 0; i < s.length(); i++) {
        for (int j = 0; j < t.length(); j++) {
            int k = 0;
            while (i + k < s.length() && j + k < t.length() && s[i + k] == t[j + k]) {
                k++;
            }
            maxLen = max(maxLen, k);
        }
    }
    return maxLen;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n * m)$ where $n$ and $m$ are the lengths of `s` and `t`, respectively. This is because we have two nested loops over the strings, and inside these loops, we potentially iterate over the rest of the strings once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum length and loop variables.
> - **Optimality proof:** This approach is optimal because it ensures we find the longest common prefix in a single pass through the relevant parts of the strings, without unnecessary comparisons.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two-pointer technique, nested loops for substring comparison.
- Problem-solving patterns identified: Looking for common prefixes or substrings between strings.
- Optimization techniques learned: Avoiding brute force by using more efficient algorithms that reduce the number of comparisons needed.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect loop bounds, missing checks for edge cases like empty strings.
- Edge cases to watch for: Strings of significantly different lengths, strings with no common prefix.
- Performance pitfalls: Using algorithms with high time complexities for large inputs.
- Testing considerations: Ensure to test with a variety of inputs, including edge cases and large strings.