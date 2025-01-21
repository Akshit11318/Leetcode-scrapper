## Height of Special Binary Tree
**Problem Link:** https://leetcode.com/problems/height-of-special-binary-tree/description

**Problem Statement:**
- Input format: A binary tree where each node has a value and two children (left and right).
- Constraints: The input tree will have at most 100 nodes.
- Expected output format: The height of the binary tree.
- Key requirements: The height of a binary tree is the number of edges on the longest path from the root to a leaf.
- Edge cases: An empty tree has a height of 0.

Example test cases:
- Input: `root = [1, 0, 0, 0, 0, 0, 0]`
  - Output: `3`
  - Explanation: The height of the binary tree is 3.
- Input: `root = [1, 1, 0, 0, 0, 0, 0]`
  - Output: `2`
  - Explanation: The height of the binary tree is 2.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the height of the binary tree, we can recursively calculate the height of the left and right subtrees and return the maximum height plus one.
- Step-by-step breakdown:
  1. Define a recursive function to calculate the height of a tree.
  2. Base case: If the tree is empty, return 0.
  3. Recursive case: Calculate the height of the left and right subtrees and return the maximum height plus one.

```cpp
class Solution {
public:
    int height(TreeNode* root) {
        if (!root) {
            return 0;
        }
        int leftHeight = height(root->left);
        int rightHeight = height(root->right);
        return max(leftHeight, rightHeight) + 1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, since we visit each node once.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree, due to the recursive call stack.
> - **Why these complexities occur:** The time complexity is linear because we visit each node once, and the space complexity is dependent on the height of the tree because of the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The brute force approach is already optimal for this problem, as we must visit each node at least once to calculate the height of the tree.
- Detailed breakdown: The same approach as the brute force solution.
- Proof of optimality: Since we must visit each node at least once, the time complexity of $O(n)$ is optimal.

```cpp
class Solution {
public:
    int height(TreeNode* root) {
        if (!root) {
            return 0;
        }
        int leftHeight = height(root->left);
        int rightHeight = height(root->right);
        return max(leftHeight, rightHeight) + 1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree.
> - **Optimality proof:** The time complexity is optimal because we must visit each node at least once, and the space complexity is optimal because we only use a recursive call stack of size $h$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concept: Recursion
- Problem-solving pattern: Calculating the height of a tree
- Optimization technique: Using a recursive call stack to calculate the height

**Mistakes to Avoid:**
- Not handling the base case correctly (i.e., returning 0 for an empty tree)
- Not using a recursive approach to calculate the height of the tree
- Not considering the space complexity of the recursive call stack

This problem demonstrates the importance of using recursion to solve tree-related problems and highlights the need to consider both time and space complexity when evaluating solutions.