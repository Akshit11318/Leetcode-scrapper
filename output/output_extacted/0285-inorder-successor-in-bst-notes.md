## Inorder Successor in BST
**Problem Link:** https://leetcode.com/problems/inorder-successor-in-bst/description

**Problem Statement:**
- Input format: The root of a binary search tree (`TreeNode* root`) and a node (`TreeNode* p`).
- Constraints: The number of nodes in the tree is in the range `[1, 10^5]`. Each node has a unique value between `1` and `10^5`.
- Expected output format: The node with a value greater than `p->val` that is closest to `p->val`. If no such node exists, return `nullptr`.
- Key requirements and edge cases to consider:
  - The tree is a binary search tree, meaning for every node, all elements in its left subtree are less than the node, and all the elements in its right subtree are greater than the node.
  - The node `p` is guaranteed to be in the tree.
  - Example test cases include finding the inorder successor in a balanced tree, an unbalanced tree, and edge cases like when `p` is the root or a leaf node.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Perform an inorder traversal of the tree, storing the node values in a list. Then, find the index of `p->val` in the list and return the next element.
- Step-by-step breakdown of the solution:
  1. Define a helper function to perform inorder traversal and store node values in a list.
  2. Perform inorder traversal starting from the root, appending each node's value to the list.
  3. Find the index of `p->val` in the list.
  4. If `p->val` is the last element in the list, return `nullptr`. Otherwise, return the node with the next value in the list.
- Why this approach comes to mind first: It directly utilizes the definition of inorder traversal and successor in a straightforward manner.

```cpp
class Solution {
public:
    TreeNode* inorderSuccessor(TreeNode* root, TreeNode* p) {
        vector<int> inorder;
        // Helper function for inorder traversal
        function<void(TreeNode*)> inorderTraversal = [&](TreeNode* node) {
            if (node) {
                inorderTraversal(node->left);
                inorder.push_back(node->val);
                inorderTraversal(node->right);
            }
        };
        inorderTraversal(root);
        
        // Find the index of p->val in the inorder list
        int idx = find(inorder.begin(), inorder.end(), p->val) - inorder.begin();
        
        // If p->val is the last element, return nullptr
        if (idx == inorder.size() - 1) return nullptr;
        
        // Find the node with the next value in the inorder list
        int nextVal = inorder[idx + 1];
        function<TreeNode*(TreeNode*)> findNode = [&](TreeNode* node) {
            if (!node) return nullptr;
            if (node->val == nextVal) return node;
            if (node->val < nextVal) return findNode(node->right);
            return findNode(node->left);
        };
        return findNode(root);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we perform a full inorder traversal of the tree.
> - **Space Complexity:** $O(n)$, as we store all node values in a list.
> - **Why these complexities occur:** The brute force approach requires visiting every node in the tree once for the inorder traversal and potentially again to find the node with the next value, leading to linear time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Since the tree is a binary search tree, we can exploit its property to find the inorder successor without needing to traverse the entire tree. The inorder successor of a node `p` is the smallest node in the subtree rooted at `p->right`. If `p` has no right child, then the inorder successor is the node that is the parent of `p` when moving up the tree until we find a node that is to the right of its parent.
- Detailed breakdown of the approach:
  1. If `p` has a right child, find the smallest node in the subtree rooted at `p->right`.
  2. If `p` does not have a right child, move up the tree until we find a node that is to the right of its parent.
- Proof of optimality: This approach is optimal because it minimizes the number of nodes that need to be visited, taking advantage of the BST property.

```cpp
class Solution {
public:
    TreeNode* inorderSuccessor(TreeNode* root, TreeNode* p) {
        // Case 1: p has a right child
        if (p->right) {
            TreeNode* successor = p->right;
            while (successor->left) {
                successor = successor->left;
            }
            return successor;
        }
        
        // Case 2: p does not have a right child
        TreeNode* successor = nullptr;
        TreeNode* current = root;
        while (current != p) {
            if (current->val > p->val) {
                successor = current;
                current = current->left;
            } else {
                current = current->right;
            }
        }
        return successor;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(h)$, where $h$ is the height of the tree. In the worst case (a skewed tree), this is $O(n)$, but for a balanced tree, it's $O(\log n)$.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the successor and current nodes.
> - **Optimality proof:** This is optimal because we only visit nodes that are necessary to find the inorder successor, leveraging the BST properties to minimize the number of nodes visited.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Exploiting properties of binary search trees, understanding inorder traversal and successor concepts.
- Problem-solving patterns identified: Using the structure of the data (in this case, a BST) to optimize the solution.
- Optimization techniques learned: Minimizing the number of nodes visited by leveraging the BST property.
- Similar problems to practice: Finding the inorder predecessor, implementing BST operations (insert, delete, search).

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases (like when `p` is the root or a leaf node), not properly leveraging the BST property.
- Edge cases to watch for: When `p` has or does not have a right child, when `p` is the root or a leaf node.
- Performance pitfalls: Not optimizing the solution to take advantage of the BST structure, leading to unnecessary node visits.
- Testing considerations: Ensure to test with various tree structures (balanced, unbalanced, different node values) and edge cases.