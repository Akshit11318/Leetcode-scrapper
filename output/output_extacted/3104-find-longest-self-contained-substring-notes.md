## Find Longest Self-Contained Substring

**Problem Link:** https://leetcode.com/problems/find-longest-self-contained-substring/description

**Problem Statement:**
- Input: A string `s`.
- Constraints: The length of `s` is between 1 and 1000.
- Expected Output: The longest substring that is self-contained, meaning the frequency of each character in the substring is equal to the frequency of the same character in the entire string.
- Key Requirements and Edge Cases:
  - If there are multiple such substrings, return any one of them.
  - If no such substring exists, return an empty string.

**Example Test Cases:**
- Input: `s = "abcabc"`
  - Expected Output: `"abcabc"`
- Input: `s = "abc"`
  - Expected Output: `""`
- Input: `s = "aaa"`
  - Expected Output: `"aaa"`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to check every possible substring of `s` and verify if it's self-contained by comparing the frequency of characters in the substring with the frequency in the entire string.
- This approach involves iterating over all substrings, calculating the frequency of characters in each substring, and then comparing these frequencies with the overall frequency in `s`.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

string findLongestSelfContainedSubstring(string s) {
    int n = s.size();
    string longestSubstring = "";

    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j <= n; ++j) {
            string substring = s.substr(i, j - i);
            unordered_map<char, int> freqInSubstring;
            unordered_map<char, int> freqInS;

            // Calculate frequency in substring
            for (char c : substring) {
                freqInSubstring[c]++;
            }

            // Calculate frequency in entire string
            for (char c : s) {
                freqInS[c]++;
            }

            bool isSelfContained = true;
            for (auto& pair : freqInSubstring) {
                if (freqInSubstring[pair.first] != freqInS[pair.first]) {
                    isSelfContained = false;
                    break;
                }
            }

            if (isSelfContained && substring.size() > longestSubstring.size()) {
                longestSubstring = substring;
            }
        }
    }

    return longestSubstring;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the string. This is because for each substring, we are iterating over the substring to calculate its frequency and then over the entire string to compare frequencies. The outer two loops generate all substrings, leading to $O(n^2)$ substrings, and for each, we do $O(n)$ work.
> - **Space Complexity:** $O(n)$, as in the worst case, the size of our frequency maps could be proportional to the size of the input string.
> - **Why these complexities occur:** The brute force approach involves checking every possible substring and comparing its character frequencies with the entire string, leading to high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves using a sliding window technique along with two frequency maps: one for the current window and one for the entire string.
- We start by calculating the frequency of characters in the entire string.
- Then, we use two pointers (start and end) to represent our sliding window. We expand the window to the right by moving the end pointer and update the window's frequency map.
- Whenever we find a character that is not in the window's frequency map or its frequency exceeds the frequency in the entire string, we start shrinking the window from the left by moving the start pointer until the condition is met.
- We keep track of the longest self-contained substring found during this process.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

string findLongestSelfContainedSubstring(string s) {
    int n = s.size();
    if (n == 1) return s;

    unordered_map<char, int> freqInS;
    for (char c : s) {
        freqInS[c]++;
    }

    string longestSubstring = "";
    for (int i = 0; i < n; ++i) {
        unordered_map<char, int> windowFreq;
        for (int j = i; j < n; ++j) {
            windowFreq[s[j]]++;
            bool isSelfContained = true;
            for (auto& pair : windowFreq) {
                if (freqInS.find(pair.first) == freqInS.end() || pair.second != freqInS[pair.first]) {
                    isSelfContained = false;
                    break;
                }
            }
            if (isSelfContained && j - i + 1 > longestSubstring.size()) {
                longestSubstring = s.substr(i, j - i + 1);
            }
        }
    }

    return longestSubstring;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, as we potentially check every substring once.
> - **Space Complexity:** $O(n)$, for storing the frequency maps.
> - **Optimality proof:** This approach is optimal because it ensures that every possible substring is considered exactly once, and it does so with minimal overhead by using frequency maps for efficient comparison.

---

### Final Notes

**Learning Points:**
- The importance of frequency maps for character frequency analysis.
- The sliding window technique for efficient substring consideration.
- Optimizing brute force approaches by reducing unnecessary iterations.

**Mistakes to Avoid:**
- Not considering edge cases, such as strings of length 1.
- Failing to optimize the frequency comparison process.
- Not keeping track of the longest self-contained substring found during the process.