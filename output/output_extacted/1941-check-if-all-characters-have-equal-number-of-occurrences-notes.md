## Check If All Characters Have Equal Number of Occurrences

**Problem Link:** https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description

**Problem Statement:**
- Input: A string `s`.
- Constraints: `1 <= s.length <= 500`.
- Expected Output: `true` if all characters have equal number of occurrences, `false` otherwise.
- Key Requirements: Count the occurrences of each character and compare them.
- Edge Cases: Empty string, single-character string, strings with varying character frequencies.
- Example Test Cases:
  - Input: `"abacbc"`, Output: `true`.
  - Input: `"aabb"`, Output: `false`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over the string to count the occurrences of each character.
- Step-by-step breakdown:
  1. Create a frequency map (e.g., a dictionary or an array of size 26 for lowercase English letters).
  2. Iterate over the string, incrementing the count for each character in the frequency map.
  3. After counting, iterate over the frequency map to check if all non-zero counts are equal.
- Why this approach comes to mind first: It directly addresses the requirement by counting and comparing character occurrences.

```cpp
#include <iostream>
#include <unordered_map>
using namespace std;

bool areOccurrencesEqual(string s) {
    unordered_map<char, int> frequencyMap;
    for (char c : s) {
        frequencyMap[c]++;
    }
    
    int targetCount = -1;
    for (auto& pair : frequencyMap) {
        if (pair.second > 0) {
            if (targetCount == -1) {
                targetCount = pair.second;
            } else if (pair.second != targetCount) {
                return false;
            }
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the length of the string and $m$ is the number of unique characters. This is because we make two passes: one over the string to count occurrences and another over the frequency map to compare counts.
> - **Space Complexity:** $O(m)$, as in the worst case, every character in the string could be unique, requiring a separate entry in the frequency map.
> - **Why these complexities occur:** The need to iterate over the entire string and potentially over all unique characters leads to these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can still use a frequency map but optimize the comparison step by keeping track of the first non-zero count encountered and comparing all subsequent non-zero counts to this target.
- Detailed breakdown: Similar to the brute force approach, but with an optimized comparison step that stops as soon as it finds a non-matching count.
- Proof of optimality: This approach is optimal because it must iterate over the string at least once to count occurrences and then over the unique characters to compare counts, matching the lower bound of the problem's complexity.

```cpp
#include <iostream>
#include <unordered_map>
using namespace std;

bool areOccurrencesEqual(string s) {
    unordered_map<char, int> frequencyMap;
    for (char c : s) {
        frequencyMap[c]++;
    }
    
    int targetCount = -1;
    for (auto& pair : frequencyMap) {
        if (pair.second > 0) {
            if (targetCount == -1) {
                targetCount = pair.second;
            } else if (pair.second != targetCount) {
                return false;
            }
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the length of the string and $m$ is the number of unique characters, because we make two passes: one over the string and another over the unique characters.
> - **Space Complexity:** $O(m)$, because in the worst case, every character in the string could be unique.
> - **Optimality proof:** This is the best possible time complexity because we must at least read the input string once and compare the counts of unique characters.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Using a frequency map to count character occurrences and optimizing the comparison step.
- Problem-solving patterns: Identifying the need to iterate over the input and unique characters, and optimizing based on problem constraints.
- Optimization techniques: Early termination in the comparison step as soon as a mismatch is found.
- Similar problems to practice: Other string problems involving character frequencies or comparisons.

**Mistakes to Avoid:**
- Not considering edge cases like an empty string or a string with a single character.
- Failing to optimize the comparison step, leading to unnecessary iterations.
- Not validating the input string for null or empty conditions.
- Overcomplicating the solution by using more complex data structures than necessary.