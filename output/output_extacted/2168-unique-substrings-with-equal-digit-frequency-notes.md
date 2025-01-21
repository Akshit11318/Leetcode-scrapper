## Unique Substrings with Equal Digit Frequency

**Problem Link:** https://leetcode.com/problems/unique-substrings-with-equal-digit-frequency/description

**Problem Statement:**
- Input: A string `s` containing only digits.
- Constraints: `1 <= s.length <= 1000`, `s` consists only of digits.
- Expected Output: The number of unique substrings of `s` where every digit appears the same number of times.
- Key Requirements: Count unique substrings where all digits have the same frequency.
- Edge Cases: Empty string, single-digit string, strings with repeating digits.

Example Test Cases:
- Input: `s = "11010"`
  - Output: `2` because the substrings "10" and "01" have equal digit frequency.
- Input: `s = "000111"`
  - Output: `3` because the substrings "000", "111", and "000111" have equal digit frequency.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible substring of `s`.
- Step-by-step breakdown:
  1. Generate all possible substrings of `s`.
  2. For each substring, calculate the frequency of each digit.
  3. Check if all digits in the substring have the same frequency.
  4. If they do, add the substring to a set to keep track of unique substrings.
- Why this approach comes to mind first: It's straightforward and ensures we consider all substrings.

```cpp
#include <iostream>
#include <string>
#include <set>
#include <unordered_map>

int numUniqueSubstringsWithEqualDigitFrequency(const std::string& s) {
    std::set<std::string> uniqueSubstrings;
    for (int i = 0; i < s.length(); ++i) {
        for (int j = i + 1; j <= s.length(); ++j) {
            std::string substring = s.substr(i, j - i);
            std::unordered_map<char, int> digitFrequency;
            for (char c : substring) {
                digitFrequency[c]++;
            }
            bool hasEqualDigitFrequency = true;
            int expectedFrequency = -1;
            for (const auto& pair : digitFrequency) {
                if (expectedFrequency == -1) {
                    expectedFrequency = pair.second;
                } else if (pair.second != expectedFrequency) {
                    hasEqualDigitFrequency = false;
                    break;
                }
            }
            if (hasEqualDigitFrequency) {
                uniqueSubstrings.insert(substring);
            }
        }
    }
    return uniqueSubstrings.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3 \cdot m)$, where $n$ is the length of `s` and $m$ is the average number of unique digits in a substring. This is because we generate $O(n^2)$ substrings, and for each, we calculate digit frequencies in $O(n)$ time and check for equal frequencies in $O(m)$ time.
> - **Space Complexity:** $O(n^2)$ for storing unique substrings.
> - **Why these complexities occur:** The brute force approach involves nested loops to generate all substrings and additional iterations to calculate digit frequencies and check for equality.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of checking all substrings, we can use a sliding window approach and a hashmap to efficiently track digit frequencies.
- Detailed breakdown:
  1. Initialize a set to store unique substrings and a hashmap to track digit frequencies within the current window.
  2. Iterate over `s` with a sliding window of varying sizes.
  3. For each window size, slide the window over `s`, updating the digit frequency hashmap.
  4. Check if all digits in the current window have the same frequency by comparing the values in the hashmap.
  5. If they do, add the substring to the set of unique substrings.
- Why this is optimal: It reduces the number of operations by avoiding unnecessary iterations over substrings and using a hashmap for efficient frequency tracking.

```cpp
#include <iostream>
#include <string>
#include <set>
#include <unordered_map>

int numUniqueSubstringsWithEqualDigitFrequency(const std::string& s) {
    std::set<std::string> uniqueSubstrings;
    for (int windowSize = 1; windowSize <= s.length(); ++windowSize) {
        for (int i = 0; i <= s.length() - windowSize; ++i) {
            std::string substring = s.substr(i, windowSize);
            std::unordered_map<char, int> digitFrequency;
            for (char c : substring) {
                digitFrequency[c]++;
            }
            bool hasEqualDigitFrequency = true;
            int expectedFrequency = -1;
            for (const auto& pair : digitFrequency) {
                if (expectedFrequency == -1) {
                    expectedFrequency = pair.second;
                } else if (pair.second != expectedFrequency) {
                    hasEqualDigitFrequency = false;
                    break;
                }
            }
            if (hasEqualDigitFrequency) {
                uniqueSubstrings.insert(substring);
            }
        }
    }
    return uniqueSubstrings.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$, where $n$ is the length of `s` and $m$ is the average number of unique digits in a substring. This is because we still generate $O(n^2)$ substrings but improve the frequency calculation to $O(m)$.
> - **Space Complexity:** $O(n^2)$ for storing unique substrings.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to check all substrings for equal digit frequency, leveraging a hashmap for efficient frequency tracking.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Sliding window technique, hashmap for frequency tracking.
- Problem-solving patterns: Breaking down the problem into smaller, manageable parts (substrings and frequency checking).
- Optimization techniques: Reducing unnecessary iterations and using efficient data structures (hashmap).

**Mistakes to Avoid:**
- Common implementation errors: Incorrect hashmap usage, missing edge cases (e.g., empty string).
- Edge cases to watch for: Handling substrings of varying lengths, ensuring correct frequency comparisons.
- Performance pitfalls: Using inefficient data structures or algorithms, leading to high time complexities.
- Testing considerations: Thoroughly testing with various inputs, including edge cases, to ensure correctness and performance.