## Smallest Subtree with all the Deepest Nodes

**Problem Link:** https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description

**Problem Statement:**
- Input: The root of a binary tree.
- Expected output: The root of the smallest subtree that contains all the deepest nodes.
- Key requirements: 
  - The subtree must contain all the deepest nodes.
  - The subtree should be as small as possible.
- Edge cases to consider: 
  - An empty tree.
  - A tree with a single node.
  - A tree with two nodes.

**Example Test Cases:**
- Example 1:
  - Input: root = [3,5,1,6,2,0,8,null,null,7,4]
  - Output: [2,7,4]
  - Explanation: We return the node with value 3, and the nodes 5, 3 and 2 itself. The answer is [2,7,4] because of the tie.
- Example 2:
  - Input: root = [1]
  - Output: [1]
  - Explanation: The root is the deepest node, we return it.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to traverse the tree, find the deepest level, and then try to find the smallest subtree that includes all nodes at that level.
- We can use a recursive approach to find the deepest level and then another recursive approach to find the smallest subtree.
- However, this approach comes to mind first because it directly addresses the requirements but does not consider optimization.

```cpp
class Solution {
public:
    TreeNode* subtreeWithAllDeepest(TreeNode* root) {
        if (!root) return nullptr;
        
        int maxDepth = getMaxDepth(root);
        
        return findSmallestSubtree(root, maxDepth);
    }
    
    int getMaxDepth(TreeNode* node) {
        if (!node) return 0;
        return 1 + max(getMaxDepth(node->left), getMaxDepth(node->right));
    }
    
    TreeNode* findSmallestSubtree(TreeNode* node, int maxDepth) {
        if (!node) return nullptr;
        
        int leftDepth = getMaxDepth(node->left);
        int rightDepth = getMaxDepth(node->right);
        
        if (leftDepth == maxDepth && rightDepth == maxDepth) {
            return node;
        } else if (leftDepth == maxDepth) {
            return findSmallestSubtree(node->left, maxDepth);
        } else if (rightDepth == maxDepth) {
            return findSmallestSubtree(node->right, maxDepth);
        } else {
            return node;
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of nodes in the tree. This is because we are recursively finding the maximum depth for each node and then recursively finding the smallest subtree.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree, due to the recursive call stack.
> - **Why these complexities occur:** These complexities occur because of the nested recursive calls for finding the maximum depth and then finding the smallest subtree.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to find the maximum depth and the nodes at that depth in a single pass.
- We can use a recursive approach to find the maximum depth and the nodes at that depth.
- We keep track of the nodes at the maximum depth and the parent of these nodes.
- If there are multiple nodes at the maximum depth and they have a common parent, we return that parent. Otherwise, we return the node with the maximum depth.

```cpp
class Solution {
public:
    TreeNode* subtreeWithAllDeepest(TreeNode* root) {
        if (!root) return nullptr;
        
        int maxDepth = 0;
        TreeNode* result = nullptr;
        
        dfs(root, 0, maxDepth, result);
        
        return result;
    }
    
    int dfs(TreeNode* node, int depth, int& maxDepth, TreeNode*& result) {
        if (!node) return depth;
        
        int leftDepth = dfs(node->left, depth + 1, maxDepth, result);
        int rightDepth = dfs(node->right, depth + 1, maxDepth, result);
        
        if (leftDepth == rightDepth && leftDepth > maxDepth) {
            maxDepth = leftDepth;
            result = node;
        } else if (leftDepth > maxDepth) {
            maxDepth = leftDepth;
        } else if (rightDepth > maxDepth) {
            maxDepth = rightDepth;
        }
        
        return max(leftDepth, rightDepth);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we are making a single pass through the tree.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree, due to the recursive call stack.
> - **Optimality proof:** This is the optimal solution because we are making a single pass through the tree and keeping track of the necessary information.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the use of a recursive approach to find the maximum depth and the nodes at that depth in a single pass.
- The problem-solving pattern identified is to keep track of the necessary information in a single pass.
- The optimization technique learned is to avoid making multiple passes through the tree.

**Mistakes to Avoid:**
- A common implementation error is to make multiple passes through the tree.
- An edge case to watch for is when the tree is empty or has a single node.
- A performance pitfall is to use a brute force approach that has a high time complexity.