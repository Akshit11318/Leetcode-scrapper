## Minimum Substring Partition of Equal Character Frequency
**Problem Link:** https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/description

**Problem Statement:**
- Input: A string `s`.
- Output: The minimum number of substrings of `s` that can be partitioned such that each substring has equal character frequency.
- Key Requirements:
  - A substring can be partitioned if all characters in it have the same frequency.
- Edge Cases:
  - Empty string.
  - Single character string.
- Example Test Cases:
  - Input: `s = "abc"`
    - Output: `3`
  - Input: `s = "aaabbb"`
    - Output: `2`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to check every possible substring of the input string `s`.
- For each substring, calculate the frequency of each character and check if all frequencies are equal.
- If they are equal, increment a counter for the number of valid substrings.
- This approach checks all possible partitions of the string, hence it is brute force.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

int minPartition(const std::string& s) {
    int n = s.size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j <= n; j++) {
            std::string substr = s.substr(i, j - i);
            std::unordered_map<char, int> freq;
            for (char c : substr) {
                freq[c]++;
            }
            bool equalFreq = true;
            int expectedFreq = -1;
            for (auto& pair : freq) {
                if (expectedFreq == -1) {
                    expectedFreq = pair.second;
                } else if (pair.second != expectedFreq) {
                    equalFreq = false;
                    break;
                }
            }
            if (equalFreq) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input string. This is because for each character in the string (which takes $O(n)$), we are generating all possible substrings (another $O(n)$), and for each substring, we are calculating the frequency of characters (yet another $O(n)$).
> - **Space Complexity:** $O(n)$, primarily due to the storage of the frequency map and the substring.
> - **Why these complexities occur:** The brute force approach checks every possible substring, leading to a cubic time complexity. The space complexity is linear due to the need to store the frequency of characters in the current substring.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a sliding window approach combined with a frequency map to efficiently check for substrings with equal character frequencies.
- We maintain a frequency map for characters within the current window.
- We expand the window to the right, updating the frequency map, and check if all frequencies are equal at each step.
- If they are equal, we have found a valid substring and can consider partitioning the string at this point.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

int minPartition(const std::string& s) {
    int n = s.size();
    int minCount = INT_MAX;
    for (int i = 0; i < n; i++) {
        std::unordered_map<char, int> freq;
        for (int j = i; j < n; j++) {
            freq[s[j]]++;
            bool equalFreq = true;
            int expectedFreq = -1;
            for (auto& pair : freq) {
                if (expectedFreq == -1) {
                    expectedFreq = pair.second;
                } else if (pair.second != expectedFreq) {
                    equalFreq = false;
                    break;
                }
            }
            if (equalFreq) {
                int remaining = minPartition(s.substr(j + 1));
                if (remaining != INT_MAX) {
                    minCount = std::min(minCount, 1 + remaining);
                }
            }
        }
    }
    if (minCount == INT_MAX) {
        return 1; // If no partition is found, return 1
    }
    return minCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, because for each character, we potentially scan the rest of the string once.
> - **Space Complexity:** $O(n)$, due to the recursive call stack and the frequency map.
> - **Optimality proof:** This approach is optimal because it efficiently explores all possible partitions of the string by using a sliding window and recursive calls to check the remaining part of the string after a valid partition is found.

---

### Final Notes

**Learning Points:**
- The importance of the sliding window technique in string problems.
- How to apply recursive thinking to solve problems involving partitions or splits.
- The use of frequency maps to efficiently track character frequencies.

**Mistakes to Avoid:**
- Not considering all edge cases, such as an empty string or a string with a single unique character.
- Not optimizing the solution for time complexity, which can lead to inefficient solutions for large inputs.
- Failing to validate inputs and handle potential errors, such as null or invalid input strings.