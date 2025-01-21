## Delete Node in a BST

**Problem Link:** https://leetcode.com/problems/delete-node-in-a-bst/description

**Problem Statement:**
- Input: The root of a binary search tree (`TreeNode* root`) and a value (`int key`) to be deleted.
- Constraints: Each node has a unique value (`node.val`) ranging from 0 to 100, and the number of nodes in the tree does not exceed 100.
- Expected Output: The root of the modified binary search tree after deleting the node with the given value.
- Key Requirements: Ensure the resulting tree remains a valid binary search tree.
- Example Test Cases:
  - Deleting a leaf node.
  - Deleting a node with one child.
  - Deleting a node with two children.
  - Deleting the root node.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves finding the node to be deleted and then handling three cases: the node is a leaf, the node has one child, or the node has two children.
- For a node with two children, a brute force approach would be to find the in-order successor (smallest node in the right subtree) or predecessor (largest node in the left subtree) of the node to be deleted, replace the node's value with that of its in-order successor/predecessor, and then delete the in-order successor/predecessor.

```cpp
// Brute Force Code
TreeNode* deleteNode(TreeNode* root, int key) {
    if (!root) return nullptr;

    // Find the node to be deleted
    if (key < root->val) {
        root->left = deleteNode(root->left, key);
    } else if (key > root->val) {
        root->right = deleteNode(root->right, key);
    } else {
        // Node has no children
        if (!root->left && !root->right) {
            delete root;
            return nullptr;
        }
        // Node has one child
        else if (!root->left) {
            TreeNode* temp = root->right;
            delete root;
            return temp;
        } else if (!root->right) {
            TreeNode* temp = root->left;
            delete root;
            return temp;
        }
        // Node has two children
        else {
            // Find in-order successor
            TreeNode* successor = root->right;
            while (successor->left) successor = successor->left;
            root->val = successor->val;
            root->right = deleteNode(root->right, successor->val);
        }
    }
    return root;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ in the worst case where we have to traverse the entire tree to find the node to be deleted and its in-order successor/predecessor.
> - **Space Complexity:** $O(h)$ due to the recursive call stack, where $h$ is the height of the tree. In the worst case (a skewed tree), $h = n$; in the best case (a balanced tree), $h = \log n$.
> - **Why these complexities occur:** The brute force approach involves a recursive search for the node to be deleted and potentially finding its in-order successor/predecessor, leading to these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves directly handling the three cases when finding the node to be deleted: it's a leaf node, has one child, or has two children.
- For a node with two children, instead of finding the in-order successor/predecessor and then deleting it, we can directly replace the node's value with that of its in-order successor/predecessor and then handle the deletion of the successor/predecessor.
- This approach ensures we minimize the number of tree traversals.

```cpp
// Optimal Code
TreeNode* deleteNode(TreeNode* root, int key) {
    if (!root) return nullptr;

    if (key < root->val) {
        root->left = deleteNode(root->left, key);
    } else if (key > root->val) {
        root->right = deleteNode(root->right, key);
    } else {
        // No children
        if (!root->left && !root->right) {
            delete root;
            return nullptr;
        }
        // One child
        else if (!root->left) {
            TreeNode* temp = root->right;
            delete root;
            return temp;
        } else if (!root->right) {
            TreeNode* temp = root->left;
            delete root;
            return temp;
        }
        // Two children
        else {
            // Find in-order successor
            TreeNode* successor = root->right;
            while (successor->left) successor = successor->left;
            root->val = successor->val;
            root->right = deleteNode(root->right, successor->val);
        }
    }
    return root;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(h)$, where $h$ is the height of the tree, because in the worst case we have to traverse from the root to a leaf node to find the node to be deleted and its potential in-order successor/predecessor.
> - **Space Complexity:** $O(h)$ due to the recursive call stack.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations (comparisons and node updates) required to delete a node and maintain the binary search tree property.

---

### Alternative Approach

**Explanation:**
- An alternative approach involves using an iterative method instead of recursion to delete the node. This can be beneficial in terms of avoiding potential stack overflow issues for very deep trees.
- The iterative approach would involve using a stack or queue to manually manage the traversal of the tree.

```cpp
// Alternative Iterative Code
TreeNode* deleteNode(TreeNode* root, int key) {
    if (!root) return nullptr;

    TreeNode* current = root;
    TreeNode* parent = nullptr;

    // Find the node to be deleted
    while (current && current->val != key) {
        parent = current;
        if (key < current->val) {
            current = current->left;
        } else {
            current = current->right;
        }
    }

    if (!current) return root; // Node not found

    // Node has no children
    if (!current->left && !current->right) {
        if (parent) {
            if (parent->left == current) {
                parent->left = nullptr;
            } else {
                parent->right = nullptr;
            }
        } else {
            // Current is the root
            return nullptr;
        }
    }
    // Node has one child
    else if (!current->left) {
        if (parent) {
            if (parent->left == current) {
                parent->left = current->right;
            } else {
                parent->right = current->right;
            }
        } else {
            // Current is the root
            return current->right;
        }
    } else if (!current->right) {
        if (parent) {
            if (parent->left == current) {
                parent->left = current->left;
            } else {
                parent->right = current->left;
            }
        } else {
            // Current is the root
            return current->left;
        }
    }
    // Node has two children
    else {
        // Find in-order successor
        TreeNode* successor = current->right;
        TreeNode* successorParent = current;
        while (successor->left) {
            successorParent = successor;
            successor = successor->left;
        }
        current->val = successor->val;
        if (successorParent->left == successor) {
            successorParent->left = successor->right;
        } else {
            successorParent->right = successor->right;
        }
    }
    return root;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(h)$, where $h$ is the height of the tree.
> - **Space Complexity:** $O(1)$ for the iterative approach, excluding the space needed for the tree itself.
> - **Trade-off analysis:** The iterative approach avoids the risk of stack overflow for very deep trees but might be slightly more complex to implement than the recursive version.

---

### Final Notes

**Learning Points:**
- Handling different cases for deleting a node in a binary search tree (leaf, one child, two children).
- Understanding the importance of maintaining the binary search tree property after deletion.
- Recognizing the trade-offs between recursive and iterative approaches.
- Practicing similar problems to solidify understanding of tree operations.

**Mistakes to Avoid:**
- Failing to handle edge cases properly (e.g., deleting the root node).
- Not maintaining the binary search tree property after deletion.
- Not considering the potential for stack overflow in very deep trees when using recursive approaches.
- Not testing the code thoroughly with various input scenarios.