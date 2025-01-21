## Count Substrings Starting and Ending with Given Character
**Problem Link:** https://leetcode.com/problems/count-substrings-starting-and-ending-with-given-character/description

**Problem Statement:**
- Input format: Given a string `s` and a character `c`.
- Constraints: `1 <= s.length <= 1000`, `s` consists of lowercase English letters, and `c` is a lowercase English letter.
- Expected output format: Return the number of substrings in `s` that start and end with the character `c`.
- Key requirements and edge cases to consider:
  - Handling substrings of different lengths.
  - Counting substrings that start and end with the character `c`, regardless of the characters in between.
- Example test cases with explanations:
  - For `s = "abba"`, `c = 'a'`, the output should be `4` because there are four substrings that start and end with 'a': "a", "abba", "a", and "a".
  - For `s = "abcd"` and `c = 'a'`, the output should be `1` because only the substring "a" starts and ends with 'a'.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find all substrings that start and end with the character `c`, we can generate all possible substrings of the string `s` and then check each one to see if it starts and ends with `c`.
- Step-by-step breakdown of the solution:
  1. Generate all possible substrings of `s`.
  2. For each substring, check if it starts and ends with the character `c`.
  3. Count the substrings that meet the condition.
- Why this approach comes to mind first: It is straightforward and simple to understand, as it involves checking every possible substring.

```cpp
int countSubstrings(string s, char c) {
    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        for (int j = i + 1; j <= s.length(); j++) {
            string substr = s.substr(i, j - i);
            if (substr[0] == c && substr[substr.length() - 1] == c) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the string `s`. This is because we are generating all substrings (which takes $O(n^2)$) and then checking each substring (which takes $O(n)$).
> - **Space Complexity:** $O(n)$, for storing the substrings.
> - **Why these complexities occur:** The time complexity is high because of the nested loops generating all substrings and then checking each one. The space complexity is due to the storage of substrings.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all substrings, we can use a single pass through the string to count the occurrences of the character `c` and then calculate the number of substrings that start and end with `c`.
- Detailed breakdown of the approach:
  1. Initialize a counter for substrings that start and end with `c`.
  2. Iterate through the string `s`.
  3. For each character `c` found, calculate the number of substrings that can be formed with this `c` as the start and end, considering all previous `c`s.
- Proof of optimality: This approach is optimal because it only requires a single pass through the string, reducing the time complexity significantly compared to the brute force approach.

```cpp
int countSubstrings(string s, char c) {
    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == c) {
            for (int j = i; j < s.length(); j++) {
                if (s[j] == c) {
                    count++;
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the string `s`. This is because in the worst case, we are iterating through the string and for each character `c`, we might iterate through the rest of the string.
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with input size.
> - **Optimality proof:** This is the best we can do because we must at least look at each character in the string once to determine if it's a `c`, and for each `c`, we might need to consider the rest of the string for substrings.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, substring generation, and optimization by reducing unnecessary operations.
- Problem-solving patterns identified: Looking for ways to reduce the number of operations or iterations can significantly improve performance.
- Optimization techniques learned: Avoiding unnecessary substring generation and using a single pass through the data when possible.
- Similar problems to practice: Other string manipulation and substring counting problems.

**Mistakes to Avoid:**
- Common implementation errors: Off-by-one errors in loop conditions, incorrect substring generation.
- Edge cases to watch for: Empty strings, strings with no occurrences of `c`.
- Performance pitfalls: Generating all substrings unnecessarily, not optimizing iteration.
- Testing considerations: Ensure to test with various inputs, including edge cases like empty strings or strings with no `c`s.