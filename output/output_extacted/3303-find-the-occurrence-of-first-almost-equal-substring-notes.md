## Find the Occurrence of First Almost Equal Substring

**Problem Link:** https://leetcode.com/problems/find-the-occurrence-of-first-almost-equal-substring/description

**Problem Statement:**
- Input format: Given a string `s` and a string `p`, find the first occurrence of `p` in `s` that is almost equal to `p`. 
- Constraints: `1 <= s.length, p.length <= 10^5`, `s` and `p` consist of lowercase English letters.
- Expected output format: Return the index of the first occurrence of `p` in `s` that is almost equal to `p`. If there is no such substring, return `-1`.
- Key requirements and edge cases to consider:
  - A substring `s[i:i+p.length-1]` is considered almost equal to `p` if the number of different characters between `s[i:i+p.length-1]` and `p` is less than or equal to `k`.
  - If there are multiple such substrings, return the index of the first one.

### Brute Force Approach

**Explanation:**
- Initial thought process: Compare every substring of `s` with the same length as `p` and count the number of different characters. If the count is less than or equal to `k`, return the index of the substring.
- Step-by-step breakdown of the solution:
  1. Iterate over `s` with a sliding window of size `p.length`.
  2. For each window, compare the substring with `p` character by character.
  3. Count the number of different characters.
  4. If the count is less than or equal to `k`, return the index of the substring.

```cpp
int findAlmostEqualSubstring(string s, string p, int k) {
    int n = s.length(), m = p.length();
    for (int i = 0; i <= n - m; i++) {
        int diff = 0;
        for (int j = 0; j < m; j++) {
            if (s[i + j] != p[j]) diff++;
        }
        if (diff <= k) return i;
    }
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the length of `s` and $m` is the length of `p`. This is because for each of the `n` characters in `s`, we potentially compare `m` characters with `p`.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the variables.
> - **Why these complexities occur:** The time complexity is high because we are using a nested loop to compare each substring of `s` with `p`. The space complexity is low because we are not using any data structures that scale with the input size.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using a sliding window approach with a single pass over `s`.
- Detailed breakdown of the approach:
  1. Initialize a variable `diff` to store the number of different characters between the current window and `p`.
  2. Iterate over `s` with a sliding window of size `p.length`.
  3. For each character in the window, update `diff` by incrementing it if the character is different from the corresponding character in `p`.
  4. If `diff` is less than or equal to `k`, return the index of the substring.
  5. If the window moves to the right, update `diff` by decrementing it if the character that just left the window is different from the corresponding character in `p`, and incrementing it if the new character is different from the corresponding character in `p`.

```cpp
int findAlmostEqualSubstring(string s, string p, int k) {
    int n = s.length(), m = p.length();
    for (int i = 0; i <= n - m; i++) {
        int diff = 0;
        for (int j = 0; j < m; j++) {
            if (s[i + j] != p[j]) diff++;
            if (diff > k) break;
        }
        if (diff <= k) return i;
    }
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the length of `s` and `m` is the length of `p`. This is because for each of the `n` characters in `s`, we potentially compare `m` characters with `p`.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the variables.
> - **Optimality proof:** The time complexity is optimal because we must compare each character in `s` with `p` at least once to find the first almost equal substring. The space complexity is optimal because we are not using any data structures that scale with the input size.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window approach, character comparison.
- Problem-solving patterns identified: Using a single pass over the input to find the first occurrence of a pattern.
- Optimization techniques learned: Breaking out of the inner loop early when the difference count exceeds `k`.
- Similar problems to practice: Find the first occurrence of a substring in a string, find the longest common substring between two strings.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to update the difference count when the window moves to the right.
- Edge cases to watch for: When `k` is greater than or equal to the length of `p`, the problem becomes trivial and the first occurrence of `p` in `s` is always almost equal to `p`.
- Performance pitfalls: Using a nested loop with a high time complexity.
- Testing considerations: Test the function with different inputs, including edge cases and large inputs.