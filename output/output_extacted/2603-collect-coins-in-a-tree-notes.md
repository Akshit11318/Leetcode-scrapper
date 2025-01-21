## Collect Coins in a Tree

**Problem Link:** https://leetcode.com/problems/collect-coins-in-a-tree/description

**Problem Statement:**
- Input format and constraints: The problem involves a tree with `n` nodes labeled from `1` to `n`, where each node `i` has a value `coins[i]` representing the number of coins it contains. The input is represented as a list of lists, `adj`, where `adj[i]` is a list of the nodes that are directly connected to node `i`. The goal is to find the maximum number of coins that can be collected by traversing the tree.
- Expected output format: The output should be the maximum number of coins that can be collected.
- Key requirements and edge cases to consider: The tree is not necessarily a binary tree, and each node can have any number of children. The tree may not be connected, but it's guaranteed that the input represents a tree.
- Example test cases with explanations: For example, given a tree with nodes `1`, `2`, `3`, and `4`, where `coins = [1, 2, 3, 4]` and `adj = [[2, 3], [4], [], []]`, the maximum number of coins that can be collected is `1 + 2 + 3 + 4 = 10`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to use a recursive depth-first search (DFS) to traverse the tree and collect all the coins. This involves visiting each node, collecting its coins, and recursively visiting its children.
- Step-by-step breakdown of the solution:
  1. Define a recursive function `dfs` that takes a node `i` as input.
  2. In the `dfs` function, collect the coins at node `i` and recursively call `dfs` on its children.
  3. Return the total number of coins collected.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, as it directly follows the problem statement.

```cpp
class Solution {
public:
    int collectCoins(vector<int>& coins, vector<vector<int>>& adj) {
        int maxCoins = 0;
        function<void(int, int)> dfs = [&](int i, int parent) {
            int totalCoins = coins[i];
            for (int j : adj[i]) {
                if (j != parent) {
                    totalCoins += dfs(j, i);
                }
            }
            maxCoins = max(maxCoins, totalCoins);
            return totalCoins;
        };
        dfs(0, -1);
        return maxCoins;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of nodes in the tree. This is because in the worst case, we might need to traverse the entire tree for each node.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because of the recursive call stack.
> - **Why these complexities occur:** The brute force approach has high time complexity because it involves recursive calls for each node, leading to repeated computations. The space complexity is due to the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use a dynamic programming approach to store the maximum number of coins that can be collected for each subtree. This allows us to avoid repeated computations and reduce the time complexity.
- Detailed breakdown of the approach:
  1. Define a dynamic programming table `dp` where `dp[i]` represents the maximum number of coins that can be collected for the subtree rooted at node `i`.
  2. Initialize `dp[i] = coins[i]` for each node `i`.
  3. For each node `i`, iterate over its children `j` and update `dp[i] = max(dp[i], dp[i] + dp[j])`.
  4. Return the maximum value in the `dp` table.
- Proof of optimality: This approach is optimal because it avoids repeated computations by storing the maximum number of coins for each subtree. This reduces the time complexity to $O(n)$.

```cpp
class Solution {
public:
    int collectCoins(vector<int>& coins, vector<vector<int>>& adj) {
        int n = coins.size();
        vector<int> dp(n, 0);
        for (int i = 0; i < n; i++) {
            dp[i] = coins[i];
        }
        for (int i = 0; i < n; i++) {
            for (int j : adj[i]) {
                dp[i] = max(dp[i], dp[i] + dp[j]);
            }
        }
        return *max_element(dp.begin(), dp.end());
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we only need to iterate over the nodes once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because of the dynamic programming table.
> - **Optimality proof:** This approach is optimal because it avoids repeated computations by storing the maximum number of coins for each subtree.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, recursive DFS.
- Problem-solving patterns identified: Avoiding repeated computations by storing intermediate results.
- Optimization techniques learned: Using dynamic programming to reduce time complexity.
- Similar problems to practice: Other problems involving dynamic programming and recursive DFS.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the dynamic programming table correctly, not updating the table correctly.
- Edge cases to watch for: Handling the case where the input tree is empty, handling the case where a node has no children.
- Performance pitfalls: Not using dynamic programming to avoid repeated computations, using a recursive approach with high time complexity.
- Testing considerations: Testing the solution with different input trees, testing the solution with edge cases.