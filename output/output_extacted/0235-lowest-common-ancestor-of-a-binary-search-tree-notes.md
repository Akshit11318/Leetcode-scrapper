## Lowest Common Ancestor of a Binary Search Tree
**Problem Link:** https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description

**Problem Statement:**
- Input format: The root of a binary search tree and two nodes `p` and `q`.
- Constraints: The tree is non-empty and each node has a unique value.
- Expected output format: The lowest common ancestor of `p` and `q`.
- Key requirements: The solution should find the lowest common ancestor of two nodes in a binary search tree.
- Example test cases:
  - Given the binary search tree `[6,2,8,0,4,7,9,null,null,3,5]`, `p = 2` and `q = 8`, return `6`.
  - Given the binary search tree `[6,2,8,0,4,7,9,null,null,3,5]`, `p = 2` and `q = 4`, return `2`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Traverse the tree to find the paths from the root to `p` and `q`, then compare these paths to find the last common node.
- Step-by-step breakdown of the solution:
  1. Define a helper function to find the path from the root to a given node.
  2. Use this helper function to find the paths to `p` and `q`.
  3. Compare the paths to find the last common node, which is the lowest common ancestor.
- Why this approach comes to mind first: It is straightforward and involves basic tree traversal.

```cpp
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        // Helper function to find the path from the root to a given node
        vector<TreeNode*> path;
        bool findPath(TreeNode* node, TreeNode* target, vector<TreeNode*>& path) {
            if (!node) return false;
            path.push_back(node);
            if (node == target) return true;
            if (findPath(node->left, target, path) || findPath(node->right, target, path)) return true;
            path.pop_back();
            return false;
        }
        
        // Find paths to p and q
        vector<TreeNode*> pathP, pathQ;
        findPath(root, p, pathP);
        findPath(root, q, pathQ);
        
        // Compare paths to find the lowest common ancestor
        TreeNode* lca = nullptr;
        for (int i = 0; i < min(pathP.size(), pathQ.size()); ++i) {
            if (pathP[i] == pathQ[i]) lca = pathP[i];
            else break;
        }
        return lca;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, because in the worst case, we might need to traverse the entire tree to find the paths to `p` and `q`.
> - **Space Complexity:** $O(n)$, because we need to store the paths to `p` and `q`, which in the worst case could be the height of the tree or the number of nodes if the tree is skewed.
> - **Why these complexities occur:** The brute force approach involves traversing the tree multiple times and storing the paths, which leads to these complexities.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Since this is a binary search tree, we can utilize the property that all elements to the left of a node are smaller and all elements to the right are larger.
- Detailed breakdown of the approach:
  1. Start at the root of the tree.
  2. Compare the values of `p` and `q` with the current node.
  3. If both `p` and `q` are less than the current node, move to the left subtree.
  4. If both `p` and `q` are greater than the current node, move to the right subtree.
  5. If one is less and one is greater (or equal to the current node), the current node is the lowest common ancestor.
- Proof of optimality: This approach takes advantage of the BST property, reducing the search space at each step, making it more efficient than the brute force approach.
- Why further optimization is impossible: This approach has a time complexity of $O(h)$, where $h$ is the height of the tree, which is the minimum possible time complexity for this problem because we must at least traverse the height of the tree in the worst case.

```cpp
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        // Traverse the tree, utilizing the BST property
        while (root) {
            if (p->val < root->val && q->val < root->val) {
                root = root->left;
            } else if (p->val > root->val && q->val > root->val) {
                root = root->right;
            } else {
                return root;
            }
        }
        return nullptr; // Should not reach here
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(h)$, where $h$ is the height of the tree, because in the worst case, we traverse from the root to a leaf.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the current node and do not use any data structures that scale with input size.
> - **Optimality proof:** This approach is optimal because it takes advantage of the BST property to minimize the number of nodes that need to be visited, resulting in a time complexity that is linear with respect to the height of the tree, which is the minimum required to solve this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Utilizing properties of data structures (in this case, the binary search tree) to optimize solutions.
- Problem-solving patterns identified: Starting with a brute force approach and then optimizing based on the specific characteristics of the problem.
- Optimization techniques learned: Reducing search space by leveraging the properties of the data structure.
- Similar problems to practice: Other problems involving binary search trees or graphs where properties of the data structure can be used to optimize solutions.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle edge cases, such as when `p` or `q` is not in the tree, or not properly utilizing the properties of the data structure.
- Edge cases to watch for: When `p` or `q` is the root, or when one of `p` or `q` is not in the tree.
- Performance pitfalls: Not optimizing the solution based on the properties of the data structure, leading to inefficient algorithms.
- Testing considerations: Thoroughly testing the solution with various inputs, including edge cases, to ensure correctness and efficiency.