## Create a New Column
**Problem Link:** https://leetcode.com/problems/create-a-new-column/description

**Problem Statement:**
- Input format and constraints: The input will be a list of `n` integers representing the `n` rows in the table. The task is to create a new column based on the given condition.
- Expected output format: The output should be a list of integers representing the new column.
- Key requirements and edge cases to consider: The new column is created by adding `1` to the value in the original column if the value is less than `5`, and subtracting `1` if the value is greater than or equal to `5`.
- Example test cases with explanations:
  - For input `[1, 2, 3, 4, 5, 6]`, the output should be `[2, 3, 4, 5, 4, 5]`.
  - For input `[10, 20, 30]`, the output should be `[9, 19, 29]`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The first approach that comes to mind is to iterate through each element in the input list and apply the given condition to create the new column.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list to store the new column.
  2. Iterate through each element in the input list.
  3. For each element, check if the value is less than `5` or greater than or equal to `5`.
  4. If the value is less than `5`, add `1` to the value and append it to the new column.
  5. If the value is greater than or equal to `5`, subtract `1` from the value and append it to the new column.
- Why this approach comes to mind first: This approach is straightforward and directly applies the given condition to create the new column.

```cpp
vector<int> createNewColumn(vector<int>& input) {
    vector<int> newColumn;
    for (int i = 0; i < input.size(); i++) {
        if (input[i] < 5) {
            newColumn.push_back(input[i] + 1);
        } else {
            newColumn.push_back(input[i] - 1);
        }
    }
    return newColumn;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the input list. This is because we are iterating through each element in the input list once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the input list. This is because we are creating a new list to store the new column, which has the same number of elements as the input list.
> - **Why these complexities occur:** The time complexity occurs because we are iterating through each element in the input list, and the space complexity occurs because we are creating a new list to store the new column.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is the same as the brute force approach, as we need to iterate through each element in the input list to create the new column.
- Detailed breakdown of the approach:
  1. Initialize an empty list to store the new column.
  2. Iterate through each element in the input list.
  3. For each element, check if the value is less than `5` or greater than or equal to `5`.
  4. If the value is less than `5`, add `1` to the value and append it to the new column.
  5. If the value is greater than or equal to `5`, subtract `1` from the value and append it to the new column.
- Proof of optimality: This approach is optimal because we need to iterate through each element in the input list to create the new column, and we are doing so in a single pass.
- Why further optimization is impossible: Further optimization is impossible because we need to iterate through each element in the input list to create the new column, and we are already doing so in a single pass.

```cpp
vector<int> createNewColumn(vector<int>& input) {
    vector<int> newColumn;
    for (int i = 0; i < input.size(); i++) {
        newColumn.push_back(input[i] < 5 ? input[i] + 1 : input[i] - 1);
    }
    return newColumn;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the input list. This is because we are iterating through each element in the input list once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the input list. This is because we are creating a new list to store the new column, which has the same number of elements as the input list.
> - **Optimality proof:** This approach is optimal because we need to iterate through each element in the input list to create the new column, and we are doing so in a single pass.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional statements, and list manipulation.
- Problem-solving patterns identified: The problem requires iterating through each element in the input list and applying a condition to create the new column.
- Optimization techniques learned: The optimal solution is the same as the brute force approach, as we need to iterate through each element in the input list to create the new column.
- Similar problems to practice: Problems that require iterating through each element in a list and applying a condition.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize the new column, or using the wrong condition to create the new column.
- Edge cases to watch for: The input list may be empty, or the values in the input list may be outside the expected range.
- Performance pitfalls: Using unnecessary loops or conditional statements, or creating unnecessary intermediate lists.
- Testing considerations: Test the solution with different input lists, including empty lists and lists with values outside the expected range.