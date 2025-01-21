## Binary Tree Tilt
**Problem Link:** https://leetcode.com/problems/binary-tree-tilt/description

**Problem Statement:**
- Input format and constraints: The input is a binary tree where each node has a unique value. The tree is represented as a `TreeNode` object, where each node has a `val`, `left`, and `right` attribute. The constraints are that the tree will not be empty, and the number of nodes in the tree will not exceed 100.
- Expected output format: The output is the sum of the absolute differences between the sum of the values of the left subtree and the sum of the values of the right subtree for each node in the tree.
- Key requirements and edge cases to consider: The key requirement is to calculate the tilt of each node in the tree and return the sum of these tilts. Edge cases include an empty tree (not applicable in this case since the tree will not be empty), a tree with only one node, and a tree with multiple nodes.
- Example test cases with explanations:
    - Example 1:
        - Input: root = [1,2,3]
        - Output: 1
        - Explanation: The tilt of the node with value 1 is |0-0| = 0. The tilt of the node with value 2 is |0-0| = 0. The tilt of the node with value 3 is |0-0| = 0. Therefore, the sum of the tilts is 0 + 0 + 0 = 0.
    - Example 2:
        - Input: root = [4,2,9,3,5,null,7]
        - Output: 15
        - Explanation: The tilt of the node with value 4 is |(2 + 3 + 5) - (9 + 7)| = |10 - 16| = 6. The tilt of the node with value 2 is |3 - 0| = 3. The tilt of the node with value 9 is |0 - 7| = 7. Therefore, the sum of the tilts is 6 + 3 + 7 = 16.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The initial thought process is to calculate the sum of the values of the left subtree and the sum of the values of the right subtree for each node in the tree. Then, calculate the absolute difference between these two sums for each node. Finally, return the sum of these absolute differences.
- Step-by-step breakdown of the solution:
    1. Define a helper function to calculate the sum of the values of a subtree.
    2. For each node in the tree, calculate the sum of the values of the left subtree and the sum of the values of the right subtree using the helper function.
    3. Calculate the absolute difference between the two sums for each node.
    4. Return the sum of these absolute differences.
- Why this approach comes to mind first: This approach comes to mind first because it directly addresses the problem statement. It calculates the tilt of each node in the tree and returns the sum of these tilts.

```cpp
class Solution {
public:
    int findTilt(TreeNode* root) {
        int totalTilt = 0;
        calculateTilt(root, totalTilt);
        return totalTilt;
    }
    
    int calculateSum(TreeNode* node) {
        if (node == nullptr) {
            return 0;
        }
        return node->val + calculateSum(node->left) + calculateSum(node->right);
    }
    
    void calculateTilt(TreeNode* node, int& totalTilt) {
        if (node == nullptr) {
            return;
        }
        int leftSum = calculateSum(node->left);
        int rightSum = calculateSum(node->right);
        totalTilt += abs(leftSum - rightSum);
        calculateTilt(node->left, totalTilt);
        calculateTilt(node->right, totalTilt);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of nodes in the tree. This is because for each node, we calculate the sum of the values of the left subtree and the sum of the values of the right subtree, which takes $O(n)$ time in the worst case.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree. This is because of the recursive call stack.
> - **Why these complexities occur:** The time complexity occurs because we calculate the sum of the values of the left subtree and the sum of the values of the right subtree for each node in the tree, which takes $O(n)$ time in the worst case. The space complexity occurs because of the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to calculate the sum of the values of the left subtree and the sum of the values of the right subtree only once for each node. We can do this by modifying the recursive function to return the sum of the values of the subtree and the tilt of the subtree.
- Detailed breakdown of the approach:
    1. Define a helper function to calculate the sum of the values of a subtree and the tilt of the subtree.
    2. For each node in the tree, calculate the sum of the values of the left subtree and the sum of the values of the right subtree using the helper function.
    3. Calculate the tilt of the current node by taking the absolute difference between the two sums.
    4. Return the sum of the values of the current node and the sums of the values of the left subtree and the right subtree, and the tilt of the current node and the tilts of the left subtree and the right subtree.
- Proof of optimality: This approach is optimal because it only calculates the sum of the values of the left subtree and the sum of the values of the right subtree once for each node, resulting in a time complexity of $O(n)$.

```cpp
class Solution {
public:
    int findTilt(TreeNode* root) {
        int totalTilt = 0;
        calculateSumAndTilt(root, totalTilt);
        return totalTilt;
    }
    
    int calculateSumAndTilt(TreeNode* node, int& totalTilt) {
        if (node == nullptr) {
            return 0;
        }
        int leftSum = calculateSumAndTilt(node->left, totalTilt);
        int rightSum = calculateSumAndTilt(node->right, totalTilt);
        totalTilt += abs(leftSum - rightSum);
        return node->val + leftSum + rightSum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. This is because we only calculate the sum of the values of the left subtree and the sum of the values of the right subtree once for each node.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree. This is because of the recursive call stack.
> - **Optimality proof:** The time complexity is optimal because we only calculate the sum of the values of the left subtree and the sum of the values of the right subtree once for each node, resulting in a time complexity of $O(n)$. The space complexity is optimal because we only use a recursive call stack of height $h$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The key algorithmic concepts demonstrated in this problem are recursive functions, tree traversal, and dynamic programming.
- Problem-solving patterns identified: The problem-solving pattern identified in this problem is to break down the problem into smaller sub-problems and solve each sub-problem only once.
- Optimization techniques learned: The optimization technique learned in this problem is to avoid redundant calculations by storing the results of sub-problems in a cache or by modifying the recursive function to return the results of sub-problems.
- Similar problems to practice: Similar problems to practice include calculating the sum of the values of a subtree, calculating the tilt of a subtree, and calculating the diameter of a tree.

**Mistakes to Avoid:**
- Common implementation errors: Common implementation errors include not handling the base case of the recursive function correctly, not updating the cache correctly, and not avoiding redundant calculations.
- Edge cases to watch for: Edge cases to watch for include an empty tree, a tree with only one node, and a tree with multiple nodes.
- Performance pitfalls: Performance pitfalls include redundant calculations, not using a cache to store the results of sub-problems, and not optimizing the recursive function.
- Testing considerations: Testing considerations include testing the function with different types of trees, including an empty tree, a tree with only one node, and a tree with multiple nodes.