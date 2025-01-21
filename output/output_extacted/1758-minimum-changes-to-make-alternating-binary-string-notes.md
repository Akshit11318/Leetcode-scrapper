## Minimum Changes to Make Alternating Binary String

**Problem Link:** https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description

**Problem Statement:**
- Input: A binary string `s`.
- Output: The minimum number of changes required to make the string alternating.
- Key requirements and edge cases:
  - The string `s` only contains the characters '0' and '1'.
  - An alternating binary string is a string where every '0' is followed by a '1' and every '1' is followed by a '0'.
- Example test cases:
  - Input: `s = "0100"`
    - Output: `1`
    - Explanation: We can change the last '0' to a '1' to make the string alternating.
  - Input: `s = "10"`
    - Output: `0`
    - Explanation: The string is already alternating.
  - Input: `s = "1111"`
    - Output: `2`
    - Explanation: We can change the second and fourth '1's to '0's to make the string alternating.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible binary strings of the same length as the input string and check if they are alternating.
- Then, for each generated string, compare it with the input string and count the number of different characters.
- The minimum count of different characters is the minimum number of changes required.

```cpp
class Solution {
public:
    int minChanges(string s) {
        int minChanges = INT_MAX;
        int n = s.size();
        for (int mask = 0; mask < (1 << n); mask++) {
            string alt;
            for (int i = 0; i < n; i++) {
                alt += ((mask >> i) & 1) ? '1' : '0';
            }
            int changes = 0;
            for (int i = 0; i < n; i++) {
                if (alt[i] != s[i]) {
                    changes++;
                }
            }
            minChanges = min(minChanges, changes);
        }
        return minChanges;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input string. This is because we generate all possible binary strings of length $n$ and compare each one with the input string.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we need to store the generated alternating binary string.
> - **Why these complexities occur:** The brute force approach is inefficient because it generates all possible binary strings, which results in an exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is that we only need to consider two possible alternating binary strings: one starting with '0' and one starting with '1'.
- We can then compare the input string with these two alternating binary strings and count the number of different characters.
- The minimum count of different characters is the minimum number of changes required.

```cpp
class Solution {
public:
    int minChanges(string s) {
        int n = s.size();
        int changesStartWith0 = 0;
        int changesStartWith1 = 0;
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0 && s[i] != '0') {
                changesStartWith0++;
            }
            if (i % 2 == 1 && s[i] != '1') {
                changesStartWith0++;
            }
            if (i % 2 == 0 && s[i] != '1') {
                changesStartWith1++;
            }
            if (i % 2 == 1 && s[i] != '0') {
                changesStartWith1++;
            }
        }
        return min(changesStartWith0, changesStartWith1);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we only need to iterate through the input string once.
> - **Space Complexity:** $O(1)$, where $n$ is the length of the input string. This is because we only need to use a constant amount of space to store the counts of changes.
> - **Optimality proof:** This approach is optimal because it only considers the two possible alternating binary strings, which reduces the time complexity from exponential to linear.

---

### Final Notes

**Learning Points:**
- The importance of considering all possible approaches before settling on one.
- The use of bit manipulation to generate all possible binary strings.
- The optimization technique of reducing the number of possibilities to consider.
- The trade-off between time and space complexity.

**Mistakes to Avoid:**
- Generating all possible binary strings without considering the alternating pattern.
- Not using a constant amount of space to store the counts of changes.
- Not considering the two possible alternating binary strings.
- Not using the `min` function to find the minimum count of changes.