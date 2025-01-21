## Find Longest Awesome Substring
**Problem Link:** https://leetcode.com/problems/find-longest-awesome-substring/description

**Problem Statement:**
- Input format: A string `s` containing only lowercase English letters.
- Constraints: The length of `s` is between $1$ and $10^5$.
- Expected output format: The length of the longest awesome substring.
- Key requirements: A substring is considered awesome if the number of occurrences of each character is even.
- Example test cases:
  - Input: `s = "3242415"`
    Output: `5`
    Explanation: `"24241"` or `"24142"` are the longest awesome substrings.
  - Input: `s = "02"`
    Output: `1`
    Explanation: `"0"` is the longest awesome substring.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible substring to see if it's awesome.
- Step-by-step breakdown:
  1. Generate all possible substrings of `s`.
  2. For each substring, count the occurrences of each character.
  3. Check if all character counts are even. If so, update the maximum length found.
- Why this approach comes to mind first: It's straightforward and ensures we don't miss any awesome substrings.

```cpp
int longestAwesome(string s) {
    int n = s.size();
    int maxLength = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            string substr = s.substr(i, j - i + 1);
            unordered_map<char, int> charCount;
            for (char c : substr) {
                charCount[c]++;
            }
            bool isAwesome = true;
            for (auto& pair : charCount) {
                if (pair.second % 2 != 0) {
                    isAwesome = false;
                    break;
                }
            }
            if (isAwesome) {
                maxLength = max(maxLength, (int)substr.size());
            }
        }
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of `s`. This is because for each substring ($O(n^2)$), we count character occurrences ($O(n)$).
> - **Space Complexity:** $O(n)$ for storing the substring and character counts.
> - **Why these complexities occur:** The nested loops and additional counting step lead to high time complexity, making this approach inefficient for large inputs.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of checking every substring, we can use a bitmask to represent the parity of character counts.
- Detailed breakdown:
  1. Initialize a bitmask `mask` to 0, representing all characters having even counts.
  2. Iterate through `s`, updating `mask` based on the parity of character counts.
  3. Use a hashmap to store seen `mask` values and their indices.
  4. When encountering a `mask` that has been seen before, update the maximum length if the current substring is longer.
- Proof of optimality: This approach has a linear time complexity, as we only iterate through `s` once and perform constant-time operations.

```cpp
int longestAwesome(string s) {
    int n = s.size();
    int maxLength = 0;
    unordered_map<int, int> maskIndex;
    maskIndex[0] = -1; // Base case for empty substring
    int mask = 0;
    for (int i = 0; i < n; i++) {
        mask ^= (1 << (s[i] - '0')); // Update bitmask
        if (maskIndex.find(mask) != maskIndex.end()) {
            maxLength = max(maxLength, i - maskIndex[mask]);
        }
        for (int j = 0; j <= 9; j++) {
            int newMask = mask ^ (1 << j);
            if (maskIndex.find(newMask) != maskIndex.end()) {
                maxLength = max(maxLength, i - maskIndex[newMask]);
            }
        }
        if (maskIndex.find(mask) == maskIndex.end()) {
            maskIndex[mask] = i;
        }
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot 10)$, where $n$ is the length of `s`. This simplifies to $O(n)$ since the factor 10 is constant.
> - **Space Complexity:** $O(n)$ for storing the bitmask and its indices.
> - **Optimality proof:** This approach efficiently explores all possible substrings by leveraging the properties of bitmasks and hashmaps, achieving a significant reduction in time complexity compared to the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bit manipulation, hashmap usage, and substring exploration.
- Problem-solving patterns identified: Using bitmasks to represent parity and hashmaps for efficient lookup.
- Optimization techniques learned: Reducing time complexity by avoiding redundant operations and leveraging data structures.
- Similar problems to practice: Other string manipulation and bitmask-related problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect bitmask updates, missing base cases for hashmaps.
- Edge cases to watch for: Handling empty strings, single-character strings, and strings with all characters having even counts.
- Performance pitfalls: Using inefficient data structures or algorithms, such as the brute force approach.
- Testing considerations: Thoroughly testing the solution with various input cases, including edge cases and large inputs.