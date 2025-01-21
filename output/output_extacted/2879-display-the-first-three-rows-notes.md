## Display the First Three Rows

**Problem Link:** https://leetcode.com/problems/display-the-first-three-rows/description

**Problem Statement:**
- Input format and constraints: Given a table with unknown number of rows and columns, display the first three rows.
- Expected output format: A table with the first three rows of the input table.
- Key requirements and edge cases to consider: If the table has less than three rows, display all rows.
- Example test cases with explanations:
  - Test case 1: Table with 5 rows and 3 columns. Expected output: First three rows.
  - Test case 2: Table with 1 row and 3 columns. Expected output: The single row.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Read the table row by row and append each row to the output until we have three rows or we reach the end of the table.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list to store the output rows.
  2. Iterate over each row in the table.
  3. Append each row to the output list until the list has three rows.
  4. Return the output list.
- Why this approach comes to mind first: It's the simplest way to solve the problem, but it might not be the most efficient.

```cpp
vector<vector<int>> displayFirstThreeRows(vector<vector<int>>& table) {
    vector<vector<int>> output;
    for (int i = 0; i < table.size() && i < 3; i++) {
        output.push_back(table[i]);
    }
    return output;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows in the table and $n$ is the number of columns. We iterate over each row in the table, and for each row, we iterate over each column.
> - **Space Complexity:** $O(m \cdot n)$, where $m$ is the number of rows in the output and $n$ is the number of columns. We store the output in a vector of vectors.
> - **Why these complexities occur:** The time complexity is due to the iteration over the table, and the space complexity is due to the storage of the output.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Since we only need to display the first three rows, we can stop iterating over the table once we have three rows.
- Detailed breakdown of the approach:
  1. Initialize an empty list to store the output rows.
  2. Iterate over each row in the table.
  3. Append each row to the output list until the list has three rows.
  4. Return the output list.
- Proof of optimality: This solution is optimal because we only iterate over the necessary rows and we don't store any unnecessary data.
- Why further optimization is impossible: We can't do better than this because we need to at least read the first three rows of the table.

```cpp
vector<vector<int>> displayFirstThreeRows(vector<vector<int>>& table) {
    vector<vector<int>> output;
    for (int i = 0; i < min(3, (int)table.size()); i++) {
        output.push_back(table[i]);
    }
    return output;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the minimum of 3 and the number of rows in the table, and $n$ is the number of columns. We iterate over each row in the output, and for each row, we iterate over each column.
> - **Space Complexity:** $O(m \cdot n)$, where $m$ is the minimum of 3 and the number of rows in the table, and $n$ is the number of columns. We store the output in a vector of vectors.
> - **Optimality proof:** The time complexity is optimal because we only iterate over the necessary rows, and the space complexity is optimal because we only store the necessary data.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration over a table, conditional appending to a list.
- Problem-solving patterns identified: Stopping iteration once a condition is met.
- Optimization techniques learned: Only iterating over the necessary data.
- Similar problems to practice: Displaying a subset of rows or columns from a table.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for the end of the table, not handling the case where the table has less than three rows.
- Edge cases to watch for: Tables with less than three rows, tables with no rows.
- Performance pitfalls: Iterating over the entire table when only a subset is needed.
- Testing considerations: Testing with tables of different sizes, testing with tables that have less than three rows.