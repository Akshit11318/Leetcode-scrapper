## Reconstruct a 2-Row Binary Matrix
**Problem Link:** https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/description

**Problem Statement:**
- Input: `num` - The number of columns in the matrix.
- `collimits` - A list of two integers, where the first integer is the maximum number of columns that can have a 1 in the first row, and the second integer is the maximum number of columns that can have a1 in the second row.
- Expected output: A 2D list of size 2 x `num` representing the reconstructed binary matrix.
- Key requirements: 
    1. Each row must have at most `collimits[i]` 1s.
    2. No column should have more than one 1.
- Edge cases:
    1. If it's impossible to reconstruct the matrix, return an empty list.
    2. If there are multiple possible reconstructions, return any of them.

### Brute Force Approach

**Explanation:**
- The brute force approach involves generating all possible binary matrices of size 2 x `num`.
- Then, for each matrix, check if it satisfies the given conditions: each row has at most `collimits[i]` 1s, and no column has more than one 1.
- If a matrix satisfies these conditions, return it as the reconstructed matrix.

```cpp
#include <vector>
#include <iostream>

std::vector<std::vector<int>> reconstructMatrix(int num, std::vector<int>& collimits) {
    int maxOnesInFirstRow = collimits[0];
    int maxOnesInSecondRow = collimits[1];

    // Generate all possible binary matrices of size 2 x num
    for (int mask = 0; mask < (1 << (2 * num)); mask++) {
        std::vector<std::vector<int>> matrix(2, std::vector<int>(num));
        int onesInFirstRow = 0;
        int onesInSecondRow = 0;

        // Convert the current mask to a binary matrix
        for (int i = 0; i < num; i++) {
            matrix[0][i] = (mask >> (2 * i)) & 1;
            matrix[1][i] = (mask >> (2 * i + 1)) & 1;

            // Count the number of 1s in each row
            onesInFirstRow += matrix[0][i];
            onesInSecondRow += matrix[1][i];
        }

        // Check if the current matrix satisfies the conditions
        if (onesInFirstRow <= maxOnesInFirstRow && onesInSecondRow <= maxOnesInSecondRow) {
            bool valid = true;
            for (int i = 0; i < num; i++) {
                if (matrix[0][i] == 1 && matrix[1][i] == 1) {
                    valid = false;
                    break;
                }
            }

            if (valid) {
                return matrix;
            }
        }
    }

    // If no valid matrix is found, return an empty list
    return {};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{2n})$ where n is the number of columns. This is because we are generating all possible binary matrices of size 2 x n.
> - **Space Complexity:** $O(n)$ for storing the current matrix.
> - **Why these complexities occur:** The brute force approach involves generating all possible binary matrices, which results in exponential time complexity. The space complexity is linear because we only need to store the current matrix.

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves using a greedy strategy to construct the matrix.
- We start by filling the first row with 1s until we reach the maximum allowed number of 1s in the first row (`collimits[0]`).
- Then, we fill the second row with 1s until we reach the maximum allowed number of 1s in the second row (`collimits[1]`).
- We make sure that no column has more than one 1 by checking if the current column already has a 1 in the first row before placing a 1 in the second row.

```cpp
std::vector<std::vector<int>> reconstructMatrix(int num, std::vector<int>& collimits) {
    std::vector<std::vector<int>> matrix(2, std::vector<int>(num, 0));
    int onesInFirstRow = 0;
    int onesInSecondRow = 0;

    for (int i = 0; i < num; i++) {
        if (onesInFirstRow < collimits[0]) {
            matrix[0][i] = 1;
            onesInFirstRow++;
        } else if (onesInSecondRow < collimits[1]) {
            matrix[1][i] = 1;
            onesInSecondRow++;
        } else {
            return {}; // If we can't place any more 1s, return an empty list
        }
    }

    return matrix;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where n is the number of columns. This is because we are iterating over each column once.
> - **Space Complexity:** $O(n)$ for storing the matrix.
> - **Optimality proof:** This approach is optimal because it uses a greedy strategy to construct the matrix, ensuring that we place the maximum number of 1s in each row while satisfying the conditions.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: greedy strategy, bit manipulation.
- Problem-solving patterns identified: using a greedy approach to construct a matrix.
- Optimization techniques learned: avoiding unnecessary iterations, using bit manipulation to generate all possible binary matrices.

**Mistakes to Avoid:**
- Common implementation errors: not checking if the current column already has a 1 in the first row before placing a 1 in the second row.
- Edge cases to watch for: returning an empty list if it's impossible to reconstruct the matrix.
- Performance pitfalls: using an exponential time complexity approach when a linear time complexity approach is possible.
- Testing considerations: testing the function with different inputs, including edge cases.