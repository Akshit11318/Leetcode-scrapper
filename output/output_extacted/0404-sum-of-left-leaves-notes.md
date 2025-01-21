## Sum of Left Leaves
**Problem Link:** https://leetcode.com/problems/sum-of-left-leaves/description

**Problem Statement:**
- Input: A binary tree represented as a `TreeNode` object.
- Constraints: The number of nodes in the tree is in the range `[1, 1000]`.
- Expected output: The sum of all left leaf node values.
- Key requirements: Identify left leaf nodes and sum their values.
- Edge cases: Handle empty trees, trees with a single node, and trees with no left leaf nodes.
- Example test cases:
  - Example 1: Given a binary tree with the following structure:
    ```
    3
   / \
  9  20
    /  \
   15   7
    ```
    The sum of left leaves is `9 + 15 = 24`.
  - Example 2: Given a binary tree with the following structure:
    ```
    3
     \
      20
     /  \
    15   7
    ```
    The sum of left leaves is `15`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Traverse the tree and check each node to see if it's a left leaf node.
- Step-by-step breakdown:
  1. Define a helper function to perform a depth-first search (DFS) traversal of the tree.
  2. In the helper function, check if the current node is a left leaf node (i.e., it has no children and is the left child of its parent).
  3. If the current node is a left leaf node, add its value to the sum.
  4. Recursively call the helper function on the left and right children of the current node.

```cpp
class Solution {
public:
    int sumOfLeftLeaves(TreeNode* root) {
        int sum = 0;
        dfs(root, false, sum);
        return sum;
    }
    
    void dfs(TreeNode* node, bool isLeft, int& sum) {
        if (!node) return;
        if (!node->left && !node->right && isLeft) sum += node->val;
        dfs(node->left, true, sum);
        dfs(node->right, false, sum);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, since we visit each node once.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree, due to the recursive call stack.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node. The space complexity is proportional to the height of the tree because that's the maximum depth of the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The brute force approach is already optimal because we must visit each node at least once to determine if it's a left leaf node.
- Detailed breakdown: The optimal approach is the same as the brute force approach.
- Proof of optimality: We cannot do better than $O(n)$ time complexity because we must visit each node at least once. The space complexity of $O(h)$ is also optimal because we need to store the recursive call stack.

```cpp
class Solution {
public:
    int sumOfLeftLeaves(TreeNode* root) {
        return dfs(root, false);
    }
    
    int dfs(TreeNode* node, bool isLeft) {
        if (!node) return 0;
        if (!node->left && !node->right && isLeft) return node->val;
        return dfs(node->left, true) + dfs(node->right, false);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree.
> - **Optimality proof:** The time complexity is optimal because we must visit each node at least once. The space complexity is optimal because we need to store the recursive call stack.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Depth-first search (DFS), recursive traversal, and node classification.
- Problem-solving patterns: Identifying and summing specific node values based on their properties.
- Optimization techniques: Recognizing when a brute force approach is already optimal.
- Similar problems to practice: Other tree traversal problems, such as finding the sum of all nodes or the maximum depth of a tree.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, such as an empty tree or a tree with a single node.
- Edge cases to watch for: Trees with no left leaf nodes or trees with a large number of nodes.
- Performance pitfalls: Using an inefficient traversal algorithm or not optimizing the recursive call stack.
- Testing considerations: Thoroughly testing the solution with different tree structures and node values.