## Number of Adjacent Elements with the Same Color
**Problem Link:** https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/description

**Problem Statement:**
- Input format and constraints: The input is a string `colors` consisting of lowercase English letters, representing different colors.
- Expected output format: The function should return the number of adjacent elements with the same color.
- Key requirements and edge cases to consider: The input string may be empty, or it may contain only one character. The function should handle these cases correctly.
- Example test cases with explanations:
  - Input: `colors = "aaabba"` Output: `4`
  - Input: `colors = "abcabc"` Output: `0`
  - Input: `colors = "aaaaaa"` Output: `5`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can iterate through the string and compare each character with its adjacent character.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `count` to store the number of adjacent elements with the same color.
  2. Iterate through the string `colors` using a for loop.
  3. For each character, compare it with its adjacent character (if it exists).
  4. If the characters are the same, increment the `count` variable.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, as it directly checks each pair of adjacent characters.

```cpp
int numberOfBeams(string colors) {
    int count = 0;
    for (int i = 0; i < colors.length() - 1; i++) {
        if (colors[i] == colors[i + 1]) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `colors`. This is because we iterate through the string once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the `count` variable.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each character in the string. The space complexity is constant because we do not use any data structures that grow with the size of the input.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a simple loop to iterate through the string and compare each character with its adjacent character.
- Detailed breakdown of the approach:
  1. Initialize a variable `count` to store the number of adjacent elements with the same color.
  2. Iterate through the string `colors` using a for loop.
  3. For each character, compare it with its adjacent character (if it exists).
  4. If the characters are the same, increment the `count` variable.
- Proof of optimality: This approach is optimal because it only requires a single pass through the string, resulting in a time complexity of $O(n)$.
- Why further optimization is impossible: This is because we must examine each character at least once to determine if it has the same color as its adjacent character.

```cpp
int numberOfBeams(string colors) {
    int count = 0;
    for (int i = 0; i < colors.length() - 1; i++) {
        if (colors[i] == colors[i + 1]) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `colors`. This is because we iterate through the string once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the `count` variable.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the string, resulting in a time complexity of $O(n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Simple iteration and comparison.
- Problem-solving patterns identified: Using a single loop to iterate through a string.
- Optimization techniques learned: Reducing the number of iterations to achieve optimal time complexity.
- Similar problems to practice: Other string manipulation problems, such as finding the longest common prefix or suffix.

**Mistakes to Avoid:**
- Common implementation errors: Off-by-one errors when iterating through the string.
- Edge cases to watch for: Empty strings or strings with only one character.
- Performance pitfalls: Using unnecessary data structures or algorithms that result in higher time complexity.
- Testing considerations: Test the function with different input strings, including edge cases.