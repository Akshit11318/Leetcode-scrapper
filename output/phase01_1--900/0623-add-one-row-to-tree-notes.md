## Add One Row to Tree

**Problem Link:** https://leetcode.com/problems/add-one-row-to-tree/description

**Problem Statement:**
- Input: The root of a binary tree and the values of a new row.
- Constraints: The number of nodes in the tree is in the range $[1, 10^4]$.
- Expected output: The root of the modified binary tree.
- Key requirements and edge cases to consider: The new row should be added at a given depth. If the depth is 1, the new row should be added as the root. If the depth is greater than the height of the tree, the new row should not be added.
- Example test cases with explanations:
  - Test case 1: Add a new row to the root of the tree.
  - Test case 2: Add a new row at a depth greater than the height of the tree.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Perform a depth-first search (DFS) traversal of the tree to find the nodes at the desired depth.
- Step-by-step breakdown of the solution:
  1. Define a recursive function to perform DFS traversal.
  2. Keep track of the current depth during traversal.
  3. When the desired depth is reached, add the new row.
- Why this approach comes to mind first: It is straightforward to traverse the tree and add the new row at the desired depth.

```cpp
class Solution {
public:
    TreeNode* addOneRow(TreeNode* root, int val, int depth) {
        if (depth == 1) {
            TreeNode* newRoot = new TreeNode(val);
            newRoot->left = root;
            return newRoot;
        }
        
        addRow(root, val, depth, 1);
        return root;
    }
    
    void addRow(TreeNode* node, int val, int depth, int currentDepth) {
        if (node == nullptr) return;
        
        if (currentDepth == depth - 1) {
            TreeNode* newLeft = new TreeNode(val);
            TreeNode* newRight = new TreeNode(val);
            newLeft->left = node->left;
            newRight->right = node->right;
            node->left = newLeft;
            node->right = newRight;
        } else {
            addRow(node->left, val, depth, currentDepth + 1);
            addRow(node->right, val, depth, currentDepth + 1);
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we visit each node once during the DFS traversal.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree. This is because of the recursive call stack.
> - **Why these complexities occur:** The time complexity is linear because we visit each node once. The space complexity is related to the height of the tree because of the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a similar approach as the brute force solution but with some optimizations.
- Detailed breakdown of the approach:
  1. Handle the case where the depth is 1 separately.
  2. Perform a DFS traversal to find the nodes at the desired depth.
  3. Add the new row at the desired depth.
- Proof of optimality: This solution has the same time and space complexity as the brute force solution but with some minor optimizations.
- Why further optimization is impossible: The time complexity is already linear, and the space complexity is already optimal for this problem.

```cpp
class Solution {
public:
    TreeNode* addOneRow(TreeNode* root, int val, int depth) {
        if (depth == 1) {
            TreeNode* newRoot = new TreeNode(val);
            newRoot->left = root;
            return newRoot;
        }
        
        addRow(root, val, depth, 1);
        return root;
    }
    
    void addRow(TreeNode* node, int val, int depth, int currentDepth) {
        if (node == nullptr) return;
        
        if (currentDepth == depth - 1) {
            TreeNode* newLeft = new TreeNode(val);
            TreeNode* newRight = new TreeNode(val);
            newLeft->left = node->left;
            newRight->right = node->right;
            node->left = newLeft;
            node->right = newRight;
        } else if (currentDepth < depth - 1) {
            addRow(node->left, val, depth, currentDepth + 1);
            addRow(node->right, val, depth, currentDepth + 1);
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree.
> - **Optimality proof:** This solution has the same time and space complexity as the brute force solution but with some minor optimizations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS traversal, recursive functions.
- Problem-solving patterns identified: Handling edge cases, optimizing recursive functions.
- Optimization techniques learned: Minor optimizations in the recursive function.
- Similar problems to practice: Other tree-related problems, such as tree traversal and tree modification.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, not optimizing recursive functions.
- Edge cases to watch for: Depth 1, depth greater than the height of the tree.
- Performance pitfalls: Not optimizing the recursive function, which can lead to stack overflow for large trees.
- Testing considerations: Test the function with different inputs, including edge cases.