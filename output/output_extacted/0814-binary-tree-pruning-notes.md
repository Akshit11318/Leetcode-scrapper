## Binary Tree Pruning
**Problem Link:** https://leetcode.com/problems/binary-tree-pruning/description

**Problem Statement:**
- Input: The root of a binary tree.
- Constraints: The number of nodes in the tree is in the range [1, 100].
- Expected Output: The root of the resulting binary tree after pruning.
- Key Requirements: Remove all the subtrees that only contain zeros.
- Edge Cases: Empty tree, tree with a single node, tree with all nodes being zero.

**Example Test Cases:**
- Example 1: 
  - Input: `[1,null,0,0,1]`
  - Output: `[1,null,0,null,1]`
- Example 2: 
  - Input: `[1,0,1,0,0,0,1]`
  - Output: `[1,null,1,null,1]`
- Example 3: 
  - Input: `[0]`
  - Output: `null`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to traverse the tree and check each node's value. If a node's value is 0 and it does not have any children with a value of 1, we can prune this node.
- Step-by-step breakdown:
  1. Define a helper function to check if a tree contains a node with a value of 1.
  2. Traverse the tree, and for each node, check if its value is 0 and if its children do not contain any nodes with a value of 1.
  3. If the conditions are met, prune the node.

```cpp
// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    TreeNode* pruneTree(TreeNode* root) {
        if (!root) return nullptr;
        root->left = pruneTree(root->left);
        root->right = pruneTree(root->right);
        if (root->val == 0 && !root->left && !root->right) return nullptr;
        return root;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, because we visit each node once.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree, because of the recursion stack. In the worst case, $h = n$ for an unbalanced tree.
> - **Why these complexities occur:** The time complexity is linear because we visit each node exactly once. The space complexity depends on the recursion stack, which can go up to the height of the tree in the worst case.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a recursive approach to prune the tree. This approach is optimal because it only visits each node once.
- Detailed breakdown of the approach:
  1. If the tree is empty, return `nullptr`.
  2. Recursively prune the left and right subtrees.
  3. If the current node's value is 0 and its left and right children are both `nullptr`, return `nullptr` to prune the node.
  4. Otherwise, return the current node with its pruned children.

```cpp
class Solution {
public:
    TreeNode* pruneTree(TreeNode* root) {
        if (!root) return nullptr;
        root->left = pruneTree(root->left);
        root->right = pruneTree(root->right);
        if (root->val == 0 && !root->left && !root->right) return nullptr;
        return root;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree.
> - **Optimality proof:** This approach is optimal because it only visits each node once, resulting in a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursion, tree traversal, and pruning.
- Problem-solving patterns identified: Using recursion to solve tree-related problems.
- Optimization techniques learned: Pruning the tree to reduce unnecessary nodes.
- Similar problems to practice: Other tree-related problems, such as binary tree traversal and tree construction.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the base case correctly, not pruning the tree correctly.
- Edge cases to watch for: Empty tree, tree with a single node, tree with all nodes being zero.
- Performance pitfalls: Not using recursion efficiently, resulting in a high time complexity.
- Testing considerations: Test the solution with different tree structures and edge cases.