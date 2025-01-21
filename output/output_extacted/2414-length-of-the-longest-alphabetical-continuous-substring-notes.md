## Length of the Longest Alphabetical Continuous Substring

**Problem Link:** https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/description

**Problem Statement:**
- Input: A string `s` consisting of lowercase English letters.
- Expected Output: The length of the longest substring where the letters are in alphabetical order.
- Key Requirements:
  - The substring must be continuous.
  - Letters must be in alphabetical order.
- Edge Cases:
  - Empty string.
  - Single-character string.
  - String with all characters in alphabetical order.

**Example Test Cases:**
- Input: `s = "abcde"`; Output: `5` because the entire string is in alphabetical order.
- Input: `s = "zabcd"`; Output: `4` because the substring "abcd" is the longest in alphabetical order.
- Input: `s = "vbnm"`; Output: `1` because each character is not in alphabetical order with its neighbors.

---

### Brute Force Approach

**Explanation:**
- This approach involves checking every possible substring of the input string `s`.
- For each substring, we verify if the characters are in alphabetical order.
- We keep track of the maximum length of the substring that meets the condition.

```cpp
int longestAlphabeticalSubstring(string s) {
    int maxLength = 0;
    for (int i = 0; i < s.size(); i++) {
        for (int j = i + 1; j <= s.size(); j++) {
            string substr = s.substr(i, j - i);
            bool isAlphabetical = true;
            for (int k = 0; k < substr.size() - 1; k++) {
                if (substr[k] > substr[k + 1]) {
                    isAlphabetical = false;
                    break;
                }
            }
            if (isAlphabetical && substr.size() > maxLength) {
                maxLength = substr.size();
            }
        }
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ where $n$ is the length of the string. This is because we have three nested loops: one for the start of the substring, one for the end of the substring, and one to check if the substring is alphabetical.
> - **Space Complexity:** $O(n)$ because in the worst case, we might need to create a substring that is as long as the original string.
> - **Why these complexities occur:** The brute force approach checks every possible substring and verifies each one, leading to high time complexity. The space complexity is due to the creation of substrings.

---

### Optimal Approach (Required)

**Explanation:**
- We can improve the solution by using a single pass through the string, keeping track of the current alphabetical substring length.
- Whenever we encounter a character that is not in alphabetical order with the previous one, we reset the current length.
- We keep track of the maximum length seen so far.

```cpp
int longestAlphabeticalSubstring(string s) {
    if (s.empty()) return 0;
    
    int maxLength = 1;
    int currentLength = 1;
    
    for (int i = 1; i < s.size(); i++) {
        if (s[i] >= s[i - 1]) {
            currentLength++;
        } else {
            currentLength = 1;
        }
        maxLength = max(maxLength, currentLength);
    }
    
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the string. This is because we make a single pass through the string.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store the maximum length and the current length.
> - **Optimality proof:** This approach is optimal because it checks each character in the string exactly once, which is necessary to determine the longest alphabetical substring. By keeping track of the current and maximum lengths, we avoid unnecessary comparisons and substring creations.

---

### Final Notes

**Learning Points:**
- The importance of understanding the problem constraints and requirements.
- How to approach problems with a brute force solution first and then optimize.
- The use of single-pass algorithms to improve time complexity.
- The importance of space complexity, especially when dealing with large inputs.

**Mistakes to Avoid:**
- Not considering edge cases, such as an empty string.
- Not optimizing the algorithm, leading to high time complexity.
- Not validating the inputs and outputs properly.
- Not considering alternative solutions that might offer better trade-offs.

By following this approach, we can efficiently solve the problem and understand the underlying algorithmic concepts and optimization techniques.