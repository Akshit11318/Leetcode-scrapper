## Insufficient Nodes in Root to Leaf Paths

**Problem Link:** https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/description

**Problem Statement:**
- Input format and constraints: The problem involves a binary tree where each node has a value and two child nodes (left and right). The input is the root of the binary tree, and the constraint is that the sum of the node values from the root to a leaf node should be greater than or equal to a given limit.
- Expected output format: The function should return the root of the modified binary tree after pruning insufficient nodes.
- Key requirements and edge cases to consider: 
    - The tree can be empty.
    - The tree can have only one node.
    - The limit can be any integer.
- Example test cases with explanations: 
    - For example, given a binary tree with the following structure:
        ```
        5
       / \
      4   8
     /   / \
    11  17 20
   /  \  /
  7    15
        ```
        And a limit of 22, the output should be the root of the modified binary tree after pruning insufficient nodes.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to perform a depth-first search (DFS) on the binary tree, calculating the sum of node values from the root to each leaf node. If the sum is less than the limit, we prune the leaf node.
- Step-by-step breakdown of the solution: 
    1. Perform DFS on the binary tree.
    2. For each leaf node, calculate the sum of node values from the root to the leaf node.
    3. If the sum is less than the limit, prune the leaf node.
- Why this approach comes to mind first: This approach is straightforward and easy to implement. However, it may not be efficient for large trees.

```cpp
class Solution {
public:
    TreeNode* sufficientSubset(TreeNode* root, int limit) {
        if (!root) return nullptr;
        if (!root->left && !root->right) {
            if (root->val < limit) return nullptr;
            return root;
        }
        root->left = sufficientSubset(root->left, limit - root->val);
        root->right = sufficientSubset(root->right, limit - root->val);
        if (!root->left && !root->right) return nullptr;
        return root;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where n is the number of nodes in the tree, since we visit each node once.
> - **Space Complexity:** $O(h)$, where h is the height of the tree, due to the recursive call stack.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node. The space complexity is proportional to the height of the tree because of the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is to use a recursive approach with pruning. We recursively traverse the tree, and for each node, we check if it is a leaf node. If it is, we check if the sum of node values from the root to the leaf node is greater than or equal to the limit. If not, we prune the leaf node.
- Detailed breakdown of the approach: 
    1. Define a recursive function that takes a node and the current sum as arguments.
    2. If the node is nullptr, return nullptr.
    3. If the node is a leaf node, check if the sum is greater than or equal to the limit. If not, return nullptr.
    4. Recursively call the function on the left and right child nodes, updating the sum accordingly.
- Proof of optimality: This approach is optimal because it only visits each node once and performs a constant amount of work for each node.

```cpp
class Solution {
public:
    TreeNode* sufficientSubset(TreeNode* root, int limit) {
        return dfs(root, 0, limit);
    }
    
    TreeNode* dfs(TreeNode* node, int sum, int limit) {
        if (!node) return nullptr;
        sum += node->val;
        if (!node->left && !node->right) {
            if (sum < limit) return nullptr;
            return node;
        }
        node->left = dfs(node->left, sum, limit);
        node->right = dfs(node->right, sum, limit);
        if (!node->left && !node->right) return nullptr;
        return node;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where n is the number of nodes in the tree, since we visit each node once.
> - **Space Complexity:** $O(h)$, where h is the height of the tree, due to the recursive call stack.
> - **Optimality proof:** The time complexity is linear because we perform a constant amount of work for each node. The space complexity is proportional to the height of the tree because of the recursive call stack.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive tree traversal and pruning.
- Problem-solving patterns identified: Using a recursive approach to solve tree problems.
- Optimization techniques learned: Pruning unnecessary nodes to reduce the size of the tree.
- Similar problems to practice: Other tree problems that involve recursive traversal and pruning.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for nullptr nodes before accessing their children.
- Edge cases to watch for: Empty trees, trees with only one node, and trees with negative values.
- Performance pitfalls: Using an inefficient algorithm that visits each node multiple times.
- Testing considerations: Testing the function with different types of trees and limits to ensure it works correctly.