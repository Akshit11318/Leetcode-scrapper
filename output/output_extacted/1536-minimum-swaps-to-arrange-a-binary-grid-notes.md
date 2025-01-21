## Minimum Swaps to Arrange a Binary Grid

**Problem Link:** https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/description

**Problem Statement:**
- Input: A binary grid `grid` of size `n x n`, where `grid[i][j]` is either 0 or 1.
- Constraints: `1 <= n <= 5`, `grid.length == n`, `grid[i].length == n`.
- Expected Output: The minimum number of swaps required to arrange the grid such that the top row is filled with zeros, the second row is filled with zeros except for the last column, the third row is filled with zeros except for the last two columns, and so on.
- Key Requirements: Find the minimum number of swaps to achieve the desired arrangement.
- Edge Cases: If it's impossible to achieve the desired arrangement, return -1.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible swaps and check if the desired arrangement can be achieved.
- Step-by-step breakdown:
  1. Generate all possible permutations of the grid rows.
  2. For each permutation, check if the desired arrangement can be achieved by swapping rows.
  3. If the desired arrangement can be achieved, count the number of swaps required.
  4. Return the minimum number of swaps required among all permutations.

```cpp
#include <vector>
#include <algorithm>

int minSwaps(std::vector<std::vector<int>>& grid) {
    int n = grid.size();
    int min_swaps = INT_MAX;

    // Generate all permutations of grid rows
    std::vector<int> rows(n);
    for (int i = 0; i < n; i++) rows[i] = i;
    do {
        int swaps = 0;
        std::vector<std::vector<int>> temp_grid = grid;

        // Check if the desired arrangement can be achieved by swapping rows
        for (int i = 0; i < n; i++) {
            int target_row = rows[i];
            int required_zeros = n - i - 1;

            // Count the number of zeros in the current row
            int zeros = 0;
            for (int j = 0; j < required_zeros; j++) {
                if (temp_grid[target_row][j] == 0) zeros++;
            }

            // If the number of zeros is less than required, try swapping rows
            if (zeros < required_zeros) {
                bool swapped = false;
                for (int k = i + 1; k < n; k++) {
                    int zeros_in_k = 0;
                    for (int j = 0; j < required_zeros; j++) {
                        if (temp_grid[rows[k]][j] == 0) zeros_in_k++;
                    }
                    if (zeros_in_k >= required_zeros) {
                        // Swap rows
                        std::swap(rows[i], rows[k]);
                        swaps++;
                        swapped = true;
                        break;
                    }
                }
                if (!swapped) break; // Desired arrangement cannot be achieved
            }
        }

        // Update the minimum number of swaps required
        if (swaps < min_swaps) min_swaps = swaps;
    } while (std::next_permutation(rows.begin(), rows.end()));

    return min_swaps == INT_MAX ? -1 : min_swaps;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n^2)$, where $n$ is the size of the grid. This is because we generate all permutations of the grid rows and check if the desired arrangement can be achieved for each permutation.
> - **Space Complexity:** $O(n^2)$, where $n$ is the size of the grid. This is because we need to store the temporary grid and the permutation of rows.
> - **Why these complexities occur:** The time complexity is high because we try all possible permutations of the grid rows, and for each permutation, we check if the desired arrangement can be achieved by swapping rows. The space complexity is moderate because we need to store the temporary grid and the permutation of rows.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a greedy approach. We start from the top row and try to find a row that has the maximum number of zeros in the required positions. If such a row is found, we swap it with the current row and move to the next row.
- Detailed breakdown of the approach:
  1. Initialize the minimum number of swaps required to 0.
  2. Iterate over each row in the grid.
  3. For each row, find the row that has the maximum number of zeros in the required positions.
  4. If such a row is found, swap it with the current row and increment the minimum number of swaps required.
  5. Repeat steps 3-4 until the desired arrangement is achieved or it is impossible to achieve the desired arrangement.

```cpp
int minSwaps(std::vector<std::vector<int>>& grid) {
    int n = grid.size();
    int min_swaps = 0;

    for (int i = 0; i < n; i++) {
        int required_zeros = n - i - 1;
        int max_zeros = -1;
        int max_zeros_row = -1;

        // Find the row that has the maximum number of zeros in the required positions
        for (int j = i; j < n; j++) {
            int zeros = 0;
            for (int k = 0; k < required_zeros; k++) {
                if (grid[j][k] == 0) zeros++;
            }
            if (zeros > max_zeros) {
                max_zeros = zeros;
                max_zeros_row = j;
            }
        }

        // If no row has the required number of zeros, return -1
        if (max_zeros < required_zeros) return -1;

        // Swap the row with the maximum number of zeros with the current row
        if (max_zeros_row != i) {
            std::swap(grid[i], grid[max_zeros_row]);
            min_swaps++;
        }
    }

    return min_swaps;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the grid. This is because we iterate over each row in the grid and find the row that has the maximum number of zeros in the required positions.
> - **Space Complexity:** $O(1)$, where $n$ is the size of the grid. This is because we only need to store the minimum number of swaps required and the current row index.
> - **Optimality proof:** The greedy approach ensures that we always choose the row that has the maximum number of zeros in the required positions, which minimizes the number of swaps required to achieve the desired arrangement.

---

### Final Notes

**Learning Points:**
- The problem requires finding the minimum number of swaps to arrange a binary grid in a specific way.
- The brute force approach tries all possible permutations of the grid rows, which has a high time complexity.
- The optimal approach uses a greedy approach to find the row that has the maximum number of zeros in the required positions and swaps it with the current row.
- The time complexity of the optimal approach is $O(n^2)$, where $n$ is the size of the grid.

**Mistakes to Avoid:**
- Not checking if the desired arrangement can be achieved before trying to find the minimum number of swaps.
- Not using a greedy approach to find the row that has the maximum number of zeros in the required positions.
- Not swapping the row with the maximum number of zeros with the current row if it is not already in the correct position.