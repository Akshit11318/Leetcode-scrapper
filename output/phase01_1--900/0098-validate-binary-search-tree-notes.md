## Validate Binary Search Tree
**Problem Link:** https://leetcode.com/problems/validate-binary-search-tree/description

**Problem Statement:**
- Input format and constraints: Given the root of a binary tree, determine if it is a valid binary search tree (BST).
- Expected output format: Return true if the binary tree is a valid BST, and false otherwise.
- Key requirements and edge cases to consider: 
  - All values in the left subtree must be less than the current node's value.
  - All values in the right subtree must be greater than the current node's value.
  - Both the left and right subtrees must also be valid BSTs.
- Example test cases with explanations:
  - Example 1: Input: root = [2,1,3], Output: true
  - Example 2: Input: root = [5,1,4,null,null,3,6], Output: false

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To validate a binary search tree, we can perform an in-order traversal and check if the resulting sequence is sorted in ascending order.
- Step-by-step breakdown of the solution:
  1. Perform an in-order traversal of the binary tree.
  2. Store the node values in a vector during the traversal.
  3. Check if the vector is sorted in ascending order.
- Why this approach comes to mind first: The definition of a BST implies that an in-order traversal should yield a sorted sequence.

```cpp
class Solution {
public:
    vector<int> inOrder;
    bool isValidBST(TreeNode* root) {
        inOrder.clear();
        traverse(root);
        for (int i = 0; i < inOrder.size() - 1; i++) {
            if (inOrder[i] >= inOrder[i + 1]) {
                return false;
            }
        }
        return true;
    }
    
    void traverse(TreeNode* node) {
        if (node == nullptr) return;
        traverse(node->left);
        inOrder.push_back(node->val);
        traverse(node->right);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. We visit each node once during the traversal and then potentially once more to check the sorted sequence.
> - **Space Complexity:** $O(n)$, for storing the in-order traversal sequence.
> - **Why these complexities occur:** The in-order traversal visits each node exactly once, and then we perform a linear scan of the resulting sequence to check for sorted order.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of storing the entire in-order traversal sequence, we can keep track of the previous node's value during the traversal and check if the current node's value is greater than the previous one.
- Detailed breakdown of the approach:
  1. Perform an in-order traversal of the binary tree.
  2. Keep track of the previous node's value during the traversal.
  3. Check if the current node's value is greater than the previous one.
- Proof of optimality: This approach still visits each node once but avoids the extra space needed to store the entire sequence, making it more efficient in terms of space complexity.

```cpp
class Solution {
public:
    long long prev = LLONG_MIN;
    bool isValidBST(TreeNode* root) {
        return inOrder(root);
    }
    
    bool inOrder(TreeNode* node) {
        if (node == nullptr) return true;
        if (!inOrder(node->left)) return false;
        if (node->val <= prev) return false;
        prev = node->val;
        return inOrder(node->right);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. We visit each node once during the traversal.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree, due to the recursive call stack. In the worst case (a skewed tree), this becomes $O(n)$.
> - **Optimality proof:** This is the optimal solution because we minimize both time and space complexity by only keeping track of the necessary information (the previous node's value) during the traversal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: In-order traversal of a binary tree, validation of a BST.
- Problem-solving patterns identified: Using a previous node's value to check for sorted order during traversal.
- Optimization techniques learned: Reducing space complexity by only keeping necessary information.
- Similar problems to practice: Other tree validation problems, such as validating a binary tree's height or checking for symmetry.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle the case where the tree is empty (root is nullptr), or not correctly updating the previous node's value during traversal.
- Edge cases to watch for: Trees with duplicate values, trees with a single node, or empty trees.
- Performance pitfalls: Using unnecessary extra space to store the entire traversal sequence.
- Testing considerations: Thoroughly testing the function with various tree configurations, including valid and invalid BSTs, to ensure correctness.