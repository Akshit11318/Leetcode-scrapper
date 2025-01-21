## Deepest Leaves Sum

**Problem Link:** https://leetcode.com/problems/deepest-leaves-sum/description

**Problem Statement:**
- Input: The root of a binary tree.
- Constraints: The number of nodes in the tree is in the range [1, 10^4].
- Expected Output: The sum of the values of the deepest leaves.
- Key Requirements and Edge Cases:
  - Handle empty trees (no nodes).
  - Single-node trees.
  - Balanced and unbalanced trees.
- Example Test Cases:
  - A tree with a single node should return the value of that node.
  - A balanced tree should return the sum of all leaf nodes at the deepest level.
  - An unbalanced tree should return the sum of all leaf nodes at the deepest level.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Traverse the tree to find all leaf nodes, then identify the deepest level and sum those leaf nodes.
- Step-by-step breakdown:
  1. Perform a depth-first search (DFS) to find all leaf nodes and their respective depths.
  2. Keep track of the maximum depth encountered.
  3. Sum the values of leaf nodes at the maximum depth.
- Why this approach comes to mind first: It directly addresses the problem by identifying all potential candidates (leaf nodes) and then filtering based on depth.

```cpp
// Brute Force Approach
class Solution {
public:
    int deepestLeavesSum(TreeNode* root) {
        if (!root) return 0;
        
        int maxDepth = 0;
        int sum = 0;
        
        dfs(root, 0, maxDepth, sum);
        
        return sum;
    }
    
    void dfs(TreeNode* node, int depth, int& maxDepth, int& sum) {
        if (!node) return;
        
        if (depth > maxDepth) {
            maxDepth = depth;
            sum = node->val;
        } else if (depth == maxDepth) {
            sum += node->val;
        }
        
        dfs(node->left, depth + 1, maxDepth, sum);
        dfs(node->right, depth + 1, maxDepth, sum);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree, since we visit each node once.
> - **Space Complexity:** $O(H)$, where $H$ is the height of the tree, due to the recursion stack. In the worst case, the tree is skewed, and $H = N$.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node. The space complexity is dependent on the height of the recursion stack, which is determined by the tree's height.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The optimal approach is essentially the same as the brute force approach but with a slight optimization in how we track and update the sum and maximum depth. This is because the problem requires visiting all nodes to determine the deepest leaves and their sum.
- Detailed breakdown: Perform a DFS, tracking the current depth and updating the maximum depth and sum as we encounter leaf nodes.
- Proof of optimality: Since we must visit each node at least once to determine if it's a leaf and its depth, any algorithm must have at least a linear time complexity. Thus, the given approach is optimal in terms of time complexity.

```cpp
// Optimal Approach
class Solution {
public:
    int deepestLeavesSum(TreeNode* root) {
        if (!root) return 0;
        
        int maxDepth = 0;
        int sum = 0;
        
        dfs(root, 0, maxDepth, sum);
        
        return sum;
    }
    
    void dfs(TreeNode* node, int depth, int& maxDepth, int& sum) {
        if (!node) return;
        
        if (depth > maxDepth) {
            maxDepth = depth;
            sum = node->val;
        } else if (depth == maxDepth) {
            sum += node->val;
        }
        
        if (node->left || node->right) {
            dfs(node->left, depth + 1, maxDepth, sum);
            dfs(node->right, depth + 1, maxDepth, sum);
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree.
> - **Space Complexity:** $O(H)$, where $H$ is the height of the tree.
> - **Optimality proof:** The time complexity is optimal because we visit each node exactly once, which is necessary to determine the deepest leaves and their sum.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: DFS, tracking maximum depth and sum in a tree traversal.
- Problem-solving patterns: Identifying the need to visit all nodes in a tree to solve a problem.
- Optimization techniques: Recognizing that sometimes, the brute force approach is already optimal in terms of time complexity.

**Mistakes to Avoid:**
- Not handling edge cases properly (e.g., empty tree, single-node tree).
- Failing to update the maximum depth and sum correctly during traversal.
- Not considering the space complexity implications of recursive solutions.