## Create Binary Tree From Descriptions

**Problem Link:** https://leetcode.com/problems/create-binary-tree-from-descriptions/description

**Problem Statement:**
- Input format and constraints: You are given a list of descriptions of the nodes in the binary tree, where each description is represented as a list of three elements: `[parent, child, is_left]`. The `parent` is the parent node's value, the `child` is the child node's value, and `is_left` is a boolean indicating whether the child node is the left child of the parent node.
- Expected output format: You need to return the root node of the constructed binary tree.
- Key requirements and edge cases to consider: The input list may contain duplicate descriptions for the same node, and the binary tree may not be a complete binary tree.
- Example test cases with explanations:
  - Example 1: Input: `[[20,15,1],[20,18,0],[35,33,1],[33,30,0]]`, Output: The root node of the constructed binary tree.
  - Example 2: Input: `[[0,5,1],[0,3,0],[5,6,1],[3,4,0]]`, Output: The root node of the constructed binary tree.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Create a dictionary to store the nodes of the binary tree, where each key is the node's value and the value is the node object. Iterate over the descriptions to construct the binary tree.
- Step-by-step breakdown of the solution:
  1. Create a dictionary to store the nodes of the binary tree.
  2. Iterate over the descriptions to construct the binary tree.
  3. For each description, create the parent node and the child node if they do not exist.
  4. Add the child node to the parent node based on the `is_left` value.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it may not be the most efficient.

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
    TreeNode* createBinaryTree(vector<vector<int>>& descriptions) {
        unordered_map<int, TreeNode*> nodes;
        for (auto& desc : descriptions) {
            int parent = desc[0];
            int child = desc[1];
            bool isLeft = desc[2];
            if (nodes.find(parent) == nodes.end()) {
                nodes[parent] = new TreeNode(parent);
            }
            if (nodes.find(child) == nodes.end()) {
                nodes[child] = new TreeNode(child);
            }
            if (isLeft) {
                nodes[parent]->left = nodes[child];
            } else {
                nodes[parent]->right = nodes[child];
            }
        }
        // Find the root node
        unordered_set<int> children;
        for (auto& desc : descriptions) {
            children.insert(desc[1]);
        }
        int rootVal;
        for (auto& node : nodes) {
            if (children.find(node.first) == children.end()) {
                rootVal = node.first;
                break;
            }
        }
        return nodes[rootVal];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of descriptions. This is because we iterate over the descriptions twice: once to construct the binary tree and once to find the root node.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the binary tree. This is because we store each node in the `nodes` dictionary.
> - **Why these complexities occur:** The time complexity occurs because we iterate over the descriptions twice, and the space complexity occurs because we store each node in the `nodes` dictionary.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can find the root node while constructing the binary tree by keeping track of the nodes that have been used as children.
- Detailed breakdown of the approach:
  1. Create a dictionary to store the nodes of the binary tree.
  2. Create a set to store the nodes that have been used as children.
  3. Iterate over the descriptions to construct the binary tree.
  4. For each description, create the parent node and the child node if they do not exist.
  5. Add the child node to the parent node based on the `is_left` value.
  6. Add the child node to the set of children.
- Proof of optimality: This approach is optimal because we only iterate over the descriptions once, and we use a set to keep track of the children, which allows us to find the root node in constant time.

```cpp
class Solution {
public:
    TreeNode* createBinaryTree(vector<vector<int>>& descriptions) {
        unordered_map<int, TreeNode*> nodes;
        unordered_set<int> children;
        for (auto& desc : descriptions) {
            int parent = desc[0];
            int child = desc[1];
            bool isLeft = desc[2];
            if (nodes.find(parent) == nodes.end()) {
                nodes[parent] = new TreeNode(parent);
            }
            if (nodes.find(child) == nodes.end()) {
                nodes[child] = new TreeNode(child);
            }
            if (isLeft) {
                nodes[parent]->left = nodes[child];
            } else {
                nodes[parent]->right = nodes[child];
            }
            children.insert(child);
        }
        // Find the root node
        for (auto& node : nodes) {
            if (children.find(node.first) == children.end()) {
                return node.second;
            }
        }
        return nullptr;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of descriptions. This is because we iterate over the descriptions once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the binary tree. This is because we store each node in the `nodes` dictionary and each child in the `children` set.
> - **Optimality proof:** This approach is optimal because we only iterate over the descriptions once, and we use a set to keep track of the children, which allows us to find the root node in constant time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hashing, tree construction, and set operations.
- Problem-solving patterns identified: Finding the root node of a binary tree by keeping track of the children.
- Optimization techniques learned: Using a set to keep track of the children to find the root node in constant time.
- Similar problems to practice: Constructing a binary tree from a list of node values and edges.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if a node exists before creating it, not handling the case where a node has no children.
- Edge cases to watch for: An empty list of descriptions, a list of descriptions with duplicate nodes.
- Performance pitfalls: Using a slow data structure to store the nodes, such as a linked list.
- Testing considerations: Testing the function with different inputs, including edge cases and large inputs.