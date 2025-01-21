## Step-by-Step Directions from a Binary Tree Node to Another

**Problem Link:** https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/description

**Problem Statement:**
- Input: The root of a binary tree and two node values, `startValue` and `targetValue`.
- Expected Output: The shortest path from `startValue` to `targetValue` in the binary tree, represented as a sequence of `U` (up), `L` (left), and `R` (right) directions.
- Key Requirements:
  - The tree is not guaranteed to be balanced.
  - All node values are unique.
- Edge Cases:
  - The `startValue` and `targetValue` may not exist in the tree.
  - The `startValue` and `targetValue` may be the same.
- Example Test Cases:
  - Example 1:
    - Input: `root = [5,6,7,2,3,null,9], startValue = 3, targetValue = 7`
    - Output: `["U","R","R"]`
  - Example 2:
    - Input: `root = [2,3], startValue = 2, targetValue = 3`
    - Output: `["R"]`

### Brute Force Approach

**Explanation:**
- Initial thought process: Perform a depth-first search (DFS) from the root to find both the `startValue` and `targetValue` nodes, then construct the path by backtracking.
- Step-by-Step Breakdown:
  1. Implement DFS to find the `startValue` node and store its path from the root.
  2. Implement DFS to find the `targetValue` node and store its path from the root.
  3. Find the lowest common ancestor (LCA) of the `startValue` and `targetValue` nodes by comparing their paths.
  4. Construct the path from `startValue` to `targetValue` by going up to the LCA and then down to `targetValue`.
- Why this approach comes to mind first: It directly addresses the problem statement by finding the nodes and constructing the path.

```cpp
class Solution {
public:
    vector<string> getDirections(TreeNode* root, int startValue, int targetValue) {
        // Base case
        if (!root) return {};

        // Find paths to startValue and targetValue
        vector<int> startPath, targetPath;
        findPath(root, startValue, startPath);
        findPath(root, targetValue, targetPath);

        // Find LCA and construct path
        vector<string> path;
        constructPath(startPath, targetPath, path);

        return path;
    }

    // Helper function to find path to a node
    bool findPath(TreeNode* node, int value, vector<int>& path) {
        if (!node) return false;
        path.push_back(node->val);
        if (node->val == value) return true;
        if (findPath(node->left, value, path) || findPath(node->right, value, path)) return true;
        path.pop_back();
        return false;
    }

    // Helper function to construct path from startValue to targetValue
    void constructPath(vector<int>& startPath, vector<int>& targetPath, vector<string>& path) {
        int i = 0, j = 0;
        while (i < startPath.size() && j < targetPath.size() && startPath[i] == targetPath[j]) {
            i++;
            j++;
        }
        // Go up to LCA
        for (int k = i; k < startPath.size(); k++) {
            path.push_back("U");
        }
        // Go down to targetValue
        for (int k = j - 1; k >= 0; k--) {
            if (targetPath[k] == targetPath[k + 1]->left->val) {
                path.push_back("L");
            } else {
                path.push_back("R");
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of nodes in the tree, because we visit each node at most twice (once for each DFS).
> - **Space Complexity:** $O(n)$ because in the worst case, the path from the root to a leaf node can contain $n$ nodes.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node. The space complexity is also linear due to the recursion stack and the storage of paths.

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of performing two separate DFS traversals to find the `startValue` and `targetValue` nodes, we can perform a single DFS traversal to find both nodes and construct the paths simultaneously.
- Detailed breakdown:
  1. Perform a single DFS traversal to find both the `startValue` and `targetValue` nodes.
  2. Construct the paths from the root to both nodes during the DFS traversal.
  3. Find the LCA of the two nodes by comparing their paths.
  4. Construct the path from `startValue` to `targetValue` by going up to the LCA and then down to `targetValue`.
- Why further optimization is impossible: This approach minimizes the number of node visits and path constructions, resulting in the optimal time and space complexity.

```cpp
class Solution {
public:
    vector<string> getDirections(TreeNode* root, int startValue, int targetValue) {
        // Perform DFS to find nodes and construct paths
        vector<int> startPath, targetPath;
        findNodesAndPaths(root, startValue, targetValue, startPath, targetPath);

        // Construct path from startValue to targetValue
        vector<string> path;
        constructPath(startPath, targetPath, path);

        return path;
    }

    // Helper function to find nodes and construct paths
    bool findNodesAndPaths(TreeNode* node, int startValue, int targetValue, vector<int>& startPath, vector<int>& targetPath) {
        if (!node) return false;
        if (node->val == startValue) {
            startPath.push_back(node->val);
            return true;
        }
        if (node->val == targetValue) {
            targetPath.push_back(node->val);
            return true;
        }
        if (findNodesAndPaths(node->left, startValue, targetValue, startPath, targetPath)) {
            if (startPath.size() > 0) startPath.push_back(node->val);
            if (targetPath.size() > 0) targetPath.push_back(node->val);
            return true;
        }
        if (findNodesAndPaths(node->right, startValue, targetValue, startPath, targetPath)) {
            if (startPath.size() > 0) startPath.push_back(node->val);
            if (targetPath.size() > 0) targetPath.push_back(node->val);
            return true;
        }
        return false;
    }

    // Helper function to construct path from startValue to targetValue
    void constructPath(vector<int>& startPath, vector<int>& targetPath, vector<string>& path) {
        int i = 0, j = 0;
        while (i < startPath.size() && j < targetPath.size() && startPath[i] == targetPath[j]) {
            i++;
            j++;
        }
        // Go up to LCA
        for (int k = i; k < startPath.size(); k++) {
            path.push_back("U");
        }
        // Go down to targetValue
        for (int k = j - 1; k >= 0; k--) {
            if (targetPath[k] == targetPath[k + 1]->left->val) {
                path.push_back("L");
            } else {
                path.push_back("R");
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of nodes in the tree, because we visit each node at most once.
> - **Space Complexity:** $O(n)$ because in the worst case, the path from the root to a leaf node can contain $n$ nodes.
> - **Optimality proof:** This approach minimizes the number of node visits and path constructions, resulting in the optimal time and space complexity.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, path construction, and LCA finding.
- Problem-solving patterns identified: using a single traversal to find multiple nodes and construct paths.
- Optimization techniques learned: minimizing node visits and path constructions.
- Similar problems to practice: finding the shortest path between two nodes in a graph or tree.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases, such as when the `startValue` or `targetValue` is not found in the tree.
- Edge cases to watch for: when the `startValue` and `targetValue` are the same, or when the tree is empty.
- Performance pitfalls: using multiple traversals to find nodes and construct paths, resulting in higher time complexity.
- Testing considerations: testing the implementation with different tree structures and node values to ensure correctness.