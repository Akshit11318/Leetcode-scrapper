## Trim a Binary Search Tree
**Problem Link:** https://leetcode.com/problems/trim-a-binary-search-tree/description

**Problem Statement:**
- Input: The root of a binary search tree and two integers, `low` and `high`, representing the range to trim the tree to.
- Constraints: The number of nodes in the tree is in the range `[1, 10^4]`, `1 <= Node.val <= 10^4`, and `1 <= low <= high <= 10^4`.
- Expected output: The root of the trimmed binary search tree.
- Key requirements and edge cases to consider:
  - The tree may be empty.
  - `low` and `high` may be equal.
  - The tree may contain nodes with values outside the range `[low, high]`.
- Example test cases with explanations:
  - Example 1: Given the tree `[1,0,2]`, `low = 1`, `high = 2`, the output should be `[1,null,2]`.
  - Example 2: Given the tree `[3,0,4,null,2,null,null,1]`, `low = 1`, `high = 3`, the output should be `[3,0,null,2,null,null,1]`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Start by traversing the tree and checking each node's value to see if it falls within the range `[low, high]`.
- Step-by-step breakdown of the solution:
  1. Traverse the tree using a depth-first search (DFS) or breadth-first search (BFS) algorithm.
  2. For each node, check if its value is within the range `[low, high]`.
  3. If the node's value is outside the range, remove it from the tree.
  4. Update the tree by reconnecting the child nodes of the removed node.
- Why this approach comes to mind first: It is a straightforward solution that directly addresses the problem statement.

```cpp
class Solution {
public:
    TreeNode* trimBST(TreeNode* root, int low, int high) {
        if (!root) return nullptr;
        if (root->val < low) return trimBST(root->right, low, high);
        if (root->val > high) return trimBST(root->left, low, high);
        root->left = trimBST(root->left, low, high);
        root->right = trimBST(root->right, low, high);
        return root;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, since we visit each node once.
> - **Space Complexity:** $O(n)$, due to the recursive call stack.
> - **Why these complexities occur:** The time complexity is linear because we visit each node once, and the space complexity is also linear due to the recursive call stack.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using a recursive approach that takes advantage of the properties of a binary search tree.
- Detailed breakdown of the approach:
  1. If the current node is `nullptr`, return `nullptr`.
  2. If the current node's value is less than `low`, recursively call the function on the right child.
  3. If the current node's value is greater than `high`, recursively call the function on the left child.
  4. Otherwise, recursively call the function on the left and right children.
- Proof of optimality: The time complexity is optimal because we visit each node once, and the space complexity is optimal due to the recursive call stack.

```cpp
class Solution {
public:
    TreeNode* trimBST(TreeNode* root, int low, int high) {
        if (!root) return nullptr;
        if (root->val < low) return trimBST(root->right, low, high);
        if (root->val > high) return trimBST(root->left, low, high);
        root->left = trimBST(root->left, low, high);
        root->right = trimBST(root->right, low, high);
        return root;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree, since we visit each node once.
> - **Space Complexity:** $O(n)$, due to the recursive call stack.
> - **Optimality proof:** The time complexity is optimal because we visit each node once, and the space complexity is optimal due to the recursive call stack.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive approach, binary search tree properties.
- Problem-solving patterns identified: Using recursive functions to solve tree-related problems.
- Optimization techniques learned: Taking advantage of the properties of a binary search tree to reduce the number of nodes visited.
- Similar problems to practice: Other tree-related problems, such as finding the minimum or maximum value in a binary search tree.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle the base case where the current node is `nullptr`.
- Edge cases to watch for: When the tree is empty or when `low` and `high` are equal.
- Performance pitfalls: Using an inefficient algorithm that visits each node multiple times.
- Testing considerations: Testing the function with different input scenarios, including edge cases.