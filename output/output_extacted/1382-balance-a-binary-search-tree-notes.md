## Balance a Binary Search Tree
**Problem Link:** https://leetcode.com/problems/balance-a-binary-search-tree/description

**Problem Statement:**
- Input: The root of a binary search tree.
- Constraints: The number of nodes in the tree is in the range [1, 10^4].
- Expected output: The root of the balanced binary search tree.
- Key requirements: The output tree should be a binary search tree and should be balanced, meaning the absolute difference between the heights of its left and right subtrees should not exceed 1 for all nodes.
- Example test cases:
  - Input: root = [1,null,2,null,3,null,4,null,null,null]
  - Output: [2]
  - Explanation: The tree is not balanced because the left subtree of the root node is empty and the right subtree has a height of 3.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One way to balance a binary search tree is to first flatten it into a sorted array, and then reconstruct a balanced binary search tree from the sorted array.
- Step-by-step breakdown of the solution:
  1. Perform an in-order traversal of the binary search tree to get a sorted array of its nodes.
  2. Use the sorted array to construct a balanced binary search tree.
- Why this approach comes to mind first: It is a straightforward approach that ensures the resulting tree is balanced, as we are essentially rebuilding the tree from a sorted array.

```cpp
// Brute force approach
class Solution {
public:
    vector<int> inorder;
    TreeNode* balanceBST(TreeNode* root) {
        // Perform in-order traversal to get a sorted array
        inOrderTraversal(root);
        
        // Reconstruct a balanced binary search tree
        return sortedArrayToBST(inorder, 0, inorder.size() - 1);
    }
    
    void inOrderTraversal(TreeNode* node) {
        if (!node) return;
        inOrderTraversal(node->left);
        inorder.push_back(node->val);
        inOrderTraversal(node->right);
    }
    
    TreeNode* sortedArrayToBST(vector<int>& nums, int start, int end) {
        if (start > end) return nullptr;
        int mid = start + (end - start) / 2;
        TreeNode* node = new TreeNode(nums[mid]);
        node->left = sortedArrayToBST(nums, start, mid - 1);
        node->right = sortedArrayToBST(nums, mid + 1, end);
        return node;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we perform an in-order traversal of the tree and then reconstruct a balanced binary search tree.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we store the in-order traversal of the tree in a vector.
> - **Why these complexities occur:** The time complexity occurs because we visit each node in the tree once during the in-order traversal and once during the reconstruction of the balanced binary search tree. The space complexity occurs because we store the in-order traversal of the tree in a vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use the same approach as the brute force solution, but with a more efficient implementation.
- Detailed breakdown of the approach:
  1. Perform an in-order traversal of the binary search tree to get a sorted array of its nodes.
  2. Use the sorted array to construct a balanced binary search tree.
- Proof of optimality: This approach is optimal because it ensures the resulting tree is balanced and has a time complexity of $O(n)$.

```cpp
// Optimal approach
class Solution {
public:
    vector<int> inorder;
    TreeNode* balanceBST(TreeNode* root) {
        // Perform in-order traversal to get a sorted array
        inOrderTraversal(root);
        
        // Reconstruct a balanced binary search tree
        return sortedArrayToBST(0, inorder.size() - 1);
    }
    
    void inOrderTraversal(TreeNode* node) {
        if (!node) return;
        inOrderTraversal(node->left);
        inorder.push_back(node->val);
        inOrderTraversal(node->right);
    }
    
    TreeNode* sortedArrayToBST(int start, int end) {
        if (start > end) return nullptr;
        int mid = start + (end - start) / 2;
        TreeNode* node = new TreeNode(inorder[mid]);
        node->left = sortedArrayToBST(start, mid - 1);
        node->right = sortedArrayToBST(mid + 1, end);
        return node;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree.
> - **Optimality proof:** This approach is optimal because it ensures the resulting tree is balanced and has a time complexity of $O(n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: In-order traversal, balanced binary search tree construction.
- Problem-solving patterns identified: Using a sorted array to construct a balanced binary search tree.
- Optimization techniques learned: Using a more efficient implementation of the brute force solution.
- Similar problems to practice: Constructing a balanced binary search tree from a sorted array, finding the minimum height of a binary search tree.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty tree.
- Edge cases to watch for: An empty tree, a tree with a single node.
- Performance pitfalls: Using an inefficient implementation of the in-order traversal or balanced binary search tree construction.
- Testing considerations: Testing the solution with different input trees, including edge cases.