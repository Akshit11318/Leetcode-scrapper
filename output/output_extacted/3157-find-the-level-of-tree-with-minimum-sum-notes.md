## Find the Level of Tree with Minimum Sum

**Problem Link:** https://leetcode.com/problems/find-the-level-of-tree-with-minimum-sum/description

**Problem Statement:**
- Given a binary tree, find the level with the minimum sum of node values.
- The input is the root of the binary tree.
- The expected output is the level number (1-indexed) with the minimum sum.
- Key requirements:
  - The input tree can be empty.
  - The tree can have a single node.
  - The tree can have multiple levels.
- Example test cases:
  - Test case 1:
    - Input: `root = [2,1,3]`
    - Output: `2`
    - Explanation: Level 1 has a sum of 2, Level 2 has a sum of 4, so the minimum sum level is Level 2.
  - Test case 2:
    - Input: `root = [1,2,3,4,5,6,7]`
    - Output: `1`
    - Explanation: Level 1 has a sum of 1, Level 2 has a sum of 3, Level 3 has a sum of 18, so the minimum sum level is Level 1.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to traverse the tree level by level and calculate the sum of each level.
- We can use a `queue` to perform a level-order traversal.
- For each level, we calculate the sum of node values and keep track of the minimum sum level.

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
    int minSumLevel(TreeNode* root) {
        if (!root) return 0;
        
        queue<TreeNode*> q;
        q.push(root);
        int minSum = INT_MAX;
        int minLevel = 0;
        int level = 0;
        
        while (!q.empty()) {
            level++;
            int levelSize = q.size();
            int sum = 0;
            
            for (int i = 0; i < levelSize; i++) {
                TreeNode* node = q.front();
                q.pop();
                sum += node->val;
                
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            
            if (sum < minSum) {
                minSum = sum;
                minLevel = level;
            }
        }
        
        return minLevel;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, since we visit each node once.
> - **Space Complexity:** $O(n)$, since in the worst case (a complete binary tree), the queue will contain $n/2$ nodes at the last level.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node. The space complexity is also linear due to the queue used for level-order traversal.

---

### Optimal Approach (Required)

The brute force approach is already optimal for this problem, as we need to visit each node at least once to calculate the sum of each level. However, we can make some minor improvements to the code.

```cpp
class Solution {
public:
    int minSumLevel(TreeNode* root) {
        if (!root) return 0;
        
        queue<TreeNode*> q;
        q.push(root);
        int minSum = INT_MAX;
        int minLevel = 0;
        int level = 0;
        
        while (!q.empty()) {
            level++;
            int levelSize = q.size();
            int sum = 0;
            
            for (int i = 0; i < levelSize; i++) {
                TreeNode* node = q.front();
                q.pop();
                sum += node->val;
                
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            
            if (sum < minSum) {
                minSum = sum;
                minLevel = level;
            }
        }
        
        return minLevel;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, since we visit each node once.
> - **Space Complexity:** $O(n)$, since in the worst case (a complete binary tree), the queue will contain $n/2$ nodes at the last level.
> - **Optimality proof:** This is the optimal solution because we must visit each node at least once to calculate the sum of each level.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: level-order traversal, queue data structure.
- Problem-solving patterns identified: calculating sums of levels in a tree.
- Optimization techniques learned: using a queue for efficient level-order traversal.
- Similar problems to practice: finding the maximum sum level, finding the level with the minimum number of nodes.

**Mistakes to Avoid:**
- Common implementation errors: forgetting to update the minimum sum and level when a new minimum sum is found.
- Edge cases to watch for: empty tree, tree with a single node, tree with multiple levels.
- Performance pitfalls: using a recursive approach, which can lead to stack overflow for very deep trees.
- Testing considerations: testing with different tree structures and sizes to ensure correctness and efficiency.