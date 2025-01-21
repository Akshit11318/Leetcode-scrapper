## Binary Tree Postorder Traversal
**Problem Link:** https://leetcode.com/problems/binary-tree-postorder-traversal/description

**Problem Statement:**
- Input format: The input is the root of a binary tree where each node has a unique value.
- Constraints: The number of nodes in the tree is in the range `[1, 100]`.
- Expected output format: A list of integers representing the postorder traversal of the binary tree.
- Key requirements and edge cases to consider: The input tree may be empty, or it may be a tree with only one node. The tree may also be skewed to the left or right.
- Example test cases with explanations:
  - Example 1: 
    - Input: `root = [1,null,2,3]`
    - Output: `[3,2,1]`
  - Example 2: 
    - Input: `root = [1,2,3,4,5,6,7]`
    - Output: `[4,5,2,6,7,3,1]`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Perform a recursive depth-first search (DFS) on the binary tree. For each node, first visit the left subtree, then the right subtree, and finally the current node.
- Step-by-step breakdown of the solution:
  1. Define a recursive function that takes a node as input.
  2. If the input node is `NULL`, return immediately.
  3. Recursively call the function on the left child of the node.
  4. Recursively call the function on the right child of the node.
  5. Append the value of the current node to the result list.
- Why this approach comes to mind first: This approach is straightforward and directly follows the definition of a postorder traversal.

```cpp
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> result;
        postorderTraversalHelper(root, result);
        return result;
    }
    
    void postorderTraversalHelper(TreeNode* node, vector<int>& result) {
        if (node == NULL) {
            return;
        }
        
        postorderTraversalHelper(node->left, result);
        postorderTraversalHelper(node->right, result);
        result.push_back(node->val);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the binary tree. This is because each node is visited exactly once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the binary tree. This is because in the worst case, the recursive call stack can grow up to the height of the tree, which is $n$ for a skewed tree.
> - **Why these complexities occur:** The time complexity is linear because each node is visited once. The space complexity is linear because of the recursive call stack.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is to use an iterative approach with a stack to mimic the recursive call stack.
- Detailed breakdown of the approach:
  1. Initialize an empty stack and push the root node onto it.
  2. Initialize an empty list to store the postorder traversal result.
  3. While the stack is not empty:
    - Pop a node from the stack.
    - Push the node's value onto the result list.
    - Push the node's right child onto the stack (if it exists).
    - Push the node's left child onto the stack (if it exists).
  4. Return the result list.
- Proof of optimality: This approach is optimal because it visits each node exactly once and uses a constant amount of extra space (excluding the space needed for the output).
- Why further optimization is impossible: This approach has a time complexity of $O(n)$ and a space complexity of $O(n)$, which is the best possible for this problem.

```cpp
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> result;
        if (root == NULL) {
            return result;
        }
        
        stack<TreeNode*> s;
        s.push(root);
        stack<int> output;
        
        while (!s.empty()) {
            TreeNode* node = s.top();
            s.pop();
            output.push(node->val);
            
            if (node->left != NULL) {
                s.push(node->left);
            }
            if (node->right != NULL) {
                s.push(node->right);
            }
        }
        
        while (!output.empty()) {
            result.push_back(output.top());
            output.pop();
        }
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the binary tree. This is because each node is visited exactly once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the binary tree. This is because in the worst case, the stack can grow up to the height of the tree, which is $n$ for a skewed tree.
> - **Optimality proof:** The time complexity is linear because each node is visited once. The space complexity is linear because of the stack.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive depth-first search, iterative stack-based approach.
- Problem-solving patterns identified: Using a stack to mimic recursive call stack.
- Optimization techniques learned: Avoiding recursive function calls by using an iterative approach.
- Similar problems to practice: Inorder and preorder traversal of a binary tree.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle the case where the input tree is empty.
- Edge cases to watch for: Skewed trees, trees with only one node.
- Performance pitfalls: Using recursive function calls for large inputs.
- Testing considerations: Test the solution with different types of input trees, including skewed trees and trees with only one node.