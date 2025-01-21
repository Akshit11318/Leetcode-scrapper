## Detect Capital
**Problem Link:** [https://leetcode.com/problems/detect-capital/description](https://leetcode.com/problems/detect-capital/description)

**Problem Statement:**
- Input format and constraints: Given a string `word`, return `true` if the usage of capitals in it is right, otherwise return `false`. The usage is considered right if all letters are capitalized (like "USA"), all letters are not capitalized (like "usa"), or only the first letter is capitalized (like "Usa").
- Expected output format: A boolean value indicating whether the capital usage is correct.
- Key requirements and edge cases to consider: 
  - The input string `word` will only contain English letters.
  - The input string `word` will have at least one character.
- Example test cases with explanations:
  - Input: `word = "USA"` Output: `true` Explanation: All letters are capitalized.
  - Input: `word = "usa"` Output: `true` Explanation: All letters are not capitalized.
  - Input: `word = "Usa"` Output: `true` Explanation: Only the first letter is capitalized.
  - Input: `word = "uSa"` Output: `false` Explanation: Only the first letter and some other letters are capitalized.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To determine if the capital usage in a string is correct, we can check each character individually to see if it matches one of the three valid capitalization patterns: all uppercase, all lowercase, or only the first character uppercase.
- Step-by-step breakdown of the solution:
  1. Initialize counters for uppercase and lowercase letters.
  2. Iterate through the string, checking each character.
  3. If the character is uppercase, increment the uppercase counter. If it's lowercase, increment the lowercase counter.
  4. After iterating through the entire string, check the counters against the three valid capitalization patterns.
- Why this approach comes to mind first: It's straightforward and directly addresses the conditions for correct capital usage.

```cpp
class Solution {
public:
    bool detectCapitalUse(string word) {
        int upper = 0, lower = 0;
        for (char c : word) {
            if (isupper(c)) upper++;
            else lower++;
        }
        return (upper == 0 || lower == 0 || (upper == 1 && isupper(word[0])));
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `word`, because we iterate through the string once.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store the counters, regardless of the input size.
> - **Why these complexities occur:** The iteration through the string to count uppercase and lowercase letters directly influences the time complexity, while the use of a fixed number of variables for counters determines the space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of counting all uppercase and lowercase letters, we can stop as soon as we find a pattern that violates the conditions for correct capital usage. This can potentially reduce the number of iterations.
- Detailed breakdown of the approach:
  1. Check if the first character is uppercase.
  2. If it is, then check the rest of the string to see if all characters are uppercase or if the rest are lowercase.
  3. If the first character is lowercase, then check the rest of the string to ensure all characters are lowercase.
- Proof of optimality: This approach is optimal because it only requires a single pass through the string in the worst case, which matches the lower bound for this problem since we must at least read the input once.

```cpp
class Solution {
public:
    bool detectCapitalUse(string word) {
        int n = word.size();
        int capitals = 0;
        for (char c : word) {
            if (isupper(c)) capitals++;
        }
        return capitals == 0 || capitals == n || (capitals == 1 && isupper(word[0]));
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `word`, because in the worst case, we still have to check every character.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space.
> - **Optimality proof:** This is the best time complexity achievable because we must examine each character at least once to determine if the capitalization is correct.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional checks, and the importance of understanding the problem constraints.
- Problem-solving patterns identified: Checking for specific patterns in strings and optimizing the solution based on the constraints of the problem.
- Optimization techniques learned: Reducing unnecessary iterations and using conditional checks to minimize the number of operations.
- Similar problems to practice: Other string manipulation problems that involve checking for specific patterns or conditions.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases (like an empty string), not validating inputs, and not considering all possible conditions for correct capital usage.
- Edge cases to watch for: Strings with only one character, strings with all uppercase or all lowercase letters, and strings where only the first letter is uppercase.
- Performance pitfalls: Unnecessary iterations or operations that can be avoided with a more efficient algorithm.
- Testing considerations: Ensure to test with a variety of inputs, including edge cases, to ensure the solution is robust.