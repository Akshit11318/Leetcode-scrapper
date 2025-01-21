## Construct String from Binary Tree

**Problem Link:** https://leetcode.com/problems/construct-string-from-binary-tree/description

**Problem Statement:**
- Input: The root node of a binary tree where each node has a unique string value.
- Constraints: The binary tree is not guaranteed to be balanced or complete. Each node has a unique string value.
- Expected Output: A string that represents the pre-order traversal of the binary tree with parentheses indicating the hierarchy of the tree.
- Key Requirements and Edge Cases:
  - Handle empty trees.
  - Ensure the correct ordering of nodes in the output string.
  - Use parentheses to denote the tree structure.
- Example Test Cases:
  - For a tree with a single node "root", the output should be "root".
  - For a tree where "root" has a left child "left" and a right child "right", the output should be "root(left(right))".

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Perform a pre-order traversal of the binary tree and append the node values to a string, using parentheses to denote the tree hierarchy.
- Step-by-step breakdown:
  1. Start at the root node.
  2. Append the current node's value to the result string.
  3. If the current node has a left child, recursively traverse the left subtree and append the result to the current string, enclosed in parentheses.
  4. If the current node has a right child, recursively traverse the right subtree and append the result to the current string, enclosed in parentheses.
- Why this approach comes to mind first: It directly follows the definition of a pre-order traversal and the requirement to include the tree hierarchy in the output string.

```cpp
class Solution {
public:
    string tree2str(TreeNode* root) {
        if (!root) return "";
        string result = "";
        result += root->val;
        if (root->left) {
            result += "(" + tree2str(root->left) + ")";
        }
        if (root->right) {
            if (!root->left) result += "()";
            result += "(" + tree2str(root->right) + ")";
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree, since we visit each node exactly once.
> - **Space Complexity:** $O(H)$, where $H$ is the height of the tree, due to the recursive call stack. In the worst case, the tree is skewed, and $H = N$.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each node. The space complexity is dependent on the height of the recursive call stack, which is determined by the tree's height.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The problem can be solved using a recursive approach similar to the brute force, but we need to handle the case where a node has only a right child to ensure the correct output format.
- Detailed breakdown: The solution provided in the brute force section is already optimal for this problem, as it correctly handles all cases and has the best possible time and space complexity given the constraints of the problem.
- Proof of optimality: Since we must visit each node at least once to construct the string and the recursive approach ensures that we do not perform any redundant operations, the time complexity of $O(N)$ is optimal. Similarly, the space complexity of $O(H)$ is optimal because it is inherent to the recursive nature of the solution.

```cpp
class Solution {
public:
    string tree2str(TreeNode* root) {
        if (!root) return "";
        string result = "";
        result += root->val;
        if (root->left) {
            result += "(" + tree2str(root->left) + ")";
        }
        if (root->right) {
            if (!root->left) result += "()";
            result += "(" + tree2str(root->right) + ")";
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the tree.
> - **Space Complexity:** $O(H)$, where $H$ is the height of the tree.
> - **Optimality proof:** The solution is optimal because it visits each node exactly once and uses the minimum necessary space to store the recursive call stack.

---

### Final Notes

**Learning Points:**
- Recursion is a powerful tool for solving tree-based problems.
- Handling edge cases, such as an empty tree or a node with only one child, is crucial for ensuring the correctness of the solution.
- Understanding the time and space complexity of a solution helps in determining its optimality.

**Mistakes to Avoid:**
- Not handling the case where a node has only a right child correctly.
- Forgetting to include parentheses around the subtree strings.
- Not checking for an empty tree as a base case for the recursion.