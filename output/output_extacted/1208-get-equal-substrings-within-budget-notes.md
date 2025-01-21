## Get Equal Substrings Within Budget
**Problem Link:** https://leetcode.com/problems/get-equal-substrings-within-budget/description

**Problem Statement:**
- Input format and constraints: Given two strings `s` and `t`, and an integer `maxCost`, we need to find the maximum length of a substring of `s` that can be made equal to a substring of `t` by changing at most `maxCost` characters.
- Expected output format: The function should return the maximum length of the substring.
- Key requirements and edge cases to consider: The function should handle edge cases where the input strings are empty or have different lengths.
- Example test cases with explanations:
  - Example 1: Input: `s = "abcd", t = "bcdf", maxCost = 3`, Output: `3`
  - Example 2: Input: `s = "abcd", t = "cdef", maxCost = 3`, Output: `1`
  - Example 3: Input: `s = "", t = "", maxCost = 3`, Output: `0`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves checking all possible substrings of `s` and `t` and calculating the cost of making them equal.
- Step-by-step breakdown of the solution:
  1. Generate all possible substrings of `s` and `t`.
  2. For each pair of substrings, calculate the cost of making them equal by counting the number of different characters.
  3. If the cost is less than or equal to `maxCost`, update the maximum length of the substring.
- Why this approach comes to mind first: The brute force approach is straightforward and easy to implement, but it is not efficient for large input strings.

```cpp
int equalSubstring(string s, string t, int maxCost) {
    int maxLen = 0;
    for (int i = 0; i < s.length(); i++) {
        for (int j = i + 1; j <= s.length(); j++) {
            for (int k = 0; k < t.length(); k++) {
                for (int end = k + 1; end <= t.length(); end++) {
                    int cost = 0;
                    for (int p = 0; p < j - i; p++) {
                        if (s[i + p] != t[k + p]) {
                            cost++;
                        }
                    }
                    if (cost <= maxCost && j - i > maxLen) {
                        maxLen = j - i;
                    }
                }
            }
        }
    }
    return maxLen;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^4)$, where $n$ is the length of the input strings. This is because we are generating all possible substrings and comparing them.
> - **Space Complexity:** $O(1)$, as we are not using any extra space that scales with the input size.
> - **Why these complexities occur:** The time complexity is high because we are using four nested loops to generate all possible substrings and compare them.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a sliding window approach to reduce the time complexity. We can maintain a window of characters in `s` and `t` and calculate the cost of making them equal.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `i` and `j`, to the start of `s` and `t`, respectively.
  2. Initialize a variable `cost` to 0, which will store the cost of making the current window of characters equal.
  3. Initialize a variable `maxLen` to 0, which will store the maximum length of the substring.
  4. Move the pointers `i` and `j` to the right and calculate the cost of making the current window of characters equal.
  5. If the cost exceeds `maxCost`, move the left pointer of the window to the right until the cost is less than or equal to `maxCost`.
  6. Update `maxLen` if the current window size is greater than `maxLen`.
- Proof of optimality: The sliding window approach is optimal because it reduces the time complexity to $O(n^2)$, which is the best possible time complexity for this problem.

```cpp
int equalSubstring(string s, string t, int maxCost) {
    int maxLen = 0;
    for (int i = 0; i < s.length(); i++) {
        for (int j = 0; j < t.length(); j++) {
            int cost = 0;
            int k = 0;
            while (i + k < s.length() && j + k < t.length()) {
                if (s[i + k] != t[j + k]) {
                    cost++;
                }
                if (cost > maxCost) {
                    break;
                }
                k++;
            }
            maxLen = max(maxLen, k);
        }
    }
    return maxLen;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input strings. This is because we are using two nested loops to generate all possible windows of characters.
> - **Space Complexity:** $O(1)$, as we are not using any extra space that scales with the input size.
> - **Optimality proof:** The sliding window approach is optimal because it reduces the time complexity to $O(n^2)$, which is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window approach, dynamic programming.
- Problem-solving patterns identified: Using a window of characters to reduce the time complexity.
- Optimization techniques learned: Reducing the time complexity by using a sliding window approach.
- Similar problems to practice: Other problems that involve finding the maximum length of a substring, such as the Longest Common Substring problem.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as empty input strings.
- Edge cases to watch for: Empty input strings, input strings with different lengths.
- Performance pitfalls: Using a brute force approach, which can result in a high time complexity.
- Testing considerations: Testing the function with different input strings and edge cases to ensure that it works correctly.