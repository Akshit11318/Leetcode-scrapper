## Longest Substring with At Most Two Distinct Characters

**Problem Link:** https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/description

**Problem Statement:**
- Input format and constraints: Given a string `s`, find the length of the longest substring that contains at most two distinct characters.
- Expected output format: Return the length of the longest substring.
- Key requirements and edge cases to consider: Handle empty strings, strings with one or two distinct characters, and strings with more than two distinct characters.
- Example test cases with explanations:
  - Example 1: Input: `s = "eceba"`, Output: `3`, Explanation: The substring `"ece"` contains at most two distinct characters.
  - Example 2: Input: `s = "ccaabbb"`, Output: `5`, Explanation: The substring `"aabbb"` contains at most two distinct characters.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible substring of the input string and count the number of distinct characters in each substring.
- Step-by-step breakdown of the solution:
  1. Iterate over the input string to generate all possible substrings.
  2. For each substring, use a `set` to count the number of distinct characters.
  3. If the number of distinct characters is less than or equal to 2, update the maximum length of the substring.
- Why this approach comes to mind first: It is straightforward and easy to implement, but it is not efficient for large input strings.

```cpp
class Solution {
public:
    int lengthOfLongestSubstringTwoDistinct(string s) {
        int n = s.size();
        int maxLength = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                string substring = s.substr(i, j - i + 1);
                set<char> distinctChars(substring.begin(), substring.end());
                if (distinctChars.size() <= 2) {
                    maxLength = max(maxLength, (int)substring.size());
                }
            }
        }
        return maxLength;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input string. The reason is that we are generating all possible substrings ($O(n^2)$) and then using a `set` to count the number of distinct characters in each substring ($O(n)$).
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string. The reason is that we are using a `set` to store the distinct characters in each substring.
> - **Why these complexities occur:** The brute force approach has a high time complexity because it generates all possible substrings and checks each one individually. The space complexity is relatively low because we are only storing the distinct characters in each substring.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a sliding window approach to keep track of the maximum length of the substring with at most two distinct characters.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `left` and `right`, to the beginning of the input string.
  2. Use a `map` to store the frequency of each character in the current window.
  3. Move the `right` pointer to the right and update the frequency of each character in the `map`.
  4. If the number of distinct characters in the `map` exceeds 2, move the `left` pointer to the right and update the frequency of each character in the `map`.
  5. Update the maximum length of the substring with at most two distinct characters.
- Proof of optimality: The sliding window approach ensures that we only consider substrings with at most two distinct characters, and we only need to consider each character once.

```cpp
class Solution {
public:
    int lengthOfLongestSubstringTwoDistinct(string s) {
        int n = s.size();
        int maxLength = 0;
        int left = 0;
        map<char, int> charFrequency;
        
        for (int right = 0; right < n; right++) {
            charFrequency[s[right]]++;
            while (charFrequency.size() > 2) {
                charFrequency[s[left]]--;
                if (charFrequency[s[left]] == 0) {
                    charFrequency.erase(s[left]);
                }
                left++;
            }
            maxLength = max(maxLength, right - left + 1);
        }
        return maxLength;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string. The reason is that we are only considering each character once.
> - **Space Complexity:** $O(1)$, where $n$ is the length of the input string. The reason is that we are only storing the frequency of each character in the current window.
> - **Optimality proof:** The sliding window approach ensures that we only consider substrings with at most two distinct characters, and we only need to consider each character once. This approach is optimal because it has a linear time complexity and a constant space complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window approach, `map` data structure.
- Problem-solving patterns identified: Using a `map` to store frequency of characters, using a sliding window approach to consider substrings.
- Optimization techniques learned: Avoiding unnecessary computations by only considering each character once.
- Similar problems to practice: Longest substring with at most k distinct characters, longest substring without repeating characters.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the frequency of characters correctly, not handling edge cases correctly.
- Edge cases to watch for: Empty strings, strings with one or two distinct characters, strings with more than two distinct characters.
- Performance pitfalls: Using a brute force approach with a high time complexity.
- Testing considerations: Testing with different input strings, testing with edge cases.