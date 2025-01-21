## First Letter to Appear Twice

**Problem Link:** https://leetcode.com/problems/first-letter-to-appear-twice/description

**Problem Statement:**
- Input format: A string `s` containing only lowercase English letters.
- Constraints: `1 <= s.length <= 10^5`.
- Expected output format: The first letter that appears at least twice in the string, or an empty string if no such letter exists.
- Key requirements and edge cases to consider:
  - Handling strings with no repeating letters.
  - Finding the first letter that repeats, not just any repeating letter.
- Example test cases with explanations:
  - Input: `"abaccdeff"`; Output: `"a"`.
  - Input: `"abc"`; Output: `""`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through the string and for each character, check the rest of the string to see if it appears again.
- Step-by-step breakdown of the solution:
  1. Initialize an empty string to store the first repeating letter.
  2. Iterate through each character in the input string.
  3. For each character, iterate through the rest of the string to check if it appears again.
  4. If a repeating character is found and no repeating character has been found yet, store this character.
  5. After iterating through the entire string, return the stored repeating character or an empty string if none was found.
- Why this approach comes to mind first: It's a straightforward, naive approach that checks every possibility without considering efficiency.

```cpp
string repeatedCharacter(string s) {
    string result = "";
    for (int i = 0; i < s.length(); i++) {
        for (int j = i + 1; j < s.length(); j++) {
            if (s[i] == s[j] && result.empty()) {
                result = s[i];
                break;
            }
        }
        if (!result.empty()) break;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the length of the string, because in the worst case, we're iterating through the string for each character.
> - **Space Complexity:** $O(1)$, because we're using a constant amount of space to store the result and loop variables.
> - **Why these complexities occur:** The nested loops cause the quadratic time complexity, and the minimal use of extra space results in constant space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a `bool` array of size 26 (since there are 26 lowercase English letters) to keep track of the letters we've seen. This way, we only need to iterate through the string once.
- Detailed breakdown of the approach:
  1. Initialize a `bool` array of size 26, all set to `false`.
  2. Iterate through each character in the input string.
  3. For each character, check the corresponding index in the `bool` array (where 'a' corresponds to index 0, 'b' to index 1, etc.).
  4. If the value at that index is already `true`, return the current character as it's the first to appear twice.
  5. Otherwise, set the value at that index to `true`.
  6. If we finish iterating through the string without finding a repeating character, return an empty string.
- Proof of optimality: This approach is optimal because it only requires a single pass through the string, resulting in a linear time complexity.

```cpp
string repeatedCharacter(string s) {
    bool seen[26] = {false};
    for (char c : s) {
        if (seen[c - 'a']) {
            return string(1, c);
        }
        seen[c - 'a'] = true;
    }
    return "";
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the string, because we're making a single pass through the string.
> - **Space Complexity:** $O(1)$, because we're using a fixed-size array regardless of the input size.
> - **Optimality proof:** This is the best possible time complexity for this problem because we must at least read the input once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a `bool` array for efficient tracking of seen characters, reducing time complexity from $O(n^2)$ to $O(n)$.
- Problem-solving patterns identified: Looking for ways to avoid nested loops and using extra space efficiently to improve performance.
- Optimization techniques learned: Reducing the number of iterations and using data structures that allow for constant time access (like arrays).
- Similar problems to practice: Other string manipulation problems, especially those involving finding specific patterns or characters.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize the `bool` array, or incorrectly indexing it.
- Edge cases to watch for: Handling strings with no repeating letters, and ensuring the solution works for strings of length 1.
- Performance pitfalls: Using nested loops when a single pass is sufficient, and not considering the space complexity of the solution.
- Testing considerations: Thoroughly testing the solution with various inputs, including edge cases like empty strings or strings with a single character repeated.