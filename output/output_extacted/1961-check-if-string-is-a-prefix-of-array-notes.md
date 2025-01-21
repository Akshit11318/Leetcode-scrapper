## Check if String is a Prefix of Array

**Problem Link:** https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/description

**Problem Statement:**
- Input: a string `s` and an array of strings `words`.
- Constraints: `1 <= words.length <= 100`, `1 <= words[i].length <= 100`, `1 <= s.length <= 10^5`.
- Expected Output: `true` if `s` is a prefix of the concatenation of `words`, `false` otherwise.
- Key Requirements: Check if the input string `s` is a prefix of the concatenated string of `words`.
- Example Test Cases:
  - Input: `s = "a", words = ["a","b","c"]`, Output: `true`.
  - Input: `s = "b", words = ["a","b","c"]`, Output: `false`.
  - Input: `s = "ab", words = ["a","b","c"]`, Output: `true`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to concatenate all strings in the `words` array and then check if the resulting string starts with `s`.
- This approach involves iterating over each string in `words`, concatenating them, and then using a string comparison method to check for the prefix.

```cpp
class Solution {
public:
    bool isPrefixString(string s, vector<string>& words) {
        string concatenated;
        for (const auto& word : words) {
            concatenated += word;
            if (s == concatenated) return true;
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of words and $m$ is the average length of a word, because in the worst case, we concatenate and compare all words.
> - **Space Complexity:** $O(n \cdot m)$ for storing the concatenated string.
> - **Why these complexities occur:** The time complexity is due to the iteration over each word and the string comparison. The space complexity is due to the storage of the concatenated string.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight here is to realize that we don't necessarily need to concatenate all strings to check if `s` is a prefix of the concatenated string.
- We can achieve the same result by iterating through `s` and checking each character against the characters in the concatenated string of `words`, stopping as soon as we find a mismatch or reach the end of `s`.
- This approach avoids unnecessary concatenation and comparison operations.

```cpp
class Solution {
public:
    bool isPrefixString(string s, vector<string>& words) {
        string concatenated;
        for (const auto& word : words) {
            concatenated += word;
            if (s.size() <= concatenated.size()) {
                if (s == concatenated.substr(0, s.size())) return true;
            }
        }
        return false;
    }
};
```

However, a more efficient approach would be to directly compare characters from `s` with the characters from the `words` array without explicit concatenation:

```cpp
class Solution {
public:
    bool isPrefixString(string s, vector<string>& words) {
        int sIndex = 0;
        for (const auto& word : words) {
            for (char c : word) {
                if (sIndex == s.size()) return true;
                if (s[sIndex] != c) return false;
                sIndex++;
            }
        }
        return sIndex == s.size();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of words and $m$ is the average length of a word, because we potentially iterate through each character in each word once.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space to store the index and do not perform any explicit concatenation.
> - **Optimality proof:** This is the best possible time complexity because we must at least read the input once to solve the problem. The space complexity is optimal as we only use a constant amount of space.

---

### Final Notes

**Learning Points:**
- The importance of avoiding unnecessary operations (like concatenation) when solving string problems.
- How to optimize string comparison by directly comparing characters without concatenation.
- Understanding the trade-offs between different approaches in terms of time and space complexity.

**Mistakes to Avoid:**
- Not considering the possibility of early returns or breaks in loops to reduce unnecessary computations.
- Failing to analyze the space complexity implications of string concatenation.
- Not optimizing string comparisons by leveraging the properties of substrings and character-wise comparisons.