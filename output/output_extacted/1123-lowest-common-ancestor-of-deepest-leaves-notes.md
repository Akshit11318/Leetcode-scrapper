## Lowest Common Ancestor of Deepest Leaves

**Problem Link:** https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/description

**Problem Statement:**
- Input format: The root of a binary tree.
- Constraints: The number of nodes in the tree is between 1 and 1000.
- Expected output format: The lowest common ancestor of the deepest leaves.
- Key requirements and edge cases to consider: The tree may be unbalanced, and the deepest leaves may be on the same side of the tree.
- Example test cases with explanations:
  - Test case 1: A balanced tree with two leaves at the same depth.
  - Test case 2: An unbalanced tree with the deepest leaves on the same side.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Perform a depth-first search (DFS) to find all leaves and their depths, then find the lowest common ancestor of the deepest leaves.
- Step-by-step breakdown of the solution:
  1. Perform a DFS to find all leaves and their depths.
  2. Find the maximum depth of the leaves.
  3. Find the lowest common ancestor of the deepest leaves.
- Why this approach comes to mind first: It's a straightforward approach that involves finding all leaves and their depths, then finding the lowest common ancestor.

```cpp
class Solution {
public:
    TreeNode* lcaDeepestLeaves(TreeNode* root) {
        if (!root) return nullptr;
        
        // Perform DFS to find all leaves and their depths
        vector<pair<TreeNode*, int>> leaves;
        dfs(root, 0, leaves);
        
        // Find the maximum depth of the leaves
        int maxDepth = 0;
        for (auto& leaf : leaves) {
            maxDepth = max(maxDepth, leaf.second);
        }
        
        // Find the lowest common ancestor of the deepest leaves
        TreeNode* lca = nullptr;
        for (auto& leaf : leaves) {
            if (leaf.second == maxDepth) {
                if (!lca) {
                    lca = leaf.first;
                } else {
                    lca = findLCA(root, lca, leaf.first);
                }
            }
        }
        
        return lca;
    }
    
    void dfs(TreeNode* node, int depth, vector<pair<TreeNode*, int>>& leaves) {
        if (!node) return;
        
        if (!node->left && !node->right) {
            leaves.push_back({node, depth});
        } else {
            dfs(node->left, depth + 1, leaves);
            dfs(node->right, depth + 1, leaves);
        }
    }
    
    TreeNode* findLCA(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (!root) return nullptr;
        
        if (root == p || root == q) return root;
        
        TreeNode* left = findLCA(root->left, p, q);
        TreeNode* right = findLCA(root->right, p, q);
        
        if (left && right) return root;
        return left ? left : right;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we perform a DFS to find all leaves and their depths, and then find the lowest common ancestor of the deepest leaves.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we store all leaves and their depths in a vector.
> - **Why these complexities occur:** The time complexity occurs because we perform a DFS to find all leaves and their depths, and then find the lowest common ancestor of the deepest leaves. The space complexity occurs because we store all leaves and their depths in a vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can find the depth of each node and the lowest common ancestor of the deepest leaves in a single DFS pass.
- Detailed breakdown of the approach:
  1. Perform a DFS to find the depth of each node and the lowest common ancestor of the deepest leaves.
  2. Update the depth of each node and the lowest common ancestor of the deepest leaves as we traverse the tree.
- Proof of optimality: This approach is optimal because we only need to traverse the tree once to find the depth of each node and the lowest common ancestor of the deepest leaves.
- Why further optimization is impossible: This approach is already optimal because we only need to traverse the tree once.

```cpp
class Solution {
public:
    int maxDepth = 0;
    TreeNode* lca = nullptr;
    
    TreeNode* lcaDeepestLeaves(TreeNode* root) {
        dfs(root, 0);
        return lca;
    }
    
    int dfs(TreeNode* node, int depth) {
        if (!node) return depth;
        
        maxDepth = max(maxDepth, depth);
        
        int leftDepth = dfs(node->left, depth + 1);
        int rightDepth = dfs(node->right, depth + 1);
        
        if (leftDepth == maxDepth && rightDepth == maxDepth) {
            lca = node;
        }
        
        return max(leftDepth, rightDepth);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we perform a single DFS pass to find the depth of each node and the lowest common ancestor of the deepest leaves.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree. This is because we need to store the recursive call stack.
> - **Optimality proof:** This approach is optimal because we only need to traverse the tree once to find the depth of each node and the lowest common ancestor of the deepest leaves.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, tree traversal, and lowest common ancestor.
- Problem-solving patterns identified: Using a single DFS pass to find the depth of each node and the lowest common ancestor of the deepest leaves.
- Optimization techniques learned: Reducing the number of tree traversals to find the solution.
- Similar problems to practice: Finding the lowest common ancestor of two nodes in a tree, finding the diameter of a tree.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the depth of each node correctly, not finding the lowest common ancestor of the deepest leaves correctly.
- Edge cases to watch for: Empty trees, trees with a single node, trees with multiple nodes at the same depth.
- Performance pitfalls: Using multiple tree traversals to find the solution, not using a single DFS pass to find the depth of each node and the lowest common ancestor of the deepest leaves.
- Testing considerations: Testing with different tree structures, testing with different node values, testing with different edge cases.