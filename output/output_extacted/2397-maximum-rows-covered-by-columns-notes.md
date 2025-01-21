## Maximum Rows Covered by Columns

**Problem Link:** https://leetcode.com/problems/maximum-rows-covered-by-columns/description

**Problem Statement:**
- Input: A 2D array `mat` representing a matrix and an integer `numSelect` representing the number of columns to select.
- Expected Output: The maximum number of rows that can be covered by selecting `numSelect` columns.
- Key Requirements:
  - The matrix `mat` contains binary values (0 or 1).
  - A row is considered covered if it contains at least one 1 in the selected columns.
- Example Test Cases:
  - For `mat = [[0,0,0],[1,0,1],[0,1,1]]` and `numSelect = 2`, the maximum rows covered is 3 because we can select the last two columns.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible combinations of selecting `numSelect` columns from the given matrix and then check which combination covers the most rows.
- Step-by-step breakdown:
  1. Generate all possible combinations of `numSelect` columns from the matrix.
  2. For each combination, iterate through the rows of the matrix and count the number of rows that have at least one 1 in the selected columns.
  3. Keep track of the maximum count of rows covered by any combination.

```cpp
#include <vector>
#include <algorithm>

int maxRowsCovered(std::vector<std::vector<int>>& mat, int numSelect) {
    int rows = mat.size();
    int cols = mat[0].size();
    int maxCovered = 0;

    // Generate all possible combinations of numSelect columns
    for (int mask = 0; mask < (1 << cols); ++mask) {
        int count = 0;
        for (int row = 0; row < rows; ++row) {
            bool covered = false;
            for (int col = 0; col < cols; ++col) {
                if ((mask & (1 << col)) && mat[row][col] == 1) {
                    covered = true;
                    break;
                }
            }
            if (covered) count++;
        }
        // Update maxCovered if current combination covers more rows
        if (count > maxCovered && __builtin_popcount(mask) == numSelect) {
            maxCovered = count;
        }
    }
    return maxCovered;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^C \times R \times C)$ where $C$ is the number of columns and $R$ is the number of rows because we generate all possible combinations of columns and for each combination, we iterate through all rows and columns to check coverage.
> - **Space Complexity:** $O(1)$ as we do not use any additional space that scales with input size.
> - **Why these complexities occur:** The brute force approach involves generating all possible subsets of columns, which leads to an exponential time complexity due to the $2^C$ factor. The iteration through rows and columns for each subset adds linear factors of $R$ and $C$.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight for the optimal solution is to use bit manipulation to efficiently generate all possible combinations of selecting `numSelect` columns and then count the rows covered by each combination.
- Detailed breakdown:
  1. Initialize a variable to keep track of the maximum rows covered.
  2. Iterate through all possible combinations of selecting `numSelect` columns using bit manipulation.
  3. For each combination, count the number of rows that are covered (i.e., have at least one 1 in the selected columns).
  4. Update the maximum rows covered if the current combination covers more rows.

```cpp
#include <vector>
#include <algorithm>

int maxRowsCovered(std::vector<std::vector<int>>& mat, int numSelect) {
    int rows = mat.size();
    int cols = mat[0].size();
    int maxCovered = 0;

    // Generate all possible combinations of numSelect columns
    for (int mask = 0; mask < (1 << cols); ++mask) {
        if (__builtin_popcount(mask) == numSelect) {
            int count = 0;
            for (int row = 0; row < rows; ++row) {
                bool covered = false;
                for (int col = 0; col < cols; ++col) {
                    if ((mask & (1 << col)) && mat[row][col] == 1) {
                        covered = true;
                        break;
                    }
                }
                if (covered) count++;
            }
            // Update maxCovered if current combination covers more rows
            maxCovered = std::max(maxCovered, count);
        }
    }
    return maxCovered;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^C \times R \times C)$, similar to the brute force approach, because we still generate all possible combinations of columns and check each row for coverage.
> - **Space Complexity:** $O(1)$ as we do not use any additional space that scales with input size.
> - **Optimality proof:** This approach is optimal because it checks all possible combinations of selecting `numSelect` columns, ensuring that we find the maximum number of rows that can be covered. Further optimization is impossible without reducing the number of combinations to check, which would risk missing the optimal solution.

---

### Final Notes

**Learning Points:**
- **Bit Manipulation:** The problem demonstrates the use of bit manipulation to efficiently generate combinations of columns.
- **Combinatorial Optimization:** It shows how to approach problems that require finding the optimal combination of elements (in this case, columns) to maximize a certain metric (rows covered).
- **Exhaustive Search:** Sometimes, the optimal approach involves checking all possible solutions, especially when the problem space is relatively small or when an efficient algorithm to prune the search space is not apparent.

**Mistakes to Avoid:**
- **Inefficient Iteration:** Avoid iterating over all columns for each row in an inefficient manner. Instead, use bit manipulation to generate combinations and iterate through rows and columns in a structured way.
- **Missing Combinations:** Ensure that all possible combinations of selecting `numSelect` columns are considered to avoid missing the optimal solution.
- **Incorrect Counting:** Be careful when counting the number of rows covered by each combination to ensure accuracy.