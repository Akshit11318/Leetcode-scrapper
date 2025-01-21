## Minimum Cost Tree From Leaf Values

**Problem Link:** https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/description

**Problem Statement:**
- Input: An array of integers `arr` representing the leaf values of a binary tree.
- Output: The minimum cost to construct a binary tree from the given leaf values.
- Key requirements and edge cases to consider:
  - The input array `arr` will have at least two elements.
  - The constructed binary tree should have the given leaf values.
  - The cost of constructing a binary tree is the sum of the product of the two smallest numbers in each node.
- Example test cases with explanations:
  - For `arr = [6, 2, 4]`, the minimum cost is `32`. The binary tree can be constructed as follows:
    - Create a node with value `2` and `4`, with a cost of `2 * 4 = 8`.
    - Create a node with value `6` and the previously created node, with a cost of `6 * (2 + 4) = 36 - 8 = 28`.
    - The total cost is `8 + 28 = 36 - 4 = 32`.

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the minimum cost, we can try all possible ways to construct the binary tree.
- Step-by-step breakdown of the solution:
  1. Generate all possible binary trees from the given leaf values.
  2. Calculate the cost of each tree by summing the product of the two smallest numbers in each node.
  3. Return the minimum cost among all trees.
- Why this approach comes to mind first: It's a straightforward approach to try all possible solutions and select the best one.

```cpp
class Solution {
public:
    int mctFromLeafValues(vector<int>& arr) {
        int n = arr.size();
        vector<vector<int>> dp(n, vector<int>(n, 0));
        for (int i = 0; i < n; i++) {
            dp[i][i] = 0;
        }
        for (int len = 2; len <= n; len++) {
            for (int i = 0; i <= n - len; i++) {
                int j = i + len - 1;
                dp[i][j] = INT_MAX;
                for (int k = i; k < j; k++) {
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + max(arr[i], max(arr[k + 1], arr[j])));
                }
            }
        }
        return dp[0][n - 1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of leaf values. This is because we have three nested loops: two for iterating over the leaf values and one for trying all possible splits.
> - **Space Complexity:** $O(n^2)$, where $n$ is the number of leaf values. This is because we need a 2D array to store the minimum cost for each subarray.
> - **Why these complexities occur:** The brute force approach has high time and space complexities due to the nested loops and the need to store the minimum cost for each subarray.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to store the minimum cost for each subarray and avoid redundant calculations.
- Detailed breakdown of the approach:
  1. Initialize a 2D array `dp` to store the minimum cost for each subarray.
  2. Iterate over the leaf values and fill the `dp` array using the following recurrence relation: `dp[i][j] = min(dp[i][k] + dp[k + 1][j] + max(arr[i], max(arr[k + 1], arr[j])))` for all `i <= k < j`.
  3. Return the minimum cost stored in `dp[0][n - 1]`.
- Proof of optimality: This approach is optimal because it uses dynamic programming to avoid redundant calculations and has a time complexity of $O(n^3)$, which is the best possible time complexity for this problem.

```cpp
class Solution {
public:
    int mctFromLeafValues(vector<int>& arr) {
        int n = arr.size();
        vector<vector<int>> dp(n, vector<int>(n, 0));
        vector<int> max_val(n, 0);
        for (int i = 0; i < n; i++) {
            max_val[i] = arr[i];
        }
        for (int len = 2; len <= n; len++) {
            for (int i = 0; i <= n - len; i++) {
                int j = i + len - 1;
                dp[i][j] = INT_MAX;
                for (int k = i; k < j; k++) {
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + max(max_val[i], max_val[k + 1]));
                }
                max_val[i] = max(max_val[i], arr[j]);
            }
        }
        return dp[0][n - 1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of leaf values.
> - **Space Complexity:** $O(n^2)$, where $n$ is the number of leaf values.
> - **Optimality proof:** This approach is optimal because it uses dynamic programming to avoid redundant calculations and has a time complexity of $O(n^3)$, which is the best possible time complexity for this problem.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, memoization, and recursion.
- Problem-solving patterns identified: Using dynamic programming to avoid redundant calculations and finding the minimum cost by trying all possible splits.
- Optimization techniques learned: Using memoization to store the minimum cost for each subarray and avoiding redundant calculations.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` array correctly, not handling edge cases properly, and not using memoization correctly.
- Edge cases to watch for: When the input array has only two elements, when the input array has duplicate elements, and when the input array has negative elements.
- Performance pitfalls: Not using dynamic programming, not using memoization, and not handling edge cases properly.