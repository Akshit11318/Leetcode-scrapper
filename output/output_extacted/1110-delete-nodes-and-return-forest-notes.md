## Delete Nodes and Return Forest

**Problem Link:** https://leetcode.com/problems/delete-nodes-and-return-forest/description

**Problem Statement:**
- Input format: A binary tree where each node has a value and two child pointers (`left` and `right`).
- Constraints: The input tree is not guaranteed to be balanced or have any specific structure.
- Expected output format: A list of roots of the resulting forest after deleting nodes with specified values.
- Key requirements and edge cases to consider:
  - Handling the case where the root node itself needs to be deleted.
  - Ensuring that all nodes with the specified values are removed, and the resulting trees are correctly identified.
- Example test cases with explanations:
  - Deleting a leaf node, an internal node, and the root node.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Traverse the tree, check each node's value against the list of nodes to delete, and manually manage the tree structure by updating child pointers and handling the case where a node to be deleted has children.
- Step-by-step breakdown of the solution:
  1. Perform a depth-first search (DFS) or breadth-first search (BFS) traversal of the tree.
  2. For each node, check if its value is in the list of nodes to delete.
  3. If a node is to be deleted, handle its children:
    - If the node has no children, simply remove it by updating its parent's child pointer.
    - If the node has one child, replace the node with its child.
    - If the node has two children, this approach becomes complicated as it involves finding a replacement node (e.g., the node's in-order successor or predecessor) or merging the subtrees.
  4. After handling all nodes, collect the roots of the resulting forest.

```cpp
vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
    vector<TreeNode*> result;
    unordered_set<int> deleteSet(to_delete.begin(), to_delete.end());
    
    function<void(TreeNode*)> dfs = [&](TreeNode* node) {
        if (!node) return;
        
        dfs(node->left);
        dfs(node->right);
        
        if (deleteSet.find(node->val) != deleteSet.end()) {
            // Handle deletion logic here, but this approach quickly becomes cumbersome
            // without a clear, systematic way to manage the tree structure changes.
        }
    };
    
    dfs(root);
    // The brute force approach does not easily lend itself to a clean, systematic
    // implementation due to the complexity of handling node deletions and tree restructuring.
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree, because we visit each node once.
> - **Space Complexity:** $O(N)$, for the recursion stack in the worst case (when the tree is skewed) and for storing the result.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node. The space complexity is also linear due to the recursion stack and the storage needed for the result.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use a recursive approach to delete nodes and return the roots of the resulting forest. This involves checking if a node should be deleted and then handling its children appropriately.
- Detailed breakdown of the approach:
  1. Define a recursive function that takes a node and returns a list of roots of the subtrees that are not deleted.
  2. Within the function, check if the current node should be deleted. If it should, recursively call the function on its children and collect the roots of the resulting subtrees.
  3. If the current node should not be deleted, add it to the result if it's a root (i.e., it's the original root or its parent was deleted), and then recursively process its children.
- Proof of optimality: This approach is optimal because it visits each node exactly once, performing a constant amount of work for each node, thus achieving a linear time complexity.

```cpp
vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
    unordered_set<int> deleteSet(to_delete.begin(), to_delete.end());
    vector<TreeNode*> result;
    
    function<TreeNode*(TreeNode*)> dfs = [&](TreeNode* node) {
        if (!node) return nullptr;
        
        node->left = dfs(node->left);
        node->right = dfs(node->right);
        
        if (deleteSet.find(node->val) != deleteSet.end()) {
            if (node->left) result.push_back(node->left);
            if (node->right) result.push_back(node->right);
            return nullptr; // Node is deleted
        }
        
        return node; // Node is not deleted
    };
    
    if (dfs(root)) result.push_back(root); // If root is not deleted, add it to the result
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree, because we visit each node once.
> - **Space Complexity:** $O(N)$, for the recursion stack in the worst case and for storing the result.
> - **Optimality proof:** The approach is optimal because it achieves a linear time complexity by visiting each node exactly once and performing a constant amount of work for each node.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive tree traversal, node deletion, and tree restructuring.
- Problem-solving patterns identified: Using recursion to solve tree-related problems and handling edge cases systematically.
- Optimization techniques learned: Achieving linear time complexity by visiting each node exactly once.
- Similar problems to practice: Other tree manipulation problems, such as inserting nodes, finding paths, or calculating tree properties.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases (e.g., a null tree, deleting the root), incorrectly managing tree structure changes.
- Edge cases to watch for: Deleting the root node, handling nodes with one or two children.
- Performance pitfalls: Using inefficient data structures or algorithms that lead to higher than necessary time or space complexity.
- Testing considerations: Thoroughly testing with various input scenarios, including edge cases and large inputs to ensure correctness and performance.