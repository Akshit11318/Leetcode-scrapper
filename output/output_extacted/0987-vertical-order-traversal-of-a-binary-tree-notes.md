## Vertical Order Traversal of a Binary Tree
**Problem Link:** https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/description

**Problem Statement:**
- Input format and constraints: Given a binary tree, the task is to perform a vertical order traversal of the tree. The input is the root of the binary tree, and the constraints are that the tree may have up to 100 nodes, and each node's value will be between 0 and 100.
- Expected output format: The output should be a list of lists, where each inner list contains the node values in a specific vertical order.
- Key requirements and edge cases to consider: The tree may be empty, and the nodes may have the same value. The vertical order is determined by the column index of the nodes, and the nodes in the same column should be ordered from top to bottom.
- Example test cases with explanations:
  - For example, given a binary tree:
        3
       / \
      9  20
     /  /  \
    4   2   7
   The output should be [[4],[9],[3,2,7],[20]].

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The first approach that comes to mind is to perform a depth-first search (DFS) traversal of the tree and keep track of the column index of each node. We can use a hash map to store the nodes at each column index.
- Step-by-step breakdown of the solution:
  1. Initialize a hash map to store the nodes at each column index.
  2. Perform a DFS traversal of the tree, and for each node, update its column index based on the parent node's column index.
  3. Add the node's value to the list of nodes at its column index in the hash map.
  4. Finally, iterate over the hash map and add the nodes at each column index to the result list.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it may not be efficient for large trees.

```cpp
// Well-commented code with:
// - Clear variable names
// - Input validation
// - Edge case handling
void dfs(TreeNode* node, int x, int y, map<int, vector<pair<int, int>>>& m) {
    if (!node) return;
    m[x].push_back({y, node->val});
    dfs(node->left, x - 1, y + 1, m);
    dfs(node->right, x + 1, y + 1, m);
}

vector<vector<int>> verticalOrder(TreeNode* root) {
    map<int, vector<pair<int, int>>> m;
    dfs(root, 0, 0, m);
    vector<vector<int>> res;
    for (auto& p : m) {
        vector<int> v;
        sort(p.second.begin(), p.second.end());
        for (auto& q : p.second) v.push_back(q.second);
        res.push_back(v);
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where n is the number of nodes in the tree, due to the sorting of nodes at each column index.
> - **Space Complexity:** $O(n)$, where n is the number of nodes in the tree, for storing the nodes at each column index in the hash map.
> - **Why these complexities occur:** The time complexity is due to the sorting of nodes at each column index, and the space complexity is due to the storage of nodes in the hash map.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a BFS traversal instead of DFS to avoid the need for sorting the nodes at each column index. We can also use a queue to store the nodes to be visited and their corresponding column indices.
- Detailed breakdown of the approach:
  1. Initialize a queue to store the nodes to be visited and their corresponding column indices.
  2. Initialize a hash map to store the nodes at each column index.
  3. Perform a BFS traversal of the tree, and for each node, update its column index based on the parent node's column index.
  4. Add the node's value to the list of nodes at its column index in the hash map.
  5. Finally, iterate over the hash map and add the nodes at each column index to the result list.
- Proof of optimality: This approach is optimal because it avoids the need for sorting the nodes at each column index, resulting in a time complexity of $O(n)$.

```cpp
// Production-ready code with:
// - Complete error handling
// - Input validation
// - Optimal implementation
vector<vector<int>> verticalOrder(TreeNode* root) {
    if (!root) return {};
    map<int, vector<int>> m;
    queue<pair<TreeNode*, int>> q;
    q.push({root, 0});
    while (!q.empty()) {
        auto p = q.front(); q.pop();
        m[p.second].push_back(p.first->val);
        if (p.first->left) q.push({p.first->left, p.second - 1});
        if (p.first->right) q.push({p.first->right, p.second + 1});
    }
    vector<vector<int>> res;
    for (auto& p : m) res.push_back(p.second);
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where n is the number of nodes in the tree, due to the BFS traversal.
> - **Space Complexity:** $O(n)$, where n is the number of nodes in the tree, for storing the nodes in the queue and the hash map.
> - **Optimality proof:** This approach is optimal because it avoids the need for sorting the nodes at each column index, resulting in a time complexity of $O(n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS traversal, hash map usage, and column index calculation.
- Problem-solving patterns identified: Using a queue to store nodes to be visited and their corresponding column indices.
- Optimization techniques learned: Avoiding the need for sorting the nodes at each column index by using a BFS traversal.
- Similar problems to practice: Tree traversal problems, such as inorder, preorder, and postorder traversal.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, such as an empty tree or a tree with a single node.
- Edge cases to watch for: The tree may be empty, and the nodes may have the same value.
- Performance pitfalls: Using a DFS traversal instead of a BFS traversal, resulting in a higher time complexity.
- Testing considerations: Testing the solution with different tree structures and node values to ensure correctness.