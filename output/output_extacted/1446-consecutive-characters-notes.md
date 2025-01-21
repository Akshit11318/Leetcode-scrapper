## Consecutive Characters

**Problem Link:** https://leetcode.com/problems/consecutive-characters/description

**Problem Statement:**
- Input format and constraints: The input is a string `s` containing only lowercase English letters.
- Expected output format: The maximum number of consecutive repeating characters in the string.
- Key requirements and edge cases to consider: The input string may be empty, and we need to handle this case. We also need to consider strings with only one character.
- Example test cases with explanations:
  - Input: `s = "leetcode"`
    - Output: `2`
    - Explanation: The longest consecutive repeating character is `e`, which repeats twice.
  - Input: `s = "abbbbb"`
    - Output: `4`
    - Explanation: The longest consecutive repeating character is `b`, which repeats four times.
  - Input: `s = "aabbcc"`
    - Output: `2`
    - Explanation: The longest consecutive repeating characters are `a`, `b`, and `c`, each repeating twice.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can iterate through the string and count the consecutive occurrences of each character.
- Step-by-step breakdown of the solution:
  1. Initialize a variable to store the maximum count of consecutive characters.
  2. Iterate through the string, and for each character, count the number of consecutive occurrences.
  3. Update the maximum count if the current count is higher.
- Why this approach comes to mind first: This approach is straightforward and easy to understand.

```cpp
int maxConsecutiveChars(string s) {
    int maxCount = 0;
    int currentCount = 1;

    for (int i = 1; i <= s.size(); i++) {
        if (i == s.size() || s[i] != s[i - 1]) {
            maxCount = max(maxCount, currentCount);
            currentCount = 1;
        } else {
            currentCount++;
        }
    }

    return maxCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string, because we are iterating through the string once.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the maximum count and the current count.
> - **Why these complexities occur:** The time complexity is linear because we are scanning the string once, and the space complexity is constant because we are using a fixed amount of space to store the counts.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal for this problem, as we need to scan the string at least once to count the consecutive characters.
- Detailed breakdown of the approach: The optimal approach is the same as the brute force approach, as it has a linear time complexity and constant space complexity.
- Proof of optimality: The optimal approach is optimal because it has a linear time complexity, which is the best we can achieve for this problem.
- Why further optimization is impossible: Further optimization is impossible because we need to scan the string at least once to count the consecutive characters.

```cpp
int maxConsecutiveChars(string s) {
    int maxCount = 0;
    int currentCount = 1;

    for (int i = 1; i <= s.size(); i++) {
        if (i == s.size() || s[i] != s[i - 1]) {
            maxCount = max(maxCount, currentCount);
            currentCount = 1;
        } else {
            currentCount++;
        }
    }

    return maxCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string, because we are iterating through the string once.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the maximum count and the current count.
> - **Optimality proof:** The optimal approach is optimal because it has a linear time complexity, which is the best we can achieve for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the concept of scanning a string and counting consecutive characters.
- Problem-solving patterns identified: The problem requires a simple iterative approach to solve.
- Optimization techniques learned: The problem does not require any optimization techniques beyond the brute force approach.
- Similar problems to practice: Other problems that involve scanning a string and counting characters, such as counting the frequency of each character.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the edge case where the input string is empty.
- Edge cases to watch for: The input string may be empty, and we need to handle this case.
- Performance pitfalls: Not using a constant amount of space to store the counts.
- Testing considerations: We should test the function with different input strings, including empty strings and strings with only one character.