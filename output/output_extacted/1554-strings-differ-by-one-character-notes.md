## Strings Differ by One Character
**Problem Link:** https://leetcode.com/problems/strings-differ-by-one-character/description

**Problem Statement:**
- Input format: Two strings `a` and `b`.
- Constraints: `a` and `b` are non-empty strings consisting of lowercase letters.
- Expected output format: `true` if `a` and `b` differ by one character, `false` otherwise.
- Key requirements and edge cases to consider: 
    - Handling strings of different lengths.
    - Comparing strings character by character.
    - Counting the number of different characters.
- Example test cases with explanations:
    - `a = "ab"`, `b = "ba"`: Returns `false` because `a` and `b` differ by more than one character.
    - `a = "a"`, `b = "b"`: Returns `true` because `a` and `b` differ by one character.
    - `a = "pale"`, `b = "bale"`: Returns `true` because `a` and `b` differ by one character.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Compare each character of the two strings and count the number of differences.
- Step-by-step breakdown of the solution:
    1. Initialize a counter for the number of differences.
    2. Iterate over the characters of the two strings.
    3. If the characters at the current position are different, increment the counter.
    4. If the counter exceeds 1, return `false` because the strings differ by more than one character.
    5. If the loop completes and the counter is 1, return `true` because the strings differ by one character.
- Why this approach comes to mind first: It is a straightforward and intuitive solution that directly addresses the problem statement.

```cpp
bool differByOneChar(string a, string b) {
    if (a.length() != b.length()) {
        return false; // strings of different lengths cannot differ by one character
    }

    int diffCount = 0;
    for (int i = 0; i < a.length(); i++) {
        if (a[i] != b[i]) {
            diffCount++;
            if (diffCount > 1) {
                return false;
            }
        }
    }

    return diffCount == 1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the strings, because we are iterating over the characters of the strings once.
> - **Space Complexity:** $O(1)$ because we are using a constant amount of space to store the counter and loop variables.
> - **Why these complexities occur:** The time complexity is linear because we are performing a single pass over the input strings, and the space complexity is constant because we are not using any data structures that grow with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same insight as the brute force approach, but with a slight optimization to return as soon as we find more than one difference.
- Detailed breakdown of the approach:
    1. Check if the strings have the same length. If not, return `false`.
    2. Initialize a counter for the number of differences.
    3. Iterate over the characters of the two strings, comparing each pair of characters.
    4. If a difference is found, increment the counter. If the counter exceeds 1, immediately return `false`.
    5. After iterating over all characters, return `true` if the counter is exactly 1, indicating the strings differ by one character.
- Proof of optimality: This solution is optimal because it only requires a single pass over the input strings and uses a constant amount of extra space.

```cpp
bool differByOneChar(string a, string b) {
    if (a.length() != b.length()) {
        return false;
    }

    int diffCount = 0;
    for (int i = 0; i < a.length(); i++) {
        if (a[i] != b[i]) {
            diffCount++;
            if (diffCount > 1) {
                return false; // early return as soon as we find more than one difference
            }
        }
    }

    return diffCount == 1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the strings, because we are still iterating over the characters of the strings once.
> - **Space Complexity:** $O(1)$ because we are still using a constant amount of space.
> - **Optimality proof:** This solution is optimal because it has the same time and space complexity as the brute force approach but with the added benefit of returning early as soon as it finds more than one difference, potentially reducing the number of iterations in practice.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, comparison, and counting.
- Problem-solving patterns identified: Checking for differences between two sequences.
- Optimization techniques learned: Early return to reduce unnecessary iterations.
- Similar problems to practice: Other string comparison problems, such as checking for anagrams or substrings.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for the length of the strings before comparing them.
- Edge cases to watch for: Strings of different lengths, or strings that are identical.
- Performance pitfalls: Not returning early when more than one difference is found, leading to unnecessary iterations.
- Testing considerations: Make sure to test with strings of different lengths, and with strings that have more than one difference.