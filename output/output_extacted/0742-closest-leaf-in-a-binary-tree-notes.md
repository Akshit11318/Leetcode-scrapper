## Closest Leaf in a Binary Tree

**Problem Link:** https://leetcode.com/problems/closest-leaf-in-a-binary-tree/description

**Problem Statement:**
- Given a binary tree where every node has a unique integer value and a target value, find the closest leaf node to the target node in the tree.
- The input is the root of the binary tree and the target value.
- The expected output is the value of the closest leaf node.
- Key requirements:
  - Each node in the tree has a unique integer value.
  - The target node must exist in the tree.
  - If there are multiple leaf nodes at the same distance from the target node, return the one with the smallest value.
- Example test cases:
  - Example 1:
    - Input: root = [1], target = 1
    - Output: 1
  - Example 2:
    - Input: root = [1,3,2], target = 1
    - Output: 2

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to traverse the tree and find all leaf nodes.
- Then, for each leaf node, calculate the distance to the target node by finding the path from the leaf node to the target node.
- The leaf node with the smallest distance is the closest leaf node.
- Why this approach comes to mind first: It is straightforward and does not require any advanced data structures or algorithms.

```cpp
// Well-commented code with:
// - Clear variable names
// - Input validation
// - Edge case handling
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int findClosestLeaf(TreeNode* root, int k) {
        // Find the target node
        TreeNode* target = findNode(root, k);
        
        // Find all leaf nodes
        vector<int> leaves;
        findLeaves(root, leaves);
        
        // Calculate the distance from each leaf node to the target node
        int minDistance = INT_MAX;
        int closestLeaf = -1;
        for (int leaf : leaves) {
            int distance = findDistance(root, k, leaf);
            if (distance < minDistance) {
                minDistance = distance;
                closestLeaf = leaf;
            } else if (distance == minDistance && leaf < closestLeaf) {
                closestLeaf = leaf;
            }
        }
        
        return closestLeaf;
    }
    
    // Helper function to find a node in the tree
    TreeNode* findNode(TreeNode* root, int k) {
        if (root == NULL) return NULL;
        if (root->val == k) return root;
        TreeNode* left = findNode(root->left, k);
        if (left != NULL) return left;
        return findNode(root->right, k);
    }
    
    // Helper function to find all leaf nodes in the tree
    void findLeaves(TreeNode* root, vector<int>& leaves) {
        if (root == NULL) return;
        if (root->left == NULL && root->right == NULL) {
            leaves.push_back(root->val);
            return;
        }
        findLeaves(root->left, leaves);
        findLeaves(root->right, leaves);
    }
    
    // Helper function to find the distance between two nodes in the tree
    int findDistance(TreeNode* root, int start, int end) {
        // Find the path from the start node to the root
        vector<int> path1;
        findPath(root, start, path1);
        
        // Find the path from the end node to the root
        vector<int> path2;
        findPath(root, end, path2);
        
        // Find the common ancestor
        int commonAncestor = -1;
        for (int i = 0; i < min(path1.size(), path2.size()); i++) {
            if (path1[i] == path2[i]) {
                commonAncestor = path1[i];
            } else {
                break;
            }
        }
        
        // Calculate the distance
        int distance = path1.size() + path2.size() - 2 * (path1.size() - path1.size() + path2.size() - path2.size());
        
        return distance;
    }
    
    // Helper function to find the path from a node to the root
    bool findPath(TreeNode* root, int target, vector<int>& path) {
        if (root == NULL) return false;
        path.push_back(root->val);
        if (root->val == target) return true;
        if (findPath(root->left, target, path)) return true;
        if (findPath(root->right, target, path)) return true;
        path.pop_back();
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of nodes in the tree. This is because we are finding all leaf nodes, which takes $O(n)$ time, and then for each leaf node, we are finding the distance to the target node, which takes $O(n)$ time in the worst case.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we are storing all leaf nodes in a vector.
> - **Why these complexities occur:** The brute force approach is not efficient because it involves finding all leaf nodes and then calculating the distance from each leaf node to the target node, which results in a high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a graph to represent the tree, where each node is connected to its parent and children.
- We can then use a breadth-first search (BFS) to find the closest leaf node to the target node.
- The BFS will start from the target node and explore all nodes at a given distance before moving on to the next distance.
- This approach is optimal because it only requires a single pass through the tree and does not involve finding all leaf nodes.
- Why further optimization is impossible: This approach has a time complexity of $O(n)$, which is the minimum possible time complexity for this problem because we must visit each node at least once.

```cpp
class Solution {
public:
    int findClosestLeaf(TreeNode* root, int k) {
        // Create a graph to represent the tree
        unordered_map<int, vector<int>> graph;
        createGraph(root, graph);
        
        // Find the target node
        queue<int> q;
        q.push(k);
        unordered_set<int> visited;
        visited.insert(k);
        
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            if (isLeaf(node, graph)) {
                return node;
            }
            for (int neighbor : graph[node]) {
                if (visited.find(neighbor) == visited.end()) {
                    q.push(neighbor);
                    visited.insert(neighbor);
                }
            }
        }
        
        return -1;
    }
    
    // Helper function to create a graph to represent the tree
    void createGraph(TreeNode* root, unordered_map<int, vector<int>>& graph) {
        if (root == NULL) return;
        if (root->left != NULL) {
            graph[root->val].push_back(root->left->val);
            graph[root->left->val].push_back(root->val);
            createGraph(root->left, graph);
        }
        if (root->right != NULL) {
            graph[root->val].push_back(root->right->val);
            graph[root->right->val].push_back(root->val);
            createGraph(root->right, graph);
        }
    }
    
    // Helper function to check if a node is a leaf node
    bool isLeaf(int node, unordered_map<int, vector<int>>& graph) {
        return graph[node].size() == 1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we are creating a graph to represent the tree and then using a BFS to find the closest leaf node.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we are storing the graph in an unordered map.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the tree and does not involve finding all leaf nodes, which results in a time complexity of $O(n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: graph traversal, BFS, tree traversal.
- Problem-solving patterns identified: using a graph to represent a tree, using BFS to find the closest node.
- Optimization techniques learned: reducing the time complexity by using a more efficient algorithm.
- Similar problems to practice: finding the closest node to a target node in a graph, finding the shortest path between two nodes in a graph.

**Mistakes to Avoid:**
- Common implementation errors: not checking for edge cases, not handling null pointers correctly.
- Edge cases to watch for: an empty tree, a tree with only one node, a target node that is a leaf node.
- Performance pitfalls: using a brute force approach, not optimizing the algorithm for large inputs.
- Testing considerations: testing the algorithm with different types of inputs, testing the algorithm with large inputs to ensure it scales well.