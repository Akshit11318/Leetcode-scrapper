## Lowest Common Ancestor of a Binary Tree III
**Problem Link:** https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/description

**Problem Statement:**
- Given two nodes of a binary tree, find their lowest common ancestor.
- The binary tree is not necessarily a binary search tree.
- Each node has a unique value.
- The tree is represented using a `Node` class with `val`, `left`, and `right` attributes.
- The function should return the `Node` object that represents the lowest common ancestor of the two input nodes.

**Input Format and Constraints:**
- The input is a binary tree and two nodes.
- The tree has at most $10^4$ nodes.
- The values of the nodes are unique.
- The two input nodes are guaranteed to exist in the tree.

**Expected Output Format:**
- The function should return the `Node` object that represents the lowest common ancestor of the two input nodes.

**Key Requirements and Edge Cases to Consider:**
- The two input nodes can be in different subtrees of the tree.
- The two input nodes can be the same node.
- The tree can be unbalanced.
- The tree can have only one node.

**Example Test Cases with Explanations:**
- If the tree is `     1
       / \
      2   3`, and the two nodes are `2` and `3`, the lowest common ancestor is `1`.
- If the tree is `     1
       / \
      2   3`, and the two nodes are `2` and `2`, the lowest common ancestor is `2`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to traverse the tree from the root to find the paths to the two input nodes.
- Then, we can compare the paths to find the last common node, which is the lowest common ancestor.
- This approach comes to mind first because it is a straightforward way to solve the problem.

```cpp
class Solution {
public:
    Node* lowestCommonAncestor(Node* root, Node* p, Node* q) {
        // Base case: if the tree is empty, return nullptr
        if (root == nullptr) {
            return nullptr;
        }

        // If the current node is one of the input nodes, return the current node
        if (root == p || root == q) {
            return root;
        }

        // Recursively search for the input nodes in the left and right subtrees
        Node* left = lowestCommonAncestor(root->left, p, q);
        Node* right = lowestCommonAncestor(root->right, p, q);

        // If both input nodes are found in different subtrees, the current node is the lowest common ancestor
        if (left != nullptr && right != nullptr) {
            return root;
        }

        // If both input nodes are found in the left subtree, the lowest common ancestor is in the left subtree
        if (left != nullptr) {
            return left;
        }

        // If both input nodes are found in the right subtree, the lowest common ancestor is in the right subtree
        if (right != nullptr) {
            return right;
        }

        // If neither input node is found in the left or right subtree, return nullptr
        return nullptr;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, because we visit each node at most twice.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree, because of the recursive call stack.
> - **Why these complexities occur:** The time complexity is linear because we visit each node at most twice, and the space complexity is proportional to the height of the tree because of the recursive call stack.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight that leads to the optimal solution is to use a recursive approach to find the lowest common ancestor.
- The approach is to recursively search for the input nodes in the left and right subtrees.
- If both input nodes are found in different subtrees, the current node is the lowest common ancestor.
- This approach is optimal because it has a time complexity of $O(n)$ and a space complexity of $O(h)$.

```cpp
class Solution {
public:
    Node* lowestCommonAncestor(Node* root, Node* p, Node* q) {
        // Base case: if the tree is empty, return nullptr
        if (root == nullptr) {
            return nullptr;
        }

        // If the current node is one of the input nodes, return the current node
        if (root == p || root == q) {
            return root;
        }

        // Recursively search for the input nodes in the left and right subtrees
        Node* left = lowestCommonAncestor(root->left, p, q);
        Node* right = lowestCommonAncestor(root->right, p, q);

        // If both input nodes are found in different subtrees, the current node is the lowest common ancestor
        if (left != nullptr && right != nullptr) {
            return root;
        }

        // If both input nodes are found in the left subtree, the lowest common ancestor is in the left subtree
        if (left != nullptr) {
            return left;
        }

        // If both input nodes are found in the right subtree, the lowest common ancestor is in the right subtree
        if (right != nullptr) {
            return right;
        }

        // If neither input node is found in the left or right subtree, return nullptr
        return nullptr;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, because we visit each node at most twice.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree, because of the recursive call stack.
> - **Optimality proof:** This approach is optimal because it has a time complexity of $O(n)$ and a space complexity of $O(h)$, which is the best possible complexity for this problem.

---

### Final Notes
**Learning Points:**
- The key algorithmic concept demonstrated is the use of recursive approaches to solve tree problems.
- The problem-solving pattern identified is to use a recursive approach to find the lowest common ancestor of two nodes in a tree.
- The optimization technique learned is to use a recursive approach to reduce the time complexity of the solution.

**Mistakes to Avoid:**
- A common implementation error is to not handle the base case correctly.
- An edge case to watch for is when the two input nodes are the same node.
- A performance pitfall is to use a non-recursive approach, which can have a higher time complexity.
- A testing consideration is to test the solution with different input scenarios, including when the two input nodes are in different subtrees.