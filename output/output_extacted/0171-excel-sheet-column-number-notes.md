## Excel Sheet Column Number

**Problem Link:** [https://leetcode.com/problems/excel-sheet-column-number/description](https://leetcode.com/problems/excel-sheet-column-number/description)

**Problem Statement:**
- Input format and constraints: The input will be a string `s` consisting of uppercase letters representing a column title in an Excel sheet.
- Expected output format: The output should be an integer representing the column number corresponding to the input column title.
- Key requirements and edge cases to consider: The input string `s` will only contain uppercase letters, and the length of `s` will be between 1 and 100.
- Example test cases with explanations:
  - Input: `s = "A"`; Output: `1` (since A is the first column in Excel)
  - Input: `s = "AB"`; Output: `28` (since AB corresponds to the 28th column in Excel)
  - Input: `s = "ZY"`; Output: `701` (since ZY corresponds to the 701st column in Excel)

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One might start by trying to manually map each possible column title to its corresponding number, but this approach quickly becomes impractical due to the large number of possible titles.
- Step-by-step breakdown of the solution: 
  1. Create a dictionary or map to store the column titles and their corresponding numbers.
  2. Iterate through all possible column titles (from A to ZZZ...), calculating the column number for each title.
  3. Store each title and its corresponding number in the dictionary.
  4. Once the dictionary is populated, use it to look up the column number for the input title.
- Why this approach comes to mind first: It seems straightforward to manually enumerate all possibilities and store them for lookup, but this approach is not efficient for large inputs.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

int titleToNumber(std::string s) {
    std::unordered_map<std::string, int> map;
    int count = 1;
    for (int i = 1; i <= 26; i++) {
        std::string title(1, 'A' + i - 1);
        map[title] = count++;
    }
    for (int i = 1; i <= 26; i++) {
        for (int j = 1; j <= 26; j++) {
            std::string title(2, 'A' + i - 1);
            title[1] = 'A' + j - 1;
            map[title] = count++;
        }
    }
    // Continue this pattern for longer titles...
    return map[s];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(26^n)$ where $n$ is the length of the input string, because we're generating all possible titles up to a certain length.
> - **Space Complexity:** $O(26^n)$ because we're storing all generated titles in the dictionary.
> - **Why these complexities occur:** The brute force approach involves generating all possible column titles and storing them, which leads to exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Recognize that Excel column titles are essentially base-26 numbers, where 'A' represents 1, 'B' represents 2, and so on up to 'Z' representing 26.
- Detailed breakdown of the approach: 
  1. Initialize a variable `result` to 0.
  2. Iterate through the input string `s` from left to right.
  3. For each character `c` in `s`, calculate its corresponding number (where 'A' = 1, 'B' = 2, ..., 'Z' = 26).
  4. Update `result` by multiplying the current `result` by 26 (since we're moving to the next position in the base-26 number) and adding the number corresponding to `c`.
- Proof of optimality: This approach directly calculates the column number without unnecessary intermediate steps or storage, making it efficient for inputs of any length.

```cpp
int titleToNumber(std::string s) {
    int result = 0;
    for (char c : s) {
        result *= 26;
        result += c - 'A' + 1; // Convert character to corresponding number
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the input string, because we iterate through the string once.
> - **Space Complexity:** $O(1)$ because we use a constant amount of space to store the result and temporary calculations.
> - **Optimality proof:** This solution has linear time complexity and constant space complexity, making it optimal for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Base conversion (specifically, converting from a base-26 representation to decimal).
- Problem-solving patterns identified: Recognizing that certain string representations can be treated as numbers in a different base.
- Optimization techniques learned: Avoiding unnecessary storage and calculations by directly computing the result.
- Similar problems to practice: Other problems involving base conversion or string representations of numbers.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling the conversion from character to number (e.g., forgetting to subtract 'A' to get the correct offset).
- Edge cases to watch for: Inputs with length 1 (single character), and ensuring the calculation correctly handles the base-26 to decimal conversion.
- Performance pitfalls: Using inefficient data structures or algorithms that scale poorly with input size.
- Testing considerations: Thoroughly testing the function with various inputs, including edge cases like single characters and longer strings.