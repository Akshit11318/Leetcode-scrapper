## Delete Greatest Value in Each Row
**Problem Link:** https://leetcode.com/problems/delete-greatest-value-in-each-row/description

**Problem Statement:**
- Input: A 2D array `grid` of size `m x n`, where `m` is the number of rows and `n` is the number of columns.
- Constraints: `1 <= m, n <= 10^5`.
- Expected output: The minimum number of columns to delete to make the grid sorted in non-decreasing order after deleting the columns.
- Key requirements and edge cases to consider: Handling empty grid, single row or column, and already sorted grid.
- Example test cases:
  - `grid = [[1,2,3],[2,2,3],[3,2,3]]`, the output should be `0` because the grid is already sorted.
  - `grid = [[1,2,3],[2,1,3],[3,1,3]]`, the output should be `1` because we can delete the second column to make the grid sorted.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through all possible combinations of columns and check if the grid is sorted after deleting each combination.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of columns.
  2. For each combination, delete the columns from the grid.
  3. Check if the grid is sorted after deleting the columns.
  4. Keep track of the minimum number of columns to delete to make the grid sorted.
- Why this approach comes to mind first: It is a straightforward approach to try all possible solutions and find the optimal one.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int minDeletionSize(vector<string>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    int minDeletions = INT_MAX;
    
    for (int mask = 0; mask < (1 << n); mask++) {
        vector<string> newGrid;
        for (int i = 0; i < m; i++) {
            string newRow;
            for (int j = 0; j < n; j++) {
                if (!(mask & (1 << j))) {
                    newRow += grid[i][j];
                }
            }
            newGrid.push_back(newRow);
        }
        
        bool isSorted = true;
        for (int i = 0; i < m - 1; i++) {
            for (int j = 0; j < newGrid[i].size(); j++) {
                if (newGrid[i][j] > newGrid[i + 1][j]) {
                    isSorted = false;
                    break;
                }
            }
            if (!isSorted) break;
        }
        
        if (isSorted) {
            int deletions = __builtin_popcount(mask);
            minDeletions = min(minDeletions, deletions);
        }
    }
    
    return minDeletions;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot m \cdot n)$, where $n$ is the number of columns and $m$ is the number of rows. This is because we generate all possible combinations of columns and check if the grid is sorted after deleting each combination.
> - **Space Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns. This is because we create a new grid after deleting the columns.
> - **Why these complexities occur:** The time complexity is high because we try all possible combinations of columns, and the space complexity is moderate because we create a new grid after deleting the columns.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can iterate through the columns and check if the current column is sorted. If it is not sorted, we can delete the current column.
- Detailed breakdown of the approach:
  1. Initialize a variable `deletions` to 0.
  2. Iterate through the columns.
  3. For each column, check if the column is sorted.
  4. If the column is not sorted, increment `deletions` and continue to the next column.
- Proof of optimality: This approach is optimal because it only deletes the columns that are not sorted, and it does not try all possible combinations of columns.

```cpp
int minDeletionSize(vector<string>& grid) {
    int m = grid.size();
    int n = grid[0].size();
    int deletions = 0;
    
    for (int j = 0; j < n; j++) {
        for (int i = 0; i < m - 1; i++) {
            if (grid[i][j] > grid[i + 1][j]) {
                deletions++;
                break;
            }
        }
    }
    
    return deletions;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns. This is because we iterate through the columns and check if each column is sorted.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the `deletions` variable.
> - **Optimality proof:** This approach is optimal because it only deletes the columns that are not sorted, and it does not try all possible combinations of columns.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, sorting, and deletion of columns.
- Problem-solving patterns identified: Checking if a column is sorted and deleting it if it is not.
- Optimization techniques learned: Avoiding unnecessary iterations and deletions.
- Similar problems to practice: Other problems that involve sorting and deletion of columns or rows.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if a column is sorted before deleting it.
- Edge cases to watch for: Empty grid, single row or column, and already sorted grid.
- Performance pitfalls: Trying all possible combinations of columns, which can lead to high time complexity.
- Testing considerations: Test the solution with different inputs, including edge cases, to ensure it works correctly.