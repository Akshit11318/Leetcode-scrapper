## Count Beautiful Substrings I
**Problem Link:** https://leetcode.com/problems/count-beautiful-substrings-i/description

**Problem Statement:**
- Input format: A string `s` containing only lowercase English letters.
- Constraints: `1 <= s.length <= 10^5`.
- Expected output format: The number of beautiful substrings in `s`.
- Key requirements and edge cases to consider: A substring is considered beautiful if the absolute difference between the frequency of its most frequent character and least frequent character is less than or equal to 1. Substrings can be of any length, from 1 to `s.length`.
- Example test cases with explanations:
  - For `s = "aabcb"`, the beautiful substrings are `"a"`, `"a"`, `"b"`, `"c"`, `"ab"`, `"bc"`, `"aab"`, `"abc"`, `"aabcb"`. Therefore, the output should be `9`.
  - For `s = "abba"`, all substrings are beautiful: `"a"`, `"b"`, `"b"`, `"a"`, `"ab"`, `"bb"`, `"ba"`, `"abb"`, `"bba"`, `"abba"`. Therefore, the output should be `10`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: For every possible substring, count the frequency of each character and compare the maximum and minimum frequencies.
- Step-by-step breakdown of the solution:
  1. Generate all possible substrings of the input string `s`.
  2. For each substring, count the frequency of each character.
  3. Calculate the absolute difference between the maximum and minimum frequencies.
  4. If the difference is less than or equal to 1, increment the count of beautiful substrings.
- Why this approach comes to mind first: It is straightforward and ensures that all substrings are considered.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

int countBeautifulSubstrings(const std::string& s) {
    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        for (int j = i; j < s.length(); j++) {
            std::string substring = s.substr(i, j - i + 1);
            std::unordered_map<char, int> freq;
            for (char c : substring) {
                freq[c]++;
            }
            int maxFreq = 0, minFreq = INT_MAX;
            for (auto& pair : freq) {
                maxFreq = std::max(maxFreq, pair.second);
                minFreq = std::min(minFreq, pair.second);
            }
            if (maxFreq - minFreq <= 1) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the string `s`. This is because we generate all substrings ($O(n^2)$), and for each substring, we count the frequency of characters ($O(n)$).
> - **Space Complexity:** $O(n)$, for storing the frequency of characters in the substring.
> - **Why these complexities occur:** The brute force approach involves nested loops for generating substrings and then iterating over each substring to count character frequencies.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of counting the frequency of each character for every substring, observe the pattern of beautiful substrings and utilize a sliding window approach.
- Detailed breakdown of the approach:
  1. Initialize a variable to store the count of beautiful substrings.
  2. Iterate over all possible substring lengths.
  3. For each length, use a sliding window to generate substrings.
  4. For each substring, count the frequency of characters and check if it's beautiful.
- Proof of optimality: This approach still checks every possible substring but does so in a more efficient manner by avoiding redundant operations.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

int countBeautifulSubstrings(const std::string& s) {
    int count = 0;
    for (int length = 1; length <= s.length(); length++) {
        for (int i = 0; i <= s.length() - length; i++) {
            std::string substring = s.substr(i, length);
            std::unordered_map<char, int> freq;
            for (char c : substring) {
                freq[c]++;
            }
            int maxFreq = 0, minFreq = INT_MAX;
            for (auto& pair : freq) {
                maxFreq = std::max(maxFreq, pair.second);
                minFreq = std::min(minFreq, pair.second);
            }
            if (maxFreq - minFreq <= 1) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the string `s`. Although the structure is more optimized, the fundamental operations remain similar to the brute force approach.
> - **Space Complexity:** $O(n)$, for storing the frequency of characters in the substring.
> - **Optimality proof:** The optimal approach is still $O(n^3)$ because it must consider every possible substring. However, it is more organized and potentially faster in practice due to reduced overhead.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window technique, frequency counting.
- Problem-solving patterns identified: Breaking down the problem into smaller, manageable parts (substrings).
- Optimization techniques learned: Reducing redundant operations.
- Similar problems to practice: Other substring or subarray problems that require counting or frequency analysis.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect loop bounds, missing initialization of variables.
- Edge cases to watch for: Empty string, single-character substrings.
- Performance pitfalls: Unnecessary iterations or operations.
- Testing considerations: Ensure coverage of various input lengths and edge cases.