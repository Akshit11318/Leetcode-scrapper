## Height of Binary Tree After Subtree Removal Queries
**Problem Link:** https://leetcode.com/problems/height-of-binary-tree-after-subtree-queries/description

**Problem Statement:**
- Given a binary tree and a list of nodes to remove, find the height of the binary tree after removing the specified subtrees.
- Input format and constraints: The input tree is represented as a list of nodes where each node contains a unique value, and the list of nodes to remove is given as a list of node values.
- Expected output format: The output should be a list of heights of the binary tree after removing each specified subtree.
- Key requirements and edge cases to consider: The tree may be empty, and the list of nodes to remove may be empty or contain nodes not present in the tree.
- Example test cases with explanations: 
    - For an empty tree and an empty list of nodes, the output should be an empty list.
    - For a tree with a single node and a list containing that node, the output should be [0].

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over the list of nodes to remove and for each node, finding and removing the corresponding subtree from the original tree.
- Step-by-step breakdown of the solution:
    1. Create a copy of the original tree to avoid modifying it directly.
    2. For each node to remove, find its parent node in the copied tree.
    3. Remove the subtree rooted at the node to remove by updating the parent's child pointer.
    4. Calculate the height of the modified tree.
    5. Repeat steps 2-4 for each node in the list of nodes to remove.
- Why this approach comes to mind first: This approach is straightforward and involves directly implementing the problem statement.

```cpp
// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<int> treeQueriesAfterSubtreeRemoval(vector<vector<int>>& edges, vector<int>& queries) {
        // Create an adjacency list representation of the tree
        unordered_map<int, vector<int>> adjList;
        for (const auto& edge : edges) {
            adjList[edge[0]].push_back(edge[1]);
            adjList[edge[1]].push_back(edge[0]);
        }
        
        // Create the tree
        unordered_map<int, TreeNode*> tree;
        for (int i = 1; i <= edges.size() + 1; ++i) {
            tree[i] = new TreeNode(i);
        }
        for (const auto& edge : edges) {
            int u = edge[0], v = edge[1];
            if (tree[u]->left == nullptr) {
                tree[u]->left = tree[v];
            } else {
                tree[u]->right = tree[v];
            }
        }
        
        // Find the root of the tree (assuming it's the node with the most connections)
        int root = 1;
        for (const auto& pair : adjList) {
            if (pair.second.size() > adjList[root].size()) {
                root = pair.first;
            }
        }
        
        vector<int> results;
        for (int query : queries) {
            // Remove the subtree rooted at query
            unordered_set<int> toRemove;
            dfs(tree[query], toRemove);
            // Update the tree by removing the nodes
            for (int node : toRemove) {
                if (tree[node]->left != nullptr) {
                    tree[node]->left = nullptr;
                }
                if (tree[node]->right != nullptr) {
                    tree[node]->right = nullptr;
                }
            }
            // Calculate the height of the modified tree
            int height = getHeight(tree[root]);
            results.push_back(height);
        }
        return results;
    }
    
    void dfs(TreeNode* node, unordered_set<int>& toRemove) {
        if (node == nullptr) return;
        toRemove.insert(node->val);
        dfs(node->left, toRemove);
        dfs(node->right, toRemove);
    }
    
    int getHeight(TreeNode* node) {
        if (node == nullptr) return 0;
        return 1 + max(getHeight(node->left), getHeight(node->right));
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of nodes in the tree and $m$ is the number of queries. This is because for each query, we potentially visit all nodes in the tree.
> - **Space Complexity:** $O(n)$, as we need to store the tree and the nodes to remove.
> - **Why these complexities occur:** The brute force approach involves iterating over the list of nodes to remove and for each node, finding and removing the corresponding subtree from the original tree, which results in these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of removing the subtree for each query, we can use a depth-first search (DFS) to calculate the height of the subtree rooted at each node and store the results. Then, for each query, we can simply look up the height of the subtree rooted at the query node and subtract it from the total height of the tree.
- Detailed breakdown of the approach:
    1. Perform a DFS traversal of the tree to calculate the height of the subtree rooted at each node.
    2. Store the heights in a data structure for quick lookup.
    3. For each query, look up the height of the subtree rooted at the query node and subtract it from the total height of the tree.
- Why further optimization is impossible: This approach has a time complexity of $O(n + m)$, which is optimal because we must visit each node at least once to calculate the heights and process the queries.

```cpp
class Solution {
public:
    vector<int> treeQueriesAfterSubtreeRemoval(vector<vector<int>>& edges, vector<int>& queries) {
        // Create an adjacency list representation of the tree
        unordered_map<int, vector<int>> adjList;
        for (const auto& edge : edges) {
            adjList[edge[0]].push_back(edge[1]);
            adjList[edge[1]].push_back(edge[0]);
        }
        
        // Create the tree
        unordered_map<int, TreeNode*> tree;
        for (int i = 1; i <= edges.size() + 1; ++i) {
            tree[i] = new TreeNode(i);
        }
        for (const auto& edge : edges) {
            int u = edge[0], v = edge[1];
            if (tree[u]->left == nullptr) {
                tree[u]->left = tree[v];
            } else {
                tree[u]->right = tree[v];
            }
        }
        
        // Find the root of the tree (assuming it's the node with the most connections)
        int root = 1;
        for (const auto& pair : adjList) {
            if (pair.second.size() > adjList[root].size()) {
                root = pair.first;
            }
        }
        
        // Calculate the height of the subtree rooted at each node
        unordered_map<int, int> heights;
        dfs(tree[root], heights);
        
        // Calculate the height of the tree after removing each subtree
        vector<int> results;
        for (int query : queries) {
            int height = heights[root] - heights[query];
            results.push_back(height);
        }
        return results;
    }
    
    void dfs(TreeNode* node, unordered_map<int, int>& heights) {
        if (node == nullptr) return;
        heights[node->val] = 1 + max(getHeight(node->left), getHeight(node->right));
        dfs(node->left, heights);
        dfs(node->right, heights);
    }
    
    int getHeight(TreeNode* node) {
        if (node == nullptr) return 0;
        return heights[node->val];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of nodes in the tree and $m$ is the number of queries.
> - **Space Complexity:** $O(n)$, as we need to store the heights of the subtrees rooted at each node.
> - **Optimality proof:** This approach is optimal because we must visit each node at least once to calculate the heights and process the queries.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, tree traversal, and dynamic programming.
- Problem-solving patterns identified: Using a data structure to store intermediate results for quick lookup.
- Optimization techniques learned: Avoiding redundant calculations by storing intermediate results.
- Similar problems to practice: Other tree-related problems, such as finding the lowest common ancestor or calculating the diameter of a tree.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty tree or an empty list of queries.
- Edge cases to watch for: The tree may be empty, and the list of queries may be empty or contain nodes not present in the tree.
- Performance pitfalls: Using a brute force approach that results in high time complexity.
- Testing considerations: Test the solution with different inputs, including edge cases, to ensure correctness and performance.