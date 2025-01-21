## Leaf Similar Trees

**Problem Link:** https://leetcode.com/problems/leaf-similar-trees/description

**Problem Statement:**
- Input format and constraints: Given the roots of two binary trees `root1` and `root2`, return `true` if the leaf values of both trees are the same regardless of the order of the leaves, otherwise return `false`.
- Expected output format: A boolean indicating whether the leaf values are the same.
- Key requirements and edge cases to consider: 
  - Both trees may have different structures but the same leaf values.
  - The trees may be empty (i.e., `root1` or `root2` is `nullptr`).
- Example test cases with explanations:
  - Example 1: `root1 = [3,3,4]`, `root2 = [3,3,4]`, output: `true` because both trees have the same leaf values.
  - Example 2: `root1 = [1]`, `root2 = [2]`, output: `false` because the leaf values are different.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to traverse both trees, collect all the leaf node values, and then compare these values.
- Step-by-step breakdown of the solution:
  1. Define a helper function to perform a depth-first search (DFS) on a tree and collect leaf node values in a vector.
  2. Use this helper function to collect leaf values from both trees.
  3. Compare the two vectors of leaf values. If they are equal, return `true`; otherwise, return `false`.
- Why this approach comes to mind first: It's straightforward and directly addresses the problem statement by comparing leaf values.

```cpp
class Solution {
public:
    vector<int> getLeafValues(TreeNode* root) {
        vector<int> leafValues;
        dfs(root, leafValues);
        return leafValues;
    }
    
    void dfs(TreeNode* node, vector<int>& leafValues) {
        if (!node) return;
        if (!node->left && !node->right) {
            leafValues.push_back(node->val);
        }
        dfs(node->left, leafValues);
        dfs(node->right, leafValues);
    }
    
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int> leafValues1 = getLeafValues(root1);
        vector<int> leafValues2 = getLeafValues(root2);
        return leafValues1 == leafValues2;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ and $m$ are the number of nodes in `root1` and `root2`, respectively. This is because in the worst case, we visit every node in both trees.
> - **Space Complexity:** $O(n + m)$, as we store the leaf values of both trees. In the worst case, if all nodes are leaf nodes, the space complexity would be linear with respect to the total number of nodes.
> - **Why these complexities occur:** The time complexity is due to the DFS traversal of both trees, and the space complexity is due to storing the leaf values.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal approach is essentially the same as the brute force because we must visit every node in both trees to determine if they are leaf-similar. However, we can optimize the code slightly by combining the DFS and comparison into a single step, although this doesn't change the time or space complexity.
- Detailed breakdown of the approach: Perform DFS on both trees simultaneously, comparing leaf values as we encounter them.
- Proof of optimality: This approach is optimal because we only visit each node once and only store the leaf values, which is necessary for the comparison.

```cpp
class Solution {
public:
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int> leafValues1, leafValues2;
        dfs(root1, leafValues1);
        dfs(root2, leafValues2);
        return leafValues1 == leafValues2;
    }
    
    void dfs(TreeNode* node, vector<int>& leafValues) {
        if (!node) return;
        if (!node->left && !node->right) {
            leafValues.push_back(node->val);
        }
        dfs(node->left, leafValues);
        dfs(node->right, leafValues);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ and $m$ are the number of nodes in `root1` and `root2`, respectively.
> - **Space Complexity:** $O(n + m)$, for storing the leaf values of both trees.
> - **Optimality proof:** This is the most efficient approach because we must examine every node in both trees to ensure they are leaf-similar, and we only store the necessary information (leaf values).

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-First Search (DFS), tree traversal, and comparison of vectors.
- Problem-solving patterns identified: The need to visit all nodes in a tree to gather specific information (in this case, leaf values).
- Optimization techniques learned: While the optimal solution doesn't differ significantly from the brute force in terms of complexity, the approach highlights the importance of directly addressing the problem's requirements without unnecessary steps.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle the base case of `nullptr` nodes, or incorrectly identifying leaf nodes.
- Edge cases to watch for: Empty trees or trees with a single node.
- Performance pitfalls: Unnecessary traversal or storage of non-leaf nodes.
- Testing considerations: Ensure that the solution works correctly for trees of different sizes and structures, and that it correctly identifies both similar and dissimilar leaf values.