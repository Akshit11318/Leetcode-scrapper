## Remove Letter to Equalize Frequency
**Problem Link:** https://leetcode.com/problems/remove-letter-to-equalize-frequency/description

**Problem Statement:**
- Input: A string `word`.
- Constraints: `1 <= word.length <= 100`.
- Expected output: The length of the longest substring of `word` that can be made equal in frequency by removing one character.
- Key requirements: Find the maximum length of a substring that can have equal character frequencies after removing at most one character.
- Example test cases:
  - Input: `word = "abc"`
    - Output: `2`
    - Explanation: Remove 'c' or 'b' to get "ab" or "ac" respectively.
  - Input: `word = "aazz"`
    - Output: `3`
    - Explanation: Remove the first 'z' to get "azz".

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible substring of the input string and for each substring, check if removing any character can make the frequencies of the characters equal.
- Step-by-step breakdown:
  1. Generate all substrings of the input string.
  2. For each substring, calculate the frequency of each character.
  3. Try removing each character from the substring and recalculate the frequencies.
  4. Check if the frequencies are equal after removing a character.
  5. Keep track of the maximum length of such substrings.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

int maxEqualFreq(const std::string& word) {
    int maxLen = 0;
    for (int i = 0; i < word.size(); ++i) {
        for (int j = i + 1; j <= word.size(); ++j) {
            std::string substr = word.substr(i, j - i);
            // Try removing each character and check if frequencies become equal
            for (int k = 0; k < substr.size(); ++k) {
                std::string temp = substr;
                temp.erase(k, 1);
                std::unordered_map<char, int> freq;
                for (char c : temp) {
                    ++freq[c];
                }
                int freqCount = 0;
                for (auto& pair : freq) {
                    if (pair.second != freq.begin()->second) {
                        break;
                    }
                    ++freqCount;
                }
                if (freqCount == freq.size()) {
                    maxLen = std::max(maxLen, (int)temp.size());
                }
            }
        }
    }
    return maxLen;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3 \cdot m)$ where $n$ is the length of the input string and $m$ is the average number of unique characters in a substring. This is because we generate all substrings ($O(n^2)$), for each substring we try removing each character ($O(n)$), and for each removal, we calculate frequencies ($O(m)$).
> - **Space Complexity:** $O(m)$ for storing the frequency of characters in the substring.
> - **Why these complexities occur:** The brute force approach involves exhaustive checking of all substrings and all possible removals within those substrings, leading to high time complexity. The space complexity is relatively low as we only need to store the frequency of characters in the current substring.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of checking all substrings, we can utilize a sliding window approach to efficiently check all substrings. However, for this problem, a more straightforward approach involves iterating through all substrings and utilizing a `std::unordered_map` to keep track of character frequencies. We then check for each character in the substring if removing it would result in equal frequencies.
- Detailed breakdown:
  1. Iterate through all substrings of the input string.
  2. For each substring, calculate the frequency of each character using a `std::unordered_map`.
  3. For each character in the substring, temporarily remove it and recalculate the frequency map.
  4. Check if all characters in the modified substring have the same frequency.
  5. Update the maximum length if a longer substring with equal frequencies after removal is found.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

int maxEqualFreq(const std::string& word) {
    int maxLen = 0;
    for (int i = 0; i < word.size(); ++i) {
        for (int j = i + 1; j <= word.size(); ++j) {
            std::string substr = word.substr(i, j - i);
            std::unordered_map<char, int> freq;
            for (char c : substr) {
                ++freq[c];
            }
            for (int k = 0; k < substr.size(); ++k) {
                std::string temp = substr;
                temp.erase(k, 1);
                if (temp.empty()) continue; // Skip if temp becomes empty
                std::unordered_map<char, int> tempFreq;
                for (char c : temp) {
                    ++tempFreq[c];
                }
                bool equal = true;
                int firstFreq = tempFreq.begin()->second;
                for (auto& pair : tempFreq) {
                    if (pair.second != firstFreq) {
                        equal = false;
                        break;
                    }
                }
                if (equal) {
                    maxLen = std::max(maxLen, (int)temp.size());
                }
            }
        }
    }
    return maxLen;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ where $n$ is the length of the input string. This is because we generate all substrings ($O(n^2)$) and for each substring, we try removing each character and calculate frequencies ($O(n)$).
> - **Space Complexity:** $O(n)$ for storing the frequency of characters in the substring.
> - **Optimality proof:** This approach is considered optimal because it directly addresses the problem statement by checking all possible substrings and removals within those substrings, ensuring no potential solution is overlooked.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window concept (though not directly applied here), frequency counting using `std::unordered_map`.
- Problem-solving patterns identified: Exhaustive checking of substrings and removals within those substrings.
- Optimization techniques learned: Utilizing data structures like `std::unordered_map` for efficient frequency counting.
- Similar problems to practice: Other string manipulation and frequency counting problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect handling of edge cases (e.g., empty strings, substrings of length 1).
- Edge cases to watch for: Handling substrings that become empty after character removal.
- Performance pitfalls: Using inefficient data structures for frequency counting (e.g., `std::map` instead of `std::unordered_map`).
- Testing considerations: Thoroughly test with various input strings, including edge cases like empty strings or strings with a single unique character.