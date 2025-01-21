## Number of Times Binary String is Prefix Aligned
**Problem Link:** https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/description

**Problem Statement:**
- Input: A binary string `s`.
- Constraints: `1 <= s.length <= 10^5`.
- Expected output: The number of times a binary string is prefix-aligned.
- Key requirements: Count the number of indices where the binary string is prefix-aligned.
- Edge cases: Handle strings of varying lengths and prefix patterns.
- Example test cases:
  - Input: `s = "00110"`
  - Output: `4`
  - Explanation: The string is prefix-aligned at indices 0, 1, 3, and 4.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check each prefix of the string to see if it's aligned with the full string.
- Step-by-step breakdown:
  1. Iterate through each prefix of the string.
  2. Check if the prefix is aligned with the full string by comparing characters.
  3. Count the number of indices where the string is prefix-aligned.

```cpp
int numberOfTimesBinaryStringIsPrefixAligned(string s) {
    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        bool aligned = true;
        for (int j = 0; j <= i; j++) {
            if (s[j] != s[j % (i + 1)]) {
                aligned = false;
                break;
            }
        }
        if (aligned) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the string. This is because we're iterating through each prefix of the string and comparing characters.
> - **Space Complexity:** $O(1)$, as we're only using a constant amount of space to store the count and indices.
> - **Why these complexities occur:** The nested loops cause the quadratic time complexity, while the constant space usage is due to only using a few variables to store the count and indices.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of checking each prefix, we can use the fact that a binary string is prefix-aligned if and only if its length is a power of 2.
- Detailed breakdown:
  1. Initialize a count variable to 0.
  2. Iterate through each index in the string.
  3. Check if the index + 1 is a power of 2.
  4. If it is, increment the count.
- Proof of optimality: This approach is optimal because it only requires a single pass through the string, resulting in a linear time complexity.

```cpp
int numberOfTimesBinaryStringIsPrefixAligned(string s) {
    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        if ((i + 1) && !(i + 1 & (i + 1 - 1))) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string. This is because we're only iterating through the string once.
> - **Space Complexity:** $O(1)$, as we're only using a constant amount of space to store the count.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the string, resulting in a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Prefix alignment, power of 2 checking.
- Problem-solving patterns identified: Using properties of binary strings to simplify the problem.
- Optimization techniques learned: Reducing the time complexity from quadratic to linear by using a more efficient approach.
- Similar problems to practice: Other problems involving binary strings and prefix alignment.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty string.
- Edge cases to watch for: Strings of varying lengths, prefix patterns.
- Performance pitfalls: Using a brute force approach with a high time complexity.
- Testing considerations: Testing the function with different input strings and edge cases.