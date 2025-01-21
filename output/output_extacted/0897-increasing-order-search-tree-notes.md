## Increasing Order Search Tree

**Problem Link:** https://leetcode.com/problems/increasing-order-search-tree/description

**Problem Statement:**
- Input: The root of a binary search tree (`BST`).
- Constraints: The number of nodes in the tree is in the range `[1, 100]`. The values of the nodes in the tree are in the range `[0, 100]`.
- Expected Output: The root of the increasing order search tree.
- Key Requirements: Reconstruct the tree in such a way that all values are in increasing order.
- Edge Cases: Handle cases where the input tree is empty or has only one node.

**Example Test Cases:**
- For the input `root = [5,3,6,2,4,null,8,1,null,null,null,7,9]`, the output should be `[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]`.
- For the input `root = [5,1,7]`, the output should be `[1,null,5,null,7]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to traverse the tree, collect all node values, sort them, and then reconstruct a new tree with these sorted values.
- Step-by-step breakdown:
  1. Perform an in-order traversal of the tree to collect all node values in a list.
  2. Sort the list of node values.
  3. Reconstruct a new tree by iterating through the sorted list and creating nodes in increasing order.

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* increasingBST(TreeNode* root) {
        vector<int> values;
        inOrderTraversal(root, values);
        sort(values.begin(), values.end());
        
        // Reconstruct the tree
        TreeNode* newRoot = new TreeNode(values[0]);
        TreeNode* current = newRoot;
        for (int i = 1; i < values.size(); i++) {
            current->right = new TreeNode(values[i]);
            current = current->right;
        }
        
        return newRoot;
    }
    
    void inOrderTraversal(TreeNode* node, vector<int>& values) {
        if (node == nullptr) return;
        inOrderTraversal(node->left, values);
        values.push_back(node->val);
        inOrderTraversal(node->right, values);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting step, where $n$ is the number of nodes in the tree.
> - **Space Complexity:** $O(n)$ for storing the node values and the new tree.
> - **Why these complexities occur:** The sorting step dominates the time complexity, while the space complexity is due to storing all node values and the new tree.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to perform an in-order traversal and reconstruct the tree on the fly, avoiding the need for sorting.
- Detailed breakdown:
  1. Perform an in-order traversal of the tree.
  2. During the traversal, create new nodes with the current value and link them to the previous node's right child.
  3. Return the root of the new tree.

```cpp
class Solution {
public:
    TreeNode* increasingBST(TreeNode* root) {
        TreeNode* newRoot = new TreeNode();
        TreeNode* current = newRoot;
        inOrderTraversal(root, current);
        return newRoot->right;
    }
    
    void inOrderTraversal(TreeNode* node, TreeNode*& current) {
        if (node == nullptr) return;
        inOrderTraversal(node->left, current);
        current->right = new TreeNode(node->val);
        current = current->right;
        inOrderTraversal(node->right, current);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, since we visit each node once.
> - **Space Complexity:** $O(n)$ for the new tree.
> - **Optimality proof:** This is optimal because we must visit each node at least once to reconstruct the tree in increasing order.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: in-order traversal, tree reconstruction.
- Problem-solving patterns identified: avoiding unnecessary steps (like sorting) by leveraging the properties of binary search trees.
- Optimization techniques learned: reconstructing the tree on the fly during traversal.

**Mistakes to Avoid:**
- Not considering the properties of binary search trees, leading to unnecessary complexity.
- Failing to handle edge cases, such as an empty input tree.
- Not optimizing the solution for time and space complexity.