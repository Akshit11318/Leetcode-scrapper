## Cousins in Binary Tree II

**Problem Link:** https://leetcode.com/problems/cousins-in-binary-tree-ii/description

**Problem Statement:**
- Input: A binary tree and two nodes' values.
- Constraints: The tree is not empty, and the two nodes are distinct and exist in the tree.
- Expected Output: The values of all nodes that are cousins of the two input nodes.
- Key Requirements:
  - A node is a cousin of another if they have different parents but the same depth level.
- Edge Cases:
  - Nodes with the same parent are not cousins.
  - Nodes at different depths are not cousins.

**Example Test Cases:**
- Example 1:
  - Input: `root = [2,1,3,4]`, `x = 4`, `y = 3`
  - Output: `[1]`
  - Explanation: Node 4 and node 3 are cousins because they have different parents (node 2 is their parent's parent) and are at the same level.
- Example 2:
  - Input: `root = [5,4,6,1,2]`, `x = 1`, `y = 2`
  - Output: `[]`
  - Explanation: Node 1 and node 2 are not cousins because they have the same parent (node 4).

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves traversing the tree to find the parents and depths of the two given nodes.
- We can use a recursive or iterative approach to perform the traversal.
- Once we have the parents and depths, we can identify if the nodes are cousins by checking if they have different parents but the same depth.

```cpp
class Solution {
public:
    vector<int> cousinsInBinaryTree(TreeNode* root, int x, int y) {
        // Find the parents and depths of nodes x and y
        int parentX, parentY, depthX, depthY;
        findNode(root, x, &parentX, &depthX, 0);
        findNode(root, y, &parentY, &depthY, 0);
        
        // Check if nodes x and y are cousins
        if (parentX != parentY && depthX == depthY) {
            // Find all nodes at the same depth with different parents
            vector<int> cousins;
            findCousins(root, depthX, parentX, parentY, cousins);
            return cousins;
        } else {
            return {};
        }
    }
    
    void findNode(TreeNode* node, int target, int* parent, int* depth, int currentDepth) {
        if (!node) return;
        if (node->val == target) {
            *parent = node->val;
            *depth = currentDepth;
            return;
        }
        findNode(node->left, target, parent, depth, currentDepth + 1);
        findNode(node->right, target, parent, depth, currentDepth + 1);
    }
    
    void findCousins(TreeNode* node, int targetDepth, int parentX, int parentY, vector<int>& cousins) {
        if (!node) return;
        if (targetDepth == 1 && node->val != parentX && node->val != parentY) {
            cousins.push_back(node->val);
            return;
        }
        findCousins(node->left, targetDepth - 1, parentX, parentY, cousins);
        findCousins(node->right, targetDepth - 1, parentX, parentY, cousins);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, since we potentially visit each node once for each of the two input nodes and then once for finding cousins.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree, due to the recursive call stack.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node in the tree. The space complexity is dependent on the height of the tree due to the recursive calls.

---

### Optimal Approach (Required)

**Explanation:**
- A more optimal approach involves using a single pass through the tree to find the parents and depths of all nodes.
- We can use a hash map to store the parent and depth of each node as we traverse the tree.
- This allows us to find the parents and depths of the input nodes in constant time and then identify their cousins.

```cpp
class Solution {
public:
    vector<int> cousinsInBinaryTree(TreeNode* root, int x, int y) {
        unordered_map<int, pair<int, int>> nodeInfo;
        traverse(root, nodeInfo, 0);
        
        // Check if nodes x and y are cousins
        if (nodeInfo[x].first != nodeInfo[y].first && nodeInfo[x].second == nodeInfo[y].second) {
            vector<int> cousins;
            for (auto& node : nodeInfo) {
                if (node.second.second == nodeInfo[x].second && node.second.first != nodeInfo[x].first && node.first != x && node.first != y) {
                    cousins.push_back(node.first);
                }
            }
            return cousins;
        } else {
            return {};
        }
    }
    
    void traverse(TreeNode* node, unordered_map<int, pair<int, int>>& nodeInfo, int depth) {
        if (!node) return;
        nodeInfo[node->val] = {node->val == root->val ? -1 : (node == root->left ? root->val : root->right->val), depth};
        if (node->left) {
            nodeInfo[node->left->val] = {node->val, depth + 1};
        }
        if (node->right) {
            nodeInfo[node->right->val] = {node->val, depth + 1};
        }
        traverse(node->left, nodeInfo, depth + 1);
        traverse(node->right, nodeInfo, depth + 1);
    }
};
```

However, the optimal approach would be to store parent and depth of each node while doing a single level order traversal of the tree.

```cpp
class Solution {
public:
    vector<int> cousinsInBinaryTree(TreeNode* root, int x, int y) {
        unordered_map<int, pair<int, int>> nodeInfo;
        queue<pair<TreeNode*, int>> q;
        q.push({root, 0});
        while (!q.empty()) {
            auto node = q.front().first;
            int depth = q.front().second;
            q.pop();
            if (node->left) {
                nodeInfo[node->left->val] = {node->val, depth + 1};
                q.push({node->left, depth + 1});
            }
            if (node->right) {
                nodeInfo[node->right->val] = {node->val, depth + 1};
                q.push({node->right, depth + 1});
            }
        }
        
        // Check if nodes x and y are cousins
        if (nodeInfo[x].first != nodeInfo[y].first && nodeInfo[x].second == nodeInfo[y].second) {
            vector<int> cousins;
            for (auto& node : nodeInfo) {
                if (node.second.second == nodeInfo[x].second && node.second.first != nodeInfo[x].first && node.first != x && node.first != y) {
                    cousins.push_back(node.first);
                }
            }
            return cousins;
        } else {
            return {};
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, since we visit each node once.
> - **Space Complexity:** $O(n)$, for storing the parent and depth of each node.
> - **Optimality proof:** This is optimal because we only traverse the tree once and store necessary information about each node, allowing us to find cousins in constant time after the traversal.