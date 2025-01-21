## Check if String is Decomposable into Value-Equal Substrings

**Problem Link:** https://leetcode.com/problems/check-if-string-is-decomposable-into-value-equal-substrings/description

**Problem Statement:**
- Input: A string `s` containing only lowercase letters.
- Expected output: A boolean indicating whether `s` can be decomposed into value-equal substrings.
- Key requirements: 
  - A string is considered value-equal if all characters in the string have the same number of occurrences.
  - The decomposition should be such that all substrings have the same length.
- Edge cases to consider:
  - Empty string
  - Single character string
  - Strings with varying lengths of substrings

Example test cases:
- Input: `s = "ababab"` Output: `true` Explanation: The string can be decomposed into 3 substrings of length 2 ("ab", "ab", "ab") where each character occurs the same number of times.
- Input: `s = "aabb"` Output: `false` Explanation: The string cannot be decomposed into substrings where each character occurs the same number of times.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking all possible decompositions of the string into substrings of the same length.
- For each decomposition, check if all characters occur the same number of times in each substring.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

bool isDecomposable(const std::string& s) {
    int n = s.size();
    for (int len = 1; len <= n / 2; len++) {
        if (n % len == 0) { // Check if string can be divided into substrings of length 'len'
            bool isDecomposable = true;
            for (int i = 0; i < n; i += len) {
                std::unordered_map<char, int> charCount;
                for (int j = i; j < i + len; j++) {
                    charCount[s[j]]++;
                }
                // Check if all characters occur the same number of times
                int expectedCount = -1;
                for (const auto& pair : charCount) {
                    if (expectedCount == -1) {
                        expectedCount = pair.second;
                    } else if (pair.second != expectedCount) {
                        isDecomposable = false;
                        break;
                    }
                }
                if (!isDecomposable) break;
            }
            if (isDecomposable) return true;
        }
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the string. This is because in the worst case, we are iterating over the string for each possible substring length.
> - **Space Complexity:** $O(n)$, due to the use of the `unordered_map` to store character counts for each substring.
> - **Why these complexities occur:** The brute force approach involves checking all possible decompositions and for each, counting character occurrences in substrings, leading to quadratic time complexity.

---

### Optimal Approach

**Explanation:**
- The key insight is to realize that for a string to be decomposable into value-equal substrings, the total count of each character must be divisible by the number of substrings. 
- This allows us to directly check divisibility of character counts by potential substring counts without explicitly decomposing the string.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

bool isDecomposable(const std::string& s) {
    int n = s.size();
    std::unordered_map<char, int> charCount;
    for (char c : s) {
        charCount[c]++;
    }
    for (int len = 1; len <= n / 2; len++) {
        if (n % len == 0) { // Check if string can be divided into substrings of length 'len'
            bool allDivisible = true;
            for (const auto& pair : charCount) {
                if (pair.second % (n / len) != 0) {
                    allDivisible = false;
                    break;
                }
            }
            if (allDivisible) {
                // Now, verify if the string can indeed be decomposed into substrings of length 'len'
                // where each character occurs the same number of times in each substring.
                int substrings = n / len;
                for (int i = 0; i < n; i += len) {
                    std::unordered_map<char, int> substrCharCount;
                    for (int j = i; j < i + len; j++) {
                        substrCharCount[s[j]]++;
                    }
                    int expectedCount = -1;
                    for (const auto& pair : substrCharCount) {
                        if (expectedCount == -1) {
                            expectedCount = pair.second;
                        } else if (pair.second != expectedCount) {
                            allDivisible = false;
                            break;
                        }
                    }
                    if (!allDivisible) break;
                }
                if (allDivisible) return true;
            }
        }
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, because in the worst case, we are still iterating over the string for each possible substring length and then verifying the decomposition condition.
> - **Space Complexity:** $O(n)$, due to the use of `unordered_map` for storing character counts.
> - **Optimality proof:** While this approach still has a quadratic time complexity, it optimizes the brute force by directly checking divisibility of character counts and then verifying the decomposition, making it more efficient in practice.

---

### Final Notes

**Learning Points:**
- The importance of character count analysis in string problems.
- Divisibility checks for optimizing string decomposition problems.
- Verification steps to ensure the correctness of the decomposition.

**Mistakes to Avoid:**
- Not considering all possible substring lengths.
- Not verifying the decomposition condition after checking divisibility.
- Incorrectly calculating character counts or substring lengths.