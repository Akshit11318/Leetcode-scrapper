## Lowest Common Ancestor of a Binary Tree IV
**Problem Link:** https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/description

**Problem Statement:**
- Input format and constraints: Given the `root` of a binary tree and an array of `node` values, find the lowest common ancestor (LCA) of all the nodes in the array.
- Expected output format: Return the `TreeNode` that is the LCA of all the nodes in the array.
- Key requirements and edge cases to consider: The binary tree is not necessarily a binary search tree, and the nodes in the array may not be unique. The LCA is the node farthest from the root that is an ancestor of all the nodes in the array.
- Example test cases with explanations:
  - Example 1: 
    - Input: `root = [3,5,1,6,2,0,8,null,null,7,4]`, `nodes = [4,7]`
    - Output: `2`
    - Explanation: The lowest common ancestor of nodes 4 and 7 is node 2.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Find the path from the root to each node in the array, then find the last common node in all the paths.
- Step-by-step breakdown of the solution:
  1. Perform a depth-first search (DFS) to find the path from the root to each node in the array.
  2. Store the paths in a data structure such as a vector of vectors.
  3. Iterate through the paths to find the last common node.
- Why this approach comes to mind first: It is a straightforward approach that involves finding the paths to each node and then comparing the paths to find the common ancestor.

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, vector<int>& nodes) {
        // Find the paths from the root to each node
        vector<vector<int>> paths;
        for (int node : nodes) {
            vector<int> path;
            findPath(root, node, path);
            paths.push_back(path);
        }
        
        // Find the last common node in all the paths
        vector<int> lcaPath = paths[0];
        for (int i = 1; i < paths.size(); i++) {
            vector<int> path = paths[i];
            int j = 0;
            while (j < lcaPath.size() && j < path.size() && lcaPath[j] == path[j]) {
                j++;
            }
            lcaPath.resize(j);
        }
        
        // Find the node corresponding to the last common node in the path
        TreeNode* lca = root;
        for (int node : lcaPath) {
            if (lca->val == node) {
                if (lca->left && lca->left->val == node) {
                    lca = lca->left;
                } else if (lca->right && lca->right->val == node) {
                    lca = lca->right;
                }
            }
        }
        return lca;
    }
    
    void findPath(TreeNode* root, int node, vector<int>& path) {
        if (!root) return;
        path.push_back(root->val);
        if (root->val == node) return;
        findPath(root->left, node, path);
        if (path.back() == node) return;
        findPath(root->right, node, path);
        if (path.back() == node) return;
        path.pop_back();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where $n$ is the number of nodes in the tree and $m$ is the number of nodes in the array. This is because we perform a DFS for each node in the array.
> - **Space Complexity:** $O(n \times m)$, where $n$ is the number of nodes in the tree and $m$ is the number of nodes in the array. This is because we store the paths to each node in the array.
> - **Why these complexities occur:** The time complexity occurs because we perform a DFS for each node in the array, and the space complexity occurs because we store the paths to each node in the array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a recursive approach to find the LCA of two nodes, and then use this approach to find the LCA of all nodes in the array.
- Detailed breakdown of the approach:
  1. Define a recursive function to find the LCA of two nodes.
  2. Use this function to find the LCA of all nodes in the array.
- Proof of optimality: This approach is optimal because it only requires a single pass through the tree to find the LCA of all nodes.
- Why further optimization is impossible: This approach is already optimal because it only requires a single pass through the tree.

```cpp
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, vector<int>& nodes) {
        unordered_set<int> nodeSet(nodes.begin(), nodes.end());
        return findLCA(root, nodeSet);
    }
    
    TreeNode* findLCA(TreeNode* root, unordered_set<int>& nodeSet) {
        if (!root) return nullptr;
        if (nodeSet.count(root->val)) return root;
        
        TreeNode* left = findLCA(root->left, nodeSet);
        TreeNode* right = findLCA(root->right, nodeSet);
        
        if (left && right) return root;
        return left ? left : right;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we only require a single pass through the tree.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we use a recursive approach that requires space on the call stack.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the tree to find the LCA of all nodes.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive approach, LCA of a binary tree.
- Problem-solving patterns identified: Using a recursive approach to solve a problem that requires finding the LCA of multiple nodes.
- Optimization techniques learned: Using a recursive approach to reduce the time complexity of a problem.
- Similar problems to practice: Finding the LCA of two nodes in a binary tree, finding the LCA of multiple nodes in a binary tree.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where a node is not found in the tree.
- Edge cases to watch for: The case where the input array is empty, the case where the tree is empty.
- Performance pitfalls: Using an approach that requires multiple passes through the tree.
- Testing considerations: Testing the function with different inputs, including edge cases.