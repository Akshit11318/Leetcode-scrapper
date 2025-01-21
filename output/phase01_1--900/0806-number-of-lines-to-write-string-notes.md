## Number of Lines to Write String

**Problem Link:** https://leetcode.com/problems/number-of-lines-to-write-string/description

**Problem Statement:**
- Input: An array of strings `widths` and a string `s`.
- Constraints: The length of `widths` is 26, and each element is a positive integer. `s` consists of lowercase English letters.
- Expected output: An array of two integers representing the number of lines and the width of the last line.
- Key requirements: Calculate the number of lines and the width of the last line when writing the string `s` with the given character widths.
- Example test cases:
  - Input: `widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]`, `s = "abcdefghijklmnopqrstuvwxyz"`
  - Output: `[3, 60]`
  - Explanation: The string `s` can be written in 3 lines with the last line having a width of 60.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each character in the string `s`, calculate its width using the `widths` array, and update the line count and last line width accordingly.
- Step-by-step breakdown:
  1. Initialize variables to store the line count and the last line width.
  2. Iterate over each character in the string `s`.
  3. For each character, calculate its width using the `widths` array.
  4. If adding the current character to the current line would exceed 100, start a new line.
  5. Update the last line width and line count as necessary.
- Why this approach comes to mind first: It directly addresses the problem statement by iterating over the input string and calculating the required metrics.

```cpp
vector<int> numberOfLines(vector<int>& widths, string s) {
    int lines = 1;
    int lastLineWidth = 0;
    for (char c : s) {
        int charWidth = widths[c - 'a'];
        if (lastLineWidth + charWidth > 100) {
            lines++;
            lastLineWidth = 0;
        }
        lastLineWidth += charWidth;
    }
    return {lines, lastLineWidth};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`, because we iterate over each character in the string once.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store the line count and last line width, regardless of the input size.
> - **Why these complexities occur:** The time complexity is linear because we process each character in the string once. The space complexity is constant because we only use a fixed amount of space to store the necessary variables.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved in a single pass through the string `s`, as demonstrated in the brute force approach. No further optimization is necessary.
- Detailed breakdown of the approach: The same as the brute force approach, as it is already optimal.
- Proof of optimality: The solution has a time complexity of $O(n)$, which is the best possible time complexity because we must at least read the input string once. The space complexity is $O(1)$, which is also optimal because we only use a constant amount of space.
- Why further optimization is impossible: We must process each character in the string at least once to calculate the required metrics, so the time complexity cannot be improved. We also only use a constant amount of space, so the space complexity is already optimal.

```cpp
vector<int> numberOfLines(vector<int>& widths, string s) {
    int lines = 1;
    int lastLineWidth = 0;
    for (char c : s) {
        int charWidth = widths[c - 'a'];
        if (lastLineWidth + charWidth > 100) {
            lines++;
            lastLineWidth = 0;
        }
        lastLineWidth += charWidth;
    }
    return {lines, lastLineWidth};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store the line count and last line width.
> - **Optimality proof:** The solution has the best possible time and space complexities because it must at least read the input string once and only uses a constant amount of space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Single-pass processing, constant space usage.
- Problem-solving patterns identified: Iterating over input data to calculate metrics.
- Optimization techniques learned: Recognizing when a brute force approach is already optimal.
- Similar problems to practice: Other string processing problems, such as calculating the length of the longest substring without repeating characters.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle edge cases, such as an empty input string.
- Edge cases to watch for: Empty input string, string with a single character.
- Performance pitfalls: Using unnecessary data structures or algorithms that increase the time or space complexity.
- Testing considerations: Test the solution with different input strings, including edge cases, to ensure correctness.