## Construct 2D Grid Matching Graph Layout
**Problem Link:** https://leetcode.com/problems/construct-2d-grid-matching-graph-layout/description

**Problem Statement:**
- Input: `n`, `m`, `col`, `grid`
- Constraints: `1 <= n <= 100`, `1 <= m <= 100`, `1 <= col[i] <= m`, `grid` is a `2D` array of size `n x m`
- Expected Output: `true` if it's possible to color the grid such that each row and column has the same number of `1`s as the corresponding `col` value, and `false` otherwise
- Key Requirements:
  - Each cell in the grid can either be `0` or `1`
  - Each row and column should have the same number of `1`s as the corresponding `col` value
- Example Test Cases:
  - Input: `n = 2`, `m = 2`, `col = [1,1]`, `grid = [[1,0],[1,0]]`
    - Output: `true`
  - Input: `n = 2`, `m = 2`, `col = [1,1]`, `grid = [[1,0],[0,1]]`
    - Output: `true`
  - Input: `n = 2`, `m = 2`, `col = [1,1]`, `grid = [[0,0],[0,0]]`
    - Output: `false`

---

### Brute Force Approach

**Explanation:**
- The brute force approach involves trying all possible combinations of `0`s and `1`s in the grid
- For each combination, we check if the number of `1`s in each row and column matches the corresponding `col` value
- If we find a valid combination, we return `true`
- If we exhaust all combinations without finding a valid one, we return `false`

```cpp
#include <iostream>
#include <vector>

bool construct2DGrid(int n, int m, std::vector<int>& col, std::vector<std::vector<int>>& grid) {
    int totalOnes = 0;
    for (int i = 0; i < m; i++) {
        totalOnes += col[i];
    }
    if (totalOnes != n * m) {
        return false;
    }

    std::vector<std::vector<int>> result(n, std::vector<int>(m, 0));

    // Generate all possible combinations
    std::vector<std::vector<int>> combinations;
    generateCombinations(n, m, combinations);

    for (const auto& combination : combinations) {
        // Check if the current combination matches the col values
        if (isValidCombination(combination, col, n, m)) {
            return true;
        }
    }

    return false;
}

void generateCombinations(int n, int m, std::vector<std::vector<int>>& combinations) {
    std::vector<int> currentCombination(n * m, 0);
    generateCombinationsRecursive(n, m, 0, currentCombination, combinations);
}

void generateCombinationsRecursive(int n, int m, int index, std::vector<int>& currentCombination, std::vector<std::vector<int>>& combinations) {
    if (index == n * m) {
        combinations.push_back(currentCombination);
        return;
    }

    currentCombination[index] = 0;
    generateCombinationsRecursive(n, m, index + 1, currentCombination, combinations);

    currentCombination[index] = 1;
    generateCombinationsRecursive(n, m, index + 1, currentCombination, combinations);
}

bool isValidCombination(const std::vector<int>& combination, const std::vector<int>& col, int n, int m) {
    for (int i = 0; i < m; i++) {
        int count = 0;
        for (int j = 0; j < n; j++) {
            if (combination[j * m + i] == 1) {
                count++;
            }
        }
        if (count != col[i]) {
            return false;
        }
    }

    for (int i = 0; i < n; i++) {
        int count = 0;
        for (int j = 0; j < m; j++) {
            if (combination[i * m + j] == 1) {
                count++;
            }
        }
        if (count != col[i % m]) {
            return false;
        }
    }

    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{n \cdot m})$ due to generating all possible combinations of `0`s and `1`s in the grid
> - **Space Complexity:** $O(2^{n \cdot m})$ for storing all combinations
> - **Why these complexities occur:** The brute force approach tries all possible combinations, resulting in exponential time and space complexity

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves using a backtracking algorithm to construct the grid
- We start by initializing an empty grid and then try to fill it with `0`s and `1`s
- For each cell, we check if placing a `0` or a `1` would lead to a valid solution
- If placing a `0` or a `1` would not lead to a valid solution, we backtrack and try the other option

```cpp
#include <iostream>
#include <vector>

bool construct2DGrid(int n, int m, std::vector<int>& col, std::vector<std::vector<int>>& grid) {
    int totalOnes = 0;
    for (int i = 0; i < m; i++) {
        totalOnes += col[i];
    }
    if (totalOnes != n * m) {
        return false;
    }

    std::vector<std::vector<int>> result(n, std::vector<int>(m, 0));

    if (!backtrack(result, col, 0, 0)) {
        return false;
    }

    grid = result;
    return true;
}

bool backtrack(std::vector<std::vector<int>>& grid, const std::vector<int>& col, int row, int colIndex) {
    if (row == grid.size()) {
        return true;
    }

    if (colIndex == grid[0].size()) {
        return backtrack(grid, col, row + 1, 0);
    }

    for (int val = 0; val <= 1; val++) {
        if (isValidMove(grid, col, row, colIndex, val)) {
            grid[row][colIndex] = val;
            if (backtrack(grid, col, row, colIndex + 1)) {
                return true;
            }
            grid[row][colIndex] = 0;
        }
    }

    return false;
}

bool isValidMove(const std::vector<std::vector<int>>& grid, const std::vector<int>& col, int row, int colIndex, int val) {
    int rowOnes = 0;
    for (int i = 0; i < grid[0].size(); i++) {
        if (grid[row][i] == 1) {
            rowOnes++;
        }
    }

    if (val == 1) {
        rowOnes++;
    }

    if (rowOnes > col[row % col.size()]) {
        return false;
    }

    int colOnes = 0;
    for (int i = 0; i < grid.size(); i++) {
        if (grid[i][colIndex] == 1) {
            colOnes++;
        }
    }

    if (val == 1) {
        colOnes++;
    }

    if (colOnes > col[colIndex]) {
        return false;
    }

    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot 2^{n \cdot m})$ due to the backtracking algorithm
> - **Space Complexity:** $O(n \cdot m)$ for the grid and the recursion stack
> - **Optimality proof:** The backtracking algorithm tries all possible combinations of `0`s and `1`s in the grid, ensuring that all possible solutions are explored. The `isValidMove` function ensures that the algorithm only explores valid solutions, reducing the search space.

---

### Final Notes

**Learning Points:**
- The importance of validating input and handling edge cases
- The use of backtracking algorithms to solve complex problems
- The need to optimize solutions to reduce time and space complexity

**Mistakes to Avoid:**
- Not validating input and handling edge cases
- Not optimizing solutions to reduce time and space complexity
- Not using backtracking algorithms to solve complex problems

By following the optimal approach, we can construct a 2D grid matching the graph layout in an efficient manner. The backtracking algorithm ensures that all possible solutions are explored, and the `isValidMove` function reduces the search space by only exploring valid solutions.