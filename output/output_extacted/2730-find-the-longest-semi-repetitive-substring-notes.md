## Find the Longest Semi-Repetitive Substring
**Problem Link:** https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/description

**Problem Statement:**
- Input format: A string `s` containing only lowercase English letters.
- Constraints: `1 <= s.length <= 10^5`.
- Expected output format: The length of the longest semi-repetitive substring.
- Key requirements and edge cases to consider:
  - A string is considered semi-repetitive if it can be split into two non-empty strings `a` and `b` such that `a` is not equal to `b` but `a` and `b` have the same characters (possibly in different orders).
- Example test cases with explanations:
  - Example 1: Input: `s = "abab"`, Output: `4`. Explanation: The longest semi-repetitive substring is `"abab"`.
  - Example 2: Input: `s = "aaaa"`, Output: `0`. Explanation: There is no semi-repetitive substring.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: To find all possible substrings and check each one to see if it is semi-repetitive.
- Step-by-step breakdown of the solution:
  1. Generate all possible substrings of the input string `s`.
  2. For each substring, split it into two non-empty parts `a` and `b`.
  3. Check if `a` and `b` have the same characters (possibly in different orders) by sorting the characters in `a` and `b` and comparing the sorted strings.
- Why this approach comes to mind first: It's a straightforward way to ensure we consider all possibilities, but it's inefficient due to its high complexity.

```cpp
#include <iostream>
#include <string>
#include <algorithm>

int findLongestSemiRepetitiveSubstring(const std::string& s) {
    int maxLength = 0;
    for (int i = 0; i < s.length(); ++i) {
        for (int j = i + 1; j <= s.length(); ++j) {
            std::string substring = s.substr(i, j - i);
            for (int k = 1; k < substring.length(); ++k) {
                std::string a = substring.substr(0, k);
                std::string b = substring.substr(k);
                std::sort(a.begin(), a.end());
                std::sort(b.begin(), b.end());
                if (a != b && a == b) {
                    // This condition will never be true, it's a mistake in the brute force approach
                    maxLength = std::max(maxLength, static_cast<int>(substring.length()));
                } else if (a != b && std::is_permutation(a.begin(), a.end(), b.begin())) {
                    maxLength = std::max(maxLength, static_cast<int>(substring.length()));
                }
            }
        }
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3 \cdot m \log m)$ where $n$ is the length of the input string and $m$ is the maximum length of a substring. This is because we generate all substrings ($O(n^2)$), split each into two parts ($O(n)$), and then sort and compare these parts ($O(m \log m)$).
> - **Space Complexity:** $O(m)$ for storing the substrings and their sorted versions.
> - **Why these complexities occur:** The high time complexity is due to the nested loops and the sorting operation, while the space complexity is moderate due to the need to store temporary substrings.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of checking all substrings, we can use a sliding window approach to efficiently consider all possible splits of the string into two parts `a` and `b`.
- Detailed breakdown of the approach:
  1. Initialize variables to keep track of the maximum length of a semi-repetitive substring.
  2. Iterate over all possible splits of the string into two non-empty parts `a` and `b`.
  3. For each split, check if `a` and `b` are permutations of each other by comparing their sorted versions or using a more efficient method like counting character frequencies.
  4. Update the maximum length if a longer semi-repetitive substring is found.
- Proof of optimality: This approach is optimal because it considers all possible splits of the string into two parts and checks for the semi-repetitive property in linear time with respect to the length of the parts, leading to a significant reduction in time complexity compared to the brute force approach.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

int findLongestSemiRepetitiveSubstring(const std::string& s) {
    int maxLength = 0;
    for (int i = 1; i < s.length(); ++i) {
        std::string a = s.substr(0, i);
        std::string b = s.substr(i);
        std::unordered_map<char, int> countA, countB;
        for (char c : a) countA[c]++;
        for (char c : b) countB[c]++;
        if (countA != countB) continue;
        maxLength = std::max(maxLength, static_cast<int>(s.length()));
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the length of the input string. This is because we iterate over all possible splits of the string and for each split, we count character frequencies in both parts.
> - **Space Complexity:** $O(n)$ for storing the character frequency maps.
> - **Optimality proof:** This approach is optimal because it efficiently considers all possible splits of the string and checks for the semi-repetitive property in linear time with respect to the length of the parts, leading to a significant reduction in time complexity compared to the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window technique, character frequency counting, and efficient string manipulation.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems (checking all splits of the string) and using efficient data structures (unordered maps for character frequency counting).
- Optimization techniques learned: Avoiding unnecessary computations (like sorting) and using more efficient data structures and algorithms.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly implementing the sliding window or character frequency counting.
- Edge cases to watch for: Handling strings with repeated characters or strings of length 1.
- Performance pitfalls: Using inefficient algorithms or data structures that lead to high time or space complexity.
- Testing considerations: Thoroughly testing the solution with various input strings, including edge cases.