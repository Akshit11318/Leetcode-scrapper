## Binary Tree Level Order Traversal

**Problem Link:** https://leetcode.com/problems/binary-tree-level-order-traversal/description

**Problem Statement:**
- Input format: The input is the root of a binary tree, where each node has a unique value.
- Constraints: The number of nodes in the tree is in the range [0, 2000], -1000 <= Node.val <= 1000, and -1000 <= Node.left.val <= 1000 and -1000 <= Node.right.val <= 1000.
- Expected output format: A 2D vector where each sub-vector represents the node values at a specific level of the binary tree, ordered from left to right, top to bottom.
- Key requirements and edge cases to consider:
  - Handling an empty tree (root is NULL).
  - Handling a tree with a single node.
  - Handling a tree with multiple levels and nodes.
- Example test cases with explanations:
  - Example 1:
    - Input: root = [3,9,20,null,null,15,7]
    - Output: [[3],[9,20],[15,7]]
  - Example 2:
    - Input: root = [1]
    - Output: [[1]]
  - Example 3:
    - Input: root = []
    - Output: []

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to traverse the tree recursively or iteratively and store the node values level by level. However, this requires keeping track of the current level and appending node values accordingly.
- Step-by-step breakdown of the solution:
  1. Initialize an empty vector to store the result.
  2. Define a helper function to perform the level order traversal recursively.
  3. In the helper function, append the current node's value to the corresponding level vector.
  4. Recursively call the helper function for the left and right child nodes, incrementing the level index.
  5. After the traversal, return the result vector.
- Why this approach comes to mind first: It's a straightforward way to traverse a tree and collect node values level by level.

```cpp
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        if (!root) return result;
        
        levelOrderHelper(root, 0, result);
        return result;
    }
    
    void levelOrderHelper(TreeNode* node, int level, vector<vector<int>>& result) {
        if (!node) return;
        
        if (level >= result.size()) {
            result.push_back({});
        }
        
        result[level].push_back(node->val);
        
        levelOrderHelper(node->left, level + 1, result);
        levelOrderHelper(node->right, level + 1, result);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree, since we visit each node exactly once.
> - **Space Complexity:** $O(N)$, for the recursive call stack and the result vector.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node. The space complexity is also linear due to the recursive call stack and the storage required for the result vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of using recursion, we can use a queue to perform an iterative level order traversal. This approach eliminates the recursive call stack and reduces the space complexity.
- Detailed breakdown of the approach:
  1. Initialize an empty vector to store the result and a queue with the root node.
  2. While the queue is not empty, process the nodes at the current level.
  3. For each node at the current level, append its value to the corresponding level vector and enqueue its child nodes.
  4. After processing all nodes at the current level, move on to the next level.
- Proof of optimality: This approach has the same time complexity as the brute force approach but reduces the space complexity by avoiding the recursive call stack.
- Why further optimization is impossible: We must visit each node at least once to perform a level order traversal, so the time complexity is already optimal.

```cpp
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        if (!root) return result;
        
        queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            int levelSize = q.size();
            vector<int> level;
            
            for (int i = 0; i < levelSize; i++) {
                TreeNode* node = q.front();
                q.pop();
                level.push_back(node->val);
                
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            
            result.push_back(level);
        }
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree, since we visit each node exactly once.
> - **Space Complexity:** $O(N)$, for the queue and the result vector.
> - **Optimality proof:** The time complexity is already optimal, and the space complexity is reduced compared to the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Level order traversal, recursive and iterative approaches, and queue data structure.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems (levels) and processing each level separately.
- Optimization techniques learned: Avoiding recursive call stacks and using iterative approaches to reduce space complexity.
- Similar problems to practice: Other tree traversal problems, such as inorder, preorder, and postorder traversals.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases (e.g., empty tree or tree with a single node).
- Edge cases to watch for: Handling nodes with only one child or no children.
- Performance pitfalls: Using recursive approaches for large trees, which can lead to stack overflow errors.
- Testing considerations: Testing the solution with different tree structures and edge cases to ensure correctness.