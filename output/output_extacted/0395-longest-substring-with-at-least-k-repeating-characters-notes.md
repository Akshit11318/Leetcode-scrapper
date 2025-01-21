## Longest Substring with At Least K Repeating Characters

**Problem Link:** https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description

**Problem Statement:**
- Input: A string `s` and an integer `k`.
- Output: The length of the longest substring of `s` where at least `k` characters repeat.
- Key Requirements:
  - The input string `s` consists of lowercase letters.
  - `k` is a positive integer.
- Edge Cases:
  - When `k` is greater than the length of the string, the answer is `0`.
  - When `k` is `1`, the answer is the length of the string.

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible substring of `s`.
- For each substring, count the occurrence of each character and check if at least one character appears `k` or more times.
- This approach is straightforward but inefficient due to the high number of substrings and the need to count character occurrences in each.

```cpp
class Solution {
public:
    int longestSubstring(string s, int k) {
        int n = s.size();
        int maxLen = 0;
        
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j <= n; j++) {
                string substr = s.substr(i, j - i);
                if (isValid(substr, k)) {
                    maxLen = max(maxLen, (int)substr.size());
                }
            }
        }
        return maxLen;
    }
    
    bool isValid(string s, int k) {
        if (s.size() < k) return false;
        unordered_map<char, int> count;
        for (char c : s) {
            count[c]++;
        }
        for (auto& pair : count) {
            if (pair.second >= k) return true;
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the string. The outer two loops generate all substrings ($O(n^2)$), and the `isValid` function counts character occurrences in each substring ($O(n)$).
> - **Space Complexity:** $O(n)$, primarily for storing the current substring and the character count map.
> - **Why these complexities occur:** The brute force approach involves checking every substring and counting character occurrences in each, leading to high time and space complexities.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a divide-and-conquer strategy. Split the string into substrings based on characters that appear less than `k` times.
- If a character appears less than `k` times in the entire string, it cannot be part of the longest substring with at least `k` repeating characters.
- Recursively apply this strategy to the split substrings.

```cpp
class Solution {
public:
    int longestSubstring(string s, int k) {
        int n = s.size();
        if (n < k) return 0;
        
        for (char c = 'a'; c <= 'z'; c++) {
            int count = 0;
            for (int i = 0; i < n; i++) {
                if (s[i] == c) count++;
            }
            if (count >= k) continue;
            int maxLen = 0;
            string substr;
            for (int i = 0; i < n; i++) {
                if (s[i] == c) {
                    if (!substr.empty()) {
                        maxLen = max(maxLen, longestSubstring(substr, k));
                    }
                    substr.clear();
                } else {
                    substr += s[i];
                }
            }
            if (!substr.empty()) {
                maxLen = max(maxLen, longestSubstring(substr, k));
            }
            return maxLen;
        }
        return n;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot 26)$, where $n$ is the length of the string. The factor of `26` comes from potentially iterating over all lowercase letters.
> - **Space Complexity:** $O(n)$, for the recursive call stack and storing substrings.
> - **Optimality proof:** This approach is optimal because it efficiently splits the problem into smaller subproblems based on characters that cannot contribute to the solution, avoiding unnecessary computation.

---

### Final Notes

**Learning Points:**
- The importance of identifying key characters that can split the problem into smaller subproblems.
- The application of divide-and-conquer strategies in string problems.
- Optimization techniques for reducing unnecessary computation by eliminating characters that cannot contribute to the solution.

**Mistakes to Avoid:**
- Not considering the base case where the string length is less than `k`.
- Failing to eliminate characters that appear less than `k` times, which cannot be part of the solution.
- Not optimizing the recursive approach, which can lead to high time complexity.