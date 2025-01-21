## Percentage of Letter in String

**Problem Link:** https://leetcode.com/problems/percentage-of-letter-in-string/description

**Problem Statement:**
- Input format: A string `s` and a character `letter`.
- Constraints: The input string `s` will be non-empty and will only contain lowercase letters.
- Expected output format: The percentage of the character `letter` in the string `s`.
- Key requirements and edge cases to consider: 
  - Handling cases where `letter` does not appear in `s`.
  - Calculating the percentage correctly, considering the total length of the string.
- Example test cases with explanations:
  - Example 1: `s = "foobar", letter = "o"` returns `33.33`.
  - Example 2: `s = "jjjj", letter = "k"` returns `0.00`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Count the occurrences of the `letter` in the string `s`, then divide by the total length of `s` and multiply by 100 to get the percentage.
- Step-by-step breakdown of the solution:
  1. Initialize a counter for the occurrences of `letter`.
  2. Iterate through each character in the string `s`.
  3. If the current character matches `letter`, increment the counter.
  4. After iterating through all characters, calculate the percentage by dividing the counter by the length of `s` and then multiplying by 100.
- Why this approach comes to mind first: It directly addresses the problem by counting the occurrences of the specified letter and then calculating the percentage based on the total length of the string.

```cpp
double percentageLetterInString(string s, char letter) {
    int count = 0;
    for (char c : s) {
        if (c == letter) {
            count++;
        }
    }
    return (static_cast<double>(count) / s.length()) * 100;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the string `s`, because we are iterating through each character in the string once.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the count and the result, regardless of the size of the input string.
> - **Why these complexities occur:** The time complexity is linear because we are scanning the string once, and the space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal for this problem because we must examine each character in the string at least once to count the occurrences of the specified letter.
- Detailed breakdown of the approach: The same as the brute force approach, as it is already optimal.
- Proof of optimality: Since we must look at each character at least once to count the occurrences of the letter, the optimal time complexity is $O(n)$, which is achieved by the brute force approach.
- Why further optimization is impossible: Any algorithm that solves this problem must examine each character in the string at least once, making $O(n)$ the best possible time complexity.

```cpp
double percentageLetterInString(string s, char letter) {
    int count = 0;
    for (char c : s) {
        if (c == letter) {
            count++;
        }
    }
    return (static_cast<double>(count) / s.length()) * 100;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`, because we are iterating through each character in the string once.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the count and the result, regardless of the size of the input string.
> - **Optimality proof:** The time complexity is linear and optimal because we must scan the string once to count the occurrences of the letter, and the space complexity is constant because we are not using any data structures that scale with the input size.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Linear scanning, counting occurrences of a specific character.
- Problem-solving patterns identified: The need to examine each element in a collection at least once to gather specific information.
- Optimization techniques learned: Recognizing when the initial approach is already optimal due to the inherent requirements of the problem.
- Similar problems to practice: Other string manipulation and analysis problems, such as finding the most frequent character or checking for substring presence.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, such as an empty string or a letter that does not appear in the string.
- Edge cases to watch for: Ensuring the calculation handles cases where the letter does not appear (resulting in 0.00%) and when the string is empty (which should be considered an invalid input or handled according to specific problem constraints).
- Performance pitfalls: Attempting to use more complex data structures or algorithms than necessary, which could increase time or space complexity without providing any benefits for this particular problem.
- Testing considerations: Thoroughly testing the function with various inputs, including different letters, strings of varying lengths, and edge cases like empty strings or strings without the specified letter.