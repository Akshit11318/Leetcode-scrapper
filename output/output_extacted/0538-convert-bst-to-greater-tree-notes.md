## Convert BST to Greater Tree
**Problem Link:** https://leetcode.com/problems/convert-bst-to-greater-tree/description

**Problem Statement:**
- Input format and constraints: Given the root of a binary search tree (BST), convert it to a greater tree such that every key of the original BST is changed to the sum of all keys greater than the original key.
- Expected output format: The root of the modified BST.
- Key requirements and edge cases to consider: The input tree is a valid BST, and the tree may contain negative numbers.
- Example test cases with explanations:
    - Example 1: Input: `root = [4,1,6,0,2,5,7,null,null,null,null,null,null,8]`, Output: `[30,36,21,36,35,26,15,null,null,null,null,null,null,8]`.
    - Example 2: Input: `root = [0,null,1]`, Output: `[1,null,1]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Perform an in-order traversal of the BST, storing the node values in a vector. Then, for each node, calculate the sum of all node values greater than the current node's value and update the node's value accordingly.
- Step-by-step breakdown of the solution:
    1. Perform an in-order traversal of the BST and store the node values in a vector.
    2. For each node, find the sum of all node values greater than the current node's value.
    3. Update the node's value with the calculated sum.
- Why this approach comes to mind first: It's a straightforward approach that involves traversing the tree, storing node values, and then updating node values based on the stored values.

```cpp
class Solution {
public:
    TreeNode* convertBST(TreeNode* root) {
        vector<int> values;
        inOrderTraversal(root, values);
        for (int i = 0; i < values.size(); i++) {
            int sum = 0;
            for (int j = i + 1; j < values.size(); j++) {
                sum += values[j];
            }
            values[i] += sum;
        }
        updateNodeValues(root, values);
        return root;
    }
    
    void inOrderTraversal(TreeNode* node, vector<int>& values) {
        if (node == nullptr) return;
        inOrderTraversal(node->left, values);
        values.push_back(node->val);
        inOrderTraversal(node->right, values);
    }
    
    void updateNodeValues(TreeNode* node, vector<int>& values) {
        if (node == nullptr) return;
        updateNodeValues(node->left, values);
        for (int i = 0; i < values.size(); i++) {
            if (node->val == values[i]) {
                node->val = values[i];
                break;
            }
        }
        updateNodeValues(node->right, values);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of nodes in the BST. This is because for each node, we're performing another traversal to find the sum of greater node values.
> - **Space Complexity:** $O(n)$, as we're storing the node values in a vector.
> - **Why these complexities occur:** The brute force approach involves multiple traversals of the tree, resulting in high time complexity. The space complexity is due to storing node values in a vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can perform a reverse in-order traversal (right-root-left) and keep a running sum of node values. This way, we can update each node's value with the sum of all node values greater than the current node's value in a single pass.
- Detailed breakdown of the approach:
    1. Initialize a variable `runningSum` to store the sum of node values.
    2. Perform a reverse in-order traversal of the BST.
    3. For each node, update its value with the current `runningSum`.
    4. Add the node's original value to `runningSum`.
- Proof of optimality: This approach has a time complexity of $O(n)$, where $n$ is the number of nodes in the BST, as we're performing a single traversal of the tree. The space complexity is $O(h)$, where $h$ is the height of the tree, due to the recursive call stack.

```cpp
class Solution {
public:
    TreeNode* convertBST(TreeNode* root) {
        int runningSum = 0;
        reverseInOrderTraversal(root, runningSum);
        return root;
    }
    
    void reverseInOrderTraversal(TreeNode* node, int& runningSum) {
        if (node == nullptr) return;
        reverseInOrderTraversal(node->right, runningSum);
        runningSum += node->val;
        node->val = runningSum;
        reverseInOrderTraversal(node->left, runningSum);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the BST.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree.
> - **Optimality proof:** This approach is optimal as it involves a single traversal of the tree, resulting in the minimum possible time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Reverse in-order traversal, running sum.
- Problem-solving patterns identified: Using a running sum to update node values in a single pass.
- Optimization techniques learned: Reducing time complexity by avoiding multiple traversals.
- Similar problems to practice: Other problems involving tree traversals and node updates.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to update node values correctly, using incorrect traversal order.
- Edge cases to watch for: Handling empty trees, trees with negative numbers.
- Performance pitfalls: Using brute force approaches with high time complexity.
- Testing considerations: Testing with different tree structures, node values.