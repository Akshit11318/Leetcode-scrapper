## Find Nearest Right Node in Binary Tree

**Problem Link:** [https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/description](https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/description)

**Problem Statement:**
- Input: A binary tree and a target node.
- Constraints: The binary tree is not empty and the target node is not null.
- Expected Output: The nearest right node to the target node in the binary tree.
- Key Requirements: If there is no right node at the same level as the target node, return null.
- Edge Cases: The target node is the rightmost node at its level, or the target node is a leaf node.

**Example Test Cases:**
- Test Case 1: A binary tree with multiple levels and a target node that is not the rightmost node at its level.
- Test Case 2: A binary tree with a target node that is the rightmost node at its level.
- Test Case 3: A binary tree with a target node that is a leaf node.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Perform a level-order traversal of the binary tree to find the target node and then search for the nearest right node at the same level.
- Step-by-step breakdown:
  1. Perform a level-order traversal of the binary tree using a queue.
  2. Keep track of the current level and the nodes at the current level.
  3. When the target node is found, search for the nearest right node at the same level.
  4. If no right node is found at the same level, return null.

```cpp
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    TreeNode* findNearestRightNode(TreeNode* root, TreeNode* u) {
        if (!root || !u) return nullptr;
        
        queue<TreeNode*> q;
        q.push(root);
        bool found = false;
        
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();
                
                if (node == u) {
                    found = true;
                }
                
                if (found && node != u) {
                    return node;
                }
                
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            found = false;
        }
        
        return nullptr;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the binary tree, because we visit each node once during the level-order traversal.
> - **Space Complexity:** $O(n)$, because in the worst case, the queue will store all nodes at the last level of the binary tree.
> - **Why these complexities occur:** The brute force approach requires visiting each node in the binary tree to find the target node and the nearest right node, resulting in a time complexity of $O(n)$. The space complexity is also $O(n)$ because we use a queue to store nodes during the level-order traversal.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Perform a level-order traversal of the binary tree and keep track of the nodes at each level. When the target node is found, return the next node at the same level.
- Detailed breakdown:
  1. Perform a level-order traversal of the binary tree using a queue.
  2. Keep track of the current level and the nodes at the current level.
  3. When the target node is found, return the next node at the same level.
  4. If no next node is found at the same level, return null.

```cpp
class Solution {
public:
    TreeNode* findNearestRightNode(TreeNode* root, TreeNode* u) {
        if (!root || !u) return nullptr;
        
        queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();
                
                if (node == u) {
                    if (i < size - 1) {
                        return q.front();
                    } else {
                        break;
                    }
                }
                
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
        }
        
        return nullptr;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the binary tree, because we visit each node once during the level-order traversal.
> - **Space Complexity:** $O(n)$, because in the worst case, the queue will store all nodes at the last level of the binary tree.
> - **Optimality proof:** This approach is optimal because we only visit each node once and use a queue to store nodes during the level-order traversal, resulting in a time complexity of $O(n)$ and a space complexity of $O(n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Level-order traversal of a binary tree.
- Problem-solving patterns identified: Finding the nearest right node in a binary tree.
- Optimization techniques learned: Using a queue to store nodes during the level-order traversal.
- Similar problems to practice: Finding the nearest left node in a binary tree, finding the nearest node in a graph.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for null nodes, not handling edge cases.
- Edge cases to watch for: The target node is the rightmost node at its level, or the target node is a leaf node.
- Performance pitfalls: Using an inefficient data structure, such as a linked list, to store nodes during the level-order traversal.
- Testing considerations: Test the solution with different binary tree structures and target nodes to ensure correctness.