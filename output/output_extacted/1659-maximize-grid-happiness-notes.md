## Maximize Grid Happiness

**Problem Link:** https://leetcode.com/problems/maximize-grid-happiness/description

**Problem Statement:**
- Input format and constraints: The problem takes as input an integer `m` representing the number of rows in the grid, an integer `n` representing the number of columns in the grid, and an integer `introvert` representing the number of introverts.
- Expected output format: The output is the maximum possible happiness of the grid.
- Key requirements and edge cases to consider: The grid must be filled with either introverts or extroverts, and the happiness of each cell depends on the type of person and the number of neighboring people of the same type.
- Example test cases with explanations: For example, if we have a 2x2 grid and 2 introverts, the maximum happiness can be achieved by placing the introverts in the corners of the grid.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to try all possible combinations of placing introverts and extroverts in the grid.
- Step-by-step breakdown of the solution: 
  1. Generate all possible combinations of placing `introvert` introverts in the `m * n` grid.
  2. For each combination, calculate the happiness of each cell based on the number of neighboring people of the same type.
  3. Calculate the total happiness of the grid by summing up the happiness of all cells.
  4. Keep track of the maximum happiness found among all combinations.

```cpp
#include <iostream>
#include <vector>

int maxHappiness(int m, int n, int introvert) {
    int max_happiness = 0;
    // Generate all possible combinations
    for (int mask = 0; mask < (1 << (m * n)); mask++) {
        int current_happiness = 0;
        std::vector<std::vector<int>> grid(m, std::vector<int>(n, 0));
        int introvert_count = 0;
        // Create the grid based on the current combination
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if ((mask & (1 << (i * n + j))) != 0) {
                    grid[i][j] = -1; // introvert
                    introvert_count++;
                } else {
                    grid[i][j] = 1; // extrovert
                }
            }
        }
        // Check if the current combination has the correct number of introverts
        if (introvert_count == introvert) {
            // Calculate the happiness of each cell
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    int neighboring_same_type = 0;
                    if (i > 0 && grid[i - 1][j] == grid[i][j]) neighboring_same_type++;
                    if (i < m - 1 && grid[i + 1][j] == grid[i][j]) neighboring_same_type++;
                    if (j > 0 && grid[i][j - 1] == grid[i][j]) neighboring_same_type++;
                    if (j < n - 1 && grid[i][j + 1] == grid[i][j]) neighboring_same_type++;
                    if (grid[i][j] == -1) {
                        current_happiness += 120 - 30 * neighboring_same_type;
                    } else {
                        current_happiness += 40 + 20 * neighboring_same_type;
                    }
                }
            }
            // Update the maximum happiness
            max_happiness = std::max(max_happiness, current_happiness);
        }
    }
    return max_happiness;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{m \cdot n})$, which is the number of possible combinations of placing introverts and extroverts in the grid.
> - **Space Complexity:** $O(m \cdot n)$, which is the space needed to store the grid.
> - **Why these complexities occur:** The brute force approach tries all possible combinations, resulting in an exponential time complexity. The space complexity is linear because we only need to store the current grid.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution can be achieved by using dynamic programming to store the maximum happiness for each subproblem.
- Detailed breakdown of the approach: 
  1. Initialize a 2D array `dp` of size `(m * n + 1) x (introvert + 1)` to store the maximum happiness for each subproblem.
  2. Fill up the `dp` array in a bottom-up manner by considering each cell in the grid and trying both possibilities (introvert and extrovert).
  3. For each cell, calculate the maximum happiness by considering the neighboring cells and the type of person (introvert or extrovert).
  4. The final answer is stored in `dp[m * n][introvert]`.

```cpp
int maxHappiness(int m, int n, int introvert) {
    std::vector<std::vector<int>> dp(m * n + 1, std::vector<int>(introvert + 1, -1));
    return dfs(0, 0, m, n, introvert, dp);
}

int dfs(int index, int introvert_count, int m, int n, int introvert, std::vector<std::vector<int>>& dp) {
    if (index == m * n) {
        if (introvert_count == introvert) {
            return 0;
        } else {
            return -1000000;
        }
    }
    if (dp[index][introvert_count] != -1) {
        return dp[index][introvert_count];
    }
    int max_happiness = -1000000;
    // Try introvert
    if (introvert_count < introvert) {
        int neighboring_same_type = 0;
        if (index > n) neighboring_same_type += (index - n >= 0 && (index - n) % n == (index % n)) ? 1 : 0;
        if (index > 0 && index % n != 0) neighboring_same_type += (index - 1) % n == index % n ? 1 : 0;
        max_happiness = std::max(max_happiness, 120 - 30 * neighboring_same_type + dfs(index + 1, introvert_count + 1, m, n, introvert, dp));
    }
    // Try extrovert
    {
        int neighboring_same_type = 0;
        if (index > n) neighboring_same_type += (index - n >= 0 && (index - n) % n == (index % n)) ? 1 : 0;
        if (index > 0 && index % n != 0) neighboring_same_type += (index - 1) % n == index % n ? 1 : 0;
        max_happiness = std::max(max_happiness, 40 + 20 * neighboring_same_type + dfs(index + 1, introvert_count, m, n, introvert, dp));
    }
    dp[index][introvert_count] = max_happiness;
    return max_happiness;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot introvert)$, which is the number of subproblems in the dynamic programming approach.
> - **Space Complexity:** $O(m \cdot n \cdot introvert)$, which is the space needed to store the `dp` array.
> - **Optimality proof:** The dynamic programming approach ensures that we consider all possible combinations of placing introverts and extroverts in the grid, and we store the maximum happiness for each subproblem to avoid redundant calculations. This approach guarantees the optimal solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, backtracking, and bit manipulation.
- Problem-solving patterns identified: The problem requires considering all possible combinations of placing introverts and extroverts in the grid, and calculating the maximum happiness for each combination.
- Optimization techniques learned: The dynamic programming approach helps to avoid redundant calculations and reduce the time complexity.
- Similar problems to practice: Other problems that involve dynamic programming, backtracking, and bit manipulation, such as the **N-Queens** problem and the **Partition Equal Subset Sum** problem.

**Mistakes to Avoid:**
- Common implementation errors: Not considering all possible combinations of placing introverts and extroverts in the grid, or not calculating the maximum happiness correctly.
- Edge cases to watch for: The case where the number of introverts is 0 or the number of extroverts is 0.
- Performance pitfalls: Not using dynamic programming to store the maximum happiness for each subproblem, resulting in redundant calculations and a high time complexity.
- Testing considerations: Testing the solution with different inputs, including edge cases, to ensure that it produces the correct output.