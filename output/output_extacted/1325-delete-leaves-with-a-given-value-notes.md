## Delete Leaves With a Given Value
**Problem Link:** https://leetcode.com/problems/delete-leaves-with-a-given-value/description

**Problem Statement:**
- Input format and constraints: The problem involves a binary tree and two integers, `target` and `value`. We need to delete all the leaves with the given `value`.
- Expected output format: The function should return the root of the modified binary tree.
- Key requirements and edge cases to consider: The function should handle cases where the tree is empty, the tree has only one node, or the tree has multiple nodes with the given `value`.
- Example test cases with explanations:
  - Example 1: 
    - Input: root = [1,1,1], target = 1, value = 1
    - Output: [1,null,null,1]
    - Explanation: The tree is [1,1,1], and we need to delete all the leaves with value 1. After deletion, the tree becomes [1,null,null,1].
  - Example 2: 
    - Input: root = [1,3,3,3], target = 3, value = 3
    - Output: [1,null,null,null]
    - Explanation: The tree is [1,3,3,3], and we need to delete all the leaves with value 3. After deletion, the tree becomes [1,null,null,null].

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The first approach that comes to mind is to traverse the tree and delete all the leaves with the given `value`. We can use a recursive approach to traverse the tree and delete the leaves.
- Step-by-step breakdown of the solution:
  1. Define a recursive function to traverse the tree.
  2. In the recursive function, check if the current node is a leaf and its value is equal to the given `value`.
  3. If the current node is a leaf and its value is equal to the given `value`, return `nullptr` to delete the node.
  4. If the current node is not a leaf, recursively traverse its left and right subtrees.
  5. If the left or right subtree of the current node is deleted, update the left or right child of the current node to `nullptr`.
- Why this approach comes to mind first: This approach is straightforward and easy to implement. It involves traversing the tree and deleting the leaves with the given `value`.

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
    TreeNode* removeLeafNodes(TreeNode* root, int target, int value) {
        if (!root) return nullptr;
        
        root->left = removeLeafNodes(root->left, target, value);
        root->right = removeLeafNodes(root->right, target, value);
        
        if (root->val == value && !root->left && !root->right) return nullptr;
        
        return root;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we are traversing the tree once.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree. This is because of the recursive call stack.
> - **Why these complexities occur:** The time complexity occurs because we are traversing the tree once, and the space complexity occurs because of the recursive call stack.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is similar to the brute force approach. However, we can optimize the solution by avoiding unnecessary recursive calls.
- Detailed breakdown of the approach:
  1. Define a recursive function to traverse the tree.
  2. In the recursive function, check if the current node is a leaf and its value is equal to the given `value`.
  3. If the current node is a leaf and its value is equal to the given `value`, return `nullptr` to delete the node.
  4. If the current node is not a leaf, recursively traverse its left and right subtrees.
  5. If the left or right subtree of the current node is deleted, update the left or right child of the current node to `nullptr`.
- Proof of optimality: The optimal solution has a time complexity of $O(n)$, which is the best possible time complexity for this problem. This is because we need to traverse the tree at least once to delete the leaves with the given `value`.
- Why further optimization is impossible: Further optimization is impossible because we need to traverse the tree at least once to delete the leaves with the given `value`. Any optimization would require traversing the tree in less than $O(n)$ time, which is not possible.

```cpp
class Solution {
public:
    TreeNode* removeLeafNodes(TreeNode* root, int target, int value) {
        if (!root) return nullptr;
        
        root->left = removeLeafNodes(root->left, target, value);
        root->right = removeLeafNodes(root->right, target, value);
        
        if (root->val == value && !root->left && !root->right) return nullptr;
        
        return root;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we are traversing the tree once.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree. This is because of the recursive call stack.
> - **Optimality proof:** The optimal solution has a time complexity of $O(n)$, which is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of recursive functions to traverse a binary tree and delete nodes.
- Problem-solving patterns identified: The problem requires identifying the base case for the recursion and handling the recursive calls.
- Optimization techniques learned: The problem demonstrates the use of recursive functions to optimize the solution.
- Similar problems to practice: Similar problems to practice include deleting nodes from a binary tree, traversing a binary tree, and optimizing recursive functions.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is not handling the base case for the recursion correctly.
- Edge cases to watch for: Edge cases to watch for include handling an empty tree, a tree with one node, and a tree with multiple nodes with the given `value`.
- Performance pitfalls: A performance pitfall is not optimizing the recursive function calls.
- Testing considerations: Testing considerations include testing the function with different inputs, including an empty tree, a tree with one node, and a tree with multiple nodes with the given `value`.