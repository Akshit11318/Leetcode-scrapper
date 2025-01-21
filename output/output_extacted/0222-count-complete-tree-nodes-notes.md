## Count Complete Tree Nodes

**Problem Link:** https://leetcode.com/problems/count-complete-tree-nodes/description

**Problem Statement:**
- Given a complete binary tree, count the number of nodes.
- The input is the root of a complete binary tree.
- The expected output is the number of nodes in the tree.
- Key requirements: the tree is complete, meaning every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.
- Edge cases: an empty tree (root is NULL), a tree with one node, or a tree with multiple levels.

**Example Test Cases:**
- Example 1: Input: `[1,2,3,4,5,6]`, Output: `6`
- Example 2: Input: `[1]`, Output: `1`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to traverse the tree and count the nodes.
- We can use a recursive or iterative approach to traverse the tree.
- We start at the root and recursively visit each node, incrementing the count for each node.

```cpp
class Solution {
public:
    int countNodes(TreeNode* root) {
        if (root == NULL) return 0;
        return 1 + countNodes(root->left) + countNodes(root->right);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where n is the number of nodes in the tree, because in the worst case, we visit each node once.
> - **Space Complexity:** $O(n)$, because of the recursive call stack.
> - **Why these complexities occur:** The recursive approach visits each node once, resulting in exponential time complexity, and the recursive call stack uses linear space.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use the properties of a complete binary tree to reduce the number of nodes to visit.
- We can calculate the height of the tree and then use a binary search approach to find the number of nodes in the last level.
- We start at the root and recursively calculate the height of the left and right subtrees.
- We then use a binary search approach to find the number of nodes in the last level.

```cpp
class Solution {
public:
    int countNodes(TreeNode* root) {
        if (root == NULL) return 0;
        int leftHeight = getHeight(root, true);
        int rightHeight = getHeight(root, false);
        if (leftHeight == rightHeight) {
            return (1 << leftHeight) - 1;
        } else {
            return (1 << rightHeight) - 1 + countNodes(root->right) + 1;
        }
    }
    
    int getHeight(TreeNode* node, bool isLeft) {
        int height = 0;
        while (node != NULL) {
            height++;
            if (isLeft) {
                node = node->left;
            } else {
                node = node->right;
            }
        }
        return height;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(log^2 n)$, where n is the number of nodes in the tree, because we calculate the height of the tree and then use a binary search approach to find the number of nodes in the last level.
> - **Space Complexity:** $O(log n)$, because of the recursive call stack.
> - **Optimality proof:** This approach is optimal because it uses the properties of a complete binary tree to reduce the number of nodes to visit, resulting in a significant improvement in time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: recursive and iterative approaches, binary search, and properties of complete binary trees.
- Problem-solving patterns identified: using properties of data structures to reduce complexity.
- Optimization techniques learned: using binary search to reduce the number of nodes to visit.
- Similar problems to practice: counting nodes in a binary tree, finding the height of a binary tree.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases, such as an empty tree or a tree with one node.
- Edge cases to watch for: trees with multiple levels, trees with a large number of nodes.
- Performance pitfalls: using an exponential time complexity approach, not using properties of complete binary trees to reduce complexity.
- Testing considerations: testing with different types of trees, including empty trees, trees with one node, and trees with multiple levels.