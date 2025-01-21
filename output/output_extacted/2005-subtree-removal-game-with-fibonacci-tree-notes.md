## Subtree Removal Game with Fibonacci Tree

**Problem Link:** https://leetcode.com/problems/subtree-removal-game-with-fibonacci-tree/description

**Problem Statement:**
- Input format and constraints: The problem involves a tree where each node has a value and two children. The input is a tree represented as an adjacency list, and the goal is to find the maximum number of nodes that can be removed in a game where two players take turns removing subtrees.
- Expected output format: The output should be the maximum number of nodes that can be removed.
- Key requirements and edge cases to consider: The tree can have up to $10^5$ nodes, and each node can have up to two children. The game is played with two players, and the goal is to remove the maximum number of nodes.
- Example test cases with explanations: For example, given a tree with the following structure:
```
    1
   / \
  2   3
 / \   \
4   5   6
```
The maximum number of nodes that can be removed is 6.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The initial thought is to use a recursive approach to traverse the tree and calculate the maximum number of nodes that can be removed.
- Step-by-step breakdown of the solution:
  1. Define a recursive function `dfs` that takes a node as input and returns the maximum number of nodes that can be removed.
  2. In the `dfs` function, calculate the maximum number of nodes that can be removed by considering two cases: removing the current node or not removing it.
  3. If the current node is removed, recursively call `dfs` on its children and add their results to the current node's value.
  4. If the current node is not removed, recursively call `dfs` on its children and add their results to the current node's value.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it has a high time complexity due to the recursive calls.

```cpp
int dfs(Node* node) {
  if (!node) return 0;
  int remove = node->val + dfs(node->left) + dfs(node->right);
  int notRemove = dfs(node->left) + dfs(node->right);
  return max(remove, notRemove);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the number of nodes in the tree. This is because each node is visited twice in the worst case.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because of the recursive call stack.
> - **Why these complexities occur:** The high time complexity occurs because of the recursive calls, and the space complexity occurs because of the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use dynamic programming to store the results of subproblems and avoid redundant calculations.
- Detailed breakdown of the approach:
  1. Define a `dp` array to store the maximum number of nodes that can be removed for each node.
  2. Initialize the `dp` array with the base case where each node is removed.
  3. Iterate through the tree and update the `dp` array using the following recurrence relation: `dp[node] = max(node->val + dp[node->left] + dp[node->right], dp[node->left] + dp[node->right])`.
- Proof of optimality: The dynamic programming approach ensures that each subproblem is solved only once, resulting in a significant reduction in time complexity.

```cpp
int subtreeRemovalGame(Node* root) {
  int n = countNodes(root);
  vector<int> dp(n, 0);
  dfs(root, dp);
  return dp[0];
}

int dfs(Node* node, vector<int>& dp) {
  if (!node) return 0;
  int idx = node->val - 1;
  int left = dfs(node->left, dp);
  int right = dfs(node->right, dp);
  dp[idx] = max(node->val + left + right, left + right);
  return dp[idx];
}

int countNodes(Node* node) {
  if (!node) return 0;
  return 1 + countNodes(node->left) + countNodes(node->right);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because each node is visited once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because of the `dp` array.
> - **Optimality proof:** The dynamic programming approach ensures that each subproblem is solved only once, resulting in a significant reduction in time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, tree traversal, and memoization.
- Problem-solving patterns identified: Using dynamic programming to store the results of subproblems and avoid redundant calculations.
- Optimization techniques learned: Using memoization to store the results of subproblems and reduce time complexity.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` array correctly, not updating the `dp` array correctly, and not using memoization correctly.
- Edge cases to watch for: Handling the base case where each node is removed, handling the case where a node has no children, and handling the case where a node has one child.
- Performance pitfalls: Not using dynamic programming, not using memoization, and not optimizing the recursive calls.