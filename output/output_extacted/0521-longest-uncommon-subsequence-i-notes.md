## Longest Uncommon Subsequence I
**Problem Link:** https://leetcode.com/problems/longest-uncommon-subsequence-i/description

**Problem Statement:**
- Given two strings `a` and `b`, find the length of the longest uncommon subsequence of these two strings.
- A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without disturbing the relative positions of the remaining characters (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
- A subsequence `x` of `a` is considered uncommon if it is not a subsequence of `b`. Similarly, a subsequence `y` of `b` is considered uncommon if it is not a subsequence of `a`.
- Input format: Two strings `a` and `b`.
- Constraints: `1 <= a.length, b.length <= 100`.
- Expected output format: The length of the longest uncommon subsequence.
- Key requirements: Find the longest subsequence that is unique to either `a` or `b`.
- Edge cases: If `a` and `b` are the same, there is no uncommon subsequence.

**Example Test Cases:**
- `a = "aba", b = "cdc"`, Output: `3` (Explanation: The longest uncommon subsequence is "aba" (or "cdc"), which has a length of 3.)
- `a = "aaa", b = "bbb"`, Output: `3` (Explanation: The longest uncommon subsequence is "aaa" (or "bbb"), which has a length of 3.)
- `a = "aaa", b = "aaa"`, Output: `-1` (Explanation: There is no uncommon subsequence.)

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible subsequences of both strings `a` and `b`, and then check each subsequence of `a` to see if it is not a subsequence of `b`, and vice versa.
- This involves using nested loops to generate all subsequences and then checking for each subsequence if it is uncommon.

```cpp
#include <iostream>
#include <vector>
#include <string>

int findLUSlength(std::string a, std::string b) {
    if (a == b) return -1; // If strings are the same, no uncommon subsequence exists

    int maxLength = 0;
    for (int mask = 1; mask < (1 << a.size()); ++mask) {
        std::string subsequence;
        for (int i = 0; i < a.size(); ++i) {
            if (mask & (1 << i)) {
                subsequence += a[i];
            }
        }

        bool isUncommon = true;
        for (int i = 0; i < b.size(); ++i) {
            int j = 0;
            for (; j < subsequence.size() && i < b.size(); ++i) {
                if (subsequence[j] == b[i]) {
                    j++;
                }
            }
            if (j == subsequence.size()) {
                isUncommon = false;
                break;
            }
            i--; // To correctly reset for the next iteration
        }
        if (isUncommon) {
            maxLength = std::max(maxLength, (int)subsequence.size());
        }
    }

    for (int mask = 1; mask < (1 << b.size()); ++mask) {
        std::string subsequence;
        for (int i = 0; i < b.size(); ++i) {
            if (mask & (1 << i)) {
                subsequence += b[i];
            }
        }

        bool isUncommon = true;
        for (int i = 0; i < a.size(); ++i) {
            int j = 0;
            for (; j < subsequence.size() && i < a.size(); ++i) {
                if (subsequence[j] == a[i]) {
                    j++;
                }
            }
            if (j == subsequence.size()) {
                isUncommon = false;
                break;
            }
            i--; // To correctly reset for the next iteration
        }
        if (isUncommon) {
            maxLength = std::max(maxLength, (int)subsequence.size());
        }
    }

    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot m)$ where $n$ is the length of the shorter string and $m$ is the length of the longer string. This is because we generate all subsequences (which takes $O(2^n)$ time) and for each subsequence, we check if it is uncommon by comparing it against the other string (taking $O(m)$ time).
> - **Space Complexity:** $O(n)$ for storing the subsequence.
> - **Why these complexities occur:** The brute force approach involves generating all possible subsequences and then checking each one, leading to exponential time complexity due to the number of subsequences and linear space complexity for storing each subsequence.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal insight is realizing that if `a` and `b` are not equal, then the longer string must contain a subsequence that is not present in the shorter string. Thus, the longest uncommon subsequence can be either `a` or `b` itself if they are of different lengths.
- If `a` and `b` are of the same length and not equal, then the longest uncommon subsequence will be the entire string `a` or `b` because they cannot be subsequences of each other due to their differing characters.
- If `a` and `b` are equal, there is no uncommon subsequence, so we return `-1`.

```cpp
#include <iostream>
#include <string>

int findLUSlength(std::string a, std::string b) {
    if (a == b) {
        return -1; // No uncommon subsequence
    } else {
        return std::max(a.size(), b.size()); // The longer string is the longest uncommon subsequence
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the string, because comparing two strings takes linear time in the length of the strings.
> - **Space Complexity:** $O(1)$, as we do not use any additional space that scales with input size.
> - **Optimality proof:** This is optimal because we directly compare the two input strings and return the length of the longer one if they are different, or `-1` if they are the same. This approach takes advantage of the fact that the longest uncommon subsequence must be one of the input strings themselves if they are different, or there is none if they are the same.

---

### Final Notes

**Learning Points:**
- The importance of understanding the problem constraints and how they can simplify the solution.
- Recognizing that sometimes, the optimal solution involves directly utilizing the given constraints without needing to explore all possible solutions.
- The difference between brute force and optimal approaches, and how to identify when a simpler, more efficient solution exists.

**Mistakes to Avoid:**
- Overcomplicating the problem by not fully considering the constraints.
- Failing to recognize when a simpler approach can solve the problem more efficiently.
- Not testing edge cases, such as when the input strings are equal or of different lengths.