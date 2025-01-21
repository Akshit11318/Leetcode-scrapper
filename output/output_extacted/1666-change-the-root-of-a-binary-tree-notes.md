## Change the Root of a Binary Tree

**Problem Link:** https://leetcode.com/problems/change-the-root-of-a-binary-tree/description

**Problem Statement:**
- Input format: A binary tree `root` and an integer `node` representing the new root of the tree.
- Constraints: The binary tree is non-empty, and the `node` exists in the tree.
- Expected output format: The new root of the binary tree.
- Key requirements and edge cases to consider: Finding the new root node in the tree, updating the parent-child relationships, and handling edge cases such as an empty tree or a non-existent new root node.

**Example Test Cases:**
- Example 1: Given a binary tree `root = [3,5,1,6,2,0,8,null,null,7,4]` and `node = 5`, the new root of the tree is `5`.
- Example 2: Given a binary tree `root = [3,5,1,6,2,0,8,null,null,7,4]` and `node = 1`, the new root of the tree is `1`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To change the root of a binary tree, we need to find the new root node in the tree and update the parent-child relationships.
- Step-by-step breakdown of the solution:
  1. Find the new root node in the tree by traversing the tree and checking if the current node's value matches the new root node's value.
  2. Update the parent-child relationships by making the new root node the root of the tree and updating the parent pointers of the other nodes.
- Why this approach comes to mind first: This approach is straightforward and involves a simple tree traversal to find the new root node.

```cpp
// Brute Force Approach
TreeNode* changeRoot(TreeNode* root, int node) {
    if (!root) return NULL;
    if (root->val == node) return root;
    TreeNode* newRoot = changeRoot(root->left, node);
    if (newRoot) return newRoot;
    return changeRoot(root->right, node);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, because we may need to traverse the entire tree to find the new root node.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree, because of the recursive call stack.
> - **Why these complexities occur:** The time complexity occurs because we need to traverse the tree to find the new root node, and the space complexity occurs because of the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of traversing the tree to find the new root node, we can use a `TreeNode` pointer to keep track of the current node and its parent node.
- Detailed breakdown of the approach:
  1. Initialize a `TreeNode` pointer `current` to the root of the tree and a `TreeNode` pointer `parent` to `NULL`.
  2. Traverse the tree until we find the new root node.
  3. Update the parent-child relationships by making the new root node the root of the tree and updating the parent pointers of the other nodes.
- Proof of optimality: This approach is optimal because it only requires a single traversal of the tree to find the new root node.

```cpp
// Optimal Approach
TreeNode* changeRoot(TreeNode* root, int node) {
    if (!root) return NULL;
    TreeNode* current = root;
    TreeNode* parent = NULL;
    while (current && current->val != node) {
        parent = current;
        if (current->val < node) current = current->right;
        else current = current->left;
    }
    if (!current) return NULL;
    if (parent) {
        if (parent->left == current) parent->left = current->right;
        else parent->right = current->right;
    }
    if (current->right) current->right->parent = parent;
    return current;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(h)$, where $h$ is the height of the tree, because we only need to traverse the tree until we find the new root node.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the current node and its parent node.
> - **Optimality proof:** This approach is optimal because it only requires a single traversal of the tree to find the new root node.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Tree traversal, recursive functions, and pointer manipulation.
- Problem-solving patterns identified: Finding a specific node in a tree, updating parent-child relationships, and handling edge cases.
- Optimization techniques learned: Using a `TreeNode` pointer to keep track of the current node and its parent node.
- Similar problems to practice: Finding the lowest common ancestor of two nodes in a tree, deleting a node from a tree, and inserting a node into a tree.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for `NULL` pointers, not updating parent pointers correctly, and not handling edge cases.
- Edge cases to watch for: An empty tree, a non-existent new root node, and a tree with a single node.
- Performance pitfalls: Using a brute force approach that traverses the entire tree to find the new root node.
- Testing considerations: Testing the function with different tree structures and edge cases to ensure correctness and efficiency.