## Diameter of Binary Tree

**Problem Link:** [https://leetcode.com/problems/diameter-of-binary-tree/description](https://leetcode.com/problems/diameter-of-binary-tree/description)

**Problem Statement:**
- Input format: The input is the `root` of a binary tree.
- Constraints: The number of nodes in the tree is in the range $[1, 10^4]$.
- Expected output format: The function should return the length of the diameter of the binary tree.
- Key requirements and edge cases to consider: The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
- Example test cases with explanations:
  - For the binary tree with nodes `1`, `2`, `3`, `4`, `5`, where `1` is the root, `2` and `3` are its children, and `4` and `5` are children of `2` and `3` respectively, the diameter is `3` (path `4-2-1-3-5`).
  - For a tree with a single node, the diameter is `0`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each node, calculate the longest path that passes through it and keep track of the maximum length found.
- Step-by-step breakdown of the solution:
  1. Perform a depth-first search (DFS) from each node.
  2. For each node, find the longest path that passes through it by considering all possible paths.
  3. Update the maximum diameter if a longer path is found.
- Why this approach comes to mind first: It's straightforward to think about examining each node and its connections to find the longest path.

```cpp
class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        int maxDiameter = 0;
        dfs(root, maxDiameter);
        return maxDiameter;
    }
    
    int dfs(TreeNode* node, int& maxDiameter) {
        if (!node) return 0;
        
        int leftDepth = dfs(node->left, maxDiameter);
        int rightDepth = dfs(node->right, maxDiameter);
        
        maxDiameter = max(maxDiameter, leftDepth + rightDepth);
        
        return 1 + max(leftDepth, rightDepth);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, because we visit each node once.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree, due to the recursive call stack. In the worst case, $h = n$ for an unbalanced tree.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node, and the space complexity depends on the tree's height due to recursion.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of performing DFS from each node, we can calculate the depth of the left and right subtrees for each node in a single DFS pass and update the diameter accordingly.
- Detailed breakdown of the approach:
  1. Initialize `maxDiameter` to 0.
  2. Perform DFS, calculating the depth of the left and right subtrees for each node.
  3. Update `maxDiameter` if the sum of the left and right depths is greater than the current `maxDiameter`.
- Proof of optimality: This approach is optimal because it visits each node exactly once, resulting in a time complexity of $O(n)$, which is the best possible for this problem since we must examine every node.

```cpp
class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        int maxDiameter = 0;
        dfs(root, maxDiameter);
        return maxDiameter;
    }
    
    int dfs(TreeNode* node, int& maxDiameter) {
        if (!node) return 0;
        
        int leftDepth = dfs(node->left, maxDiameter);
        int rightDepth = dfs(node->right, maxDiameter);
        
        maxDiameter = max(maxDiameter, leftDepth + rightDepth);
        
        return 1 + max(leftDepth, rightDepth);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree.
> - **Optimality proof:** Visiting each node once and calculating the necessary depths in a single pass ensures this is the most efficient approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-first search, tree traversal, and dynamic programming.
- Problem-solving patterns identified: Calculating the maximum or minimum of a property (in this case, diameter) by considering all possible configurations.
- Optimization techniques learned: Reducing the number of traversals or passes through the data structure.
- Similar problems to practice: Finding the longest path in a graph, calculating the height of a tree, or determining the minimum or maximum path sum in a tree.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle the base case of an empty tree or not updating the maximum diameter correctly.
- Edge cases to watch for: Trees with a single node, or trees that are highly unbalanced.
- Performance pitfalls: Using an inefficient algorithm that results in a higher time complexity than necessary.
- Testing considerations: Ensure that the solution works correctly for a variety of tree structures and sizes.