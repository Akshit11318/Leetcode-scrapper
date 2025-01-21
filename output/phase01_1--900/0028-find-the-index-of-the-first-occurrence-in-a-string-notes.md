## Find the Index of the First Occurrence in a String
**Problem Link:** https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description

**Problem Statement:**
- Input format and constraints: Given two strings `haystack` and `needle`, find the index of the first occurrence of `needle` in `haystack`. If `needle` is an empty string, return 0. If `needle` is not found in `haystack`, return -1.
- Expected output format: The index of the first occurrence of `needle` in `haystack`.
- Key requirements and edge cases to consider: 
  - Handling empty strings for both `haystack` and `needle`.
  - Finding the first occurrence, not just any occurrence.
  - Returning -1 if `needle` is not found.
- Example test cases with explanations:
  - `haystack = "hello", needle = "ll"` should return 2, the index of the first 'l' in "hello".
  - `haystack = "aaaaa", needle = "bba"` should return -1, since "bba" is not found in "aaaaa".
  - `haystack = "", needle = ""` should return 0, as specified for empty strings.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every substring of `haystack` that is the same length as `needle` to see if it matches `needle`.
- Step-by-step breakdown of the solution:
  1. Loop through each character in `haystack`.
  2. For each character, check the substring of `haystack` starting at that character with the same length as `needle`.
  3. Compare this substring with `needle`. If they match, return the current index.
  4. If the loop completes without finding a match, return -1.
- Why this approach comes to mind first: It directly implements the problem's requirement by checking every possible position in `haystack` where `needle` could start.

```cpp
class Solution {
public:
    int strStr(string haystack, string needle) {
        if (needle.empty()) return 0; // Handle empty needle
        for (int i = 0; i <= haystack.length() - needle.length(); i++) {
            // Check if the substring matches needle
            bool match = true;
            for (int j = 0; j < needle.length(); j++) {
                if (haystack[i + j] != needle[j]) {
                    match = false;
                    break;
                }
            }
            if (match) return i; // Return index if match found
        }
        return -1; // Return -1 if no match found
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the length of `haystack` and $m$ is the length of `needle`, because in the worst case, we compare every character of `needle` with every possible starting position in `haystack`.
> - **Space Complexity:** $O(1)$, since we only use a constant amount of space to store indices and the result.
> - **Why these complexities occur:** The nested loop structure leads to the time complexity, while the constant space usage is due to not allocating any additional space that scales with input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Utilize the KMP (Knuth-Morris-Pratt) algorithm, which is designed for substring searching and can reduce the number of comparisons needed by precomputing information about the `needle`.
- Detailed breakdown of the approach:
  1. Preprocess `needle` to create a lookup table that stores the longest proper prefix which is also a suffix.
  2. Use this table to guide the search in `haystack`, allowing us to skip over characters in `haystack` that cannot possibly match the current position in `needle`.
- Proof of optimality: KMP has a linear time complexity of $O(n + m)$, making it optimal for substring searching when the `needle` is known beforehand.

```cpp
class Solution {
public:
    int strStr(string haystack, string needle) {
        if (needle.empty()) return 0;
        int n = haystack.length(), m = needle.length();
        vector<int> lps(m, 0); // Initialize lookup table
        computeLPSArray(needle, m, lps); // Preprocess needle
        int i = 0, j = 0; // Indices for haystack and needle
        while (i < n) {
            if (needle[j] == haystack[i]) {
                i++; j++;
            }
            if (j == m) {
                return i - j; // Match found, return index
            } else if (i < n && needle[j] != haystack[i]) {
                if (j != 0) {
                    j = lps[j - 1]; // Use lookup table to skip characters
                } else {
                    i++; // If j is 0, just move to next character in haystack
                }
            }
        }
        return -1; // No match found
    }

    void computeLPSArray(string pattern, int M, vector<int>& lps) {
        int length = 0; // Length of the previous longest prefix suffix
        lps[0] = 0; // lps[0] is always 0
        int i = 1;
        while (i < M) {
            if (pattern[i] == pattern[length]) {
                length++;
                lps[i] = length;
                i++;
            } else {
                if (length != 0) {
                    length = lps[length - 1];
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the length of `haystack` and $m$ is the length of `needle`, because we make a single pass through `haystack` and a single pass through `needle` to build the lookup table.
> - **Space Complexity:** $O(m)$, for the lookup table used in the KMP algorithm.
> - **Optimality proof:** This is the best time complexity achievable for this problem because we must at least read the input strings once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Substring searching, use of lookup tables for optimization.
- Problem-solving patterns identified: Preprocessing the input to reduce the complexity of the main algorithm.
- Optimization techniques learned: Using the KMP algorithm for efficient substring searching.
- Similar problems to practice: Other string matching algorithms like Rabin-Karp or Boyer-Moore.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect handling of edge cases, such as empty strings or strings of length 1.
- Edge cases to watch for: Handling `needle` being longer than `haystack`, or when `needle` is an empty string.
- Performance pitfalls: Not using an optimized algorithm like KMP for large inputs.
- Testing considerations: Thoroughly testing with various inputs, including edge cases and large strings.