## Largest BST Subtree

**Problem Link:** https://leetcode.com/problems/largest-bst-subtree/description

**Problem Statement:**
- Input: The root of a binary tree.
- Constraints: The number of nodes in the tree is in the range [0, 10^4].
- Expected Output: The size of the largest binary search tree (BST) in the given binary tree.
- Key Requirements:
  - A binary search tree is a binary tree where for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node.
  - The size of a tree is the number of nodes in the tree.
- Example Test Cases:
  - Given the following tree: 
    ```
    10
   /  \
  5   15
 / \   \
1   8   7
```
    The largest BST subtree has 3 nodes.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible subtree to see if it is a BST and keeping track of the largest one found.
- This involves a depth-first search (DFS) approach where for each node, we check if the subtree rooted at that node is a BST.
- We use a helper function to check if a subtree is a BST and another to calculate the size of the subtree.

```cpp
class Solution {
public:
    int largestBSTSubtree(TreeNode* root) {
        int maxSize = 0;
        for (TreeNode* node = root; node != nullptr; node = node->right) {
            // This is a simplification and does not actually work as intended
            // It's meant to illustrate the brute force thought process
            if (isBST(node)) {
                maxSize = max(maxSize, size(node));
            }
        }
        return maxSize;
    }
    
    bool isBST(TreeNode* node) {
        if (node == nullptr) return true;
        if (node->left != nullptr && node->val <= node->left->val) return false;
        if (node->right != nullptr && node->val >= node->right->val) return false;
        return isBST(node->left) && isBST(node->right);
    }
    
    int size(TreeNode* node) {
        if (node == nullptr) return 0;
        return 1 + size(node->left) + size(node->right);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of nodes in the tree. This is because in the worst case, for each node, we are potentially checking all other nodes to see if they form a valid BST.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree. This is due to the recursive call stack.
> - **Why these complexities occur:** The brute force approach involves checking every possible subtree, leading to a high time complexity. The space complexity is due to the recursive calls.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves a post-order DFS traversal where we calculate the minimum and maximum values in the subtree rooted at each node, along with the size of the subtree.
- We use a struct to hold the results of the DFS traversal for each node: whether the subtree is a BST, the minimum value in the subtree, the maximum value in the subtree, and the size of the subtree.
- We update the maximum size of a BST subtree as we traverse the tree.

```cpp
class Solution {
public:
    int largestBSTSubtree(TreeNode* root) {
        int maxSize = 0;
        postOrder(root, maxSize);
        return maxSize;
    }
    
    struct Info {
        bool isBST;
        int minVal, maxVal, size;
    };
    
    Info postOrder(TreeNode* node, int& maxSize) {
        if (node == nullptr) {
            return {true, INT_MAX, INT_MIN, 0};
        }
        
        Info left = postOrder(node->left, maxSize);
        Info right = postOrder(node->right, maxSize);
        
        if (left.isBST && right.isBST && node->val > left.maxVal && node->val < right.minVal) {
            int size = left.size + right.size + 1;
            maxSize = max(maxSize, size);
            return {true, min(left.minVal, node->val), max(right.maxVal, node->val), size};
        } else {
            return {false, INT_MIN, INT_MAX, 0};
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we visit each node once during the post-order DFS traversal.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree. This is due to the recursive call stack.
> - **Optimality proof:** This approach is optimal because it visits each node exactly once, reducing the time complexity significantly compared to the brute force approach.

---

### Final Notes

**Learning Points:**
- The importance of using a post-order DFS traversal to calculate properties of subtrees.
- How to use a struct to hold multiple values returned from a recursive function.
- The trade-off between time and space complexity in different approaches.

**Mistakes to Avoid:**
- Not considering the properties of BSTs when designing the solution.
- Not using a post-order DFS traversal to calculate subtree properties efficiently.
- Not keeping track of the maximum size of a BST subtree found during the traversal.