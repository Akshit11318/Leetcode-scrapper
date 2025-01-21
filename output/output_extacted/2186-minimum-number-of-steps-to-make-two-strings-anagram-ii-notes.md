## Minimum Number of Steps to Make Two Strings Anagram II

**Problem Link:** https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/description

**Problem Statement:**
- Input: Two strings `s` and `t` consisting of lowercase English letters.
- Constraints: $1 \leq s.length, t.length \leq 10^5$
- Expected Output: The minimum number of steps to make `s` and `t` anagrams of each other.
- Key Requirements: The steps include adding a character to `s` or removing a character from `s`.
- Edge Cases: If `s` and `t` are already anagrams, the output should be 0.

### Brute Force Approach

**Explanation:**
- The initial thought process involves comparing each character in `s` and `t` to determine the differences.
- However, this approach quickly becomes inefficient as it does not consider the optimal way to make `s` and `t` anagrams.
- A brute force approach would involve generating all possible combinations of adding or removing characters from `s` and checking if the resulting string is an anagram of `t`.
- This approach is impractical due to its high time complexity.

```cpp
int minSteps(string s, string t) {
    int res = 0;
    unordered_map<char, int> countS, countT;
    for (char c : s) countS[c]++;
    for (char c : t) countT[c]++;
    for (char c = 'a'; c <= 'z'; c++) {
        res += abs(countS[c] - countT[c]);
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ where $n$ and $m$ are the lengths of `s` and `t`, respectively.
> - **Space Complexity:** $O(1)$ as we are using a constant amount of space to store the count of characters.
> - **Why these complexities occur:** The time complexity occurs because we are iterating over each character in `s` and `t` once. The space complexity occurs because we are using a constant amount of space to store the count of characters.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves using a frequency count to determine the differences between `s` and `t`.
- We can use an `unordered_map` to store the frequency of each character in `s` and `t`.
- The minimum number of steps is the sum of the absolute differences between the frequency counts of each character.
- This approach is optimal because it only requires a single pass over `s` and `t`.

```cpp
int minSteps(string s, string t) {
    int res = 0;
    unordered_map<char, int> countS, countT;
    for (char c : s) countS[c]++;
    for (char c : t) countT[c]++;
    for (char c = 'a'; c <= 'z'; c++) {
        res += abs(countS[c] - countT[c]);
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ where $n$ and $m$ are the lengths of `s` and `t`, respectively.
> - **Space Complexity:** $O(1)$ as we are using a constant amount of space to store the count of characters.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over `s` and `t`, and it uses a constant amount of space to store the count of characters.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: frequency count, absolute difference.
- Problem-solving patterns identified: using a frequency count to determine the differences between two strings.
- Optimization techniques learned: using a single pass over the input strings, using a constant amount of space to store the count of characters.
- Similar problems to practice: finding the minimum number of steps to make two strings equal, finding the minimum number of operations to transform one string into another.

**Mistakes to Avoid:**
- Common implementation errors: not using a frequency count, not using a single pass over the input strings.
- Edge cases to watch for: when `s` and `t` are already anagrams, when `s` and `t` have different lengths.
- Performance pitfalls: using a high time complexity algorithm, using a high space complexity data structure.
- Testing considerations: testing with different input sizes, testing with different edge cases.