## Find the Maximum Sum of Node Values
**Problem Link:** https://leetcode.com/problems/find-the-maximum-sum-of-node-values/description

**Problem Statement:**
- Input format and constraints: The problem takes a binary tree as input, where each node has a `val`, `left`, and `right` child.
- Expected output format: The maximum sum of node values from root to a leaf node.
- Key requirements and edge cases to consider: The tree can be empty, and the sum of node values can be negative.
- Example test cases with explanations: 
    - For the tree `[1,2,3]`, the maximum sum is `6` (1 + 2 + 3).
    - For the tree `[5,4,5,1,1,null,5]`, the maximum sum is `15` (5 + 4 + 5).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Traverse the tree using DFS and calculate the sum of node values for each path from root to a leaf node.
- Step-by-step breakdown of the solution: 
    1. Define a helper function to perform DFS.
    2. In the helper function, update the current sum by adding the current node's value.
    3. If the current node is a leaf node, update the maximum sum if the current sum is greater.
    4. Recursively call the helper function for the left and right child nodes.
- Why this approach comes to mind first: It is a straightforward way to traverse the tree and calculate the sum of node values for each path.

```cpp
class Solution {
public:
    int maxSumPath = INT_MIN;
    int maxPathSum(TreeNode* root) {
        dfs(root, 0);
        return maxSumPath;
    }
    
    void dfs(TreeNode* node, int currentSum) {
        if (!node) return;
        currentSum += node->val;
        if (!node->left && !node->right) {
            maxSumPath = max(maxSumPath, currentSum);
        }
        dfs(node->left, currentSum);
        dfs(node->right, currentSum);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, because we visit each node once.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree, because of the recursive call stack.
> - **Why these complexities occur:** The time complexity is linear because we visit each node once, and the space complexity is proportional to the height of the tree because of the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is the same as the brute force approach because we need to visit each node to calculate the sum of node values for each path.
- Detailed breakdown of the approach: 
    1. Define a helper function to perform DFS.
    2. In the helper function, update the current sum by adding the current node's value.
    3. If the current node is a leaf node, update the maximum sum if the current sum is greater.
    4. Recursively call the helper function for the left and right child nodes.
- Proof of optimality: This approach is optimal because we need to visit each node to calculate the sum of node values for each path.
- Why further optimization is impossible: Further optimization is impossible because we need to visit each node at least once to calculate the sum of node values for each path.

```cpp
class Solution {
public:
    int maxSumPath = INT_MIN;
    int maxPathSum(TreeNode* root) {
        dfs(root, 0);
        return maxSumPath;
    }
    
    void dfs(TreeNode* node, int currentSum) {
        if (!node) return;
        currentSum += node->val;
        if (!node->left && !node->right) {
            maxSumPath = max(maxSumPath, currentSum);
        }
        dfs(node->left, currentSum);
        dfs(node->right, currentSum);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, because we visit each node once.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree, because of the recursive call stack.
> - **Optimality proof:** This approach is optimal because we need to visit each node to calculate the sum of node values for each path.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, recursive call stack, and dynamic programming.
- Problem-solving patterns identified: The problem can be solved using a recursive approach with a helper function.
- Optimization techniques learned: The optimal solution is the same as the brute force approach because we need to visit each node to calculate the sum of node values for each path.
- Similar problems to practice: Find the minimum sum of node values from root to a leaf node, find the maximum sum of node values in a subtree.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the maximum sum correctly, not handling the case where the tree is empty.
- Edge cases to watch for: The tree can be empty, and the sum of node values can be negative.
- Performance pitfalls: The recursive call stack can cause a stack overflow for very large trees.
- Testing considerations: Test the solution with different inputs, including empty trees, trees with negative node values, and trees with large node values.