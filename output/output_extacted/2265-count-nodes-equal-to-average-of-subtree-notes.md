## Count Nodes Equal to Average of Subtree

**Problem Link:** https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/description

**Problem Statement:**
- Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.
- Input: The root of a binary tree.
- Output: The number of nodes that satisfy the condition.
- Key requirements and edge cases:
  - Handle empty trees.
  - Consider the average of a single node as the node's value itself.
  - Round averages to the nearest integer if necessary.

**Example Test Cases:**
- A tree with a single node will always satisfy the condition because the node's value is its own average.
- For a tree with multiple nodes, only nodes where the sum of their subtree divided by the number of nodes in the subtree equals the node's value should be counted.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves calculating the sum and count of nodes for each subtree and then checking if the average (sum divided by count) equals the node's value.
- This approach requires traversing the tree for each node to calculate the sum and count of its subtree.

```cpp
int countNodesEqualToAverage(TreeNode* root) {
    if (!root) return 0;
    int count = 0;
    if (isAverage(root, sumOfSubtree(root), countOfSubtree(root))) count++;
    return count + countNodesEqualToAverage(root->left) + countNodesEqualToAverage(root->right);
}

bool isAverage(TreeNode* node, int sum, int count) {
    if (count == 0) return false;
    return node->val == sum / count;
}

int sumOfSubtree(TreeNode* node) {
    if (!node) return 0;
    return node->val + sumOfSubtree(node->left) + sumOfSubtree(node->right);
}

int countOfSubtree(TreeNode* node) {
    if (!node) return 0;
    return 1 + countOfSubtree(node->left) + countOfSubtree(node->right);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ because for each node, we potentially traverse its entire subtree to calculate the sum and count.
> - **Space Complexity:** $O(h)$ due to the recursive call stack, where $h$ is the height of the tree.
> - **Why these complexities occur:** The brute force approach recalculates the sum and count for each node's subtree, leading to redundant calculations and high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to calculate the sum and count of each subtree only once by passing these values up the recursive call stack.
- This approach involves a depth-first search (DFS) where each node returns the sum and count of its subtree, allowing for efficient calculation of the average.

```cpp
int countNodesEqualToAverage(TreeNode* root) {
    int result = 0;
    dfs(root, result);
    return result;
}

pair<int, int> dfs(TreeNode* node, int& result) {
    if (!node) return {0, 0};
    auto [leftSum, leftCount] = dfs(node->left, result);
    auto [rightSum, rightCount] = dfs(node->right, result);
    int totalSum = node->val + leftSum + rightSum;
    int totalCount = 1 + leftCount + rightCount;
    if (totalCount > 0 && node->val == totalSum / totalCount) result++;
    return {totalSum, totalCount};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because each node is visited once.
> - **Space Complexity:** $O(h)$ due to the recursive call stack.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to solve the problem by calculating the sum and count of each subtree exactly once.

---

### Final Notes

**Learning Points:**
- The importance of avoiding redundant calculations in recursive algorithms.
- Using DFS to efficiently traverse and calculate properties of a binary tree.
- Passing values up the recursive call stack to reduce computation.

**Mistakes to Avoid:**
- Recalculating values that can be computed once and reused.
- Not considering the base case of recursion (e.g., an empty tree).
- Failing to update the result correctly in recursive functions.