## Dynamic Unpivoting of a Table

**Problem Link:** https://leetcode.com/problems/dynamic-unpivoting-of-a-table/description

**Problem Statement:**
- Input format: A table `items` with `m` rows and `n` columns, where each cell is a string.
- Constraints: `1 <= m <= 10^5`, `1 <= n <= 10^3`, and the length of each string is at most `10`.
- Expected output format: A list of tuples, where each tuple contains three strings: `item_id`, `attribute`, and `value`.
- Key requirements: Unpivot the table by creating a new row for each cell in the original table, with the row index as `item_id`, the column index as `attribute`, and the cell value as `value`.
- Edge cases: Empty table, single-row table, single-column table.

**Example Test Cases:**
- `items = [["M","M","S"],["L","M","L"],["S","M","S"]]`
  - Output: `[["0","0","M"],["0","1","M"],["0","2","S"],["1","0","L"],["1","1","M"],["1","2","L"],["2","0","S"],["2","1","M"],["2","2","S"]]`
- `items = [["Q","W","E"],["R","T","Y"]]`
  - Output: `[["0","0","Q"],["0","1","W"],["0","2","E"],["1","0","R"],["1","1","T"],["1","2","Y"]]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each cell in the table and create a new tuple for each cell.
- Step-by-step breakdown:
  1. Initialize an empty list to store the unpivoted tuples.
  2. Iterate over each row in the table.
  3. For each row, iterate over each cell in the row.
  4. For each cell, create a new tuple with the row index, column index, and cell value.
  5. Append the tuple to the list of unpivoted tuples.

```cpp
vector<vector<string>> unpivotTable(vector<vector<string>>& items) {
    vector<vector<string>> result;
    for (int i = 0; i < items.size(); i++) {
        for (int j = 0; j < items[i].size(); j++) {
            vector<string> tuple = {to_string(i), to_string(j), items[i][j]};
            result.push_back(tuple);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns. This is because we iterate over each cell in the table once.
> - **Space Complexity:** $O(m \cdot n)$, as we store each cell as a separate tuple in the result list.
> - **Why these complexities occur:** The brute force approach has a linear time complexity with respect to the total number of cells in the table, which is $m \cdot n$. The space complexity is also linear because we store each cell as a separate tuple.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The brute force approach is already optimal because we must visit each cell at least once to unpivot the table.
- Detailed breakdown: The optimal approach is the same as the brute force approach, as it has the minimum possible time complexity for this problem.
- Proof of optimality: Any algorithm that unpivots the table must visit each cell at least once, resulting in a time complexity of at least $O(m \cdot n)$.

```cpp
vector<vector<string>> unpivotTable(vector<vector<string>>& items) {
    vector<vector<string>> result;
    for (int i = 0; i < items.size(); i++) {
        for (int j = 0; j < items[i].size(); j++) {
            vector<string> tuple = {to_string(i), to_string(j), items[i][j]};
            result.push_back(tuple);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns.
> - **Space Complexity:** $O(m \cdot n)$, as we store each cell as a separate tuple in the result list.
> - **Optimality proof:** The optimal approach has the minimum possible time complexity for this problem, which is $O(m \cdot n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Iteration, tuple creation, and list manipulation.
- Problem-solving patterns: Unpivoting a table by iterating over each cell and creating new tuples.
- Optimization techniques: The brute force approach is already optimal for this problem.

**Mistakes to Avoid:**
- Not validating the input table for empty rows or columns.
- Not handling edge cases correctly, such as a table with a single row or column.
- Not using efficient data structures, such as vectors, to store the result.