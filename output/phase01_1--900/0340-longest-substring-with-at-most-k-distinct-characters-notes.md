## Longest Substring with At Most K Distinct Characters

**Problem Link:** https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description

**Problem Statement:**
- Input: a string `s` and an integer `k`.
- Constraints: `1 <= s.length <= 5 * 10^4`, `0 <= k <= 10^4`.
- Expected Output: the length of the longest substring of `s` that contains at most `k` distinct characters.
- Key Requirements: find the longest substring with at most `k` distinct characters.
- Edge Cases: handle cases where `k` is 0, `k` equals the number of unique characters in `s`, or `s` is empty.
- Example Test Cases:
  - Input: `s = "eceba", k = 2`
    - Output: `3`
    - Explanation: `"ece"` is the longest substring with at most `2` distinct characters.
  - Input: `s = "aa", k = 1`
    - Output: `2`
    - Explanation: `"aa"` is the longest substring with at most `1` distinct character.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: generate all possible substrings of `s`, then for each substring, count the number of distinct characters. If the count is less than or equal to `k`, update the maximum length found so far.
- Step-by-step breakdown:
  1. Generate all substrings of `s`.
  2. For each substring, count the number of distinct characters.
  3. If the count is less than or equal to `k`, update the maximum length found so far.
- Why this approach comes to mind first: it's straightforward and directly addresses the problem statement.

```cpp
#include <string>
#include <unordered_set>

int lengthOfLongestSubstringKDistinct(std::string s, int k) {
    int maxLength = 0;
    for (int i = 0; i < s.length(); ++i) {
        for (int j = i + 1; j <= s.length(); ++j) {
            std::string substring = s.substr(i, j - i);
            std::unordered_set<char> distinctChars(substring.begin(), substring.end());
            if (distinctChars.size() <= k) {
                maxLength = std::max(maxLength, (int)substring.length());
            }
        }
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ where $n$ is the length of `s`. This is because we are generating all substrings ($O(n^2)$) and for each substring, we are counting distinct characters which in the worst case (all characters are unique) takes $O(n)$ time.
> - **Space Complexity:** $O(n)$ for storing the substring and the set of distinct characters.
> - **Why these complexities occur:** The nested loops for generating all substrings and the operation to count distinct characters within each substring lead to these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: use a sliding window approach to efficiently scan through the string and keep track of the distinct characters within the current window. This approach allows us to avoid generating all substrings explicitly.
- Detailed breakdown:
  1. Initialize a window with two pointers, `left` and `right`, both starting at the beginning of `s`.
  2. Use an unordered map to store the frequency of each character within the current window.
  3. Expand the window to the right by moving `right`. For each new character, update its frequency in the map.
  4. If the number of keys in the map exceeds `k`, shrink the window from the left by moving `left` until the number of keys is less than or equal to `k`.
  5. Update the maximum length of the substring with at most `k` distinct characters.
- Proof of optimality: this approach ensures that we consider all possible substrings without explicitly generating them, reducing the time complexity significantly.

```cpp
#include <string>
#include <unordered_map>

int lengthOfLongestSubstringKDistinct(std::string s, int k) {
    if (s.empty() || k == 0) return 0;
    
    int left = 0, maxLength = 0;
    std::unordered_map<char, int> charFrequency;
    
    for (int right = 0; right < s.length(); ++right) {
        charFrequency[s[right]]++;
        
        while (charFrequency.size() > k) {
            charFrequency[s[left]]--;
            if (charFrequency[s[left]] == 0) {
                charFrequency.erase(s[left]);
            }
            left++;
        }
        
        maxLength = std::max(maxLength, right - left + 1);
    }
    
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of `s`. This is because we are scanning the string once, and the operations within the loop (updating the map and moving the pointers) take constant time on average.
> - **Space Complexity:** $O(min(n, k))$ for storing the frequency of characters in the map.
> - **Optimality proof:** This approach is optimal because it achieves a linear time complexity by avoiding the generation of all substrings and using a sliding window to efficiently scan the string.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sliding window technique, use of unordered maps for frequency counting.
- Problem-solving patterns identified: reducing complexity by avoiding explicit generation of all possible substrings.
- Optimization techniques learned: using a sliding window to efficiently scan through the input string.

**Mistakes to Avoid:**
- Common implementation errors: not updating the frequency map correctly, not handling edge cases properly (e.g., empty string, `k` equals 0).
- Edge cases to watch for: handling `k` being greater than the number of unique characters in `s`, ensuring the sliding window approach correctly handles substrings of varying lengths.
- Performance pitfalls: using a brute force approach that generates all substrings, leading to high time complexity.
- Testing considerations: thoroughly testing the function with various inputs, including edge cases, to ensure correctness and efficiency.