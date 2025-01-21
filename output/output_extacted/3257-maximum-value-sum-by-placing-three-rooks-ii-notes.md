## Maximum Value Sum by Placing Three Rooks II

**Problem Link:** https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-ii/description

**Problem Statement:**
- Input: A 3x3 grid, represented as a vector of vectors, where each cell contains a non-negative integer.
- Constraints: The grid will have exactly 3 rows and 3 columns.
- Expected Output: The maximum sum that can be achieved by placing three rooks in the grid such that no two rooks are in the same row or column.
- Key Requirements: Each rook must be placed in a unique row and a unique column.
- Edge Cases: The grid may contain zeros, and the sum of the values in the grid may exceed the maximum limit of an integer.

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible combinations of placing three rooks in the grid.
- This can be achieved by using three nested loops to iterate over each cell in the grid, and then checking if the current cell can be used to place a rook.
- The brute force approach comes to mind first because it is straightforward and easy to implement.

```cpp
class Solution {
public:
    int maxSum(vector<vector<int>>& grid) {
        int max_sum = 0;
        // Iterate over all possible combinations of placing three rooks
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    for (int l = 0; l < 3; l++) {
                        for (int m = 0; m < 3; m++) {
                            for (int n = 0; n < 3; n++) {
                                // Check if the current combination is valid
                                if (i != k && i != m && k != m && j != l && j != n && l != n) {
                                    // Calculate the sum for the current combination
                                    int sum = grid[i][j] + grid[k][l] + grid[m][n];
                                    // Update the maximum sum
                                    max_sum = max(max_sum, sum);
                                }
                            }
                        }
                    }
                }
            }
        }
        return max_sum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(3^6)$, which simplifies to $O(729)$. This is because we have six nested loops, each iterating over three possible values.
> - **Space Complexity:** $O(1)$, which means the space required does not change with the size of the input grid, making it constant.
> - **Why these complexities occur:** The brute force approach has a high time complexity because it tries all possible combinations of placing three rooks in the grid. The space complexity is low because we only use a constant amount of space to store the maximum sum.

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to realize that we can place the first rook in any of the nine cells, the second rook in any of the remaining four cells that are not in the same row or column as the first rook, and the third rook in any of the remaining cell that is not in the same row or column as the first two rooks.
- However, a more efficient approach is to consider the columns and rows as separate entities and use a permutation-based approach to find the maximum sum.
- We can use a single loop to iterate over all possible permutations of the columns and calculate the sum for each permutation.

```cpp
class Solution {
public:
    int maxSum(vector<vector<int>>& grid) {
        int max_sum = 0;
        // Iterate over all possible permutations of the columns
        vector<int> cols = {0, 1, 2};
        do {
            int sum = 0;
            // Calculate the sum for the current permutation
            for (int i = 0; i < 3; i++) {
                sum += grid[i][cols[i]];
            }
            // Update the maximum sum
            max_sum = max(max_sum, sum);
        } while (next_permutation(cols.begin(), cols.end()));
        return max_sum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(3!)$, which simplifies to $O(6)$. This is because we have a single loop that iterates over all possible permutations of the columns.
> - **Space Complexity:** $O(1)$, which means the space required does not change with the size of the input grid, making it constant.
> - **Optimality proof:** This approach is optimal because it considers all possible permutations of the columns and calculates the sum for each permutation. This ensures that we find the maximum sum that can be achieved by placing three rooks in the grid.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: permutation-based approach, iteration over all possible combinations.
- Problem-solving patterns identified: using a single loop to iterate over all possible permutations, calculating the sum for each permutation.
- Optimization techniques learned: using a permutation-based approach to reduce the time complexity.
- Similar problems to practice: other problems that involve finding the maximum sum or minimum sum by placing objects in a grid.

**Mistakes to Avoid:**
- Common implementation errors: not checking for invalid combinations, not updating the maximum sum correctly.
- Edge cases to watch for: the grid may contain zeros, the sum of the values in the grid may exceed the maximum limit of an integer.
- Performance pitfalls: using a brute force approach with a high time complexity, not using a permutation-based approach to reduce the time complexity.
- Testing considerations: testing the function with different input grids, testing the function with edge cases.