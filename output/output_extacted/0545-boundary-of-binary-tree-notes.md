## Boundary of Binary Tree

**Problem Link:** [https://leetcode.com/problems/boundary-of-binary-tree/description](https://leetcode.com/problems/boundary-of-binary-tree/description)

**Problem Statement:**
- Input format and constraints: The input is a binary tree's root node, and the constraints include the tree's structure and node values.
- Expected output format: The output is a list of node values representing the boundary of the binary tree, including the left boundary, leaves, and right boundary in that order.
- Key requirements and edge cases to consider: The boundary includes all nodes on the left boundary, all leaf nodes, and all nodes on the right boundary. Edge cases include an empty tree, a tree with a single node, and trees with varying numbers of nodes on the left and right boundaries.
- Example test cases with explanations: For example, given the binary tree with the following structure:
        ____1_____
       /          \
      2            3
     / \          / 
    4   5        6   
       / \      / \
      7   8    9  10 
the boundary of the binary tree is [1,2,4,7,8,9,10,6,3].

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves traversing the binary tree to identify nodes on the left boundary, leaves, and right boundary.
- Step-by-step breakdown of the solution:
  1. Perform a depth-first search (DFS) traversal to identify all nodes in the tree.
  2. For each node, check if it's on the left boundary, a leaf node, or on the right boundary.
  3. If a node is on the left boundary, add it to the boundary list.
  4. If a node is a leaf node, add it to the boundary list.
  5. If a node is on the right boundary, add it to the boundary list.
- Why this approach comes to mind first: This approach is straightforward and involves checking each node's position in the tree.

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> boundaryOfBinaryTree(TreeNode* root) {
        vector<int> boundary;
        if (!root) return boundary;
        
        // Add root node to boundary
        boundary.push_back(root->val);
        
        // Add left boundary nodes
        addLeftBoundary(root->left, boundary);
        
        // Add leaf nodes
        addLeafNodes(root, boundary);
        
        // Add right boundary nodes
        addRightBoundary(root->right, boundary);
        
        return boundary;
    }
    
    void addLeftBoundary(TreeNode* node, vector<int>& boundary) {
        if (!node || (!node->left && !node->right)) return;
        boundary.push_back(node->val);
        if (node->left) addLeftBoundary(node->left, boundary);
        else addLeftBoundary(node->right, boundary);
    }
    
    void addLeafNodes(TreeNode* node, vector<int>& boundary) {
        if (!node) return;
        if (!node->left && !node->right) boundary.push_back(node->val);
        addLeafNodes(node->left, boundary);
        addLeafNodes(node->right, boundary);
    }
    
    void addRightBoundary(TreeNode* node, vector<int>& boundary) {
        if (!node || (!node->left && !node->right)) return;
        if (node->right) addRightBoundary(node->right, boundary);
        else addRightBoundary(node->left, boundary);
        boundary.push_back(node->val);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the binary tree, because we visit each node once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the binary tree, because in the worst case, we need to store all nodes in the boundary list.
> - **Why these complexities occur:** The time complexity is $O(n)$ because we perform a DFS traversal of the tree, visiting each node once. The space complexity is $O(n)$ because we need to store the boundary nodes in a list.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a recursive approach to identify the boundary nodes.
- Detailed breakdown of the approach:
  1. Define a recursive function to add left boundary nodes.
  2. Define a recursive function to add leaf nodes.
  3. Define a recursive function to add right boundary nodes.
  4. Use these functions to populate the boundary list.
- Proof of optimality: This approach is optimal because it visits each node only once, resulting in a time complexity of $O(n)$.
- Why further optimization is impossible: Further optimization is impossible because we must visit each node at least once to determine its position in the boundary.

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> boundaryOfBinaryTree(TreeNode* root) {
        vector<int> boundary;
        if (!root) return boundary;
        
        // Add root node to boundary
        boundary.push_back(root->val);
        
        // Add left boundary nodes
        addLeftBoundary(root->left, boundary);
        
        // Add leaf nodes
        addLeafNodes(root->left, boundary);
        addLeafNodes(root->right, boundary);
        
        // Add right boundary nodes
        addRightBoundary(root->right, boundary);
        
        return boundary;
    }
    
    void addLeftBoundary(TreeNode* node, vector<int>& boundary) {
        if (!node || (!node->left && !node->right)) return;
        boundary.push_back(node->val);
        if (node->left) addLeftBoundary(node->left, boundary);
        else addLeftBoundary(node->right, boundary);
    }
    
    void addLeafNodes(TreeNode* node, vector<int>& boundary) {
        if (!node) return;
        if (!node->left && !node->right) boundary.push_back(node->val);
        addLeafNodes(node->left, boundary);
        addLeafNodes(node->right, boundary);
    }
    
    void addRightBoundary(TreeNode* node, vector<int>& boundary) {
        if (!node || (!node->left && !node->right)) return;
        if (node->right) addRightBoundary(node->right, boundary);
        else addRightBoundary(node->left, boundary);
        boundary.push_back(node->val);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the binary tree, because we visit each node once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the binary tree, because in the worst case, we need to store all nodes in the boundary list.
> - **Optimality proof:** The time complexity is $O(n)$ because we perform a DFS traversal of the tree, visiting each node once. The space complexity is $O(n)$ because we need to store the boundary nodes in a list.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of DFS traversal and recursive functions to solve a tree-related problem.
- Problem-solving patterns identified: The problem requires identifying the boundary nodes of a binary tree, which involves checking each node's position in the tree.
- Optimization techniques learned: The problem requires optimizing the solution to achieve a time complexity of $O(n)$.
- Similar problems to practice: Similar problems include finding the minimum depth of a binary tree, finding the maximum depth of a binary tree, and finding the lowest common ancestor of two nodes in a binary tree.

**Mistakes to Avoid:**
- Common implementation errors: A common error is not checking for null nodes before accessing their children.
- Edge cases to watch for: Edge cases include an empty tree, a tree with a single node, and trees with varying numbers of nodes on the left and right boundaries.
- Performance pitfalls: A performance pitfall is not optimizing the solution to achieve a time complexity of $O(n)$.
- Testing considerations: Testing considerations include testing the solution with different types of input, such as an empty tree, a tree with a single node, and trees with varying numbers of nodes on the left and right boundaries.