## Longest Univalue Path
**Problem Link:** https://leetcode.com/problems/longest-univalue-path/description

**Problem Statement:**
- Input: The root of a binary tree where each node has a unique integer value.
- Constraints: 0 <= number of nodes <= 10^4, -1000 <= Node.val <= 1000.
- Expected Output: The length of the longest path where each node has the same value.
- Key Requirements and Edge Cases:
  - The path must start and end at the same value.
  - The path can be in any direction (left, right, or a combination of both).
  - The path must be continuous, with each node having the same value as the previous one.
- Example Test Cases:
  - Example 1: Given a tree with root node having value 5, and its left and right child having values 4 and 5 respectively, the longest univalue path is 2 (from the root to its right child).
  - Example 2: Given a tree with root node having value 1, and its left child having value 1, and its left child having value 1, the longest univalue path is 3 (from the root to its left child's left child).

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible path in the binary tree to see if it's a univalue path.
- Step-by-step breakdown:
  1. Define a helper function to check if a path is a univalue path.
  2. Use a depth-first search (DFS) approach to explore all paths in the tree.
  3. For each path, check if all nodes have the same value. If they do, update the maximum path length.
- Why this approach comes to mind first: It's a straightforward approach that checks all possible paths, ensuring that no potential solution is missed.

```cpp
// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int longestUnivaluePath(TreeNode* root) {
        if (!root) return 0;
        int maxLen = 0;
        dfs(root, maxLen);
        return maxLen;
    }
    
    void dfs(TreeNode* node, int& maxLen) {
        if (!node) return;
        if (node->left && node->val == node->left->val) {
            int leftLen = getLen(node->left, node->val);
            if (node->right && node->val == node->right->val) {
                int rightLen = getLen(node->right, node->val);
                maxLen = max(maxLen, leftLen + rightLen);
            }
            maxLen = max(maxLen, leftLen);
        }
        if (node->right && node->val == node->right->val) {
            int rightLen = getLen(node->right, node->val);
            maxLen = max(maxLen, rightLen);
        }
        dfs(node->left, maxLen);
        dfs(node->right, maxLen);
    }
    
    int getLen(TreeNode* node, int val) {
        if (!node || node->val != val) return 0;
        return 1 + max(getLen(node->left, val), getLen(node->right, val));
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where n is the number of nodes in the tree, because in the worst case, we might be traversing each node for every other node.
> - **Space Complexity:** $O(h)$ where h is the height of the tree, due to the recursion stack. In the worst case, the tree is skewed, and $h = n$.
> - **Why these complexities occur:** The brute force approach involves checking every possible path, which leads to a high time complexity. The space complexity is due to the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of checking every path, we can use a recursive approach to calculate the length of the longest univalue path passing through each node.
- Detailed breakdown:
  1. Define a recursive function that calculates the length of the longest univalue path passing through a node.
  2. If the node is null, return 0.
  3. Recursively calculate the length of the longest univalue path passing through the left and right children.
  4. If the node's value matches the left or right child's value, update the maximum path length.
- Proof of optimality: This approach ensures that we only visit each node once, reducing the time complexity significantly.

```cpp
class Solution {
public:
    int longestUnivaluePath(TreeNode* root) {
        int maxLen = 0;
        dfs(root, maxLen);
        return maxLen;
    }
    
    int dfs(TreeNode* node, int& maxLen) {
        if (!node) return 0;
        int leftLen = dfs(node->left, maxLen);
        int rightLen = dfs(node->right, maxLen);
        if (node->left && node->val == node->left->val) leftLen++;
        else leftLen = 0;
        if (node->right && node->val == node->right->val) rightLen++;
        else rightLen = 0;
        maxLen = max(maxLen, leftLen + rightLen);
        return max(leftLen, rightLen);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where n is the number of nodes in the tree, because we visit each node exactly once.
> - **Space Complexity:** $O(h)$ where h is the height of the tree, due to the recursion stack. In the worst case, the tree is skewed, and $h = n$.
> - **Optimality proof:** This approach ensures that we only visit each node once, reducing the time complexity significantly. The space complexity remains the same due to the recursive call stack.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive approach, depth-first search, and optimization techniques.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems and solving them recursively.
- Optimization techniques learned: Reducing the time complexity by avoiding redundant calculations and using a recursive approach.
- Similar problems to practice: Longest Increasing Path in a Matrix, Longest Consecutive Sequence.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as null nodes or empty trees.
- Edge cases to watch for: Trees with a single node, trees with no univalue paths.
- Performance pitfalls: Using a brute force approach that leads to high time complexity.
- Testing considerations: Testing the solution with different tree structures and values to ensure correctness.