## Count Univalue Subtrees
**Problem Link:** https://leetcode.com/problems/count-univalue-subtrees/description

**Problem Statement:**
- Input format and constraints: Given a binary tree, count the number of `univalue` subtrees. A `univalue` subtree is a subtree where all nodes have the same value.
- Expected output format: The function should return the count of `univalue` subtrees.
- Key requirements and edge cases to consider: The function should handle empty trees and trees with a single node. It should also handle trees with multiple nodes, some of which may be `univalue` subtrees.
- Example test cases with explanations:
  - For the input `[5,1,5,5,5,null,5]`, the output should be `4`, because there are four `univalue` subtrees: `[5,5,5]`, `[5]`, `[5]`, and `[5]`.
  - For the input `[5,5,5]`, the output should be `3`, because there are three `univalue` subtrees: `[5,5,5]`, `[5]`, and `[5]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to traverse the tree and check each subtree to see if it's a `univalue` subtree.
- Step-by-step breakdown of the solution:
  1. Traverse the tree using a depth-first search (DFS) approach.
  2. For each node, check if the subtree rooted at that node is a `univalue` subtree.
  3. If it is, increment the count of `univalue` subtrees.
- Why this approach comes to mind first: This approach is straightforward and easy to implement. However, it's not efficient because it checks each subtree multiple times.

```cpp
class Solution {
public:
    int countUnivalSubtrees(TreeNode* root) {
        if (!root) return 0;
        int count = 0;
        if (isUnival(root)) count++;
        count += countUnivalSubtrees(root->left);
        count += countUnivalSubtrees(root->right);
        return count;
    }

    bool isUnival(TreeNode* root) {
        if (!root) return true;
        int val = root->val;
        return isUnival(root->left, val) && isUnival(root->right, val);
    }

    bool isUnival(TreeNode* root, int val) {
        if (!root) return true;
        return root->val == val && isUnival(root->left, val) && isUnival(root->right, val);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of nodes in the tree. This is because in the worst case, we're checking each subtree multiple times.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree. This is because of the recursive call stack.
> - **Why these complexities occur:** The time complexity occurs because we're using a recursive approach to check each subtree, and in the worst case, we're checking each subtree multiple times. The space complexity occurs because of the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking each subtree multiple times, we can check each subtree only once and store the result.
- Detailed breakdown of the approach:
  1. Traverse the tree using a DFS approach.
  2. For each node, check if the subtree rooted at that node is a `univalue` subtree.
  3. If it is, increment the count of `univalue` subtrees and return `true`.
  4. If it's not, return `false`.
- Proof of optimality: This approach is optimal because we're checking each subtree only once, which reduces the time complexity to $O(n)$.
- Why further optimization is impossible: We have to check each subtree at least once to determine if it's a `univalue` subtree, so we can't do better than $O(n)$ time complexity.

```cpp
class Solution {
public:
    int count = 0;
    bool isUnival(TreeNode* root) {
        if (!root) return true;
        bool left = isUnival(root->left);
        bool right = isUnival(root->right);
        if (left && right && (root->left == NULL || root->left->val == root->val) && (root->right == NULL || root->right->val == root->val)) {
            count++;
            return true;
        }
        return false;
    }

    int countUnivalSubtrees(TreeNode* root) {
        isUnival(root);
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we're checking each subtree only once.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree. This is because of the recursive call stack.
> - **Optimality proof:** This approach is optimal because we're checking each subtree only once, which reduces the time complexity to $O(n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive DFS, checking for `univalue` subtrees.
- Problem-solving patterns identified: Checking each subtree only once to reduce time complexity.
- Optimization techniques learned: Storing the result of checking each subtree to avoid checking it multiple times.
- Similar problems to practice: Other problems involving recursive DFS and checking for specific properties in a tree.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for `NULL` pointers, not handling edge cases.
- Edge cases to watch for: Empty trees, trees with a single node.
- Performance pitfalls: Checking each subtree multiple times, which can lead to high time complexity.
- Testing considerations: Test the function with different types of trees, including empty trees and trees with a single node.