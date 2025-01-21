## Valid Word Square

**Problem Link:** https://leetcode.com/problems/valid-word-square/description

**Problem Statement:**
- Input: A list of `strings` representing words.
- Constraints: The input is a square (i.e., the number of rows equals the number of columns), and each word is the same length as the number of rows.
- Expected Output: A boolean indicating whether the input forms a valid word square. A word square is valid if the `i-th` row and the `i-th` column form the same word.
- Key Requirements:
  - The input list of strings represents a square matrix.
  - The length of each string must be equal to the number of strings.
- Edge Cases:
  - An empty input list.
  - A list containing a single string.
  - A list where the length of the strings does not match the number of strings.
- Example Test Cases:
  - `["abcd","bnrt","crmy","dtye"]` returns `true` because the first row and first column form "abcd", the second row and second column form "bnrt", and so on.
  - `["abcd","bnrt","crm","dtye"]` returns `false` because the third row and third column do not form the same word.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking each row against its corresponding column to see if they form the same word.
- This approach comes to mind first because it directly addresses the problem statement's requirement for a valid word square.
- Step-by-step breakdown:
  1. Iterate over each row in the input list.
  2. For each row, iterate over each character in the row.
  3. Compare the character at the current position in the row with the character at the same position in the corresponding column.
  4. If any pair of characters does not match, return `false`.
  5. If the loop completes without finding any mismatches, return `true`.

```cpp
bool validWordSquare(vector<string>& words) {
    int n = words.size();
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (j >= words[i].size() || i >= words[j].size() || words[i][j] != words[j][i]) {
                return false;
            }
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of strings. This is because we are iterating over each character in the square once.
> - **Space Complexity:** $O(1)$, not including the space required for the input. This is because we are using a constant amount of space to store our variables.
> - **Why these complexities occur:** The time complexity is $O(n^2)$ because we are performing a nested loop over the input, which has $n$ rows and $n$ columns. The space complexity is $O(1)$ because we are not using any data structures that scale with the size of the input.

---

### Optimal Approach (Required)

The brute force approach provided is already optimal for this problem because it directly checks the condition for a valid word square without any unnecessary operations. It iterates over each character in the input once, which is the minimum required to verify if the input forms a valid word square.

Therefore, the **Optimal Approach** is the same as the **Brute Force Approach** in this case.

```cpp
bool validWordSquare(vector<string>& words) {
    int n = words.size();
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (j >= words[i].size() || i >= words[j].size() || words[i][j] != words[j][i]) {
                return false;
            }
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of strings.
> - **Space Complexity:** $O(1)$, not including the space required for the input.
> - **Optimality proof:** This is optimal because we must at least read the input once to verify if it forms a valid word square, and the algorithm does so in a single pass.

---

### Final Notes

**Learning Points:**
- The importance of directly addressing the problem statement's requirements.
- How to analyze the time and space complexity of an algorithm.
- Understanding that sometimes, the brute force approach can be optimal if it directly solves the problem without unnecessary overhead.

**Mistakes to Avoid:**
- Not checking for edge cases such as an empty input or input with mismatched string lengths.
- Not validating the input before processing it.
- Overcomplicating the solution by introducing unnecessary steps or data structures.