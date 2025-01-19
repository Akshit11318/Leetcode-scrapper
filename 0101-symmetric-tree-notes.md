## Symmetric Tree

**Problem Link:** [leetcode.com/problems/symmetric-tree/description](leetcode.com/problems/symmetric-tree/description)

**Problem Statement:**
- Input: The root of a binary tree.
- Constraints: The number of nodes in the tree is in the range [1, 1000].
- Expected Output: True if the tree is symmetric, False otherwise.
- Key Requirements: A tree is symmetric if it is the same when its left subtree is a mirror reflection of its right subtree.
- Edge Cases: Empty tree, single node tree, unbalanced trees.

**Example Test Cases:**
- Test Case 1:
  - Input: root = [1,2,2,3,4,4,3]
  - Output: true
  - Explanation: The binary tree [1,2,2,3,4,4,3] is symmetric.
- Test Case 2:
  - Input: root = [1,2,2,null,3,null,3]
  - Output: false
  - Explanation: The binary tree [1,2,2,null,3,null,3] is not symmetric.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to check if the left subtree is a mirror reflection of the right subtree by comparing their nodes level by level from left to right.
- We can achieve this by performing a level-order traversal (BFS) and checking if the nodes at corresponding positions from the left and right subtrees are equal.
- This approach comes to mind first because it directly addresses the symmetry condition without requiring additional insight into tree properties.

```cpp
// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (root == NULL) return true;
        
        std::queue<TreeNode*> leftQueue;
        std::queue<TreeNode*> rightQueue;
        
        leftQueue.push(root->left);
        rightQueue.push(root->right);
        
        while (!leftQueue.empty() && !rightQueue.empty()) {
            TreeNode* leftNode = leftQueue.front();
            TreeNode* rightNode = rightQueue.front();
            leftQueue.pop();
            rightQueue.pop();
            
            if (leftNode == NULL && rightNode == NULL) continue;
            if (leftNode == NULL || rightNode == NULL) return false;
            if (leftNode->val != rightNode->val) return false;
            
            leftQueue.push(leftNode->left);
            leftQueue.push(leftNode->right);
            rightQueue.push(rightNode->right);
            rightQueue.push(rightNode->left);
        }
        
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** O(n), where n is the number of nodes in the tree. This is because we visit each node once.
> - **Space Complexity:** O(n), because in the worst case, the queue will contain all nodes at the last level of the tree, which is roughly n/2 nodes, simplifying to O(n).
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node. The space complexity is also linear due to the potential size of the queue.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is recognizing that we can solve this problem recursively by comparing the left and right subtrees directly without needing to explicitly perform a level-order traversal.
- This approach is optimal because it minimizes the amount of code and directly addresses the problem statement without unnecessary overhead.
- We define a helper function that checks if two trees are mirror images of each other.

```cpp
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (root == NULL) return true;
        return isMirror(root->left, root->right);
    }
    
    bool isMirror(TreeNode* left, TreeNode* right) {
        if (left == NULL && right == NULL) return true;
        if (left == NULL || right == NULL) return false;
        return (left->val == right->val) && isMirror(left->right, right->left) && isMirror(left->left, right->right);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** O(n), where n is the number of nodes in the tree. Each node is visited once.
> - **Space Complexity:** O(h), where h is the height of the tree. This is due to the recursion stack. In the worst case (a skewed tree), this can be O(n), but for a balanced tree, it's O(log n).
> - **Optimality proof:** This solution is optimal because it directly checks for symmetry with minimal overhead, visiting each node exactly once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated include recursive problem-solving and the use of helper functions to simplify code.
- Problem-solving patterns identified include breaking down the problem into smaller sub-problems (checking if two trees are mirror images).
- Optimization techniques learned include minimizing unnecessary computations and using recursion efficiently.
- Similar problems to practice include other tree-related problems, such as checking if a tree is balanced or finding the lowest common ancestor.

**Mistakes to Avoid:**
- Common implementation errors include not handling the case where one of the subtrees is null but the other is not.
- Edge cases to watch for include empty trees and single-node trees.
- Performance pitfalls include using inefficient traversal methods or not optimizing the recursion.
- Testing considerations include ensuring that the solution works for both symmetric and asymmetric trees, as well as for trees of varying sizes and structures.