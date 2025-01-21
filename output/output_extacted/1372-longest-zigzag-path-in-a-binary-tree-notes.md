## Longest Zigzag Path in a Binary Tree

**Problem Link:** https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description

**Problem Statement:**
- Input: The root of a binary tree.
- Output: The length of the longest zigzag path.
- Key requirements and edge cases to consider:
  - A zigzag path starts at any node and is composed of alternating left and right child nodes.
  - The longest zigzag path may not pass through the root.
- Example test cases with explanations:
  - For the binary tree `[1,1,1,null,1,null,null,1,1,null,1]`, the longest zigzag path has a length of `3`.
  - For an empty tree, the longest zigzag path has a length of `0`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the longest zigzag path, we can start at each node and explore all possible zigzag paths.
- Step-by-step breakdown of the solution:
  1. Perform a depth-first search (DFS) from each node.
  2. At each node, try going left and then right, and going right and then left, to form a zigzag path.
  3. Keep track of the maximum length of the zigzag path found so far.
- Why this approach comes to mind first: It's a straightforward way to explore all possibilities, but it's inefficient due to the repeated computations.

```cpp
class Solution {
public:
    int longestZigZag(TreeNode* root) {
        int maxLen = 0;
        dfs(root, maxLen);
        return maxLen;
    }
    
    void dfs(TreeNode* node, int& maxLen) {
        if (!node) return;
        
        // Try all possible zigzag paths from this node
        if (node->left) {
            dfs(node->left, maxLen);
            if (node->right) dfs(node->right, maxLen);
        }
        if (node->right) {
            dfs(node->right, maxLen);
            if (node->left) dfs(node->left, maxLen);
        }
        
        // Update maxLen if a longer zigzag path is found
        maxLen = max(maxLen, maxLength(node));
    }
    
    int maxLength(TreeNode* node) {
        if (!node) return 0;
        int leftLen = maxLength(node->left);
        int rightLen = maxLength(node->right);
        return max(leftLen, rightLen) + 1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the number of nodes in the tree, because we're trying all possible zigzag paths from each node.
> - **Space Complexity:** $O(n)$, for the recursion stack.
> - **Why these complexities occur:** The brute force approach has an exponential time complexity due to the repeated computations, and a linear space complexity due to the recursion stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of trying all possible zigzag paths, we can keep track of the longest zigzag path ending at each node, with the last edge being either from the left or the right.
- Detailed breakdown of the approach:
  1. Perform a DFS from the root node.
  2. At each node, update the longest zigzag path ending at that node, with the last edge being either from the left or the right.
  3. Keep track of the maximum length of the zigzag path found so far.
- Why further optimization is impossible: This approach has a linear time complexity and only visits each node once, making it optimal.

```cpp
class Solution {
public:
    int longestZigZag(TreeNode* root) {
        int maxLen = 0;
        dfs(root, maxLen);
        return maxLen;
    }
    
    pair<int, int> dfs(TreeNode* node, int& maxLen) {
        if (!node) return {0, 0};
        
        pair<int, int> left = dfs(node->left, maxLen);
        pair<int, int> right = dfs(node->right, maxLen);
        
        // Update maxLen if a longer zigzag path is found
        maxLen = max(maxLen, max(left.second + 1, right.first + 1));
        
        // Return the longest zigzag path ending at this node
        return {left.second + 1, right.first + 1};
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, because we're visiting each node once.
> - **Space Complexity:** $O(n)$, for the recursion stack.
> - **Optimality proof:** This approach is optimal because it visits each node only once and keeps track of the longest zigzag path ending at each node, making it impossible to further optimize the time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, memoization, and optimization techniques.
- Problem-solving patterns identified: Using a recursive approach to solve tree-related problems.
- Optimization techniques learned: Avoiding repeated computations and using memoization to store intermediate results.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, such as an empty tree.
- Edge cases to watch for: Handling the case where a node has only one child.
- Performance pitfalls: Using an exponential time complexity approach, such as the brute force approach.
- Testing considerations: Testing the solution with different tree structures and edge cases to ensure correctness.