## Subtree of Another Tree

**Problem Link:** https://leetcode.com/problems/subtree-of-another-tree/description

**Problem Statement:**
- Given two non-empty trees `s` and `t`, find if `t` has exactly the same structure and node values with a subtree of `s`.
- Input format: Two binary tree nodes, `s` and `t`.
- Constraints: `1 <= number of nodes in s <= 10^4`, `1 <= number of nodes in t <= 10^4`, and the values of the nodes are in the range `[0, 10^4]`.
- Expected output: A boolean indicating whether `t` is a subtree of `s`.
- Key requirements: Correctly identify a subtree within another tree, considering the structure and values of nodes.
- Edge cases: Empty trees, trees with a single node, trees with identical structures but different values.

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible subtree of `s` to see if any match `t`.
- Step-by-step breakdown:
  1. Traverse tree `s` and for each node, consider it as a potential root of a subtree.
  2. For each potential subtree rooted at a node in `s`, compare its structure and node values with `t`.
  3. If a match is found, return `true`.
- This approach comes to mind first because it systematically checks all possibilities, ensuring no potential subtree is overlooked.

```cpp
class Solution {
public:
    bool isSubtree(TreeNode* s, TreeNode* t) {
        if (!s) return false;
        if (isSameTree(s, t)) return true;
        return isSubtree(s->left, t) || isSubtree(s->right, t);
    }

    bool isSameTree(TreeNode* s, TreeNode* t) {
        if (!s && !t) return true;
        if (!s || !t) return false;
        if (s->val != t->val) return false;
        return isSameTree(s->left, t->left) && isSameTree(s->right, t->right);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of nodes in `s` and $m$ is the number of nodes in `t`, because in the worst case, we are comparing every node of `s` with every node of `t`.
> - **Space Complexity:** $O(h_s + h_t)$, where $h_s$ and $h_t$ are the heights of `s` and `t`, respectively, due to the recursive call stack.
> - **Why these complexities occur:** The time complexity is due to the nested traversal and comparison of the two trees, while the space complexity is due to the recursive function calls.

### Optimal Approach (Required)

**Explanation:**
- The key insight is to utilize a recursive approach similar to the brute force but with optimizations in the comparison function.
- Detailed breakdown:
  1. Define a helper function `isSameTree` to compare two trees.
  2. In the main function, recursively traverse `s` and for each node, call `isSameTree` with the current node and `t`.
- This approach is optimal because it minimizes unnecessary comparisons by immediately returning `false` when a mismatch is found.

```cpp
class Solution {
public:
    bool isSubtree(TreeNode* s, TreeNode* t) {
        if (!s) return false;
        if (isSameTree(s, t)) return true;
        return isSubtree(s->left, t) || isSubtree(s->right, t);
    }

    bool isSameTree(TreeNode* s, TreeNode* t) {
        if (!s && !t) return true;
        if (!s || !t || s->val != t->val) return false;
        return isSameTree(s->left, t->left) && isSameTree(s->right, t->right);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, as explained before.
> - **Space Complexity:** $O(h_s + h_t)$, also as explained before.
> - **Optimality proof:** This solution is optimal because it only compares nodes when necessary and stops as soon as it finds a mismatch, minimizing the number of comparisons.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive tree traversal and comparison.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems (comparing subtrees).
- Optimization techniques learned: Early return on finding a mismatch to reduce unnecessary comparisons.
- Similar problems to practice: Other tree and graph traversal problems.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the base cases correctly (e.g., not checking for `NULL` nodes).
- Edge cases to watch for: Empty trees, single-node trees, and trees with identical structures but different values.
- Performance pitfalls: Unnecessary comparisons and deep recursion without optimization.
- Testing considerations: Thoroughly test with various tree structures and values to ensure correctness.