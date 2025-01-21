## Minimum Changes to Make K Semi-Palindromes
**Problem Link:** https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/description

**Problem Statement:**
- Input format: Two strings `s` and `t`, and an integer `k`.
- Constraints: The lengths of `s` and `t` are both `n`, where `1 <= n <= 1000`. `0 <= k <= n`.
- Expected output format: The minimum number of changes required to make `s` and `t` `k`-semi-palindromes.
- Key requirements: A `k`-semi-palindrome is a string that can be made into a palindrome by changing at most `k` characters.
- Edge cases: If `k` is greater than or equal to the length of the string, it is always possible to make the string a palindrome.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Compare characters from the start and end of both strings, and count the differences.
- Step-by-step breakdown of the solution:
  1. Initialize two pointers, one at the start and one at the end of each string.
  2. Compare characters at the current positions of the pointers. If they are different, increment a counter for the number of changes needed.
  3. Move the pointers towards the center of the strings.
  4. Repeat steps 2-3 until the pointers meet or cross.
  5. Repeat the process for the second string.
- Why this approach comes to mind first: It is a straightforward way to compare the strings and count the differences.

```cpp
int minChanges(string s, string t, int k) {
    int changes = 0;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] != s[s.size() - 1 - i]) changes++;
        if (t[i] != t[t.size() - 1 - i]) changes++;
    }
    return changes;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the strings.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the counter.
> - **Why these complexities occur:** The time complexity is linear because we only iterate over the strings once, and the space complexity is constant because we only use a fixed amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We only need to count the differences between the strings and their reversals, and then find the minimum of these two counts.
- Detailed breakdown of the approach:
  1. Initialize two counters, one for the differences between `s` and its reversal, and one for the differences between `t` and its reversal.
  2. Compare characters from the start and end of each string, and increment the corresponding counter if they are different.
  3. Return the minimum of the two counters.
- Proof of optimality: This approach is optimal because it only requires a single pass over the strings, and it correctly counts the minimum number of changes needed to make the strings `k`-semi-palindromes.

```cpp
int minChanges(string s, string t, int k) {
    int changesS = 0;
    int changesT = 0;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] != s[s.size() - 1 - i]) changesS++;
        if (t[i] != t[t.size() - 1 - i]) changesT++;
    }
    return min(changesS, changesT);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the strings.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the counters.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the strings, and it correctly counts the minimum number of changes needed to make the strings `k`-semi-palindromes.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: String manipulation, counting differences, and finding the minimum of two values.
- Problem-solving patterns identified: Using counters to keep track of differences, and finding the minimum of two values.
- Optimization techniques learned: Using a single pass over the strings to count the differences, and using a constant amount of space to store the counters.
- Similar problems to practice: Other string manipulation problems, such as finding the longest common substring or the minimum edit distance between two strings.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the counters correctly, or not comparing the characters correctly.
- Edge cases to watch for: When `k` is greater than or equal to the length of the string, it is always possible to make the string a palindrome.
- Performance pitfalls: Using a nested loop to compare the characters, which would result in a time complexity of $O(n^2)$.
- Testing considerations: Testing the function with different inputs, including edge cases and boundary cases.