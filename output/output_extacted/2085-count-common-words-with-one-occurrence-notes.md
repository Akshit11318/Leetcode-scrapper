## Count Common Words With One Occurrence
**Problem Link:** https://leetcode.com/problems/count-common-words-with-one-occurrence/description

**Problem Statement:**
- Input format: Two arrays of strings, `words1` and `words2`.
- Constraints: Each word is composed of lowercase English letters.
- Expected output format: An integer representing the number of common words that appear exactly once in both arrays.
- Key requirements and edge cases to consider: Handling duplicate words, case sensitivity, and ensuring words appear exactly once in both arrays.
- Example test cases with explanations:
  - Input: `words1 = ["leetcode","apple","apple"], words2 = ["leetcode","apple","love","apple"]`
    - Output: `1`
    - Explanation: Only "leetcode" appears once in both arrays.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Compare each word in `words1` with each word in `words2` to find common words, then count occurrences of each word in both arrays to ensure it appears exactly once.
- Step-by-step breakdown of the solution:
  1. Create frequency maps for `words1` and `words2`.
  2. Iterate through each word in `words1` and check if it exists in `words2`'s frequency map.
  3. If a common word is found, verify that its frequency is 1 in both arrays.
- Why this approach comes to mind first: It directly addresses the problem statement by comparing words and counting occurrences.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>

int countCommonWords(vector<string>& words1, vector<string>& words2) {
    unordered_map<string, int> freq1, freq2;
    for (const string& word : words1) freq1[word]++;
    for (const string& word : words2) freq2[word]++;
    
    int count = 0;
    for (const auto& pair : freq1) {
        if (freq2.find(pair.first) != freq2.end() && pair.second == 1 && freq2[pair.first] == 1) {
            count++;
        }
    }
    
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ and $m$ are the sizes of `words1` and `words2`, respectively. This is because we make two passes through the input arrays to create frequency maps and then a pass through one of the maps to count common words.
> - **Space Complexity:** $O(n + m)$, for storing the frequency maps.
> - **Why these complexities occur:** The time complexity is linear because we perform constant-time operations for each word in both arrays. The space complexity is also linear because in the worst case, every word could be unique, requiring a separate entry in the frequency maps.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The same as the brute force approach, since the problem inherently requires comparing each word in one array with each word in the other and counting occurrences.
- Detailed breakdown of the approach: Same as the brute force, but recognizing that the initial solution is already optimal due to the problem's constraints.
- Proof of optimality: Any solution must at least read the input arrays once and compare each word, leading to a time complexity of at least $O(n + m)$. The space complexity of $O(n + m)$ is also optimal because we must store the frequency of each word.
- Why further optimization is impossible: The problem requires a comparison of each word in both arrays and a count of their occurrences, which cannot be done in less than linear time or space.

```cpp
// The code provided in the brute force section is already optimal.
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ and $m$ are the sizes of `words1` and `words2`, respectively.
> - **Space Complexity:** $O(n + m)$, for storing the frequency maps.
> - **Optimality proof:** The time and space complexities are optimal because any algorithm must perform at least these operations to solve the problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Frequency counting, hash table usage, and understanding the trade-offs between time and space complexity.
- Problem-solving patterns identified: Directly addressing the problem statement and considering the minimum necessary operations to achieve the desired outcome.
- Optimization techniques learned: Recognizing when an initial solution is already optimal and understanding the inherent constraints of the problem.
- Similar problems to practice: Other problems involving frequency counting, string comparisons, and hash table optimizations.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases (e.g., empty arrays, duplicate words), and not validating input.
- Edge cases to watch for: Empty input arrays, arrays with a single element, and arrays with all unique or all duplicate words.
- Performance pitfalls: Using inefficient data structures or algorithms that lead to higher than necessary time or space complexities.
- Testing considerations: Thoroughly testing with a variety of inputs, including edge cases, to ensure the solution is robust and correct.