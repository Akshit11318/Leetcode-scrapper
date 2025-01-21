## Check If Grid Satisfies Conditions
**Problem Link:** https://leetcode.com/problems/check-if-grid-satisfies-conditions/description

**Problem Statement:**
- Input: A 2D grid `grid` of size `m x n` where each cell contains a boolean value, and a list of conditions `condition`.
- Constraints: The grid only contains `0`s and `1`s, and `condition` is a list of lists where each sublist contains three integers: `row1`, `col1`, `row2`, and `col2`.
- Expected Output: A boolean indicating whether the grid satisfies all the conditions.
- Key Requirements: For each condition, if the cell at `(row1, col1)` has a value of `1`, then the cell at `(row2, col2)` must also have a value of `1`.
- Edge Cases: The grid can be empty, or the conditions list can be empty. Also, the row and column indices in the conditions can be out of bounds.

### Brute Force Approach
**Explanation:**
- The initial thought process is to iterate over each condition and check if the grid satisfies it by directly accessing the cells specified in the condition.
- This approach comes to mind first because it directly implements the condition checking without considering any optimizations.

```cpp
class Solution {
public:
    bool satisfiesConditions(vector<vector<int>>& grid, vector<vector<int>>& condition) {
        // Iterate over each condition
        for (auto& cond : condition) {
            int row1 = cond[0], col1 = cond[1], row2 = cond[2], col2 = cond[3];
            // Check if row1, col1 is within grid bounds and has a value of 1
            if (row1 < grid.size() && col1 < grid[0].size() && grid[row1][col1] == 1) {
                // Check if row2, col2 is within grid bounds and has a value of 1
                if (row2 >= grid.size() || col2 >= grid[0].size() || grid[row2][col2] != 1) {
                    return false; // Condition not satisfied
                }
            }
        }
        return true; // All conditions satisfied
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot c)$ where $m$ and $n$ are the dimensions of the grid and $c$ is the number of conditions, because in the worst case, we might need to check every cell for every condition.
> - **Space Complexity:** $O(1)$, not considering the space required for the input, because we only use a constant amount of space to store the indices and the result.
> - **Why these complexities occur:** The brute force approach has high time complexity due to the nested iteration over conditions and grid cells, but it has low space complexity since it only uses a constant amount of space.

### Optimal Approach (Required)
**Explanation:**
- The key insight is that we can still directly check each condition without any additional optimizations because the problem constraints do not allow for any significant reductions in the number of checks.
- This approach is optimal because we must check every condition at least once to ensure all are satisfied.

```cpp
class Solution {
public:
    bool satisfiesConditions(vector<vector<int>>& grid, vector<vector<int>>& condition) {
        // Iterate over each condition
        for (auto& cond : condition) {
            int row1 = cond[0], col1 = cond[1], row2 = cond[2], col2 = cond[3];
            // Check if the condition is satisfied
            if (row1 < grid.size() && col1 < grid[0].size() && grid[row1][col1] == 1 &&
                (row2 >= grid.size() || col2 >= grid[0].size() || grid[row2][col2] != 1)) {
                return false; // Condition not satisfied
            }
        }
        return true; // All conditions satisfied
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(c)$ where $c$ is the number of conditions, because we only need to check each condition once.
> - **Space Complexity:** $O(1)$, not considering the space required for the input, because we only use a constant amount of space to store the indices and the result.
> - **Optimality proof:** This is the optimal approach because we must check every condition at least once, and we do so with minimal overhead.

### Final Notes

**Learning Points:**
- Direct condition checking can be the optimal approach when the problem constraints are simple and do not allow for significant optimizations.
- Always consider the problem constraints when analyzing the time and space complexity of an algorithm.

**Mistakes to Avoid:**
- Assuming that a brute force approach is always suboptimal. In some cases, it can be the simplest and most efficient solution.
- Not considering the problem constraints when analyzing complexity. The constraints can significantly impact the optimal approach.