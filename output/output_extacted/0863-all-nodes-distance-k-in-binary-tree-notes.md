## All Nodes Distance K in Binary Tree
**Problem Link:** https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description

**Problem Statement:**
- Input format: Given the root of a binary tree, a node, and a distance `k`, return a list of the values of all nodes that are distance `k` from the given node.
- Constraints: The number of nodes in the tree is in the range `[1, 5 * 10^4]`.
- Expected output format: A list of node values.
- Key requirements and edge cases to consider: Handling cases where `k` is 0, where the given node is not in the tree, or where `k` is larger than the height of the tree.
- Example test cases with explanations:
  - Given the root of a binary tree `root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]`, a node `target = 5`, and a distance `k = 2`, return `[7, 4, 1]`.
  - Given the root of a binary tree `root = [1]`, a node `target = 1`, and a distance `k = 3`, return `[]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Perform a depth-first search (DFS) or breadth-first search (BFS) from the target node to find all nodes at distance `k`.
- Step-by-step breakdown of the solution:
  1. Define a helper function to perform DFS or BFS from a given node.
  2. Use the helper function to find all nodes at distance `k` from the target node.
- Why this approach comes to mind first: It's a straightforward way to explore the tree and calculate distances.

```cpp
class Solution {
public:
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        vector<int> result;
        dfs(root, target, k, result);
        return result;
    }
    
    int dfs(TreeNode* node, TreeNode* target, int k, vector<int>& result) {
        if (!node) return -1;
        if (node == target) {
            dfsDown(node, k, result);
            return 0;
        }
        int left = dfs(node->left, target, k, result);
        if (left != -1) {
            if (left == k - 1) result.push_back(node->val);
            dfsDown(node->right, k - left - 1, result);
            return left + 1;
        }
        int right = dfs(node->right, target, k, result);
        if (right != -1) {
            if (right == k - 1) result.push_back(node->val);
            dfsDown(node->left, k - right - 1, result);
            return right + 1;
        }
        return -1;
    }
    
    void dfsDown(TreeNode* node, int k, vector<int>& result) {
        if (!node) return;
        if (k == 0) {
            result.push_back(node->val);
            return;
        }
        dfsDown(node->left, k - 1, result);
        dfsDown(node->right, k - 1, result);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$ where $N$ is the number of nodes in the tree, because we visit each node at most twice.
> - **Space Complexity:** $O(N)$ for the recursion stack and the result vector.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node, and the space complexity is linear because of the recursion stack and the result vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a similar approach to the brute force solution but optimize it by using a more efficient data structure to store the nodes and their distances.
- Detailed breakdown of the approach:
  1. Perform a DFS to find the target node and calculate the distance from the target node to all other nodes.
  2. Use the calculated distances to find the nodes at distance `k`.
- Proof of optimality: This solution has the same time complexity as the brute force solution but is more efficient in practice because it uses a more efficient data structure.

```cpp
class Solution {
public:
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        vector<int> result;
        unordered_map<TreeNode*, TreeNode*> parent;
        dfs(root, nullptr, parent);
        unordered_set<TreeNode*> visited;
        dfsDown(target, k, 0, result, visited);
        return result;
    }
    
    void dfs(TreeNode* node, TreeNode* par, unordered_map<TreeNode*, TreeNode*>& parent) {
        if (!node) return;
        parent[node] = par;
        dfs(node->left, node, parent);
        dfs(node->right, node, parent);
    }
    
    void dfsDown(TreeNode* node, int k, int dist, vector<int>& result, unordered_set<TreeNode*>& visited) {
        if (!node || visited.count(node)) return;
        visited.insert(node);
        if (dist == k) result.push_back(node->val);
        if (dist < k) {
            dfsDown(node->left, k, dist + 1, result, visited);
            dfsDown(node->right, k, dist + 1, result, visited);
            dfsDown(parent[node], k, dist + 1, result, visited);
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$ where $N$ is the number of nodes in the tree, because we visit each node at most twice.
> - **Space Complexity:** $O(N)$ for the recursion stack and the result vector.
> - **Optimality proof:** This solution is optimal because it has the same time complexity as the brute force solution but is more efficient in practice because it uses a more efficient data structure.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-first search (DFS), breadth-first search (BFS), and using a parent map to store the parent of each node.
- Problem-solving patterns identified: Using a recursive approach to solve the problem and using a parent map to store the parent of each node.
- Optimization techniques learned: Using a more efficient data structure to store the nodes and their distances.
- Similar problems to practice: Problems that involve finding nodes at a certain distance from a given node in a graph or tree.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where the target node is not in the tree, not handling the case where `k` is 0, and not handling the case where `k` is larger than the height of the tree.
- Edge cases to watch for: The case where the target node is not in the tree, the case where `k` is 0, and the case where `k` is larger than the height of the tree.
- Performance pitfalls: Using a naive approach that has a high time complexity, not using a more efficient data structure to store the nodes and their distances.
- Testing considerations: Testing the solution with different inputs, including edge cases, to ensure that it works correctly.