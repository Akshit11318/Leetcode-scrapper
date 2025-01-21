## Valid Word Abbreviation

**Problem Link:** https://leetcode.com/problems/valid-word-abbreviation/description

**Problem Statement:**
- Input: Two strings `word` and `abbr`, where `word` is a non-empty string and `abbr` is a non-empty string consisting of uppercase and lowercase letters, and digits.
- Constraints: `1 <= word.length <= 20` and `1 <= abbr.length <= 10`.
- Expected Output: `true` if `word` can be abbreviated into `abbr`, `false` otherwise.
- Key Requirements: `abbr` is a valid abbreviation for `word` if `abbr` contains the first letter of `word`, followed by the count of characters that are not included in `abbr`, followed by the last letter of `word`. If `abbr` contains a number `m`, it means `m` characters have been omitted.
- Example Test Cases:
  - Input: `word = "internationalization", abbr = "i12iz4n17"`
    - Output: `true`
    - Explanation: The abbreviation "i12iz4n17" is equivalent to "internationalization" because the first letter 'i' is followed by 12 omitted characters, then 'i', then 4 omitted characters, then 'z', then 4 omitted characters, then 'n', then 17 omitted characters, and finally the last letter 'n'.
  - Input: `word = "hello", abbr = "hl"`
    - Output: `false`
    - Explanation: The abbreviation "hl" is not equivalent to "hello" because the count of omitted characters is missing.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible way to abbreviate the `word` and compare it with the given `abbr`.
- We start by generating all possible abbreviations of `word` and then check if `abbr` matches any of them.

```cpp
#include <string>

class Solution {
public:
    bool validWordAbbreviation(std::string word, std::string abbr) {
        int i = 0, j = 0;
        while (i < word.length() && j < abbr.length()) {
            if (abbr[j] >= '0' && abbr[j] <= '9') {
                int count = 0;
                while (j < abbr.length() && abbr[j] >= '0' && abbr[j] <= '9') {
                    count = count * 10 + (abbr[j] - '0');
                    j++;
                }
                i += count;
            } else if (word[i] == abbr[j]) {
                i++;
                j++;
            } else {
                return false;
            }
        }
        return i == word.length() && j == abbr.length();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the length of `word` and $m$ is the length of `abbr`. This is because we are potentially scanning through both strings once.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space.
> - **Why these complexities occur:** The time complexity is linear because we are making a single pass through both the `word` and `abbr` strings. The space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

The provided brute force approach is actually the optimal solution for this problem, as it directly addresses the requirements of checking if `word` can be abbreviated into `abbr` by making a single pass through both strings.

**Explanation:**
- The optimal approach involves directly comparing characters and handling numbers in `abbr` to skip corresponding characters in `word`.
- It iterates through `word` and `abbr` simultaneously, checking for matches and handling numbers to skip characters.

```cpp
class Solution {
public:
    bool validWordAbbreviation(std::string word, std::string abbr) {
        int i = 0, j = 0;
        while (i < word.length() && j < abbr.length()) {
            if (abbr[j] >= '0' && abbr[j] <= '9') {
                int count = 0;
                while (j < abbr.length() && abbr[j] >= '0' && abbr[j] <= '9') {
                    count = count * 10 + (abbr[j] - '0');
                    j++;
                }
                i += count;
            } else if (word[i] == abbr[j]) {
                i++;
                j++;
            } else {
                return false;
            }
        }
        return i == word.length() && j == abbr.length();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the length of `word` and $m$ is the length of `abbr`.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space.
> - **Optimality proof:** This is the optimal solution because we must at least read the input strings once, and this solution achieves that in a single pass.

---

### Final Notes

**Learning Points:**
- The importance of understanding the problem constraints and requirements.
- How to handle abbreviations with numbers to skip characters in a string.
- The value of making a single pass through the input data for efficiency.

**Mistakes to Avoid:**
- Not properly handling the case where `abbr` contains numbers.
- Failing to check if the entire `word` and `abbr` have been processed.
- Not considering the constraints on the lengths of `word` and `abbr`.