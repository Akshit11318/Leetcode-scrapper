## Longest Common Prefix

**Problem Link:** https://leetcode.com/problems/longest-common-prefix/description

**Problem Statement:**
- Input format: An array of strings `strs`.
- Constraints: `1 <= strs.length <= 200`, `0 <= strs[i].length <= 200`, `strs[i]` consists of only lowercase English letters.
- Expected output format: A string representing the longest common prefix among all strings in `strs`.
- Key requirements and edge cases to consider: 
  - The input array may contain empty strings.
  - The input array may contain strings of varying lengths.
  - The input array may be empty.
- Example test cases with explanations:
  - Input: `strs = ["flower","flow","flight"]`, Output: `"fl"`.
  - Input: `strs = ["dog","racecar","car"]`, Output: `""`.
  - Input: `strs = ["a"]`, Output: `"a"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Compare each character of the first string with the corresponding character of the remaining strings.
- Step-by-step breakdown of the solution:
  1. Initialize an empty string `prefix` to store the common prefix.
  2. Iterate over the characters of the first string in `strs`.
  3. For each character, compare it with the corresponding character of the remaining strings in `strs`.
  4. If a mismatch is found, break the loop and return the `prefix` up to the previous character.
  5. If the loop completes without finding a mismatch, return the entire first string as the common prefix.
- Why this approach comes to mind first: It is a straightforward approach that checks each character of the strings one by one.

```cpp
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) return "";
        string prefix = "";
        for (int i = 0; i < strs[0].length(); i++) {
            char c = strs[0][i];
            for (int j = 1; j < strs.size(); j++) {
                if (i >= strs[j].length() || strs[j][i] != c) {
                    return prefix;
                }
            }
            prefix += c;
        }
        return prefix;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where $n$ is the number of strings and $m$ is the length of the shortest string. This is because we are iterating over each character of the strings.
> - **Space Complexity:** $O(m)$, where $m$ is the length of the longest common prefix. This is because we are storing the common prefix in a string.
> - **Why these complexities occur:** The time complexity occurs because we are using nested loops to compare each character of the strings. The space complexity occurs because we are storing the common prefix in a string.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of comparing each character of the first string with the corresponding character of the remaining strings, we can compare the characters of the first two strings and then compare the result with the next string, and so on.
- Detailed breakdown of the approach:
  1. Initialize an empty string `prefix` to store the common prefix.
  2. Iterate over the strings in `strs`.
  3. For each string, compare its characters with the corresponding characters of the `prefix`.
  4. If a mismatch is found, update the `prefix` to the common prefix of the current string and the previous `prefix`.
  5. If the loop completes without finding a mismatch, return the `prefix`.
- Proof of optimality: This approach is optimal because it only requires a single pass through the strings, and it minimizes the number of comparisons required to find the common prefix.

```cpp
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) return "";
        string prefix = strs[0];
        for (int i = 1; i < strs.size(); i++) {
            while (strs[i].find(prefix) != 0) {
                prefix = prefix.substr(0, prefix.length() - 1);
                if (prefix.empty()) return "";
            }
        }
        return prefix;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where $n$ is the number of strings and $m$ is the length of the longest string. This is because we are iterating over each string and each character of the strings.
> - **Space Complexity:** $O(m)$, where $m$ is the length of the longest common prefix. This is because we are storing the common prefix in a string.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the strings, and it minimizes the number of comparisons required to find the common prefix.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: String comparison, prefix matching, and iteration over a list of strings.
- Problem-solving patterns identified: Using a brute force approach to understand the problem, and then optimizing the solution by reducing the number of comparisons required.
- Optimization techniques learned: Minimizing the number of comparisons required to find the common prefix, and using a single pass through the strings to optimize the solution.
- Similar problems to practice: Longest common suffix, shortest common supersequence, and longest repeated substring.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for empty strings, not handling edge cases, and not optimizing the solution.
- Edge cases to watch for: Empty strings, strings of varying lengths, and strings with no common prefix.
- Performance pitfalls: Using nested loops to compare each character of the strings, and not minimizing the number of comparisons required to find the common prefix.
- Testing considerations: Testing the solution with different input cases, including empty strings, strings of varying lengths, and strings with no common prefix.