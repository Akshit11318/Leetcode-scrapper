## Count Nodes Equal to Sum of Descendants

**Problem Link:** https://leetcode.com/problems/count-nodes-equal-to-sum-of-descendants/description

**Problem Statement:**
- Input: A binary tree where each node has a value.
- Constraints: The tree is not empty.
- Expected Output: The number of nodes that are equal to the sum of their descendants.
- Key Requirements and Edge Cases:
  - Handle empty subtrees.
  - Consider nodes with no children.
  - Count only nodes that are exactly equal to the sum of their descendants, not greater or lesser.
- Example Test Cases:
  - A tree with one node: the node's value is the sum of its descendants (0), so it counts.
  - A tree where a node's value equals the sum of its children and grandchildren but not its great-grandchildren.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Traverse the tree for each node to calculate the sum of its descendants and compare it with the node's value.
- Step-by-step breakdown of the solution:
  1. Perform a depth-first search (DFS) to traverse the tree.
  2. For each node, recursively calculate the sum of its descendants.
  3. Compare the node's value with the sum of its descendants. If they are equal, increment a counter.

```cpp
int countNodes(TreeNode* root) {
    int count = 0;
    dfs(root, count);
    return count;
}

void dfs(TreeNode* node, int& count) {
    if (!node) return;
    int sum = sumOfDescendants(node);
    if (node->val == sum) count++;
    dfs(node->left, count);
    dfs(node->right, count);
}

int sumOfDescendants(TreeNode* node) {
    if (!node) return 0;
    int sum = node->val;
    sum += sumOfDescendants(node->left);
    sum += sumOfDescendants(node->right);
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the number of nodes in the tree, because for each node, we potentially traverse the entire subtree again.
> - **Space Complexity:** $O(h)$ where $h$ is the height of the tree, due to the recursive call stack.
> - **Why these complexities occur:** The repeated calculation of the sum of descendants for each node leads to inefficient time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Calculate the sum of descendants in a bottom-up manner to avoid redundant calculations.
- Detailed breakdown of the approach:
  1. Perform a post-order DFS to calculate the sum of each node's descendants.
  2. During the DFS, update the sum of descendants for each node and compare it with the node's value.
  3. Use a single pass to calculate the sums and count the nodes that match the condition.

```cpp
int countNodes(TreeNode* root) {
    int count = 0;
    dfs(root, count);
    return count;
}

int dfs(TreeNode* node, int& count) {
    if (!node) return 0;
    int leftSum = dfs(node->left, count);
    int rightSum = dfs(node->right, count);
    if (node->val == leftSum + rightSum) count++;
    return node->val + leftSum + rightSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of nodes, since we visit each node once.
> - **Space Complexity:** $O(h)$ where $h$ is the height of the tree, due to the recursive call stack.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the tree, avoiding redundant calculations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Post-order DFS, bottom-up calculation.
- Problem-solving patterns: Avoiding redundant calculations by changing the order of operations.
- Optimization techniques: Using a single pass to calculate multiple properties of a tree.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle the base case of an empty tree or node.
- Edge cases to watch for: Nodes with no children or subtrees with zero sum.
- Performance pitfalls: Using a brute force approach that leads to high time complexity.
- Testing considerations: Ensure the solution works for trees of varying sizes and structures.