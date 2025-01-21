## Amount of Time for Binary Tree to be Infected
**Problem Link:** https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/description

**Problem Statement:**
- Input format: A binary tree represented as a `TreeNode` object and a time limit `start` and `target` value.
- Constraints: Each node in the binary tree has a unique value, and the tree does not contain more than $10^4$ nodes.
- Expected output format: The minimum time required to infect all nodes in the binary tree.
- Key requirements and edge cases to consider: The tree may be empty, and the `start` node may not exist in the tree.

**Example Test Cases:**
- Example 1:
  - Input: `root = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]`, `start = 2`, `target = 7`
  - Output: `4`
- Example 2:
  - Input: `root = [1]`, `start = 1`, `target = 1`
  - Output: `0`

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to perform a depth-first search (DFS) or breadth-first search (BFS) from the `start` node to infect all nodes in the binary tree.
- We will keep track of the time required to infect each node and update the maximum time required.

```cpp
// Brute Force Approach
class Solution {
public:
    int amountOfTime(TreeNode* root, int start, int target) {
        int result = 0;
        if (root == nullptr) return result;
        
        queue<pair<TreeNode*, int>> q;
        q.push({root, 0});
        
        while (!q.empty()) {
            TreeNode* node = q.front().first;
            int time = q.front().second;
            q.pop();
            
            if (node->val == start) {
                // Infect all nodes from the start node
                infectNodes(node, time + 1, result);
            }
            
            if (node->left) q.push({node->left, time + 1});
            if (node->right) q.push({node->right, time + 1});
        }
        
        return result;
    }
    
    void infectNodes(TreeNode* node, int time, int& result) {
        if (node == nullptr) return;
        
        if (node->val == target) {
            result = time;
        }
        
        infectNodes(node->left, time + 1, result);
        infectNodes(node->right, time + 1, result);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the binary tree, because we perform a DFS from the `start` node to infect all nodes.
> - **Space Complexity:** $O(n)$, because we use a queue to store nodes and their corresponding times.
> - **Why these complexities occur:** The time complexity occurs because we visit each node in the binary tree, and the space complexity occurs because we store nodes in the queue.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a graph to represent the binary tree and perform a BFS from the `start` node to infect all nodes.
- We will keep track of the time required to infect each node and update the maximum time required.

```cpp
// Optimal Approach
class Solution {
public:
    int amountOfTime(TreeNode* root, int start, int target) {
        if (root == nullptr) return 0;
        
        // Create a graph to represent the binary tree
        unordered_map<int, vector<int>> graph;
        createGraph(root, graph);
        
        // Perform a BFS from the start node to infect all nodes
        queue<pair<int, int>> q;
        q.push({start, 0});
        unordered_set<int> visited;
        visited.insert(start);
        int result = 0;
        
        while (!q.empty()) {
            int node = q.front().first;
            int time = q.front().second;
            q.pop();
            
            if (node == target) {
                result = time;
                break;
            }
            
            for (int neighbor : graph[node]) {
                if (visited.find(neighbor) == visited.end()) {
                    q.push({neighbor, time + 1});
                    visited.insert(neighbor);
                }
            }
        }
        
        return result;
    }
    
    void createGraph(TreeNode* node, unordered_map<int, vector<int>>& graph) {
        if (node == nullptr) return;
        
        if (node->left) {
            graph[node->val].push_back(node->left->val);
            graph[node->left->val].push_back(node->val);
            createGraph(node->left, graph);
        }
        
        if (node->right) {
            graph[node->val].push_back(node->right->val);
            graph[node->right->val].push_back(node->val);
            createGraph(node->right, graph);
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the binary tree, because we create a graph and perform a BFS from the `start` node.
> - **Space Complexity:** $O(n)$, because we use a graph and a queue to store nodes.
> - **Optimality proof:** This approach is optimal because we only visit each node once and use a BFS to find the shortest path from the `start` node to the `target` node.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is using a graph to represent a binary tree and performing a BFS to find the shortest path.
- The problem-solving pattern identified is using a graph to model a problem and applying graph algorithms to solve it.
- The optimization technique learned is using a BFS to find the shortest path in a graph.

**Mistakes to Avoid:**
- A common implementation error is not handling the case where the `start` node is not in the binary tree.
- An edge case to watch for is when the `target` node is not in the binary tree.
- A performance pitfall is using a DFS instead of a BFS to find the shortest path.
- A testing consideration is to test the solution with different inputs and edge cases.