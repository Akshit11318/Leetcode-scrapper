## Unique Substrings in Wraparound String
**Problem Link:** https://leetcode.com/problems/unique-substrings-in-wraparound-string/description

**Problem Statement:**
- Input: A string `p`.
- Output: The number of unique non-empty substrings of `p` when considering a wraparound string.
- Key requirements: 
  - Consider all substrings, including those that wrap around to the beginning of the string.
  - Count each unique substring only once.
- Example test cases:
  - Input: `p = "a"`
    - Output: `1`
    - Explanation: The unique substrings are `"a"`.
  - Input: `p = "cac"`
    - Output: `2`
    - Explanation: The unique substrings are `"a"`, `"c"`, but `"ca"` and `"ac"` are not unique due to the wraparound, so only `"a"` and `"c"` are counted.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves generating all possible substrings of `p` and then checking for uniqueness.
- Step-by-step breakdown:
  1. Generate all substrings of `p`, including those that wrap around.
  2. Store each substring in a set to automatically eliminate duplicates.
  3. Count the number of unique substrings in the set.

```cpp
#include <iostream>
#include <string>
#include <unordered_set>

int findSubstringInWraproundString(const std::string& p) {
    std::unordered_set<std::string> uniqueSubstrings;
    int n = p.size();
    
    for (int length = 1; length <= n; ++length) {
        for (int start = 0; start < n; ++start) {
            std::string substring;
            for (int i = 0; i < length; ++i) {
                int index = (start + i) % n;
                substring += p[index];
            }
            uniqueSubstrings.insert(substring);
        }
    }
    
    return uniqueSubstrings.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$, where $n$ is the length of string `p` and $m$ is the average length of substrings. The reason is that we generate all substrings and insert them into a set, which takes linear time per insertion.
> - **Space Complexity:** $O(n^2)$, because in the worst case, we might store all substrings in the set.
> - **Why these complexities occur:** These complexities occur due to the brute force nature of generating all substrings and checking for uniqueness.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Instead of generating all substrings, we can observe the pattern of wraparound and uniqueness.
- Detailed breakdown:
  1. Initialize a set to store unique substrings and a variable to track the current maximum length of substrings ending at each character.
  2. Iterate through the string `p`. For each character, check if it can extend the current substring or if it needs to start a new one due to the wraparound condition.
  3. Update the set of unique substrings and the maximum length accordingly.

```cpp
#include <iostream>
#include <string>
#include <unordered_set>

int findSubstringInWraproundString(const std::string& p) {
    std::unordered_set<std::string> uniqueSubstrings;
    int n = p.size();
    int maxLengths[26] = {0}; // Maximum length of substrings ending at each character
    
    int maxLength = 0;
    for (int i = 0; i < n; ++i) {
        int charIndex = p[i] - 'a';
        if (i == 0 || (p[i] - p[i-1] != 1 && p[i] - p[i-1] != -25)) {
            // If the current character cannot extend the previous substring, reset maxLength
            maxLength = 1;
        } else {
            // If it can extend, increment maxLength
            maxLength++;
        }
        
        // Update maxLengths for the current character
        maxLengths[charIndex] = std::max(maxLengths[charIndex], maxLength);
    }
    
    int count = 0;
    for (int i = 0; i < 26; ++i) {
        count += maxLengths[i];
    }
    
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of string `p`. We only need to iterate through the string once.
> - **Space Complexity:** $O(1)$, because we use a fixed-size array `maxLengths` to track the maximum lengths.
> - **Optimality proof:** This approach is optimal because it directly calculates the number of unique substrings without generating all of them, thus avoiding unnecessary computations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Observing patterns, using sets for uniqueness, and optimizing iterations.
- Problem-solving patterns: Identifying the need to avoid brute force and looking for patterns that can reduce computational complexity.
- Optimization techniques: Using fixed-size arrays for tracking maximum lengths instead of dynamic data structures.

**Mistakes to Avoid:**
- Generating all substrings unnecessarily.
- Not considering the wraparound condition correctly.
- Using inefficient data structures for tracking unique substrings.