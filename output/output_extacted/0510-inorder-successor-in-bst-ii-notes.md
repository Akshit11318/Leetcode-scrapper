## Inorder Successor in BST II
**Problem Link:** https://leetcode.com/problems/inorder-successor-in-bst-ii/description

**Problem Statement:**
- Input: A `Node` object representing a node in a binary search tree (`BST`) and the `p` node for which we need to find the inorder successor.
- Constraints: The input BST is not guaranteed to be balanced, and the node `p` is guaranteed to exist in the tree.
- Expected Output: The node that is the inorder successor of `p` in the BST. If there is no inorder successor, return `nullptr`.
- Key Requirements: 
  - The solution should handle cases where `p` has a right child.
  - The solution should handle cases where `p` does not have a right child but has a parent node that is the left child of its parent.
  - The solution should handle edge cases where `p` is the rightmost node in the tree.
- Example Test Cases:
  - For a BST with nodes `1, 2, 3`, where `1` is the root, `2` is the right child of `1`, and `3` is the right child of `2`, if `p` is `1`, the inorder successor of `1` is `2`.
  - For a BST with nodes `5, 3, 6, 2, 4, 7`, where `5` is the root, `3` is the left child of `5`, `6` is the right child of `5`, `2` is the left child of `3`, `4` is the right child of `3`, and `7` is the right child of `6`, if `p` is `3`, the inorder successor of `3` is `4`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to perform an inorder traversal of the BST and store the nodes in a vector or array as we visit them.
- Once we have all nodes in order, we can easily find the successor of `p` by locating `p` in the vector and returning the next node if it exists.
- This approach comes to mind first because it directly leverages the definition of inorder traversal and successor in a BST.

```cpp
class Solution {
public:
    Node* inorderSuccessor(Node* root, Node* p) {
        vector<Node*> inorder;
        traverse(root, inorder);
        for (int i = 0; i < inorder.size() - 1; ++i) {
            if (inorder[i] == p) {
                return inorder[i + 1];
            }
        }
        return nullptr; // No successor found
    }
    
    void traverse(Node* node, vector<Node*>& inorder) {
        if (!node) return;
        traverse(node->left, inorder);
        inorder.push_back(node);
        traverse(node->right, inorder);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the BST, because we visit each node once during the inorder traversal.
> - **Space Complexity:** $O(n)$, because in the worst case (a skewed tree), we might store all nodes in the `inorder` vector.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node. The space complexity is also linear because we store all nodes in the vector for the inorder traversal.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to leverage the properties of a BST to find the inorder successor without needing to store all nodes.
- If `p` has a right child, the inorder successor is the smallest node in the right subtree of `p`.
- If `p` does not have a right child, we need to find the smallest ancestor of `p` that is greater than `p`, which will be the parent node of `p` if `p` is the left child of its parent, or the parent of an ancestor of `p` that is a left child.
- This approach is optimal because it minimizes the number of nodes we need to visit to find the successor.

```cpp
class Solution {
public:
    Node* inorderSuccessor(Node* root, Node* p) {
        // Case 1: p has a right child
        if (p->right) {
            Node* node = p->right;
            while (node->left) {
                node = node->left;
            }
            return node;
        }
        
        // Case 2: p does not have a right child
        Node* successor = nullptr;
        Node* current = root;
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
> - **Time Complexity:** $O(h)$, where $h$ is the height of the BST, because in the worst case, we need to traverse from the root to the deepest leaf.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the successor and the current node.
> - **Optimality proof:** This is the best possible complexity because we must visit at least the nodes on the path from the root to `p` to find its successor, and the height of the tree represents the minimum number of nodes we must visit in the worst case.