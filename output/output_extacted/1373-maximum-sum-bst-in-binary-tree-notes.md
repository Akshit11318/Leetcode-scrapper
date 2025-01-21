## Maximum Sum BST in Binary Tree

**Problem Link:** https://leetcode.com/problems/maximum-sum-bST-in-binary-tree/description

**Problem Statement:**
- Input: The root of a binary tree, where each node has an integer value.
- Output: The maximum sum of the values in a valid Binary Search Tree (BST) within the given tree.
- Key requirements:
  - A valid BST is a binary tree where for every node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node.
  - The sum of a BST is the sum of all its node values.
- Edge cases:
  - The input tree could be empty (i.e., the root is NULL).
  - The tree could contain only one node.
- Example test cases:
  - Given a tree with nodes having values 1, 4, 3, 2, 4, 2, 5, where the nodes form a valid BST, the maximum sum should be the sum of all these nodes.
  - Given a tree with nodes that do not form a valid BST, the maximum sum should still be the sum of the largest valid BST within the tree.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible subtree to see if it's a valid BST and calculate its sum.
- Step-by-step breakdown:
  1. Generate all possible subtrees of the given tree.
  2. For each subtree, check if it's a valid BST by verifying the BST property for every node.
  3. If a subtree is a valid BST, calculate the sum of its node values.
  4. Keep track of the maximum sum found among all valid BSTs.

```cpp
class Solution {
public:
    int maxSumBST(TreeNode* root) {
        int maxSum = 0;
        // Function to check if a tree is a BST and return its sum
        function<int(TreeNode*)> checkBST = [&](TreeNode* node) {
            if (!node) return 0;
            int sum = node->val;
            bool isBST = true;
            // Check if left and right subtrees are within valid ranges
            auto checkRange = [&](TreeNode* node, int minVal, int maxVal) {
                if (!node) return true;
                if (node->val <= minVal || node->val >= maxVal) return false;
                return checkRange(node->left, minVal, node->val) && checkRange(node->right, node->val, maxVal);
            };
            if (node->left && node->left->val >= node->val) isBST = false;
            if (node->right && node->right->val <= node->val) isBST = false;
            if (!isBST) return 0; // Not a BST, return 0
            // Recursively check and sum left and right subtrees
            sum += checkBST(node->left);
            sum += checkBST(node->right);
            maxSum = max(maxSum, sum); // Update maxSum if necessary
            return sum;
        };
        checkBST(root);
        return maxSum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N^2)$ where $N$ is the number of nodes in the tree. This is because in the worst case, we might end up checking every node against every other node to verify the BST property.
> - **Space Complexity:** $O(N)$ due to the recursive call stack in the worst case (when the tree is skewed).
> - **Why these complexities occur:** The brute force approach involves generating all possible subtrees and checking each one, leading to exponential time complexity. The space complexity is due to the recursive function calls.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Utilize a post-order traversal to calculate the sum of each subtree and verify if it's a BST in a single pass.
- Detailed breakdown:
  1. Perform a post-order traversal (left, right, root) of the tree.
  2. For each node, calculate the sum of its subtree and verify the BST property by checking the minimum and maximum values in its left and right subtrees.
  3. Use a struct or class to return multiple values from the recursive function: the sum of the subtree, the minimum value in the subtree, and the maximum value in the subtree.
  4. Keep track of the maximum sum found among all valid BSTs.

```cpp
class Solution {
public:
    int maxSumBST(TreeNode* root) {
        int maxSum = 0;
        function<tuple<int, int, int, bool>(TreeNode*)> postOrder = [&](TreeNode* node) {
            if (!node) return {0, INT_MAX, INT_MIN, true};
            auto [leftSum, leftMin, leftMax, leftIsBST] = postOrder(node->left);
            auto [rightSum, rightMin, rightMax, rightIsBST] = postOrder(node->right);
            int sum = leftSum + rightSum + node->val;
            bool isBST = leftIsBST && rightIsBST && node->val > leftMax && node->val < rightMin;
            if (isBST) maxSum = max(maxSum, sum);
            return {sum, min(node->val, leftMin), max(node->val, rightMax), isBST};
        };
        postOrder(root);
        return maxSum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$ where $N$ is the number of nodes in the tree. This is because we visit each node once during the post-order traversal.
> - **Space Complexity:** $O(N)$ due to the recursive call stack in the worst case (when the tree is skewed).
> - **Optimality proof:** This approach is optimal because it visits each node exactly once, minimizing the time complexity. The use of a post-order traversal allows for the calculation of subtree sums and verification of the BST property in a single pass, making it the most efficient approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Post-order traversal, verification of BST property, and calculation of subtree sums.
- Problem-solving patterns identified: Using recursive functions to solve tree-related problems, optimizing brute force approaches by reducing unnecessary computations.
- Optimization techniques learned: Utilizing specific traversal orders to minimize computations, using data structures to return multiple values from recursive functions.
- Similar problems to practice: Other tree-related problems that involve traversals and property verifications, such as finding the lowest common ancestor in a tree.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly implementing the traversal order, failing to update the maximum sum correctly.
- Edge cases to watch for: Empty trees, trees with a single node, skewed trees.
- Performance pitfalls: Using brute force approaches for large inputs, failing to optimize recursive functions.
- Testing considerations: Thoroughly testing the function with various tree structures and edge cases to ensure correctness and efficiency.