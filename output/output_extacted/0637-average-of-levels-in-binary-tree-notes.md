## Average of Levels in Binary Tree

**Problem Link:** https://leetcode.com/problems/average-of-levels-in-binary-tree/description

**Problem Statement:**
- Input: The root of a binary tree.
- Output: An array of the average values of each level.
- Key requirements: Calculate the average value of each level in the binary tree.
- Edge cases: Empty tree, tree with one node, unbalanced tree.

Example test cases:
- Input: root = [3,9,20,null,null,15,7]
  Output: [3.00000,14.50000,11.00000]
  Explanation: The average of the first level (3) is 3. The average of the second level (9 + 20) / 2 = 14.5. The average of the third level (15 + 7) / 2 = 11.
- Input: root = [3]
  Output: [3.00000]
  Explanation: The average of the only level (3) is 3.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to traverse the tree level by level and calculate the sum of each level.
- Then, divide the sum by the number of nodes at each level to get the average.
- This approach comes to mind first because it directly addresses the problem statement.

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
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> result;
        if (!root) return result;
        
        queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            int levelSize = q.size();
            double levelSum = 0.0;
            
            for (int i = 0; i < levelSize; i++) {
                TreeNode* node = q.front();
                q.pop();
                levelSum += node->val;
                
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            
            result.push_back(levelSum / levelSize);
        }
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree. Each node is visited once.
> - **Space Complexity:** $O(N)$, where $N$ is the number of nodes in the tree. In the worst case, the queue will hold all nodes at the last level.
> - **Why these complexities occur:** The time complexity is linear because we visit each node once. The space complexity is also linear due to the queue used for level order traversal.

---

### Optimal Approach (Required)

The brute force approach is already optimal for this problem. It has a time complexity of $O(N)$ and a space complexity of $O(N)$, which is the best we can achieve for this problem because we must visit each node at least once.

However, we can slightly optimize the code by using more descriptive variable names and comments:

```cpp
class Solution {
public:
    vector<double> averageOfLevels(TreeNode* root) {
        // Initialize result vector
        vector<double> averages;
        
        // Check for empty tree
        if (!root) return averages;
        
        // Initialize queue with root node
        queue<TreeNode*> levelQueue;
        levelQueue.push(root);
        
        // Perform level order traversal
        while (!levelQueue.empty()) {
            int nodesAtCurrentLevel = levelQueue.size();
            double sumOfCurrentLevel = 0.0;
            
            // Process each node at the current level
            for (int i = 0; i < nodesAtCurrentLevel; i++) {
                TreeNode* currentNode = levelQueue.front();
                levelQueue.pop();
                sumOfCurrentLevel += currentNode->val;
                
                // Add children to queue for next level
                if (currentNode->left) levelQueue.push(currentNode->left);
                if (currentNode->right) levelQueue.push(currentNode->right);
            }
            
            // Calculate and store average of current level
            averages.push_back(sumOfCurrentLevel / nodesAtCurrentLevel);
        }
        
        return averages;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree.
> - **Space Complexity:** $O(N)$, where $N$ is the number of nodes in the tree.
> - **Optimality proof:** This is the optimal solution because we must visit each node at least once to calculate the average of each level, resulting in a time complexity of $O(N)$. The space complexity is also optimal because we need to store the nodes at each level in the queue.

---

### Final Notes

**Learning Points:**
- Level order traversal is useful for problems that require processing nodes level by level.
- Using a queue data structure is efficient for level order traversal.
- Calculating averages requires summing values and dividing by the count of values.

**Mistakes to Avoid:**
- Not checking for an empty tree.
- Not handling the case where a node has no children.
- Incorrectly calculating the average by not dividing by the correct number of nodes.
- Not using descriptive variable names and comments for clarity.