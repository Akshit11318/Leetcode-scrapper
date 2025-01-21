## Invert Binary Tree

**Problem Link:** https://leetcode.com/problems/invert-binary-tree/description

**Problem Statement:**
- Input format: The root of a binary tree.
- Constraints: The number of nodes in the tree is in the range [0, 100].
- Expected output format: The root of the inverted binary tree.
- Key requirements and edge cases to consider: 
  - The input tree can be empty (i.e., `root` is `nullptr`).
  - The input tree can be a single node.
  - The input tree can be unbalanced.
- Example test cases with explanations:
  - Example 1: Input: `root = [4,2,7,1,3,6,9]`, Output: `[4,7,2,9,6,3,1]`
  - Example 2: Input: `root = [2,1,3]`, Output: `[2,3,1]`
  - Example 3: Input: `root = []`, Output: `[]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To invert a binary tree, we need to swap the left and right child nodes of each internal node.
- Step-by-step breakdown of the solution: 
  1. Start with the root node.
  2. If the root is `nullptr`, return `nullptr`.
  3. Swap the left and right child nodes of the root.
  4. Recursively invert the left and right subtrees.
- Why this approach comes to mind first: It directly addresses the problem statement by swapping child nodes.

```cpp
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        // Base case: if the tree is empty, return nullptr
        if (root == nullptr) {
            return nullptr;
        }
        
        // Swap the left and right child nodes
        TreeNode* temp = root->left;
        root->left = root->right;
        root->right = temp;
        
        // Recursively invert the left and right subtrees
        root->left = invertTree(root->left);
        root->right = invertTree(root->right);
        
        return root;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. We visit each node once.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree. This is the maximum depth of the recursive call stack.
> - **Why these complexities occur:** We traverse the tree once, visiting each node, and the recursive call stack can grow up to the height of the tree.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal because we must visit each node to invert the tree. However, we can slightly improve the code by reducing the number of operations.
- Detailed breakdown of the approach: 
  1. Start with the root node.
  2. If the root is `nullptr`, return `nullptr`.
  3. Swap the left and right child nodes of the root.
  4. Recursively invert the left and right subtrees.
- Proof of optimality: We must visit each node at least once to invert the tree, so the time complexity cannot be improved beyond $O(n)$.

```cpp
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (root == nullptr) return nullptr;
        TreeNode* temp = root->left;
        root->left = invertTree(root->right);
        root->right = invertTree(temp);
        return root;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree.
> - **Optimality proof:** The time complexity is optimal because we must visit each node. The space complexity is also optimal because we need at least $O(h)$ space for the recursive call stack.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Tree traversal, recursion.
- Problem-solving patterns identified: Divide and conquer, swapping nodes.
- Optimization techniques learned: Reducing the number of operations.
- Similar problems to practice: Tree traversal problems, such as inorder, preorder, and postorder traversal.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle the base case (`root == nullptr`).
- Edge cases to watch for: Empty tree, single-node tree, unbalanced tree.
- Performance pitfalls: Using unnecessary operations or recursive calls.
- Testing considerations: Test with different tree structures, including empty and single-node trees.