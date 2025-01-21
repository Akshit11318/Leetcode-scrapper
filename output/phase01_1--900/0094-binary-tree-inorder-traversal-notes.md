## Binary Tree Inorder Traversal
**Problem Link:** https://leetcode.com/problems/binary-tree-inorder-traversal/description

**Problem Statement:**
- Input: The root of a binary tree.
- Output: A list of values in the inorder traversal of the binary tree.
- Key requirements: The solution should handle all possible binary tree structures, including empty trees and trees with only one node.
- Example test cases:
  - Input: root = [4,2,5,1,3]
    - Output: [1,2,3,4,5]
  - Input: root = [1]
    - Output: [1]

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to visit each node in the tree and perform the inorder traversal recursively.
- However, the brute force approach can be considered as a simple recursive solution without any optimization.

```cpp
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        if (root == nullptr) return result;
        
        result = inorderTraversal(root->left);
        result.push_back(root->val);
        vector<int> right = inorderTraversal(root->right);
        result.insert(result.end(), right.begin(), right.end());
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the binary tree. This is because each node is visited once.
> - **Space Complexity:** $O(n)$, due to the recursive call stack and the storage of the result vector.
> - **Why these complexities occur:** The time complexity is $O(n)$ because we visit each node once. The space complexity is $O(n)$ due to the recursive call stack and the result vector.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal solution is to use an iterative approach with a stack to store nodes to be visited.
- We start by pushing the root node onto the stack, then we enter a loop that continues until the stack is empty.
- Inside the loop, we pop the top node from the stack, add its value to the result vector, and push its right child onto the stack if it exists.
- Before popping the node, we check if it has a left child. If it does, we push the node back onto the stack and push its left child onto the stack. This way, we ensure that we visit the left subtree before visiting the node itself.
- This approach avoids the recursive call stack and uses a manual stack to store nodes to be visited.

```cpp
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        stack<TreeNode*> s;
        TreeNode* curr = root;
        
        while (curr != nullptr || !s.empty()) {
            while (curr != nullptr) {
                s.push(curr);
                curr = curr->left;
            }
            curr = s.top();
            s.pop();
            result.push_back(curr->val);
            curr = curr->right;
        }
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the binary tree.
> - **Space Complexity:** $O(n)$, due to the stack used to store nodes to be visited.
> - **Optimality proof:** This is the optimal solution because we visit each node exactly once, and we use a stack to store nodes to be visited, which has a space complexity of $O(n)$.

---

### Alternative Approach

**Explanation:**
- Another approach is to use a Morris traversal, which is an in-order traversal that doesn't use a stack or recursion.
- The basic idea is to create a temporary link between the current node and its predecessor (the node that would be visited before the current node in an in-order traversal).
- We start by setting the current node to the root of the tree.
- Then, we enter a loop that continues until the current node is null.
- Inside the loop, we check if the current node has a left child. If it does, we find the predecessor of the current node and check if the predecessor's right child is null. If it is, we set the predecessor's right child to the current node and move the current node to its left child. If the predecessor's right child is not null, we reset the predecessor's right child to null, add the current node's value to the result vector, and move the current node to its right child.
- If the current node does not have a left child, we add its value to the result vector and move the current node to its right child.

```cpp
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        TreeNode* curr = root;
        
        while (curr != nullptr) {
            if (curr->left == nullptr) {
                result.push_back(curr->val);
                curr = curr->right;
            } else {
                TreeNode* predecessor = curr->left;
                while (predecessor->right != nullptr && predecessor->right != curr) {
                    predecessor = predecessor->right;
                }
                
                if (predecessor->right == nullptr) {
                    predecessor->right = curr;
                    curr = curr->left;
                } else {
                    predecessor->right = nullptr;
                    result.push_back(curr->val);
                    curr = curr->right;
                }
            }
        }
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the binary tree.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the current node and its predecessor.
> - **Trade-off analysis:** This approach has a better space complexity than the optimal approach, but it is more complex and harder to understand.

---

### Final Notes

**Learning Points:**
- The importance of understanding the problem statement and identifying the key requirements.
- The use of recursive and iterative approaches to solve problems.
- The trade-offs between time and space complexity.
- The use of stacks and temporary links to solve problems.

**Mistakes to Avoid:**
- Not checking for edge cases, such as an empty tree or a tree with only one node.
- Not considering the time and space complexity of the solution.
- Not using the most efficient data structures and algorithms.
- Not testing the solution thoroughly.