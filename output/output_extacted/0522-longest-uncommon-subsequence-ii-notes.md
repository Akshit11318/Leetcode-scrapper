## Longest Uncommon Subsequence II
**Problem Link:** https://leetcode.com/problems/longest-uncommon-subsequence-ii/description

**Problem Statement:**
- Input format and constraints: Given an array of strings `strs`, return the length of the longest uncommon subsequence between them. All the strings in `strs` have the same length. The longest uncommon subsequence is a subsequence that is not common to all the strings in `strs`. If the longest uncommon subsequence does not exist, return `-1`.
- Expected output format: An integer representing the length of the longest uncommon subsequence.
- Key requirements and edge cases to consider: The input array `strs` contains between 2 and 50 strings, each of length between 1 and 10. The total number of characters in all strings does not exceed 500. All strings consist only of lowercase letters.
- Example test cases with explanations:
  - For `strs = ["aba","cdc","eae"]`, the output should be `3`, because the longest uncommon subsequence is `"aba"`, `"cdc"`, or `"eae"`.
  - For `strs = ["aaa","aaa","aa"]`, the output should be `-1`, because all strings are the same.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subsequences of each string in `strs` and check if they are common to all strings. If not, update the length of the longest uncommon subsequence.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsequences of each string in `strs`.
  2. For each subsequence, check if it is common to all strings in `strs`.
  3. If a subsequence is not common to all strings, update the length of the longest uncommon subsequence.
- Why this approach comes to mind first: It is a straightforward approach that checks all possible subsequences.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

int findLUSlength(std::vector<std::string>& strs) {
    int n = strs.size();
    int maxLen = -1;
    
    for (int i = 0; i < n; i++) {
        bool isCommon = true;
        for (int j = 0; j < n; j++) {
            if (i == j) continue;
            if (!isSubsequence(strs[i], strs[j])) {
                isCommon = false;
                break;
            }
        }
        if (!isCommon) {
            maxLen = std::max(maxLen, (int)strs[i].size());
        }
    }
    
    return maxLen;
}

bool isSubsequence(const std::string& s1, const std::string& s2) {
    int i = 0, j = 0;
    while (i < s1.size() && j < s2.size()) {
        if (s1[i] == s2[j]) i++;
        j++;
    }
    return i == s1.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \times m)$, where $n$ is the number of strings and $m$ is the length of each string. This is because we compare each string with every other string.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum length.
> - **Why these complexities occur:** The time complexity is high because we compare each string with every other string, and the space complexity is low because we only use a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: If a string is not a subsequence of any other string, it is the longest uncommon subsequence. Otherwise, if all strings are the same, there is no longest uncommon subsequence.
- Detailed breakdown of the approach:
  1. Sort the strings in descending order of their lengths.
  2. For each string, check if it is a subsequence of any other string. If not, return its length.
  3. If all strings are the same, return -1.
- Proof of optimality: This approach is optimal because it checks each string only once and returns the length of the longest uncommon subsequence as soon as it finds one.

```cpp
int findLUSlength(std::vector<std::string>& strs) {
    std::sort(strs.begin(), strs.end(), [](const std::string& s1, const std::string& s2) {
        return s1.size() > s2.size();
    });
    
    for (int i = 0; i < strs.size(); i++) {
        bool isSubsequence = false;
        for (int j = 0; j < strs.size(); j++) {
            if (i == j) continue;
            if (isSubsequenceOf(strs[i], strs[j])) {
                isSubsequence = true;
                break;
            }
        }
        if (!isSubsequence) {
            return strs[i].size();
        }
    }
    
    return -1;
}

bool isSubsequenceOf(const std::string& s1, const std::string& s2) {
    int i = 0, j = 0;
    while (i < s1.size() && j < s2.size()) {
        if (s1[i] == s2[j]) i++;
        j++;
    }
    return i == s1.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \times m)$, where $n$ is the number of strings and $m$ is the length of each string. This is because we compare each string with every other string.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum length.
> - **Optimality proof:** This approach is optimal because it checks each string only once and returns the length of the longest uncommon subsequence as soon as it finds one.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Subsequence checking, sorting, and iteration.
- Problem-solving patterns identified: Checking each string only once and returning the length of the longest uncommon subsequence as soon as it is found.
- Optimization techniques learned: Sorting the strings in descending order of their lengths to reduce the number of comparisons.
- Similar problems to practice: Longest Common Subsequence, Shortest Common Supersequence.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if a string is a subsequence of itself, not handling the case where all strings are the same.
- Edge cases to watch for: Empty strings, strings with different lengths, strings with the same length but different characters.
- Performance pitfalls: Comparing each string with every other string without sorting them first.
- Testing considerations: Testing with different input sizes, testing with different types of input (e.g., strings with the same length but different characters).