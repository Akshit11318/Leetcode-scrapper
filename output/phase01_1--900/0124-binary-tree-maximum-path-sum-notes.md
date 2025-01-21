## [Binary Tree Maximum Path Sum]

**Problem Link:** [https://leetcode.com/problems/binary-tree-maximum-path-sum/description](https://leetcode.com/problems/binary-tree-maximum-path-sum/description)

**Problem Statement:**
- Input format: The input is the root of a binary tree.
- Constraints: The number of nodes in the tree is in the range $[1, 10^4]$.
- Expected output format: Return the maximum path sum of any non-empty path in the tree.
- Key requirements and edge cases to consider: 
  - The path must be a valid path in the tree.
  - A path can start and end at any node.
  - Each node can only be used once in the path.
- Example test cases with explanations:
  - Example 1: 
    - Input: root = [1,2,3]
    - Output: 6
    - Explanation: The path 1->2->3 gives the maximum path sum.
  - Example 2: 
    - Input: root = [-10,9,20,null,null,15,7]
    - Output: 42
    - Explanation: The path 20->15->7 gives the maximum path sum.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each node, calculate the maximum path sum that starts and ends at that node. This can be done by calculating the maximum path sum of the left subtree and the right subtree, and then combining them with the current node.
- Step-by-step breakdown of the solution: 
  1. Define a recursive function to calculate the maximum path sum of a subtree.
  2. In the recursive function, calculate the maximum path sum of the left subtree and the right subtree.
  3. Calculate the maximum path sum that includes the current node by combining the maximum path sum of the left subtree, the current node, and the maximum path sum of the right subtree.
  4. Update the maximum path sum if the calculated path sum is greater than the current maximum path sum.
- Why this approach comes to mind first: This approach is intuitive because it considers all possible paths in the tree.

```cpp
class Solution {
public:
    int maxPathSum(TreeNode* root) {
        int max_sum = INT_MIN;
        maxPathSumHelper(root, max_sum);
        return max_sum;
    }
    
    int maxPathSumHelper(TreeNode* node, int& max_sum) {
        if (!node) return 0;
        
        int left_sum = max(0, maxPathSumHelper(node->left, max_sum));
        int right_sum = max(0, maxPathSumHelper(node->right, max_sum));
        
        max_sum = max(max_sum, node->val + left_sum + right_sum);
        
        return node->val + max(left_sum, right_sum);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree, since we visit each node once.
> - **Space Complexity:** $O(H)$, where $H$ is the height of the tree, due to the recursive call stack.
> - **Why these complexities occur:** The time complexity is $O(N)$ because we visit each node once, and the space complexity is $O(H)$ because the recursive call stack can go as deep as the height of the tree.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is the same as the brute force approach, because we need to consider all possible paths in the tree to find the maximum path sum.
- Detailed breakdown of the approach: 
  1. Define a recursive function to calculate the maximum path sum of a subtree.
  2. In the recursive function, calculate the maximum path sum of the left subtree and the right subtree.
  3. Calculate the maximum path sum that includes the current node by combining the maximum path sum of the left subtree, the current node, and the maximum path sum of the right subtree.
  4. Update the maximum path sum if the calculated path sum is greater than the current maximum path sum.
- Proof of optimality: This approach is optimal because it considers all possible paths in the tree and finds the maximum path sum.
- Why further optimization is impossible: Further optimization is impossible because we need to visit each node at least once to find the maximum path sum.

```cpp
class Solution {
public:
    int maxPathSum(TreeNode* root) {
        int max_sum = INT_MIN;
        maxPathSumHelper(root, max_sum);
        return max_sum;
    }
    
    int maxPathSumHelper(TreeNode* node, int& max_sum) {
        if (!node) return 0;
        
        int left_sum = max(0, maxPathSumHelper(node->left, max_sum));
        int right_sum = max(0, maxPathSumHelper(node->right, max_sum));
        
        max_sum = max(max_sum, node->val + left_sum + right_sum);
        
        return node->val + max(left_sum, right_sum);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree, since we visit each node once.
> - **Space Complexity:** $O(H)$, where $H$ is the height of the tree, due to the recursive call stack.
> - **Optimality proof:** This approach is optimal because it considers all possible paths in the tree and finds the maximum path sum.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursion, tree traversal, and dynamic programming.
- Problem-solving patterns identified: Breaking down the problem into smaller subproblems and solving them recursively.
- Optimization techniques learned: Pruning branches that do not contribute to the maximum path sum.
- Similar problems to practice: Maximum Path Sum II, Diameter of Binary Tree.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the base case correctly, not updating the maximum path sum correctly.
- Edge cases to watch for: Empty tree, tree with only one node.
- Performance pitfalls: Not pruning branches that do not contribute to the maximum path sum, resulting in unnecessary computation.
- Testing considerations: Testing with different tree structures and edge cases to ensure the solution is correct and efficient.