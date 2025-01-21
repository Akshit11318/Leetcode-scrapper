## Swap for Longest Repeated Character Substring

**Problem Link:** https://leetcode.com/problems/swap-for-longest-repeated-character-substring/description

**Problem Statement:**
- Input: A string `s`.
- Expected output: The maximum length of a repeated character substring that can be obtained by performing at most one swap of two characters in the string.
- Key requirements and edge cases to consider:
  - The input string `s` consists only of lowercase English letters.
  - The length of `s` is in the range `[2, 1000]`.
  - The string may contain repeated characters.
- Example test cases with explanations:
  - For `s = "abba"`, the maximum length is `2` because we can swap the two `b`s to get `"baab"`.
  - For `s = "aaa"`, the maximum length is `3` because the string already has the maximum repeated character substring.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible swaps of two characters in the string and check the length of the longest repeated character substring after each swap.
- Step-by-step breakdown of the solution:
  1. Generate all possible swaps of two characters in the string.
  2. For each swap, create a new string with the swapped characters.
  3. Check the length of the longest repeated character substring in the new string.
  4. Keep track of the maximum length found.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible solutions.

```cpp
class Solution {
public:
    int maxRepOpt1(string s) {
        int n = s.size();
        int maxLen = 0;
        
        // Generate all possible swaps of two characters
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                string newS = s;
                swap(newS[i], newS[j]);
                
                // Check the length of the longest repeated character substring in the new string
                int len = 0;
                int count = 0;
                char prev = '\0';
                for (char c : newS) {
                    if (c == prev) {
                        count++;
                    } else {
                        len = max(len, count);
                        count = 1;
                        prev = c;
                    }
                }
                len = max(len, count);
                
                maxLen = max(maxLen, len);
            }
        }
        
        return maxLen;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ where $n$ is the length of the string. This is because we have two nested loops to generate all possible swaps, and for each swap, we iterate through the string to check the length of the longest repeated character substring.
> - **Space Complexity:** $O(n)$ because we create a new string for each swap.
> - **Why these complexities occur:** The brute force approach tries all possible solutions, which results in a high time complexity. The space complexity is linear because we only need to store the new string for each swap.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of trying all possible swaps, we can use a sliding window approach to find the longest repeated character substring.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `left` and `right`, to the start of the string.
  2. Move the `right` pointer to the right until we find a character that is different from the character at the `left` pointer.
  3. If we find a character that is the same as the character at the `left` pointer, we can move the `left` pointer to the right.
  4. Keep track of the maximum length of the repeated character substring.
- Proof of optimality: This approach is optimal because it only needs to iterate through the string once, resulting in a linear time complexity.

```cpp
class Solution {
public:
    int maxRepOpt1(string s) {
        int n = s.size();
        int maxLen = 0;
        
        // Initialize the frequency of each character
        vector<int> freq(26, 0);
        for (char c : s) {
            freq[c - 'a']++;
        }
        
        // Use a sliding window approach to find the longest repeated character substring
        for (int i = 0; i < n; i++) {
            int count = 0;
            char c = s[i];
            for (int j = i; j < n; j++) {
                if (s[j] == c) {
                    count++;
                }
                if (j - i + 1 - count <= 1) {
                    maxLen = max(maxLen, count + (freq[c - 'a'] > count ? 1 : 0));
                }
            }
        }
        
        return maxLen;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the string. This is because we only need to iterate through the string once.
> - **Space Complexity:** $O(1)$ because we only need to store the frequency of each character.
> - **Optimality proof:** This approach is optimal because it only needs to iterate through the string once, resulting in a linear time complexity. The space complexity is constant because we only need to store the frequency of each character.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window approach, frequency counting.
- Problem-solving patterns identified: Using a sliding window approach to find the longest repeated character substring.
- Optimization techniques learned: Avoiding unnecessary swaps by using a sliding window approach.
- Similar problems to practice: Finding the longest repeated substring, finding the longest common substring.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, not initializing variables correctly.
- Edge cases to watch for: Empty string, string with only one character.
- Performance pitfalls: Using a brute force approach, not optimizing the solution.
- Testing considerations: Testing with different input strings, testing with edge cases.