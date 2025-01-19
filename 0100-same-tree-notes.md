## Same Tree

**Problem Link:** [leetcode.com/problems/same-tree/description](https://leetcode.com/problems/same-tree/description)

**Problem Statement:**
- Input format: Two binary trees, `p` and `q`.
- Constraints: Each tree has at most 100 nodes, and each node has a value between 0 and 9.
- Expected output format: A boolean indicating whether the two trees are the same.
- Key requirements and edge cases to consider:
  - Empty trees are considered the same.
  - Trees with different structures or values are not the same.
- Example test cases:
  - Example 1:
    - Input: `p = [1,2,3]`, `q = [1,2,3]`
    - Output: `true`
    - Explanation: Both trees have the same structure and values.
  - Example 2:
    - Input: `p = [1,2]`, `q = [1,null,2]`
    - Output: `false`
    - Explanation: The trees have different structures.

---

### Initial Approach

**Explanation:**
- Initial thought process: To determine if two trees are the same, we need to compare their structures and values recursively.
- Step-by-step breakdown of the solution:
  1. If both trees are empty, they are the same.
  2. If one tree is empty and the other is not, they are not the same.
  3. If both trees are not empty, compare their values and recursively compare their left and right subtrees.
- Why this approach comes to mind first: It is a straightforward recursive approach that checks all nodes in both trees.

```cpp
// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        // If both trees are empty, they are the same
        if (p == NULL && q == NULL) {
            return true;
        }
        // If one tree is empty and the other is not, they are not the same
        if (p == NULL || q == NULL) {
            return false;
        }
        // If both trees are not empty, compare their values and recursively compare their left and right subtrees
        if (p->val != q->val) {
            return false;
        }
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** O(N), where N is the total number of nodes in both trees, since we visit each node once.
> - **Space Complexity:** O(H), where H is the height of the deeper tree, since that is the maximum depth of the recursive call stack.
> - **Why these complexities occur:** The time complexity is O(N) because we visit each node once, and the space complexity is O(H) because of the recursive call stack.

---

### Better Approach

**Explanation:**
- Key insight that leads to improvement: The initial approach is already optimal in terms of time complexity, but we can improve the code by reducing the number of comparisons and making it more concise.
- How it improves upon the initial approach: The improved code reduces the number of comparisons and makes the code more concise.
- Detailed breakdown of the approach:
  1. If both trees are empty, they are the same.
  2. If one tree is empty and the other is not, they are not the same.
  3. If both trees are not empty, compare their values and recursively compare their left and right subtrees.
- Concrete examples of the improvements:
  - Reduced number of comparisons.
  - More concise code.

```cpp
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (!p && !q) return true;
        if (!p || !q || p->val != q->val) return false;
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** O(N), where N is the total number of nodes in both trees, since we visit each node once.
> - **Space Complexity:** O(H), where H is the height of the deeper tree, since that is the maximum depth of the recursive call stack.
> - **Improvement over initial approach:** The improved code reduces the number of comparisons and makes the code more concise.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive tree traversal, comparison of tree structures and values.
- Problem-solving patterns identified: Recursive approach, comparison of tree nodes.
- Optimization techniques learned: Reducing the number of comparisons, making the code more concise.
- Similar problems to practice: Tree traversal, tree comparison, recursive algorithms.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for empty trees, not comparing tree values correctly.
- Edge cases to watch for: Empty trees, trees with different structures or values.
- Performance pitfalls: Not optimizing the code for performance.
- Testing considerations: Testing the code with different input cases, including empty trees and trees with different structures and values.