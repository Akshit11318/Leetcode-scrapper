## Cells in a Range on an Excel Sheet
**Problem Link:** https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/description

**Problem Statement:**
- Input format: Two strings `s` and `t` representing the start and end of the range, respectively.
- Constraints: `s` and `t` are non-empty and contain only uppercase letters and digits.
- Expected output format: A list of strings representing the cells in the range.
- Key requirements: The range is inclusive, and the order of the cells is from top to bottom and left to right.
- Edge cases: The start and end cells may be the same, or the start cell may be to the right of or below the end cell.

Example test cases:
- `s = "K1", t = "K2"`: The output should be `["K1", "K2"]`.
- `s = "A1", t = "B2"`: The output should be `["A1", "A2", "B1", "B2"]`.
- `s = "Z1", t = "Z1"`: The output should be `["Z1"]`.

---

### Brute Force Approach
**Explanation:**
- The brute force approach involves iterating over all possible cells in the range and checking if they are within the start and end cells.
- This approach comes to mind first because it is straightforward and easy to implement.
- However, it is inefficient because it has to check every cell, resulting in a high time complexity.

```cpp
vector<string> cellsInRange(string s, string t) {
    vector<string> result;
    int startRow = s[1] - '1';
    int startCol = s[0] - 'A';
    int endRow = t[1] - '1';
    int endCol = t[0] - 'A';
    
    for (int row = startRow; row <= endRow; row++) {
        for (int col = startCol; col <= endCol; col++) {
            string cell = "";
            cell += (char)('A' + col);
            cell += (char)('1' + row);
            result.push_back(cell);
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O((endRow - startRow + 1) * (endCol - startCol + 1))$ because we are iterating over every cell in the range.
> - **Space Complexity:** $O((endRow - startRow + 1) * (endCol - startCol + 1))$ because we are storing every cell in the result vector.
> - **Why these complexities occur:** The time complexity is high because we are checking every cell, and the space complexity is high because we are storing every cell.

---

### Optimal Approach (Required)
**Explanation:**
- The optimal approach involves using two nested loops to generate the cells in the range.
- The outer loop iterates over the rows, and the inner loop iterates over the columns.
- This approach is optimal because it only generates the cells that are within the range, resulting in a lower time complexity.

```cpp
vector<string> cellsInRange(string s, string t) {
    vector<string> result;
    int startRow = s[1] - '1';
    int startCol = s[0] - 'A';
    int endRow = t[1] - '1';
    int endCol = t[0] - 'A';
    
    for (int row = startRow; row <= endRow; row++) {
        for (int col = startCol; col <= endCol; col++) {
            string cell = "";
            cell += (char)('A' + col);
            cell += (char)('1' + row);
            result.push_back(cell);
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O((endRow - startRow + 1) * (endCol - startCol + 1))$ because we are generating every cell in the range.
> - **Space Complexity:** $O((endRow - startRow + 1) * (endCol - startCol + 1))$ because we are storing every cell in the result vector.
> - **Optimality proof:** This is the optimal approach because we are only generating the cells that are within the range, and we are not checking any cells that are outside the range.

---

### Final Notes

**Learning Points:**
- The importance of understanding the problem constraints and requirements.
- The use of nested loops to generate the cells in the range.
- The importance of optimizing the solution to reduce the time and space complexities.

**Mistakes to Avoid:**
- Not checking the input strings for validity.
- Not handling the edge cases correctly.
- Not optimizing the solution to reduce the time and space complexities.
- Not using the correct data structures to store the result.