## Difference of Number of Distinct Values on Diagonals

**Problem Link:** https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/description

**Problem Statement:**
- Input: A 2D array `grid` of integers, where each cell represents a value.
- Constraints: The grid will have at least 1 row and 1 column, and at most 300 rows and 300 columns. Each cell's value will be between 1 and 10^9.
- Expected Output: The absolute difference between the number of distinct values on the primary diagonal and the number of distinct values on the secondary diagonal.
- Key Requirements: The primary diagonal runs from top-left to bottom-right (cells where row index equals column index), and the secondary diagonal runs from top-right to bottom-left (cells where row index equals grid size minus column index minus one).
- Example Test Cases:
  - Input: `[[1,2,3],[4,5,6],[7,8,9]]`
    - Primary diagonal: `[1, 5, 9]`
    - Secondary diagonal: `[3, 5, 7]`
    - Output: `|3 - 3| = 0`
  - Input: `[[1,1,1],[1,1,1],[1,1,1]]`
    - Primary diagonal: `[1, 1, 1]`
    - Secondary diagonal: `[1, 1, 1]`
    - Output: `|1 - 1| = 0`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves iterating over the grid to extract values on both diagonals.
- Then, we count the distinct values in each diagonal.
- This approach comes to mind first because it directly addresses the problem statement with minimal complexity.

```cpp
#include <vector>
#include <unordered_set>

int countDistinct(vector<vector<int>>& grid, bool primary) {
    unordered_set<int> distinct;
    for (int i = 0; i < grid.size(); i++) {
        if (primary) {
            distinct.insert(grid[i][i]);
        } else {
            distinct.insert(grid[i][grid.size() - i - 1]);
        }
    }
    return distinct.size();
}

int differenceOfDistinctValues(vector<vector<int>>& grid) {
    int primaryCount = countDistinct(grid, true);
    int secondaryCount = countDistinct(grid, false);
    return abs(primaryCount - secondaryCount);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows (or columns) in the grid. This is because we are iterating over the grid once for each diagonal.
> - **Space Complexity:** $O(n)$, for storing distinct values in the `unordered_set`.
> - **Why these complexities occur:** The iteration over the grid and the use of `unordered_set` for counting distinct values lead to these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to realize that we don't need to store all distinct values, just count them.
- We can achieve this by using `unordered_set` to count distinct values on the fly as we iterate over the diagonals.
- This approach is optimal because it minimizes both time and space complexity by avoiding unnecessary operations and data structures.

```cpp
#include <vector>
#include <unordered_set>

int differenceOfDistinctValues(vector<vector<int>>& grid) {
    unordered_set<int> primary;
    unordered_set<int> secondary;
    for (int i = 0; i < grid.size(); i++) {
        primary.insert(grid[i][i]);
        secondary.insert(grid[i][grid.size() - i - 1]);
    }
    return abs(primary.size() - secondary.size());
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows (or columns) in the grid, as we only iterate over the grid once.
> - **Space Complexity:** $O(n)$, for storing distinct values in the `unordered_set`s.
> - **Optimality proof:** This is the best possible complexity because we must at least read the input once, and using `unordered_set` allows us to count distinct values in constant time per insertion, making it optimal for this problem.

---

### Final Notes

**Learning Points:**
- Using `unordered_set` for counting distinct values efficiently.
- Minimizing space complexity by only storing necessary data.
- Understanding the trade-off between time and space complexity in algorithm design.

**Mistakes to Avoid:**
- Not considering the use of `unordered_set` for efficient distinct value counting.
- Overcomplicating the solution by using unnecessary data structures or iterations.
- Not analyzing the problem for potential optimizations before implementing a brute force approach.

---