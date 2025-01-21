## Binary Tree Preorder Traversal

**Problem Link:** https://leetcode.com/problems/binary-tree-preorder-traversal/description

**Problem Statement:**
- Input format and constraints: The input is the root of a binary tree where each node has a unique value. The tree can have any number of nodes, and the values are integers. The task is to return the preorder traversal of the binary tree.
- Expected output format: The output should be a vector of integers representing the preorder traversal of the binary tree.
- Key requirements and edge cases to consider: The solution should handle empty trees (where the root is nullptr), trees with a single node, and trees with multiple levels.
- Example test cases with explanations:
    - Example 1: Input: root = [1,null,2,3], Output: [1,2,3]
    - Example 2: Input: root = [], Output: []
    - Example 3: Input: root = [1], Output: [1]

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves recursively visiting each node in the binary tree in a preorder manner (root, left, right) and adding the node's value to the result vector.
- Step-by-step breakdown of the solution:
    1. Start with the root node.
    2. If the node is not nullptr, add its value to the result vector.
    3. Recursively call the function on the left child and then the right child.
- Why this approach comes to mind first: This approach is straightforward because it directly follows the definition of preorder traversal.

```cpp
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> result;
        preorderHelper(root, result);
        return result;
    }
    
    void preorderHelper(TreeNode* node, vector<int>& result) {
        if (node == nullptr) return;
        result.push_back(node->val);
        preorderHelper(node->left, result);
        preorderHelper(node->right, result);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree, because each node is visited once.
> - **Space Complexity:** $O(N)$, because in the worst case (a skewed tree), the recursion stack can go as high as $N$, and the result vector also stores $N$ elements.
> - **Why these complexities occur:** These complexities occur because the algorithm visits each node once and uses recursive calls that can go up to $N$ levels deep in the worst case.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution uses an iterative approach with a stack to simulate the recursion stack. This approach avoids the overhead of recursive function calls.
- Detailed breakdown of the approach:
    1. Initialize a stack with the root node.
    2. While the stack is not empty, pop a node from the stack, add its value to the result vector, and push its right child and then its left child onto the stack (in that order so they are processed in the correct order).
- Proof of optimality: This solution is optimal because it still visits each node once but uses a stack to manage the nodes to visit, avoiding the overhead of recursive calls.
- Why further optimization is impossible: Further optimization is impossible because any preorder traversal algorithm must visit each node at least once, resulting in a time complexity of at least $O(N)$.

```cpp
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> result;
        if (root == nullptr) return result;
        
        stack<TreeNode*> s;
        s.push(root);
        
        while (!s.empty()) {
            TreeNode* node = s.top();
            s.pop();
            result.push_back(node->val);
            if (node->right) s.push(node->right);
            if (node->left) s.push(node->left);
        }
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, because each node is visited once.
> - **Space Complexity:** $O(N)$, because in the worst case, the stack can hold $N$ nodes.
> - **Optimality proof:** This is the optimal solution because it minimizes the overhead of visiting each node while still achieving the required preorder traversal.

---

### Alternative Approach

**Explanation:**
- Different perspective or technique: Another approach is to use Morris traversal, which temporarily changes the tree structure to avoid using a stack or recursion.
- Unique trade-offs: Morris traversal has the advantage of using $O(1)$ extra space (excluding the output), but it modifies the tree and has a more complex implementation.
- Scenarios where this approach might be preferred: This approach is preferred when memory is extremely limited, and the tree can be modified.
- Comparison with optimal approach: While the Morris traversal is more space-efficient, the iterative stack approach is generally easier to understand and implement.

```cpp
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> result;
        TreeNode* current = root;
        while (current) {
            if (current->left == nullptr) {
                result.push_back(current->val);
                current = current->right;
            } else {
                TreeNode* predecessor = current->left;
                while (predecessor->right && predecessor->right != current) {
                    predecessor = predecessor->right;
                }
                if (predecessor->right == nullptr) {
                    predecessor->right = current;
                    result.push_back(current->val);
                    current = current->left;
                } else {
                    predecessor->right = nullptr;
                    current = current->right;
                }
            }
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, because each node is visited once.
> - **Space Complexity:** $O(1)$, excluding the output, because no extra space is used.
> - **Trade-off analysis:** This approach is useful when memory is limited, but it has a more complex implementation and modifies the tree.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Preorder traversal, recursion, stack simulation, and Morris traversal.
- Problem-solving patterns identified: Using a stack to simulate recursion and modifying the tree structure for space efficiency.
- Optimization techniques learned: Avoiding recursive function call overhead and minimizing extra space usage.
- Similar problems to practice: Inorder and postorder traversal, and other tree traversal problems.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle the nullptr case, incorrectly pushing nodes onto the stack, and not properly resetting the Morris traversal pointers.
- Edge cases to watch for: Empty trees, trees with a single node, and trees with multiple levels.
- Performance pitfalls: Using recursive functions for large inputs and not considering space complexity.
- Testing considerations: Testing with various tree structures and edge cases to ensure correctness.