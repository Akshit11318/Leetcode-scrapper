## Drop Duplicate Rows

**Problem Link:** https://leetcode.com/problems/drop-duplicate-rows/description

**Problem Statement:**
- Input format: A table with `id` and `name` columns.
- Constraints: The table has at least one row and at most 100 rows.
- Expected output format: A table with unique rows based on the `name` column.
- Key requirements: Remove duplicate rows based on the `name` column.
- Edge cases: Handle cases where the input table is empty or contains only one row.

Example test cases:

| id | name |
|----|------|
| 1  | John |
| 2  | John |
| 3  | Jane |

Expected output:

| id | name |
|----|------|
| 1  | John |
| 3  | Jane |

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate over each row in the table and check if the `name` column value already exists in the result table.
- Step-by-step breakdown:
  1. Create an empty result table.
  2. Iterate over each row in the input table.
  3. For each row, check if the `name` column value exists in the result table.
  4. If it does not exist, add the row to the result table.

```cpp
#include <vector>
#include <string>

struct Row {
    int id;
    std::string name;
};

std::vector<Row> dropDuplicateRows(std::vector<Row>& table) {
    std::vector<Row> result;
    for (const auto& row : table) {
        bool exists = false;
        for (const auto& resRow : result) {
            if (resRow.name == row.name) {
                exists = true;
                break;
            }
        }
        if (!exists) {
            result.push_back(row);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of rows in the table. This is because we are iterating over each row and checking if the `name` column value exists in the result table, which also involves iteration.
> - **Space Complexity:** $O(n)$, where $n$ is the number of unique rows in the table. This is because we are storing the result in a separate table.
> - **Why these complexities occur:** The brute force approach involves nested iteration, which leads to a quadratic time complexity. The space complexity is linear because we are storing the result in a separate table.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a `std::unordered_set` to keep track of unique `name` column values.
- Step-by-step breakdown:
  1. Create an empty `std::unordered_set` to store unique `name` column values.
  2. Create an empty result table.
  3. Iterate over each row in the input table.
  4. For each row, check if the `name` column value exists in the `std::unordered_set`.
  5. If it does not exist, add the row to the result table and the `name` column value to the `std::unordered_set`.

```cpp
#include <vector>
#include <string>
#include <unordered_set>

struct Row {
    int id;
    std::string name;
};

std::vector<Row> dropDuplicateRows(std::vector<Row>& table) {
    std::vector<Row> result;
    std::unordered_set<std::string> uniqueNames;
    for (const auto& row : table) {
        if (uniqueNames.find(row.name) == uniqueNames.end()) {
            result.push_back(row);
            uniqueNames.insert(row.name);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the table. This is because we are iterating over each row and checking if the `name` column value exists in the `std::unordered_set`, which has an average constant time complexity.
> - **Space Complexity:** $O(n)$, where $n$ is the number of unique `name` column values. This is because we are storing the unique `name` column values in the `std::unordered_set` and the result in a separate table.
> - **Optimality proof:** This approach is optimal because we are using a data structure with an average constant time complexity to check for duplicate `name` column values, and we are only iterating over the input table once.

---

### Final Notes

**Learning Points:**
- The importance of choosing the right data structure for the problem.
- The use of `std::unordered_set` to keep track of unique values.
- The optimization of iteration by using a data structure with an average constant time complexity.

**Mistakes to Avoid:**
- Using a brute force approach that involves nested iteration.
- Not considering the use of a data structure with an average constant time complexity.
- Not handling edge cases such as an empty input table or a table with only one row.