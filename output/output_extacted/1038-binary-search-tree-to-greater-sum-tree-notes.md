## Binary Search Tree to Greater Sum Tree

**Problem Link:** https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description

**Problem Statement:**
- Input: The root of a binary search tree (`BST`).
- Output: The root of the transformed `BST`.
- Key requirements: The transformed tree should have the same structure as the original, but each node's value should be the sum of all values greater than it in the original tree.
- Example test cases:
  - Input: `[4,1,6,0,2,5,7,null,null,null,null,null,null,8]`
  - Output: `[30,36,21,36,35,26,15,null,null,null,null,null,null,8]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Traverse the tree to calculate the sum of all nodes greater than each node, and then update the node's value with this sum.
- Step-by-step breakdown:
  1. Perform an in-order traversal to get all node values in ascending order.
  2. For each node, calculate the sum of all values greater than it by iterating through the sorted list of node values.
  3. Update the node's value with the calculated sum.

```cpp
class Solution {
public:
    TreeNode* bstToGst(TreeNode* root) {
        vector<int> values;
        // Perform in-order traversal to get node values in ascending order
        inOrderTraversal(root, values);
        
        // Calculate the sum of all values greater than each node
        for (int i = 0; i < values.size(); ++i) {
            int sum = 0;
            for (int j = i + 1; j < values.size(); ++j) {
                sum += values[j];
            }
            // Update the node's value with the calculated sum
            updateNode(root, values[i], sum);
        }
        
        return root;
    }
    
    void inOrderTraversal(TreeNode* node, vector<int>& values) {
        if (!node) return;
        inOrderTraversal(node->left, values);
        values.push_back(node->val);
        inOrderTraversal(node->right, values);
    }
    
    void updateNode(TreeNode* node, int oldValue, int newValue) {
        if (!node) return;
        if (node->val == oldValue) node->val = newValue;
        updateNode(node->left, oldValue, newValue);
        updateNode(node->right, oldValue, newValue);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of nodes in the tree. The outer loop iterates through each node, and the inner loop calculates the sum of all values greater than each node.
> - **Space Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. We store all node values in a vector.
> - **Why these complexities occur:** The brute force approach has a high time complexity due to the nested loops, and the space complexity is moderate due to the storage of node values.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Perform a reverse in-order traversal (right-root-left) to calculate the sum of all values greater than each node in a single pass.
- Detailed breakdown:
  1. Initialize a variable `sum` to store the sum of all values greater than the current node.
  2. Perform a reverse in-order traversal (right-root-left) to update each node's value with the sum of all values greater than it.

```cpp
class Solution {
public:
    TreeNode* bstToGst(TreeNode* root) {
        int sum = 0;
        reverseInOrderTraversal(root, sum);
        return root;
    }
    
    void reverseInOrderTraversal(TreeNode* node, int& sum) {
        if (!node) return;
        reverseInOrderTraversal(node->right, sum);
        sum += node->val;
        node->val = sum;
        reverseInOrderTraversal(node->left, sum);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. We perform a single pass through the tree.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree. This is the maximum depth of the recursion call stack.
> - **Optimality proof:** This approach is optimal because we only visit each node once, and we calculate the sum of all values greater than each node in a single pass.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Reverse in-order traversal, single-pass calculation of sums.
- Problem-solving patterns identified: Using a recursive approach to traverse the tree and update node values.
- Optimization techniques learned: Reducing the number of passes through the tree to improve time complexity.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to update the node's value with the calculated sum, or using the wrong traversal order.
- Edge cases to watch for: Handling empty trees or trees with a single node.
- Performance pitfalls: Using a brute force approach with high time complexity.
- Testing considerations: Verifying the correctness of the transformed tree by checking the node values.