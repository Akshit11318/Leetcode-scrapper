## Find Longest Special Substring That Occurs Thrice I

**Problem Link:** https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/description

**Problem Statement:**
- Input format: a string `s`
- Constraints: `1 <= s.length <= 100`
- Expected output format: the longest special substring that occurs at least three times in `s`
- Key requirements and edge cases to consider:
  - The substring should be as long as possible.
  - If there are multiple substrings of the same length that occur at least three times, any of them can be returned.
- Example test cases with explanations:
  - `s = "abcabc"` returns `"abc"`.
  - `s = "aaaa"` returns `"a"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: check all possible substrings of `s` to see if they occur at least three times.
- Step-by-step breakdown of the solution:
  1. Generate all possible substrings of `s`.
  2. For each substring, count its occurrences in `s`.
  3. Keep track of the longest substring that occurs at least three times.
- Why this approach comes to mind first: it is straightforward and ensures that we do not miss any possible substrings.

```cpp
class Solution {
public:
    string longestSubstrRepeating(const string& s) {
        int n = s.size();
        string longestSubstr = "";
        
        for (int len = 1; len <= n; ++len) {
            for (int i = 0; i <= n - len; ++i) {
                string substr = s.substr(i, len);
                int count = 0;
                for (int j = 0; j <= n - len; ++j) {
                    if (s.substr(j, len) == substr) {
                        ++count;
                    }
                }
                if (count >= 3 && substr.size() > longestSubstr.size()) {
                    longestSubstr = substr;
                }
            }
        }
        return longestSubstr;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3 \cdot m)$, where $n$ is the length of the string `s` and $m$ is the average length of substrings. The reason is that we generate $O(n^2)$ substrings, and for each substring, we count its occurrences in $s$ in $O(n \cdot m)$ time.
> - **Space Complexity:** $O(n)$, as we need to store the substrings.
> - **Why these complexities occur:** The brute force approach involves generating all possible substrings and counting their occurrences, which leads to high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: instead of generating all substrings and counting their occurrences, we can use a hashmap to store the substrings and their counts.
- Detailed breakdown of the approach:
  1. Initialize an empty hashmap to store substrings and their counts.
  2. Iterate over all possible substrings of `s`.
  3. For each substring, increment its count in the hashmap.
  4. Keep track of the longest substring that occurs at least three times.
- Why further optimization is impossible: we need to check all substrings to ensure that we do not miss any possible solutions.

```cpp
class Solution {
public:
    string longestSubstrRepeating(const string& s) {
        int n = s.size();
        string longestSubstr = "";
        unordered_map<string, int> countMap;
        
        for (int len = 1; len <= n; ++len) {
            for (int i = 0; i <= n - len; ++i) {
                string substr = s.substr(i, len);
                ++countMap[substr];
                if (countMap[substr] >= 3 && substr.size() > longestSubstr.size()) {
                    longestSubstr = substr;
                }
            }
        }
        return longestSubstr;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$, where $n$ is the length of the string `s` and $m$ is the average length of substrings. The reason is that we generate $O(n^2)$ substrings, and for each substring, we update its count in the hashmap in $O(m)$ time.
> - **Space Complexity:** $O(n^2)$, as we need to store all substrings in the hashmap.
> - **Optimality proof:** This approach is optimal because we need to check all substrings to ensure that we do not miss any possible solutions.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: hashmap, substring generation, and counting.
- Problem-solving patterns identified: using a hashmap to store counts of substrings.
- Optimization techniques learned: reducing time complexity by using a hashmap.

**Mistakes to Avoid:**
- Common implementation errors: not initializing the hashmap correctly, not updating the count of substrings correctly.
- Edge cases to watch for: empty string, string with only one character.
- Performance pitfalls: using a brute force approach with high time complexity.
- Testing considerations: testing with different input strings, including edge cases.