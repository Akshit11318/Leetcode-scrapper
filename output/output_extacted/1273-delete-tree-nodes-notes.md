## Delete Tree Nodes
**Problem Link:** https://leetcode.com/problems/delete-tree-nodes/description

**Problem Statement:**
- Input: A binary tree and a list of values to delete (`tree`, `del_nodes`).
- Output: The number of nodes in each tree after deletion.
- Key requirements: Delete the specified nodes and count the nodes in each resulting tree.
- Edge cases: Empty tree, nodes not found in the tree.

Example test cases:
- Input: `[1,2,3,null,4,null,5]`, `[3,5]`
- Output: `[1,1,1]`

### Brute Force Approach

**Explanation:**
1. Create a function to delete a node from the binary tree.
2. Iterate over the list of nodes to delete and call the delete function for each node.
3. Count the number of nodes in each resulting tree.

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
    vector<int> delNodes(TreeNode* root, vector<int>& to_delete) {
        vector<int> result;
        for (int val : to_delete) {
            root = deleteNode(root, val);
            result.push_back(countNodes(root));
        }
        return result;
    }

    TreeNode* deleteNode(TreeNode* root, int val) {
        if (!root) return root;
        if (root->val == val) {
            return merge(root->left, root->right);
        }
        root->left = deleteNode(root->left, val);
        root->right = deleteNode(root->right, val);
        return root;
    }

    TreeNode* merge(TreeNode* left, TreeNode* right) {
        if (!left) return right;
        if (!right) return left;
        // This is a simplified version, in a real scenario, you would need to properly merge the trees
        left->right = merge(left->right, right);
        return left;
    }

    int countNodes(TreeNode* root) {
        if (!root) return 0;
        return 1 + countNodes(root->left) + countNodes(root->right);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot h)$, where $n$ is the number of nodes to delete, $m$ is the number of nodes in the tree, and $h$ is the height of the tree.
> - **Space Complexity:** $O(h)$, for the recursive call stack.
> - **Why these complexities occur:** The time complexity is due to the recursive deletion and counting of nodes, and the space complexity is due to the recursive call stack.

### Optimal Approach (Required)

**Explanation:**
1. Create a function to perform a depth-first search (DFS) on the tree.
2. During the DFS, check if the current node is in the list of nodes to delete.
3. If it is, remove the node and recursively count the nodes in the resulting subtrees.
4. If it's not, recursively count the nodes in the subtree.

```cpp
class Solution {
public:
    vector<int> delNodes(TreeNode* root, vector<int>& to_delete) {
        unordered_set<int> del_set(to_delete.begin(), to_delete.end());
        vector<int> result;
        dfs(root, del_set, result);
        return result;
    }

    TreeNode* dfs(TreeNode* root, unordered_set<int>& del_set, vector<int>& result) {
        if (!root) return nullptr;
        root->left = dfs(root->left, del_set, result);
        root->right = dfs(root->right, del_set, result);
        if (del_set.find(root->val) != del_set.end()) {
            if (root->left) {
                result.push_back(countNodes(root->left));
            }
            if (root->right) {
                result.push_back(countNodes(root->right));
            }
            return nullptr;
        }
        return root;
    }

    int countNodes(TreeNode* root) {
        if (!root) return 0;
        return 1 + countNodes(root->left) + countNodes(root->right);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m)$, where $m$ is the number of nodes in the tree.
> - **Space Complexity:** $O(h)$, for the recursive call stack.
> - **Optimality proof:** This approach is optimal because it only visits each node once during the DFS, and it only counts the nodes in the resulting subtrees when a node is deleted.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, tree manipulation.
- Problem-solving patterns identified: recursive approach, node deletion.
- Optimization techniques learned: reducing the number of node visits, using a set for fast lookup.
- Similar problems to practice: tree traversal, node insertion, tree merging.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases (e.g., empty tree, nodes not found).
- Performance pitfalls: using an inefficient data structure (e.g., a list instead of a set) for fast lookup.
- Testing considerations: testing with different tree structures, node values, and deletion lists.