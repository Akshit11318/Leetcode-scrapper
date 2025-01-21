## Longest Repeating Substring

**Problem Link:** https://leetcode.com/problems/longest-repeating-substring/description

**Problem Statement:**
- Input: A string `s`.
- Output: The length of the longest repeating substring in `s`.
- Constraints: `2 <= s.length <= 10^5`.
- Key requirements: The repeating substring must be non-overlapping and appear at least twice in `s`.
- Example test cases:
  - Input: `s = "abcd"`
    - Output: `0` because there is no repeating substring.
  - Input: `s = "abbaba"`
    - Output: `3` because the longest repeating substring is `"abba"`, but the problem asks for non-overlapping substrings, so the answer is `"aba"` which is `3`.
  - Input: `s = "aabcaabdaab"`
    - Output: `3` because the longest repeating substring is `"aab"`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible substring of `s` to see if it repeats.
- We start by generating all substrings of `s` and then check each one to see if it appears more than once in `s`.
- This approach comes to mind first because it is straightforward and ensures we consider all possibilities.

```cpp
class Solution {
public:
    int longestRepeatingSubstring(string s) {
        int n = s.length();
        int maxLength = 0;
        
        for (int length = 1; length <= n / 2; length++) {
            for (int i = 0; i <= n - length; i++) {
                string substr = s.substr(i, length);
                size_t found = s.find(substr, i + 1);
                if (found != string::npos) {
                    maxLength = max(maxLength, length);
                }
            }
        }
        
        return maxLength;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of `s`. This is because for each substring of length $l$, we potentially search for it in the remaining string, which takes $O(n)$ time, and we do this for all substrings, leading to $O(n^2)$ substrings, and for each, we do a search.
> - **Space Complexity:** $O(n)$, because we are creating substrings of `s`.
> - **Why these complexities occur:** The time complexity is high due to the nested loops and the string search operation. The space complexity is due to creating substrings.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a suffix array or a similar data structure that allows us to efficiently compare all suffixes of `s`.
- We can then use a dynamic programming approach or a similar method to find the longest common prefix between any two suffixes, which corresponds to the longest repeating substring.
- This approach is optimal because it reduces the problem to comparing suffixes of `s`, which can be done efficiently.

```cpp
class Solution {
public:
    int longestRepeatingSubstring(string s) {
        int n = s.length();
        vector<int> lcp(2 * n - 1);
        vector<int> sa(2 * n - 1);
        
        // Build suffix array
        vector<pair<char, int>> suffixes(n);
        for (int i = 0; i < n; i++) {
            suffixes[i] = {s[i], i};
        }
        sort(suffixes.begin(), suffixes.end());
        
        for (int i = 0; i < n; i++) {
            sa[i] = suffixes[i].second;
        }
        
        // Calculate LCP array
        lcp[0] = 0;
        for (int i = 1; i < n; i++) {
            int j = sa[i - 1];
            int k = sa[i];
            while (j + lcp[i - 1] < n && k + lcp[i - 1] < n && s[j + lcp[i - 1]] == s[k + lcp[i - 1]]) {
                lcp[i] = lcp[i - 1] + 1;
            }
            if (j + lcp[i] >= n || k + lcp[i] >= n || s[j + lcp[i]] != s[k + lcp[i]]) {
                lcp[i] = lcp[i];
            }
        }
        
        int maxLength = 0;
        for (int i = 1; i < n; i++) {
            maxLength = max(maxLength, lcp[i]);
        }
        
        return maxLength;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the length of `s`, due to sorting the suffixes.
> - **Space Complexity:** $O(n)$, for storing the suffix array and LCP array.
> - **Optimality proof:** This is optimal because it reduces the comparison of all substrings to comparing suffixes, which can be done in $O(n \log n)$ time using sorting, and then finding the LCP, which can be done in linear time after sorting.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: suffix arrays, LCP arrays, and dynamic programming.
- Problem-solving patterns identified: reducing the problem to comparing suffixes.
- Optimization techniques learned: using efficient data structures like suffix arrays.
- Similar problems to practice: finding the longest common substring between two strings.

**Mistakes to Avoid:**
- Common implementation errors: incorrect indexing, not handling edge cases.
- Edge cases to watch for: empty strings, strings with a single character.
- Performance pitfalls: using brute force approaches for large inputs.
- Testing considerations: test with strings of varying lengths, including edge cases.