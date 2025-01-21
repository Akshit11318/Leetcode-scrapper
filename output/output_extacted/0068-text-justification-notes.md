## Text Justification
**Problem Link:** [https://leetcode.com/problems/text-justification/description](https://leetcode.com/problems/text-justification/description)

**Problem Statement:**
- Input format and constraints: The input is a list of words and a maximum width for the justified text. The list of words can contain any number of words, and the maximum width is a positive integer.
- Expected output format: The output is a list of strings, where each string represents a line of the justified text.
- Key requirements and edge cases to consider: The text should be justified to the maximum width, and the last line should be left-justified.
- Example test cases with explanations:
  - Example 1:
    - Input: `words = ["This", "is", "an", "example", "of", "text", "justification."]`, `maxWidth = 16`
    - Output: `["This    is    an", "example  of text", "justification.  "]`
  - Example 2:
    - Input: `words = ["What","must","be","acknowledgment","shall","be"]`, `maxWidth = 20`
    - Output: `["What   must   be", "acknowledgment  ", "shall be        "]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over each word and checking if adding it to the current line would exceed the maximum width.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list to store the justified lines.
  2. Initialize an empty string to store the current line.
  3. Iterate over each word in the list of words.
  4. For each word, check if adding it to the current line would exceed the maximum width.
  5. If it would exceed the maximum width, add the current line to the list of justified lines and reset the current line.
  6. Add the word to the current line and add spaces as needed to justify the line.
  7. After iterating over all words, add the last line to the list of justified lines.
- Why this approach comes to mind first: This approach is straightforward and involves checking each word individually, which is a common technique in string manipulation problems.

```cpp
vector<string> fullJustify(vector<string>& words, int maxWidth) {
    vector<string> result;
    string currentLine;
    for (string word : words) {
        if (currentLine.size() + word.size() + 1 > maxWidth) {
            // Justify the current line
            int spaces = maxWidth - currentLine.size();
            int gaps = count(currentLine.begin(), currentLine.end(), ' ') + 1;
            int spacePerGap = spaces / gaps;
            int extraSpaces = spaces % gaps;
            string justifiedLine;
            istringstream iss(currentLine);
            string token;
            while (iss >> token) {
                justifiedLine += token;
                if (justifiedLine.size() < maxWidth) {
                    justifiedLine += string(spacePerGap, ' ');
                    if (extraSpaces > 0) {
                        justifiedLine += ' ';
                        extraSpaces--;
                    }
                }
            }
            result.push_back(justifiedLine);
            currentLine = word;
        } else {
            if (!currentLine.empty()) {
                currentLine += ' ';
            }
            currentLine += word;
        }
    }
    // Handle the last line
    if (!currentLine.empty()) {
        currentLine += string(maxWidth - currentLine.size(), ' ');
        result.push_back(currentLine);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of words and $m$ is the maximum width. This is because we iterate over each word and perform string operations to justify the line.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of words and $m$ is the maximum width. This is because we store the justified lines in a vector.
> - **Why these complexities occur:** These complexities occur because we perform string operations and store the justified lines in a vector, which requires memory proportional to the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a two-pointer technique to track the start and end of each line.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `start` and `end`, to the beginning of the list of words.
  2. Iterate over the list of words, and for each word, check if adding it to the current line would exceed the maximum width.
  3. If it would exceed the maximum width, justify the current line and add it to the result.
  4. Update the `start` pointer to the next word.
  5. After iterating over all words, justify the last line and add it to the result.
- Proof of optimality: This approach is optimal because it only requires a single pass over the list of words and uses a constant amount of extra memory to store the justified lines.

```cpp
vector<string> fullJustify(vector<string>& words, int maxWidth) {
    vector<string> result;
    int start = 0;
    for (int end = 0; end < words.size(); end++) {
        int width = 0;
        for (int i = start; i <= end; i++) {
            width += words[i].size() + 1;
        }
        if (width - 1 > maxWidth) {
            // Justify the current line
            int spaces = maxWidth;
            for (int i = start; i < end; i++) {
                spaces -= words[i].size();
            }
            int gaps = end - start;
            int spacePerGap = gaps > 1 ? spaces / (gaps - 1) : spaces;
            int extraSpaces = gaps > 1 ? spaces % (gaps - 1) : 0;
            string justifiedLine;
            for (int i = start; i < end; i++) {
                justifiedLine += words[i];
                if (i < end - 1) {
                    justifiedLine += string(spacePerGap, ' ');
                    if (i - start < extraSpaces) {
                        justifiedLine += ' ';
                    }
                }
            }
            result.push_back(justifiedLine);
            start = end;
        }
    }
    // Handle the last line
    string lastLine;
    for (int i = start; i < words.size(); i++) {
        lastLine += words[i] + (i < words.size() - 1 ? " " : "");
    }
    lastLine += string(maxWidth - lastLine.size(), ' ');
    result.push_back(lastLine);
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of words and $m$ is the maximum width. This is because we iterate over each word and perform string operations to justify the line.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of words and $m$ is the maximum width. This is because we store the justified lines in a vector.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the list of words and uses a constant amount of extra memory to store the justified lines.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two-pointer technique, string manipulation, and dynamic programming.
- Problem-solving patterns identified: The problem involves iterating over a list of words and performing string operations to justify the lines.
- Optimization techniques learned: The optimal approach uses a two-pointer technique to track the start and end of each line, reducing the time complexity.
- Similar problems to practice: Other string manipulation problems, such as text wrapping and formatting.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty list of words or a maximum width of 0.
- Edge cases to watch for: The last line should be left-justified, and the maximum width should be checked for each line.
- Performance pitfalls: Using excessive string operations or nested loops can increase the time complexity.
- Testing considerations: Test the implementation with different input sizes and edge cases to ensure correctness and performance.