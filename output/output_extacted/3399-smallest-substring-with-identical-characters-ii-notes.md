## Smallest Substring with Identical Characters II

**Problem Link:** https://leetcode.com/problems/smallest-substring-with-identical-characters-ii/description

**Problem Statement:**
- Input: a string `s` and an integer `k`.
- Constraints: `1 <= s.length <= 10^5`, `1 <= k <= 26`.
- Expected Output: the length of the smallest substring that contains `k` distinct characters.
- Key Requirements: Find the smallest substring with `k` distinct characters. If no such substring exists, return `-1`.
- Edge Cases: Handle cases where `s` is empty, `k` is greater than the number of distinct characters in `s`, or `k` is 1.
- Example Test Cases:
  - Input: `s = "abc", k = 2`, Output: `2`
  - Input: `s = "abc", k = 3`, Output: `3`
  - Input: `s = "aa", k = 1`, Output: `1`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible substring of `s` and count the number of distinct characters in each substring.
- Step-by-step breakdown of the solution:
  1. Generate all possible substrings of `s`.
  2. For each substring, count the number of distinct characters.
  3. If the number of distinct characters is equal to `k`, update the minimum length.
- Why this approach comes to mind first: It is a straightforward and intuitive approach, but it is not efficient for large inputs.

```cpp
class Solution {
public:
    int smallestSubstring(string s, int k) {
        int n = s.length();
        int minLen = INT_MAX;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j <= n; j++) {
                string substr = s.substr(i, j - i);
                unordered_set<char> distinctChars(substr.begin(), substr.end());
                if (distinctChars.size() == k) {
                    minLen = min(minLen, (int)substr.length());
                }
            }
        }
        return minLen == INT_MAX ? -1 : minLen;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of `s`. This is because we generate all possible substrings of `s` and for each substring, we count the number of distinct characters.
> - **Space Complexity:** $O(n)$, where $n$ is the length of `s`. This is because we store the distinct characters of each substring in a set.
> - **Why these complexities occur:** The brute force approach has high time complexity because it generates all possible substrings of `s`, which is $O(n^2)$. Additionally, for each substring, it counts the number of distinct characters, which is $O(n)$. Therefore, the overall time complexity is $O(n^3)$.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a sliding window approach to efficiently find the smallest substring with `k` distinct characters.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `left` and `right`, to the beginning of `s`.
  2. Use an unordered map to store the frequency of each character in the current window.
  3. Move the `right` pointer to the right and update the frequency map.
  4. If the number of distinct characters in the current window is greater than or equal to `k`, move the `left` pointer to the right and update the frequency map.
  5. Keep track of the minimum length of the substring with `k` distinct characters.
- Proof of optimality: The sliding window approach ensures that we only consider substrings that have at least `k` distinct characters, which reduces the search space significantly.

```cpp
class Solution {
public:
    int smallestSubstring(string s, int k) {
        int n = s.length();
        int minLen = INT_MAX;
        unordered_map<char, int> freq;
        for (int right = 0; right < n; right++) {
            freq[s[right]]++;
            int distinctChars = 0;
            for (auto& pair : freq) {
                if (pair.second > 0) {
                    distinctChars++;
                }
            }
            if (distinctChars >= k) {
                for (int left = 0; left <= right; left++) {
                    if (freq[s[left]] == 1) {
                        freq.erase(s[left]);
                    } else {
                        freq[s[left]]--;
                    }
                    distinctChars = 0;
                    for (auto& pair : freq) {
                        if (pair.second > 0) {
                            distinctChars++;
                        }
                    }
                    if (distinctChars < k) {
                        break;
                    }
                    minLen = min(minLen, right - left + 1);
                }
            }
        }
        return minLen == INT_MAX ? -1 : minLen;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `s`. This is because we use a sliding window approach to efficiently find the smallest substring with `k` distinct characters.
> - **Space Complexity:** $O(n)$, where $n` is the length of `s`. This is because we store the frequency of each character in the current window in an unordered map.
> - **Optimality proof:** The sliding window approach ensures that we only consider substrings that have at least `k` distinct characters, which reduces the search space significantly. Therefore, the time complexity is $O(n)$, which is optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window approach, frequency counting, and optimization techniques.
- Problem-solving patterns identified: Reducing the search space by considering only substrings with at least `k` distinct characters.
- Optimization techniques learned: Using an unordered map to store the frequency of each character in the current window.
- Similar problems to practice: Find the smallest substring with at least `k` distinct characters, find the longest substring with at most `k` distinct characters.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the frequency map correctly, not considering edge cases.
- Edge cases to watch for: Empty string, `k` is greater than the number of distinct characters in `s`, `k` is 1.
- Performance pitfalls: Using a brute force approach, not optimizing the search space.
- Testing considerations: Test the solution with different inputs, including edge cases, and verify the correctness of the output.