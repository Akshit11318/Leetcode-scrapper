## Lowest Common Ancestor of a Binary Tree II
**Problem Link:** https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/description

**Problem Statement:**
- Given a binary tree and two nodes, find the lowest common ancestor of these two nodes.
- Input: `root` of the binary tree, and `p` and `q`, the two nodes.
- Expected output: The node that is the lowest common ancestor of `p` and `q`.
- Key requirements and edge cases:
  - `p` and `q` are guaranteed to exist in the tree.
  - All node values are unique.
- Example test cases:
  - Example 1: Given the binary tree `[3,5,1,6,2,0,8,null,null,7,4]`, `p = 5`, and `q = 1`, the output should be `3`.
  - Example 2: Given the binary tree `[3,5,1,6,2,0,8,null,null,7,4]`, `p = 5`, and `q = 4`, the output should be `5`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to perform a depth-first search (DFS) or breadth-first search (BFS) from the root to find all paths to `p` and `q`.
- Then, compare these paths to find the last common node, which is the lowest common ancestor.
- This approach comes to mind first because it directly addresses the problem statement without requiring additional insight into the properties of binary trees.

```cpp
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        // Base case
        if (!root) return nullptr;
        
        // If the current node is p or q, return it
        if (root == p || root == q) return root;
        
        // Recursively search for p and q in the left and right subtrees
        TreeNode* left = lowestCommonAncestor(root->left, p, q);
        TreeNode* right = lowestCommonAncestor(root->right, p, q);
        
        // If both left and right are not null, it means p and q are in different subtrees,
        // so the current node is the LCA
        if (left && right) return root;
        
        // If only one of them is not null, it means p and q are in the same subtree,
        // so return the non-null one
        return left ? left : right;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the binary tree. This is because in the worst case, we might have to visit every node.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the binary tree, due to the recursive call stack. In the worst case, for an unbalanced tree, $h = n$.
> - **Why these complexities occur:** These complexities occur because we are potentially visiting every node in the tree once and using a recursive approach that can go as deep as the height of the tree.

---

### Optimal Approach (Required)
**Explanation:**
- The optimal approach is essentially the same as the brute force approach provided above because it already leverages the properties of binary trees and recursive search efficiently.
- The key insight is recognizing that the lowest common ancestor will be the node where the paths to `p` and `q` diverge.
- This approach is optimal because it only visits each node once, leading to a linear time complexity, and it uses the recursive call stack efficiently, minimizing space complexity.

```cpp
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (!root) return nullptr;
        if (root == p || root == q) return root;
        TreeNode* left = lowestCommonAncestor(root->left, p, q);
        TreeNode* right = lowestCommonAncestor(root->right, p, q);
        if (left && right) return root;
        return left ? left : right;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the binary tree.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the binary tree.
> - **Optimality proof:** This is optimal because we only visit each node once and use a minimal amount of extra space for the recursive call stack.

---

### Final Notes

**Learning Points:**
- Recognizing the properties of binary trees and how they can be leveraged for efficient search.
- Understanding recursive search and how it can be applied to tree structures.
- Identifying the lowest common ancestor as the point where paths to two nodes diverge.

**Mistakes to Avoid:**
- Not considering the base cases properly (e.g., a null root or finding `p` or `q`).
- Not optimizing the search by considering the structure of the binary tree.
- Not handling the recursive call stack efficiently, which can lead to stack overflow for very deep trees.