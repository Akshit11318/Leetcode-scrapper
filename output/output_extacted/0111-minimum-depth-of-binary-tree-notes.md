## Minimum Depth of Binary Tree

**Problem Link:** https://leetcode.com/problems/minimum-depth-of-binary-tree/description

**Problem Statement:**
- Input: A binary tree represented by its `root` node.
- Constraints: The tree can be empty, and the number of nodes in the tree is in the range `[0, 10^4]`.
- Expected Output: The minimum depth of the binary tree, which is the number of nodes along the shortest path from the `root` node down to the nearest leaf node.
- Key Requirements:
  - The tree can be unbalanced.
  - A leaf node is a node with no children.
- Edge Cases:
  - An empty tree (i.e., `root` is `NULL`).
  - A tree with a single node.
- Example Test Cases:
  - Example 1:
    - Input: `root = [3,9,20,null,null,15,7]`
    - Output: `2`
    - Explanation: The shortest path from the root to a leaf is `3 -> 9`.
  - Example 2:
    - Input: `root = [1,null,2]`
    - Output: `2`
    - Explanation: The shortest path from the root to a leaf is `1 -> 2`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to traverse the tree and calculate the depth of each leaf node.
- We can use a recursive approach to traverse the tree.
- For each node, we check if it is a leaf node. If it is, we return its depth.

```cpp
class Solution {
public:
    int minDepth(TreeNode* root) {
        if (!root) return 0;
        if (!root->left && !root->right) return 1;
        
        int left_depth = INT_MAX;
        if (root->left) left_depth = minDepth(root->left) + 1;
        
        int right_depth = INT_MAX;
        if (root->right) right_depth = minDepth(root->right) + 1;
        
        return min(left_depth, right_depth);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree. This is because in the worst case, we visit every node.
> - **Space Complexity:** $O(H)$, where $H$ is the height of the tree. This is because of the recursive call stack.
> - **Why these complexities occur:** The time complexity occurs because we are visiting every node in the tree, and the space complexity occurs because of the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Instead of using recursion, we can use a level-order traversal (BFS) to find the minimum depth.
- We start from the root node and explore all nodes at each level before moving to the next level.
- The first leaf node we encounter will be the node with the minimum depth.

```cpp
class Solution {
public:
    int minDepth(TreeNode* root) {
        if (!root) return 0;
        
        queue<pair<TreeNode*, int>> q;
        q.push({root, 1});
        
        while (!q.empty()) {
            auto [node, depth] = q.front();
            q.pop();
            
            if (!node->left && !node->right) return depth;
            
            if (node->left) q.push({node->left, depth + 1});
            if (node->right) q.push({node->right, depth + 1});
        }
        
        return 0; // This line should not be reached
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree. This is because in the worst case, we visit every node.
> - **Space Complexity:** $O(N)$, where $N$ is the number of nodes in the tree. This is because in the worst case, we need to store all nodes in the queue.
> - **Optimality proof:** This approach is optimal because we are guaranteed to find the first leaf node, which is the node with the minimum depth.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Level-order traversal (BFS) and recursion.
- Problem-solving patterns identified: Using BFS to find the shortest path in an unweighted graph.
- Optimization techniques learned: Avoiding unnecessary recursive calls by using BFS.

**Mistakes to Avoid:**
- Not handling the edge case where the tree is empty.
- Not checking for the existence of child nodes before accessing them.
- Using recursion when BFS is more efficient.