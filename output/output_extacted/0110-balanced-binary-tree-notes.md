## Balanced Binary Tree
**Problem Link:** https://leetcode.com/problems/balanced-binary-tree/description

**Problem Statement:**
- Input: The root of a binary tree.
- Output: A boolean indicating whether the tree is balanced.
- Key requirements: A binary tree is balanced if the absolute difference between the heights of its left and right subtrees does not exceed 1 for all nodes.
- Edge cases: An empty tree is considered balanced.

**Example Test Cases:**
- Example 1:
  - Input: `root = [3,9,20,null,null,15,7]`
  - Output: `true`
  - Explanation: The absolute difference between the heights of the left and right subtrees of every node does not exceed 1.
- Example 2:
  - Input: `root = [1,2,2,3,3,null,null,4,4]`
  - Output: `false`
  - Explanation: The absolute difference between the heights of the left and right subtrees of the root node exceeds 1.

---

### Brute Force Approach
**Explanation:**
- Calculate the height of the left and right subtrees for each node recursively.
- Compare the absolute difference of these heights to determine if the tree is balanced.
- This approach comes to mind first because it directly checks the condition for a balanced binary tree.

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
    bool isBalanced(TreeNode* root) {
        if (root == nullptr) return true;
        
        int leftHeight = getHeight(root->left);
        int rightHeight = getHeight(root->right);
        
        return (abs(leftHeight - rightHeight) <= 1) && 
               isBalanced(root->left) && 
               isBalanced(root->right);
    }
    
    int getHeight(TreeNode* node) {
        if (node == nullptr) return 0;
        return 1 + max(getHeight(node->left), getHeight(node->right));
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ in the worst case, where $n$ is the number of nodes in the tree, because for each node, we calculate the height of its subtrees, potentially leading to repeated calculations.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree, due to the recursive call stack.
> - **Why these complexities occur:** The brute force approach involves recursive calls for calculating the height of each subtree and checking if the tree is balanced. This leads to potential repeated calculations for the heights of subtrees, increasing the time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Instead of calculating the height of each subtree separately, we can calculate the height and check if the tree is balanced in a single pass by returning the height if the tree is balanced and -1 if it's not.
- This approach avoids the repeated calculations of subtree heights.

```cpp
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        return check(root) != -1;
    }
    
    int check(TreeNode* node) {
        if (node == nullptr) return 0;
        
        int leftHeight = check(node->left);
        if (leftHeight == -1) return -1; // Left subtree is not balanced
        
        int rightHeight = check(node->right);
        if (rightHeight == -1) return -1; // Right subtree is not balanced
        
        if (abs(leftHeight - rightHeight) > 1) return -1; // Current node is not balanced
        
        return 1 + max(leftHeight, rightHeight); // Return the height if balanced
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, because we visit each node once.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree, due to the recursive call stack.
> - **Optimality proof:** This is the optimal approach because we only visit each node once and perform a constant amount of work for each node, resulting in linear time complexity.

---

### Final Notes

**Learning Points:**
- The importance of avoiding repeated calculations in recursive problems.
- How to transform a problem that initially seems to require multiple passes into one that can be solved in a single pass.
- The use of recursion to solve tree problems and how to optimize recursive solutions.

**Mistakes to Avoid:**
- Not considering the possibility of early returns to simplify code and improve performance.
- Failing to recognize when a problem can be solved with a single pass, leading to inefficient solutions.
- Not optimizing recursive functions to avoid repeated work, which can significantly impact performance for large inputs.