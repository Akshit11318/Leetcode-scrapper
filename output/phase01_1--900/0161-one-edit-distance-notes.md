## One Edit Distance
**Problem Link:** https://leetcode.com/problems/one-edit-distance/description

**Problem Statement:**
- Input format and constraints: Given two strings `s` and `t` of lengths `m` and `n` respectively, with `m` and `n` being at most 100. 
- Expected output format: Return `true` if `s` and `t` are one edit distance apart, and `false` otherwise.
- Key requirements and edge cases to consider: The edit distance between two strings is the minimum number of operations (insertions, deletions, and substitutions) required to change one string into the other. We need to check if this distance is exactly 1.
- Example test cases with explanations:
  - `s = "ab", t = "ac"`: Return `true` because by replacing the character 'b' with 'c', we can make `s` equal to `t`.
  - `s = "ab", t = "abc"`: Return `true` because by inserting the character 'c' at the end of `s`, we can make `s` equal to `t`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible strings that are one edit away from `s` and check if any of them match `t`.
- Step-by-step breakdown of the solution:
  1. For each character in `s`, create a new string by deleting that character.
  2. For each character in `s`, create a new string by replacing that character with every possible character.
  3. For each position in `s`, create a new string by inserting every possible character at that position.
  4. Check if any of these new strings match `t`.
- Why this approach comes to mind first: It directly addresses the problem statement by considering all possible edits.

```cpp
class Solution {
public:
    bool isOneEditDistance(string s, string t) {
        // Generate all possible strings that are one edit away from s
        vector<string> edits;
        for (int i = 0; i < s.size(); ++i) {
            // Deletion
            string deletion = s.substr(0, i) + s.substr(i + 1);
            edits.push_back(deletion);
            // Replacement
            for (char c = 'a'; c <= 'z'; ++c) {
                string replacement = s.substr(0, i) + c + s.substr(i + 1);
                edits.push_back(replacement);
            }
        }
        // Insertion
        for (int i = 0; i <= s.size(); ++i) {
            for (char c = 'a'; c <= 'z'; ++c) {
                string insertion = s.substr(0, i) + c + s.substr(i);
                edits.push_back(insertion);
            }
        }
        // Check if any of these edits match t
        for (const auto& edit : edits) {
            if (edit == t) {
                return true;
            }
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot 26 \cdot n)$, where $m$ is the length of `s`, $n$ is the length of `t`, and $26$ accounts for all possible characters that can replace a character in `s`. This complexity arises from generating all possible edits and comparing them to `t`.
> - **Space Complexity:** $O(m \cdot 26 \cdot n)$, due to storing all generated edits.
> - **Why these complexities occur:** The brute force approach is inefficient because it generates and checks a large number of strings.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible edits, we can directly compare `s` and `t` character by character and determine if they are one edit distance apart.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `i` and `j`, to the start of `s` and `t`, respectively.
  2. Compare characters at `i` and `j`. If they are different, we have found a potential edit.
  3. If the lengths of `s` and `t` differ by more than 1, we cannot be one edit distance apart.
  4. If `s` is longer than `t`, we consider deleting a character from `s`. If `t` is longer than `s`, we consider inserting a character into `s`.
  5. Continue comparing characters, allowing for at most one edit (insertion, deletion, or substitution).
- Proof of optimality: This approach checks the strings in a single pass, ensuring that we only consider the minimum number of edits necessary.

```cpp
class Solution {
public:
    bool isOneEditDistance(string s, string t) {
        int m = s.size(), n = t.size();
        if (abs(m - n) > 1) return false;
        
        int i = 0, j = 0, count = 0;
        while (i < m && j < n) {
            if (s[i] != t[j]) {
                count++;
                if (count > 1) return false;
                if (m > n) i++;
                else if (m < n) j++;
                else {
                    i++;
                    j++;
                }
            } else {
                i++;
                j++;
            }
        }
        // If one string is longer than the other by 1 character
        if (i < m || j < n) count++;
        return count == 1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m + n)$, where $m$ and $n$ are the lengths of `s` and `t`, respectively. This is because we make a single pass through both strings.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the pointers and the count of edits.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to determine if two strings are one edit distance apart, achieving a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: String comparison, edit distance.
- Problem-solving patterns identified: Direct comparison and edit counting.
- Optimization techniques learned: Reducing the number of operations by directly comparing strings and allowing for at most one edit.
- Similar problems to practice: Longest common subsequence, edit distance between two strings.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases where strings have different lengths.
- Edge cases to watch for: When one string is longer than the other by more than one character.
- Performance pitfalls: Generating all possible edits, which leads to exponential time complexity.
- Testing considerations: Ensure to test cases where strings are of equal length and where they differ in length by one character.