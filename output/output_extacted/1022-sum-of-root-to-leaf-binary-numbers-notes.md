## Sum of Root to Leaf Binary Numbers

**Problem Link:** https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description

**Problem Statement:**
- Input: The root of a binary tree where each node has a value `val` from `0` to `1`.
- Constraints: The number of nodes in the tree is in the range `[1, 1000]`.
- Expected Output: The sum of the numbers represented by the root-to-leaf paths in the binary tree.
- Key Requirements and Edge Cases:
  - Each node's value is either `0` or `1`.
  - The tree can be empty, but in this problem, it's guaranteed to have at least one node.
- Example Test Cases:
  - Example 1:
    - Input: `root = [1,0,1,0,1,0,1]`
    - Output: `22`
    - Explanation: The binary numbers represented by the paths are `101`, `100`, `110`, and `111`, which sum up to `5 + 4 + 6 + 7 = 22`.

### Brute Force Approach

**Explanation:**
- The initial thought process involves traversing the tree and calculating the binary number represented by each root-to-leaf path.
- This can be achieved by performing a depth-first search (DFS) on the tree, keeping track of the current path's binary representation.

```cpp
class Solution {
public:
    int sumRootToLeaf(TreeNode* root) {
        return dfs(root, 0);
    }
    
    int dfs(TreeNode* node, int path) {
        if (!node) return 0;
        path = path * 2 + node->val;
        if (!node->left && !node->right) return path;
        return dfs(node->left, path) + dfs(node->right, path);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree, since we visit each node once.
> - **Space Complexity:** $O(H)$, where $H$ is the height of the tree, due to the recursive call stack.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node, and the space complexity depends on the tree's height due to the recursive calls.

### Optimal Approach (Required)

**Explanation:**
- The optimal approach is essentially the same as the brute force approach, as we must visit each node to calculate the sum of the root-to-leaf binary numbers.
- However, we can slightly optimize the code by reducing the number of operations within the recursive function.

```cpp
class Solution {
public:
    int sumRootToLeaf(TreeNode* root) {
        return dfs(root, 0);
    }
    
    int dfs(TreeNode* node, int path) {
        if (!node) return 0;
        path = (path << 1) | node->val;
        return node->left || node->right ? dfs(node->left, path) + dfs(node->right, path) : path;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$
> - **Space Complexity:** $O(H)$
> - **Optimality proof:** This approach is optimal because it visits each node exactly once, which is necessary to calculate the sum of the root-to-leaf binary numbers.

### Final Notes

**Learning Points:**
- The problem demonstrates the use of DFS in traversing a binary tree.
- It highlights the importance of keeping track of the current path during the traversal.
- The solution shows how to optimize the recursive function by reducing the number of operations.

**Mistakes to Avoid:**
- Not handling the base case of an empty tree or null node correctly.
- Failing to update the path correctly during the recursive calls.
- Not considering the case where a node has no children (i.e., it's a leaf node).