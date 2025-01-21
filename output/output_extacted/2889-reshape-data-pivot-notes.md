## Reshape Data Pivot
**Problem Link:** https://leetcode.com/problems/reshape-data-pivot/description

**Problem Statement:**
- Input format and constraints: The input is a table with `id` and `value` columns, and a `pivot` column that determines how to pivot the table. The `id` column is the identifier for each row, the `value` column is the value to be pivoted, and the `pivot` column is the column to pivot on.
- Expected output format: The output is a pivoted table with `id` as the identifier, and columns for each unique value in the `pivot` column.
- Key requirements and edge cases to consider: The table can have multiple rows with the same `id` and `pivot` value, in which case the values should be aggregated using the `SUM` function.
- Example test cases with explanations:
  - If the input table is:
    | id | value | pivot |
    |----|-------|--------|
    | 1  | 10    | A      |
    | 2  | 20    | B      |
    | 1  | 30    | B      |
  - The output should be:
    | id | A    | B    |
    |----|------|------|
    | 1  | 10   | 30   |
    | 2  | NULL | 20   |

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to iterate over the input table, and for each row, check if the `id` and `pivot` value already exist in the output table. If they do, update the corresponding value in the output table. If they don't, create a new row in the output table.
- Step-by-step breakdown of the solution:
  1. Create an empty output table.
  2. Iterate over the input table.
  3. For each row in the input table, check if the `id` and `pivot` value already exist in the output table.
  4. If they do, update the corresponding value in the output table.
  5. If they don't, create a new row in the output table.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient for large input tables.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

struct Row {
    int id;
    int value;
    char pivot;
};

std::vector<std::vector<int>> reshapeDataPivot(std::vector<Row>& rows) {
    std::unordered_map<int, std::unordered_map<char, int>> outputTable;
    
    for (const auto& row : rows) {
        if (outputTable.find(row.id) == outputTable.end()) {
            outputTable[row.id] = {};
        }
        
        if (outputTable[row.id].find(row.pivot) == outputTable[row.id].end()) {
            outputTable[row.id][row.pivot] = 0;
        }
        
        outputTable[row.id][row.pivot] += row.value;
    }
    
    // Create the output table with the correct columns
    std::vector<char> pivotValues;
    for (const auto& row : rows) {
        if (std::find(pivotValues.begin(), pivotValues.end(), row.pivot) == pivotValues.end()) {
            pivotValues.push_back(row.pivot);
        }
    }
    
    std::sort(pivotValues.begin(), pivotValues.end());
    
    std::vector<std::vector<int>> result;
    for (const auto& id : outputTable) {
        std::vector<int> row = {id.first};
        for (const auto& pivot : pivotValues) {
            if (id.second.find(pivot) != id.second.end()) {
                row.push_back(id.second[pivot]);
            } else {
                row.push_back(0);
            }
        }
        result.push_back(row);
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot log(m))$, where $n$ is the number of rows in the input table and $m$ is the number of unique pivot values. This is because we iterate over the input table, and for each row, we iterate over the unique pivot values to find the correct column.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of rows in the input table and $m$ is the number of unique pivot values. This is because we create an output table with $n$ rows and $m$ columns.
> - **Why these complexities occur:** These complexities occur because we iterate over the input table and create an output table with the correct columns.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use a hash table to store the output table, where the key is the `id` and the value is another hash table with the pivot values as keys and the values as values.
- Detailed breakdown of the approach:
  1. Create an empty hash table to store the output table.
  2. Iterate over the input table.
  3. For each row in the input table, check if the `id` already exists in the output table. If it does, update the corresponding value in the output table. If it doesn't, create a new entry in the output table.
  4. Create the output table with the correct columns by iterating over the unique pivot values.
- Proof of optimality: This approach is optimal because it has a time complexity of $O(n \cdot m)$, where $n$ is the number of rows in the input table and $m$ is the number of unique pivot values. This is because we iterate over the input table and create an output table with the correct columns.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

struct Row {
    int id;
    int value;
    char pivot;
};

std::vector<std::vector<int>> reshapeDataPivot(std::vector<Row>& rows) {
    std::unordered_map<int, std::unordered_map<char, int>> outputTable;
    std::unordered_set<char> pivotValues;
    
    for (const auto& row : rows) {
        if (outputTable.find(row.id) == outputTable.end()) {
            outputTable[row.id] = {};
        }
        
        if (outputTable[row.id].find(row.pivot) == outputTable[row.id].end()) {
            outputTable[row.id][row.pivot] = 0;
        }
        
        outputTable[row.id][row.pivot] += row.value;
        pivotValues.insert(row.pivot);
    }
    
    // Create the output table with the correct columns
    std::vector<std::vector<int>> result;
    for (const auto& id : outputTable) {
        std::vector<int> row = {id.first};
        for (const auto& pivot : pivotValues) {
            if (id.second.find(pivot) != id.second.end()) {
                row.push_back(id.second[pivot]);
            } else {
                row.push_back(0);
            }
        }
        result.push_back(row);
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of rows in the input table and $m$ is the number of unique pivot values. This is because we iterate over the input table and create an output table with the correct columns.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of rows in the input table and $m$ is the number of unique pivot values. This is because we create an output table with $n$ rows and $m$ columns.
> - **Optimality proof:** This approach is optimal because it has a time complexity of $O(n \cdot m)$, which is the minimum time complexity required to solve this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hash tables, iteration over input tables, creation of output tables with correct columns.
- Problem-solving patterns identified: Using hash tables to store output tables, iterating over input tables to create output tables.
- Optimization techniques learned: Using hash tables to reduce time complexity, iterating over input tables to reduce space complexity.
- Similar problems to practice: Pivoting tables, creating output tables with correct columns, using hash tables to store output tables.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the `id` already exists in the output table, not updating the correct value in the output table.
- Edge cases to watch for: Handling cases where the input table is empty, handling cases where the output table is empty.
- Performance pitfalls: Using nested loops to iterate over the input table, using recursive functions to create the output table.
- Testing considerations: Testing with different input tables, testing with different pivot values, testing with different output tables.