## Univalued Binary Tree
**Problem Link:** https://leetcode.com/problems/univalued-binary-tree/description

**Problem Statement:**
- Input format: The root of a binary tree.
- Constraints: The number of nodes in the tree is in the range [1, 100].
- Expected output format: A boolean indicating whether the binary tree is univalued.
- Key requirements and edge cases to consider: 
  - A binary tree is univalued if every node has the same value.
  - An empty tree is not considered univalued.
- Example test cases with explanations:
  - Example 1: 
    - Input: root = [1,1,1,1,1,null,1]
    - Output: true
    - Explanation: All nodes have the same value.
  - Example 2: 
    - Input: root = [2,2,2,5,2]
    - Output: false
    - Explanation: Node with value 5 is different from the others.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To determine if a binary tree is univalued, we can compare the value of each node with the value of the root node.
- Step-by-step breakdown of the solution:
  1. Start at the root node.
  2. Use a recursive or iterative approach to traverse the tree.
  3. For each node, check if its value matches the value of the root node.
  4. If any node has a different value, immediately return false.
  5. If the traversal completes without finding any nodes with different values, return true.

```cpp
class Solution {
public:
    bool isUnivalTree(TreeNode* root) {
        // Base case: An empty tree is not univalued.
        if (!root) return false;

        // Compare each node's value with the root's value.
        return traverse(root, root->val);
    }

    bool traverse(TreeNode* node, int val) {
        // Base case: If the node is null, it doesn't affect the result.
        if (!node) return true;

        // If the node's value doesn't match the target value, return false.
        if (node->val != val) return false;

        // Recursively check the left and right subtrees.
        return traverse(node->left, val) && traverse(node->right, val);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, since we visit each node once.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree, due to the recursive call stack. In the worst case (a skewed tree), $h = n$, but for a balanced tree, $h = \log n$.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node. The space complexity depends on the maximum depth of the recursive call stack, which varies with the tree's structure.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal for this problem since we must check every node to ensure the tree is univalued.
- Detailed breakdown of the approach: The same approach as the brute force is used, as it is already optimal.
- Proof of optimality: Since we must visit every node to verify if the tree is univalued, any algorithm must have at least a time complexity of $O(n)$, making the brute force approach optimal in terms of time complexity.

```cpp
class Solution {
public:
    bool isUnivalTree(TreeNode* root) {
        // Base case: An empty tree is not univalued.
        if (!root) return false;

        // Compare each node's value with the root's value.
        return traverse(root, root->val);
    }

    bool traverse(TreeNode* node, int val) {
        // Base case: If the node is null, it doesn't affect the result.
        if (!node) return true;

        // If the node's value doesn't match the target value, return false.
        if (node->val != val) return false;

        // Recursively check the left and right subtrees.
        return traverse(node->left, val) && traverse(node->right, val);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, as we visit each node once.
> - **Space Complexity:** $O(h)$, where $h$ is the height of the tree, due to the recursive call stack.
> - **Optimality proof:** This solution is optimal because it checks every node exactly once, which is necessary to solve the problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Tree traversal (recursive and potentially iterative), comparison of node values.
- Problem-solving patterns identified: Ensuring all elements in a data structure (in this case, a tree) meet a certain condition.
- Optimization techniques learned: Recognizing when a brute force approach is already optimal due to the nature of the problem.
- Similar problems to practice: Other tree-related problems, such as checking for symmetry, finding paths, or calculating sums.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle the base case (empty tree or null node), incorrect recursive function calls.
- Edge cases to watch for: Empty trees, trees with a single node, highly unbalanced trees.
- Performance pitfalls: Using an unnecessarily complex algorithm when a simpler one will suffice.
- Testing considerations: Ensure to test with various tree structures (balanced, unbalanced, single-node, empty) and values.