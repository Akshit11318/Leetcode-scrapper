## Root Equals Sum of Children
**Problem Link:** https://leetcode.com/problems/root-equals-sum-of-children/description

**Problem Statement:**
- Input: The root of a binary tree where each node has a unique integer value.
- Output: True if the root's value is equal to the sum of its children's values, False otherwise.
- Key requirements and edge cases to consider:
  - The tree can be empty.
  - A node can have zero, one, or two children.
  - The tree is not necessarily a binary search tree.
- Example test cases with explanations:
  - For the tree with root node having value 10, left child having value 4, and right child having value 6, the output should be True because 10 equals 4 + 6.
  - For an empty tree, the output should be True as there's no root to compare.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check if the tree is empty. If not, calculate the sum of the children's values and compare it with the root's value.
- Step-by-step breakdown of the solution:
  1. Check if the tree is empty. If it is, return True.
  2. If the tree is not empty, check if the root node has children.
  3. Calculate the sum of the children's values.
  4. Compare the sum of the children's values with the root's value.
- Why this approach comes to mind first: It's straightforward and directly addresses the problem statement.

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool checkTree(TreeNode* root) {
        // Check if the tree is empty
        if (root == nullptr) return true;
        
        // Calculate the sum of the children's values
        int sum = 0;
        if (root->left != nullptr) sum += root->left->val;
        if (root->right != nullptr) sum += root->right->val;
        
        // Compare the sum of the children's values with the root's value
        return root->val == sum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because we're performing a constant number of operations regardless of the tree's size.
> - **Space Complexity:** $O(1)$ because we're using a constant amount of space to store the sum and the result.
> - **Why these complexities occur:** The operations are constant and do not depend on the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved in a single pass by checking the root's value against the sum of its children's values.
- Detailed breakdown of the approach:
  1. Check if the tree is empty. If it is, return True.
  2. If the tree is not empty, calculate the sum of the children's values.
  3. Compare the sum of the children's values with the root's value.
- Proof of optimality: This approach is optimal because it only requires a single pass through the tree and uses a constant amount of space.

```cpp
class Solution {
public:
    bool checkTree(TreeNode* root) {
        // Check if the tree is empty
        if (root == nullptr) return true;
        
        // Calculate the sum of the children's values
        int sum = (root->left ? root->left->val : 0) + (root->right ? root->right->val : 0);
        
        // Compare the sum of the children's values with the root's value
        return root->val == sum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because we're performing a constant number of operations regardless of the tree's size.
> - **Space Complexity:** $O(1)$ because we're using a constant amount of space to store the sum and the result.
> - **Optimality proof:** The approach is optimal because it only requires a single pass through the tree and uses a constant amount of space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Tree traversal, conditional checks.
- Problem-solving patterns identified: Checking for edge cases, using conditional statements to handle different scenarios.
- Optimization techniques learned: Using constant space, minimizing the number of operations.
- Similar problems to practice: Other tree-related problems, such as checking if a tree is balanced or finding the maximum depth of a tree.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, using incorrect conditional statements.
- Edge cases to watch for: Empty trees, trees with a single node, trees with multiple nodes.
- Performance pitfalls: Using excessive space or time complexity.
- Testing considerations: Test with different types of trees, including empty trees and trees with a single node.