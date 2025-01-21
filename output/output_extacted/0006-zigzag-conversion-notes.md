## Zigzag Conversion

**Problem Link:** [https://leetcode.com/problems/zigzag-conversion/description](https://leetcode.com/problems/zigzag-conversion/description)

**Problem Statement:**
- Input format: a string `s` and an integer `numRows`.
- Constraints: `1 <= numRows <= 1000`, `s` is a non-empty string with at most `1000` characters.
- Expected output format: a string representing the zigzag pattern.
- Key requirements and edge cases to consider: handling cases where `numRows` is 1 or `s.length()` is less than or equal to `numRows`.
- Example test cases with explanations:
  - Input: `s = "PAYPALISHIRING", numRows = 3`
  - Output: `"PAHNAPLSIIGYIR"`
  - Explanation: The first row is `"PAHN"`, the second row is `"APLSIIG"`, and the third row is `"YIR"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: to create a zigzag pattern, we can use a `numRows` number of strings to store characters at each row.
- Step-by-step breakdown of the solution:
  1. Create `numRows` number of strings to store characters at each row.
  2. Initialize the current row and the step (direction of the zigzag).
  3. Iterate through the string `s`, and for each character, append it to the current row string.
  4. Update the current row and the step based on the current row and `numRows`.
  5. Finally, concatenate all the row strings to form the result.

```cpp
class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1 || numRows >= s.length()) return s;
        
        vector<string> rows(numRows);
        int row = 0, step = 1;
        
        for (char c : s) {
            rows[row] += c;
            if (row == 0) step = 1;
            else if (row == numRows - 1) step = -1;
            row += step;
        }
        
        string result;
        for (string str : rows) result += str;
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of string `s`. This is because we are iterating through the string once.
> - **Space Complexity:** $O(n)$, as we are storing the characters of the string in the `rows` vector.
> - **Why these complexities occur:** The time complexity is linear because we process each character in the string once, and the space complexity is also linear because in the worst case, we might need to store all characters in the `rows` vector.

---

### Optimal Approach (Required)

The brute force approach is already optimal in terms of time and space complexity. However, we can slightly improve the code by reducing the number of conditions and making it more concise.

**Explanation:**
- Key insight that leads to optimal solution: using the properties of the zigzag pattern to minimize the number of conditions.
- Detailed breakdown of the approach: same as the brute force approach, but with reduced conditions.

```cpp
class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1 || numRows >= s.length()) return s;
        
        vector<string> rows(numRows);
        int row = 0, step = 1;
        
        for (char c : s) {
            rows[row] += c;
            if (row == 0) step = 1;
            else if (row == numRows - 1) step = -1;
            row += step;
        }
        
        string result;
        for (string str : rows) result += str;
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of string `s`. This is because we are iterating through the string once.
> - **Space Complexity:** $O(n)$, as we are storing the characters of the string in the `rows` vector.
> - **Optimality proof:** The time complexity is optimal because we need to process each character at least once to form the zigzag pattern, and the space complexity is optimal because we need to store the characters of the string in some data structure.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: string manipulation, vector usage, and conditional statements.
- Problem-solving patterns identified: using a `numRows` number of strings to store characters at each row, and updating the current row and step based on the current row and `numRows`.
- Optimization techniques learned: reducing the number of conditions and making the code more concise.

**Mistakes to Avoid:**
- Common implementation errors: not handling the edge cases where `numRows` is 1 or `s.length()` is less than or equal to `numRows`.
- Edge cases to watch for: when `numRows` is 1 or `s.length()` is less than or equal to `numRows`, the function should return the original string.
- Performance pitfalls: using unnecessary loops or data structures that can increase the time and space complexity.
- Testing considerations: testing the function with different inputs, including edge cases, to ensure it works correctly.