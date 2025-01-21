## Find All the Lonely Nodes
**Problem Link:** https://leetcode.com/problems/find-all-the-lonely-nodes/description

**Problem Statement:**
- Input format: A binary tree `root`.
- Constraints: `The number of nodes in the tree is in the range [1, 100]`.
- Expected output format: A list of node values that are lonely nodes.
- Key requirements and edge cases to consider:
  - A node is a `lonely node` if it is a child of a node that has only one child.
  - The tree may be unbalanced.
- Example test cases with explanations:
  - Given a binary tree: 
    ```
    1
     \
      2
       \
        3
    ```
    The output should be `[3]`, because `3` is the only node that is a child of a node with only one child (`2`).
  - Given a binary tree: 
    ```
      7
     / \
    1   4
       / \
      5   6
    ```
    The output should be `[1, 5, 6]`, because `1`, `5`, and `6` are children of nodes that have only one child (`7`, `4`, and `4`, respectively).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Perform a depth-first search (DFS) traversal of the tree to identify lonely nodes.
- Step-by-step breakdown of the solution:
  1. Define a recursive function to perform DFS traversal.
  2. For each node, check if it has only one child.
  3. If a node has only one child, mark the child as a lonely node.
- Why this approach comes to mind first: It is a straightforward and intuitive solution that directly addresses the problem statement.

```cpp
class Solution {
public:
    vector<int> getLonelyNodes(TreeNode* root) {
        vector<int> lonelyNodes;
        dfs(root, lonelyNodes);
        return lonelyNodes;
    }
    
    void dfs(TreeNode* node, vector<int>& lonelyNodes) {
        if (!node) return;
        
        if (node->left && !node->right) lonelyNodes.push_back(node->left->val);
        if (!node->left && node->right) lonelyNodes.push_back(node->right->val);
        
        dfs(node->left, lonelyNodes);
        dfs(node->right, lonelyNodes);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, since we visit each node once during the DFS traversal.
> - **Space Complexity:** $O(n)$, for the recursive call stack and the vector to store lonely nodes.
> - **Why these complexities occur:** The time complexity is linear because we visit each node once, and the space complexity is also linear due to the recursive call stack and the storage of lonely nodes.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal, as we need to visit each node at least once to determine if it is a lonely node.
- Detailed breakdown of the approach: The same as the brute force approach, since it is already optimal.
- Proof of optimality: The optimal time complexity is $O(n)$, as we must visit each node at least once. The optimal space complexity is also $O(n)$, for the recursive call stack and the storage of lonely nodes.
- Why further optimization is impossible: We cannot avoid visiting each node, so the time complexity cannot be improved. Similarly, we cannot avoid storing the lonely nodes, so the space complexity cannot be improved.

```cpp
class Solution {
public:
    vector<int> getLonelyNodes(TreeNode* root) {
        vector<int> lonelyNodes;
        dfs(root, lonelyNodes);
        return lonelyNodes;
    }
    
    void dfs(TreeNode* node, vector<int>& lonelyNodes) {
        if (!node) return;
        
        if (node->left && !node->right) lonelyNodes.push_back(node->left->val);
        if (!node->left && node->right) lonelyNodes.push_back(node->right->val);
        
        dfs(node->left, lonelyNodes);
        dfs(node->right, lonelyNodes);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree.
> - **Space Complexity:** $O(n)$, for the recursive call stack and the vector to store lonely nodes.
> - **Optimality proof:** The time and space complexities are optimal, as we must visit each node at least once and store the lonely nodes.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS traversal, recursive functions, and node traversal.
- Problem-solving patterns identified: Identifying lonely nodes in a binary tree.
- Optimization techniques learned: None, as the brute force approach is already optimal.
- Similar problems to practice: Finding nodes with specific properties in a binary tree.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle the base case (empty tree) or not checking for null nodes.
- Edge cases to watch for: Empty tree, tree with only one node, or tree with only left or right children.
- Performance pitfalls: Not using a recursive approach or not storing lonely nodes efficiently.
- Testing considerations: Testing with different tree structures and node values to ensure correctness.