## Unique Paths
**Problem Link:** https://leetcode.com/problems/unique-paths/description

**Problem Statement:**
- Input format and constraints: The problem takes two integers `m` and `n` as input, representing the number of rows and columns in a grid. The goal is to find the number of unique paths from the top-left corner to the bottom-right corner.
- Expected output format: The output should be an integer representing the number of unique paths.
- Key requirements and edge cases to consider: The grid has obstacles or not, but in this problem, there are no obstacles. The grid size is within the range [1, 100].
- Example test cases with explanations: 
    - Example 1: `m = 3`, `n = 7`, the output should be `28`. This is because there are 28 unique paths from the top-left corner to the bottom-right corner in a 3x7 grid.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we can think of it as a series of choices. At each step, we can either move down or right. We can use recursion to explore all possible paths.
- Step-by-step breakdown of the solution: 
    1. Start at the top-left corner.
    2. If we are at the bottom-right corner, return 1 (we have found a unique path).
    3. Otherwise, try moving down and right, and recursively count the number of unique paths from the new position.
- Why this approach comes to mind first: This approach is intuitive because it directly models the problem statement. However, it is not efficient due to the repeated computation of the same subproblems.

```cpp
class Solution {
public:
    int uniquePaths(int m, int n) {
        return dfs(1, 1, m, n);
    }

    int dfs(int x, int y, int m, int n) {
        if (x == m && y == n) {
            return 1;
        }
        int count = 0;
        if (x < m) {
            count += dfs(x + 1, y, m, n);
        }
        if (y < n) {
            count += dfs(x, y + 1, m, n);
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{m+n-2})$, where $m$ and $n$ are the number of rows and columns. This is because in the worst case, we have to explore all possible paths, which is exponential in the size of the input.
> - **Space Complexity:** $O(m+n-2)$, due to the recursion stack.
> - **Why these complexities occur:** The brute force approach has high time complexity due to the repeated computation of the same subproblems. The space complexity is due to the recursion stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem has overlapping subproblems, which can be solved using dynamic programming. We can build a table `dp` where `dp[i][j]` represents the number of unique paths from the top-left corner to the cell at position `(i, j)`.
- Detailed breakdown of the approach: 
    1. Initialize a table `dp` of size `m x n` with all elements set to 0.
    2. Fill the first row and first column with 1, because there is only one way to reach each cell in the first row and first column.
    3. Fill the rest of the table using the recurrence relation `dp[i][j] = dp[i-1][j] + dp[i][j-1]`.
- Proof of optimality: The dynamic programming approach is optimal because it avoids the repeated computation of the same subproblems, reducing the time complexity to polynomial.

```cpp
class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> dp(m, vector<int>(n, 0));
        for (int i = 0; i < m; i++) {
            dp[i][0] = 1;
        }
        for (int j = 0; j < n; j++) {
            dp[0][j] = 1;
        }
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        return dp[m-1][n-1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the number of rows and columns. This is because we need to fill the table `dp` of size `m x n`.
> - **Space Complexity:** $O(m \cdot n)$, due to the table `dp`.
> - **Optimality proof:** The dynamic programming approach is optimal because it avoids the repeated computation of the same subproblems, reducing the time complexity to polynomial.

---

### Alternative Approach

**Explanation:**
- Different perspective or technique: The problem can also be solved using combinatorics. The number of unique paths from the top-left corner to the bottom-right corner is equal to the number of ways to choose `m-1` steps down from a total of `m+n-2` steps.
- Unique trade-offs: The combinatorial approach has a time complexity of $O(m+n)$, but it requires the use of a large integer data type to handle the large values of the binomial coefficient.
- Scenarios where this approach might be preferred: The combinatorial approach is preferred when the input size is large and the time complexity is critical.

```cpp
class Solution {
public:
    int uniquePaths(int m, int n) {
        long long res = 1;
        for (int i = 1; i <= m - 1; i++) {
            res = res * (n + i - 1) / i;
        }
        return res;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m+n)$, where $m$ and $n$ are the number of rows and columns. This is because we need to calculate the binomial coefficient.
> - **Space Complexity:** $O(1)$, because we only need a constant amount of space to store the result.
> - **Trade-off analysis:** The combinatorial approach has a better time complexity than the dynamic programming approach, but it requires the use of a large integer data type and has a higher constant factor.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, combinatorics.
- Problem-solving patterns identified: Overlapping subproblems, combinatorial problems.
- Optimization techniques learned: Memoization, dynamic programming.
- Similar problems to practice: Unique Paths II, Minimum Path Sum.

**Mistakes to Avoid:**
- Common implementation errors: Off-by-one errors, incorrect initialization of the table.
- Edge cases to watch for: Input size is 1, input size is large.
- Performance pitfalls: Repeated computation of the same subproblems, use of large integer data type.
- Testing considerations: Test the function with different input sizes, test the function with edge cases.