## Correct a Binary Tree
**Problem Link:** https://leetcode.com/problems/correct-a-binary-tree/description

**Problem Statement:**
- Input format and constraints: The input is the root of a binary tree where exactly one node has two parents. The tree has at most $10^4$ nodes and the values of the nodes are in the range $[-10^5, 10^5]$.
- Expected output format: Return the root of the corrected binary tree.
- Key requirements and edge cases to consider: The tree has at most one node with two parents. The tree has at most $10^4$ nodes.
- Example test cases with explanations: For example, given the following tree:
```
     3
    / \
   1   2
  / \
 0   3
```
The corrected tree should be:
```
     3
    / \
   1   2
  /
 0
```

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves traversing the tree and keeping track of the parent of each node. If a node has two parents, we need to correct the tree by removing the incorrect parent.
- Step-by-step breakdown of the solution:
  1. Traverse the tree using DFS or BFS and keep track of the parent of each node.
  2. If a node has two parents, remove the incorrect parent.
- Why this approach comes to mind first: This approach is straightforward and involves a simple traversal of the tree.

```cpp
class Solution {
public:
    TreeNode* correctBinaryTree(TreeNode* root) {
        unordered_set<TreeNode*> parents;
        unordered_set<TreeNode*> visited;
        return dfs(root, parents, visited);
    }

    TreeNode* dfs(TreeNode* node, unordered_set<TreeNode*>& parents, unordered_set<TreeNode*>& visited) {
        if (!node) return node;
        if (parents.count(node)) {
            // Remove the incorrect parent
            node->left = nullptr;
            node->right = nullptr;
        }
        parents.insert(node);
        visited.insert(node);
        dfs(node->left, parents, visited);
        dfs(node->right, parents, visited);
        return node;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, since we are doing a single pass through the tree.
> - **Space Complexity:** $O(n)$, since we are storing the parents of each node in a set.
> - **Why these complexities occur:** The time complexity is $O(n)$ because we are visiting each node once. The space complexity is $O(n)$ because we are storing the parents of each node in a set.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a single pass through the tree and keeping track of the parent of each node. If a node has two parents, we need to correct the tree by removing the incorrect parent.
- Detailed breakdown of the approach:
  1. Traverse the tree using DFS or BFS and keep track of the parent of each node.
  2. If a node has two parents, remove the incorrect parent.
- Proof of optimality: This solution is optimal because it involves a single pass through the tree and uses a minimal amount of extra space.

```cpp
class Solution {
public:
    TreeNode* correctBinaryTree(TreeNode* root) {
        unordered_set<TreeNode*> parents;
        return dfs(root, parents);
    }

    TreeNode* dfs(TreeNode* node, unordered_set<TreeNode*>& parents) {
        if (!node) return node;
        if (parents.count(node)) {
            // Remove the incorrect parent
            node->left = nullptr;
            node->right = nullptr;
        }
        parents.insert(node);
        dfs(node->left, parents);
        dfs(node->right, parents);
        return node;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, since we are doing a single pass through the tree.
> - **Space Complexity:** $O(n)$, since we are storing the parents of each node in a set.
> - **Optimality proof:** This solution is optimal because it involves a single pass through the tree and uses a minimal amount of extra space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Tree traversal, parent tracking.
- Problem-solving patterns identified: Single pass through the tree, minimal extra space.
- Optimization techniques learned: Using a single pass through the tree and minimal extra space.
- Similar problems to practice: Tree traversal problems, parent tracking problems.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for null nodes, not handling edge cases.
- Edge cases to watch for: Nodes with two parents, nodes with no parents.
- Performance pitfalls: Using too much extra space, doing multiple passes through the tree.
- Testing considerations: Test with different tree structures, test with different edge cases.