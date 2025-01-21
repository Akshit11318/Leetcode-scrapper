## Encode N-ary Tree to Binary Tree

**Problem Link:** https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/description

**Problem Statement:**
- Input: An `n-ary` tree with a given root node, where each node has a unique value and a list of children.
- Output: A binary tree representation of the input `n-ary` tree, where each node contains a value and pointers to its left and right children.
- Key requirements:
  - The binary tree should preserve the structure of the `n-ary` tree.
  - Each node in the binary tree should have a unique value.
- Edge cases to consider:
  - An empty `n-ary` tree (i.e., a null root node).
  - An `n-ary` tree with a single node.
- Example test cases:
  - An `n-ary` tree with multiple levels and nodes.
  - An `n-ary` tree with a large number of children per node.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Create a binary tree node for each `n-ary` tree node and manually connect the children.
- Step-by-step breakdown:
  1. Create a binary tree node class with a value and pointers to its left and right children.
  2. Iterate through the `n-ary` tree nodes and create corresponding binary tree nodes.
  3. Manually connect the children of each binary tree node.
- Why this approach comes to mind first: It is a straightforward, intuitive approach that mirrors the structure of the `n-ary` tree.

```cpp
// Define the binary tree node class
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

// Define the n-ary tree node class
struct Node {
    int val;
    vector<Node*> children;
    Node(int _val) {
        val = _val;
    }
};

class Solution {
public:
    TreeNode* encode(Node* root) {
        if (!root) return nullptr;
        TreeNode* binaryRoot = new TreeNode(root->val);
        if (!root->children.empty()) {
            binaryRoot->left = encode(root->children[0]);
            TreeNode* sibling = binaryRoot->left;
            for (int i = 1; i < root->children.size(); i++) {
                sibling->right = encode(root->children[i]);
                sibling = sibling->right;
            }
        }
        return binaryRoot;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the `n-ary` tree. We visit each node once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the `n-ary` tree. We create a binary tree node for each `n-ary` tree node.
> - **Why these complexities occur:** We iterate through the `n-ary` tree nodes and create corresponding binary tree nodes, resulting in linear time and space complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The brute force approach is already optimal, as we must visit each node in the `n-ary` tree to create the binary tree representation.
- Detailed breakdown: The provided brute force approach is already efficient and optimal.
- Proof of optimality: We cannot do better than linear time complexity, as we must visit each node at least once to create the binary tree representation.

```cpp
// Same code as the brute force approach
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the `n-ary` tree. We visit each node once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the `n-ary` tree. We create a binary tree node for each `n-ary` tree node.
> - **Optimality proof:** We cannot do better than linear time complexity, as we must visit each node at least once to create the binary tree representation.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Tree traversal, node creation, and connection.
- Problem-solving patterns identified: Iteration through tree nodes, creation of corresponding binary tree nodes, and manual connection of children.
- Optimization techniques learned: None, as the brute force approach is already optimal.

**Mistakes to Avoid:**
- Common implementation errors: Null pointer dereferences, incorrect child connections.
- Edge cases to watch for: Empty `n-ary` tree, single-node `n-ary` tree.
- Performance pitfalls: Excessive memory allocation, slow iteration through tree nodes.
- Testing considerations: Verify correctness for various `n-ary` tree structures, including empty and single-node trees.