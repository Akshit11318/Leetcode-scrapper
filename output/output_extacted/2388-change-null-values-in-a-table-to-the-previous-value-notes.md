## Change Null Values in a Table to the Previous Value

**Problem Link:** https://leetcode.com/problems/change-null-values-in-a-table-to-the-previous-value/description

**Problem Statement:**
- Input format and constraints: The input is a table with a single column, and the table may contain null values. The task is to update the null values to the previous non-null value in the same column.
- Expected output format: The modified table with null values replaced.
- Key requirements and edge cases to consider: Handling the first null value, preserving non-null values, and updating subsequent null values to the last non-null value.
- Example test cases with explanations:
  - Test case 1: A table with a single column containing non-null values only.
  - Test case 2: A table with a single column containing null values and non-null values.
  - Test case 3: A table with a single column containing only null values.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through the table row by row, and for each null value, find the previous non-null value and update the null value.
- Step-by-step breakdown of the solution:
  1. Initialize a variable to store the last non-null value.
  2. Iterate through the table row by row.
  3. For each row, check if the value is null.
  4. If the value is null, update it to the last non-null value.
  5. If the value is not null, update the last non-null value.
- Why this approach comes to mind first: It is a straightforward and intuitive solution.

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

// Define a function to update null values
void updateNullValues(vector<string>& table) {
  string lastNonNullValue;
  
  for (int i = 0; i < table.size(); i++) {
    if (table[i] != "null") {
      lastNonNullValue = table[i];
    } else {
      table[i] = lastNonNullValue;
    }
  }
}

int main() {
  vector<string> table = {"1", "null", "2", "null", "3"};
  updateNullValues(table);
  
  // Print the updated table
  for (int i = 0; i < table.size(); i++) {
    cout << table[i] << endl;
  }
  
  return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the table. This is because we iterate through the table once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the last non-null value.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each row in the table. The space complexity is constant because we only use a fixed amount of space to store the last non-null value.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can still iterate through the table row by row and update null values to the previous non-null value.
- Detailed breakdown of the approach:
  1. Initialize a variable to store the last non-null value.
  2. Iterate through the table row by row.
  3. For each row, check if the value is null.
  4. If the value is null, update it to the last non-null value.
  5. If the value is not null, update the last non-null value.
- Proof of optimality: This approach is optimal because it only requires a single pass through the table, resulting in a linear time complexity.
- Why further optimization is impossible: We must at least read the input table once, resulting in a time complexity of at least $O(n)$.

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

// Define a function to update null values
void updateNullValues(vector<string>& table) {
  string lastNonNullValue;
  
  for (int i = 0; i < table.size(); i++) {
    if (table[i] != "null") {
      lastNonNullValue = table[i];
    } else {
      table[i] = lastNonNullValue;
    }
  }
}

int main() {
  vector<string> table = {"1", "null", "2", "null", "3"};
  updateNullValues(table);
  
  // Print the updated table
  for (int i = 0; i < table.size(); i++) {
    cout << table[i] << endl;
  }
  
  return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the table. This is because we iterate through the table once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the last non-null value.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the table, resulting in a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional statements, and updating values in a table.
- Problem-solving patterns identified: Handling null values and updating them to the previous non-null value.
- Optimization techniques learned: Reducing the number of iterations and using a constant amount of space.
- Similar problems to practice: Handling null values in a table with multiple columns, updating null values to the next non-null value.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the last non-null value, not updating the last non-null value correctly.
- Edge cases to watch for: Handling the first null value, preserving non-null values, and updating subsequent null values to the last non-null value.
- Performance pitfalls: Using more than a single pass through the table, using more than a constant amount of space.
- Testing considerations: Testing with different input tables, including tables with only non-null values, tables with only null values, and tables with a mix of non-null and null values.