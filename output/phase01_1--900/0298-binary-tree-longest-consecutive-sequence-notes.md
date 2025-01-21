## Binary Tree Longest Consecutive Sequence

**Problem Link:** https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/description

**Problem Statement:**
- Given a binary tree, find the length of the longest consecutive sequence path.
- The path can be either increasing or decreasing, and each node's value must be consecutive.
- Input: A binary tree's root node.
- Expected output: The length of the longest consecutive sequence path.
- Key requirements and edge cases to consider: The path can be either increasing or decreasing, and the tree may be empty.
- Example test cases with explanations:
  - For a tree with nodes 1, 2, and 3, where node 1 has a left child of 2 and a right child of 3, the longest consecutive sequence path is of length 2.
  - For an empty tree, the longest consecutive sequence path is 0.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Perform a depth-first search (DFS) for each node in the tree, exploring all possible paths.
- Step-by-step breakdown of the solution:
  1. Start DFS from each node in the tree.
  2. For each node, explore all possible paths (both increasing and decreasing sequences).
  3. Keep track of the longest consecutive sequence path found so far.
- Why this approach comes to mind first: It is a straightforward approach to explore all possibilities, but it is inefficient due to the repeated computations.

```cpp
class Solution {
public:
    int longestConsecutive(TreeNode* root) {
        if (!root) return 0;
        int maxLen = 0;
        dfs(root, root->val, 1, maxLen, true);
        dfs(root, root->val, 1, maxLen, false);
        return maxLen;
    }

    void dfs(TreeNode* node, int parentVal, int currLen, int& maxLen, bool isIncreasing) {
        if (!node) return;
        if ((isIncreasing && node->val == parentVal + 1) || (!isIncreasing && node->val == parentVal - 1)) {
            currLen++;
        } else {
            currLen = 1;
        }
        maxLen = max(maxLen, currLen);
        dfs(node->left, node->val, currLen, maxLen, isIncreasing);
        dfs(node->right, node->val, currLen, maxLen, isIncreasing);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot h)$, where $n$ is the number of nodes and $h$ is the height of the tree, because in the worst case, we visit each node $h$ times.
> - **Space Complexity:** $O(h)$, for the recursion stack.
> - **Why these complexities occur:** The time complexity is high due to the repeated DFS calls from each node, and the space complexity is due to the recursion stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of performing DFS from each node, we can pass the current sequence length and the parent's value as parameters to the DFS function.
- Detailed breakdown of the approach:
  1. Perform DFS from the root node, passing the current sequence length and the parent's value as parameters.
  2. For each node, check if the current node's value is consecutive to the parent's value.
  3. If it is, update the current sequence length and update the maximum sequence length if necessary.
- Proof of optimality: This approach has a time complexity of $O(n)$, which is the minimum required to visit each node once.

```cpp
class Solution {
public:
    int longestConsecutive(TreeNode* root) {
        if (!root) return 0;
        int maxLen = 0;
        dfs(root, NULL, 0, maxLen);
        return maxLen;
    }

    void dfs(TreeNode* node, TreeNode* parent, int currLen, int& maxLen) {
        if (!node) return;
        if (parent && (node->val == parent->val + 1 || node->val == parent->val - 1)) {
            currLen++;
        } else {
            currLen = 1;
        }
        maxLen = max(maxLen, currLen);
        dfs(node->left, node, currLen, maxLen);
        dfs(node->right, node, currLen, maxLen);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes, because we visit each node once.
> - **Space Complexity:** $O(h)$, for the recursion stack.
> - **Optimality proof:** This approach has the minimum required time complexity to visit each node once, making it optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, recursion, and sequence length tracking.
- Problem-solving patterns identified: Avoiding repeated computations by passing parameters to recursive functions.
- Optimization techniques learned: Reducing the number of function calls by passing relevant information as parameters.
- Similar problems to practice: Other tree traversal and sequence-related problems.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty tree or nodes with the same value.
- Edge cases to watch for: Handling sequences with decreasing values.
- Performance pitfalls: Not optimizing the solution to avoid repeated computations.
- Testing considerations: Testing the solution with different tree structures and edge cases.