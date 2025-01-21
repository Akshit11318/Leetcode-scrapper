## Lowest Common Ancestor of a Binary Tree

**Problem Link:** https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description

**Problem Statement:**
- Input: A binary tree and two nodes `p` and `q`.
- Output: The lowest common ancestor (LCA) of `p` and `q`.
- Key requirements: 
  - `p` and `q` are guaranteed to exist in the binary tree.
  - The LCA of `p` and `q` is the node farthest from the root that is an ancestor of both `p` and `q`.
- Edge cases: 
  - `p` and `q` can be the same node.
  - `p` or `q` can be the root of the tree.

### Brute Force Approach

**Explanation:**
- The initial thought process is to traverse the tree from the root to both `p` and `q`, and then compare the paths to find the last common node.
- Step-by-step breakdown:
  1. Perform a depth-first search (DFS) from the root to find the path to `p`.
  2. Perform another DFS from the root to find the path to `q`.
  3. Compare the two paths to find the last common node, which is the LCA.

```cpp
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        // Base case: if the tree is empty, return NULL
        if (!root) return NULL;
        
        // If the current node is p or q, return the current node
        if (root == p || root == q) return root;
        
        // Recursively search for p and q in the left and right subtrees
        TreeNode* left = lowestCommonAncestor(root->left, p, q);
        TreeNode* right = lowestCommonAncestor(root->right, p, q);
        
        // If both p and q are found in different subtrees, the current node is the LCA
        if (left && right) return root;
        
        // If both p and q are found in the left subtree, the LCA is in the left subtree
        if (left) return left;
        
        // If both p and q are found in the right subtree, the LCA is in the right subtree
        if (right) return right;
        
        // If neither p nor q is found in the left or right subtree, return NULL
        return NULL;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, because we visit each node at most twice.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree, because of the recursive call stack.
> - **Why these complexities occur:** The time complexity is linear because we visit each node at most twice, and the space complexity is related to the height of the tree because of the recursive call stack.

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a recursive approach to find the LCA.
- The optimal solution is the same as the brute force approach, as it is already quite efficient.

```cpp
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        // Base case: if the tree is empty, return NULL
        if (!root) return NULL;
        
        // If the current node is p or q, return the current node
        if (root == p || root == q) return root;
        
        // Recursively search for p and q in the left and right subtrees
        TreeNode* left = lowestCommonAncestor(root->left, p, q);
        TreeNode* right = lowestCommonAncestor(root->right, p, q);
        
        // If both p and q are found in different subtrees, the current node is the LCA
        if (left && right) return root;
        
        // If both p and q are found in the left subtree, the LCA is in the left subtree
        if (left) return left;
        
        // If both p and q are found in the right subtree, the LCA is in the right subtree
        if (right) return right;
        
        // If neither p nor q is found in the left or right subtree, return NULL
        return NULL;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, because we visit each node at most twice.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree, because of the recursive call stack.
> - **Optimality proof:** This is the optimal solution because we must visit each node at least once to find the LCA, and the recursive approach allows us to do so in a single pass.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the use of recursive approaches to solve tree problems.
- The problem-solving pattern identified is to use a divide-and-conquer approach to find the LCA.
- The optimization technique learned is to use a recursive approach to reduce the time complexity.

**Mistakes to Avoid:**
- A common implementation error is to forget to handle the base case where the tree is empty.
- An edge case to watch for is when `p` and `q` are the same node.
- A performance pitfall is to use an iterative approach with a queue, which can lead to a higher time complexity.
- A testing consideration is to test the solution with different tree structures and node values.