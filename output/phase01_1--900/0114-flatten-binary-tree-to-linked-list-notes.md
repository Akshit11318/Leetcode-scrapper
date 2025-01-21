## Flatten Binary Tree to Linked List

**Problem Link:** https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description

**Problem Statement:**
- Input: The root of a binary tree.
- Output: The root of the flattened binary tree.
- Key requirements:
  - The binary tree should be flattened in-place, meaning no extra space should be used.
  - The nodes should be connected as a linked list in the order of a pre-order traversal (root, left, right).
- Example test cases:
  - Input: `[1,2,5,3,4,null,6]`
    - Output: `[1,null,2,null,3,null,4,null,5,null,6]`
  - Input: `[]`
    - Output: `[]`
  - Input: `[0]`
    - Output: `[0]`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves performing a pre-order traversal of the binary tree and storing the nodes in a list.
- Then, we can iterate over the list and connect the nodes in a linked list fashion.
- This approach comes to mind first because it directly addresses the problem statement by traversing the tree in the desired order and then rearranging the nodes.

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
    void flatten(TreeNode* root) {
        if (!root) return;
        
        vector<TreeNode*> nodes;
        preOrderTraversal(root, nodes);
        
        for (int i = 0; i < nodes.size(); i++) {
            nodes[i]->left = nullptr;
            if (i < nodes.size() - 1) {
                nodes[i]->right = nodes[i + 1];
            } else {
                nodes[i]->right = nullptr;
            }
        }
    }
    
    void preOrderTraversal(TreeNode* node, vector<TreeNode*>& nodes) {
        if (!node) return;
        nodes.push_back(node);
        preOrderTraversal(node->left, nodes);
        preOrderTraversal(node->right, nodes);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of nodes in the binary tree. This is because we visit each node once during the pre-order traversal and once during the list iteration.
> - **Space Complexity:** $O(n)$ because in the worst case, we might need to store all nodes in the list.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node. The space complexity is also linear because we store all nodes in the list.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to perform the flattening in-place during the pre-order traversal itself, rather than storing all nodes and then rearranging them.
- This approach avoids the need for extra space to store the nodes, thus reducing the space complexity.
- We can achieve this by maintaining a pointer to the previous node in the traversal and updating the `right` child of the previous node to the current node, effectively creating the linked list structure.

```cpp
class Solution {
public:
    void flatten(TreeNode* root) {
        if (!root) return;
        
        TreeNode* prev = nullptr;
        preOrderTraversal(root, prev);
    }
    
    void preOrderTraversal(TreeNode* node, TreeNode*& prev) {
        if (!node) return;
        
        if (prev) {
            prev->left = nullptr;
            prev->right = node;
        }
        
        prev = node;
        TreeNode* right = node->right;
        preOrderTraversal(node->left, prev);
        preOrderTraversal(right, prev);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of nodes in the binary tree. Each node is visited once during the traversal.
> - **Space Complexity:** $O(h)$ where $h$ is the height of the binary tree. This is due to the recursive call stack.
> - **Optimality proof:** This solution is optimal because it performs the flattening in a single pass through the tree, minimizing both time and space complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated include pre-order traversal and in-place modification of a binary tree.
- Problem-solving patterns identified include the use of recursive functions to traverse tree structures and the optimization of space complexity by avoiding unnecessary storage.
- Optimization techniques learned include minimizing extra space usage and performing operations in a single pass when possible.

**Mistakes to Avoid:**
- Common implementation errors include incorrect handling of edge cases (e.g., empty trees or trees with a single node) and improper management of recursive function calls.
- Performance pitfalls include using excessive extra space or performing unnecessary operations, leading to increased time or space complexity.
- Testing considerations should include verifying the correctness of the solution for various input scenarios, including edge cases and large inputs.