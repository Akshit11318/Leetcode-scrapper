## Number of Ways of Cutting a Pizza

**Problem Link:** https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/description

**Problem Statement:**
- Input format and constraints: The input is a 2D grid `pizza` representing the pizza, where `'A'` represents an apple and `'.'` represents an empty space. The constraints are that the grid is not empty and the number of rows and columns are within the range `[1, 10]`.
- Expected output format: The output is the number of ways to cut the pizza into `k` pieces such that each piece contains at least one apple.
- Key requirements and edge cases to consider: The pizza can be cut in any direction (horizontally or vertically) and each cut must be a straight line.
- Example test cases with explanations:
  - Input: `pizza = ["A..", "AAA", "..."]`, `k = 3`
    - Output: `3`
    - Explanation: There are three ways to cut the pizza into three pieces such that each piece contains at least one apple.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves generating all possible ways to cut the pizza and then checking each way to see if it satisfies the condition of each piece containing at least one apple.
- Step-by-step breakdown of the solution:
  1. Generate all possible ways to cut the pizza.
  2. For each way, check if each piece contains at least one apple.
  3. Count the number of ways that satisfy the condition.
- Why this approach comes to mind first: It is a straightforward and intuitive approach that involves trying all possible solutions and checking if they satisfy the condition.

```cpp
int ways(int row, int col, int k, vector<vector<char>>& pizza) {
    if (k == 1) {
        for (int i = row; i < pizza.size(); i++) {
            for (int j = col; j < pizza[0].size(); j++) {
                if (pizza[i][j] == 'A') return 1;
            }
        }
        return 0;
    }

    int count = 0;
    for (int i = row; i < pizza.size(); i++) {
        for (int j = col; j < pizza[0].size(); j++) {
            if (pizza[i][j] == 'A') {
                count += ways(row, j + 1, k - 1, pizza);
                count += ways(i + 1, col, k - 1, pizza);
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{m \cdot n})$ where $m$ and $n$ are the number of rows and columns in the pizza grid. This is because in the worst case, we are generating all possible ways to cut the pizza.
> - **Space Complexity:** $O(m \cdot n)$ for the recursive call stack.
> - **Why these complexities occur:** The brute force approach involves trying all possible solutions, which leads to an exponential time complexity. The space complexity is due to the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using dynamic programming and memoization. We can use a 3D DP array to store the number of ways to cut the pizza into `k` pieces for each sub-grid.
- Detailed breakdown of the approach:
  1. Initialize a 3D DP array `dp` with dimensions `(m + 1) x (n + 1) x (k + 1)` where `m` and `n` are the number of rows and columns in the pizza grid.
  2. For each sub-grid, calculate the number of ways to cut the pizza into `k` pieces.
  3. Use memoization to store the results of sub-problems to avoid redundant calculations.
- Proof of optimality: The optimal solution has a time complexity of $O(m \cdot n \cdot k)$, which is much better than the brute force approach.

```cpp
int ways(vector<string>& pizza, int k) {
    int m = pizza.size(), n = pizza[0].size();
    vector<vector<vector<int>>> dp(m + 1, vector<vector<int>>(n + 1, vector<int>(k + 1, 0)));
    vector<vector<int>> prefix(m + 1, vector<int>(n + 1, 0));

    // Calculate prefix sum
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + (pizza[i - 1][j - 1] == 'A');
        }
    }

    // Calculate dp values
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            dp[i][j][1] = prefix[i][j] > 0;
        }
    }

    for (int p = 2; p <= k; p++) {
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                for (int x = 1; x < i; x++) {
                    dp[i][j][p] += dp[x][j][p - 1] * (prefix[i][j] - prefix[x][j] > 0);
                }
                for (int y = 1; y < j; y++) {
                    dp[i][j][p] += dp[i][y][p - 1] * (prefix[i][j] - prefix[i][y] > 0);
                }
            }
        }
    }

    return dp[m][n][k];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot k)$ where $m$ and $n$ are the number of rows and columns in the pizza grid.
> - **Space Complexity:** $O(m \cdot n \cdot k)$ for the DP array.
> - **Optimality proof:** The optimal solution has a time complexity of $O(m \cdot n \cdot k)$, which is much better than the brute force approach. The space complexity is also much better than the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming and memoization.
- Problem-solving patterns identified: The problem can be solved using a 3D DP array to store the number of ways to cut the pizza into `k` pieces for each sub-grid.
- Optimization techniques learned: Memoization can be used to store the results of sub-problems to avoid redundant calculations.
- Similar problems to practice: Other problems that can be solved using dynamic programming and memoization.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the DP array correctly, not using memoization correctly.
- Edge cases to watch for: The pizza grid can be empty, the number of rows and columns can be 1.
- Performance pitfalls: Not using memoization can lead to redundant calculations and a high time complexity.
- Testing considerations: Test the solution with different inputs, including edge cases.