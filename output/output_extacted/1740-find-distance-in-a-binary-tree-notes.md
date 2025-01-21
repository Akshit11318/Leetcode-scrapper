## Find Distance in a Binary Tree
**Problem Link:** https://leetcode.com/problems/find-distance-in-a-binary-tree/description

**Problem Statement:**
- Given a binary tree and two nodes, find the distance between these nodes.
- The distance between two nodes is defined as the number of edges between them.
- Input: The root of the binary tree and the values of the two nodes.
- Expected output: The distance between the two nodes.
- Key requirements and edge cases: The tree may not contain the nodes, and the nodes may be the same.
- Example test cases:
  - For a tree with nodes 1, 2, 3, 4, 5, and the nodes 2 and 3, the distance is 1.
  - For a tree with nodes 1, 2, 3, 4, 5, and the nodes 2 and 4, the distance is 2.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to find the paths from the root to each node and then find the common ancestor.
- Step-by-step breakdown:
  1. Find the path from the root to the first node.
  2. Find the path from the root to the second node.
  3. Find the common ancestor by comparing the paths.
  4. Calculate the distance by finding the length of the paths from the common ancestor to each node.

```cpp
class Solution {
public:
    int findDistance(TreeNode* root, int p, int q) {
        // Base case
        if (root == nullptr) return 0;

        // Find the path from the root to the first node
        vector<int> path1 = findPath(root, p);

        // Find the path from the root to the second node
        vector<int> path2 = findPath(root, q);

        // Find the common ancestor
        int commonAncestor = findCommonAncestor(path1, path2);

        // Calculate the distance
        int distance = findDistanceFromCommonAncestor(root, p, commonAncestor) + findDistanceFromCommonAncestor(root, q, commonAncestor);

        return distance;
    }

    // Helper function to find the path from the root to a node
    vector<int> findPath(TreeNode* root, int target) {
        if (root == nullptr) return {};

        vector<int> path;
        findPathHelper(root, target, path);
        return path;
    }

    // Helper function to find the path from the root to a node
    bool findPathHelper(TreeNode* root, int target, vector<int>& path) {
        if (root == nullptr) return false;

        path.push_back(root->val);

        if (root->val == target) return true;

        if (findPathHelper(root->left, target, path) || findPathHelper(root->right, target, path)) return true;

        path.pop_back();
        return false;
    }

    // Helper function to find the common ancestor
    int findCommonAncestor(vector<int>& path1, vector<int>& path2) {
        for (int i = 0; i < min(path1.size(), path2.size()); i++) {
            if (path1[i] != path2[i]) {
                return path1[i - 1];
            }
        }
        return path1.back();
    }

    // Helper function to find the distance from the common ancestor to a node
    int findDistanceFromCommonAncestor(TreeNode* root, int target, int commonAncestor) {
        if (root == nullptr) return 0;

        if (root->val == commonAncestor) return 0;

        if (root->val == target) return 1;

        return 1 + findDistanceFromCommonAncestor(root->left, target, commonAncestor) + findDistanceFromCommonAncestor(root->right, target, commonAncestor);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of nodes in the tree, because in the worst case, we need to traverse the entire tree to find the paths.
> - **Space Complexity:** $O(n)$ because we need to store the paths in the vectors.
> - **Why these complexities occur:** The time complexity occurs because we need to traverse the tree to find the paths, and the space complexity occurs because we need to store the paths in the vectors.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to find the lowest common ancestor (LCA) of the two nodes.
- The LCA is the node that is farthest from the root and is an ancestor of both nodes.
- We can find the LCA by traversing the tree and keeping track of the ancestors of each node.
- Once we have the LCA, we can find the distance by calculating the length of the paths from the LCA to each node.

```cpp
class Solution {
public:
    int findDistance(TreeNode* root, int p, int q) {
        // Find the LCA
        TreeNode* lca = findLCA(root, p, q);

        // Calculate the distance
        int distance = findDistanceFromLCA(root, p, lca) + findDistanceFromLCA(root, q, lca);

        return distance;
    }

    // Helper function to find the LCA
    TreeNode* findLCA(TreeNode* root, int p, int q) {
        if (root == nullptr) return nullptr;

        if (root->val == p || root->val == q) return root;

        TreeNode* left = findLCA(root->left, p, q);
        TreeNode* right = findLCA(root->right, p, q);

        if (left != nullptr && right != nullptr) return root;

        return left != nullptr ? left : right;
    }

    // Helper function to find the distance from the LCA to a node
    int findDistanceFromLCA(TreeNode* root, int target, TreeNode* lca) {
        if (root == nullptr) return -1;

        if (root->val == target) return 0;

        int left = findDistanceFromLCA(root->left, target, lca);
        int right = findDistanceFromLCA(root->right, target, lca);

        if (left != -1) return 1 + left;
        if (right != -1) return 1 + right;

        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of nodes in the tree, because in the worst case, we need to traverse the entire tree to find the LCA.
> - **Space Complexity:** $O(1)$ because we only need to keep track of the LCA and the distances.
> - **Optimality proof:** This is the optimal solution because we only need to traverse the tree once to find the LCA, and then we can calculate the distance in constant time.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is finding the lowest common ancestor (LCA) of two nodes in a binary tree.
- The problem-solving pattern identified is using a recursive approach to traverse the tree and find the LCA.
- The optimization technique learned is to use a single traversal of the tree to find the LCA, rather than multiple traversals.
- Similar problems to practice are finding the LCA in a binary search tree, and finding the distance between two nodes in a graph.

**Mistakes to Avoid:**
- A common implementation error is to not handle the case where the tree does not contain the nodes.
- An edge case to watch for is when the nodes are the same.
- A performance pitfall is to use a brute force approach that traverses the tree multiple times.
- A testing consideration is to test the solution with different types of trees, such as balanced and unbalanced trees, and with different node values.