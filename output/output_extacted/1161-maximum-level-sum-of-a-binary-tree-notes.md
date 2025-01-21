## Maximum Level Sum of a Binary Tree

**Problem Link:** https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description

**Problem Statement:**
- Input format and constraints: Given the root of a binary tree, return the maximum level sum of the binary tree.
- Expected output format: The maximum level sum.
- Key requirements and edge cases to consider: 
    - The input tree is not empty.
    - The tree has at least one node and at most $10^4$ nodes.
    - Each node's value is between $-10^4$ and $10^4$.
- Example test cases with explanations: 
    - Example 1: Given the binary tree `[1,2,3,4,5,6,7]`, the maximum level sum is `18` (at level `3`).
    - Example 2: Given the binary tree `[1]`, the maximum level sum is `1` (at level `1`).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can calculate the sum of each level and keep track of the maximum sum.
- Step-by-step breakdown of the solution:
    1. Perform a level-order traversal of the binary tree.
    2. At each level, calculate the sum of node values.
    3. Keep track of the maximum sum seen so far.
- Why this approach comes to mind first: It is a straightforward way to solve the problem and does not require any additional data structures.

```cpp
class Solution {
public:
    int maxLevelSum(TreeNode* root) {
        if (!root) return 0;
        
        queue<TreeNode*> q;
        q.push(root);
        int maxSum = INT_MIN;
        int maxLevel = 0;
        int level = 0;
        
        while (!q.empty()) {
            int levelSize = q.size();
            int sum = 0;
            level++;
            
            for (int i = 0; i < levelSize; i++) {
                TreeNode* node = q.front();
                q.pop();
                sum += node->val;
                
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            
            if (sum > maxSum) {
                maxSum = sum;
                maxLevel = level;
            }
        }
        
        return maxLevel;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the binary tree. We visit each node once during the level-order traversal.
> - **Space Complexity:** $O(n)$, as in the worst case, we might have to store all nodes at the last level in the queue.
> - **Why these complexities occur:** The time complexity is linear because we visit each node once, and the space complexity is also linear because we use a queue to store nodes at each level.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal because we must visit each node to calculate its value and determine the maximum level sum.
- Detailed breakdown of the approach:
    1. Perform a level-order traversal of the binary tree.
    2. At each level, calculate the sum of node values.
    3. Keep track of the maximum sum seen so far and the corresponding level.
- Proof of optimality: Since we must visit each node at least once to calculate its value, the optimal time complexity is $O(n)$. The space complexity is also optimal because we use a queue to store nodes at each level, which is necessary for the level-order traversal.

```cpp
class Solution {
public:
    int maxLevelSum(TreeNode* root) {
        if (!root) return 0;
        
        queue<TreeNode*> q;
        q.push(root);
        int maxSum = INT_MIN;
        int maxLevel = 0;
        int level = 0;
        
        while (!q.empty()) {
            int levelSize = q.size();
            int sum = 0;
            level++;
            
            for (int i = 0; i < levelSize; i++) {
                TreeNode* node = q.front();
                q.pop();
                sum += node->val;
                
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            
            if (sum > maxSum) {
                maxSum = sum;
                maxLevel = level;
            }
        }
        
        return maxLevel;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the binary tree. We visit each node once during the level-order traversal.
> - **Space Complexity:** $O(n)$, as in the worst case, we might have to store all nodes at the last level in the queue.
> - **Optimality proof:** The time complexity is linear because we visit each node once, and the space complexity is also linear because we use a queue to store nodes at each level.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Level-order traversal, queue data structure.
- Problem-solving patterns identified: Keeping track of maximum sum and corresponding level.
- Optimization techniques learned: Using a queue to store nodes at each level.
- Similar problems to practice: Maximum Depth of Binary Tree, Minimum Depth of Binary Tree.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to update the maximum sum and corresponding level.
- Edge cases to watch for: Empty tree, tree with single node.
- Performance pitfalls: Using an inefficient data structure, such as a linked list, to store nodes at each level.
- Testing considerations: Test cases with different tree structures, such as balanced and unbalanced trees.