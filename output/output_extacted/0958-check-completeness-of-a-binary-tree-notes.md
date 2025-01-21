## Check Completeness of a Binary Tree

**Problem Link:** https://leetcode.com/problems/check-completeness-of-a-binary-tree/description

**Problem Statement:**
- Input: A binary tree's root node.
- Output: A boolean indicating whether the binary tree is complete.
- Key requirements:
  - A complete binary tree is a binary tree in which all the levels are completely filled except possibly the last level, which is filled from left to right.
  - Edge cases: Empty tree, tree with one node, unbalanced trees.
- Example test cases:
  - A tree with levels fully filled is complete.
  - A tree with the last level not fully filled from left to right is not complete.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Count the number of nodes and compare it with the maximum possible nodes in a complete binary tree of the same height.
- Step-by-step breakdown:
  1. Calculate the height of the tree.
  2. Calculate the maximum possible nodes in a complete binary tree of that height.
  3. Count the actual number of nodes in the tree.
  4. Compare the actual node count with the maximum possible nodes.

```cpp
class Solution {
public:
    bool isCompleteTree(TreeNode* root) {
        if (!root) return true;
        
        // Calculate the height of the tree
        int height = getHeight(root);
        
        // Calculate the maximum possible nodes in a complete binary tree of that height
        int maxNodes = (1 << height) - 1;
        
        // Count the actual number of nodes in the tree
        int actualNodes = countNodes(root);
        
        return actualNodes == maxNodes;
    }
    
    int getHeight(TreeNode* node) {
        if (!node) return 0;
        return 1 + max(getHeight(node->left), getHeight(node->right));
    }
    
    int countNodes(TreeNode* node) {
        if (!node) return 0;
        return 1 + countNodes(node->left) + countNodes(node->right);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to calculating the height and counting nodes, where $n$ is the number of nodes in the tree. The height calculation itself is $O(\log n)$ for a balanced tree, but since we do it for every node in the worst case, it becomes $O(n \log n)$.
> - **Space Complexity:** $O(\log n)$ due to the recursive call stack for calculating the height and counting nodes.
> - **Why these complexities occur:** The brute force approach involves multiple passes over the tree (to calculate height and count nodes), leading to higher time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: A complete binary tree can be identified by performing a level-order traversal and checking for any gaps in the node sequence.
- Detailed breakdown:
  1. Perform a level-order traversal of the tree.
  2. During the traversal, check for any `nullptr` values before encountering the end of the level.
  3. If a `nullptr` is found before the end of the level, the tree is not complete.

```cpp
class Solution {
public:
    bool isCompleteTree(TreeNode* root) {
        if (!root) return true;
        
        queue<TreeNode*> q;
        q.push(root);
        bool seenNull = false;
        
        while (!q.empty()) {
            TreeNode* node = q.front();
            q.pop();
            
            if (node) {
                if (seenNull) return false; // If we've seen a null and now see a node, tree is not complete
                q.push(node->left);
                q.push(node->right);
            } else {
                seenNull = true; // First null encountered, mark it
            }
        }
        
        return true; // If we've traversed the entire tree without returning false, it's complete
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, since we visit each node exactly once during the level-order traversal.
> - **Space Complexity:** $O(n)$ for the queue in the worst case (when the tree is a complete binary tree and all levels are fully filled).
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the tree, checking each node's presence and order, which is necessary to determine completeness.

---

### Final Notes

**Learning Points:**
- The importance of level-order traversal in tree problems.
- How to identify a complete binary tree by checking for gaps in node sequence during traversal.
- Optimization techniques: reducing the number of passes over the data structure.

**Mistakes to Avoid:**
- Incorrectly assuming that a tree is complete based solely on its height and node count.
- Failing to check for gaps in the node sequence during traversal.
- Not considering edge cases like an empty tree or a tree with one node.