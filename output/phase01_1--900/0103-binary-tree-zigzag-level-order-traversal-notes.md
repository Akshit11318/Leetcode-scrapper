## Binary Tree Zigzag Level Order Traversal

**Problem Link:** https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description

**Problem Statement:**
- Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
- Input format: The input is the root of a binary tree.
- Constraints: The number of nodes in the tree is in the range $[1, 2000]$.
- Expected output format: A list of lists, where each sublist contains the node values at a given level, ordered according to the zigzag pattern.
- Key requirements and edge cases to consider: Handling an empty tree, a tree with a single node, and ensuring the correct zigzag pattern for each level.
- Example test cases with explanations: 
  - For the tree `[3,9,20,null,null,15,7]`, the output should be `[[3],[20,9],[15,7]]`.
  - For the tree `[1]`, the output should be `[[1]]`.
  - For the tree `[]`, the output should be `[]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to traverse the tree level by level, storing the node values in a list for each level.
- For each level, we then check if it's an even or odd level to determine the order of the node values.
- We use a queue to perform the level order traversal.

```cpp
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        if (!root) return {};
        
        vector<vector<int>> result;
        queue<TreeNode*> q;
        q.push(root);
        bool isLeftToRight = true;
        
        while (!q.empty()) {
            vector<int> level;
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();
                if (isLeftToRight) {
                    level.push_back(node->val);
                } else {
                    level.insert(level.begin(), node->val);
                }
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            result.push_back(level);
            isLeftToRight = !isLeftToRight;
        }
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree, since we visit each node once.
> - **Space Complexity:** $O(N)$, for storing the node values in the result and the queue for level order traversal.
> - **Why these complexities occur:** The time complexity is linear because we visit each node once, and the space complexity is also linear because in the worst case (a complete binary tree), the queue will store $N/2$ nodes at the last level.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a deque (double-ended queue) to store the node values for each level, allowing for efficient insertion at both ends.
- We alternate the direction of insertion into the deque for each level to achieve the zigzag pattern.
- This approach is optimal because it minimizes the number of operations required to achieve the desired output.

```cpp
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        if (!root) return {};
        
        vector<vector<int>> result;
        queue<TreeNode*> q;
        q.push(root);
        bool isLeftToRight = true;
        
        while (!q.empty()) {
            deque<int> level;
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();
                if (isLeftToRight) {
                    level.push_back(node->val);
                } else {
                    level.push_front(node->val);
                }
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            result.push_back(vector<int>(level.begin(), level.end()));
            isLeftToRight = !isLeftToRight;
        }
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree, since we visit each node once.
> - **Space Complexity:** $O(N)$, for storing the node values in the result and the queue for level order traversal.
> - **Optimality proof:** This approach is optimal because it achieves the desired output with a single pass through the tree, minimizing the number of operations required.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Level order traversal, use of queues for tree traversal, and the application of deque for efficient insertion at both ends.
- Problem-solving patterns identified: Alternating patterns, use of boolean flags to track direction.
- Optimization techniques learned: Minimizing the number of operations, using appropriate data structures for efficient insertion and retrieval.
- Similar problems to practice: Other tree traversal problems, such as inorder, preorder, and postorder traversals.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect use of queues or deques, failure to alternate the direction of insertion correctly.
- Edge cases to watch for: Empty trees, trees with a single node, and ensuring the correct zigzag pattern for each level.
- Performance pitfalls: Using inefficient data structures or algorithms, resulting in higher time or space complexities.
- Testing considerations: Thoroughly testing the implementation with various input scenarios to ensure correctness and efficiency.