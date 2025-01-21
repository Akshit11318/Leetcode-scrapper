## Construct the Longest New String

**Problem Link:** https://leetcode.com/problems/construct-the-longest-new-string/description

**Problem Statement:**
- Input: Two strings `s` and `t`.
- Constraints: `1 <= s.length <= 10^5`, `1 <= t.length <= 10^5`.
- Expected Output: The length of the longest string that can be constructed by removing characters from `s` to form `t`.
- Key Requirements: Determine the longest possible string by removing characters from `s` to form `t`, where the order of characters in `s` must be maintained.
- Edge Cases: Consider cases where `t` is longer than `s`, or when `s` does not contain all characters in `t`.
- Example Test Cases:
  - Input: `s = "abanana"`, `t = "anana"`
    - Output: `3`
  - Input: `s = "abanana"`, `t = "banana"`
    - Output: `5`
  - Input: `s = "abc"`, `t = "abcd"`
    - Output: `0`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible substrings of `s` and check if any of them is equal to `t`.
- Step-by-step breakdown of the solution:
  1. Generate all possible substrings of `s`.
  2. For each substring, check if it is equal to `t`.
  3. Keep track of the maximum length of the substrings that are equal to `t`.

```cpp
int longestNewString(string s, string t) {
    int maxLength = 0;
    for (int i = 0; i < s.length(); i++) {
        for (int j = i + 1; j <= s.length(); j++) {
            string substring = s.substr(i, j - i);
            if (substring == t) {
                maxLength = max(maxLength, (int)substring.length());
            }
        }
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of `s`. This is because we generate all possible substrings of `s` and compare each of them with `t`.
> - **Space Complexity:** $O(n)$, where $n$ is the length of `s`. This is because we need to store each substring of `s`.
> - **Why these complexities occur:** The brute force approach involves generating all possible substrings of `s`, which results in a cubic time complexity. The space complexity is linear because we only need to store each substring of `s`.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a two-pointer technique to find the longest substring of `s` that is equal to `t`.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `i` and `j`, to the beginning of `s` and `t`, respectively.
  2. Initialize a variable `maxLength` to store the maximum length of the substrings that are equal to `t`.
  3. Iterate through `s` using the pointer `i`.
  4. For each character in `s`, check if it is equal to the character at the current position of `t`.
  5. If the characters are equal, increment both pointers and update `maxLength`.
  6. If the characters are not equal, reset the pointer `j` to the beginning of `t`.

```cpp
int longestNewString(string s, string t) {
    int maxLength = 0;
    for (int i = 0; i < s.length(); i++) {
        int j = 0;
        int currentLength = 0;
        for (int k = i; k < s.length(); k++) {
            if (s[k] == t[j]) {
                j++;
                currentLength++;
                if (j == t.length()) {
                    maxLength = max(maxLength, currentLength);
                    break;
                }
            }
        }
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the length of `s` and $m$ is the length of `t`. This is because we iterate through `s` and `t` using two nested loops.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the pointers and the maximum length.
> - **Optimality proof:** This approach is optimal because we only need to iterate through `s` and `t` once to find the longest substring of `s` that is equal to `t`. The time complexity is linear with respect to the lengths of `s` and `t`, which is the best we can achieve.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: two-pointer technique, substring matching.
- Problem-solving patterns identified: using a brute force approach to understand the problem, and then optimizing it using a more efficient algorithm.
- Optimization techniques learned: reducing the time complexity by using a more efficient algorithm.
- Similar problems to practice: substring matching, longest common subsequence.

**Mistakes to Avoid:**
- Common implementation errors: incorrect use of pointers, incorrect handling of edge cases.
- Edge cases to watch for: cases where `t` is longer than `s`, or when `s` does not contain all characters in `t`.
- Performance pitfalls: using a brute force approach that results in a high time complexity.
- Testing considerations: testing the algorithm with different inputs, including edge cases.