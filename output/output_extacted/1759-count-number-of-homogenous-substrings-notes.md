## Count Number of Homogenous Substrings

**Problem Link:** https://leetcode.com/problems/count-number-of-homogenous-substrings/description

**Problem Statement:**
- Input format: a string `s` containing only lowercase letters.
- Constraints: `1 <= s.length <= 100`.
- Expected output format: the number of homogenous substrings in `s`.
- Key requirements and edge cases to consider: A homogenous substring is one where all characters are the same. We must count all possible substrings, including single-character substrings.

**Example Test Cases:**
- For `s = "abc"`, the output should be `3` because there are three homogenous substrings: `"a"`, `"b"`, and `"c"`.
- For `s = "aaa"`, the output should be `6` because the homogenous substrings are `"a"`, `"a"`, `"a"`, `"aa"`, `"aa"`, and `"aaa"`.

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible substring of `s` to see if it is homogenous.
- Step-by-step breakdown:
  1. Generate all possible substrings of `s`.
  2. For each substring, check if all its characters are the same.
  3. If a substring is homogenous, increment a counter.
- This approach comes to mind first because it directly addresses the problem statement without requiring additional insights.

```cpp
int countHomogenousSubstrings(string s) {
    int count = 0;
    for (int i = 0; i < s.size(); i++) {
        for (int j = i + 1; j <= s.size(); j++) {
            string substr = s.substr(i, j - i);
            bool isHomogenous = true;
            for (int k = 1; k < substr.size(); k++) {
                if (substr[k] != substr[k - 1]) {
                    isHomogenous = false;
                    break;
                }
            }
            if (isHomogenous) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of `s`. This is because for each character in `s`, we generate all possible substrings (which takes $O(n^2)$) and then check each substring for homogeneity (which takes $O(n)$ in the worst case).
> - **Space Complexity:** $O(n)$, as we need to store the substrings.
> - **Why these complexities occur:** The brute force approach involves nested loops to generate substrings and then another loop to check for homogeneity, leading to high time complexity. The space complexity is due to storing the substrings.

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of generating all substrings and then checking for homogeneity, we can use a sliding window approach to directly count homogenous substrings.
- Detailed breakdown:
  1. Initialize two pointers, `left` and `right`, to the start of `s`.
  2. Move `right` to the right until we find a character that is different from the character at `left`.
  3. For each position of `right`, calculate the number of homogenous substrings ending at that position by using the formula for the sum of an arithmetic series.
  4. Move `left` to the right of the last homogenous character and repeat.
- This approach is optimal because it only requires a single pass through `s`, significantly reducing the time complexity.

```cpp
int countHomogenousSubstrings(string s) {
    int count = 0;
    for (int left = 0; left < s.size(); left++) {
        char c = s[left];
        for (int right = left; right < s.size(); right++) {
            if (s[right] != c) break;
            // For each position of right, calculate the number of homogenous substrings
            // Since we are counting substrings ending at right, the length of the substring
            // can vary from 1 to (right - left + 1), which is the length of the current window
            count += right - left + 1;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of `s`. This is because in the worst case, for each character, we might need to iterate through the rest of the string.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store our pointers and the count.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to count all homogenous substrings. By directly calculating the count for each window of homogenous characters, we avoid unnecessary iterations.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window technique, direct calculation of substring counts.
- Problem-solving patterns identified: Reducing time complexity by avoiding unnecessary iterations.
- Optimization techniques learned: Using arithmetic series formula to calculate counts directly.
- Similar problems to practice: Other substring counting problems, such as counting substrings with certain properties.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating the count of homogenous substrings, forgetting to handle edge cases.
- Edge cases to watch for: Empty strings, strings with a single character repeated throughout.
- Performance pitfalls: Using brute force approaches for large inputs.
- Testing considerations: Ensure to test with a variety of inputs, including edge cases and large strings.