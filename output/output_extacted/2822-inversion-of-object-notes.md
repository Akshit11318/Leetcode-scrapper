## Inversion of Object
**Problem Link:** https://leetcode.com/problems/inversion-of-object/description

**Problem Statement:**
- Input format and constraints: Given a binary tree, we need to invert the object, i.e., swap the left and right child of each node.
- Expected output format: The inverted binary tree.
- Key requirements and edge cases to consider: 
  - The input tree can be empty.
  - The tree can have nodes with only one child.
- Example test cases with explanations: 
  - Test case 1: Input: [4,2,7,1,3,6,9], Output: [4,7,2,9,6,3,1]
  - Test case 2: Input: [2,1,3], Output: [2,3,1]

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Start from the root node and recursively traverse the tree. For each node, swap its left and right child.
- Step-by-step breakdown of the solution:
  1. Check if the current node is NULL. If it is, return NULL.
  2. Swap the left and right child of the current node.
  3. Recursively invert the left and right subtree.
- Why this approach comes to mind first: This is the most straightforward way to invert a binary tree. We simply need to swap the left and right child of each node.

```cpp
// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (root == NULL) {
            return NULL;
        }
        // Swap the left and right child
        TreeNode* temp = root->left;
        root->left = root->right;
        root->right = temp;
        
        // Recursively invert the left and right subtree
        root->left = invertTree(root->left);
        root->right = invertTree(root->right);
        
        return root;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where n is the number of nodes in the tree. This is because we visit each node once.
> - **Space Complexity:** $O(h)$, where h is the height of the tree. This is because of the recursive call stack.
> - **Why these complexities occur:** The time complexity is $O(n)$ because we visit each node once. The space complexity is $O(h)$ because of the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use the same approach as the brute force solution, but with some minor optimizations. However, the time and space complexity remain the same.
- Detailed breakdown of the approach: 
  1. Check if the current node is NULL. If it is, return NULL.
  2. Swap the left and right child of the current node.
  3. Recursively invert the left and right subtree.
- Proof of optimality: This is the optimal solution because we need to visit each node at least once to invert the tree. Therefore, the time complexity cannot be improved.

```cpp
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (root == NULL) {
            return NULL;
        }
        // Swap the left and right child
        TreeNode* temp = root->left;
        root->left = invertTree(root->right);
        root->right = invertTree(temp);
        
        return root;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where n is the number of nodes in the tree. This is because we visit each node once.
> - **Space Complexity:** $O(h)$, where h is the height of the tree. This is because of the recursive call stack.
> - **Optimality proof:** This is the optimal solution because we need to visit each node at least once to invert the tree. Therefore, the time complexity cannot be improved.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Tree traversal, recursion.
- Problem-solving patterns identified: Inverting a binary tree.
- Optimization techniques learned: None, as this is already the optimal solution.
- Similar problems to practice: 
  - [LeetCode 226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
  - [LeetCode 100. Same Tree](https://leetcode.com/problems/same-tree/)

**Mistakes to Avoid:**
- Common implementation errors: Not checking for NULL nodes before accessing their children.
- Edge cases to watch for: Empty trees, trees with only one child.
- Performance pitfalls: Using an iterative approach with a queue can also solve this problem, but it may have a higher constant factor than the recursive approach.
- Testing considerations: Test the function with different types of binary trees, including empty trees, trees with only one child, and trees with multiple children.