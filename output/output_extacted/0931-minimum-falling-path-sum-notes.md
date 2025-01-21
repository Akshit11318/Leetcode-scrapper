## Minimum Falling Path Sum
**Problem Link:** https://leetcode.com/problems/minimum-falling-path-sum/description

**Problem Statement:**
- Given a square array of integers `arr` of size `n x n`, where `n >= 2`.
- The task is to find the minimum falling path sum.
- A falling path is defined as a path from any element in the first row to any element in the last row, such that for each element in the path, the next element is either directly below it or below and to the left or right of it.
- The sum of all elements in the path is the falling path sum.

**Expected Output Format:**
- The minimum falling path sum.

**Key Requirements and Edge Cases to Consider:**
- The input array `arr` is guaranteed to be a square array of size `n x n`, where `n >= 2`.
- The array may contain negative numbers.
- The minimum falling path sum should be calculated considering all possible paths.

**Example Test Cases with Explanations:**
- For the input `arr = [[2,1,3],[6,5,4],[7,8,9]]`, the minimum falling path sum is `13`.
- For the input `arr = [[100,-42,-46,-41],[31,97,10,-10],[-58,-51,82,89],[51,81,69,-51]]`, the minimum falling path sum is `-36`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible paths from the first row to the last row and calculate the sum of each path.
- This approach comes to mind first because it directly addresses the problem statement by considering all possible paths.

```cpp
int minFallingPathSum(vector<vector<int>>& arr) {
    int n = arr.size();
    int minSum = INT_MAX;

    // Function to calculate the sum of a path
    function<int(int, int)> dfs = [&](int row, int col) {
        if (row == n - 1) return arr[row][col];

        int sum = INT_MAX;
        for (int i = -1; i <= 1; i++) {
            int newCol = col + i;
            if (newCol >= 0 && newCol < n) {
                sum = min(sum, arr[row][col] + dfs(row + 1, newCol));
            }
        }
        return sum;
    };

    // Try all possible paths from the first row
    for (int i = 0; i < n; i++) {
        minSum = min(minSum, dfs(0, i));
    }

    return minSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(3^n)$, where $n$ is the size of the input array. This is because in the worst case, we are trying all possible paths from the first row to the last row, and each path can branch out in three different ways (left, straight, right).
> - **Space Complexity:** $O(n)$, where $n$ is the size of the input array. This is because of the recursive call stack.
> - **Why these complexities occur:** These complexities occur because the brute force approach tries all possible paths, which leads to an exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use dynamic programming to store the minimum falling path sum up to each cell.
- We can calculate the minimum falling path sum up to each cell in the current row by considering the minimum falling path sum up to the cells in the previous row that are directly above, above-left, and above-right of the current cell.

```cpp
int minFallingPathSum(vector<vector<int>>& arr) {
    int n = arr.size();

    // Create a copy of the input array to store the minimum falling path sum up to each cell
    vector<vector<int>> dp = arr;

    // Calculate the minimum falling path sum up to each cell in the current row
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int sum = INT_MAX;
            for (int k = -1; k <= 1; k++) {
                int newJ = j + k;
                if (newJ >= 0 && newJ < n) {
                    sum = min(sum, dp[i - 1][newJ]);
                }
            }
            dp[i][j] = arr[i][j] + sum;
        }
    }

    // Find the minimum falling path sum up to any cell in the last row
    int minSum = INT_MAX;
    for (int i = 0; i < n; i++) {
        minSum = min(minSum, dp[n - 1][i]);
    }

    return minSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the input array. This is because we are iterating over the input array once to calculate the minimum falling path sum up to each cell.
> - **Space Complexity:** $O(n^2)$, where $n$ is the size of the input array. This is because we are storing the minimum falling path sum up to each cell in a separate array.
> - **Optimality proof:** This is the optimal solution because we are using dynamic programming to avoid redundant calculations and store the minimum falling path sum up to each cell.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, memoization.
- Problem-solving patterns identified: breaking down the problem into smaller sub-problems, using a bottom-up approach to solve the problem.
- Optimization techniques learned: avoiding redundant calculations, using a separate array to store the minimum falling path sum up to each cell.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases correctly, not initializing the dynamic programming array correctly.
- Edge cases to watch for: handling the first row and last row correctly, handling the boundary cells correctly.
- Performance pitfalls: using a brute force approach, not using dynamic programming to avoid redundant calculations.
- Testing considerations: testing the solution with different input sizes, testing the solution with different input values.