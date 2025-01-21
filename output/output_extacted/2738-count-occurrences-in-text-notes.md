## Count Occurrences in Text

**Problem Link:** https://leetcode.com/problems/count-occurrences-in-text/description

**Problem Statement:**
- Input format and constraints: Given a string `text` and a string `pattern`, find the number of occurrences of `pattern` in `text`.
- Expected output format: Return the number of occurrences of `pattern` in `text`.
- Key requirements and edge cases to consider: The `pattern` can be a substring of `text`, and we need to count all non-overlapping occurrences.
- Example test cases with explanations:
  - `text = "abab", pattern = "ab"`: The output should be `2`, because `pattern` occurs twice in `text`.
  - `text = "ababab", pattern = "aba"`: The output should be `2`, because `pattern` occurs twice in `text`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can iterate through the `text` and check if the `pattern` matches at each position.
- Step-by-step breakdown of the solution:
  1. Initialize a counter to store the number of occurrences.
  2. Iterate through the `text` using a sliding window of size equal to the length of `pattern`.
  3. At each position, check if the substring of `text` matches the `pattern`.
  4. If it matches, increment the counter.
- Why this approach comes to mind first: It is a straightforward and intuitive solution that checks all possible substrings of `text`.

```cpp
int countOccurrences(string text, string pattern) {
    int count = 0;
    for (int i = 0; i <= text.size() - pattern.size(); i++) {
        if (text.substr(i, pattern.size()) == pattern) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the length of `text` and $m$ is the length of `pattern`, because we are iterating through `text` and checking each substring of length $m$.
> - **Space Complexity:** $O(1)$, because we only need a constant amount of space to store the counter.
> - **Why these complexities occur:** The time complexity is high because we are checking all possible substrings of `text`, and the space complexity is low because we only need a small amount of space to store the counter.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use the KMP (Knuth-Morris-Pratt) algorithm to efficiently find all occurrences of `pattern` in `text`.
- Detailed breakdown of the approach:
  1. Preprocess the `pattern` to build a lookup table.
  2. Iterate through the `text` using the lookup table to efficiently find matches.
- Proof of optimality: The KMP algorithm has a time complexity of $O(n + m)$, which is optimal because we need to at least read the input strings once.
- Why further optimization is impossible: The KMP algorithm is already optimal, and any further optimization would require a different approach that is not based on string matching.

```cpp
vector<int> computeLPSArray(const string& pattern) {
    int m = pattern.size();
    vector<int> lps(m);
    int j = 0;
    for (int i = 1; i < m; i++) {
        while (j > 0 && pattern[i] != pattern[j]) {
            j = lps[j - 1];
        }
        if (pattern[i] == pattern[j]) {
            j++;
        }
        lps[i] = j;
    }
    return lps;
}

int countOccurrences(string text, string pattern) {
    vector<int> lps = computeLPSArray(pattern);
    int count = 0;
    int j = 0;
    for (int i = 0; i < text.size(); i++) {
        while (j > 0 && text[i] != pattern[j]) {
            j = lps[j - 1];
        }
        if (text[i] == pattern[j]) {
            j++;
        }
        if (j == pattern.size()) {
            count++;
            j = lps[j - 1];
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the length of `text` and $m$ is the length of `pattern`, because we are iterating through `text` and `pattern` once.
> - **Space Complexity:** $O(m)$, because we need to store the lookup table for the `pattern`.
> - **Optimality proof:** The KMP algorithm is optimal because it has a linear time complexity, and any further optimization would require a different approach that is not based on string matching.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: String matching, KMP algorithm, and lookup tables.
- Problem-solving patterns identified: Using a lookup table to efficiently find matches in a string.
- Optimization techniques learned: Using the KMP algorithm to reduce the time complexity of string matching.
- Similar problems to practice: Other string matching problems, such as finding the longest common substring or the shortest common supersequence.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty `text` or `pattern`.
- Edge cases to watch for: When the `pattern` is longer than the `text`, or when the `pattern` is empty.
- Performance pitfalls: Using a naive approach that has a high time complexity, such as checking all possible substrings of `text`.
- Testing considerations: Testing the function with different inputs, such as an empty `text` or `pattern`, or a `pattern` that is longer than the `text`.