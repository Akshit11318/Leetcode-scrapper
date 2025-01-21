## Maximum Length Substring with Two Occurrences

**Problem Link:** https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/description

**Problem Statement:**
- Input format: a string `s`
- Constraints: `1 <= s.length <= 10^5`
- Expected output format: the length of the maximum length substring with exactly two occurrences
- Key requirements: find the maximum length of a substring that appears exactly twice in the string
- Example test cases:
  - Input: `s = "aababa"`; Output: `3`
  - Input: `s = "aaaaaa"`; Output: `0`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: generate all possible substrings and count their occurrences
- Step-by-step breakdown:
  1. Generate all possible substrings of the input string
  2. For each substring, count its occurrences in the string
  3. If a substring appears exactly twice, update the maximum length
- Why this approach comes to mind first: it's a straightforward, exhaustive search

```cpp
int maxRepeating(const string& s) {
    int n = s.length();
    int maxLength = 0;
    for (int len = 1; len <= n; len++) {
        for (int i = 0; i <= n - len; i++) {
            string substr = s.substr(i, len);
            int count = 0;
            for (int j = 0; j <= n - len; j++) {
                if (s.substr(j, len) == substr) {
                    count++;
                }
            }
            if (count == 2) {
                maxLength = max(maxLength, len);
            }
        }
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input string. This is because we generate all possible substrings ($O(n^2)$) and for each substring, we count its occurrences in the string ($O(n)$).
> - **Space Complexity:** $O(n)$, as we need to store each substring.
> - **Why these complexities occur:** The brute force approach involves exhaustive search and counting, leading to high time complexity. The space complexity is due to storing substrings.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: use a hashmap to store the substrings and their counts, and use a sliding window approach to generate substrings
- Detailed breakdown:
  1. Initialize a hashmap to store substrings and their counts
  2. Iterate over the string with a sliding window of increasing size
  3. For each window size, iterate over the string and generate substrings
  4. For each substring, update its count in the hashmap
  5. If a substring appears exactly twice, update the maximum length
- Why this is optimal: we avoid generating all possible substrings and use a hashmap to efficiently count occurrences

```cpp
int maxRepeating(const string& s) {
    int n = s.length();
    int maxLength = 0;
    for (int len = 1; len <= n / 2; len++) {
        unordered_map<string, int> countMap;
        for (int i = 0; i <= n - len; i++) {
            string substr = s.substr(i, len);
            countMap[substr]++;
            if (countMap[substr] == 2) {
                maxLength = max(maxLength, len);
            }
        }
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input string. This is because we iterate over the string with a sliding window of increasing size.
> - **Space Complexity:** $O(n)$, as we need to store substrings in the hashmap.
> - **Optimality proof:** We avoid generating all possible substrings and use a hashmap to efficiently count occurrences, reducing the time complexity from $O(n^3)$ to $O(n^2)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: hashmap, sliding window, substring generation
- Problem-solving patterns: using a hashmap to efficiently count occurrences, avoiding exhaustive search
- Optimization techniques: reducing time complexity by using a hashmap and sliding window approach

**Mistakes to Avoid:**
- Common implementation errors: incorrect substring generation, incorrect counting of occurrences
- Edge cases to watch for: empty string, single-character string
- Performance pitfalls: using a brute force approach, generating all possible substrings
- Testing considerations: test with different input sizes, test with different character sets