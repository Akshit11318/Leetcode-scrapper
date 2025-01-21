## Cousins in Binary Tree

**Problem Link:** https://leetcode.com/problems/cousins-in-binary-tree/description

**Problem Statement:**
- Input: The root of a binary tree and two node values, x and y.
- Output: Return true if the nodes with values x and y are cousins, false otherwise.
- Constraints: The number of nodes in the binary tree will be between 2 and 100.
- Key requirements: Two nodes are cousins if they are at the same level but have different parents.
- Edge cases: Nodes with values x and y might not exist in the tree.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Traverse the tree level by level, checking each node's value and parent.
- Step-by-step breakdown:
  1. Perform a level-order traversal (BFS) of the binary tree.
  2. For each node, store its value, level, and parent in a data structure (e.g., a vector of pairs).
  3. After traversal, iterate through the stored nodes to find the levels and parents of nodes with values x and y.
  4. Compare the levels and parents of the found nodes to determine if they are cousins.

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
    bool isCousins(TreeNode* root, int x, int y) {
        if (!root) return false;
        
        queue<pair<TreeNode*, TreeNode*>> q; // node, parent
        q.push({root, nullptr});
        
        while (!q.empty()) {
            int levelSize = q.size();
            unordered_map<int, TreeNode*> levelNodes;
            
            for (int i = 0; i < levelSize; ++i) {
                auto node = q.front().first;
                auto parent = q.front().second;
                q.pop();
                
                if (node->val == x || node->val == y) {
                    levelNodes[node->val] = parent;
                }
                
                if (node->left) q.push({node->left, node});
                if (node->right) q.push({node->right, node});
            }
            
            if (levelNodes.count(x) && levelNodes.count(y) && levelNodes[x] != levelNodes[y]) {
                return true;
            }
        }
        
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree, since we visit each node once.
> - **Space Complexity:** $O(N)$, for storing nodes in the queue and the levelNodes map.
> - **Why these complexities occur:** The BFS traversal visits each node once, and in the worst case, the queue and map can hold all nodes.

---

### Optimal Approach (Required)

The provided brute force approach is already optimal for this problem, with a time complexity of $O(N)$ and space complexity of $O(N)$. This is because we must potentially visit every node in the tree to find the cousins and verify their relationship. The use of a queue for BFS and an unordered map to store node parents at each level is efficient and necessary for the task.

However, we can slightly optimize the code by directly returning as soon as we find both nodes at the same level with different parents, without the need for the `levelNodes` map.

```cpp
class Solution {
public:
    bool isCousins(TreeNode* root, int x, int y) {
        if (!root) return false;
        
        queue<pair<TreeNode*, TreeNode*>> q; // node, parent
        q.push({root, nullptr});
        
        while (!q.empty()) {
            int levelSize = q.size();
            unordered_map<int, TreeNode*> levelNodes;
            
            for (int i = 0; i < levelSize; ++i) {
                auto node = q.front().first;
                auto parent = q.front().second;
                q.pop();
                
                if (node->val == x) {
                    levelNodes[x] = parent;
                }
                if (node->val == y) {
                    levelNodes[y] = parent;
                }
                
                if (node->left) q.push({node->left, node});
                if (node->right) q.push({node->right, node});
            }
            
            if (levelNodes.count(x) && levelNodes.count(y) && levelNodes[x] != levelNodes[y]) {
                return true;
            } else if (levelNodes.count(x) || levelNodes.count(y)) {
                return false; // If only one node is found, they cannot be cousins
            }
        }
        
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree.
> - **Space Complexity:** $O(N)$, for storing nodes in the queue and the levelNodes map.
> - **Optimality proof:** This approach is optimal because it visits each node once and uses efficient data structures for storing and comparing node relationships.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS traversal, use of queues, and unordered maps for efficient data storage and comparison.
- Problem-solving patterns identified: The importance of understanding the definition of cousins in a binary tree and designing an algorithm that efficiently verifies this relationship.
- Optimization techniques learned: Directly returning upon finding the required condition can slightly improve performance.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases, such as when nodes with values x and y do not exist in the tree.
- Performance pitfalls: Using inefficient data structures or algorithms that lead to higher time or space complexities than necessary.