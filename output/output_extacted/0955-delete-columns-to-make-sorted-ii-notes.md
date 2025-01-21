## Delete Columns to Make Sorted II

**Problem Link:** https://leetcode.com/problems/delete-columns-to-make-sorted-ii/description

**Problem Statement:**
- Input format: A 2D `vector<string>` `strs` where each string represents a row in a grid.
- Constraints: `1 <= strs.length <= 100`, `1 <= strs[i].length <= 100`.
- Expected output format: The minimum number of columns that need to be deleted to make the grid sorted.
- Key requirements and edge cases to consider:
  - A grid is considered sorted if for each column, all elements are in non-decreasing order.
  - If the grid is already sorted, return `0`.
  - The input grid may contain duplicate rows or columns.
- Example test cases with explanations:
  - For input `[["abc","bce","cae"],["abc","bce","cae"]]`, the output is `1` because deleting the third column makes the grid sorted.
  - For input `[["a","b","c"],["aaa","bbb","ccc"]]`, the output is `0` because the grid is already sorted.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we need to check all possible combinations of columns and see if deleting those columns makes the grid sorted.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsets of columns.
  2. For each subset, create a new grid by removing the columns in the subset.
  3. Check if the new grid is sorted.
  4. If the new grid is sorted, update the minimum number of columns to delete.
- Why this approach comes to mind first: It's a straightforward approach that checks all possibilities.

```cpp
#include <vector>
#include <string>

class Solution {
public:
    int minDeletionSize(std::vector<std::string>& strs) {
        int minColumns = INT_MAX;
        int n = strs.size();
        int m = strs[0].size();
        for (int mask = 0; mask < (1 << m); mask++) {
            std::vector<std::string> newStrs(n);
            bool isValid = true;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if ((mask & (1 << j)) == 0) {
                        newStrs[i] += strs[i][j];
                    }
                }
            }
            for (int i = 0; i < n - 1; i++) {
                if (newStrs[i] > newStrs[i + 1]) {
                    isValid = false;
                    break;
                }
            }
            if (isValid) {
                int columns = __builtin_popcount(mask);
                minColumns = std::min(minColumns, columns);
            }
        }
        return minColumns;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^m \cdot n \cdot m)$ where $m$ is the number of columns and $n$ is the number of rows. This is because we generate all possible subsets of columns and for each subset, we create a new grid and check if it's sorted.
> - **Space Complexity:** $O(n \cdot m)$ where $n$ is the number of rows and $m$ is the number of columns. This is because we create a new grid for each subset of columns.
> - **Why these complexities occur:** The time complexity occurs because we use a brute force approach and check all possible subsets of columns. The space complexity occurs because we create a new grid for each subset of columns.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a greedy approach to solve this problem. We iterate through each column and check if it's sorted. If it's not sorted, we delete the column.
- Detailed breakdown of the approach:
  1. Initialize a variable `minColumns` to `0`.
  2. Iterate through each column.
  3. For each column, check if it's sorted.
  4. If the column is not sorted, increment `minColumns` by `1`.
- Proof of optimality: This approach is optimal because it only deletes columns that are not sorted, and it does so in a single pass through the grid.

```cpp
class Solution {
public:
    int minDeletionSize(std::vector<std::string>& strs) {
        int minColumns = 0;
        int n = strs.size();
        int m = strs[0].size();
        for (int j = 0; j < m; j++) {
            bool isValid = true;
            for (int i = 0; i < n - 1; i++) {
                if (strs[i][j] > strs[i + 1][j]) {
                    isValid = false;
                    break;
                }
            }
            if (!isValid) {
                minColumns++;
            }
        }
        return minColumns;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of rows and $m$ is the number of columns. This is because we iterate through each column and check if it's sorted.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store the `minColumns` variable.
> - **Optimality proof:** This approach is optimal because it only deletes columns that are not sorted, and it does so in a single pass through the grid.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy approach, bit manipulation.
- Problem-solving patterns identified: Checking all possible subsets of columns, using a greedy approach to solve the problem.
- Optimization techniques learned: Using a greedy approach to reduce the time complexity of the solution.
- Similar problems to practice: Other problems that involve checking all possible subsets of columns or using a greedy approach to solve the problem.

**Mistakes to Avoid:**
- Common implementation errors: Not checking all possible subsets of columns, not using a greedy approach to solve the problem.
- Edge cases to watch for: The input grid may contain duplicate rows or columns, the grid may already be sorted.
- Performance pitfalls: Using a brute force approach to solve the problem, not optimizing the solution to reduce the time complexity.
- Testing considerations: Testing the solution with different input grids, including grids with duplicate rows or columns, and grids that are already sorted.