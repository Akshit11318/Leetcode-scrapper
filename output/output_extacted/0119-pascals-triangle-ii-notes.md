## Pascal's Triangle II
**Problem Link:** https://leetcode.com/problems/pascals-triangle-ii/description

**Problem Statement:**
- Input format: Given an integer `rowIndex`, return the `rowIndex`-th row of the Pascal's triangle.
- Constraints: `0 <= rowIndex <= 33`
- Expected output format: A list of integers representing the `rowIndex`-th row of the Pascal's triangle.
- Key requirements and edge cases to consider: Handling edge cases where `rowIndex` is 0 or 1, and ensuring the solution scales for larger `rowIndex` values.

Example test cases:
- Input: `rowIndex = 3`
  Output: `[1, 3, 3, 1]`
- Input: `rowIndex = 4`
  Output: `[1, 4, 6, 4, 1]`

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves generating the entire Pascal's triangle up to the `rowIndex` and then returning the last row.
- This approach comes to mind first because it directly follows the definition of Pascal's triangle, where each element is the sum of the two elements directly above it.

```cpp
vector<int> getRow(int rowIndex) {
    vector<vector<int>> triangle;
    for (int i = 0; i <= rowIndex; i++) {
        vector<int> row = {1};
        if (!triangle.empty()) {
            vector<int> lastRow = triangle.back();
            for (int j = 0; j < lastRow.size() - 1; j++) {
                row.push_back(lastRow[j] + lastRow[j + 1]);
            }
            row.push_back(1);
        }
        triangle.push_back(row);
    }
    return triangle.back();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the `rowIndex`. This is because we generate each row of the triangle, and for each row, we perform operations proportional to the row number.
> - **Space Complexity:** $O(n^2)$, as we store the entire triangle up to the `rowIndex`.
> - **Why these complexities occur:** The brute force approach involves generating the entire triangle, which requires both time and space proportional to the square of the `rowIndex`.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to only generate the `rowIndex`-th row of the Pascal's triangle without storing the entire triangle.
- This is achieved by recognizing that each element in the row can be calculated using the formula for combinations, specifically `C(n, k) = n! / [k!(n-k)!]`, where `n` is the `rowIndex` and `k` is the element's position in the row (0-indexed).

```cpp
vector<int> getRow(int rowIndex) {
    vector<int> row(rowIndex + 1, 1);
    for (int i = 1; i < rowIndex; i++) {
        for (int j = i; j > 0; j--) {
            row[j] = row[j] + row[j - 1];
        }
    }
    return row;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the `rowIndex`. Although this seems similar to the brute force, the key difference is we only store and calculate the current row, reducing space complexity.
> - **Space Complexity:** $O(n)$, as we only store the current row.
> - **Optimality proof:** This approach is optimal because it minimizes both time and space complexity by only calculating and storing the necessary row.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated include dynamic programming and the application of combinatorial formulas.
- Problem-solving patterns identified include recognizing opportunities to reduce space complexity by only storing necessary data.
- Optimization techniques learned include avoiding unnecessary calculations and memory usage.

**Mistakes to Avoid:**
- Common implementation errors include incorrect indexing and boundary checks.
- Edge cases to watch for include handling `rowIndex` values of 0 and 1 correctly.
- Performance pitfalls include using inefficient algorithms or data structures that lead to high time or space complexity.