## Find Bottom Left Tree Value

**Problem Link:** https://leetcode.com/problems/find-bottom-left-tree-value/description

**Problem Statement:**
- Input: The root of a binary tree.
- Constraints: The number of nodes in the tree is in the range `[1, 10^4]`.
- Output: The value of the bottom left node in the binary tree.
- Key requirements: 
  - The tree is not guaranteed to be balanced.
  - All node values are unique.
- Edge cases to consider:
  - The tree has only one node.
  - The tree has multiple levels.
- Example test cases:
  - A balanced tree with unique values.
  - An unbalanced tree with unique values.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves traversing the tree level by level to find the bottom left node.
- Step-by-step breakdown:
  1. Initialize a queue with the root node.
  2. Perform a level order traversal (BFS) of the tree.
  3. Keep track of the current level and the first node encountered at each level.
  4. Update the result with the value of the first node at each level.
- Why this approach comes to mind first: It's a straightforward way to traverse the tree and find the desired node.

```cpp
class Solution {
public:
    int findBottomLeftValue(TreeNode* root) {
        if (!root) return 0;
        queue<TreeNode*> q;
        q.push(root);
        int result = root->val;
        while (!q.empty()) {
            // Get the size of the current level
            int levelSize = q.size();
            // Update the result with the value of the first node at this level
            result = q.front()->val;
            // Process all nodes at the current level
            for (int i = 0; i < levelSize; i++) {
                TreeNode* node = q.front();
                q.pop();
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, since we visit each node once.
> - **Space Complexity:** $O(n)$, as in the worst case (a complete binary tree), the queue will store $n/2$ nodes at the last level.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node. The space complexity is also linear due to the storage required for the queue.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is the same as the brute force approach: performing a level order traversal and keeping track of the first node at each level.
- Detailed breakdown of the approach:
  1. Initialize a queue with the root node.
  2. Perform a level order traversal (BFS) of the tree.
  3. Keep track of the current level and the first node encountered at each level.
  4. Update the result with the value of the first node at each level.
- Proof of optimality: This approach is optimal because it visits each node exactly once, which is necessary to find the bottom left node.
- Why further optimization is impossible: We must visit each node at least once to determine the bottom left node, so any algorithm must have a time complexity of at least $O(n)$.

```cpp
class Solution {
public:
    int findBottomLeftValue(TreeNode* root) {
        if (!root) return 0;
        queue<TreeNode*> q;
        q.push(root);
        int result = root->val;
        while (!q.empty()) {
            // Get the size of the current level
            int levelSize = q.size();
            // Update the result with the value of the first node at this level
            result = q.front()->val;
            // Process all nodes at the current level
            for (int i = 0; i < levelSize; i++) {
                TreeNode* node = q.front();
                q.pop();
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, since we visit each node once.
> - **Space Complexity:** $O(n)$, as in the worst case (a complete binary tree), the queue will store $n/2$ nodes at the last level.
> - **Optimality proof:** The time complexity is linear because we perform a constant amount of work for each node. The space complexity is also linear due to the storage required for the queue.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Level order traversal (BFS), queue data structure.
- Problem-solving patterns identified: Finding a specific node in a tree, keeping track of the first node at each level.
- Optimization techniques learned: Visiting each node exactly once to minimize time complexity.
- Similar problems to practice: Finding the rightmost node at each level, finding the node with the maximum value at each level.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to update the result with the value of the first node at each level, not checking for null nodes before accessing their children.
- Edge cases to watch for: An empty tree, a tree with only one node.
- Performance pitfalls: Using a recursive approach instead of an iterative one, which can lead to stack overflow errors for large trees.
- Testing considerations: Testing the function with different types of trees (balanced, unbalanced, empty) and verifying that it returns the correct result.