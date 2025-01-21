## Find Leaves of Binary Tree
**Problem Link:** https://leetcode.com/problems/find-leaves-of-binary-tree/description

**Problem Statement:**
- Input: The root of a binary tree.
- Expected output: A list of lists, where each sublist contains the node values of leaves that are at the same distance from the root.
- Key requirements: The leaves should be ordered from left to right.
- Example test cases:
  - Input: `root = [1,2,3,4,5]`
    - Output: `[[4,5,3],[2],[1]]`
  - Input: `root = [1]`
    - Output: `[[1]]`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves traversing the tree and identifying the leaves.
- We can use a depth-first search (DFS) to traverse the tree and calculate the height of each node.
- We can store the node values at each height in separate lists.

```cpp
class Solution {
public:
    vector<vector<int>> findLeaves(TreeNode* root) {
        vector<vector<int>> result;
        dfs(root, result);
        return result;
    }
    
    int dfs(TreeNode* node, vector<vector<int>>& result) {
        if (!node) return -1;
        
        int leftHeight = dfs(node->left, result);
        int rightHeight = dfs(node->right, result);
        
        int height = max(leftHeight, rightHeight) + 1;
        
        if (height == result.size()) {
            result.push_back({});
        }
        
        result[height].push_back(node->val);
        
        return height;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, because we visit each node once.
> - **Space Complexity:** $O(n)$, because in the worst case, the tree is completely unbalanced, and we need to store the height of each node.
> - **Why these complexities occur:** These complexities occur because we are using a recursive DFS approach to traverse the tree, which requires a stack of size $n$ in the worst case.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a single pass DFS traversal to calculate the height of each node and store the node values at each height in separate lists.
- This approach is optimal because it only requires a single pass through the tree, and we are not storing any unnecessary information.

```cpp
class Solution {
public:
    vector<vector<int>> findLeaves(TreeNode* root) {
        vector<vector<int>> result;
        dfs(root, result);
        return result;
    }
    
    int dfs(TreeNode* node, vector<vector<int>>& result) {
        if (!node) return -1;
        
        int leftHeight = dfs(node->left, result);
        int rightHeight = dfs(node->right, result);
        
        int height = max(leftHeight, rightHeight) + 1;
        
        if (height == result.size()) {
            result.push_back({});
        }
        
        result[height].push_back(node->val);
        
        return height;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, because we visit each node once.
> - **Space Complexity:** $O(n)$, because in the worst case, the tree is completely unbalanced, and we need to store the height of each node.
> - **Optimality proof:** This is the optimal solution because we are only visiting each node once, and we are not storing any unnecessary information.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS traversal, calculating the height of each node.
- Problem-solving patterns identified: using a single pass traversal to solve the problem.
- Optimization techniques learned: avoiding unnecessary calculations and storing only necessary information.

**Mistakes to Avoid:**
- Common implementation errors: not handling the base case correctly, not updating the height of each node correctly.
- Edge cases to watch for: an empty tree, a tree with only one node.
- Performance pitfalls: using an inefficient traversal algorithm, storing unnecessary information.
- Testing considerations: testing the solution with different types of trees, including balanced and unbalanced trees.